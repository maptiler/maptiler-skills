# Source: https://docs.maptiler.com/leaflet/examples/npm-get-started/

# 

How to use Leaflet with NPM: this tutorial shows how to install Leaflet from NPM and create a map and display it on a web page.

<iframe style="height: 400px; width: 100%" src="?key="></iframe>

You can pick from a large selection of bundlers and always find the best solution for your project. Whether you prefer [Parcel](https://parceljs.org/), [Webpack](https://webpack.js.org/), [Rollup](https://rollupjs.org/), [Turbopack](https://turbo.build/pack), or anything else.

1. Install the npm package.

<pre><code class="language-bash"><!--
npm install --save leaflet
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
   > ```html liquid
   > <link rel="stylesheet" href="https://unpkg.com/leaflet@/dist/leaflet.css" />
   > ```
   > 

1. Finally, load the map with the style. Include the following code in your JavaScript.

<pre><code class="language-js">
import L from "leaflet";

import 'leaflet/dist/leaflet.css';

const map = L.map('map', {
  center: L.latLng(, ),
  zoom: ,
});

const key = 'YOUR_MAPTILER_API_KEY_HERE';

L.tileLayer(`https://api.maptiler.com/maps/streets-v4/{z}/{x}/{y}.png?key=${key}`,{ //style URL
  tileSize: 512,
  zoomOffset: -1,
  minZoom: 1,
  attribution: "\u003ca href=\"https://www.maptiler.com/copyright/\" target=\"_blank\"\u003e\u0026copy; MapTiler\u003c/a\u003e \u003ca href=\"https://www.openstreetmap.org/copyright\" target=\"_blank\"\u003e\u0026copy; OpenStreetMap contributors\u003c/a\u003e",
  crossOrigin: true
}).addTo(map);
</code></pre>

1. 



## Learn more

## NPM / Modules / Framework Implementation

### `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="robots" content="noindex">
  <title>Display a map</title>
  <link rel="stylesheet" href="./style.css">
</head>
<body>
  <div id="map"></div>
  <script type="module" src="./main.js"></script>
</body>
</html>
```

### `main.js`
```javascript
---
layout: none
---
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';

const key = 'YOUR_MAPTILER_API_KEY_HERE';
  
const map = L.map('map').setView([0,0], 2);
const layer = L.tileLayer(`https://api.maptiler.com/maps/streets-v4/{z}/{x}/{y}.png?key=${key}`,{
  tileSize: 512,
  zoomOffset: -1,
  minZoom: 1,
  attribution: "\u003ca href=\"https://www.maptiler.com/copyright/\" target=\"_blank\"\u003e\u0026copy; MapTiler\u003c/a\u003e \u003ca href=\"https://www.openstreetmap.org/copyright\" target=\"_blank\"\u003e\u0026copy; OpenStreetMap contributors\u003c/a\u003e",
  crossOrigin: true
}).addTo(map);
```

### `package.json`
```json
{
  "name": "maptiler-how-to-use-leaflet",
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "leaflet": "^1.9.4"
  },
  "devDependencies": {
    "vite": "^5.0.0"
  }
}
```

### `style.css`
```css
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
```

