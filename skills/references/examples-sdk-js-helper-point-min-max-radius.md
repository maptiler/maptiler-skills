# Source: https://docs.maptiler.com/sdk-js/examples/helper-point-min-max-radius/

# Point helper

This example illustrates the process of adjusting the default point size values for a point layer by utilizing the point layer helper. To replicate this example, download the [earthquake sample data](../../assets/earthquakes.geojson){:target="_blank" rel="noopener"}.

Our objective is to modify the default point size values, making smaller points even smaller and larger points even larger. Given that there is often overlap among multiple points, it is necessary to introduce a slight level of transparency.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', async function () {
      await maptilersdk.helpers.addPoint(map, {
        data: 'YOUR_MAPTILER_DATASET_ID_HERE',
        property: "mag",
        pointColor: maptilersdk.ColorRampCollection.VIRIDIS.scale(1, 5),
        minPointRadius: 2,
        maxPointRadius: 100,
        pointOpacity: 0.7,
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
    <title>Point helper</title>
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
            center: [-97.793, 36.504],
            zoom: 7.28
        });

        map.on('load', async function () {
              await maptilersdk.helpers.addPoint(map, {
                data: 'YOUR_MAPTILER_DATASET_ID_HERE',
                property: "mag",
                pointColor: maptilersdk.ColorRampCollection.VIRIDIS.scale(1, 5),
                minPointRadius: 2,
                maxPointRadius: 100,
                pointOpacity: 0.7,
              });
            });
    </script>
</body>
</html>
```
