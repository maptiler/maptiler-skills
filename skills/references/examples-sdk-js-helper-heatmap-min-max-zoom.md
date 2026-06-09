# Source: https://docs.maptiler.com/sdk-js/examples/helper-heatmap-min-max-zoom/

# Heatmap helper

In this example, we will illustrate the process of configuring the minimum and maximum zoom levels for a heatmap layer. To achieve this, we will utilize the heatmap layer helper. You can access the [earthquake sample data](../../assets/earthquakes.geojson){:target="_blank" rel="noopener"} required for this exercise.

When setting the maximum zoom level, the heatmap will gradually appear (fade-in), starting at -.25z after reaching the minimum zoom level. Similarly, as the maximum zoom level is approached, the heatmap will gradually fade-out by 0.25z.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', async function () {
      await maptilersdk.helpers.addHeatmap(map, {
        data: 'YOUR_MAPTILER_DATASET_ID_HERE',
        minzoom: 6,
        maxzoom: 8,
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
            center: [-118.609, 37.54],
            zoom: 7.92
        });

        map.on('load', async function () {
              await maptilersdk.helpers.addHeatmap(map, {
                data: 'YOUR_MAPTILER_DATASET_ID_HERE',
                minzoom: 6,
                maxzoom: 8,
              });
            });
    </script>
</body>
</html>
```
