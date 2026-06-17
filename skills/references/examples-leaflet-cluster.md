# Source: https://docs.maptiler.com/leaflet/examples/cluster/

# Cluste

This tutorial shows how to visualize points as cluster maps with Leaflet JS. Learn how to group data points into clusters for effective data analysis and visualization.

In this Leaflet example, we use the Leaflet.markercluster plugin to create a cluster map with smooth animations and high-performance.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const markers = L.markerClusterGroup();

    (async () => {
      const response = await fetch('https://docs.maptiler.com/sdk-js/assets/earthquakes.geojson');
      const jsonData = await response.json();

      for (let i = 0; i < jsonData.features.length; i++) {
        const feature = jsonData.features[i];
        const title = feature.properties.mag;
        const marker = L.marker(new L.LatLng(feature.geometry.coordinates[1], feature.geometry.coordinates[0]), { title: title });
        marker.bindPopup(`${title}`);
        markers.addLayer(marker);
      }

      map.addLayer(markers);
    })();
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Cluste</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <script src="https://cdn.maptiler.com/leaflet-maptilersdk/v4.1.0/leaflet-maptilersdk.umd.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.5.3/leaflet.markercluster.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.5.3/MarkerCluster.css" rel="stylesheet" />
    <link href="https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.5.3/MarkerCluster.Default.css" rel="stylesheet" />
    <style>
        body { margin: 0; padding: 0; }
        #map { position: absolute; top: 0; bottom: 0; width: 100%; }
    </style>
</head>
<body>
    <div id="map"></div>
    <script>
        const key = 'YOUR_MAPTILER_API_KEY';
            const map = new L.Map('map', {maxZoom: 22}).setView([0, 20], 1);
            const mtLayer = L.maptiler.maptilerLayer({
              style: L.maptiler.MapStyle.DATAVIZ.LIGHT,
              apiKey: key,
            }).addTo(map);

            const markers = L.markerClusterGroup();

            (async () => {
              const response = await fetch('https://docs.maptiler.com/sdk-js/assets/earthquakes.geojson');
              const jsonData = await response.json();

              for (let i = 0; i < jsonData.features.length; i++) {
                const feature = jsonData.features[i];
                const title = feature.properties.mag;
                const marker = L.marker(new L.LatLng(feature.geometry.coordinates[1], feature.geometry.coordinates[0]), { title: title });
                marker.bindPopup(`${title}`);
                markers.addLayer(marker);
              }

              map.addLayer(markers);
            })();
    </script>
</body>
</html>
```
