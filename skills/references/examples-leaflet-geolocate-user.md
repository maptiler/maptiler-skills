# Source: https://docs.maptiler.com/leaflet/examples/geolocate-user/

# Vector Tiles in Leaflet JS

This tutorial shows how to use the geolocate control with Leaflet to get the user’s location using the GPS or the browser location.

Unlock the power of GPS and Leaflet geolocate control to access your user's location effortlessly and enhance your application's functionality.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript

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

              // but this is going to be superseded by the `geolocate: true` options
              const map = L.map('map').setView([0, 0], 1);
              const mtLayer = L.maptiler.maptilerLayer({
                apiKey: key,
                style: L.maptiler.MapStyle.STREETS, // optional
                geolocate: true //set the initial view to the user's location
              }).addTo(map);
    </script>
</body>
</html>
```
