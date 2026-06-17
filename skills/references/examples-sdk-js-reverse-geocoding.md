# Source: https://docs.maptiler.com/sdk-js/examples/reverse-geocoding/

# Reverse Geocoding

In this step-by-step tutorial, we will demonstrate the process of finding locations using coordinates through the utilization of the [MapTiler Geocoding API](https://www.maptiler.com/cloud/geocoding/){:target="_blank" rel="noopener"}. The option to search by coordinates allows for the conversion of specific coordinates into corresponding place names, a technique commonly referred to as **reverse geocoding**.

MapTiler's all-in-one Geocoding search API offers users the ability to effortlessly locate specific places either by their names or addresses (direct geocoding) or by inputting coordinates (reverse geocoding).

<sup>Click on the map to search for places.</sup>

<div class="tab-common-content" markdown="1">

1. Create the map layer where we will display the search results.

<pre class="line-numbers" data-start="24" data-line-offset="23" data-line="24-43"><code class="language-js"><!--

map.on('load', () => {

map.addSource('search-results', {

type: 'geojson',

data: {

"type": "FeatureCollection",

"features": []

}

});

map.addLayer({

'id': 'point-result',

'type': 'circle',

'source': 'search-results',

'paint': {

'circle-radius': 8,

'circle-color': '#B42222',

'circle-opacity': 0.5

},

'filter': ['==', '$type', 'Point']

});

});

--></code></pre>

1. Create the function to perform the reverse geocoding search when the map is clicked. Show the results on the map and adjust the map view to the results.

<pre class="line-numbers" data-start="44" data-line-offset="43" data-line="44-53"><code class="language-js"><!--

map.on('click', async (e) => {

const {lng, lat} = e.lngLat;

const results = await maptilersdk.geocoding.reverse([lng, lat]);

const map = e.target;

map.getSource('search-results').setData(results);

const bounds = results.features.reduce(function (bounds, feature) {

return bounds.extend(feature.bbox);

}, new maptilersdk.LngLatBounds(results.features[0].bbox));

map.fitBounds(bounds);

});

--></code></pre>

1. We already have the results on the map, now we will create a list to show the place names found. By clicking on a name we will zoom to the bbox of the place

<pre class="line-numbers" data-start="44" data-line-offset="43" data-line="53-56"><code class="language-js"><!--

map.on('click', async (e) => {

const {lng, lat} = e.lngLat;

const results = await maptilersdk.geocoding.reverse([lng, lat]);

const map = e.target;

map.getSource('search-results').setData(results);

const bounds = results.features.reduce(function (bounds, feature) {

return bounds.extend(feature.bbox);

}, new maptilersdk.LngLatBounds(results.features[0].bbox));

map.fitBounds(bounds);

const resultList = results.features.map((feature) => {

return `<li onClick="map.fitBounds([${feature.bbox}], {maxZoom: 19})">${feature.place_name}</li>`

});

document.getElementById('search-results').innerHTML = resultList.join('');

});

--></code></pre>

1. Create the html element where to display the list. Add after the element that contains the map

<pre><code class="language-html"><!--

<div id="results">

<ul id="search-results">

</ul>

</div>

--></code></pre>

1. Create the style of the list. Add the list style to your stylesheet.

<pre><code class="language-css"><!--

position: absolute;

top: 0;

left: 0;

width: 30%;

overflow: auto;

background: rgba(255, 255, 255, 0.8);

}

list-style-type: none;

padding: 0;

margin: 0;

}

padding: 10px;

cursor: pointer;

border-bottom: 1px solid gray;

}

color: gray;

}

border-bottom-width: 0;

}

--></code></pre>

</div>

<div class="tab-content cdn-steps" markdown="1">

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element to render the map
        style: maptilersdk.MapStyle.STREETS,
        center: [13.3975, 52.5196], // starting position [lng, lat]
        zoom: 11, // starting zoom
      });
      map.on('load', () => {
        map.addSource('search-results', {
            type: 'geojson',
            data: {
                "type": "FeatureCollection",
                "features": []
            }
        });
        map.addLayer({
            'id': 'point-result',
            'type': 'circle',
            'source': 'search-results',
            'paint': {
                'circle-radius': 8,
                'circle-color': '#B42222',
                'circle-opacity': 0.5
            },
            'filter': ['==', '$type', 'Point']
        });
      });
      map.on('click', async (e) => {
        const {lng, lat} = e.lngLat;
        const results = await maptilersdk.geocoding.reverse([lng, lat]);
        map.getSource('search-results').setData(results);
        const bounds = results.features.reduce(function (bounds, feature) {
            return bounds.extend(feature.bbox);
        }, new maptilersdk.LngLatBounds(results.features[0].bbox));
        map.fitBounds(bounds);
        const resultList = results.features.map((feature) => {
          return `<li onClick="map.fitBounds([${feature.bbox}], {maxZoom: 19})">${feature.place_name}</li>`
        });
        document.getElementById('search-results').innerHTML = resultList.join('');
      });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Reverse Geocoding</title>
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
            center: [13.3975, 52.5196],
            zoom: 11
        });

        container: 'map', // container's id or the HTML element to render the map
                style: maptilersdk.MapStyle.STREETS,
                center: [13.3975, 52.5196], // starting position [lng, lat]
                zoom: 11, // starting zoom
              });
              map.on('load', () => {
                map.addSource('search-results', {
                    type: 'geojson',
                    data: {
                        "type": "FeatureCollection",
                        "features": []
                    }
                });
                map.addLayer({
                    'id': 'point-result',
                    'type': 'circle',
                    'source': 'search-results',
                    'paint': {
                        'circle-radius': 8,
                        'circle-color': '#B42222',
                        'circle-opacity': 0.5
                    },
                    'filter': ['==', '$type', 'Point']
                });
              });
              map.on('click', async (e) => {
                const {lng, lat} = e.lngLat;
                const results = await maptilersdk.geocoding.reverse([lng, lat]);
                map.getSource('search-results').setData(results);
                const bounds = results.features.reduce(function (bounds, feature) {
                    return bounds.extend(feature.bbox);
                }, new maptilersdk.LngLatBounds(results.features[0].bbox));
                map.fitBounds(bounds);
                const resultList = results.features.map((feature) => {
                  return `<li onClick="map.fitBounds([${feature.bbox}], {maxZoom: 19})">${feature.place_name}</li>`
                });
                document.getElementById('search-results').innerHTML = resultList.join('');
              });
    </script>
</body>
</html>
```
