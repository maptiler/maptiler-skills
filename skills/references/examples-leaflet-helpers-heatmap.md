# Source: https://docs.maptiler.com/leaflet/examples/helpers-heatmap/

# Vector Tiles in Leaflet JS

Learn how to create a heatmap layer in Leaflet JavaScript library using the leaflet-maptilersdk plugin.

In this example, the heatmap layer is zoom-compensated and as a result the blobs roughly maintain their size in world-scale as we zoom-in/out. Download the [earthquake sample data](/sdk-js/assets/earthquakes.geojson).

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
mtLayer.on("ready", () => {     
        
        // Leverage the MapTiler SDK layer helpers to easily add polyline / point / polygon / heatmap layers
        mtLayer.addHeatmap({
          data: 'earthquakes.geojson',
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

        const map = L.map('map').setView([37.999, -119.715], 7);
              const mtLayer = L.maptiler.maptilerLayer({
                apiKey: 'YOUR_MAPTILER_API_KEY_HERE',
                style: L.maptiler.MapStyle.DATAVIZ.LIGHT, // optional
              }).addTo(map);

              mtLayer.on("ready", () => {     

                // Leverage the MapTiler SDK layer helpers to easily add polyline / point / polygon / heatmap layers
                mtLayer.addHeatmap({
                  data: 'earthquakes.geojson',
                });

              });
    </script>
</body>
</html>
```
