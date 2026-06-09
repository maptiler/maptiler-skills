# Source: https://docs.maptiler.com/openlayers/examples/wmts/

# Display a WMTS map

This tutorial shows how to add an OGC WMTS from MapTiler to your web map using OpenLayers. The easiest way to add a WMTS to a map is to get the configuration information directly from the GetCapabilities response.

1. Create the WMTS capabilities parser.

<pre class="line-numbers" data-start="19" data-line-offset="18" data-line="22"><code class="language-js"><!--

const attribution = new ol.control.Attribution({

collapsible: false,

});

const parser = new ol.format.WMTSCapabilities();

const source = new ol.source.TileJSON({

--></code></pre>

1. Get the WMTS Capabilities information and read it with the parser.

<pre class="line-numbers" data-start="22" data-line-offset="21" data-line="23-32, 54"><code class="language-js"><!--

const parser = new ol.format.WMTSCapabilities();

fetch(`https://api.maptiler.com/maps/streets-v4/WMTSCapabilities.xml?key=${key}`)

.then(function (response) {

return response.text();

})

.then(function (text) {

const result = parser.read(text);

const options = ol.source.WMTS.optionsFromCapabilities(result, {

layer: 'maps/',

matrixSet: 'GoogleMapsCompatible512-z0-22'

});

const source = new ol.source.TileJSON({

url: `https://api.maptiler.com/maps/streets-v4/tiles.json?key=${key}`, // source URL

tileSize: 512,

crossOrigin: 'anonymous'

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

center: ol.proj.fromLonLat([16.62662018, 49.2125578]), // starting position [lng, lat]

zoom: 14 // starting zoom

})

});

});

--></code></pre>

1. Change the `source` to use the WMTS

<pre class="line-numbers" data-start="34" data-line-offset="33" data-line="34-39"><code class="language-js"><!--

const source = new ol.source.WMTS({...options,

attributions: [

'<a href="https://www.maptiler.com/copyright/" target="_blank">© MapTiler</a>',

'<a href="https://www.openstreetmap.org/copyright" target="_blank">© OpenStreetMap contributors</a>'

]

});

--></code></pre>

</div>

1. Import the new modules needed to add the new functionality.

<pre class="line-numbers" data-start="1" data-line-offset="0" data-line="4, 6"><code class="language-js">

import Map from 'ol/Map.js';

import View from 'ol/View.js';

import TileLayer from 'ol/layer/Tile.js';

import WMTS, {optionsFromCapabilities} from 'ol/source/WMTS.js';

import Attribution from 'ol/control/Attribution.js';

import WMTSCapabilities from 'ol/format/WMTSCapabilities.js';

import { defaults as defaultControls } from 'ol/control/defaults.js';

import { fromLonLat } from 'ol/proj.js';

</code></pre>

1. Create the WMTS capabilities parser.

<pre class="line-numbers" data-start="17" data-line-offset="16" data-line="17"><code class="language-js"><!--

const parser = new WMTSCapabilities();

--></code></pre>

1. Get the WMTS Capabilities information and read it with the parser.

<pre class="line-numbers" data-start="17" data-line-offset="16" data-line="18-28, 49"><code class="language-js"><!--

const parser = new WMTSCapabilities();

fetch(`https://api.maptiler.com/maps/streets-v4/WMTSCapabilities.xml?key=${key}`)

.then(function (response) {

return response.text();

})

.then(function (text) {

const result = parser.read(text);

const options = optionsFromCapabilities(result, {

layer: 'maps/',

matrixSet: 'GoogleMapsCompatible512-z0-22'

});

const source = new TileJSON({

url: `https://api.maptiler.com/maps/streets-v4/tiles.json?key=${key}`, // source URL

tileSize: 512,

crossOrigin: 'anonymous'

});

const map = new Map({

layers: [

new Tile({

source: source

})

],

controls: defaultControls({attribution: false}).extend([attribution]),

target: 'map',

view: new View({

constrainResolution: true,

center: fromLonLat([16.62662018, 49.2125578]), // starting position [lng, lat]

zoom: 14 // starting zoom

})

});

});

--></code></pre>

1. Change the `source` to use the WMTS

<pre class="line-numbers" data-start="29" data-line-offset="28" data-line="29-34"><code class="language-js"><!--

const source = new WMTS({...options,

attributions: [

'<a href="https://www.maptiler.com/copyright/" target="_blank">© MapTiler</a>',

'<a href="https://www.openstreetmap.org/copyright" target="_blank">© OpenStreetMap contributors</a>'

]

});

--></code></pre>

</div>

> [!WARNING]

> The WMTS functionality requires at least a FLEX plan subscription. For more information, read about the different [MapTiler plans](https://www.maptiler.com/cloud/pricing/).

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
});
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Display a WMTS map</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/ol@10.9.0/ol.css">
    <script src="https://cdn.jsdelivr.net/npm/ol@10.9.0/dist/ol.js"></script>
    <style>
        body { margin: 0; padding: 0; }
        #map { position: absolute; top: 0; bottom: 0; width: 100%; }
    </style>
</head>
<body>
    <div id="map"></div>
    <script>
        const key = 'YOUR_MAPTILER_API_KEY';

            const attribution = new ol.control.Attribution({
              collapsible: false,
            });

            const parser = new ol.format.WMTSCapabilities();
            fetch(`https://api.maptiler.com/maps/streets-v4/WMTSCapabilities.xml?key=${key}`)
              .then(function (response) {
                return response.text();
              })
              .then(function (text) {
                const result = parser.read(text);
                const options = ol.source.WMTS.optionsFromCapabilities(result, {
                  layer: 'maps/streets-v4',
                  matrixSet: 'GoogleMapsCompatible512-z0-22'
                });

                const source = new ol.source.WMTS({
                  ...options,
                  attributions: [
                    '<a href="https://www.maptiler.com/copyright/" target="_blank">© MapTiler</a>',
                    '<a href="https://www.openstreetmap.org/copyright" target="_blank">© OpenStreetMap contributors</a>'
                  ]
                });

                const map = new ol.Map({
                  layers: [
                    new ol.layer.Tile({
                      source: source
                    })
                  ],
                  controls: ol.control.defaults.defaults({ attribution: false }).extend([attribution]),
                  target: 'map',
                  view: new ol.View({
                    constrainResolution: true,
                    center: ol.proj.fromLonLat([16.62662018, 49.2125578]),
                    zoom: 12
                  })
                });
              });
    </script>
</body>
</html>
```
