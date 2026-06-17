# Source: https://docs.maptiler.com/openlayers/examples/choropleth-geojson/

# Display a choropleth Map from GeoJSON

This tutorial will walk you through the process of adding a styled GeoJSON overlay to your map, displaying a popup on click, and creating a map legend. To demonstrate, we will be using GeoJSON formatted data from EUROSTAT that includes countries with attributes. Download the [sample data for average age at first marriage](/sdk-js/assets/Mean_age_of_women_at_first_marriage_in_2019.geojson).

1. Add the GeoJSON layer. The following snippet creates GeoJSON layer hosted on MapTiler (check out the [How to Upload GeoJSON to MapTiler](/guides/maps-apis/maps-platform/prepare-geojson-with-attributes-for-choropleth-map-and-upload-geojson-to-maptiler-cloud#PrepareGeoJSONwithattributesforchoroplethmapanduploadGeoJSONtoMapTilerCloud-UploadGeoJSONtoMapTilerCloud){:target="\_blank" rel="noopener"} tutorial). The GeoJSON used in the example contains Marriage indicators data from EUROSTAT. The dataset was filtered to just countries with some value of mean age of women at first marriage in 2019. Download the [sample data for average age at first marriage](/sdk-js/assets/Mean_age_of_women_at_first_marriage_in_2019.geojson)

<pre class="line-numbers" data-start="39" data-line-offset="38" data-line="42-48"><code class="language-js"><!--

zoom: 3 // starting zoom

})

});

const geojson = new ol.layer.Vector({

source: new ol.source.Vector({

format: new ol.format.GeoJSON(),

url: `https://api.maptiler.com/data/YOUR_CUSTOM_MAP_ID/features.json?key=${key}`,

}),

});

map.addLayer(geojson);

--></code></pre>

1. Create the functions to get the style based on the age attribute.

<pre class="line-numbers" data-start="39" data-line-offset="38" data-line="42-63"><code class="language-js"><!--

zoom: 3 // starting zoom

})

});

const styles = function(feature,resolution) {

if (feature.get('age') >= 30) {color = '#8c2d04' ;}

else if (feature.get('age') >= 29 ){color ='#d94801';}

else if (feature.get('age') >= 28 ){color ='#f16913';}

else if (feature.get('age') >= 27 ){color ='#fd8d3c';}

else if (feature.get('age') >= 26 ){color ='#fdae6b';}

else if (feature.get('age') >= 25 ){color ='#fdd0a2';}

else if (feature.get('age') >= 24 ){color ='#fee6ce';}

else {color = '#fff5eb';}

return  [

new ol.style.Style({

stroke: new ol.style.Stroke({

color: 'black',

width: 0.7,

}),

fill: new ol.style.Fill({

color: color,

}),

}),

]

};

