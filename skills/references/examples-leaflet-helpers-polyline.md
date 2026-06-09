# Source: https://docs.maptiler.com/leaflet/examples/helpers-polyline/

# Vector Tiles in Leaflet JS

Learn how to handle thousands of lines with Leaflet JavaScript library using the leaflet-maptilersdk plugin. No matter how many vertices your lines have, the performance of your application will not be affected.

This Leaflet example shows how to add a line layer with an outline glow blur symbol to the map using the polyline layer helper. Download the [NY Subway lines sample data](/sdk-js/assets/NY_Subway_lines.geojson).

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
mtLayer.on("ready", () => {     
        
        // Leverage the MapTiler SDK layer helpers to easily add polyline / point / polygon / heatmap layers
        mtLayer.addPolyline({
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

        const map = L.map('map').setView([40.7396, -73.8931], 11);
              const mtLayer = L.maptiler.maptilerLayer({
                apiKey: 'YOUR_MAPTILER_API_KEY_HERE',
                style: L.maptiler.MapStyle.DATAVIZ.DARK, // optional
              }).addTo(map);

              mtLayer.on("ready", () => {     

                // Leverage the MapTiler SDK layer helpers to easily add polyline / point / polygon / heatmap layers
                mtLayer.addPolyline({
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
