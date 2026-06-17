# Source: https://docs.maptiler.com/leaflet/examples/default-marker/

# Display a marker

This tutorial shows how to add the default marker to the map using Leaflet JS.

<div class="tab-common-content" markdown="1">

1. Create a new marker using the L.marker function. Set Lat/Lng of the marker and finally added it to the current map using .addTo() function.

<pre class="line-numbers" data-start="27" data-line-offset="26" data-line="27"><code class="language-js">

L.marker([, ]).addTo(map);

</code></pre>

</div>

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
L.marker([55.665957, 12.550343]).addTo(map);
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Display a marker</title>
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

          const map = L.map('map').setView([0, 0], 2);
          const layer = L.tileLayer(`https://api.maptiler.com/maps/streets-v4/{z}/{x}/{y}.png?key=${key}`, {
            tileSize: 512,
            zoomOffset: -1,
            minZoom: 1,
            attribution: "\u003ca href=\"https://www.maptiler.com/copyright/\" target=\"_blank\"\u003e\u0026copy; MapTiler\u003c/a\u003e \u003ca href=\"https://www.openstreetmap.org/copyright\" target=\"_blank\"\u003e\u0026copy; OpenStreetMap contributors\u003c/a\u003e",
            crossOrigin: true
          }).addTo(map);
          L.marker([55.665957, 12.550343]).addTo(map);
    </script>
</body>
</html>
```
