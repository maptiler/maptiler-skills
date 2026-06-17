# Source: https://docs.maptiler.com/sdk-js/examples/helper-heatmap-color-ramp/

# Heatmap helper

This example illustrates the process of incorporating a heatmap layer into the map by utilizing the heatmap layer helper. With the assistance of the helper, it becomes feasible to introduce a personalized color ramp. In the given example, we define a customized `WARM` color scheme, instead of the default `TURBO` option. To replicate this example, download the [earthquake sample data](../../assets/earthquakes.geojson){:target="_blank" rel="noopener"}.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', async function () {
      await maptilersdk.helpers.addHeatmap(map, {
        data: 'YOUR_MAPTILER_DATASET_ID_HERE',
        colorRamp: maptilersdk.ColorRampCollection.WARM,
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
            center: [-119.715, 37.999],
            zoom: 6.56
        });

        map.on('load', async function () {
              await maptilersdk.helpers.addHeatmap(map, {
                data: 'YOUR_MAPTILER_DATASET_ID_HERE',
                colorRamp: maptilersdk.ColorRampCollection.WARM,
              });
            });
    </script>
</body>
</html>
```
