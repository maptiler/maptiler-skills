# Source: https://docs.maptiler.com/openlayers/examples/how-to-use-openlayers/

# Display a map

This Step-by-Step tutorial shows how to create an OpenLayers map and display it on a web page using MapTiler.

By following these steps, you will be able to harness the power of MapTiler to effortlessly integrate stunning map visuals and functionality into your web applications. Experiment with different map styles, customizations, and functionalities to create an exceptional mapping experience for your web application users.

1. Create a basic HTML file.

<pre class="line-numbers"><code class="language-html"><!--

<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title></title>

<style>

body {

margin: 0;

padding: 0;

}

</style>

</head>

<body>

</body>

<script>

</script>

</html>

--></code></pre>

1.  Include the OpenLayers JavaScript and CSS files in the `<head>` of your HTML file.

<pre class="line-numbers" data-start="7" data-line-offset="6" data-line="7,8"><code class="language-html"><!--

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/ol@/ol.css">

<script src="https://cdn.jsdelivr.net/npm/ol@/dist/ol.js"></script>

<style>

--></code></pre>

1.  Create a `<div>` element with a certain id where you want your map to be.

Add `<div>` tag into your page. This div will be the container where the map will be loaded.

<pre class="line-numbers" data-start="16" data-line-offset="15" data-line="17"><code class="language-html"><!--

<body>

<div id="map"></div>

</body>

--></code></pre>

1.  The div must have non-zero height. Go to the head style section and copy the following lines:

<pre class="line-numbers" data-start="15" data-line-offset="14" data-line="15-20"><code class="language-css">

position: absolute;

top: 0;

bottom: 0;

width: 100%;

}

</code></pre>

1.  Finally, load the map with the style. Go back to the body script section and white:

<pre class="line-numbers" data-start="27" data-line-offset="26" data-line="27-46"><code class="language-js">

const key = 'YOUR_MAPTILER_API_KEY_HERE';

const source = new ol.source.TileJSON({

url: `https://api.maptiler.com/maps/streets-v4/tiles.json?key=${key}`,

tileSize: 512,

crossOrigin: 'anonymous'

});

const map = new ol.Map({

layers: [

new ol.layer.Tile({

source: source

})

],

target: 'map',

view: new ol.View({

constrainResolution: true,

center: ol.proj.fromLonLat([, ]),

zoom:

})

});

</code></pre>

</div>

1. Install the npm package.

<pre><code class="language-bash"><!--

npm install --save ol

--></code></pre>

1.  Create the map style. Add the map style to your stylesheet. The div must have non-zero height.

<pre><code class="language-css">

body {

margin: 0;

padding: 0;

}

position: absolute;

top: 0;

bottom: 0;

width: 100%;

}

</code></pre>

1.  Create a `<div>` element with a certain id where you want your map to be.

Add `<div>` tag into your page. This div will be the container where the map will be loaded.

<pre><code class="language-html"><!--

<div id="map"></div>

--></code></pre>

1.  Include the CSS file.

If you have a bundler that can handle CSS, you can import the CSS from ol/ol.css.

<pre><code class="language-js"><!--

import 'ol/ol.css';

--></code></pre>

> [!INFO]

> Including the CSS file using a `<link>` in the head of the document via the CDN is the easiest way.

>

> ```html

> <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/ol@/dist/ol.js" />

> ```

>

1.  Include the following code in your JavaScript file (Example: main.js).

<pre class="line-numbers"><code class="language-js"><!--

import Map from 'ol/Map.js';

import View from 'ol/View.js';

import TileLayer from 'ol/layer/Tile.js';

import TileJSON from 'ol/source/TileJSON.js';

import { defaults as defaultControls } from 'ol/control/defaults.js';

import { fromLonLat } from 'ol/proj.js';

const key = 'YOUR_MAPTILER_API_KEY_HERE';

const source = new TileJSON({

url: `https://api.maptiler.com/maps/streets-v4/tiles.json?key=${key}`, // source URL

tileSize: 512,

crossOrigin: 'anonymous'

});

const map = new Map({

layers: [

new TileLayer({

source: source

})

],

target: 'map',

view: new View({

constrainResolution: true,

center: fromLonLat([, ]), // starting position [lng, lat]

zoom:  // starting zoom

})

});

--></code></pre>

</div>

<div class="tab-common-content" markdown="1">

1.

</div>

1. Create an attribution control that is not collapsible so that it is always visible.

<pre class="line-numbers" data-start="27" data-line-offset="26" data-line="34, 35, 36"><code class="language-js">

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

target: 'map',

view: new ol.View({

constrainResolution: true,

center: ol.proj.fromLonLat([, ]),

zoom:

})

});

</code></pre>

1. Add the new attribution control to the map. We will modify the default controls on the map so that the attribution is always visible using the non-collapsible attribution control.

<pre class="line-numbers" data-start="38" data-line-offset="37" data-line="44"><code class="language-js">

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

center: ol.proj.fromLonLat([, ]),

zoom:

})

});

</code></pre>

</div>

1. Import the attribution control module

<pre class="line-numbers" data-start="1" data-line-offset="0" data-line="5"><code class="language-js">

import Map from 'ol/Map.js';

import View from 'ol/View.js';

import TileLayer from 'ol/layer/Tile.js';

import TileJSON from 'ol/source/TileJSON.js';

import Attribution from 'ol/control/Attribution.js';

import { defaults as defaultControls } from 'ol/control/defaults.js';

import { fromLonLat } from 'ol/proj.js';

</code></pre>

1. Create an attribution control that is not collapsible so that it is always visible.

<pre class="line-numbers" data-start="9" data-line-offset="8" data-line="11-13"><code class="language-js">

const key = 'YOUR_MAPTILER_API_KEY_HERE';

const attribution = new Attribution({

collapsible: false,

});

const source = new TileJSON({

url: `https://api.maptiler.com/maps/streets-v4/tiles.json?key=${key}`, // source URL

tileSize: 512,

crossOrigin: 'anonymous'

});

const map = new Map({

layers: [

new TileLayer({

source: source

})

],

target: 'map',

view: new View({

constrainResolution: true,

center: fromLonLat([, ]), // starting position [lng, lat]

zoom:  // starting zoom

})

});

</code></pre>

1. Add the new attribution control to the map. We will modify the default controls on the map so that the attribution is always visible using the non-collapsible attribution control.

<pre class="line-numbers" data-start="21" data-line-offset="20" data-line="27"><code class="language-js">

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

center: fromLonLat([, ]), // starting position [lng, lat]

zoom:  // starting zoom

})

});

</code></pre>

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
    <title>Display a map</title>
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

            const source = new ol.source.TileJSON({
              url: `https://api.maptiler.com/maps/streets-v4/tiles.json?key=${key}`,
              tileSize: 512,
              crossOrigin: 'anonymous'
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
                zoom: 14
              })
            });
    </script>
</body>
</html>
```
