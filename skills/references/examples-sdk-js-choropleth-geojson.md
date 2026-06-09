# Source: https://docs.maptiler.com/sdk-js/examples/choropleth-geojson/

# Display a choropleth Map from GeoJSON

This tutorial demonstrates the process of generating a Choropleth map through the application of styling to a GeoJSON overlay layer on the map. Additionally, it explains how to display a popup when clicked and create a map legend. As an illustrative example, we will be using countries with attributes sourced from EUROSTAT in GeoJSON format. You can download the [Age of the first marriage sample data](/sdk-js/assets/Mean_age_of_women_at_first_marriage_in_2019.geojson).

<div class="tab-common-content" markdown="1">

1. Add event handler for map load event. You will add code to create a GeoJSON source and a vector layer in this handler.

<pre class="line-numbers" data-start="24" data-line-offset="23" data-line="24-26"><code class="language-js"><!--

map.on('load', async function() {

});

--></code></pre>

1. Create GeoJSON source. The following snippet creates GeoJSON source hosted on MapTiler (check out the [How to Upload GeoJSON to MapTiler](/guides/maps-apis/maps-platform/prepare-geojson-with-attributes-for-choropleth-map-and-upload-geojson-to-maptiler-cloud#PrepareGeoJSONwithattributesforchoroplethmapanduploadGeoJSONtoMapTilerCloud-UploadGeoJSONtoMapTilerCloud){:target="\_blank" rel="noopener"} tutorial). Publish the dataset and copy the link to the GeoJSON. The GeoJSON used in the example contains data from EUROSTAT Marriage indicators dataset filtrated to just countries with some value of mean age of women at first marriage in 2019. Download the [Age of the first marriage sample data](/sdk-js/assets/Mean_age_of_women_at_first_marriage_in_2019.geojson).

<pre class="line-numbers" data-start="24" data-line-offset="23" data-line="25-29"><code class="language-js"><!--

map.on('load', async function() {

const result = await maptilersdk.data.get('YOUR_MAPTILER_DATASET_ID_HERE');

map.addSource('age', {

'type': 'geojson',

'data': result

});

});

--></code></pre>

1. Get the ID of the first symbol layer. We want to include GeoJSON below the map labels. That means we need to know the ID of the first symbol layer so we can include the GeoJSON layer before this layer.

<pre class="line-numbers" data-start="30" data-line-offset="29" data-line="30-32"><code class="language-js"><!--

// Find the ID of the first symbol layer in the map style

const layers = map.getStyle().layers;

const firstSymbolId = layers.find(layer => layer.type === 'symbol').id;

--></code></pre>

1. Add the GeoJSON layer. We need to include `firsSymbolId` on the `map.addLayer` function to display the GeoJSON under the map's labels.

<pre class="line-numbers" data-start="33" data-line-offset="32" data-line="33-45"><code class="language-js"><!--

map.addLayer(

{

'id': 'IDage',

'source': 'age',

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

1. Create a choropleth map based on the age attribute. Change the `fill-color` property of the layer.

<pre class="line-numbers" data-start="33" data-line-offset="32" data-line="39-59"><code class="language-js"><!--

map.addLayer(

{

'id': 'IDage',

'source': 'age',

'type': 'fill',

'paint': {

'fill-color': [

'interpolate',

['linear'],

['get', 'age'],

23.0,

'#fff5eb',

24.0,

'#fee6ce',

25.0,

'#fdd0a2',

26.0,

'#fdae6b',

27.0,

'#fd8d3c',

28.0,

'#f16913',

29.0,

'#d94801',

30.0,

'#8c2d04'

],

'fill-opacity': 1,

'fill-outline-color': '#000'

}

},

firstSymbolId

);

--></code></pre>

1. Display a popup when clicking on the geojson layer and show the information of the age attribute.

<pre class="line-numbers" data-start="66" data-line-offset="65" data-line="66-71"><code class="language-js"><!--

map.on('click', 'IDage', function (e) {

new maptilersdk.Popup()

.setLngLat(e.lngLat)

.setHTML(`<h3>Average age of </br> women at first marriage </br>in 2019</h3><p>${e.features[0].properties.age}</p>`)

.addTo(map);

});

--></code></pre>

1. To make our map more user-friendly, we will change the cursor when hovering over a geometry in the geojson layer to indicate to the user that they can click on it.

<pre class="line-numbers" data-start="72" data-line-offset="71" data-line="72-80"><code class="language-js"><!--

// Change the cursor to a pointer when the mouse is over the layer.

map.on('mouseenter', 'IDage', function () {

map.getCanvas().style.cursor = 'pointer';

});

// Change it back to a pointer when it leaves.

map.on('mouseleave', 'IDage', function () {

map.getCanvas().style.cursor = '';

});

--></code></pre>

1. Create a map legend style. Add the legend style to your stylesheet.

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

1. Create the map legend elements. Add after the element that contains the map.

<pre><code class="language-html"><!--

<div id="state-legend" class="legend">

<h4>Mean age of </br> women at first marriage</br>in 2019</h4>

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

<div class="tab-content cdn-steps" markdown="1">

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', async function () {
      const result = await maptilersdk.data.get('YOUR_MAPTILER_DATASET_ID_HERE');
      map.addSource('age', {
        'type': 'geojson',
        'data': result
      });
      // Find the id of the first symbol layer in the map style
      const layers = map.getStyle().layers;
      const firstSymbolId = layers.find(layer => layer.type === 'symbol').id;

      map.addLayer(
        {
          'id': 'IDage',
          'source': 'age',
          'type': 'fill',
          'paint': {
            'fill-color': [
              'interpolate',
              ['linear'],
              ['get', 'age'],
              23.0,
              '#fff5eb',
              24.0,
              '#fee6ce',
              25.0,
              '#fdd0a2',
              26.0,
              '#fdae6b',
              27.0,
              '#fd8d3c',
              28.0,
              '#f16913',
              29.0,
              '#d94801',
              30.0,
              '#8c2d04'
            ],
            'fill-opacity': 1,
            'fill-outline-color': '#000'
          }
        },
        firstSymbolId
      );

      map.on('click', 'IDage', function (e) {
        new maptilersdk.Popup()
          .setLngLat(e.lngLat)
          .setHTML(`<h3>Average age of </br> women at first marriage</br>in 2019</h3><p>${e.features[0].properties.age}</p>`)
          .addTo(map);
      });

      // Change the cursor to a pointer when the mouse is over the layer.
      map.on('mouseenter', 'IDage', function () {
        map.getCanvas().style.cursor = 'pointer';
      });

      // Change it back to a pointer when it leaves.
      map.on('mouseleave', 'IDage', function () {
        map.getCanvas().style.cursor = '';
      });
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
            style: maptilersdk.MapStyle.DATAVIZ.DARK,
            center: [13.39, 52.51],
            zoom: 2
        });

        map.on('load', async function () {
              const result = await maptilersdk.data.get('YOUR_MAPTILER_DATASET_ID_HERE');
              map.addSource('age', {
                'type': 'geojson',
                'data': result
              });
              // Find the id of the first symbol layer in the map style
              const layers = map.getStyle().layers;
              const firstSymbolId = layers.find(layer => layer.type === 'symbol').id;

              map.addLayer(
                {
                  'id': 'IDage',
                  'source': 'age',
                  'type': 'fill',
                  'paint': {
                    'fill-color': [
                      'interpolate',
                      ['linear'],
                      ['get', 'age'],
                      23.0,
                      '#fff5eb',
                      24.0,
                      '#fee6ce',
                      25.0,
                      '#fdd0a2',
                      26.0,
                      '#fdae6b',
                      27.0,
                      '#fd8d3c',
                      28.0,
                      '#f16913',
                      29.0,
                      '#d94801',
                      30.0,
                      '#8c2d04'
                    ],
                    'fill-opacity': 1,
                    'fill-outline-color': '#000'
                  }
                },
                firstSymbolId
              );

              map.on('click', 'IDage', function (e) {
                new maptilersdk.Popup()
                  .setLngLat(e.lngLat)
                  .setHTML(`<h3>Average age of </br> women at first marriage</br>in 2019</h3><p>${e.features[0].properties.age}</p>`)
                  .addTo(map);
              });

              // Change the cursor to a pointer when the mouse is over the layer.
              map.on('mouseenter', 'IDage', function () {
                map.getCanvas().style.cursor = 'pointer';
              });

              // Change it back to a pointer when it leaves.
              map.on('mouseleave', 'IDage', function () {
                map.getCanvas().style.cursor = '';
              });
            });
    </script>
</body>
</html>
```
