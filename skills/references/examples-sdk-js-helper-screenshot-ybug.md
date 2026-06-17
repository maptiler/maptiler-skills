# Source: https://docs.maptiler.com/sdk-js/examples/helper-screenshot-ybug/

# Maptiler screenshot

This tutorial addresses the common issue of blank images (missing maps) appearing in screenshots instead of a beautiful map displays when using Ybug reporting and feedback tool.

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

1. Insert the Ybug snippet. Copy this code into your webpage, right before the closing `</body>` tag or view the [Ybug installation guide](https://ybug.io/docs/installation)

<pre class="line-numbers" data-start="44" data-line-offset="43" data-line="44-51"><code class="language-html"><!--

<script type='text/javascript'>

(function() {

window.ybug_settings = {"id":"YOUR-YBUG-PROJECT-ID"};

var ybug = document.createElement('script'); ybug.type = 'text/javascript'; ybug.async = true;

ybug.src = 'https://widget.ybug.io/button/'+window.ybug_settings.id+'.js';

var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ybug, s);

})();

</script>

--></code></pre>

1. Replace `YOUR-YBUG-PROJECT-ID` with your designated Ybug project id.

1. Reload the page. Here is what the basic web page looks like:

1. Get user feedback. Click the Feedback button to Report an issue. Thanks to the Feedback widget with screen capture, you can collect not only the feedback of your users but also take screenshots or screen recordings from their browsers.

1. Utilize the integrated feedback tools to annotate the map by drawing relevant markings and complete the detailed issue submission form with pertinent information.

1. Click the Submit button to send your feedback.

1. Review the user feedback. Access the Ybug dashboard interface and select the specific issue report created during the previous step.

1. Open the attached screenshot image. Sadly, you'll notice the screenshot appears in the Ybug dashboard without the map image (no map image). This is how the screenshot looks in the Ybug dashboard:

1. Make the rendering buffer available. Use the Ybug's `beforescreenshot` event which allows you to perform any necessary preparations or modifications to the page before the screenshot is taken. Read more about other [Ybug events](https://ybug.io/docs/installation#js-events).

<pre class="line-numbers" data-start="38" data-line-offset="37" data-line="44-52"><code class="language-js"><!--

const map = new maptilersdk.Map({

container: document.getElementById("map-container"),

style: maptilersdk.MapStyle.STREETS,

geolocate: true

});

map.on('ready', () => {

Ybug.on('beforescreenshot', () => {

// Do some sync work here...

// If you need to perform some async actions, you can return a Promise

return new Promise(async(resolve) => {

// Do some async work...

resolve();

});

});

--></code></pre>

1. Get the map screenshot using the [MapTiler SDK screenshot helper](/sdk-js/api/helpers/#screenshot).

<pre class="line-numbers" data-start="44" data-line-offset="43" data-line="47,48,51-62"><code class="language-js"><!--

map.on('ready', () => {

Ybug.on('beforescreenshot', () => {

// Do some sync work here...

const mapCanvas = map.getCanvas();

// If you need to perform some async actions, you can return a Promise

return new Promise(async(resolve) => {

// Do some async work...

const mapBlob = await maptilersdk.helpers.takeScreenshot(map);

//Convert Blob to dataURL

const a = new FileReader();

a.onload = function(e) {

mapCanvas.toDataURL = (type, quality) => {

// Return the screenshot directly (e.g., Base64 string)

return e.target.result;

};

resolve();

}

a.readAsDataURL(mapBlob);

});

});

--></code></pre>

1. Create an issue report using the feedback button.

1. Access the Ybug dashboard and locate your newly created issue report.

1. View the attached screenshot image to confirm the successful capture of the map image. Now you have the map image in the report.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('ready', () => {
      Ybug.on('beforescreenshot', () => {
        // Do some sync work here...
        const mapCanvas = map.getCanvas();

        // If you need to perform some async actions, you can return a Promise
        return new Promise(async(resolve) => {
          // Do some async work...
          const mapBlob = await maptilersdk.helpers.takeScreenshot(map);
          //Convert Blob to dataURL
          const a = new FileReader();
          a.onload = function(e) {
            mapCanvas.toDataURL = (type, quality) => {
               // Return the screenshot directly (e.g., Base64 string)
               return e.target.result;
            };
            resolve();
          }
          a.readAsDataURL(mapBlob);
        });
      });
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

        map.on('ready', () => {
              Ybug.on('beforescreenshot', () => {
                // Do some sync work here...
                const mapCanvas = map.getCanvas();

                // If you need to perform some async actions, you can return a Promise
                return new Promise(async(resolve) => {
                  // Do some async work...
                  const mapBlob = await maptilersdk.helpers.takeScreenshot(map);
                  //Convert Blob to dataURL
                  const a = new FileReader();
                  a.onload = function(e) {
                    mapCanvas.toDataURL = (type, quality) => {
                       // Return the screenshot directly (e.g., Base64 string)
                       return e.target.result;
                    };
                    resolve();
                  }
                  a.readAsDataURL(mapBlob);
                });
              });
            });
    </script>
</body>
</html>
```
