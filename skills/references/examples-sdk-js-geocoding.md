# Source: https://docs.maptiler.com/sdk-js/examples/geocoding/

# Search a placename

This tutorial shows how you can use place search using the [MapTiler Geocoding API](https://www.maptiler.com/cloud/geocoding/){:target="_blank" rel="noopener"}. The resultant map application takes a search query from the URL and displays the search results on the map, zooming in on the first result.

<sup>The map shows as a red dot the first search result for <b>""</b>.</sup>

<div class="tab-common-content" markdown="1">

1. Get the query string of the map URL.

<pre class="line-numbers" data-start="17" data-line-offset="16" data-line="17"><code class="language-js"><!--

const urlParams = new URLSearchParams(window.location.search);

--></code></pre>

1. Create the map layer where we will display the search results.

<pre class="line-numbers" data-start="25" data-line-offset="24" data-line="25-44"><code class="language-js"><!--

map.on('load', async () => {

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

1. Check if the search parameter called `q` exists. If it exists, call the forward geocoding function with the value of the parameter `q`.

<pre class="line-numbers" data-start="44" data-line-offset="43" data-line="44-46"><code class="language-js"><!--

if (urlParams.get('q')) {

const results = await maptilersdk.geocoding.forward(urlParams.get('q'));

}

--></code></pre>

1. Show the results on the map and zoom in on the first result.

<pre class="line-numbers" data-start="44" data-line-offset="43" data-line="46-49"><code class="language-js"><!--

if (urlParams.get('q')) {

const results = await searchPlace(urlParams.get('q'), key);

map.getSource('search-results').setData(results);

if (results.features[0]) {

map.fitBounds(results.features[0].bbox, {maxZoom: 19})

}

}

--></code></pre>

</div>

<div class="tab-content cdn-steps" markdown="1">

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const urlParams = new URLSearchParams(window.location.search);
        container: 'map', // container's id or the HTML element to render the map
        style: maptilersdk.MapStyle.STREETS,
        center: [-97.7485, 30.2711], // starting position [lng, lat]
        zoom: 11.7, // starting zoom
      });
      map.on('load', async () => {
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
        if (urlParams.get('q')) {
          const results = await maptilersdk.geocoding.forward(urlParams.get('q'));
          map.getSource('search-results').setData(results);
          if (results.features[0]) {
            map.fitBounds(results.features[0].bbox, {maxZoom: 19})
          }
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
    <title>Search a placename</title>
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
            center: [-97.7485, 30.2711],
            zoom: 11.7
        });

        const urlParams = new URLSearchParams(window.location.search);
                container: 'map', // container's id or the HTML element to render the map
                style: maptilersdk.MapStyle.STREETS,
                center: [-97.7485, 30.2711], // starting position [lng, lat]
                zoom: 11.7, // starting zoom
              });
              map.on('load', async () => {
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
                if (urlParams.get('q')) {
                  const results = await maptilersdk.geocoding.forward(urlParams.get('q'));
                  map.getSource('search-results').setData(results);
                  if (results.features[0]) {
                    map.fitBounds(results.features[0].bbox, {maxZoom: 19})
                  }
                }
              });
    </script>
</body>
</html>
```
