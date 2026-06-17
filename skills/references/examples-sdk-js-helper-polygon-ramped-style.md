# Source: https://docs.maptiler.com/sdk-js/examples/helper-polygon-ramped-style/

# Polygon helper

This example showcases the procedure of integrating a polygon layer that utilizes a color ramp symbol into a map. This allows for the alteration of the fill color based on the map's zoom level. To achieve this, the polygon layer helper is employed. You can access the sample data by downloading the [sample data of Switzerland](../../assets/switzerland.geojson){:target="_blank" rel="noopener"}.

Furthermore, in this example, we also modify the color of the polygon border depending on the zoom level of the map.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', async function () {
      await maptilersdk.helpers.addPolygon(map, {
        data: 'YOUR_MAPTILER_DATASET_ID_HERE',
        fillColor: [
          {zoom: 5, value: "#d12d0d"},
          {zoom: 6, value: "#d18c0d"},
          {zoom: 7, value: "#a0d10d"},
          {zoom: 8, value: "#0dd189"},
          {zoom: 9, value: "#0d93d1"},
          {zoom: 10, value: "#340dd1"},
          ],
          outline: true,
          outlineDashArray: "__ ",
          outlineWidth: [
            {zoom: 0, value: 0},
            {zoom: 3, value: 1},
            {zoom: 6, value: 2},
            {zoom: 8, value: 4},
            {zoom: 15, value: 10},
            {zoom: 22, value: 20},
          ],
          outlineColor: [
            {zoom: 4, value: "white"},
            {zoom: 5, value: "red"},
            {zoom: 6, value: "white"},
            {zoom: 7, value: "red"},
            {zoom: 8, value: "white"},
            {zoom: 9, value: "red"},
            {zoom: 10, value: "white"},
          ],
          outlinePosition: "inside",
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
            style: maptilersdk.MapStyle.STREETS,
            center: [8.224, 46.823],
            zoom: 6.62
        });

        map.on('load', async function () {
              await maptilersdk.helpers.addPolygon(map, {
                data: 'YOUR_MAPTILER_DATASET_ID_HERE',
                fillColor: [
                  {zoom: 5, value: "#d12d0d"},
                  {zoom: 6, value: "#d18c0d"},
                  {zoom: 7, value: "#a0d10d"},
                  {zoom: 8, value: "#0dd189"},
                  {zoom: 9, value: "#0d93d1"},
                  {zoom: 10, value: "#340dd1"},
                  ],
                  outline: true,
                  outlineDashArray: "__ ",
                  outlineWidth: [
                    {zoom: 0, value: 0},
                    {zoom: 3, value: 1},
                    {zoom: 6, value: 2},
                    {zoom: 8, value: 4},
                    {zoom: 15, value: 10},
                    {zoom: 22, value: 20},
                  ],
                  outlineColor: [
                    {zoom: 4, value: "white"},
                    {zoom: 5, value: "red"},
                    {zoom: 6, value: "white"},
                    {zoom: 7, value: "red"},
                    {zoom: 8, value: "white"},
                    {zoom: 9, value: "red"},
                    {zoom: 10, value: "white"},
                  ],
                  outlinePosition: "inside",
              });
            });
    </script>
</body>
</html>
```
