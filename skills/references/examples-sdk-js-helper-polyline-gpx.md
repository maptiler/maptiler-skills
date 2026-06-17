# Source: https://docs.maptiler.com/sdk-js/examples/helper-polyline-gpx/

# Polyline helper

Learn how to incorporate a GPX line layer into your map by utilizing the polyline layer helper in this illustrative example. To replicate this example, download the [GPX run sample data](./run.gpx){:target="_blank" rel="noopener"}.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', async function () {
      await maptilersdk.helpers.addPolyline(map, {
        data: 'https://docs.maptiler.com/sdk-js/examples/helper-polyline-gpx/run.gpx',
        outline: true
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
    <title>Polyline helper</title>
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
            style: maptilersdk.MapStyle.DATAVIZ.DARK,
            center: [-77.01801, 38.92368],
            zoom: 14.5
        });

        map.on('load', async function () {
              await maptilersdk.helpers.addPolyline(map, {
                data: 'https://docs.maptiler.com/sdk-js/examples/helper-polyline-gpx/run.gpx',
                outline: true
              });
            });
    </script>
</body>
</html>
```
