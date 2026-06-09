# Source: https://docs.maptiler.com/sdk-js/examples/helper-polyline-simple/

# Polyline helper

This example demonstrates the process of incorporating and customizing a GeoJSON line layer on the map by utilizing the polyline layer helper. In this specific case, we will generate a line that is purple and has a border in gray. You can access the sample data by downloading the [Blue Hills sample data](./blue_hills.geojson){:target="_blank" rel="noopener"}.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', async function () {
      await maptilersdk.helpers.addPolyline(map, {
        data: 'https://docs.maptiler.com/sdk-js/examples/helper-polyline-simple/blue_hills.geojson',
        outline: true,
        lineColor: "purple",
        lineWidth: 6,
        outlineColor: "#D3DBEC", // mid gray
        outlineWidth: 10,
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
    <title>Polyline helper</title>
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
            center: [-110.75926, 43.72683],
            zoom: 13
        });

        map.on('load', async function () {
              await maptilersdk.helpers.addPolyline(map, {
                data: 'https://docs.maptiler.com/sdk-js/examples/helper-polyline-simple/blue_hills.geojson',
                outline: true,
                lineColor: "purple",
                lineWidth: 6,
                outlineColor: "#D3DBEC", // mid gray
                outlineWidth: 10,
              });
            });
    </script>
</body>
</html>
```
