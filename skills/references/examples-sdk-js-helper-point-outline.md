# Source: https://docs.maptiler.com/sdk-js/examples/helper-point-outline/

# Point helper

The following example demonstrates the process of including a point layer on the map along with an outline. This can be achieved by utilizing the point layer helper.  To replicate this example, download the [earthquake sample data](../../assets/earthquakes.geojson){:target="_blank" rel="noopener"}.

In this example, the outline starts at zoom level 7. Additionally, the width and opacity of the outline can be gradually increased to create a visually appealing effect.

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
        showLabel: true,
        labelSize: 10, // 12 by default
        outline: true,
        outlineWidth: [
          {zoom: 6, value: 0},
          {zoom: 7, value: 1},
          {zoom: 12, value: 5},
        ],
        outlineOpacity: [
          {zoom: 7, value: 0},
          {zoom: 10, value: 1},
        ],
        outlineColor: "#000",
        labelColor: "#000"
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
            center: [151.401, -5.096],
            zoom: 7.88
        });

        map.on('load', async function () {
              await maptilersdk.helpers.addPoint(map, {
                data: 'YOUR_MAPTILER_DATASET_ID_HERE',
                property: "mag",
                pointColor: maptilersdk.ColorRampCollection.VIRIDIS.scale(1, 5),
                minPointRadius: 2,
                maxPointRadius: 100,
                pointOpacity: 0.7,
                showLabel: true,
                labelSize: 10, // 12 by default
                outline: true,
                outlineWidth: [
                  {zoom: 6, value: 0},
                  {zoom: 7, value: 1},
                  {zoom: 12, value: 5},
                ],
                outlineOpacity: [
                  {zoom: 7, value: 0},
                  {zoom: 10, value: 1},
                ],
                outlineColor: "#000",
                labelColor: "#000"
              });
            });
    </script>
</body>
</html>
```
