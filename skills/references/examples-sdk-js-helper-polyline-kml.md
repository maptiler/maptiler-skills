# Source: https://docs.maptiler.com/sdk-js/examples/helper-polyline-kml/

# Polyline helper

This example shows the process of incorporating a KML line layer into the map by utilizing the polyline layer helper. You can download the [KML track sample data](./track.kml){:target="_blank" rel="noopener"} for this example.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', async function () {
      await maptilersdk.helpers.addPolyline(map, {
        data: 'https://docs.maptiler.com/sdk-js/examples/helper-polyline-kml/track.kml',
        outline: true,
        lineColor: '#3A1888'
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
            style: maptilersdk.MapStyle.BASE,
            center: [2.3101528, 48.7299456],
            zoom: 18
        });

        map.on('load', async function () {
              await maptilersdk.helpers.addPolyline(map, {
                data: 'https://docs.maptiler.com/sdk-js/examples/helper-polyline-kml/track.kml',
                outline: true,
                lineColor: '#3A1888'
              });
            });
    </script>
</body>
</html>
```
