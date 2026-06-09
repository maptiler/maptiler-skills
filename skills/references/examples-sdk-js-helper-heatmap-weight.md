# Source: https://docs.maptiler.com/sdk-js/examples/helper-heatmap-weight/

# Heatmap helper

This example shows how to add a heatmap layer into a map by utilizing a property as the weight. To accomplish this, the heatmap layer helper is employed. If you wish to access the [earthquake sample data](../../assets/earthquakes.geojson){:target="_blank" rel="noopener"}.

Incorporating a property as the weight **MUST** be paired with a ramping description. By configuring these options, earthquakes with magnitudes close to zero will be displayed with reduced intensity, while earthquakes with magnitudes of 6 or higher will be portrayed at their maximum intensity.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', async function () {
      await maptilersdk.helpers.addHeatmap(map, {
        data: 'YOUR_MAPTILER_DATASET_ID_HERE',
        property: "mag", // use the earthquake magnitude to add weight to each point
         weight: [
          {propertyValue: 0, value: 0},
          {propertyValue: 6, value: 1},
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
            center: [-112.5033, 46.8634],
            zoom: 10.82
        });

        map.on('load', async function () {
              await maptilersdk.helpers.addHeatmap(map, {
                data: 'YOUR_MAPTILER_DATASET_ID_HERE',
                property: "mag", // use the earthquake magnitude to add weight to each point
                 weight: [
                  {propertyValue: 0, value: 0},
                  {propertyValue: 6, value: 1},
                ],
              });
            });
    </script>
</body>
</html>
```
