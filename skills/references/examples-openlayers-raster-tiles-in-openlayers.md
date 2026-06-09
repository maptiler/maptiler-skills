# Source: https://docs.maptiler.com/openlayers/examples/raster-tiles-in-openlayers/

# 

Raster tiles maps are actually nothing else than raster images. Zoomable raster maps consist of many raster map tiles (in the .png or .jpg format) placed next to each other, ordered in a pyramid scheme. This clever trick allows you to browse just a small part of the map without loading it whole while maintaining the feeling of exploring a single large document. Read more about zoomable maps and the pyramid scheme in [this article](https://www.maptiler.com/google-maps-coordinates-tile-bounds-projection/).

Use **recommended 512x512** raster tiles with TileJSON or XYZ.

Next, we will explain two ways how to create a map in OpenLayers using your MapTiler maps.

The first way is to use the TileJSON source function; this function is in charge of interpreting the TileJson file and creating the source with all the options and metadata. In a second way, we have to use the XYZ source; in this case, we must indicate the URL of the tiles that we want to load in our map and we will not have any metadata associated with the source.

<iframe style="height: 400px; width: 100%" src="?key="></iframe>

## Raster tiles TileJSON



Raster tiles TileJSON are loaded with [TileJSON](https://openlayers.org/en/latest/apidoc/module-ol_source_TileJSON-TileJSON.html) function. Start your code with the following starter:

<div class="tab-content cdn-steps" markdown="1">
<pre><code class="language-html"><!--
  <!DOCTYPE html>
  <html>
    <head>
      <meta name="viewport" content="initial-scale=1,maximum-scale=1,user-scalable=no" />
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/ol@/ol.css">
      <script src="https://cdn.jsdelivr.net/npm/ol@/dist/ol.js"></script>
      <style>
        #map {position: absolute; top: 0; right: 0; bottom: 0; left: 0;}
      </style>
    </head>
    <body>
      <div id="map">
        <a href="https://www.maptiler.com" style="position:absolute;left:10px;bottom:10px;z-index:999;"></a>
      </div>
      <p><a href="https://www.maptiler.com/copyright/" target="_blank">© MapTiler</a> <a href="https://www.openstreetmap.org/copyright" target="_blank">© OpenStreetMap contributors</a></p>
      <script>
        const key = 'YOUR_MAPTILER_API_KEY_HERE';
        const source = new ol.source.TileJSON({
          url: `https://api.maptiler.com/maps/streets-v4/tiles.json?key=${key}`,
          tileSize: 512,
          crossOrigin: 'anonymous'
        });

        const attribution = new ol.control.Attribution({
          collapsible: false,
        });

        const map = new ol.Map({
          layers: [
            new ol.layer.Tile({
              source: source
            })
          ],
          controls: ol.control.defaults.defaults({attribution: false}).extend([attribution]),
          target: 'map',
          view: new ol.View({
            constrainResolution: true,
            center: ol.proj.fromLonLat([0, 0]),
            zoom: 2
          })
        });
      </script>
    </body>

  </html>
 --></code></pre>
</div>

<div class="tab-content bundler-steps" markdown="1">
<pre><code class="language-js"><!--
import Map from 'ol/Map.js';
import View from 'ol/View.js';
import TileLayer from 'ol/layer/Tile.js';
import TileJSON from 'ol/source/TileJSON.js';
import Attribution from 'ol/control/Attribution.js';
import { defaults as defaultControls } from 'ol/control/defaults.js';
import { fromLonLat } from 'ol/proj.js';
import 'ol/ol.css';

const key = 'YOUR_MAPTILER_API_KEY_HERE';
const source = new TileJSON({
url: `https://api.maptiler.com/maps/streets-v4/tiles.json?key=${key}`,
tileSize: 512,
crossOrigin: 'anonymous'
});

const attribution = new Attribution({
collapsible: false,
});

const map = new Map({
layers: [
new TileLayer({
source: source
})
],
controls: defaultControls({attribution: false}).extend([attribution]),
target: 'map',
view: new View({
constrainResolution: true,
center: fromLonLat([0, 0]),
zoom: 2
})
});
--></code></pre>

</div>



Use **256x256** raster tiles for compatibility with certain libraries. To use the 256px tiles you must use this URL in your layer

<pre><code class="language-http">
  `https://api.maptiler.com/maps/streets-v4/256/tiles.json?key=${key}`
</code></pre>

Example of 256x256 raster tiles

<div class="tab-content cdn-steps" markdown="1">
<pre><code class="language-js">
const source = new ol.source.TileJSON({
  url: `https://api.maptiler.com/maps/streets-v4/256/tiles.json?key=${key}`,
  crossOrigin: 'anonymous'
});
</code></pre>
</div>

<div class="tab-content bundler-steps" markdown="1">
<pre><code class="language-js">
const source = new TileJSON({
  url: `https://api.maptiler.com/maps/streets-v4/256/tiles.json?key=${key}`,
  crossOrigin: 'anonymous'
});
</code></pre>
</div>

## Raster tiles XYZ (Mercator XYZ)

Raster tiles (Mercator XYZ) are loaded with [XYZ](https://openlayers.org/en/latest/apidoc/module-ol_source_XYZ-XYZ.html) function. Start your code with the following starter:

<div class="tab-content cdn-steps" markdown="1">
<pre><code class="language-html"><!--
  <!DOCTYPE html>
  <html>
    <head>
      <meta name="viewport" content="initial-scale=1,maximum-scale=1,user-scalable=no" />
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/ol@/ol.css">
      <script src="https://cdn.jsdelivr.net/npm/ol@/dist/ol.js"></script>
      <style>
        #map {position: absolute; top: 0; right: 0; bottom: 0; left: 0;}
      </style>
    </head>
    <body>
      <div id="map">
        <a href="https://www.maptiler.com" style="position:absolute;left:10px;bottom:10px;z-index:999;"></a>
      </div>
      <p><a href="https://www.maptiler.com/copyright/" target="_blank">© MapTiler</a> <a href="https://www.openstreetmap.org/copyright" target="_blank">© OpenStreetMap contributors</a></p>
      <script>
        const key = 'YOUR_MAPTILER_API_KEY_HERE';
        const source = new ol.source.XYZ({
          url: `https://api.maptiler.com/maps/streets-v4/{z}/{x}/{y}.png?key=${key}`,
          tileSize: 512,
          crossOrigin: 'anonymous'
        });

        const attribution = new ol.control.Attribution({
          collapsible: false,
        });

        const map = new ol.Map({
          layers: [
            new ol.layer.Tile({
              source: source
            })
          ],
          controls: ol.control.defaults.defaults({attribution: false}).extend([attribution]),
          target: 'map',
          view: new ol.View({
            constrainResolution: true,
            center: ol.proj.fromLonLat([0, 0]),
            zoom: 2
          })
        });
      </script>
    </body>

  </html>
--></code></pre>
</div>

<div class="tab-content bundler-steps" markdown="1">
<pre><code class="language-js"><!--
import Map from 'ol/Map.js';
import View from 'ol/View.js';
import TileLayer from 'ol/layer/Tile.js';
import Attribution from 'ol/control/Attribution.js';
import XYZ from 'ol/source/XYZ.js';
import { defaults as defaultControls } from 'ol/control/defaults.js';
import { fromLonLat } from 'ol/proj.js';
import 'ol/ol.css';

const key = 'YOUR_MAPTILER_API_KEY_HERE';
const source = new XYZ({
url: `https://api.maptiler.com/maps/streets-v4/{z}/{x}/{y}.png?key=${key}`,
tileSize: 512,
crossOrigin: 'anonymous'
});

const attribution = new Attribution({
collapsible: false,
});

const map = new Map({
layers: [
new TileLayer({
source: source
})
],
controls: defaultControls({attribution: false}).extend([attribution]),
target: 'map',
view: new View({
constrainResolution: true,
center: fromLonLat([0, 0]),
zoom: 2
})
});
--></code></pre>

</div>



Use **256x256** raster tiles for compatibility with certain libraries. To use the 256px tiles you must use this URL in your layer

<pre><code class="language-http">
  `https://api.maptiler.com/maps/streets-v4/256/{z}/{x}/{y}.png?key=${key}`
</code></pre>

Example of 256x256 raster tiles

<div class="tab-content cdn-steps" markdown="1">
<pre><code class="language-js">
const source = new ol.source.XYZ({
  url: `https://api.maptiler.com/maps/streets-v4/256/{z}/{x}/{y}.png?key=${key}`,
  crossOrigin: 'anonymous'
});
</code></pre>
</div>

<div class="tab-content bundler-steps" markdown="1">
<pre><code class="language-js">
const source = new XYZ({
  url: `https://api.maptiler.com/maps/streets-v4/256/{z}/{x}/{y}.png?key=${key}`,
  crossOrigin: 'anonymous'
});
</code></pre>
</div>

### Summary

The two ways of working with raster layers are very similar, the advantages of using TileJson (**recommended option**) are that we have more information associated with the data source (metadata) and if the service provider changes any metadata our application will always be synchronized and working.

