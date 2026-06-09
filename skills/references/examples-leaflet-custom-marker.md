# Source: https://docs.maptiler.com/leaflet/examples/custom-marker/

# Marker with custom icon

This tutorial shows how to define your custom icons for markers using Leaflet JS.

Introducing custom images and shadows to your markers can significantly enhance the visual appeal of your map. By adding a personal touch to your Leaflet icons, you can create a unique and engaging experience for your users.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const LeafIcon = L.Icon.extend({
          options: {
            shadowUrl: "https://docs.maptiler.com/leaflet/assets/leaf_shadow.png",
            iconSize:     [38, 95],
            shadowSize:   [50, 64],
            iconAnchor:   [22, 94],
            shadowAnchor: [4, 62],
            popupAnchor:  [-3, -76]
          }
        });

      const leafIcon = new LeafIcon({iconUrl: "https://docs.maptiler.com/leaflet/assets/leaf_marker.png"});

      L.marker([45.9767521, 7.6569418], {icon: leafIcon})
        .addTo(map)
        .openPopup();
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Marker with custom icon</title>
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
                style: L.maptiler.MapStyle.OUTDOOR, // optional
              }).addTo(map);

              const LeafIcon = L.Icon.extend({
                  options: {
                    shadowUrl: "https://docs.maptiler.com/leaflet/assets/leaf_shadow.png",
                    iconSize:     [38, 95],
                    shadowSize:   [50, 64],
                    iconAnchor:   [22, 94],
                    shadowAnchor: [4, 62],
                    popupAnchor:  [-3, -76]
                  }
                });

              const leafIcon = new LeafIcon({iconUrl: "https://docs.maptiler.com/leaflet/assets/leaf_marker.png"});

              L.marker([45.9767521, 7.6569418], {icon: leafIcon})
                .addTo(map)
                .openPopup();
    </script>
</body>
</html>
```
