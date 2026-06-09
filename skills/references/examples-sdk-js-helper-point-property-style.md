# Source: https://docs.maptiler.com/sdk-js/examples/helper-point-property-style/

# Point helper

This example illustrates the process of incorporating a point layer into a map, with the color and size of the points determined by the "mag" property, which represents the magnitude of earthquakes. To achieve this, we utilize the point layer helper. To access the sample data necessary for this exercise, please download the [earthquake sample data](../../assets/earthquakes.geojson){:target="_blank" rel="noopener"}.

In this particular case, we have opted to establish magnitude boundaries ranging between 1 and 5.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', async function () {
      await maptilersdk.helpers.addPoint(map, {
        data: 'YOUR_MAPTILER_DATASET_ID_HERE',
        property: "mag",
        pointColor: maptilersdk.ColorRampCollection.VIRIDIS.scale(1, 5),
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
            center: [-167.99, 52.7],
            zoom: 4.30
        });

        map.on('load', async function () {
              await maptilersdk.helpers.addPoint(map, {
                data: 'YOUR_MAPTILER_DATASET_ID_HERE',
                property: "mag",
                pointColor: maptilersdk.ColorRampCollection.VIRIDIS.scale(1, 5),
              });
            });
    </script>
</body>
</html>
```
