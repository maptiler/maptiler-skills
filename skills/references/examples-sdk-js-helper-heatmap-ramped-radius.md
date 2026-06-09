# Source: https://docs.maptiler.com/sdk-js/examples/helper-heatmap-ramped-radius/

# Heatmap helper

This example shows how to add a heatmap layer to the map by utilizing the heatmap layer helper, along with a customized zoom-ramping radius. You can access the sample data by downloading the [US schools example data](../../assets/schools.geojson){:target="_blank" rel="noopener"}.

The radius, which can be adjusted based on custom properties, is also internally adjusted in conjunction with zoom values.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', async function () {
      await maptilersdk.helpers.addHeatmap(map, {
        data: 'schools.geojson',
        radius: [
          {zoom: 2, value: 5 },
          {zoom: 5, value: 10 },
          {zoom: 10, value: 15 },
          {zoom: 15, value: 40 },
          {zoom: 20, value: 100 },
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
            center: [-89.755, 35.073],
            zoom: 8.06
        });

        map.on('load', async function () {
              await maptilersdk.helpers.addHeatmap(map, {
                data: 'schools.geojson',
                radius: [
                  {zoom: 2, value: 5 },
                  {zoom: 5, value: 10 },
                  {zoom: 10, value: 15 },
                  {zoom: 15, value: 40 },
                  {zoom: 20, value: 100 },
                ],
              });
            });
    </script>
</body>
</html>
```
