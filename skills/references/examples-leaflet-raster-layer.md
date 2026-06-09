# Source: https://docs.maptiler.com/leaflet/examples/raster-layer/

# Display a raster image

This Leaflet JS tutorial demonstrates how to add a raster image overlay to a map. You will learn how to load and display a single image on specific map areas.

<div class="tab-common-content" markdown="1">

1. Create an image layer using the L.imageOverlay function. Set the image Lat/Lng bounds. Here you can get the example image [aerial_wgs84.png](img/aerial_wgs84.png)

<pre class="line-numbers" data-start="27" data-line-offset="26"><code class="language-js">

L.imageOverlay("./aerial_wgs84.png", [

[50.900867668253724, 4.639663696289062],

[50.89935199434383, 4.642066955566406],

], {

opacity: 0.85

}).addTo(map);

</code></pre>

</div>

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
L.imageOverlay("./aerial_wgs84.png", [
    [50.900867668253724, 4.639663696289062],
    [50.89935199434383, 4.642066955566406],
  ], {
    opacity: 0.85
  }).addTo(map);
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Display a raster image</title>
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
          L.imageOverlay("./aerial_wgs84.png", [
            [50.900867668253724, 4.639663696289062],
            [50.89935199434383, 4.642066955566406],
          ], {
            opacity: 0.85
          }).addTo(map);
    </script>
</body>
</html>
```
