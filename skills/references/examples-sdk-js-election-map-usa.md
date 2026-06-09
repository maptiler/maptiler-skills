# Source: https://docs.maptiler.com/sdk-js/examples/election-map-usa/

# US election map

This tutorial demonstrates how to make a map of US election results. You can also:

* Read about [election mapping with MapTiler](https://www.maptiler.com/elections/)

* See a [full screen Demo](https://labs.maptiler.com/showcase/election-map-us/index.html#3/35.78/-98.73)

In this tutorial, we will create a map to show the results of the 2020 elections in the US. We have obtained the data from [Hardvard Dataverse](https://dataverse.harvard.edu/dataverse/medsl_president). To use this data in our application we have transformed the downloaded CSV files into JSON. Here you can download the transformed JSON files [2020 president by state](./2020-president.json) y [2020 president by county](./2020-county-president.json)

<sup>Click on the map to get the election results. Zoom in to view results by county</sup>

<div class="tab-common-content" markdown="1">

1. Add an event handler for the map `ready` event. You will add code to create your map in this handler.

<pre class="line-numbers" data-start="25" data-line-offset="24" data-line="25-27"><code class="language-js"><!--

map.on('ready', async () => {

});

--></code></pre>

1. Add the [MapTiler countries](https://www.maptiler.com/countries/) data source.

<pre class="line-numbers" data-start="25" data-line-offset="24" data-line="26-29"><code class="language-js"><!--

map.on('ready', async () => {

map.addSource('countries', {

type: 'vector',

url: `https://api.maptiler.com/tiles/countries/tiles.json`

});

});

--></code></pre>

1. Find the id of the first symbol (text) layer in the map style. This is useful for adding polygon or line layers below the map labels.

<pre class="line-numbers" data-start="25" data-line-offset="24" data-line="31,35-39"><code class="language-js"><!--

map.on('ready', async () => {

map.addSource('countries', {

type: 'vector',

url: `https://api.maptiler.com/tiles/countries/tiles.json`

});

const firstSymbolId = findFirstSymbolLayer(map);

});

function findFirstSymbolLayer() {

const layers = map.getStyle().layers;

const firstSymbolId = layers.find(layer => layer.type === 'symbol').id;

return firstSymbolId;

}

--></code></pre>

1. Add the US state's layer

<pre class="line-numbers" data-start="25" data-line-offset="24" data-line="33-52"><code class="language-js"><!--

map.on('ready', async () => {

map.addSource('countries', {

type: 'vector',

url: `https://api.maptiler.com/tiles/countries/tiles.json`

});

const firstSymbolId = findFirstSymbolLayer(map);

map.addLayer(

{

'id': 'states',

'source': 'countries',

'source-layer': 'administrative',

'type': 'fill',

'maxzoom': 7,

'filter': [

'all',

['==', 'level', 1],

['==', 'level_0', 'US']

],

'paint': {

'fill-opacity': 1,

'fill-outline-color': '#fff',

'fill-color': '#DEDEDE',

}

},

firstSymbolId

);

});

--></code></pre>

1. Load the US election results data by states

<pre class="line-numbers" data-start="17" data-line-offset="16" data-line="17"><code class="language-js"><!--

let resultsStates;

maptilersdk.config.apiKey = 'YOUR_MAPTILER_API_KEY_HERE';

--></code></pre>

`...`

<pre class="line-numbers" data-start="55" data-line-offset="54" data-line="55"><code class="language-js"><!--

resultsStates = await getStatesResults();

--></code></pre>

`...`

<pre class="line-numbers" data-start="65" data-line-offset="64" data-line="65-69"><code class="language-js"><!--

async function getStatesResults() {

const response = await fetch("/sdk-js/examples/election-map-usa/2020-president.json");

const data = await response.json();

return data;

}

--></code></pre>

1. Add the election result data to the states layer features. We will use the `sourcedata` event to know when the data loading into the map is finished.

<pre class="line-numbers" data-start="17" data-line-offset="16" data-line="18-22"><code class="language-js"><!--

let resultsStates;

const colors = {

republicans: '#D61822',

democrats: '#0A3B7E',

nodata: '#DEDEDE'

}

--></code></pre>

`...`

<pre class="line-numbers" data-start="60" data-line-offset="59" data-line="62"><code class="language-js"><!--

resultsStates = await getStatesResults();

map.on('sourcedata', getSourceData);

--></code></pre>

`...`

<pre class="line-numbers" data-start="78" data-line-offset="77" data-line="78-186"><code class="language-js"><!--

async function getSourceData(e) {

if (e.isSourceLoaded && e.dataType === 'source') {

const {sourceId} = e;

// Do something when the source has finished loading

if (sourceId === 'countries') {

map.off('sourcedata', getSourceData);

await updatePolygonFeatures();

map.redraw();

//map.panBy([0,0]);

}

}

}

async function updatePolygonFeatures() {

const features = map.queryRenderedFeatures({layers:['states']});

const filteredFeatutes = filterFeaturesNoFeatureState(features, map);

filteredFeatutes.forEach(item => {

const resultsData = resultsStates;

const source = {

source: item.source,

sourceLayer: item.sourceLayer

}

addResultToFeature(item, resultsData, source, map);

});

}

function filterFeaturesNoFeatureState(features, map) {

const noStateFeatures = features.filter(item => {

const fState = map.getFeatureState({

source: item.source,

sourceLayer: item.sourceLayer,

id: item.id,

});

return !Object.keys(fState).length

});

return noStateFeatures

}

function addResultToFeature(feature, resultsData, source, map){

const code = getCode(feature);

const result = resultsData[code];

if (!result) return;

const {winner, winner_percentage, loser_percentage} = getWinner(result);

if (source) {

const fState = map.getFeatureState({

...source,

id: feature.id,

});

if (!fState?.winner) {

map.setFeatureState({

...source,

id: feature.id,

}, {

totalvotes: result.totalvotes,

trump: result.trump,

biden: result.biden,

winner: winner,

winner_percentage: winner_percentage,

loser_percentage: loser_percentage

});

}

} else {

const {properties} = feature;

feature.properties = {...properties,

totalvotes: result.totalvotes,

trump: result.trump,

biden: result.biden,

winner: winner,

winner_percentage: winner_percentage,

loser_percentage: loser_percentage

}

}

}

function getCode(feature) {

if (feature?.properties?.ste_stusps_code || feature?.properties?.coty_code) {

return feature?.properties?.ste_stusps_code || feature?.properties?.coty_code.replace(/^\(1:|\)$/g, "").replace(/^0+/, "");

} else {

return feature.properties.code.replace('US-','').replace(/^0+/, "");

}

}

function getWinner(result){

if (!result) return {winner: '', winner_percentage: 0};

if (parseInt(result.trump) > parseInt(result.biden)) {

return {winner: 'trump',

winner_percentage: percentage(result.trump, result.totalvotes),

loser_percentage: percentage(result.biden, result.totalvotes)}

} else {

return {winner: 'biden',

winner_percentage: percentage(result.biden, result.totalvotes),

loser_percentage: percentage(result.trump, result.totalvotes)

}

}

}

function percentage(partialValue, totalValue) {

return Math.round((100 * partialValue) / totalValue);

}

function getStyleColorByParty() {

return ['case',

['==', ['feature-state', 'winner'], 'biden'],

colors.democrats,

['==', ['feature-state', 'winner'], 'trump'],

colors.republicans,

colors.nodata

];

}

--></code></pre>

1. Change the US state's layer `fill-color` to the color of the winning party.

<pre class="line-numbers" data-start="39" data-line-offset="38" data-line="54"><code class="language-js"><!--

map.addLayer(

{

'id': 'states',

'source': 'countries',

'source-layer': 'administrative',

'type': 'fill',

'maxzoom': 7,

'filter': [

'all',

['==', 'level', 1],

['==', 'level_0', 'US']

],

'paint': {

'fill-opacity': 1,

'fill-outline-color': '#fff',

'fill-color': 'getStyleColorByParty(),

}

},

firstSymbolId

);

--></code></pre>

1. Reload the page to see the map with the states colored according to the winner.

1. In the previous step, we have assigned the election results to the states. We've only done this for the states that are visible on the map. If we move the map towards Alaska we will see that the state remains in gray (it does not have any electoral results assigned). To avoid this we are going to use the `move` and `idle` events to assign the results to the rest of the states as we move around the map.

<pre class="line-numbers" data-start="62" data-line-offset="61" data-line="64-71"><code class="language-js"><!--

map.on('sourcedata', getSourceData);

map.on('move', (e) => {

updatePolygonFeatures();

});

// just before the map enters an "idle" state.

map.on('idle', function() {

updatePolygonFeatures();

});

--></code></pre>

1. The last thing we will do is use the map's `click` event to show the election results corresponding to the state where the user clicks.

<pre class="line-numbers" data-start="69" data-line-offset="68" data-line="73-78"><code class="language-js"><!--

map.on('idle', function() {

updatePolygonFeatures();

});

map.on('click', (e) => {

const features = map.queryRenderedFeatures(e.point, {layers: ['states']});

if (features.length){

showInfo(e, features[0], map, popup);

}

});

--></code></pre>

1. To display the information we will use a popup.

<pre class="line-numbers" data-start="30" data-line-offset="29" data-line="30"><code class="language-js"><!--

const popup = new maptilersdk.Popup({closeOnClick: false}).setLngLat([0, 0]);

--></code></pre>

1. We will create the popup content with the `showInfo` function. The information displayed is the name of the state, a table showing the results according to the candidates and a graph showing the percentages of votes obtained and the winner's margin of victory.

<pre class="line-numbers" data-start="221" data-line-offset="220" data-line="221-316"><code class="language-js"><!--

function showInfo(e, feature, map, popup) {

const {lng, lat} = e.lngLat;

const info = [];

if (feature?.properties?.name) {

info.push(`<h2 class="pop-header">${feature.properties.name}</h2>`);

}

const {state} = feature;

if (state.winner === 'trump') {

state.loser_percentage = percentage(state.biden, state.totalvotes);

} else  {

state.loser_percentage = percentage(state.trump, state.totalvotes);

}

state.margin = state.winner_percentage - state.loser_percentage;

const data = {};

if (state.winner === 'trump') {

data.winner = {

name: 'Donald J. Trump',

votes: state.trump,

pct: state.winner_percentage

}

data.loser = {

name: 'Joseph R. Biden',

votes: state.biden,

pct: state.loser_percentage

}

} else {

data.winner = {

name: 'Joseph R. Biden',

votes: state.biden,

pct: state.winner_percentage

}

data.loser = {

name: 'Donald J. Trump',

votes: state.trump,

pct: state.loser_percentage

}

}

data.margin = state.margin;

info.push(`<div class="popup-results">

<div class="table">

<table>

<thead>

<tr>

<td>Candidate</td>

<td>Votes</td>

<td>%.</td>

</tr>

</thead>

<tbody>

<tr>

<td class="name">

${data.winner.name}

</td>

<td class="votes">

${data.winner.votes}

</td>

<td class="pct">

${data.winner.pct}

</td>

</tr>

<tr>

<td class="name">

${data.loser.name}

</td>

<td class="votes">

${data.loser.votes}

</td>

<td class="pct">

${data.loser.pct}

</td>

</tr>

</tbody>

</table>

</div>

</div>`);

info.push(`<div class="chart">

<div class="margin ${state.winner === 'trump'? 'rep' : 'dem'}">

<div>${data.margin}</div>

<div>Margin</div>

</div>

</div>`);

const html = info.join("");

popup.setLngLat([lng, lat])

.setHTML(html)

.addTo(map);

const svg = createChart(data, state.winner);

const charContainer = document.querySelector(".chart");

charContainer.appendChild(svg);

}

--></code></pre>

1. To create the graph we need to load the d3.js library.

<pre class="line-numbers" data-start="9" data-line-offset="8" data-line="9"><code class="language-html"><!--

<script src="https://cdn.jsdelivr.net/npm/d3@"></script>

--></code></pre>

1. Create the graph.

<pre class="line-numbers" data-start="319" data-line-offset="318" data-line="319-390"><code class="language-js"><!--

function createChart(results, winner) {

const data = [

{votes: results.winner.pct, init: 0},

{votes: results.loser.pct, init: 0},

{votes: 0, init: 100},

["votes", "init"]

]

const width = 700;

const height = Math.min(width, width / 2);

const outerRadius = height / 2 - 10;

const innerRadius = outerRadius * 0.75;

const tau = 2 * Math.PI;

const color = function(i) {

if (i === 0) {

if (winner === 'trump') {

return colors.republicans

} else {

return colors.democrats

}

} else if (i === 1) {

if (winner === 'trump') {

return colors.democrats

} else {

return colors.republicans

}

} else {

return colors.nodata

}

};

const svg = d3.create("svg")

.attr("viewBox", [-width/2, -height/2, width, height]);

const arc = d3.arc()

.innerRadius(innerRadius)

.outerRadius(outerRadius);

const pie = d3.pie().sort(null).value((d) => {

return d["init"]

});

const path = svg.datum(data).selectAll("path")

.data(pie)

.join("path")

.attr("fill", (d, i) => {

return color(i)

})

.attr("d", arc)

.each(function(d) { this._current = d; }); // store the initial angles

function change(value) {

pie.value((d) => d[value]); // change the value function

path.data(pie); // compute the new angles

path.transition().duration(750).attrTween("d", arcTween); // redraw the arcs

}

// Store the displayed angles in _current.

// Then, interpolate from _current to the new angles.

// During the transition, _current is updated in-place by d3.interpolate.

function arcTween(a) {

const i = d3.interpolate(this._current, a);

this._current = i(0);

return (t) => arc(i(t));

}

setTimeout(() => {

change('votes');

}, 300);

// Return the svg node to be displayed.

return Object.assign(svg.node(), {change});

}

--></code></pre>

1. Finally, style the information displayed in the popup so that it is more attractive and easier to understand.

<pre class="line-numbers" data-start="13" data-line-offset="12" data-line="13-98"><code class="language-css"><!--

.pop-header {

font-family: "Noto Sans", "Ubuntu", sans-serif;

font-size: 24px;

font-weight: 500;

}

.popup-results {

display: flex;

}

.maplibregl-popup {

max-width: unset !important;

}

.maplibregl-popup-close-button {

font-size: 24px;

padding: 26px;

}

.maplibregl-popup-content {

padding: 26px;

border-radius: 8px;

}

.chart {

position: relative;

text-align: center;

}

.margin {

display: flex;

flex-direction: column;

justify-items: center;

align-content: center;

font-size: 20px;

position: absolute;

top: 50%;

left: 50%;

transform: translate(-50%, -50%);

font-family: "Noto Sans", "Ubuntu", sans-serif;

}

.margin div:nth-child(2) {

color: #aeb6c7;

text-transform: uppercase;

margin: auto;

font-size: 0.7rem;

}

.margin div:nth-child(1) {

margin: auto;

font-weight: 600;

font-size: 1rem;

}

.margin.rep div:nth-child(1) {

color: #b51800;

}

.margin.dem div:nth-child(1) {

color: #005689;

}

.margin div:nth-child(1)::after {

content: '%';

}

.popup-results table {

width: 200px;

font-family: "Noto Sans", "Ubuntu", sans-serif;

}

.popup-results table thead tr {

color: #aeb6c7;

text-transform: uppercase;

border-color: #dfe1e6;

}

.popup-results table td:nth-child(2) {

text-align: right;

padding-right: 10px;

}

.popup-results table td:nth-child(3) {

text-align: right;

padding-right: 5px;

}

.popup-results table tbody tr {

border-color: #dfe1e6;

}

.popup-results table tbody td:first-child {

padding-right: 10px;

width: 75px;

}

.popup-results table tbody td:nth-child(3) {

font-weight: 600;

text-align: right;

}

.popup-results table tbody td:nth-child(3)::after {

content: '%';

}

--></code></pre>

1. Reload the map and click on a state to see the election results.

1. Congratulations, you have made a map that shows the US election results by state.

</div>

<div class="tab-content cdn-steps" markdown="1">

</div>

Below we will explain the steps to add the results by county to the map.

<div class='border rounded-3 my-1 accordion-item' id='optional-code' aria-expanded='false'>

<div class='bg-lighter rounded-3'>

<a role='button' data-bs-toggle='collapse' data-bs-target='#optionalCode' aria-expanded='false' aria-controls='optionalCode' class='collapsed'>

<span class='px-2 py-1 h6 text-secondary d-block m-0'>Look the steps to add the results by county

<span class='float-end collapse-arrow'>

<svg version='1.1' xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'>

<use href='/styles/style/icon/icon.svg#keyboard_arrow_down'></use>

</svg>

</span>

</span>

</a>

</div>

<div id='optionalCode' class='' aria-labelledby='optionalCode' data-parent='#accordion'>

<div class='card-body px-2'>

<ol>

<li>

Add the US counties layer

<pre class="line-numbers" data-start="124" data-line-offset="123" data-line="124-144"><code class="language-js"><!--

map.addLayer(

{

'id': 'county',

'source': 'countries',

'source-layer': 'administrative',

'type': 'fill',

'minzoom': 5,

'filter': [

'all',

['==', 'level', 2],

['==', 'level_0', 'US']

],

'paint': {

'fill-opacity': 1,

'fill-outline-color': '#262626',

'fill-color': getStyleColorByParty(),

}

},

firstSymbolId

);

--></code></pre>

</li>

<li>

Load the US election results data by county

<pre class="line-numbers" data-start="102" data-line-offset="101" data-line="102"><code class="language-js"><!--

let resultsCounty;

--></code></pre>

<code class="language-textplain">...</code>

<pre class="line-numbers" data-start="169" data-line-offset="168" data-line="169"><code class="language-js"><!--

resultsCounty = await getCountiesResults();

--></code></pre>

<code class="language-textplain">...</code>

<pre class="line-numbers" data-start="203" data-line-offset="202" data-line="203-207"><code class="language-js"><!--

async function getCountiesResults() {

const response = await fetch("/sdk-js/examples/election-map-usa/2020-county-president.json");

const data = await response.json();

return data;

}

--></code></pre>

</li>

<li>

Add the election result data to the county layer features.

<pre class="line-numbers" data-start="222" data-line-offset="221" data-line="223,226"><code class="language-js"><!--

async function updatePolygonFeatures() {

const features = map.queryRenderedFeatures({layers:['states', 'county']});

const filteredFeatutes = filterFeaturesNoFeatureState(features, map);

filteredFeatutes.forEach(item => {

const resultsData = (item.layer.id === 'states') ? resultsStates : resultsCounty;

const source = {

source: item.source,

sourceLayer: item.sourceLayer

}

addResultToFeature(item, resultsData, source, map);

});

}

--></code></pre>

</li>

<li>

Show the election results corresponding to the county where the user clicks.

<pre class="line-numbers" data-start="182" data-line-offset="181" data-line="183"><code class="language-js"><!--

map.on('click', (e) => {

const features = map.queryRenderedFeatures(e.point, {layers: ['states', 'county']});

if (features.length){

showInfo(e, features[0], map, popup);

}

});

--></code></pre>

</li>

<li>

Animate the transition between the state and county visualization.

<pre class="line-numbers" data-start="147" data-line-offset="146" data-line="163"><code class="language-js"><!--

map.addLayer(

{

'id': 'states',

'source': 'countries',

'source-layer': 'administrative',

'type': 'fill',

'maxzoom': 7,

'filter': [

'all',

['==', 'level', 1],

['==', 'level_0', 'US']

],

'paint': {

'fill-opacity': 1,

'fill-outline-color': '#fff',

'fill-color': getStyleColorByParty(),

'fill-opacity-transition': { duration: 300 }

}

},

firstSymbolId

);

--></code></pre>

<code class="language-textplain">...</code>

<pre class="line-numbers" data-start="190" data-line-offset="189" data-line="190-204"><code class="language-js"><!--

map.on('zoom', (e) => {

if (map.getZoom() >= 6) {

if (map.getPaintProperty('states', 'fill-opacity') === 1) {

map.setPaintProperty('states', 'fill-opacity', 0);

setTimeout(() => {

map.setLayoutProperty('states', 'visibility', 'none');

},400);

}

} else {

if (map.getPaintProperty('states', 'fill-opacity') === 0) {

map.setLayoutProperty('states', 'visibility', 'visible');

map.setPaintProperty('states', 'fill-opacity', 1);

}

}

});

--></code></pre>

</li>

<li>

Congratulations, you have made a map that shows the US election results by state and county.

</li>

</ol>

</div>

<div class="tab-content cdn-steps" markdown="1">

</div>

</div>

</div>

<script defer>

setTimeout(() => {

const myCollapse = document.getElementById('optionalCode');

myCollapse.classList.add('collapse');

}, 1000);

</script>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
let resultsStates;
      const colors = {
        republicans: '#D61822',
        democrats: '#0A3B7E',
        nodata: '#DEDEDE' 
      }
        container: 'map', // container's id or the HTML element to render the map
        style: maptilersdk.MapStyle.DATAVIZ.LIGHT,
        center: [-96.05, 36.79], // starting position [lng, lat]
        zoom: 4, // starting zoom
      });
      const popup = new maptilersdk.Popup({closeOnClick: false}).setLngLat([0, 0]);

      map.on('load', async () => {
        map.addSource('countries', {
          type: 'vector',
          url: `https://api.maptiler.com/tiles/countries/tiles.json`
        });

        const firstSymbolId = findFirstSymbolLayer(map);

        map.addLayer(
          {
            'id': 'states',
            'source': 'countries',
            'source-layer': 'administrative',
            'type': 'fill',
            'maxzoom': 7,
            'filter': [
              'all',
              ['==', 'level', 1],
              ['==', 'level_0', 'US']
            ],
            'paint': {
              'fill-opacity': 1,
              'fill-outline-color': '#fff',
              'fill-color': getStyleColorByParty(),
            }
          },
          firstSymbolId
        );

        resultsStates = await getStatesResults();

        map.on('sourcedata', getSourceData);

        map.on('move', (e) => {
          updatePolygonFeatures();
        });

        // just before the map enters an "idle" state.
        map.on('idle', function() {
          updatePolygonFeatures();
        });

        map.on('click', (e) => {
          const features = map.queryRenderedFeatures(e.point, {layers: ['states']});
          if (features.length){
            showInfo(e, features[0], map, popup);
          }
        });

      });

      function findFirstSymbolLayer() {
        const layers = map.getStyle().layers;
        const firstSymbolId = layers.find(layer => layer.type === 'symbol').id;
        return firstSymbolId;
      }

      async function getStatesResults() {
        const response = await fetch("https://docs.maptiler.com/sdk-js/examples/election-map-usa/2020-president.json");
        const data = await response.json();
        return data;
      }

      async function getSourceData(e) {
        if (e.isSourceLoaded && e.dataType === 'source') {
          const {sourceId} = e;
          // Do something when the source has finished loading
          if (sourceId === 'countries') {
            map.off('sourcedata', getSourceData);
            await updatePolygonFeatures();
            map.redraw();
            //map.panBy([0,0]);
          }
        }
      }

      async function updatePolygonFeatures() {
        const features = map.queryRenderedFeatures({layers:['states']});
        const filteredFeatutes = filterFeaturesNoFeatureState(features, map);
        filteredFeatutes.forEach(item => {
          const resultsData = resultsStates;
          const source = {
            source: item.source,
            sourceLayer: item.sourceLayer
          }
          addResultToFeature(item, resultsData, source, map);
        });
      }

      function filterFeaturesNoFeatureState(features, map) {
        const noStateFeatures = features.filter(item => {
          const fState = map.getFeatureState({
            source: item.source,
            sourceLayer: item.sourceLayer,
            id: item.id,
          });
          return !Object.keys(fState).length
        });
        return noStateFeatures
      }

      function addResultToFeature(feature, resultsData, source, map){
        const code = getCode(feature);
        const result = resultsData[code];
        if (!result) return;
        const {winner, winner_percentage, loser_percentage} = getWinner(result);
        if (source) {
          const fState = map.getFeatureState({
            ...source,
            id: feature.id,
          });
          if (!fState?.winner) {
            map.setFeatureState({
              ...source,
              id: feature.id,
            }, {
              totalvotes: result.totalvotes,
              trump: result.trump,
              biden: result.biden,
              winner: winner,
              winner_percentage: winner_percentage,
              loser_percentage: loser_percentage
            });
          }
        } else {
          const {properties} = feature;
          feature.properties = {...properties, 
            totalvotes: result.totalvotes,
            trump: result.trump,
            biden: result.biden,
            winner: winner,
            winner_percentage: winner_percentage,
            loser_percentage: loser_percentage
          }
        }
      }

      function getCode(feature) {
        if (feature?.properties?.ste_stusps_code || feature?.properties?.coty_code) {
          return feature?.properties?.ste_stusps_code || feature?.properties?.coty_code.replace(/^\(1:|\)$/g, "").replace(/^0+/, "");
        } else {
          return feature.properties.code.replace('US-','').replace(/^0+/, "");
        }
      }

      function getWinner(result){
        if (!result) return {winner: '', winner_percentage: 0};
        if (parseInt(result.trump) > parseInt(result.biden)) {
          return {winner: 'trump', 
            winner_percentage: percentage(result.trump, result.totalvotes), 
            loser_percentage: percentage(result.biden, result.totalvotes)}
        } else {
          return {winner: 'biden', 
            winner_percentage: percentage(result.biden, result.totalvotes),
            loser_percentage: percentage(result.trump, result.totalvotes)
          }
        }
      }

      function percentage(partialValue, totalValue) {
        return Math.round((100 * partialValue) / totalValue);
      }

      function getStyleColorByParty() {
        return ['case',
          ['==', ['feature-state', 'winner'], 'biden'],
          colors.democrats,
          ['==', ['feature-state', 'winner'], 'trump'],
          colors.republicans,
          colors.nodata
        ];
      }

      function showInfo(e, feature, map, popup) {
        const {lng, lat} = e.lngLat;
        const info = [];
        if (feature?.properties?.name) {
          info.push(`<h2 class="pop-header">${feature.properties.name}</h2>`);
        }
        const {state} = feature;
        if (state.winner === 'trump') {
          state.loser_percentage = percentage(state.biden, state.totalvotes);
        } else  {
          state.loser_percentage = percentage(state.trump, state.totalvotes);
        }
        state.margin = state.winner_percentage - state.loser_percentage;
        const data = {};
        if (state.winner === 'trump') {
          data.winner = {
            name: 'Donald J. Trump',
            votes: state.trump,
            pct: state.winner_percentage
          }
          data.loser = {
            name: 'Joseph R. Biden',
            votes: state.biden,
            pct: state.loser_percentage
          }
        } else {
          data.winner = {
            name: 'Joseph R. Biden',
            votes: state.biden,
            pct: state.winner_percentage
          }
          data.loser = {
            name: 'Donald J. Trump',
            votes: state.trump,
            pct: state.loser_percentage
          }
        }
        data.margin = state.margin;

        info.push(`<div class="popup-results">
          <div class="table">
            <table>
                <thead>
                  <tr>
                    <td>Candidate</td>
                    <td>Votes</td>
                    <td>%.</td>
                  </tr>
                </thead>
                <tbody>
                <tr>
                  <td class="name">
                    ${data.winner.name}
                  </td>
                  <td class="votes">
                    ${data.winner.votes}
                  </td>
                  <td class="pct">
                    ${data.winner.pct}
                  </td>
                </tr>
                <tr>
                  <td class="name">
                    ${data.loser.name}
                  </td>
                  <td class="votes">
                    ${data.loser.votes}
                  </td>
                  <td class="pct">
                    ${data.loser.pct}
                  </td>
                </tr>
                </tbody>
            </table>
          </div>
        </div>`);

        info.push(`<div class="chart">
          <div class="margin ${state.winner === 'trump'? 'rep' : 'dem'}">
            <div>${data.margin}</div>  
            <div>Margin</div>
          </div>  
        </div>`);

        const html = info.join("");

        popup.setLngLat([lng, lat])
          .setHTML(html)
          .addTo(map);

        const svg = createChart(data, state.winner);

        const charContainer = document.querySelector(".chart");
        charContainer.appendChild(svg);

      }

      function createChart(results, winner) {
        const data = [
          {votes: results.winner.pct, init: 0},
          {votes: results.loser.pct, init: 0},
          {votes: 0, init: 100},
          ["votes", "init"]
        ]
        const width = 700;
        const height = Math.min(width, width / 2);
        const outerRadius = height / 2 - 10;
        const innerRadius = outerRadius * 0.75;
        const tau = 2 * Math.PI;
        const color = function(i) {
          if (i === 0) {
            if (winner === 'trump') {
              return colors.republicans
            } else {
              return colors.democrats
            }
          } else if (i === 1) {
            if (winner === 'trump') {
              return colors.democrats
            } else {
              return colors.republicans
            }
          } else {
            return colors.nodata
          }
        };

        const svg = d3.create("svg")
            .attr("viewBox", [-width/2, -height/2, width, height]);

        const arc = d3.arc()
              .innerRadius(innerRadius)
              .outerRadius(outerRadius);

        const pie = d3.pie().sort(null).value((d) => {
          return d["init"]
        });

        const path = svg.datum(data).selectAll("path")
            .data(pie)
          .join("path")
            .attr("fill", (d, i) => {
              return color(i)
            })
            .attr("d", arc)
            .each(function(d) { this._current = d; }); // store the initial angles

        function change(value) {
          pie.value((d) => d[value]); // change the value function
          path.data(pie); // compute the new angles
          path.transition().duration(750).attrTween("d", arcTween); // redraw the arcs
        }

        // Store the displayed angles in _current.
        // Then, interpolate from _current to the new angles.
        // During the transition, _current is updated in-place by d3.interpolate.
        function arcTween(a) {
          const i = d3.interpolate(this._current, a);
          this._current = i(0);
          return (t) => arc(i(t));
        }

        setTimeout(() => {
          change('votes');
        }, 300);

        // Return the svg node to be displayed.
        return Object.assign(svg.node(), {change});
      }
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>US election map</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <script src="https://cdn.jsdelivr.net/npm/d3@7.9.0"></script>
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
            style: maptilersdk.MapStyle.DATAVIZ.LIGHT,
            center: [-96.05, 36.79],
            zoom: 4
        });

        let resultsStates;
              const colors = {
                republicans: '#D61822',
                democrats: '#0A3B7E',
                nodata: '#DEDEDE' 
              }
                container: 'map', // container's id or the HTML element to render the map
                style: maptilersdk.MapStyle.DATAVIZ.LIGHT,
                center: [-96.05, 36.79], // starting position [lng, lat]
                zoom: 4, // starting zoom
              });
              const popup = new maptilersdk.Popup({closeOnClick: false}).setLngLat([0, 0]);

              map.on('load', async () => {
                map.addSource('countries', {
                  type: 'vector',
                  url: `https://api.maptiler.com/tiles/countries/tiles.json`
                });

                const firstSymbolId = findFirstSymbolLayer(map);

                map.addLayer(
                  {
                    'id': 'states',
                    'source': 'countries',
                    'source-layer': 'administrative',
                    'type': 'fill',
                    'maxzoom': 7,
                    'filter': [
                      'all',
                      ['==', 'level', 1],
                      ['==', 'level_0', 'US']
                    ],
                    'paint': {
                      'fill-opacity': 1,
                      'fill-outline-color': '#fff',
                      'fill-color': getStyleColorByParty(),
                    }
                  },
                  firstSymbolId
                );

                resultsStates = await getStatesResults();

                map.on('sourcedata', getSourceData);

                map.on('move', (e) => {
                  updatePolygonFeatures();
                });

                // just before the map enters an "idle" state.
                map.on('idle', function() {
                  updatePolygonFeatures();
                });

                map.on('click', (e) => {
                  const features = map.queryRenderedFeatures(e.point, {layers: ['states']});
                  if (features.length){
                    showInfo(e, features[0], map, popup);
                  }
                });

              });

              function findFirstSymbolLayer() {
                const layers = map.getStyle().layers;
                const firstSymbolId = layers.find(layer => layer.type === 'symbol').id;
                return firstSymbolId;
              }

              async function getStatesResults() {
                const response = await fetch("https://docs.maptiler.com/sdk-js/examples/election-map-usa/2020-president.json");
                const data = await response.json();
                return data;
              }

              async function getSourceData(e) {
                if (e.isSourceLoaded && e.dataType === 'source') {
                  const {sourceId} = e;
                  // Do something when the source has finished loading
                  if (sourceId === 'countries') {
                    map.off('sourcedata', getSourceData);
                    await updatePolygonFeatures();
                    map.redraw();
                    //map.panBy([0,0]);
                  }
                }
              }

              async function updatePolygonFeatures() {
                const features = map.queryRenderedFeatures({layers:['states']});
                const filteredFeatutes = filterFeaturesNoFeatureState(features, map);
                filteredFeatutes.forEach(item => {
                  const resultsData = resultsStates;
                  const source = {
                    source: item.source,
                    sourceLayer: item.sourceLayer
                  }
                  addResultToFeature(item, resultsData, source, map);
                });
              }

              function filterFeaturesNoFeatureState(features, map) {
                const noStateFeatures = features.filter(item => {
                  const fState = map.getFeatureState({
                    source: item.source,
                    sourceLayer: item.sourceLayer,
                    id: item.id,
                  });
                  return !Object.keys(fState).length
                });
                return noStateFeatures
              }

              function addResultToFeature(feature, resultsData, source, map){
                const code = getCode(feature);
                const result = resultsData[code];
                if (!result) return;
                const {winner, winner_percentage, loser_percentage} = getWinner(result);
                if (source) {
                  const fState = map.getFeatureState({
                    ...source,
                    id: feature.id,
                  });
                  if (!fState?.winner) {
                    map.setFeatureState({
                      ...source,
                      id: feature.id,
                    }, {
                      totalvotes: result.totalvotes,
                      trump: result.trump,
                      biden: result.biden,
                      winner: winner,
                      winner_percentage: winner_percentage,
                      loser_percentage: loser_percentage
                    });
                  }
                } else {
                  const {properties} = feature;
                  feature.properties = {...properties, 
                    totalvotes: result.totalvotes,
                    trump: result.trump,
                    biden: result.biden,
                    winner: winner,
                    winner_percentage: winner_percentage,
                    loser_percentage: loser_percentage
                  }
                }
              }

              function getCode(feature) {
                if (feature?.properties?.ste_stusps_code || feature?.properties?.coty_code) {
                  return feature?.properties?.ste_stusps_code || feature?.properties?.coty_code.replace(/^\(1:|\)$/g, "").replace(/^0+/, "");
                } else {
                  return feature.properties.code.replace('US-','').replace(/^0+/, "");
                }
              }

              function getWinner(result){
                if (!result) return {winner: '', winner_percentage: 0};
                if (parseInt(result.trump) > parseInt(result.biden)) {
                  return {winner: 'trump', 
                    winner_percentage: percentage(result.trump, result.totalvotes), 
                    loser_percentage: percentage(result.biden, result.totalvotes)}
                } else {
                  return {winner: 'biden', 
                    winner_percentage: percentage(result.biden, result.totalvotes),
                    loser_percentage: percentage(result.trump, result.totalvotes)
                  }
                }
              }

              function percentage(partialValue, totalValue) {
                return Math.round((100 * partialValue) / totalValue);
              }

              function getStyleColorByParty() {
                return ['case',
                  ['==', ['feature-state', 'winner'], 'biden'],
                  colors.democrats,
                  ['==', ['feature-state', 'winner'], 'trump'],
                  colors.republicans,
                  colors.nodata
                ];
              }

              function showInfo(e, feature, map, popup) {
                const {lng, lat} = e.lngLat;
                const info = [];
                if (feature?.properties?.name) {
                  info.push(`<h2 class="pop-header">${feature.properties.name}</h2>`);
                }
                const {state} = feature;
                if (state.winner === 'trump') {
                  state.loser_percentage = percentage(state.biden, state.totalvotes);
                } else  {
                  state.loser_percentage = percentage(state.trump, state.totalvotes);
                }
                state.margin = state.winner_percentage - state.loser_percentage;
                const data = {};
                if (state.winner === 'trump') {
                  data.winner = {
                    name: 'Donald J. Trump',
                    votes: state.trump,
                    pct: state.winner_percentage
                  }
                  data.loser = {
                    name: 'Joseph R. Biden',
                    votes: state.biden,
                    pct: state.loser_percentage
                  }
                } else {
                  data.winner = {
                    name: 'Joseph R. Biden',
                    votes: state.biden,
                    pct: state.winner_percentage
                  }
                  data.loser = {
                    name: 'Donald J. Trump',
                    votes: state.trump,
                    pct: state.loser_percentage
                  }
                }
                data.margin = state.margin;

                info.push(`<div class="popup-results">
                  <div class="table">
                    <table>
                        <thead>
                          <tr>
                            <td>Candidate</td>
                            <td>Votes</td>
                            <td>%.</td>
                          </tr>
                        </thead>
                        <tbody>
                        <tr>
                          <td class="name">
                            ${data.winner.name}
                          </td>
                          <td class="votes">
                            ${data.winner.votes}
                          </td>
                          <td class="pct">
                            ${data.winner.pct}
                          </td>
                        </tr>
                        <tr>
                          <td class="name">
                            ${data.loser.name}
                          </td>
                          <td class="votes">
                            ${data.loser.votes}
                          </td>
                          <td class="pct">
                            ${data.loser.pct}
                          </td>
                        </tr>
                        </tbody>
                    </table>
                  </div>
                </div>`);

                info.push(`<div class="chart">
                  <div class="margin ${state.winner === 'trump'? 'rep' : 'dem'}">
                    <div>${data.margin}</div>  
                    <div>Margin</div>
                  </div>  
                </div>`);

                const html = info.join("");

                popup.setLngLat([lng, lat])
                  .setHTML(html)
                  .addTo(map);

                const svg = createChart(data, state.winner);

                const charContainer = document.querySelector(".chart");
                charContainer.appendChild(svg);

              }

              function createChart(results, winner) {
                const data = [
                  {votes: results.winner.pct, init: 0},
                  {votes: results.loser.pct, init: 0},
                  {votes: 0, init: 100},
                  ["votes", "init"]
                ]
                const width = 700;
                const height = Math.min(width, width / 2);
                const outerRadius = height / 2 - 10;
                const innerRadius = outerRadius * 0.75;
                const tau = 2 * Math.PI;
                const color = function(i) {
                  if (i === 0) {
                    if (winner === 'trump') {
                      return colors.republicans
                    } else {
                      return colors.democrats
                    }
                  } else if (i === 1) {
                    if (winner === 'trump') {
                      return colors.democrats
                    } else {
                      return colors.republicans
                    }
                  } else {
                    return colors.nodata
                  }
                };

                const svg = d3.create("svg")
                    .attr("viewBox", [-width/2, -height/2, width, height]);

                const arc = d3.arc()
                      .innerRadius(innerRadius)
                      .outerRadius(outerRadius);

                const pie = d3.pie().sort(null).value((d) => {
                  return d["init"]
                });

                const path = svg.datum(data).selectAll("path")
                    .data(pie)
                  .join("path")
                    .attr("fill", (d, i) => {
                      return color(i)
                    })
                    .attr("d", arc)
                    .each(function(d) { this._current = d; }); // store the initial angles

                function change(value) {
                  pie.value((d) => d[value]); // change the value function
                  path.data(pie); // compute the new angles
                  path.transition().duration(750).attrTween("d", arcTween); // redraw the arcs
                }

                // Store the displayed angles in _current.
                // Then, interpolate from _current to the new angles.
                // During the transition, _current is updated in-place by d3.interpolate.
                function arcTween(a) {
                  const i = d3.interpolate(this._current, a);
                  this._current = i(0);
                  return (t) => arc(i(t));
                }

                setTimeout(() => {
                  change('votes');
                }, 300);

                // Return the svg node to be displayed.
                return Object.assign(svg.node(), {change});
              }
    </script>
</body>
</html>
```
