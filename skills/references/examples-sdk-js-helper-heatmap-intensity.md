# Source: https://docs.maptiler.com/sdk-js/examples/helper-heatmap-intensity/

# Heatmap helper

This example shows how to add a heatmap layer with a custom intensity to the map using the heatmap layer helper. Download the [earthquake sample data](../../assets/earthquakes.geojson){:target="_blank" rel="noopener"} to replicate this example.

In this example, we use a custom intensity zoom ramping higher than the default to add some boost to the heatmap's impact.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', async function () {
      await maptilersdk.helpers.addHeatmap(map, {
        data: 'YOUR_MAPTILER_DATASET_ID_HERE',
        intensity: [
          {zoom: 5, value: 1},
          {zoom: 12, value: 5},
        ]
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
            center: [-116.715, 33.542],
            zoom: 8.33
        });

        map.on('load', async function () {
              await maptilersdk.helpers.addHeatmap(map, {
                data: 'YOUR_MAPTILER_DATASET_ID_HERE',
                intensity: [
                  {zoom: 5, value: 1},
                  {zoom: 12, value: 5},
                ]
              });
            });
    </script>
</body>
</html>
```
