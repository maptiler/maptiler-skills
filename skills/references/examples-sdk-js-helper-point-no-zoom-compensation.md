# Source: https://docs.maptiler.com/sdk-js/examples/helper-point-no-zoom-compensation/

# Point helper

This example demonstrates the process of incorporating a layer of points onto the map by utilizing the point layer helper while keeping zoom compensation disabled. Obtain the [USA school's sample data](../../assets/schools.geojson){:target="_blank" rel="noopener"}.

In this particular example, the size of the points is adjusted based on the quantity of students enrolled in each school. It is advisable to view this map at zoom level 12 since zoom compensation has been deactivated.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', async function () {
      await maptilersdk.helpers.addPoint(map, {
        data: 'schools.geojson',
        property: "students",
        pointColor: maptilersdk.ColorRampCollection.PORTLAND.scale(200, 2000).resample("ease-out-sqrt"),
        pointOpacity: 0.8,
        minPointRadius: 6,
        maxPointRadius: 30,
        showLabel: true,
        zoomCompensation: false,
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
            style: maptilersdk.MapStyle.DATAVIZ.DARK,
            center: [-73.99807, 40.71265],
            zoom: 12
        });

        map.on('load', async function () {
              await maptilersdk.helpers.addPoint(map, {
                data: 'schools.geojson',
                property: "students",
                pointColor: maptilersdk.ColorRampCollection.PORTLAND.scale(200, 2000).resample("ease-out-sqrt"),
                pointOpacity: 0.8,
                minPointRadius: 6,
                maxPointRadius: 30,
                showLabel: true,
                zoomCompensation: false,
              });
            });
    </script>
</body>
</html>
```
