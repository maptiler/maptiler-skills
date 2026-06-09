# Source: https://docs.maptiler.com/leaflet/examples/helpers-polygon/

# Vector Tiles in Leaflet JS

In this Leaflet JS example, you will learn how to handle thousands of polygons using the leaflet-maptilersdk plugin. Load large amounts of data into Leaflet without affecting the performance of your application.

This example shows how to add a polygon layer with a color ramp symbol that changes the fill color based on the map zoom level, with the help of the polygon layer helper.  Download the [building's sample data](/sdk-js/assets/guixols.geojson).

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
mtLayer.on("ready", () => {     
        
        // Leverage the MapTiler SDK layer helpers to easily add polyline / point / polygon / heatmap layers
        mtLayer.addPolygon({
          data: 'guixols.geojson',
          fillColor: [
            {zoom: 14, value: "#593895"},
            {zoom: 15, value: "#761FE8"},
            {zoom: 16, value: "#F1175D"},
            {zoom: 17, value: "#FB3A1B"},
            {zoom: 18, value: "#FBC935"},
            {zoom: 19, value: "#FFAA01"},
          ],
          outline: true,   
          outlineWidth: [
            {zoom: 14, value: 0},
            {zoom: 15, value: 1},
            {zoom: 16, value: 2},
            {zoom: 17, value: 3},
            {zoom: 18, value: 4},
            {zoom: 19, value: 5},
          ],
          outlineColor: [
            {zoom: 14, value: "#805CC2"},
            {zoom: 16, value: "#E25041"},
            {zoom: 18, value: "#FFD65F"},
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
    <title>Vector Tiles in Leaflet JS</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <script src="https://cdn.maptiler.com/leaflet-maptilersdk/v4.1.0/leaflet-maptilersdk.umd.min.js"></script>
    <style>
        body { margin: 0; padding: 0; }
        #map { position: absolute; top: 0; bottom: 0; width: 100%; }
    </style>
</head>
<body>
    <div id="map"></div>
    <script>
        const key = 'YOUR_MAPTILER_API_KEY';

        const map = L.map('map').setView([41.782993,3.030553], 14);
              const mtLayer = L.maptiler.maptilerLayer({
                apiKey: 'YOUR_MAPTILER_API_KEY_HERE',
                style: L.maptiler.MapStyle.DATAVIZ.LIGHT, // optional
              }).addTo(map);

              mtLayer.on("ready", () => {     

                // Leverage the MapTiler SDK layer helpers to easily add polyline / point / polygon / heatmap layers
                mtLayer.addPolygon({
                  data: 'guixols.geojson',
                  fillColor: [
                    {zoom: 14, value: "#593895"},
                    {zoom: 15, value: "#761FE8"},
                    {zoom: 16, value: "#F1175D"},
                    {zoom: 17, value: "#FB3A1B"},
                    {zoom: 18, value: "#FBC935"},
                    {zoom: 19, value: "#FFAA01"},
                  ],
                  outline: true,   
                  outlineWidth: [
                    {zoom: 14, value: 0},
                    {zoom: 15, value: 1},
                    {zoom: 16, value: 2},
                    {zoom: 17, value: 3},
                    {zoom: 18, value: 4},
                    {zoom: 19, value: 5},
                  ],
                  outlineColor: [
                    {zoom: 14, value: "#805CC2"},
                    {zoom: 16, value: "#E25041"},
                    {zoom: 18, value: "#FFD65F"},
                  ],
                  outlinePosition: "inside",
                });

              });
    </script>
</body>
</html>
```
