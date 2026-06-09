# Source: https://docs.maptiler.com/sdk-js/examples/helper-polyline-blur/

# Polyline helper

This example demonstrates the addition of an outline glow blur symbol to enhance the visual appeal of a line layer. To achieve this, the polyline layer helper is employed. To implement this feature, simply download the [NY subway lines sample data](../../assets/NY_Subway_lines.geojson){:target="_blank" rel="noopener"}.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', async function () {
      await maptilersdk.helpers.addPolyline(map, {
        data: 'YOUR_MAPTILER_DATASET_ID_HERE',
        // --> Main line
        lineColor: "#fff",       // White
        lineOpacity: 0.7,        // Partially transparent to see the halo color through

        // --> Halo line
        outline: true,           // To create the electric halo, the outline is
        outlineColor: "#d83bff", // purple
        outlineOpacity: 0.5,     // half transparent
        outlineWidth: 15,        // quite large compared to the main line
        outlineBlur: 15,         // and blurry
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
            center: [-73.8931, 40.7396],
            zoom: 9.5
        });

        map.on('load', async function () {
              await maptilersdk.helpers.addPolyline(map, {
                data: 'YOUR_MAPTILER_DATASET_ID_HERE',
                // --> Main line
                lineColor: "#fff",       // White
                lineOpacity: 0.7,        // Partially transparent to see the halo color through

                // --> Halo line
                outline: true,           // To create the electric halo, the outline is
                outlineColor: "#d83bff", // purple
                outlineOpacity: 0.5,     // half transparent
                outlineWidth: 15,        // quite large compared to the main line
                outlineBlur: 15,         // and blurry
              });
            });
    </script>
</body>
</html>
```
