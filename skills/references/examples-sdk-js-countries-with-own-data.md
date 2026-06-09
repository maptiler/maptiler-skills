# Source: https://docs.maptiler.com/sdk-js/examples/countries-with-own-data/

# Display a countries choropleth map with your own data

This tutorial demonstrates the process of merging your own personalized data with the [MapTiler Countries](https://www.maptiler.com/countries/){:target="\_blank" rel="noopener"} dataset, allowing you to create a [choropleth map](../choropleth-geojson/). The MapTiler Countries dataset primarily consists of information regarding the administrative divisions of countries and their territories around the world.

For this specific example, we will be creating a choropleth map that showcases the population of some European countries.

<div class="tab-common-content" markdown="1">

1. Add event handler for map `load` event. You will add code to create a vector source and a vector layer in this handler.

<pre class="line-numbers" data-start="24" data-line-offset="23" data-line="24-26"><code class="language-js"><!--

map.on('load', function() {

});

--></code></pre>

1. Create vector source. The following snippet creates vector source for the MapTiler Countries dataset.

<pre class="line-numbers" data-start="24" data-line-offset="23" data-line="25-28"><code class="language-js"><!--

map.on('load', function() {

map.addSource('statesData', {

type: 'vector',

url: `https://api.maptiler.com/tiles/countries/tiles.json`

});

});

--></code></pre>

1. Get the id of the first symbol layer. We want to include the vector layer below the map labels. That means we need to know the id of the first symbol layer so we can include the vector layer before this layer.

<pre class="line-numbers" data-start="29" data-line-offset="28" data-line="29-31"><code class="language-js"><!--

// Find the id of the first symbol layer in the map style

const layers = map.getStyle().layers;

const firstSymbolId = layers.find(layer => layer.type === 'symbol').id;

--></code></pre>

1. Add the vector layer. We need to include `firsSymbolId` to the `map.addLayer` function to display the vector under the maps labels

<pre class="line-numbers" data-start="32" data-line-offset="31" data-line="32-45"><code class="language-js"><!--

map.addLayer(

{

'id': 'countries',

'source': 'statesData',

'source-layer': 'administrative',

'type': 'fill',

'paint': {

'fill-color': '#6B7C93',

'fill-opacity': 1,

'fill-outline-color': '#000'

}

},

firstSymbolId

);

--></code></pre>

1. Filter the data to only show the countries. Add a filter to the layer to only display level 0 items.

<pre class="line-numbers" data-start="32" data-line-offset="31" data-line="38"><code class="language-js"><!--

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

--></code></pre>

1. Prepare your data. Each feature in the dataset has its own identification for pairing. You need to mark your data with the same identifiers as is stored by features. We will use the iso_n3 identifier for countries. Alternatively, you can use one of the properties: name, country codes (ISO A2), or wiki data-id. Check out the [Countries dataset schema](https://docs.maptiler.com/schema/countries/#administrative){:target="\_blank" rel="noopener"} to see the available fields.

<pre class="line-numbers" data-start="17" data-line-offset="16" data-line="17-54"><code class="language-js"><!--

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

--></code></pre>

1. Join the data to coresponding features. Use `querySourceFeatures` to get all features from the layer for visualization. We are also filtering for all countries with `['==', 'level', 0]` using style expressions. The second part of the following code goes throw these features and adds attributes from our data array (vizData) to relevant features.

<pre class="line-numbers" data-start="55" data-line-offset="54" data-line="55-74"><code class="language-js"><!--

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

--></code></pre>

1. Create a function that validates that the country dataset is loaded to call the `setStates` function.

<pre class="line-numbers" data-start="75" data-line-offset="74" data-line="75-79"><code class="language-js"><!--

function afterLoad() {

if (map.getSource('statesData') && map.isSourceLoaded('statesData')) {

setStates();

}

}

--></code></pre>

1. Add event handler for map `data` event. Call the `afterLoad` function

<pre class="line-numbers" data-start="113" data-line-offset="112" data-line="113"><code class="language-js"><!--

map.on('data', afterLoad);

--></code></pre>

1. Create a choropleth map based on the population attribute. Change the `fill-color` property of the layer.

<pre class="line-numbers" data-start="96" data-line-offset="95" data-line="104-110"><code class="language-js"><!--

map.addLayer(

{

'id': 'countries',

'source': 'statesData',

'source-layer': 'administrative',

'type': 'fill',

'filter': ['==', 'level', 0],

'paint': {

'fill-color': ['case',

['!=', ['to-number', ['feature-state', 'population']], 0],

['interpolate', ['linear'], ['feature-state', 'population'],

5000000, 'rgba(222,235,247,1)', 90000000, 'rgba(49,130,189,1)'

],

'rgba(0, 0, 0, 0)'

],

'fill-opacity': 1,

'fill-outline-color': '#000'

}

},

firstSymbolId

);

--></code></pre>

1. Display a popup when clicking on the vector layer and show the information of the age attribute.

<pre class="line-numbers" data-start="120" data-line-offset="119" data-line="120-125"><code class="language-js"><!--

map.on('click', 'countries', function (e) {

new maptilersdk.Popup()

.setLngLat(e.lngLat)

.setHTML(`<h3>Population</h3><p>${e.features[0].state.population.toLocaleString()}</p>`)

.addTo(map);

});

--></code></pre>

1. To make our map more user friendly, we will change the cursor when hovering over a geometry in the vector layer to indicate to the user that they can click on it.

<pre class="line-numbers" data-start="126" data-line-offset="125" data-line="126-134"><code class="language-js"><!--

// Change the cursor to a pointer when the mouse is over the layer.

map.on('mouseenter', 'countries', function () {

map.getCanvas().style.cursor = 'pointer';

});

// Change it back to a pointer when it leaves.

map.on('mouseleave', 'countries', function () {

map.getCanvas().style.cursor = '';

});

--></code></pre>

</div>

<div class="tab-content cdn-steps" markdown="1">

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
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
        container: 'map', // container's id or the HTML element to render the map
        style: maptilersdk.MapStyle.DATAVIZ.LIGHT,
        center: [13.39, 52.51], // starting position [lng, lat]
        zoom: 2, // starting zoom
      });
      map.on('load', function() {
        map.addSource('statesData', {
          type: 'vector',
          url: `https://api.maptiler.com/tiles/countries/tiles.json?`
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
                'fill-color': ['case',
                  ['!=', ['to-number', ['feature-state', 'population']], 0],
                  ['interpolate', ['linear'], ['feature-state', 'population'], 
                    5000000, 'rgba(222,235,247,1)', 90000000, 'rgba(49,130,189,1)'
                  ],
                  'rgba(0, 0, 0, 0)'
                ],
                'fill-opacity': 1,
                'fill-outline-color': '#000'
            }
          },
          firstSymbolId
        );
      });
      map.on('data', afterLoad);
      map.on('click', 'countries', function (e) {
        new maptilersdk.Popup()
          .setLngLat(e.lngLat)
          .setHTML(`<h3>Population</h3><p>${e.features[0].state.population.toLocaleString()}</p>`)
          .addTo(map);
      });
      // Change the cursor to a pointer when the mouse is over the layer.
      map.on('mouseenter', 'countries', function () {
          map.getCanvas().style.cursor = 'pointer';
      });

      // Change it back to a pointer when it leaves.
      map.on('mouseleave', 'countries', function () {
          map.getCanvas().style.cursor = '';
      });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Display a countries choropleth map with your own data</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
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
            center: [13.39, 52.51],
            zoom: 2
        });

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
                container: 'map', // container's id or the HTML element to render the map
                style: maptilersdk.MapStyle.DATAVIZ.LIGHT,
                center: [13.39, 52.51], // starting position [lng, lat]
                zoom: 2, // starting zoom
              });
              map.on('load', function() {
                map.addSource('statesData', {
                  type: 'vector',
                  url: `https://api.maptiler.com/tiles/countries/tiles.json?`
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
                        'fill-color': ['case',
                          ['!=', ['to-number', ['feature-state', 'population']], 0],
                          ['interpolate', ['linear'], ['feature-state', 'population'], 
                            5000000, 'rgba(222,235,247,1)', 90000000, 'rgba(49,130,189,1)'
                          ],
                          'rgba(0, 0, 0, 0)'
                        ],
                        'fill-opacity': 1,
                        'fill-outline-color': '#000'
                    }
                  },
                  firstSymbolId
                );
              });
              map.on('data', afterLoad);
              map.on('click', 'countries', function (e) {
                new maptilersdk.Popup()
                  .setLngLat(e.lngLat)
                  .setHTML(`<h3>Population</h3><p>${e.features[0].state.population.toLocaleString()}</p>`)
                  .addTo(map);
              });
              // Change the cursor to a pointer when the mouse is over the layer.
              map.on('mouseenter', 'countries', function () {
                  map.getCanvas().style.cursor = 'pointer';
              });

              // Change it back to a pointer when it leaves.
              map.on('mouseleave', 'countries', function () {
                  map.getCanvas().style.cursor = '';
              });
    </script>
</body>
</html>
```
