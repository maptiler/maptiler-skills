# Source: https://docs.maptiler.com/sdk-js/examples/countries-filter/

# Display a US states map

This tutorial shows the process of utilizing and refining data from the [MapTiler Countries](https://www.maptiler.com/countries/){:target="_blank" rel="noopener"} to create a [Choropleth map](../choropleth-geojson/) of the US states. The MapTiler Countries dataset primarily consists of information regarding the administrative divisions within various countries and their respective territories.

<div class="tab-common-content" markdown="1">

1. Add event handler for map `load` event. You will add code to create a vector source and a vector layer in this handler.

<pre class="line-numbers" data-start="24" data-line-offset="23" data-line="24-26"><code class="language-js"><!--

map.on('load', function() {

});

--></code></pre>

1. Create vector source. The following snippet creates a vector source for the MapTiler Countries dataset.

<pre class="line-numbers" data-start="24" data-line-offset="23" data-line="25-28"><code class="language-js"><!--

map.on('load', function() {

map.addSource('statesData', {

type: 'vector',

url: `https://api.maptiler.com/tiles/countries/tiles.json`

});

});

--></code></pre>

1. Get the ID of the first symbol layer. We want to include the vector layer below the map labels. That means we need to know the id of the first symbol layer so we can include the vector layer before this layer.

<pre class="line-numbers" data-start="29" data-line-offset="28" data-line="29-31"><code class="language-js"><!--

// Find the id of the first symbol layer in the map style

const layers = map.getStyle().layers;

const firstSymbolId = layers.find(layer => layer.type === 'symbol').id;

--></code></pre>

1. Add the vector layer. We need to include `firsSymbolId` on the `map.addLayer` function to display the vector under the maps labels

<pre class="line-numbers" data-start="32" data-line-offset="31" data-line="32-45"><code class="language-js"><!--

map.addLayer(

{

'id': 'states',

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

1. Filter the data to only show the states of USA. Add a filter to the layer to only display level 1 items. The dataset now contains divisions and sub-subdivisions only for the US, if you need other country`s divisions, please contact us.

<pre class="line-numbers" data-start="32" data-line-offset="31" data-line="38-42"><code class="language-js"><!--

map.addLayer(

{

'id': 'countries',

'source': 'statesData',

'source-layer': 'administrative',

'type': 'fill',

'filter': [

'all',

['==', 'level', 1],

['==', 'level_0', 'US']

],

'paint': {

'fill-color': '#6B7C93',

'fill-opacity': 1,

'fill-outline-color': '#000'

}

},

firstSymbolId

);

--></code></pre>

1. Create a choropleth map based on the name attribute. Change the `fill-color` property of the layer.

<pre class="line-numbers" data-start="32" data-line-offset="31" data-line="44-58"><code class="language-js"><!--

map.addLayer(

{

'id': 'countries',

'source': 'statesData',

'source-layer': 'administrative',

'type': 'fill',

'filter': [

'all',

['==', 'level', 1],

['==', 'level_0', 'US']

],

'paint': {

'fill-color': [

"match",

["get", "name"],

["Nebraska", "Alaska", "Washington", "Nevada", "New Mexico", "Montana", "Minnesota", "Louisiana", "North Carolina", "Kentucky", "Massachusetts", "Delaware", "Michigan"],

"#D5CD85",

["Oklahoma", "Florida", "Idaho", "Wisconsin", "Arizona", "Tennessee", "Pennsylvania", "New Hampshire", "Rhode Island"],

"#D58785",

["New York", "California", "Wyoming", "Kansas", "Illinois", "Mississippi", "South Carolina", "West Virginia"],

"#735F91",

["Texas", "Georgia", "Utah", "Missouri", "South Dakota", "Ohio", "Maryland", "Vermont"],

"#567986",

["Colorado", "Oregon", "Alabama", "Indiana", "North Dakota", "Iowa", "Arkansas", "Virginia", "New Jersey", "Maine", "Connecticut"],

"#69A86D",

"rgba(0, 0, 0, 0.5)"

],

'fill-opacity': 1,

'fill-outline-color': '#000'

}

},

firstSymbolId

);

--></code></pre>

</div>

<div class="tab-content cdn-steps" markdown="1">

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element to render the map
        style: maptilersdk.MapStyle.STREETS,
        center: [-94.28, 38.45], // starting position [lng, lat]
        zoom: 3, // starting zoom
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
            'id': 'US_states',
            'source': 'statesData',
            'source-layer': 'administrative',
            'type': 'fill',
            'filter': [
              'all',
              ['==', 'level', 1],
              ['==', 'level_0', 'US']
            ],
            'paint': {
                'fill-color': [
                  "match",
                  ["get", "name"],
                  ["Nebraska", "Alaska", "Washington", "Nevada", "New Mexico", "Montana", "Minnesota", "Louisiana", "North Carolina", "Kentucky", "Massachusetts", "Delaware", "Michigan"],
                  "#D5CD85",
                  ["Oklahoma", "Florida", "Idaho", "Wisconsin", "Arizona", "Tennessee", "Pennsylvania", "New Hampshire", "Rhode Island"],
                  "#D58785",
                  ["New York", "California", "Wyoming", "Kansas", "Illinois", "Mississippi", "South Carolina", "West Virginia"],
                  "#735F91",
                  ["Texas", "Georgia", "Utah", "Missouri", "South Dakota", "Ohio", "Maryland", "Vermont"],
                  "#567986",
                  ["Colorado", "Oregon", "Alabama", "Indiana", "North Dakota", "Iowa", "Arkansas", "Virginia", "New Jersey", "Maine", "Connecticut"],
                  "#69A86D",
                  "rgba(0, 0, 0, 0.5)"
                ],
                'fill-opacity': 1,
                'fill-outline-color': '#000'
            }
          },
          firstSymbolId
        );
      });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Display a US states map</title>
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
            style: maptilersdk.MapStyle.STREETS,
            center: [-94.28, 38.45],
            zoom: 3
        });

        container: 'map', // container's id or the HTML element to render the map
                style: maptilersdk.MapStyle.STREETS,
                center: [-94.28, 38.45], // starting position [lng, lat]
                zoom: 3, // starting zoom
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
                    'id': 'US_states',
                    'source': 'statesData',
                    'source-layer': 'administrative',
                    'type': 'fill',
                    'filter': [
                      'all',
                      ['==', 'level', 1],
                      ['==', 'level_0', 'US']
                    ],
                    'paint': {
                        'fill-color': [
                          "match",
                          ["get", "name"],
                          ["Nebraska", "Alaska", "Washington", "Nevada", "New Mexico", "Montana", "Minnesota", "Louisiana", "North Carolina", "Kentucky", "Massachusetts", "Delaware", "Michigan"],
                          "#D5CD85",
                          ["Oklahoma", "Florida", "Idaho", "Wisconsin", "Arizona", "Tennessee", "Pennsylvania", "New Hampshire", "Rhode Island"],
                          "#D58785",
                          ["New York", "California", "Wyoming", "Kansas", "Illinois", "Mississippi", "South Carolina", "West Virginia"],
                          "#735F91",
                          ["Texas", "Georgia", "Utah", "Missouri", "South Dakota", "Ohio", "Maryland", "Vermont"],
                          "#567986",
                          ["Colorado", "Oregon", "Alabama", "Indiana", "North Dakota", "Iowa", "Arkansas", "Virginia", "New Jersey", "Maine", "Connecticut"],
                          "#69A86D",
                          "rgba(0, 0, 0, 0.5)"
                        ],
                        'fill-opacity': 1,
                        'fill-outline-color': '#000'
                    }
                  },
                  firstSymbolId
                );
              });
    </script>
</body>
</html>
```
