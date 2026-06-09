# Source: https://docs.maptiler.com/sdk-js/examples/helper-polyline-ramped-style/

# Polyline helper

This example shows how to add a line layer to a map, utilizing a color ramp symbol that modifies the line color based on the map's zoom level. To accomplish this, the polyline layer helper is employed. To access the sample data, click on the [NY subway lines sample data](../../assets/NY_Subway_lines.geojson){:target="_blank" rel="noopener"} link.

In this particular example, it's not only the color of the line change but also the thickness of both the line and its outline dynamically adjusts as the map is zoomed in or out.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', async function () {
      await maptilersdk.helpers.addPolyline(map, {
        data: 'YOUR_MAPTILER_DATASET_ID_HERE',
        outline: true,
        lineColor: [
          {zoom: 10, value: "#d12d0d"},
          {zoom: 11, value: "#d18c0d"},
          {zoom: 12, value: "#a0d10d"},
          {zoom: 13, value: "#0dd189"},
          {zoom: 14, value: "#0d93d1"},
          {zoom: 15, value: "#340dd1"},
          {zoom: 16, value: "#ba0dd1"},
          {zoom: 17, value: "#d10d82"},
          {zoom: 18, value: "#d10d20"},
        ],
        lineWidth: [
          {zoom: 10, value: 1},
          {zoom: 16, value: 10},
        ],
        outlineColor: [
          {zoom: 10, value: "#0d93d1"},
          {zoom: 14, value: "#d10d20"},
          {zoom: 18, value: "#0d93d1"},
        ],
        outlineWidth: [
          {zoom: 9, value: 0.5},
          {zoom: 13, value: 6},
          {zoom: 15, value: 1},
          {zoom: 18, value: 8},
        ]
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
            style: maptilersdk.MapStyle.DATAVIZ.LIGHT,
            center: [-73.8931, 40.7396],
            zoom: 9.5
        });

        map.on('load', async function () {
              await maptilersdk.helpers.addPolyline(map, {
                data: 'YOUR_MAPTILER_DATASET_ID_HERE',
                outline: true,
                lineColor: [
                  {zoom: 10, value: "#d12d0d"},
                  {zoom: 11, value: "#d18c0d"},
                  {zoom: 12, value: "#a0d10d"},
                  {zoom: 13, value: "#0dd189"},
                  {zoom: 14, value: "#0d93d1"},
                  {zoom: 15, value: "#340dd1"},
                  {zoom: 16, value: "#ba0dd1"},
                  {zoom: 17, value: "#d10d82"},
                  {zoom: 18, value: "#d10d20"},
                ],
                lineWidth: [
                  {zoom: 10, value: 1},
                  {zoom: 16, value: 10},
                ],
                outlineColor: [
                  {zoom: 10, value: "#0d93d1"},
                  {zoom: 14, value: "#d10d20"},
                  {zoom: 18, value: "#0d93d1"},
                ],
                outlineWidth: [
                  {zoom: 9, value: 0.5},
                  {zoom: 13, value: 6},
                  {zoom: 15, value: 1},
                  {zoom: 18, value: 8},
                ]
              });
            });
    </script>
</body>
</html>
```
