# Source: https://docs.maptiler.com/leaflet/examples/ts-get-started/

# 

How to use Leaflet with TypeScript: this tutorial shows how to install Leaflet from NPM and create a map and display it on a TypeScript application.

<iframe style="height: 400px; width: 100%" src="?key="></iframe>

You can pick from a large selection of bundlers and always find the best solution for your project. Whether you prefer [Parcel](https://parceljs.org/), [Webpack](https://webpack.js.org/), [Rollup](https://rollupjs.org/), [Turbopack](https://turbo.build/pack), or anything else.

1. Install the npm package.

<pre><code class="language-bash"><!--
npm install --save leaflet
--></code></pre>

1. Install the Leaflet types package.

<pre><code class="language-bash"><!--
npm install --save @types/leaflet @types/geojson
--></code></pre>

1. Create the map style. Add the map style to your stylesheet. The div must have non-zero height.

<pre><code class="language-css">
body { 
  margin: 0;
  padding: 0;
}

#map {
    position: absolute;
    top: 0;
    bottom: 0;
    width: 100%;
}
</code></pre>

1. Create a `<div>` element with a certain id where you want your map to be.

   Add `<div>` tag into your page. This div will be the container where the map will be loaded.

    <pre><code class="language-html"><!--
      <div id="map"></div>
    --></code></pre>

1. Include the CSS file.

   If you have a bundler that can handle CSS, you can import the CSS from leaflet/dist/leaflet.css.

   <pre><code class="language-js"><!--
   import 'leaflet/dist/leaflet.css';
   --></code></pre>

   > [!INFO]
   > Including the CSS file using a `<link>` in the head of the document via the CDN is the easiest way.
   > 
   > ```html
   > <link rel="stylesheet" href="https://unpkg.com/leaflet@/dist/leaflet.css" />
   > ```
   > 

1. Finally, load the map with the style. Include the following code in your TypeScript.

<pre><code class="language-ts">
import { map, latLng, tileLayer, MapOptions } from "leaflet";

import 'leaflet/dist/leaflet.css';

const options: MapOptions = {
  center: latLng(40.731253, -73.996139),
  zoom: 12,
};

const mymap = map('map', options);

const key = "YOUR_MAPTILER_API_KEY_HERE";

tileLayer(`https://api.maptiler.com/maps/streets-v4/{z}/{x}/{y}.png?key=${key}`,{ //style URL
  tileSize: 512,
  zoomOffset: -1,
  minZoom: 1,
  attribution: "\u003ca href=\"https://www.maptiler.com/copyright/\" target=\"_blank\"\u003e\u0026copy; MapTiler\u003c/a\u003e \u003ca href=\"https://www.openstreetmap.org/copyright\" target=\"_blank\"\u003e\u0026copy; OpenStreetMap contributors\u003c/a\u003e",
  crossOrigin: true
}).addTo(mymap);
</code></pre>

1. 

## Learn more

