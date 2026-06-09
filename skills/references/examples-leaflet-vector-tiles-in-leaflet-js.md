# Source: https://docs.maptiler.com/leaflet/examples/vector-tiles-in-leaflet-js/

# Vector Tiles in Leaflet JS

Leaflet doesn't support vector tiles by default. You can use one of the available plugins to display vector tiles, but the best and easiest way is by using the [leaflet-maptilersdk](https://github.com/maptiler/leaflet-maptilersdk) plugin. Simply use the code below the map.

Use your MapTiler vector tiles basemaps in Leaflet using the [**L.maptiler.maptilerLayer**](https://github.com/maptiler/leaflet-maptilersdk). For basemaps, you can also use traditional [raster tiles](/leaflet/examples/raster-tiles-in-leaflet-js/) without the need to use any plugins.

Using the **L.maptiler.maptilerLayer** you have:

* All the power of [MapTiler SDK JS](/sdk-js/) to use vector tile layers (for data overlays) in your applications without any kind of limitation (show millions of geometries, choropleth maps, etc).

* Multi-lingual vector tiles basemaps for Leaflet using the MapTiler SDK.

* Use any of the many [professional looking basemaps](/sdk-js/api/map-styles/) created by MapTiler or use a map with your own custom basemap.

* Easily change the language of your map without having to create a new basemap.

* Locate the user and center the map accordingly.

<script src="/assets/js/tutorials.js"></script>

<pre><code class="language-html"><!--

<!DOCTYPE html>

<html>

<head>

<meta name="viewport" content="initial-scale=1,maximum-scale=1,user-scalable=no" />

<title>Vector Tiles in Leaflet JS</title>

<link rel="stylesheet" href="https://unpkg.com/leaflet@/dist/leaflet.css" />

<script src="https://unpkg.com/leaflet@/dist/leaflet.js"></script>

<script src="https://cdn.maptiler.com/maptiler-sdk-js//maptiler-sdk.umd.min.js"></script>

<link href="https://cdn.maptiler.com/maptiler-sdk-js//maptiler-sdk.css" rel="stylesheet" />

<script src="https://cdn.maptiler.com/leaflet-maptilersdk//leaflet-maptilersdk.umd.min.js"></script>

<style>

</style>

</head>

<body>

<div id="map"></div>

<script>

const key = 'YOUR_MAPTILER_API_KEY_HERE';

const map = L.map('map').setView([0, 0], 1);

const mtLayer = L.maptiler.maptilerLayer({

apiKey: key,

style: L.maptiler.MapStyle.STREETS, //optional

}).addTo(map);

</script>

</body>

</html>

--></code></pre>

</div>

<ol>

<li>

<p>Install the npm package.</p>

<pre><code class="language-bash"><!--

npm install --save leaflet @maptiler/leaflet-maptilersdk

--></code></pre>

</li>

<li>

<p>Include the CSS file.</p>

<p>If you have a bundler that can handle CSS, you can <a href="#" id="import-css-link"><code>import</code></a> the CSS or include it with a <a href="#"  id="cdn-css-link"><code>&lt;link&gt;</code></a> in the head of the document via the CDN</p>

<pre id="import-css-code"><code class="language-js"><!--

import 'leaflet/dist/leaflet.css';

--></code></pre>

<pre id="cdn-css-code" class="hidden"><code class="language-html"><!--

<link rel="stylesheet" href="https://unpkg.com/leaflet@/dist/leaflet.css" />

--></code></pre>

</li>

<li>

<p>Finally, load the map with the style. Include the following code in your JavaScript.</p>

<pre><code class="language-js"><!--

import L from "leaflet";

import 'leaflet/dist/leaflet.css';

// Import the Leaflet MapTiler Plugin

import "@maptiler/leaflet-maptilersdk";

const map = L.map('map', {

center: L.latLng(49.2125578, 16.62662018),

zoom: 14,

});

// Create a MapTiler Layer inside Leaflet

const mtLayer = new L.maptiler.maptilerLayer({

// Get your free API key at https://cloud.maptiler.com

apiKey: "YOUR_MAPTILER_API_KEY_HERE",

}).addTo(map);

--></code></pre>

</li>

</ol>

<p>

If you would rather stick to more modern API design and do not feel like using the <code class="language-plaintext">L</code> object, we got you covered:

</p>

<pre><code class="language-js"><!--

import { MaptilerLayer } from "@maptiler/leaflet-maptilersdk";

// ...

const mtLayer = new MaptilerLayer( options );

--></code></pre>

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

        const [zoom, lat, lng] = position.split('/');

            const map = L.map('map').setView([lat, lng], zoom);
            const mtLayer = L.maptiler.maptilerLayer({
              apiKey: key,
              style: (typeof mapId === 'string' || mapId instanceof String) ? `${mapId}` : mapId, // optional
            }).addTo(map);
    </script>
</body>
</html>
```
