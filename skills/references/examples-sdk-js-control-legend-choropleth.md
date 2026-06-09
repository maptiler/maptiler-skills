# Source: https://docs.maptiler.com/sdk-js/examples/control-legend-choropleth/

# Display an interactive choropleth map legend control

This tutorial shows how to display an interactive choropleth map legend control.

Discover the functionality of the legend control by hovering your mouse over the colored boxes in the legend, which allows you to filter the different countries on the map. Additionally, when you hover over a specific country, you will be able to view its population.

<sup>Move the mouse over the colored boxes of the legend to filter the elements of the map. Move the mouse over a country to see the population</sup>

<div class="tab-content cdn-steps" markdown="1">

1. Copy the following code, paste it into your favorite text editor, and save it as a `.html` file. This code is the result of doing steps 1 to 12 of the tutorial [How to create a countries map with your own data](../countries-with-own-data/)

<pre class="line-numbers" data-start="1" data-line-offset="0"><code class="language-html"><!--

<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta http-equiv="X-UA-Compatible" content="IE=edge">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title></title>

<script src="https://cdn.maptiler.com/maptiler-sdk-js//maptiler-sdk.umd.min.js"></script>

<link href="https://cdn.maptiler.com/maptiler-sdk-js//maptiler-sdk.css" rel="stylesheet" />

<style>

body { margin: 0; padding: 0; }

</style>

</head>

<body>

<div id="map"></div>

<script>

const vizData = {

"8":{"name":"Albania","population":2829741},

"40":{"name":"Austria","population":8932664},

"56":{"name":"Belgium","population":11566041},

"100":{"name":"Bulgaria","population":6916548},

"191":{"name":"Croatia","population":4036355},

"196":{"name":"Cyprus","population":896005},

"203":{"name":"Czechia","population":10701777},

"208":{"name":"Denmark","population":5840045},

"233":{"name":"Estonia","population":1330068},

"246":{"name":"Finland","population":5533793},

"250":{"name":"France","population":67439599},

"276":{"name":"Germany","population":83155031},

"300":{"name":"Greece","population":10682547},

"348":{"name":"Hungary","population":9730772},

"352":{"name":"Iceland","population":368792},

"372":{"name":"Ireland","population":5006907},

"380":{"name":"Italy","population":59257566},

"428":{"name":"Latvia","population":1893223},

"440":{"name":"Lithuania","population":2795680},

"442":{"name":"Luxembourg","population":634730},

"499":{"name":"Montenegro","population":620739},

"528":{"name":"Netherlands","population":17475415},

"578":{"name":"Norway","population":5391369},

"616":{"name":"Poland","population":37840001},

"620":{"name":"Portugal","population":10298252},

"642":{"name":"Romania","population":19186201},

"688":{"name":"Serbia","population":6871547},

"703":{"name":"Slovakia","population":5459781},

"705":{"name":"Slovenia","population":2108977},

"724":{"name":"Spain","population":47394223},

"752":{"name":"Sweden","population":10379295},

"756":{"name":"Switzerland","population":8667088},

"792":{"name":"Turkey","population":83614362},

"807":{"name":"North Macedonia","population":2068808}

};

function setStates() {

const countries = map.querySourceFeatures('statesData', {

sourceLayer: 'administrative',

filter: ['all', ['==', 'level', 0]],

});

countries.forEach(country => {

if(country.id && vizData[country.id]) {

map.setFeatureState({

source: 'statesData',

sourceLayer: 'administrative',

id: country.id

}, {

population: vizData[country.id].population

});

}

});

if (countries.length !== 0) {

map.off('data', afterLoad);

}

}

function afterLoad() {

if (map.getSource('statesData') && map.isSourceLoaded('statesData')) {

setStates();

}

}

maptilersdk.config.apiKey = 'YOUR_MAPTILER_API_KEY_HERE';

const map = new maptilersdk.Map({

container: 'map', // container id

style: ,

center: [, ], // starting position [lng, lat]

zoom: , // starting zoom

});

