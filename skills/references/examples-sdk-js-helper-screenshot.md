# Source: https://docs.maptiler.com/sdk-js/examples/helper-screenshot/

# Screenshot helper

This example shows how to capture the current map view as a `blob` (PNG image). The [screenshot helper](/sdk-js/api/helpers/#screenshot) is the most convenient way to save map snapshots.

The returned `blob` of a PNG image file can be very handy if the goal is to programmatically further manipulate the screenshot, such as sending it to some feedback endpoint with a POST request.

In this example we are going to use the `takeScreenshot` helper to replace the *drawn map image* (in the lower left corner of the map) with an image of the current map view.

<sup>Click on the <i>Take screenshot</i> button to replace the drawing map image for the current map view image</sup>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('ready', () => {
      document.getElementById('screenshot').addEventListener('click', function () {
        takePicture();
      });
    });

    async function takePicture() {
      const imageSnapshot = document.getElementById('snapshot');
      imageSnapshot.classList.add('hidden');
      const mapBlob = await maptilersdk.helpers.takeScreenshot(map);
      const objectURL = URL.createObjectURL(mapBlob);
      imageSnapshot.src = objectURL;
      imageSnapshot.classList.remove('hidden');
    }
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Screenshot helper</title>
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
            style: maptilersdk.MapStyle.HYBRID,
            center: [16.373344, 48.208479],
            zoom: 17.5
        });

        map.on('ready', () => {
              document.getElementById('screenshot').addEventListener('click', function () {
                takePicture();
              });
            });

            async function takePicture() {
              const imageSnapshot = document.getElementById('snapshot');
              imageSnapshot.classList.add('hidden');
              const mapBlob = await maptilersdk.helpers.takeScreenshot(map);
              const objectURL = URL.createObjectURL(mapBlob);
              imageSnapshot.src = objectURL;
              imageSnapshot.classList.remove('hidden');
            }
    </script>
</body>
</html>
```
