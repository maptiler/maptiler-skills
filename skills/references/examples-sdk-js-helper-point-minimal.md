# Source: https://docs.maptiler.com/sdk-js/examples/helper-point-minimal/

# Point helper

This example shows how to add a point layer to the map using the point layer helper with the default values. Download the [earthquake sample data](../../assets/earthquakes.geojson){:target="_blank" rel="noopener"}.

In this example, the color is chosen randomly from a predetermined list of colors. This is the standard default behavior when no specific color is mentioned.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', async function () {
      await maptilersdk.helpers.addPoint(map, {
        data: 'YOUR_MAPTILER_DATASET_ID_HERE',
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
            center: [-119.602, 35.732],
            zoom: 4.30
        });

        map.on('load', async function () {
              await maptilersdk.helpers.addPoint(map, {
                data: 'YOUR_MAPTILER_DATASET_ID_HERE',
              });
            });
    </script>
</body>
</html>
```
