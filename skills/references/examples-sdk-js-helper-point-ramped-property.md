# Source: https://docs.maptiler.com/sdk-js/examples/helper-point-ramped-property/

# Point helper

This example shows how to add a point layer to the map, where the size and color of each point are adjusted based on a specific attribute. The point layer helper is utilized to achieve this. To access the sample data, download the [USA school's sample data](../../assets/schools.geojson){:target="_blank" rel="noopener"}.

In this particular example, the size of the points is scaled proportionately to the number of students in each school. We aim to employ an ease-out resampling technique, albeit one that is not as rapidly increasing as the exponential method. Instead, we opt for the square-root approach, which proves to be quite effective.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', async function () {
      await maptilersdk.helpers.addPoint(map, {
        data: 'schools.geojson',
        property: "students",
        pointColor: maptilersdk.ColorRampCollection.PORTLAND.scale(300, 4000).resample("ease-out-sqrt"),
        pointOpacity: 0.7,
        minPointRadius: 1,
        maxPointRadius: 100,
        showLabel: true,
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
            center: [-119.807, 36.7828],
            zoom: 11.6
        });

        map.on('load', async function () {
              await maptilersdk.helpers.addPoint(map, {
                data: 'schools.geojson',
                property: "students",
                pointColor: maptilersdk.ColorRampCollection.PORTLAND.scale(300, 4000).resample("ease-out-sqrt"),
                pointOpacity: 0.7,
                minPointRadius: 1,
                maxPointRadius: 100,
                showLabel: true,
              });
            });
    </script>
</body>
</html>
```
