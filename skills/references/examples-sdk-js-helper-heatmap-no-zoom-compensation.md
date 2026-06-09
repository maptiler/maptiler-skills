# Source: https://docs.maptiler.com/sdk-js/examples/helper-heatmap-no-zoom-compensation/

# Heatmap helper

This example shows how to add a heatmap layer onto a map without adjusting the radius based on the zoom level. To achieve this, we utilize the heatmap layer helper. You can access the sample data by downloading the [US schools example data](../../assets/schools.geojson){:target="_blank" rel="noopener"}.

By disabling the `.zoomCompensation`, we ensure that the size of the data points is solely determined by their corresponding property, rather than being influenced by the zoom level.

This heatmap map approach is particularly suitable for visualizations that are either fixed at a certain zoom level or have a limited range of zoom levels.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', async function () {
      await maptilersdk.helpers.addHeatmap(map, {
        data: 'schools.geojson',
        property: "students",
        zoomCompensation: false,
        radius: [
          {propertyValue: 500, value: 20},
          {propertyValue: 6000, value: 200},
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
            style: maptilersdk.MapStyle.DATAVIZ.LIGHT,
            center: [-81.4158, 28.5213],
            zoom: 11.51
        });

        map.on('load', async function () {
              await maptilersdk.helpers.addHeatmap(map, {
                data: 'schools.geojson',
                property: "students",
                zoomCompensation: false,
                radius: [
                  {propertyValue: 500, value: 20},
                  {propertyValue: 6000, value: 200},
                ],
              });
            });
    </script>
</body>
</html>
```
