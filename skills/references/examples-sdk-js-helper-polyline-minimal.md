# Source: https://docs.maptiler.com/sdk-js/examples/helper-polyline-minimal/

# Polyline helper

Learn how to incorporate a line layer into your map by utilizing the polyline layer helper. This example shows how to add a line layer to the map using the polyline layer helper with the default values. To replicate this example, download the [Amphitheater Lake trail sample data](../../assets/Line_GeoJSON_example.geojson){:target="_blank" rel="noopener"}.

In this instance, the color is randomly selected from a predefined list of colors. This is the default action when no specific color is specified.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', async function () {
      await maptilersdk.helpers.addPolyline(map, {
        data: 'YOUR_MAPTILER_DATASET_ID_HERE',
        outline: true,
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
            style: maptilersdk.MapStyle.OUTDOOR,
            center: [-110.75926, 43.72683],
            zoom: 14
        });

        map.on('load', async function () {
              await maptilersdk.helpers.addPolyline(map, {
                data: 'YOUR_MAPTILER_DATASET_ID_HERE',
                outline: true,
              });
            });
    </script>
</body>
</html>
```
