# Source: https://docs.maptiler.com/sdk-js/examples/helper-polygon-minimal/

# Polygon helper

This example shows the process of incorporating a layer of polygons onto the map by utilizing the polygon layer helper and its default settings. Download the [Swiss sample data](../../assets/switzerland.geojson){:target="_blank" rel="noopener"}.

In this particular case, the color is assigned at random from a predetermined list of colors. This is the default behavior taken when a specific color is not designated.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', async function () {
      await maptilersdk.helpers.addPolygon(map, {
        data: 'YOUR_MAPTILER_DATASET_ID_HERE',
        fillOpacity: 0.5,
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
            style: maptilersdk.MapStyle.STREETS.LIGHT,
            center: [8.224, 46.823],
            zoom: 6.62
        });

        map.on('load', async function () {
              await maptilersdk.helpers.addPolygon(map, {
                data: 'YOUR_MAPTILER_DATASET_ID_HERE',
                fillOpacity: 0.5,
              });
            });
    </script>
</body>
</html>
```
