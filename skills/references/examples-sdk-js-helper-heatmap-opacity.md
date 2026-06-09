# Source: https://docs.maptiler.com/sdk-js/examples/helper-heatmap-opacity/

# Heatmap helper

This example demonstrates the process of incorporating a heatmap layer onto the map while customizing its opacity. To accomplish this, the heatmap layer helper is employed. To replicate this example, download the [earthquake sample data](../../assets/earthquakes.geojson){:target="_blank" rel="noopener"}.

In this particular instance, we modify the layer's transparency based on the zoom level.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', async function () {
      await maptilersdk.helpers.addHeatmap(map, {
        data: 'YOUR_MAPTILER_DATASET_ID_HERE',
        opacity: [
          {zoom: 3, value: 0 }, // fade in
          {zoom: 4, value: 1 }, // full opacity
          {zoom: 5, value: 0.75 }, // 75% opacity
          {zoom: 8, value: 0.50 }, // 50% opacity
          {zoom: 11, value: 0 }, // fade out
        ],
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
            style: maptilersdk.MapStyle.DATAVIZ.DARK,
            center: [-116.783, 33.5211],
            zoom: 8.8
        });

        map.on('load', async function () {
              await maptilersdk.helpers.addHeatmap(map, {
                data: 'YOUR_MAPTILER_DATASET_ID_HERE',
                opacity: [
                  {zoom: 3, value: 0 }, // fade in
                  {zoom: 4, value: 1 }, // full opacity
                  {zoom: 5, value: 0.75 }, // 75% opacity
                  {zoom: 8, value: 0.50 }, // 50% opacity
                  {zoom: 11, value: 0 }, // fade out
                ],
              });
            });
    </script>
</body>
</html>
```
