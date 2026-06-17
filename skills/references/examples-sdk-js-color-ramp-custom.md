# Source: https://docs.maptiler.com/sdk-js/examples/color-ramp-custom/

# Color ramp

This example shows how to create a custom color ramp and use it to visualize a point layer. Download the sample data [here](../../assets/schools.geojson){:target="_blank" rel="noopener"}.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const myCustomRamp = new maptilersdk.ColorRamp({
      stops: [
        { value: 100, color: [252, 222, 156] },
        { value: 500, color: [250, 164, 118] },
        { value: 1000, color: [240, 116, 110] },
        { value: 1500, color: [227, 79, 111] },
        { value: 2000, color: [220, 57, 119] },
        { value: 3000, color: [185, 37, 122] },
        { value: 4000, color: [124, 29, 111] },
      ]
    });

    map.on('load', async function () {
      await maptilersdk.helpers.addPoint(map, {
        data: 'schools.geojson',
        property: "students",
        pointColor: myCustomRamp,
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
    <title>Color ramp</title>
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
            center: [-119.807, 36.7828],
            zoom: 11.6
        });

        const myCustomRamp = new maptilersdk.ColorRamp({
              stops: [
                { value: 100, color: [252, 222, 156] },
                { value: 500, color: [250, 164, 118] },
                { value: 1000, color: [240, 116, 110] },
                { value: 1500, color: [227, 79, 111] },
                { value: 2000, color: [220, 57, 119] },
                { value: 3000, color: [185, 37, 122] },
                { value: 4000, color: [124, 29, 111] },
              ]
            });

            map.on('load', async function () {
              await maptilersdk.helpers.addPoint(map, {
                data: 'schools.geojson',
                property: "students",
                pointColor: myCustomRamp,
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