const geojson = new ol.layer.Vector({

--></code></pre>

1. Create a choropleth map based on the age attribute. Change the `style` property of the layer.

<pre class="line-numbers" data-start="64" data-line-offset="63" data-line="69"><code class="language-js"><!--

const geojson = new ol.layer.Vector({

source: new ol.source.Vector({

format: new ol.format.GeoJSON(),

url: `https://api.maptiler.com/data/YOUR_CUSTOM_MAP_ID/features.json?key=${key}`,

}),

style: styles

});

--></code></pre>

1. Create the popup `html` element.

<pre class="line-numbers" data-start="13" data-line-offset="12" data-line="15-18"><code class="language-html"><!--

<div id="map">

<a href="https://www.maptiler.com" style="position:absolute;left:10px;bottom:10px;z-index:999;"></a>

<div id="popup" class="ol-popup">

<a href="#" id="popup-closer" class="ol-popup-closer"></a>

<div id="popup-content"></div>

</div>

</div>

--></code></pre>

1. Create the style for the popup

<pre class="line-numbers" data-start="8" data-line-offset="7" data-line="10-50"><code class="language-html"><!--

<style>

.ol-popup {

position: absolute;

background-color: white;

box-shadow: 0 1px 4px rgba(0,0,0,0.2);

padding: 15px;

border-radius: 10px;

border: 1px solid #cccccc;

bottom: 12px;

left: -50px;

min-width: 280px;

}

.ol-popup:after, .ol-popup:before {

top: 100%;

border: solid transparent;

content: " ";

height: 0;

width: 0;

position: absolute;

pointer-events: none;

}

.ol-popup:after {

border-top-color: white;

border-width: 10px;

left: 48px;

margin-left: -10px;

}

.ol-popup:before {

border-top-color: #cccccc;

border-width: 11px;

left: 48px;

margin-left: -11px;

}

.ol-popup-closer {

text-decoration: none;

position: absolute;

top: 2px;

right: 8px;

}

.ol-popup-closer:after {

content: "✖";

}

</style>

--></code></pre>

1. Create the overlay to anchor the popup

<pre class="line-numbers" data-start="63" data-line-offset="62" data-line="65-80"><code class="language-js"><!--

const key = 'YOUR_MAPTILER_API_KEY_HERE';

const container = document.getElementById('popup');

const content = document.getElementById('popup-content');

const closer = document.getElementById('popup-closer');

const overlay = new ol.Overlay({

element: container,

autoPan: {

animation: {

duration: 250,

},

},

});

closer.onclick = function () {

overlay.setPosition(undefined);

closer.blur();

return false;

};

const source = new ol.source.TileJSON({

--></code></pre>

1. Add the overlay to the map

<pre class="line-numbers" data-start="92" data-line-offset="91" data-line="98"><code class="language-js"><!--

const map = new ol.Map({

layers: [

new ol.layer.Tile({

source: source

})

],

overlays: [overlay],

controls: ol.control.defaults.defaults({attribution: false}).extend([attribution]),

target: 'map',

view: new ol.View({

constrainResolution: true,

center: ol.proj.fromLonLat([13.39, 52.51]), // starting position [lng, lat]

zoom: 3 // starting zoom

})

});

--></code></pre>

1. Create a function to display a popup when clicking on the geojson layer and show the information of the age attribute

<pre class="line-numbers" data-start="136" data-line-offset="135" data-line="137-147"><code class="language-js"><!--

map.addLayer(geojson);

map.on('click', function (evt) {

const features = map.getFeaturesAtPixel(evt.pixel);

const feature = features.length ? features[0] : undefined;

if (feature.get('age')) {

const coordinate = evt.coordinate;

content.innerHTML = `<h3>Average age of </br> women at first marriage</h3><p>${feature.get('age')}</p>`;

overlay.setPosition(coordinate);

} else {

overlay.setPosition(undefined);

}

});

--></code></pre>

1. Create a map legend.

<pre class="line-numbers" data-start="54" data-line-offset="53" data-line="61-71"><code class="language-html"><!--

<div id="map">

<a href="https://www.maptiler.com" style="position:absolute;left:10px;bottom:10px;z-index:999;"></a>

<div id="popup" class="ol-popup">

<a href="#" id="popup-closer" class="ol-popup-closer"></a>

<div id="popup-content"></div>

</div>

</div>

<div id="state-legend" class="legend">

<h4>Mean age of </br> women at first marriage </h4>

<div><span style="background-color: #fff5eb"></span>23</div>

<div><span style="background-color: #fee6ce"></span>24</div>

<div><span style="background-color: #fdd0a2"></span>25</div>

<div><span style="background-color: #fdae6b"></span>26</div>

<div><span style="background-color: #fd8d3c"></span>27</div>

<div><span style="background-color: #f16913"></span>28</div>

<div><span style="background-color: #d94801"></span>29</div>

<div><span style="background-color: #8c2d04"></span>30</div>

</div>

<script>

--></code></pre>

1. Create the style for the map legend.

<pre class="line-numbers" data-start="48" data-line-offset="47" data-line="51-74"><code class="language-css"><!--

.ol-popup-closer:after {

content: "✖";

}

.legend {

background-color: #000;

border-radius: 3px;

bottom: 30px;

box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);

color: #fff ;

font: 12px/20px 'Helvetica Neue', Arial, Helvetica, sans-serif;

padding: 10px;

position: absolute;

right: 10px;

z-index: 1;

}

.legend h4 {

margin: 0 0 10px;

}

.legend div span {

border-radius: 50%;

display: inline-block;

height: 10px;

margin-right: 5px;

width: 10px;

}

--></code></pre>

</div>

1. Import the new modules needed to add the new functionality.

<pre class="line-numbers" data-start="1" data-line-offset="0" data-line="4-5, 7-9, 11-12"><code class="language-js">

import Map from 'ol/Map.js';

import View from 'ol/View.js';

import TileLayer from 'ol/layer/Tile.js';

import VectorLayer from 'ol/layer/Vector.js';

import VectorSource from 'ol/source/Vector.js';

import TileJSON from 'ol/source/TileJSON.js';

import Style from 'ol/style/Style.js';

import Fill from 'ol/style/Fill.js';

import Stroke from 'ol/style/Stroke.js';

import Attribution from 'ol/control/Attribution.js';

import GeoJSON from 'ol/format/GeoJSON.js';

import Overlay from 'ol/Overlay.js';

import { defaults as defaultControls } from 'ol/control/defaults.js';

import { fromLonLat } from 'ol/proj.js';

</code></pre>

1. Add the GeoJSON layer. The following snippet creates GeoJSON layer hosted on MapTiler (check out the [How to Upload GeoJSON to MapTiler](/guides/maps-apis/maps-platform/prepare-geojson-with-attributes-for-choropleth-map-and-upload-geojson-to-maptiler-cloud#PrepareGeoJSONwithattributesforchoroplethmapanduploadGeoJSONtoMapTilerCloud-UploadGeoJSONtoMapTilerCloud){:target="\_blank" rel="noopener"} tutorial). The GeoJSON used in the example contains Marriage indicators data from EUROSTAT. The dataset was filtered to just countries with some value of mean age of women at first marriage in 2019. Download the [sample data for average age at first marriage](/sdk-js/assets/Mean_age_of_women_at_first_marriage_in_2019.geojson)

<pre class="line-numbers" data-start="45" data-line-offset="44" data-line="45-51"><code class="language-js"><!--

const geojson = new VectorLayer({

source: new VectorSource({

format: new GeoJSON(),

url: `https://api.maptiler.com/data/YOUR_CUSTOM_MAP_ID/features.json?key=${key}`,

}),

});

map.addLayer(geojson);

--></code></pre>

1. Create the functions to get the style based on the age attribute.

<pre class="line-numbers" data-start="45" data-line-offset="44" data-line="42-66"><code class="language-js"><!--

const styles = function(feature,resolution) {

if (feature.get('age') >= 30) {color = '#8c2d04' ;}

else if (feature.get('age') >= 29 ){color ='#d94801';}

else if (feature.get('age') >= 28 ){color ='#f16913';}

else if (feature.get('age') >= 27 ){color ='#fd8d3c';}

else if (feature.get('age') >= 26 ){color ='#fdae6b';}

else if (feature.get('age') >= 25 ){color ='#fdd0a2';}

else if (feature.get('age') >= 24 ){color ='#fee6ce';}

else {color = '#fff5eb';}

return  [

new ol.style.Style({

stroke: new ol.style.Stroke({

color: 'black',

width: 0.7,

}),

fill: new ol.style.Fill({

color: color,

}),

}),

]

};

--></code></pre>

1. Create a choropleth map based on the age attribute. Change the `style` property of the layer.

<pre class="line-numbers" data-start="68" data-line-offset="67" data-line="73"><code class="language-js"><!--

const geojson = new VectorLayer({

source: new VectorSource({

format: new GeoJSON(),

url: `https://api.maptiler.com/data/YOUR_CUSTOM_MAP_ID/features.json?key=${key}`,

}),

style: styles

});

--></code></pre>

1. Create the popup `html` element. Add the element inside your map container.

<pre><code class="language-html"><!--

<div id="map">

<a href="https://www.maptiler.com" style="position:absolute;left:10px;bottom:10px;z-index:999;"></a>

<div id="popup" class="ol-popup">

<a href="#" id="popup-closer" class="ol-popup-closer"></a>

<div id="popup-content"></div>

</div>

</div>

--></code></pre>

1. Create the style for the popup. Add this lines into the `CSS` file

<pre><code class="language-css"><!--

.ol-popup {

position: absolute;

background-color: white;

box-shadow: 0 1px 4px rgba(0,0,0,0.2);

padding: 15px;

border-radius: 10px;

border: 1px solid #cccccc;

bottom: 12px;

left: -50px;

min-width: 280px;

}

.ol-popup:after, .ol-popup:before {

top: 100%;

border: solid transparent;

content: " ";

height: 0;

width: 0;

position: absolute;

pointer-events: none;

}

.ol-popup:after {

border-top-color: white;

border-width: 10px;

left: 48px;

margin-left: -10px;

}

.ol-popup:before {

border-top-color: #cccccc;

border-width: 11px;

left: 48px;

margin-left: -11px;

}

.ol-popup-closer {

text-decoration: none;

position: absolute;

top: 2px;

right: 8px;

}

.ol-popup-closer:after {

content: "✖";

}

--></code></pre>

1. Create the overlay to anchor the popup

<pre class="line-numbers" data-start="26" data-line-offset="25" data-line="26-41"><code class="language-js"><!--

const container = document.getElementById('popup');

const content = document.getElementById('popup-content');

const closer = document.getElementById('popup-closer');

const overlay = new Overlay({

element: container,

autoPan: {

animation: {

duration: 250,

},

},

});

closer.onclick = function () {

overlay.setPosition(undefined);

closer.blur();

return false;

};

--></code></pre>

1. Add the overlay to the map

<pre class="line-numbers" data-start="49" data-line-offset="48" data-line="55"><code class="language-js"><!--

const map = new Map({

layers: [

new TileLayer({

source: source

})

],

overlays: [overlay],

controls: defaultControls({ attribution: false }).extend([attribution]),

target: 'map',

view: new View({

constrainResolution: true,

center: fromLonLat([13.39, 52.51]), // starting position [lng, lat]

zoom: 3 // starting zoom

})

});

--></code></pre>

1. Create a function to display a popup when clicking on the geojson layer and show the information of the age attribute

<pre class="line-numbers" data-start="97" data-line-offset="98" data-line="97-107"><code class="language-js"><!--

map.on('click', function (evt) {

const features = map.getFeaturesAtPixel(evt.pixel);

const feature = features.length ? features[0] : undefined;

if (feature.get('age')) {

const coordinate = evt.coordinate;

content.innerHTML = `<h3>Average age of </br> women at first marriage</h3><p>${feature.get('age')}</p>`;

overlay.setPosition(coordinate);

} else {

overlay.setPosition(undefined);

}

});

--></code></pre>

1. Create a map legend. Update your `html` file add this lines after the map container.

<pre><code class="language-html"><!--

<div id="state-legend" class="legend">

<h4>Mean age of </br> women at first marriage </h4>

<div><span style="background-color: #fff5eb"></span>23</div>

<div><span style="background-color: #fee6ce"></span>24</div>

<div><span style="background-color: #fdd0a2"></span>25</div>

<div><span style="background-color: #fdae6b"></span>26</div>

<div><span style="background-color: #fd8d3c"></span>27</div>

<div><span style="background-color: #f16913"></span>28</div>

<div><span style="background-color: #d94801"></span>29</div>

<div><span style="background-color: #8c2d04"></span>30</div>

</div>

<script>

--></code></pre>

1. Create the style for the map legend. Add this code in your `CSS` file.

<pre><code class="language-css"><!--

.legend {

background-color: #000;

border-radius: 3px;

bottom: 30px;

box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);

color: #fff ;

font: 12px/20px 'Helvetica Neue', Arial, Helvetica, sans-serif;

padding: 10px;

position: absolute;

right: 10px;

z-index: 1;

}

.legend h4 {

margin: 0 0 10px;

}

.legend div span {

border-radius: 50%;

display: inline-block;

height: 10px;

margin-right: 5px;

width: 10px;

}

--></code></pre>

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const styles = function (feature, resolution) {
      if (feature.get('age') >= 30) { color = '#8c2d04'; }
      else if (feature.get('age') >= 29) { color = '#d94801'; }
      else if (feature.get('age') >= 28) { color = '#f16913'; }
      else if (feature.get('age') >= 27) { color = '#fd8d3c'; }
      else if (feature.get('age') >= 26) { color = '#fdae6b'; }
      else if (feature.get('age') >= 25) { color = '#fdd0a2'; }
      else if (feature.get('age') >= 24) { color = '#fee6ce'; }
      else { color = '#fff5eb'; }

      return [
        new ol.style.Style({
          stroke: new ol.style.Stroke({
            color: 'black',
            width: 0.7,
          }),
          fill: new ol.style.Fill({
            color: color,
          }),
        }),
      ]
    };

    const geojson = new ol.layer.Vector({
      source: new ol.source.Vector({
        format: new ol.format.GeoJSON(),
        url: `https://api.maptiler.com/data/YOUR_CUSTOM_MAP_ID/features.json?key=${key}`,
      }),
      style: styles
    });
    map.addLayer(geojson);

    map.on('click', function (evt) {
      const features = map.getFeaturesAtPixel(evt.pixel);
      const feature = features.length ? features[0] : undefined;
      if (feature && feature.get('age')) {
        const coordinate = evt.coordinate;
        content.innerHTML = `<h3>Average age of </br> women at first marriage</h3><p>${feature.get('age')}</p>`;
        overlay.setPosition(coordinate);
      } else {
        overlay.setPosition(undefined);
      }
    });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Display a choropleth Map from GeoJSON</title>
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

            const container = document.getElementById('popup');
            const content = document.getElementById('popup-content');
            const closer = document.getElementById('popup-closer');
            const overlay = new ol.Overlay({
              element: container,
              autoPan: {
                animation: {
                  duration: 250,
                },
              },
            });
            closer.onclick = function () {
              overlay.setPosition(undefined);
              closer.blur();
              return false;
            };

            const source = new ol.source.TileJSON({
              url: `https://api.maptiler.com/maps/dataviz-v4-dark/tiles.json?key=${key}`,
              tileSize: 512,
              crossOrigin: 'anonymous'
            });

            const map = new ol.Map({
              layers: [
                new ol.layer.Tile({
                  source: source
                })
              ],
              overlays: [overlay],
              controls: ol.control.defaults.defaults({ attribution: false }).extend([attribution]),
              target: 'map',
              view: new ol.View({
                constrainResolution: true,
                center: ol.proj.fromLonLat([13.39, 52.51]), // starting position [lng, lat]
                zoom: 3 // starting zoom
              })
            });

            const styles = function (feature, resolution) {
              if (feature.get('age') >= 30) { color = '#8c2d04'; }
              else if (feature.get('age') >= 29) { color = '#d94801'; }
              else if (feature.get('age') >= 28) { color = '#f16913'; }
              else if (feature.get('age') >= 27) { color = '#fd8d3c'; }
              else if (feature.get('age') >= 26) { color = '#fdae6b'; }
              else if (feature.get('age') >= 25) { color = '#fdd0a2'; }
              else if (feature.get('age') >= 24) { color = '#fee6ce'; }
              else { color = '#fff5eb'; }

              return [
                new ol.style.Style({
                  stroke: new ol.style.Stroke({
                    color: 'black',
                    width: 0.7,
                  }),
                  fill: new ol.style.Fill({
                    color: color,
                  }),
                }),
              ]
            };

            const geojson = new ol.layer.Vector({
              source: new ol.source.Vector({
                format: new ol.format.GeoJSON(),
                url: `https://api.maptiler.com/data/YOUR_CUSTOM_MAP_ID/features.json?key=${key}`,
              }),
              style: styles
            });
            map.addLayer(geojson);

            map.on('click', function (evt) {
              const features = map.getFeaturesAtPixel(evt.pixel);
              const feature = features.length ? features[0] : undefined;
              if (feature && feature.get('age')) {
                const coordinate = evt.coordinate;
                content.innerHTML = `<h3>Average age of </br> women at first marriage</h3><p>${feature.get('age')}</p>`;
                overlay.setPosition(coordinate);
              } else {
                overlay.setPosition(undefined);
              }
            });
    </script>
</body>
</html>
```
