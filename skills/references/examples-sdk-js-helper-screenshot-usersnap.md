# Source: https://docs.maptiler.com/sdk-js/examples/helper-screenshot-usersnap/

# Maptiler screenshot

This tutorial addresses the common issue of blank images (missing maps) appearing in screenshots instead of a beautiful map displays when using Usersnap reporting and feedback tool.

1. Create a simple web page where we will add a map.

<pre class="line-numbers"><code class="language-html"><!--

<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Maptiler screenshot</title>

<script src="https://cdn.maptiler.com/maptiler-sdk-js//maptiler-sdk.umd.min.js"></script>

<link href="https://cdn.maptiler.com/maptiler-sdk-js//maptiler-sdk.css" rel="stylesheet" />

<style>

body {

margin: 60px 40px;

font-family: Arial, sans-serif;

}

width: calc(100% - 80px);

height: calc(100vh - 120px);

position: relative;

margin: auto;

box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);

}

.maptiler-logo {

position: absolute;

top: 10px;

left: 80px;

}

</style>

</head>

<body>

<div class="maptiler-logo">

<a href="https://www.maptiler.com/" target="_blank">

</a>

</div>

<div id="map-container"></div>

<script>

maptilersdk.config.apiKey = "YOUR_MAPTILER_API_KEY_HERE";

const map = new maptilersdk.Map({

container: document.getElementById("map-container"),

style: maptilersdk.MapStyle.STREETS,

geolocate: true,

});

</script>

</body>

</html>

--></code></pre>

1. Insert your valid [MapTiler API key](https://cloud.maptiler.com/account/keys/) in place of `YOUR_MAPTILER_API_KEY_HERE`.

1. Insert the Usersnap snippet. Copy this code into your webpage, right before the closing `</body>` tag or view the [Usersnap installation guide](https://help.usersnap.com/docs/installation-via-html)

<pre class="line-numbers" data-start="44" data-line-offset="43" data-line="44-52"><code class="language-html"><!--

<script>

window.onUsersnapLoad = function(api) {

api.init();

};

var script = document.createElement('script');

script.defer = 1;

script.src = 'https://widget.usersnap.com/global/load/YOUR-USERSNAP-SPACE-API-KEY?onload=onUsersnapLoad';

document.getElementsByTagName('head')[0].appendChild(script);

</script>

--></code></pre>

1. Replace `YOUR-USERSNAP-SPACE-API-KEY` with your designated Usersnap Space API Key.

1. Reload the page. Here is what the basic web page looks like:

1. Get user feedback. Click the Feedback button to Report an issue. Thanks to the Feedback widget with screen capture, you can collect not only the feedback of your users but also take screenshots or screen recordings from their browsers.

1. Utilize the integrated feedback tools to annotate the map by drawing relevant markings and complete the detailed issue submission form with pertinent information.

1. Click the Submit button to send your feedback.

1. Review the user feedback. Access the Usersnap dashboard interface and select the specific issue report created during the previous step.

1. Open the attached screenshot image. Sadly, you'll notice the screenshot appears in the Usersnap dashboard without the map image (no map image). This is how the screenshot looks in the Usersnap dashboard:

1. Make the rendering buffer available. Replace the original `.toDataURL()` of the map canvas with a custom implementation.

<pre class="line-numbers" data-start="38" data-line-offset="37" data-line="44-70"><code class="language-js"><!--

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

1. Create an issue report using the feedback button.

1. Access the Usersnap dashboard and locate your newly created issue report.

1. View the attached screenshot image to confirm the successful capture of the map image. Now you have the map image in the report.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
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
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Maptiler screenshot</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <style>
        body { margin: 0; padding: 0; }
        #map { position: absolute; top: 0; bottom: 0; width: 100%; }
    </style>
</head>
<body>
    <div id="map"></div>
    <script>
        maptilersdk.config.apiKey = 'YOUR_MAPTILER_API_KEY';

        const map = new maptilersdk.Map({
            container: 'map',
            style: maptilersdk.MapStyle.STREETS,
            center: [0, 0],
            zoom: 0
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
    </script>
</body>
</html>
```
