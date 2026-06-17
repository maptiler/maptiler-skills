# Source: https://docs.maptiler.com/leaflet/examples/map-with-pins/

# Make a map with pins

This example shows how to make a map with pins using Leaflet JS. Load a geoJSON of points in Leaflet JS and add your custom pins or icons.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const leafIcon = new L.icon({
        iconUrl: "https://docs.maptiler.com/sdk-js/examples/custom-points-icon-png/underground.png", //your custom pin
        iconSize: [24, 26],
      });

      async function loadGeoJSON() {
        const response = await fetch(`https://api.maptiler.com/data/YOUR_MAPTILER_DATASET_ID_HERE/features.json?key=${key}`);
        const geoJSON = await response.json();
        L.geoJSON(geoJSON, {
          pointToLayer: function (geoJsonPoint, latlng) {
            return L.marker(latlng, {icon: leafIcon});
          }
        }).addTo(map);
      }

      loadGeoJSON();
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Make a map with pins</title>
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
              const map = L.map('map').setView([45.9767521, 7.6569418], 12);
              const mtLayer = L.maptiler.maptilerLayer({
                apiKey: key,
                style: L.maptiler.MapStyle.BASIC, // optional
              }).addTo(map);

              const leafIcon = new L.icon({
                iconUrl: "https://docs.maptiler.com/sdk-js/examples/custom-points-icon-png/underground.png", //your custom pin
                iconSize: [24, 26],
              });

              async function loadGeoJSON() {
                const response = await fetch(`https://api.maptiler.com/data/YOUR_MAPTILER_DATASET_ID_HERE/features.json?key=${key}`);
                const geoJSON = await response.json();
                L.geoJSON(geoJSON, {
                  pointToLayer: function (geoJsonPoint, latlng) {
                    return L.marker(latlng, {icon: leafIcon});
                  }
                }).addTo(map);
              }

              loadGeoJSON();
    </script>
</body>
</html>
```
