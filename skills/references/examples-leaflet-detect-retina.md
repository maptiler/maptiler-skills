# Source: https://docs.maptiler.com/leaflet/examples/detect-retina/

# Detect retina

This tutorial shows how to detect a retina/HiDPI display to utilize the high resolution in the map images using Leaflet JS.

Using the `detectRetina` in the tileLayer options if the user is on a retina display, it will request four tiles of half the specified size and a bigger zoom level in place of one to utilize the high resolution.

You can also use the [scale parameter](/cloud/api/maps/#raster-xyz-tiles-path-scale)(`@2x`) in the tileLayer url to get the “retina”/HiDPI images directly from the server regardless of the device resolution. For example: `https://api.maptiler.com/maps/satellite-v4/{z}/{x}/{y}@2x.jpg`.

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
    <title>Detect retina</title>
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

            const map = L.map('map').setView([45.43725, 10.69844], 14.84);
            const layer = L.tileLayer(`https://api.maptiler.com/maps/satellite-v4/{z}/{x}/{y}.png?key=${key}`, {
              tileSize: 512,
              zoomOffset: -1,
              minZoom: 1,
              attribution: "\u003ca href=\"https://www.maptiler.com/copyright/\" target=\"_blank\"\u003e\u0026copy; MapTiler\u003c/a\u003e \u003ca href=\"https://www.openstreetmap.org/copyright\" target=\"_blank\"\u003e\u0026copy; OpenStreetMap contributors\u003c/a\u003e",
              crossOrigin: true,
              detectRetina: true,
            }).addTo(map);
    </script>
</body>
</html>
```
