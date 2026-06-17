# Source: https://docs.maptiler.com/sdk-js/examples/helper-heatmap-minimal/

# Heatmap helper

This example shows the process of adding a heatmap layer onto the map by using the heatmap layer helper with its default settings. To replicate this example, download the [earthquake sample data](../../assets/earthquakes.geojson){:target="_blank" rel="noopener"}.

A **heatmap map** is a visual representation of data values using different colors to indicate their magnitude within a dataset. In certain scenarios, like crime analytics, the color in a heatmap is used to represent the density of data points rather than the specific value associated with each point.

In this particular example, the heatmap layer is designed to compensate for zooming, which means that the size of the blobs remains relatively consistent when we zoom in or out on a global scale. This behavior is the standard default setting.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', async function () {
      await maptilersdk.helpers.addHeatmap(map, {
        data: 'YOUR_MAPTILER_DATASET_ID_HERE',
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
    <title>Heatmap helper</title>
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
            style: maptilersdk.MapStyle.DATAVIZ.LIGHT,
            center: [-119.715, 37.999],
            zoom: 6.56
        });

        map.on('load', async function () {
              await maptilersdk.helpers.addHeatmap(map, {
                data: 'YOUR_MAPTILER_DATASET_ID_HERE',
              });
            });
    </script>
</body>
</html>
```
