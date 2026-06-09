# Source: https://docs.maptiler.com/sdk-js/examples/helper-polygon-pattern/

# Polygon helper

This example shows how to add a polygon layer with a fill pattern to the map using the polygon layer helper. To replicate this example, download the [Swiss sample data](../../assets/switzerland.geojson){:target="_blank" rel="noopener"} and the [cheese image](./cheese512.png).

By following this example, users can successfully integrate the desired polygon layer, complete with a unique fill pattern, into their maps using the polygon layer helper tool.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', async function () {
      await maptilersdk.helpers.addPolygon(map, {
        data: 'YOUR_MAPTILER_DATASET_ID_HERE',
        pattern: "cheese512.png",
        outline: true,
        outlineWidth: 3,
        outlineColor: "white",
        outlineDashArray: "_ ",
        fillOpacity: 0.7,
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
    <title>Polygon helper</title>
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
            center: [8.224, 46.823],
            zoom: 6.62
        });

        map.on('load', async function () {
              await maptilersdk.helpers.addPolygon(map, {
                data: 'YOUR_MAPTILER_DATASET_ID_HERE',
                pattern: "cheese512.png",
                outline: true,
                outlineWidth: 3,
                outlineColor: "white",
                outlineDashArray: "_ ",
                fillOpacity: 0.7,
              });
            });
    </script>
</body>
</html>
```
