# Source: https://docs.maptiler.com/sdk-js/examples/helper-screenshot-feedback/

# 

This tutorial addresses the common issue of blank images (missing maps) appearing in screenshots instead of a beautiful map displays when using various reporting and feedback tools.

If you're utilizing reporting platforms such as [Usersnap](https://usersnap.com), [Ybug](https://ybug.io), [Feedbucket](https://www.feedbucket.app/), [Featurebase](https://www.featurebase.app/), [BugHerd](https://bugherd.com), [Marker.io](https://marker.io/), or similar services, you might have encountered this problem: ***I cannot see a map in a screenshot produced by these services. What should I do to fix this?***. We'll explore various solutions and introduce an alternative using the [MapTiler Screenshot helper](/sdk-js/api/helpers/#screenshot).

> [!NOTE]
> For conventional screenshot needs, MapTiler SDK has a dedicated [screenshot function](/sdk-js/api/helpers/#screenshot). This feature generates a PNG binary blob that you can manipulate or send to the endpoint of your choice.
>
> Learn more about this feature [here](/sdk-js/api/helpers/#screenshot).

## How do report services create screenshots?

These services basically use one of these two ways:

* The built-in/permission-heavy way
* The stealth/no-user-permission-needed way

### The built-in/permission-heavy way

The built-in way is essentially the window-sharing popup that appears when users need to share their screen or join a video call (Zoom, Google Chat, etc.). It is very reliable and ensures viewers see exactly what's on your browser. 
However, this approach has drawbacks. The permission popup can be disruptive and often confusing. Depending on your browser, you might need to navigate through additional selections - choosing between your entire window (especially with multiple screens), specific browser windows, or individual tabs. Moreover, this method might raise privacy concerns among users.

### The stealth/no-user-permission-needed way

Most services, including Usersnap, prefer the stealth way, though it can be less reliable. The process consists in  
“redrawing” the webpage's UI within an (offscreen) canvas, implementing custom code, adjusting elements with CSS, incorporating images, and aiming to replicate the user's view accurately. While this crafty approach can encounter various challenges, Usersnap manages it quite effectively, making it their default choice. However, this approach cannot work in some specialized cases, and high-performance rendering falls right into it! 

## Canvas, where are your pixels?

As we mentioned before, the stealth approach has limitations when redrawing elements on the canvas, which explains the occurrence of "empty pixels" and the absence of map visualization in screenshots. Let's explain why this happens.

[MapTiler SDK](https://www.maptiler.com/sdk-javascript/) for JavaScript/TypeScript uses Maplibre GL JS and the WebGL API under the hood to provide a great-looking and high-performance rendering.

To simplify the technical complexities, we can explain it this way: JavaScript operations are executed on the primary processing unit (CPU), while WebGL rendering tasks are handled by the Graphics Processing Unit (GPU) - a specialized processor with dedicated memory and computational capabilities specifically designed for processing 2D and 3D graphics data.

You may be familiar with the `<canvas>` element from HTML5, but what is less known by non-developers is that a canvas can be used in two very different ways:

* CPU-based pixel computation using `canvas.getContext("2d")`
* GPU-based pixel computation using `canvas.getContext("webgl2")`

In the WebGL implementation, the pixel values (also known as the rendering buffer) are exclusively stored in GPU memory and aren't directly accessible to CPU-based processes, including JavaScript code. To access this data, we must explicitly request a copy of the rendering buffer to be transferred to CPU-accessible memory. This process, known as GPU-to-CPU readback, requires both processing units to be in specific states to make this possible. The timing of this transfer depends on various factors, including when the GPU's rendering buffer is cleared to accommodate the next frame and the specific timing of this clearance.

## Fix a missing map from the feedback button step-by-step

We have prepared a series of practical step-by-step tutorials on how to capture the screen using some of these reporting platforms services. As explored in the [previous section](#canvas-where-are-your-pixels), we established that the standard canvas method `.toDataURL()` is insufficient for accessing pixel values in CPU memory. Let's examine to resolve this limitation:

* Usersnap: [How to take a map screenshot with Usersnap](/sdk-js/examples/helper-screenshot-usersnap/)
* Ybug: [How to take a map screenshot with Ybug](/sdk-js/examples/helper-screenshot-ybug/)

In the tutorials we use the approach of *"Make the rendering buffer available"*. This approach involves explicitly establishing conditions that make the rendering buffer accessible and capturing a frame during this window of opportunity. **This is our preferred solution!** With MapTiler SDK.

A less efficient approach is *"Using the preserveDrawinBuffer"* (not recommended). This involves using the `preserveDrawinBuffer` option in the `Map` constructor. Setting this option to `true` propagates to the WebGL creation context and allows the GPU to keep the previous frame in memory, not clearing it until the very last moment when the next frame needs some room to render. This is by far the easiest way, and it guarantees that calling `.toDataURL()` on the map canvas will always produce a valid image. Unfortunately, this **has a heavy cost on performance**. Due to this limitation, we'll explore an alternative method.

Example of the preserveDrawinBuffer approach:

<pre><code class="language-js"><!--
const map = new maptilersdk.Map({
  container: document.getElementById("map-container"),
  style: maptilersdk.MapStyle.STREETS,
  geolocate: true,
  canvasContextAttributes: {
    preserveDrawingBuffer: true,
  },
});
--></code></pre>

##### Create a solution building upon this

Having covered the fundamental cause of the issue and identified a viable workaround for frame capture, we can now explore how to adapt this solution for seamless integration with feedback services like Usersnap.

It's important to note that Usersnap **will** automatically invoke the `.toDataURL()` function on the map's canvas element at an unpredictable moment. While this might seem like a minor technical detail, it leads us to walk on the thin ice of sketchy code and implement a somewhat unconventional solution. Let's acknowledge upfront that this approach could be considered a hack.

As previously discussed, the idle event triggers exclusively when all computation and rendering tasks are complete. Since this occurs during periods of user inactivity, we can leverage this opportunity to slip in some tiny extra computing without any noticeable impact on user experience.

The hack consists of two things:

* Implementing a mechanism to capture frames during each idle event
* Ensuring that the canvas .toDataURL() method returns data from the most recent idle event rather than the current moment of execution

Here's a practical implementation approach:

1. Replace the original `.toDataURL()` of the map canvas with a custom implementation.

    <pre><code class="language-js"><!--
    const map = new maptilersdk.Map({
      container: document.getElementById("map-container"),
      style: maptilersdk.MapStyle.STREETS,
      geolocate: true
    });

    // Explicitely triggering a redraw of the map
    map.redraw();

    const mapCanvas = map.getCanvas();

    // This will contain the frame data,
    // and will be replaced at every idle event
    let lastIdleDataURL = "";
    // We keep the original .toDataURL method because we still
    // need to call it!
    // (dont't forget to bind it)
    const originalToDataURL = mapCanvas.toDataURL.bind(mapCanvas);
    // Replacing the original .toDataURL() of the map canvas with a fake one that
    // returns the latest idle frame data.
    // The fake version is now the one being called by Usersnap.
    mapCanvas.toDataURL = function(type, encoderOptions) {
      
      return lastIdleDataURL;
    }
    // Waiting for the next moment, just after redraw, 
    // when the GPU will not be computing a new frame
    // When the map is idle, we get the dataURL to be stored for later.
    // Note how we are using the "originalToDataURL" function, 
    // since it's the one that does the actual frame grabbing
    map.on("idle", async () => {
      lastIdleDataURL = originalToDataURL();
    });
    --></code></pre>

    > [!WARNING]
    > It’s possible that some alternatives to Usersnap like Ybug, Feedbucket, Featurebase, BugHerd, Marker.io, etc. use `.toBlob()` [doc](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/toBlob) instead of `.toDataURL()` [doc](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/toDataURL), as this is a popular way to grab binary content of a canvas element, directly encoded and compressed as PNG or JPEG image. The main difference between these two methods is that .toBlob() relies on an asynchronous callback logic to yield the result while `.toDataURL()` synchronously returns the result.

2. Create an issue report using the feedback button.

3. Access the feedback tool dashboard and locate your newly created issue report.

4. View the attached screenshot image to confirm the successful capture of the map image. Now you have the map image in the report.

    

## Conclusion

Despite this approach being somewhat hacky, especially the part where we replace the standard `.toDataURL()` with a custom one, it proves **more efficient** than enabling the drawing buffer preservation option. For applications under your complete control, this logic can be safely implemented at the application level. Bear in mind that this should not be added to a library that could be used by multiple apps without the developer being aware of it, since their app may require the canvas object to behave in the standard way.

Performance-wise, executing the native `.toDataURL()` method typically requires from 50 to 100ms to fetch the image buffer from the GPU on an Apple Macbook Air M2, so it’s not something to use lightly. Yet, it’s acceptable to place this inside an `idle` callback due to the inherent nature of the event.

If you have your own feedback system or prefer not to utilize any of these feedback services but still need to **take a screenshot of the map** for error reporting or similar purposes, we highly recommend using the **<a href="/sdk-js/api/helpers/#screenshot">MapTiler SDK screenshot helper</a>** as the most straightforward solution.


The goal of this article was also to provide you with comprehensive technical details about why this implementation approach was necessary in the first place.



<script defer>
  setTimeout(() => {
    $("#toc").empty();
    $("#toc").toc({headings: "h2,h3"});
  }, 300);
</script>