map.on('load', function() {

map.addSource('statesData', {

type: 'vector',

url: `https://api.maptiler.com/tiles/countries/tiles.json`

});

// Find the id of the first symbol layer in the map style

const layers = map.getStyle().layers;

const firstSymbolId = layers.find(layer => layer.type === 'symbol').id;

map.addLayer(

{

'id': 'countries',

'source': 'statesData',

'source-layer': 'administrative',

'type': 'fill',

'filter': ['==', 'level', 0],

'paint': {

'fill-color': '#6B7C93',

'fill-opacity': 1,

'fill-outline-color': '#000'

}

},

firstSymbolId

);

});

map.on('data', afterLoad);

</script>

</body>

</html>

--></code></pre>

1. Include the `chroma-js` JavaScript file in the `<head>` of your HTML file. To create the legend we will use the [chroma-js](https://gka.github.io/chroma.js/){:target="_blank" rel="noopener"} library. We are going to use the library to create the color scale and create the class breaks based on the `vizData`.

<pre><code class="language-html"><!--

<script src="https://cdnjs.cloudflare.com/ajax/libs/chroma-js/2.4.2/chroma.min.js"></script>

--></code></pre>

</div>

<div class="tab-content bundler-steps" markdown="1">

1. Copy the following code, paste it into your favorite text editor, and save it as a `app.js` file. This code is the result of doing steps 1 to 14 of the tutorial [How to create a countries map with your own data](../countries-with-own-data/)

<pre class="line-numbers" data-start="1" data-line-offset="0"><code class="language-js"><!--

import * as maptilersdk from '@maptiler/sdk';

maptilersdk.config.apiKey = 'YOUR_MAPTILER_API_KEY_HERE';

const vizData = {

"8":{"name":"Albania","population":2829741},

"40":{"name":"Austria","population":8932664},

"56":{"name":"Belgium","population":11566041},

"100":{"name":"Bulgaria","population":6916548},

"191":{"name":"Croatia","population":4036355},

"196":{"name":"Cyprus","population":896005},

"203":{"name":"Czechia","population":10701777},

"208":{"name":"Denmark","population":5840045},

"233":{"name":"Estonia","population":1330068},

"246":{"name":"Finland","population":5533793},

"250":{"name":"France","population":67439599},

"276":{"name":"Germany","population":83155031},

"300":{"name":"Greece","population":10682547},

"348":{"name":"Hungary","population":9730772},

"352":{"name":"Iceland","population":368792},

"372":{"name":"Ireland","population":5006907},

"380":{"name":"Italy","population":59257566},

"428":{"name":"Latvia","population":1893223},

"438":{"name":"Liechtenstein","population":39055},

"440":{"name":"Lithuania","population":2795680},

"442":{"name":"Luxembourg","population":634730},

"470":{"name":"Malta","population":516100},

"499":{"name":"Montenegro","population":620739},

"528":{"name":"Netherlands","population":17475415},

"578":{"name":"Norway","population":5391369},

"616":{"name":"Poland","population":37840001},

"620":{"name":"Portugal","population":10298252},

"642":{"name":"Romania","population":19186201},

"688":{"name":"Serbia","population":6871547},

"703":{"name":"Slovakia","population":5459781},

"705":{"name":"Slovenia","population":2108977},

"724":{"name":"Spain","population":47394223},

"752":{"name":"Sweden","population":10379295},

"756":{"name":"Switzerland","population":8667088},

"792":{"name":"Turkey","population":83614362},

"807":{"name":"North Macedonia","population":2068808}

};

function setStates() {

const countries = map.querySourceFeatures('statesData', {

sourceLayer: 'administrative',

filter: ['all', ['==', 'level', 0]],

});

countries.forEach(country => {

if(country.id && vizData[country.id]) {

map.setFeatureState({

source: 'statesData',

sourceLayer: 'administrative',

id: country.id

}, {

population: vizData[country.id].population

});

}

});

if (countries.length !== 0) {

map.off('data', afterLoad);

}

}

function afterLoad() {

if (map.getSource('statesData') && map.isSourceLoaded('statesData')) {

setStates();

}

}

const map = new maptilersdk.Map({

container: 'map', // container's id or the HTML element to render the map

style: maptilersdk.MapStyle.DATAVIZ.LIGHT,

center: [13.39, 52.51], // starting position [lng, lat]

zoom: 2, // starting zoom

});

map.on('load', function() {

map.addSource('statesData', {

type: 'vector',

url: `https://api.maptiler.com/tiles/countries/tiles.json`

});

});

// Find the id of the first symbol layer in the map style

const layers = map.getStyle().layers;

const firstSymbolId = layers.find(layer => layer.type === 'symbol').id;

map.addLayer(

{

'id': 'countries',

'source': 'statesData',

'source-layer': 'administrative',

'type': 'fill',

'filter': ['==', 'level', 0],

'paint': {

'fill-color': '#6B7C93',

'fill-opacity': 1,

'fill-outline-color': '#000'

}

},

firstSymbolId

);

map.on('data', afterLoad);

--></code></pre>

1. Include the `chroma-js` JavaScript file in your app.js file. To create the legend we will use the [chroma-js](https://gka.github.io/chroma.js/){:target="_blank" rel="noopener"} library. We are going to use the library to create the color scale and create the class breaks based on the `vizData`.

Install chroma-js package

<pre><code class="language-bash"><!--

npm i chroma-js

--></code></pre>

Import package into project

<pre class="line-numbers" data-start="1" data-line-offset="0" data-line="2"><code class="language-js"><!--

import chroma from "chroma-js";

--></code></pre>

</div>

<div class="tab-common-content" markdown="1">

1. Get the population data from vizData.

<pre class="line-numbers" data-start="96" data-line-offset="95" data-line="96-99"><code class="language-js"><!--

const populationData = Object.keys(vizData).reduce((agg, id) => {

agg.push(vizData[id]["population"]);

return agg;

}, []);

--></code></pre>

1. Create the data **equidistant** breaks and the scale color. To do these calculations you can use any other library such as [D3.js](https://d3js.org/){:target="_blank" rel="noopener"}.

<pre class="line-numbers" data-start="100" data-line-offset="99" data-line="100-103"><code class="language-js"><!--

//chroma equidistant scale

const limits = chroma.limits(populationData, 'e', 4);

//chroma color scale

const colorScale = chroma.scale(['rgba(222,235,247,1)', 'rgba(49,130,189,1)']).mode('lch').colors(5);

--></code></pre>

1. Create a function to round the limits numbers. Now we have values in our limits matrix that are neither integers nor rounded. This is not a problem in itself, but in this case we want to have the legend with ranges of integers, for example categories between 100 - 1000, 1000 - 5000, etc. and not have ranges with numbers like 354 - 1013, 1013 - 5278, etc.

<pre class="line-numbers" data-start="100" data-line-offset="99" data-line="100-119"><code class="language-js"><!--

function roundDown(num, precision) {

num = parseFloat(num);

if (!precision) return num;

return (Math.floor(num / precision) * precision);

}

function getPrecision(num) {

const digits = parseInt(num).toString().length;

return Math.pow(10, digits-1);

}

function roundLimits(limits) {

return limits.map(num => {

const precision = getPrecision(num);

return roundDown(num, precision);

})

}

//chroma equidistant scale

const limits = roundLimits(chroma.limits(populationData, 'e', 4));

--></code></pre>

1. Create a function to create the choropleth map based on the breaks (limits) and color scale.

<pre class="line-numbers" data-start="122" data-line-offset="121" data-line="122-136"><code class="language-js"><!--

function createPaintColor(limits, colorScale){

const paintColor = ['case',

['!=', ['to-number', ['feature-state', 'population']], 0],

['step',

['feature-state', 'population'],

],

'rgba(0, 0, 0, 0)'

];

for (let i = 1; i < limits.length; i++) {

paintColor[2].push(colorScale[i-1]);

paintColor[2].push(limits[i]);

}

paintColor[2].push(colorScale[limits.length-1]);

return paintColor;

}

--></code></pre>

1. Create a choropleth map based on the population attribute. Change the `fill-color` property of the layer and get the color from the `createPaintColor` function.

<pre class="line-numbers" data-start="137" data-line-offset="136" data-line="145"><code class="language-js"><!--

map.addLayer(

{

'id': 'countries',

'source': 'statesData',

'source-layer': 'administrative',

'type': 'fill',

'filter': ['==', 'level', 0],

'paint': {

'fill-color': createPaintColor(limits, colorScale),

'fill-opacity': 1,

'fill-outline-color': '#000'

}

},

firstSymbolId

);

--></code></pre>

1. Create a file called `legendControl.js` next to your `.html` file. Copy the following code, paste it into the `legendControl.js` file.

<pre class="line-numbers" data-start="1" data-line-offset="0"><code class="language-js"><!--

class choroplethLegendControl {

constructor(options) {

this._options = {...options};

this._container = document.createElement("div");

this._container.classList.add("maplibregl-ctrl");

this._container.classList.add("maplibregl-ctrl-choropleth");

}

onAdd(map) {

this._map = map;

return this._container;

}

onRemove() {

if (!this._map || !this._container) {

return;

}

this._container.parentNode.removeChild(this._container);

this._map = undefined;

delete this._map;

}

}

--></code></pre>

</div>

<div class="tab-content bundler-steps" markdown="1">

1. Export the choroplethLegendControl

<pre class="line-numbers" data-start="21" data-line-offset="20" data-line="21"><code class="language-js"><!--

export { choroplethLegendControl };

--></code></pre>

</div>

<div class="tab-common-content" markdown="1">

1. Add the mouse events listener to the map.

<pre class="line-numbers" data-start="1" data-line-offset="0" data-line="7-8,12-16,19-24,29-30"><code class="language-js"><!--

class choroplethLegendControl {

constructor(options) {

this._options = {...options};

this._container = document.createElement("div");

this._container.classList.add("maplibregl-ctrl");

this._container.classList.add("maplibregl-ctrl-choropleth");

this.mousemove = this._mousemove.bind(this);

this.mouseleave = this._mouseleave.bind(this);

}

onAdd(map) {

this._map = map;

const layer = this._map.getLayer(this._options.layerId);

if (layer) {

this._map.on('mousemove', this._options.layerId, this.mousemove);

this._map.on('mouseleave', this._options.layerId, this.mouseleave);

}

return this._container;

}

_mousemove(e) {

}

_mouseleave() {

}

onRemove() {

if (!this._map || !this._container) {

return;

}

this._map.off('mousemove', this._options.layerId, this.mousemove);

this._map.off('mouseleave', this._options.layerId, this.mouseleave);

this._container.parentNode.removeChild(this._container);

this._map = undefined;

delete this._map;

}

}

--></code></pre>

1. Create the legend html.

<pre class="line-numbers" data-start="1" data-line-offset="0" data-line="7-8,12-16,19-24,29-30"><code class="language-js"><!--

class choroplethLegendControl {

constructor(options) {

this._options = {...options};

this._container = document.createElement("div");

this._container.classList.add("maplibregl-ctrl");

this._container.classList.add("maplibregl-ctrl-choropleth");

this.mousemove = this._mousemove.bind(this);

this.mouseleave = this._mouseleave.bind(this);

}

onAdd(map) {

this._map = map;

const layer = this._map.getLayer(this._options.layerId);

if (layer) {

this._paint = this._map.getPaintProperty(this._options.layerId, 'fill-color');

const labels = [];

const colorScaleLength = this._options.colorScale.length;

for (let i = 0; i < colorScaleLength; i++) {

if (i < colorScaleLength - 1) {

labels.push(`<li><span style="background-color: ${this._options.colorScale[i]}"></span><label>${this._options.limits[i].toLocaleString()} &mdash; ${this._options.limits[i+1].toLocaleString()}</label></li>`)

} else {

labels.push(`<li><span style="background-color: ${this._options.colorScale[i]}"></span><label>${this._options.limits[i].toLocaleString()} +</label></li>`)

}

}

this._container.innerHTML = `<h3>Population<label></label></h3>

<ul style="list-style-type:none;display:flex">${labels.join('')}</ul>

`;

this._map.on('mousemove', this._options.layerId, this.mousemove);

this._map.on('mouseleave', this._options.layerId, this.mouseleave);

}

return this._container;

}

_mousemove(e) {

}

_mouseleave() {

}

onRemove() {

if (!this._map || !this._container) {

return;

}

this._map.off('mousemove', this._options.layerId, this.mousemove);

this._map.off('mouseleave', this._options.layerId, this.mouseleave);

this._container.parentNode.removeChild(this._container);

this._map = undefined;

delete this._map;

}

}

--></code></pre>

1. Create the `choroplethLegendControl` style. Add the choroplethLegendControl style to your stylesheet.

<pre><code class="language-css"><!--

.maplibregl-ctrl-choropleth {

color: #333359;

position: relative;

padding: 6px 8px;

font-family: OpenSans Semibold, OpenSans Regular, OpenSans Italic;

background: white;

box-shadow: 0 0 15px rgb(0 0 0 / 20%);

border-radius: 5px;

bottom: 0;

right: 0;

margin: 10px;

}

.maplibregl-ctrl-choropleth h3 {

margin-block-start: 0;

margin-block-end: 0.5em;

}

.maplibregl-ctrl-choropleth ul {

padding: 0;

margin: 0;

clear: both;

flex-direction: column;

}

.maplibregl-ctrl-choropleth li {

display: inline-flex;

align-items: center;

}

.maplibregl-ctrl-choropleth li.active {

font-weight: 600;

}

.maplibregl-ctrl-choropleth li span {

display: inline-block;

width: 22px;

height: 22px;

cursor: pointer;

margin-right: 5px;

}

--></code></pre>

</div>

<div class="tab-content cdn-steps" markdown="1">

1. Include the `legendControl.js` JavaScript file in the <head> of your HTML file.

<pre><code class="language-html"><!--

<script src="legendControl.js"></script>

--></code></pre>

</div>

<div class="tab-content bundler-steps" markdown="1">

1. Import the `legendControl.js` file into project.

<pre><code class="language-js"><!--

import { choroplethLegendControl } from './legendControl.js';

--></code></pre>

</div>

<div class="tab-common-content" markdown="1">

1. Add the `choroplethLegendControl` to the map.

<pre class="line-numbers" data-start="171" data-line-offset="170" data-line="171-175"><code class="language-js"><!--

map.addControl(new choroplethLegendControl({

layerId: 'countries',

limits: limits,

colorScale: colorScale,

}), 'bottom-left');

--></code></pre>

1. We already have the legend on our map. Now we're going to add some functionality to the legend to make it interactive and allow you to filter items on the map. Back to the `legendControl.js`.

<pre class="line-numbers" data-start="1" data-line-offset="0" data-line="27-31,43-61"><code class="language-js"><!--

class choroplethLegendControl {

constructor(options) {

this._options = {...options};

this._container = document.createElement("div");

this._container.classList.add("maplibregl-ctrl");

this._container.classList.add("maplibregl-ctrl-choropleth");

this.mousemove = this._mousemove.bind(this);

this.mouseleave = this._mouseleave.bind(this);

}

onAdd(map) {

this._map = map;

const layer = this._map.getLayer(this._options.layerId);

if (layer) {

this._paint = this._map.getPaintProperty(this._options.layerId, 'fill-color');

const labels = [];

const colorScaleLength = this._options.colorScale.length;

for (let i = 0; i < colorScaleLength; i++) {

if (i < colorScaleLength - 1) {

labels.push(`<li><span style="background-color: ${this._options.colorScale[i]}"></span><label>${this._options.limits[i].toLocaleString()} &mdash; ${this._options.limits[i+1].toLocaleString()}</label></li>`)

} else {

labels.push(`<li><span style="background-color: ${this._options.colorScale[i]}"></span><label>${this._options.limits[i].toLocaleString()} +</label></li>`)

}

}

this._container.innerHTML = `<h3>Population<label></label></h3>

<ul style="list-style-type:none;display:flex">${labels.join('')}</ul>

`;

const paintCategories = this._container.querySelectorAll('span');

paintCategories.forEach((categorie, index) => {

categorie.addEventListener('mouseover', this.filterByCategorie.bind(this));

categorie.addEventListener('mouseleave', this.cleanFilterByCategorie.bind(this));

});

this._map.on('mousemove', this._options.layerId, this.mousemove);

this._map.on('mouseleave', this._options.layerId, this.mouseleave);

}

return this._container;

}

_mousemove(e) {

}

_mouseleave() {

}

filterByCategorie(e){

const index = [...e.target.parentNode.parentNode.children].indexOf(e.target.parentNode);

const paint = [...this._paint];

if(index < this._options.limits.length-1){

paint[2] = ['case',

['all', ['>=', ['feature-state', 'population'], this._options.limits[index]], ['<', ['feature-state', 'population'], this._options.limits[index+1]]],

this._options.colorScale[index],

'rgba(0, 0, 0, 0)']

}else{

paint[2] = ['case',

['>=', ['feature-state', 'population'], this._options.limits[index]],

this._options.colorScale[index],

'rgba(0, 0, 0, 0)']

}

this._map.setPaintProperty(this._options.layerId, 'fill-color', paint);

}

cleanFilterByCategorie(e){

this._map.setPaintProperty(this._options.layerId, 'fill-color', this._paint);

}

onRemove() {

if (!this._map || !this._container) {

return;

}

this._map.off('mousemove', this._options.layerId, this.mousemove);

this._map.off('mouseleave', this._options.layerId, this.mouseleave);

this._container.parentNode.removeChild(this._container);

this._map = undefined;

delete this._map;

}

}

--></code></pre>

1. Add the functionality to show the information of the selected element on the map in the legend. Hovering over a country with data will display the population in the corresponding category in the legend.

<pre class="line-numbers" data-start="1" data-line-offset="0" data-line="38-42,45,47-83"><code class="language-js"><!--

class choroplethLegendControl {

constructor(options) {

this._options = {...options};

this._container = document.createElement("div");

this._container.classList.add("maplibregl-ctrl");

this._container.classList.add("maplibregl-ctrl-choropleth");

this.mousemove = this._mousemove.bind(this);

this.mouseleave = this._mouseleave.bind(this);

}

onAdd(map) {

this._map = map;

const layer = this._map.getLayer(this._options.layerId);

if (layer) {

this._paint = this._map.getPaintProperty(this._options.layerId, 'fill-color');

const labels = [];

const colorScaleLength = this._options.colorScale.length;

for (let i = 0; i < colorScaleLength; i++) {

if (i < colorScaleLength - 1) {

labels.push(`<li><span style="background-color: ${this._options.colorScale[i]}"></span><label>${this._options.limits[i].toLocaleString()} &mdash; ${this._options.limits[i+1].toLocaleString()}</label></li>`)

} else {

labels.push(`<li><span style="background-color: ${this._options.colorScale[i]}"></span><label>${this._options.limits[i].toLocaleString()} +</label></li>`)

}

}

this._container.innerHTML = `<h3>Population<label></label></h3>

<ul style="list-style-type:none;display:flex">${labels.join('')}</ul>

`;

const paintCategories = this._container.querySelectorAll('span');

paintCategories.forEach((categorie, index) => {

categorie.addEventListener('mouseover', this.filterByCategorie.bind(this));

categorie.addEventListener('mouseleave', this.cleanFilterByCategorie.bind(this));

});

this._map.on('mousemove', this._options.layerId, this.mousemove);

this._map.on('mouseleave', this._options.layerId, this.mouseleave);

}

return this._container;

}

_mousemove(e) {

if (e.features[0]?.state?.population) {

this.legendHighlight(e.features[0]);

} else {

this.clearLegendHighlight();

}

}

_mouseleave() {

this.clearLegendHighlight();

}

legendHighlight(feature) {

if (this._selectedFeature !== feature.id) {

this._map.getCanvas().style.cursor = 'pointer';

const activeCategories = this._container.querySelector('li.active');

this._container.querySelector('h3 > label').textContent = ` (${feature.properties.name})`;

if (activeCategories) {

activeCategories.classList.remove("active");

activeCategories.querySelector('label').textContent = this._activeRange;

}

this._selectedFeature = feature.id;

const population = feature.state.population;

const limitIndex = this._options.limits.findIndex(l => l > population);

const paintCategories = this._container.querySelectorAll('li');

if (limitIndex > 0){

const paintCategory = paintCategories[limitIndex-1];

paintCategory.classList.add("active");

this._activeRange = paintCategory.querySelector('label').textContent;

paintCategory.querySelector('label').textContent = population.toLocaleString();

} else {

const paintCategory = paintCategories[paintCategories.length-1];

paintCategory.classList.add("active");

this._activeRange = paintCategory.querySelector('label').textContent;

paintCategory.querySelector('label').textContent = population.toLocaleString();

}

}

}

clearLegendHighlight() {

this._map.getCanvas().style.cursor = '';

this._selectedFeature = null;

const activeCategories = this._container.querySelector('li.active');

this._container.querySelector('h3 > label').textContent = "";

if (activeCategories) {

activeCategories.classList.remove("active");

activeCategories.querySelector('label').textContent = this._activeRange;

this._activeRange = null;

}

}

filterByCategorie(e){

const index = [...e.target.parentNode.parentNode.children].indexOf(e.target.parentNode);

const paint = [...this._paint];

if(index < this._options.limits.length-1){

paint[2] = ['case',

['all', ['>=', ['feature-state', 'population'], this._options.limits[index]], ['<', ['feature-state', 'population'], this._options.limits[index+1]]],

this._options.colorScale[index],

'rgba(0, 0, 0, 0)']

}else{

paint[2] = ['case',

['>=', ['feature-state', 'population'], this._options.limits[index]],

this._options.colorScale[index],

'rgba(0, 0, 0, 0)']

}

this._map.setPaintProperty(this._options.layerId, 'fill-color', paint);

}

cleanFilterByCategorie(e){

this._map.setPaintProperty(this._options.layerId, 'fill-color', this._paint);

}

onRemove() {

if (!this._map || !this._container) {

return;

}

this._map.off('mousemove', this._options.layerId, this.mousemove);

this._map.off('mouseleave', this._options.layerId, this.mouseleave);

this._container.parentNode.removeChild(this._container);

this._map = undefined;

delete this._map;

}

}

--></code></pre>

1. Create a popup to show the country info. In your `.html` file before creating the legend `choroplethLegendControl` add the following lines:

<pre class="line-numbers" data-start="193" data-line-offset="192" data-line="193-197"><code class="language-js"><!--

// Create a popup, but don't add it to the map yet.

const popup = new maptilersdk.Popup({

closeButton: false,

closeOnClick: false

});

--></code></pre>

1. Add the popup to the `choroplethLegendControl` constructor options.

<pre class="line-numbers" data-start="199" data-line-offset="198" data-line="203"><code class="language-js"><!--

map.addControl(new choroplethLegendControl({

layerId: 'countries',

limits: limits,

colorScale: colorScale,

popup: popup

}), 'bottom-left');

--></code></pre>

1. Showing a popup when hovering over a country with data will show the population information. In the `legendControl.js` file update the `legendHighlight` function. Add de coordinates parameter and popup functionality.

<pre class="line-numbers" data-start="47" data-line-offset="46" data-line="47, 71-79"><code class="language-js"><!--

legendHighlight(feature, coordinates) {

if (this._selectedFeature !== feature.id) {

this._map.getCanvas().style.cursor = 'pointer';

const activeCategories = this._container.querySelector('li.active');

this._container.querySelector('h3 > label').textContent = ` (${feature.properties.name})`;

if (activeCategories) {

activeCategories.classList.remove("active");

activeCategories.querySelector('label').textContent = this._activeRange;

}

this._selectedFeature = feature.id;

const population = feature.state.population;

const limitIndex = this._options.limits.findIndex(l => l > population);

const paintCategories = this._container.querySelectorAll('li');

if (limitIndex > 0){

const paintCategory = paintCategories[limitIndex-1];

paintCategory.classList.add("active");

this._activeRange = paintCategory.querySelector('label').textContent;

paintCategory.querySelector('label').textContent = population.toLocaleString();

} else {

const paintCategory = paintCategories[paintCategories.length-1];

paintCategory.classList.add("active");

this._activeRange = paintCategory.querySelector('label').textContent;

paintCategory.querySelector('label').textContent = population.toLocaleString();

}

if (this._options.popup) {

const description = `<h3 style="text-align: center">${feature.properties.name}</h3>

<span style="background-color: ${this._options.colorScale[limitIndex > 0 ? limitIndex - 1 : this._options.colorScale.length - 1]}; display: inline-block;

width: 22px;

height: 22px;

margin-right: 5px;"></span><label style="vertical-align: super;">${population.toLocaleString()}</label>

`;

this._options.popup.setLngLat(coordinates).setHTML(description).addTo(this._map);

}

}

}

--></code></pre>

1. Hide the popup when move. Update the `clearLegendHighlight` function.

<pre class="line-numbers" data-start="82" data-line-offset="81" data-line="92-94"><code class="language-js"><!--

clearLegendHighlight() {

this._map.getCanvas().style.cursor = '';

this._selectedFeature = null;

const activeCategories = this._container.querySelector('li.active');

this._container.querySelector('h3 > label').textContent = "";

if (activeCategories) {

activeCategories.classList.remove("active");

activeCategories.querySelector('label').textContent = this._activeRange;

this._activeRange = null;

}

if (this._options.popup) {

this._options.popup.remove();

}

}

--></code></pre>

1. Update the `_mousemove` function.

<pre class="line-numbers" data-start="37" data-line-offset="36" data-line="39"><code class="language-js"><!--

_mousemove(e) {

if (e.features[0]?.state?.population) {

this.legendHighlight(e.features[0], e.lngLat);

} else {

this.clearLegendHighlight();

}

}

--></code></pre>

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', function() {
        map.addSource('statesData', {
          type: 'vector',
          url: `https://api.maptiler.com/tiles/countries/tiles.json`
        });

        // Find the id of the first symbol layer in the map style
        const layers = map.getStyle().layers;
        const firstSymbolId = layers.find(layer => layer.type === 'symbol').id;

        map.addLayer(
          {
            'id': 'countries',
            'source': 'statesData',
            'source-layer': 'administrative',
            'type': 'fill',
            'filter': ['==', 'level', 0],
            'paint': {
                'fill-color': createPaintColor(limits, colorScale),
                'fill-opacity': 1,
                'fill-outline-color': '#000'
            }
          },
          firstSymbolId
        );
        
        // Create a popup, but don't add it to the map yet.
        const popup = new maptilersdk.Popup({
            closeButton: false,
            closeOnClick: false
        });

        map.addControl(new choroplethLegendControl({
          layerId: 'countries', 
          limits: limits, 
          colorScale: colorScale,
          popup: popup
        }), 'bottom-left');
      });
      map.on('data', afterLoad);
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Display an interactive choropleth map legend control</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/chroma-js/2.4.2/chroma.min.js"></script>
    <script src="../legendControl.js"></script>
    <style>
        body { margin: 0; padding: 0; }
        #map { position: absolute; top: 0; bottom: 0; width: 100%; }
    </style>
</head>
<body>
    <div id="map"></div>
    <script>
        maptilersdk.config.apiKey = 'YOUR_MAPTILER_API_KEY';

        const map = new maptilersdk.Map({
            container: 'map',
            style: maptilersdk.MapStyle.STREETS,
            center: [13.39, 52.51],
            zoom: 2
        });

        map.on('load', function() {
                map.addSource('statesData', {
                  type: 'vector',
                  url: `https://api.maptiler.com/tiles/countries/tiles.json`
                });

                // Find the id of the first symbol layer in the map style
                const layers = map.getStyle().layers;
                const firstSymbolId = layers.find(layer => layer.type === 'symbol').id;

                map.addLayer(
                  {
                    'id': 'countries',
                    'source': 'statesData',
                    'source-layer': 'administrative',
                    'type': 'fill',
                    'filter': ['==', 'level', 0],
                    'paint': {
                        'fill-color': createPaintColor(limits, colorScale),
                        'fill-opacity': 1,
                        'fill-outline-color': '#000'
                    }
                  },
                  firstSymbolId
                );

                // Create a popup, but don't add it to the map yet.
                const popup = new maptilersdk.Popup({
                    closeButton: false,
                    closeOnClick: false
                });

                map.addControl(new choroplethLegendControl({
                  layerId: 'countries', 
                  limits: limits, 
                  colorScale: colorScale,
                  popup: popup
                }), 'bottom-left');
              });
              map.on('data', afterLoad);
    </script>
</body>
</html>
```
