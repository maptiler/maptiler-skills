# Source: https://docs.maptiler.com/leaflet/examples/map-style/

# Vector Tiles in Leaflet JS

This tutorial shows how to change the basemap (background map) style. Our built-in styles are designed to make it easier for you to create beautiful maps, without the need for extra coding or worrying about outdated versions. Check out the [list of built-in styles](https://github.com/maptiler/maptiler-sdk-js#many-styles-to-choose-from).

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
document.getElementById('buttons').addEventListener('click', function (event) {
        let style = L.maptiler.MapStyle.STREETS;
        // Retrieve basemap style based on button id
        switch (event.target.id) {
          case "streets":
            style = L.maptiler.MapStyle.STREETS;
            break;
          case "outdoor":
            style = L.maptiler.MapStyle.OUTDOOR;
            break;
          case "dark":
            style = L.maptiler.MapStyle.DATAVIZ.DARK;
            break;
          case "light":
            style = L.maptiler.MapStyle.DATAVIZ.LIGHT;
            break;
        }
        mtLayer.setStyle(style);
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

              const map = L.map('map').setView([50, 20], 4);
              const mtLayer = L.maptiler.maptilerLayer({
                apiKey: key,
                style: L.maptiler.MapStyle.STREETS, // optional
              }).addTo(map);

              document.getElementById('buttons').addEventListener('click', function (event) {
                let style = L.maptiler.MapStyle.STREETS;
                // Retrieve basemap style based on button id
                switch (event.target.id) {
                  case "streets":
                    style = L.maptiler.MapStyle.STREETS;
                    break;
                  case "outdoor":
                    style = L.maptiler.MapStyle.OUTDOOR;
                    break;
                  case "dark":
                    style = L.maptiler.MapStyle.DATAVIZ.DARK;
                    break;
                  case "light":
                    style = L.maptiler.MapStyle.DATAVIZ.LIGHT;
                    break;
                }
                mtLayer.setStyle(style);
              });
    </script>
</body>
</html>
```
