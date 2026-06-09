# Source: https://docs.maptiler.com/leaflet/examples/custom-map/

# Display a custom map

This example demonstrates how to display a custom map from MapTiler on a web page using Leaflet JS.

To create your first custom map, check out the [How to create a custom map](/guides/general/how-to-create-custom-map/) tutorial.

<div class="tab-common-content" markdown="1">

1. Replace the tileLayer URL with your custom map style. Check the [Publish the map](/guides/general/how-to-create-custom-map/#publish-the-map) section to get the URL of your custom style.

<pre class="line-numbers" data-start="20" data-line-offset="20" data-line="20"><code class="language-js">

L.tileLayer(`https://api.maptiler.com/maps/YOUR_CUSTOM_MAP_ID/{z}/{x}/{y}.png?key=${key}`,{

tileSize: 512,

zoomOffset: -1,

minZoom: 1,

attribution: "\u003ca href=\"https://www.maptiler.com/copyright/\" target=\"_blank\"\u003e\u0026copy; MapTiler\u003c/a\u003e \u003ca href=\"https://www.openstreetmap.org/copyright\" target=\"_blank\"\u003e\u0026copy; OpenStreetMap contributors\u003c/a\u003e",

crossOrigin: true

}).addTo(map);

</code></pre>

</div>

</div>

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
    <title>Display a custom map</title>
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

          const map = L.map('map').setView([46.948652944430734, 10.989249486220501], 12);
          const layer = L.tileLayer(`https://api.maptiler.com/maps/YOUR_CUSTOM_MAP_ID/{z}/{x}/{y}.png?key=${key}`,{
            tileSize: 512,
            zoomOffset: -1,
            minZoom: 1,
            attribution: "\u003ca href=\"https://www.maptiler.com/copyright/\" target=\"_blank\"\u003e\u0026copy; MapTiler\u003c/a\u003e \u003ca href=\"https://www.openstreetmap.org/copyright\" target=\"_blank\"\u003e\u0026copy; OpenStreetMap contributors\u003c/a\u003e",
            crossOrigin: true
          }).addTo(map);
    </script>
</body>
</html>
```
