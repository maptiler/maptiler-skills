# Source: https://docs.maptiler.com/leaflet/examples/geojson-polygon/

# Display a GeoJSON Layer

This tutorial shows how to add a GeoJSON overlay to the map using Leaflet JS.

<div class="tab-common-content" markdown="1">

1. Create GeoJSON layer. The following snippet creates GeoJSON layer with one feature (without attributes) and polygon geometry.

<pre class="line-numbers" data-start="27" data-line-offset="26"><code class="language-js">

L.geoJSON({

'type': 'Feature',

'geometry': {

'type': 'Polygon',

'coordinates': [

[

[-67.13734351262877, 45.137451890638886],

[-66.96466, 44.8097],

[-68.03252, 44.3252],

[-69.06, 43.98],

[-70.11617, 43.68405],

[-70.64573401557249, 43.090083319667144],

[-70.75102474636725, 43.08003225358635],

[-70.79761105007827, 43.21973948828747],

[-70.98176001655037, 43.36789581966826],

[-70.94416541205806, 43.46633942318431],

[-71.08482, 45.3052400000002],

[-70.6600225491012, 45.46022288673396],

[-70.30495378282376, 45.914794623389355],

[-70.00014034695016, 46.69317088478567],

[-69.23708614772835, 47.44777598732787],

[-68.90478084987546, 47.184794623394396],

[-68.23430497910454, 47.35462921812177],

[-67.79035274928509, 47.066248887716995],

[-67.79141211614706, 45.702585354182816],

[-67.13734351262877, 45.137451890638886]

]

]

}

}, {

style: {

color: "#088",

opacity: 0.8,

fillColor: "#088",

fillOpacity: 0.8

}

}).addTo(map);

</code></pre>

</div>

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
L.geoJSON({
    'type': 'Feature',
    'geometry': {
      'type': 'Polygon',
      'coordinates': [
        [
          [-67.13734351262877, 45.137451890638886],
          [-66.96466, 44.8097],
          [-68.03252, 44.3252],
          [-69.06, 43.98],
          [-70.11617, 43.68405],
          [-70.64573401557249, 43.090083319667144],
          [-70.75102474636725, 43.08003225358635],
          [-70.79761105007827, 43.21973948828747],
          [-70.98176001655037, 43.36789581966826],
          [-70.94416541205806, 43.46633942318431],
          [-71.08482, 45.3052400000002],
          [-70.6600225491012, 45.46022288673396],
          [-70.30495378282376, 45.914794623389355],
          [-70.00014034695016, 46.69317088478567],
          [-69.23708614772835, 47.44777598732787],
          [-68.90478084987546, 47.184794623394396],
          [-68.23430497910454, 47.35462921812177],
          [-67.79035274928509, 47.066248887716995],
          [-67.79141211614706, 45.702585354182816],
          [-67.13734351262877, 45.137451890638886]
        ]
      ]
    }
  }, {
    style: {
      color: "#088",
      opacity: 0.8,
      fillColor: "#088",
      fillOpacity: 0.8
    }
  }).addTo(map);
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Display a GeoJSON Layer</title>
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

          const map = L.map('map').setView([45.137451890638886, -68.13734351262877], 6);
          const layer = L.tileLayer(`https://api.maptiler.com/maps/streets-v4/{z}/{x}/{y}.png?key=${key}`, {
            tileSize: 512,
            zoomOffset: -1,
            minZoom: 1,
            attribution: "\u003ca href=\"https://www.maptiler.com/copyright/\" target=\"_blank\"\u003e\u0026copy; MapTiler\u003c/a\u003e \u003ca href=\"https://www.openstreetmap.org/copyright\" target=\"_blank\"\u003e\u0026copy; OpenStreetMap contributors\u003c/a\u003e",
            crossOrigin: true
          }).addTo(map);
          L.geoJSON({
            'type': 'Feature',
            'geometry': {
              'type': 'Polygon',
              'coordinates': [
                [
                  [-67.13734351262877, 45.137451890638886],
                  [-66.96466, 44.8097],
                  [-68.03252, 44.3252],
                  [-69.06, 43.98],
                  [-70.11617, 43.68405],
                  [-70.64573401557249, 43.090083319667144],
                  [-70.75102474636725, 43.08003225358635],
                  [-70.79761105007827, 43.21973948828747],
                  [-70.98176001655037, 43.36789581966826],
                  [-70.94416541205806, 43.46633942318431],
                  [-71.08482, 45.3052400000002],
                  [-70.6600225491012, 45.46022288673396],
                  [-70.30495378282376, 45.914794623389355],
                  [-70.00014034695016, 46.69317088478567],
                  [-69.23708614772835, 47.44777598732787],
                  [-68.90478084987546, 47.184794623394396],
                  [-68.23430497910454, 47.35462921812177],
                  [-67.79035274928509, 47.066248887716995],
                  [-67.79141211614706, 45.702585354182816],
                  [-67.13734351262877, 45.137451890638886]
                ]
              ]
            }
          }, {
            style: {
              color: "#088",
              opacity: 0.8,
              fillColor: "#088",
              fillOpacity: 0.8
            }
          }).addTo(map);
    </script>
</body>
</html>
```
