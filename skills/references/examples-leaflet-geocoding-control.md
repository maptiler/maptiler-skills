# Source: https://docs.maptiler.com/leaflet/examples/geocoding-control/

# Geocoding in Leaflet JS

This tutorial shows how to search for places using MapTiler geocoding control. The geocoding control facilitate the use of the [MapTiler Geocoding API](https://www.maptiler.com/cloud/geocoding/){:target="\_blank" rel="noopener"}.

1. Include the geocoder component JavaScript and CSS files in the `<head>` of your HTML file.

<pre class="line-numbers" data-start="8" data-line-offset="7" data-line="8"><code class="language-html"><!--

<script src="https://cdn.maptiler.com/maptiler-geocoding-control//leaflet.umd.js"></script>

--></code></pre>

1. Instantiate the geocoding control and add it to the map.

<pre class="line-numbers" data-start="29" data-line-offset="28" data-line="29-30"><code class="language-js"><!--

const gc = new maptilerGeocoder.GeocodingControl({ apiKey: key });

map.addControl(gc);

--></code></pre>

</div>

1. Install the Geocoding control

<pre><code class="language-bash"><!--

npm install --save @maptiler/geocoding-control

--></code></pre>

1.  Import the Geocoding control component and CSS in your mapping application

<pre class="line-numbers" data-start="2" data-line-offset="1" data-line="2"><code class="language-js"><!--

import { GeocodingControl } from "@maptiler/geocoding-control/leaflet";

--></code></pre>

1.  Add the geocoder control to the map.

<pre class="line-numbers" data-start="12" data-line-offset="11" data-line="12,13"><code class="language-js"><!--

const gc = new GeocodingControl({ apiKey: key });

map.addControl(gc);

--></code></pre>

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const gc = new maptilerGeocoder.GeocodingControl({ apiKey: key });
  map.addControl(gc);
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Geocoding in Leaflet JS</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <script src="https://cdn.maptiler.com/leaflet-maptilersdk/v4.1.0/leaflet-maptilersdk.umd.min.js"></script>
    <script src="https://cdn.maptiler.com/maptiler-geocoding-control/v3.0.0/leaflet.umd.js"></script>
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

          const gc = new maptilerGeocoder.GeocodingControl({ apiKey: key });
          map.addControl(gc);
    </script>
</body>
</html>
```
