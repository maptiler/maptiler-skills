# Source: https://docs.maptiler.com/sdk-js/examples/helper-polyline-dash-array/

# Polyline helper

In this example, we will explore the process of incorporating a line layer with a dash pattern symbol into the map by utilizing the polyline layer helper. You can access the sample data by downloading the [Amphitheater Lake trail sample data](../../assets/Line_GeoJSON_example.geojson){:target="_blank" rel="noopener"}.

By following this approach, we can successfully incorporate a visually appealing dash pattern symbol into our line layer, enhancing its overall appearance and functionality on the map.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', async function () {
      await maptilersdk.helpers.addPolyline(map, {
        data: 'YOUR_MAPTILER_DATASET_ID_HERE',
        outline: true,
        lineDashArray: "___  _  ",
        lineColor: "#F1175D"
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
                lineDashArray: "___  _  ",
                lineColor: "#F1175D"
              });
            });
    </script>
</body>
</html>
```
