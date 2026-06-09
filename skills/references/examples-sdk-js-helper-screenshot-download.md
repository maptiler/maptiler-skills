# Source: https://docs.maptiler.com/sdk-js/examples/helper-screenshot-download/

# Screenshot helper

This example shows how to download the current map view as a PNG file. The [screenshot helper](/sdk-js/api/helpers/#screenshot) is the most convenient way to save map snapshots.

Getting a file directly is a nice option that can be useful to share some debugging context with colleagues, compare multiple styles, or share your creation on social media.

<sup>Click on the <i>Take screenshot</i> button to download a image for the current map view</sup>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('ready', () => {
    document.getElementById('screenshot').addEventListener('click', function () {
      maptilersdk.helpers.takeScreenshot(map, {
        download: true,
        filename: "maptiler_map_screenshot.png"
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
            style: maptilersdk.MapStyle.OUTDOOR,
            center: [0.66016, 42.62845],
            zoom: 11
        });

        map.on('ready', () => {
            document.getElementById('screenshot').addEventListener('click', function () {
              maptilersdk.helpers.takeScreenshot(map, {
                download: true,
                filename: "maptiler_map_screenshot.png"
              });
            });
          });
    </script>
</body>
</html>
```
