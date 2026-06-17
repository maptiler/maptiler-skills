# Source: https://docs.maptiler.com/leaflet/examples/map-language/

# Vector Tiles in Leaflet JS

This tutorial shows how to change the default map labels language. By default, if nothing is specified, the SDK uses the language defined in the browser. This corresponds to `maptilersdk.Language.AUTO`. To change the default language of the map, indicate the language in the `L.maptiler.maptilerLayer` config.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
document.getElementById('buttons').addEventListener('click', function (event) {
        // Retrieve language based on button id
        mtLayer.setLanguage(L.maptiler.Language[event.target.id]);
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

              const map = L.map('map').setView([50, 20], 3);
              const mtLayer = L.maptiler.maptilerLayer({
                apiKey: key,
                style: L.maptiler.MapStyle.STREETS, // optional
                language: L.maptiler.Language.JAPANESE, //change the default language
              }).addTo(map);

              document.getElementById('buttons').addEventListener('click', function (event) {
                // Retrieve language based on button id
                mtLayer.setLanguage(L.maptiler.Language[event.target.id]);
              });
    </script>
</body>
</html>
```
