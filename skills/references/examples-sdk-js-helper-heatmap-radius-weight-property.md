# Source: https://docs.maptiler.com/sdk-js/examples/helper-heatmap-radius-weight-property/

# Heatmap helper

This example shows how to add a heatmap layer to the map, simultaneously controlling the radius and weight based on a property using the heatmap layer helper. Download the sample data [here](../../assets/schools.geojson){:target="_blank" rel="noopener"}.

Since zoomCompensation is disabled in this example, it is recommended to view the map specifically on z12.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', async function () {
      await maptilersdk.helpers.addHeatmap(map, {
        data: 'schools.geojson',
        property: "students",
        radius: [
          {propertyValue: 100, value: 15},
          {propertyValue: 800, value: 50},
        ],
        weight: [
          {propertyValue: 100, value: 0.1},
          {propertyValue: 800, value: 1},
        ],
        colorRamp: maptilersdk.ColorRampCollection.MAGMA,
        zoomCompensation: false,
        opacity: 0.7,
        intensity: 1.2,
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
            style: maptilersdk.MapStyle.DATAVIZ.DARK,
            center: [-77.01162, 38.94189],
            zoom: 12
        });

        map.on('load', async function () {
              await maptilersdk.helpers.addHeatmap(map, {
                data: 'schools.geojson',
                property: "students",
                radius: [
                  {propertyValue: 100, value: 15},
                  {propertyValue: 800, value: 50},
                ],
                weight: [
                  {propertyValue: 100, value: 0.1},
                  {propertyValue: 800, value: 1},
                ],
                colorRamp: maptilersdk.ColorRampCollection.MAGMA,
                zoomCompensation: false,
                opacity: 0.7,
                intensity: 1.2,
              });
            });
    </script>
</body>
</html>
```
