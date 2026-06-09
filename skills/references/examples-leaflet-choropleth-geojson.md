# Source: https://docs.maptiler.com/leaflet/examples/choropleth-geojson/

# Display a choropleth Map from GeoJSON

This tutorial shows you how to add a styled GeoJSON overlay to your map, adjust the placement of labels, display a popup on click, and create a map legend. We'll use GeoJSON data from EUROSTAT that includes countries with attributes. To use the same data, [download the sample dataset of average age at first marriage](/sdk-js/assets/Mean_age_of_women_at_first_marriage_in_2019.geojson).

1. Include the [Leaflet-AJAX plugin](https://github.com/calvinmetcalf/leaflet-ajax){:target="_blank" rel="noopener"} JavaScript file in the `<head>` of your HTML file. To add a GeoJSON from an external URL to Leaflet, we will need to use the `Leaflet-AJAX plugin`.

<pre class="line-numbers" data-start="7" data-line-offset="6" data-line="8"><code class="language-html"><!--

<script src="https://unpkg.com/leaflet@/dist/leaflet.js"></script>

<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet-ajax/2.1.0/leaflet.ajax.min.js" crossorigin="anonymous" referrerpolicy="no-referrer"></script>

<style>

--></code></pre>

</div>

1. Install [Leaflet-AJAX plugin](https://github.com/calvinmetcalf/leaflet-ajax){:target="_blank" rel="noopener"} packages. They make it possible to add a GeoJSON from an external URL to Leaflet.

<pre><code class="language-bash"><!--

npm install --save leaflet-ajax

--></code></pre>

1. Import the new modules in your JavaScript file (Example: main.js) to add the new functionality.

<pre class="line-numbers" data-line="2"><code class="language-js"><!--

import L from 'leaflet';

import 'leaflet-ajax';

--></code></pre>

</div>

<div class="tab-common-content" markdown="1">

1. Add the GeoJSON layer. With Leaflet-AJAX it`s possible to fetch GeoJSON data hosted on MapTiler (check out the [How to upload GeoJSON](/guides/maps-apis/maps-platform/prepare-geojson-with-attributes-for-choropleth-map-and-upload-geojson-to-maptiler-cloud#PrepareGeoJSONwithattributesforchoroplethmapanduploadGeoJSONtoMapTilerCloud-UploadGeoJSONtoMapTilerCloud){:target="_blank" rel="noopener"} tutorial). The GeoJSON example uses data from Eurostat's Marriage Indicators dataset, filtered to show only countries that have available data on women's mean age at first marriage in 2019. If you want to use the same sample data, [download the dataset](/sdk-js/assets/Mean_age_of_women_at_first_marriage_in_2019.geojson).

<pre class="line-numbers" data-start="27" data-line-offset="26"><code class="language-js"><!--

const geojson = new L.GeoJSON.AJAX(`https://api.maptiler.com/data/YOUR_CUSTOM_MAP_ID/features.json?key=${key}`,{}).addTo(map);

--></code></pre>

1. Create the functions to get the style based on the age attribute.

<pre class="line-numbers" data-start="27" data-line-offset="26"><code class="language-js"><!--

function getColor(age) {

return age > 30 ? '#8c2d04' :

age > 29  ? '#d94801' :

age > 28  ? '#f16913' :

age > 27  ? '#fd8d3c' :

age > 26  ? '#fdae6b' :

age > 25  ? '#fdd0a2' :

age > 24  ? '#fee6ce' :

'#fff5eb';

}

function getStyle(feature) {

return {

weight: 1, // size of outline

opacity: 1, // outline opacity

color: 'black', // color of outline

fillOpacity: 1,

fillColor: getColor(feature.properties.age),

};

}

--></code></pre>

1. Change the `style` property of the layer.

<pre class="line-numbers" data-start="45" data-line-offset="44" data-line="46"><code class="language-js"><!--

const geojson = new L.GeoJSON.AJAX(`https://api.maptiler.com/data/YOUR_CUSTOM_MAP_ID/features.json?key=${key}`,{

style: getStyle

}).addTo(map);

--></code></pre>

1. Create a function to display a popup when clicking on the GeoJSON layer and show the information of the age attribute.

<pre class="line-numbers" data-start="45" data-line-offset="44"><code class="language-js"><!--

function popup(feature, layer){

layer.bindPopup(`<h3>Average age of </br> women at first marriage</br> in 2019</h3><p>${feature.properties.age}</p>`)

}

--></code></pre>

1. Display a popup when clicking on the GeoJSON layer.

<pre class="line-numbers" data-start="47" data-line-offset="46" data-line="48"><code class="language-js"><!--

const geojson = new L.GeoJSON.AJAX(`https://api.maptiler.com/data/YOUR_CUSTOM_MAP_ID/features.json?key=${key}`,{

onEachFeature:popup,

style: getStyle

}).addTo(map);

--></code></pre>

</div>

1. Create a map legend.

<pre class="line-numbers" data-start="1" data-line-offset="0" data-line="11-32, 40-50"><code class="language-html"><!--

<!DOCTYPE html>

<html>

<head>

<meta name="viewport" content="initial-scale=1,maximum-scale=1,user-scalable=no" />

<title>Display a choropleth Map from GeoJSON</title>

<link rel="stylesheet" href="https://unpkg.com/leaflet@/dist/leaflet.css" />

<script src="https://unpkg.com/leaflet@/dist/leaflet.js"></script>

<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet-ajax/2.1.0/leaflet.ajax.min.js" crossorigin="anonymous" referrerpolicy="no-referrer"></script>

<style>

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

z-index: 800;

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

</style>

</head>

<body>

<div id="map">

<a href="https://www.maptiler.com" style="position:absolute;left:10px;bottom:10px;z-index:999;"></a>

</div>

<p><a href="https://www.maptiler.com/copyright/" target="_blank">&copy; MapTiler</a> <a href="https://www.openstreetmap.org/copyright" target="_blank">&copy; OpenStreetMap contributors</a></p>

<div id="state-legend" class="legend">

<h4>Mean age of </br> women at first marriage </br> in 2019 </h4>

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

</div>

1. Add the map legend style code to your `css` file.

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

z-index: 800;

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

1. Create the map legend in your `html` file.

<pre><code class="language-html"><!--

<div id="state-legend" class="legend">

<h4>Mean age of </br> women at first marriage </br> in 2019</h4>

<div><span style="background-color: #fff5eb"></span>23</div>

<div><span style="background-color: #fee6ce"></span>24</div>

<div><span style="background-color: #fdd0a2"></span>25</div>

<div><span style="background-color: #fdae6b"></span>26</div>

<div><span style="background-color: #fd8d3c"></span>27</div>

<div><span style="background-color: #f16913"></span>28</div>

<div><span style="background-color: #d94801"></span>29</div>

<div><span style="background-color: #8c2d04"></span>30</div>

</div>

--></code></pre>

</div>

<div class="tab-common-content" markdown="1">

Now you have a basic choropleth map. It doesn't include country labels on the top of our GeoJSON layer, so it might lack context. If you want to add the labels, continue with the workflow below.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.createPane("labels");
  map.getPane("labels").style.zIndex = 550;
  map.getPane("labels").style.pointerEvents = "none";

  const labels = L.tileLayer(`https://api.maptiler.com/maps/YOUR_ONLY_LABEL_MAP_ID/{z}/{x}/{y}.png?key=${key}`, { //style URL
    tileSize: 512,
    zoomOffset: -1,
    minZoom: 1,
    attribution: "\u003ca href=\"https://www.maptiler.com/copyright/\" target=\"_blank\"\u003e\u0026copy; MapTiler\u003c/a\u003e \u003ca href=\"https://www.openstreetmap.org/copyright\" target=\"_blank\"\u003e\u0026copy; OpenStreetMap contributors\u003c/a\u003e",
    crossOrigin: true,
    pane: 'labels'
  }).addTo(map);


  function getColor(age) {
    return age > 30 ? '#8c2d04' :
      age > 29 ? '#d94801' :
        age > 28 ? '#f16913' :
          age > 27 ? '#fd8d3c' :
            age > 26 ? '#fdae6b' :
              age > 25 ? '#fdd0a2' :
                age > 24 ? '#fee6ce' :
                  '#fff5eb';
  }
  function getStyle(feature) {
    return {
      weight: 1, //size of outline
      opacity: 1, //outline opacity
      color: 'black', //colour of outline
      fillOpacity: 1,
      fillColor: getColor(feature.properties.age),
    };
  }
  function popup(feature, layer) {
    layer.bindPopup(`<h3>Average age of </br> women at first marriage</br> in 2019</h3><p>${feature.properties.age}</p>`)
  }
  const geojson = new L.GeoJSON.AJAX(`https://api.maptiler.com/data/55336072-ef0f-4cb5-8671-b8d6ebbb0a05/features.json?key=${key}`, {
    onEachFeature: popup,
    style: getStyle
  }).addTo(map);
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Display a choropleth Map from GeoJSON</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <script src="https://cdn.maptiler.com/leaflet-maptilersdk/v4.1.0/leaflet-maptilersdk.umd.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet-ajax/2.1.0/leaflet.ajax.min.js"></script>
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
          const layer = L.tileLayer(`https://api.maptiler.com/maps/YOUR_NO_LABEL_MAP_ID/{z}/{x}/{y}.png?key=${key}`, {
            tileSize: 512,
            zoomOffset: -1,
            minZoom: 1,
            attribution: "\u003ca href=\"https://www.maptiler.com/copyright/\" target=\"_blank\"\u003e\u0026copy; MapTiler\u003c/a\u003e \u003ca href=\"https://www.openstreetmap.org/copyright\" target=\"_blank\"\u003e\u0026copy; OpenStreetMap contributors\u003c/a\u003e",
            crossOrigin: true
          }).addTo(map);

          map.createPane("labels");
          map.getPane("labels").style.zIndex = 550;
          map.getPane("labels").style.pointerEvents = "none";

          const labels = L.tileLayer(`https://api.maptiler.com/maps/YOUR_ONLY_LABEL_MAP_ID/{z}/{x}/{y}.png?key=${key}`, { //style URL
            tileSize: 512,
            zoomOffset: -1,
            minZoom: 1,
            attribution: "\u003ca href=\"https://www.maptiler.com/copyright/\" target=\"_blank\"\u003e\u0026copy; MapTiler\u003c/a\u003e \u003ca href=\"https://www.openstreetmap.org/copyright\" target=\"_blank\"\u003e\u0026copy; OpenStreetMap contributors\u003c/a\u003e",
            crossOrigin: true,
            pane: 'labels'
          }).addTo(map);


          function getColor(age) {
            return age > 30 ? '#8c2d04' :
              age > 29 ? '#d94801' :
                age > 28 ? '#f16913' :
                  age > 27 ? '#fd8d3c' :
                    age > 26 ? '#fdae6b' :
                      age > 25 ? '#fdd0a2' :
                        age > 24 ? '#fee6ce' :
                          '#fff5eb';
          }
          function getStyle(feature) {
            return {
              weight: 1, //size of outline
              opacity: 1, //outline opacity
              color: 'black', //colour of outline
              fillOpacity: 1,
              fillColor: getColor(feature.properties.age),
            };
          }
          function popup(feature, layer) {
            layer.bindPopup(`<h3>Average age of </br> women at first marriage</br> in 2019</h3><p>${feature.properties.age}</p>`)
          }
          const geojson = new L.GeoJSON.AJAX(`https://api.maptiler.com/data/55336072-ef0f-4cb5-8671-b8d6ebbb0a05/features.json?key=${key}`, {
            onEachFeature: popup,
            style: getStyle
          }).addTo(map);
    </script>
</body>
</html>
```
