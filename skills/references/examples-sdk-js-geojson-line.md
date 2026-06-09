# Source: https://docs.maptiler.com/sdk-js/examples/geojson-line/

# Display a GeoJSON Line Layer

This step-by-step tutorial provides a detailed guide on how to incorporate a GeoJSON line overlay onto a map. The following steps will walk you through the process.

<div class="tab-common-content" markdown="1">

1. Add event handler for map load event. You will add code to create a GeoJSON source and a vector layer in this handler.

<pre class="line-numbers" data-start="24" data-line-offset="23" data-line="24-26"><code class="language-js">

map.on('load', async function() {

});

</code></pre>

1. Create GeoJSON source. The following snippet creates GeoJSON source hosted on MapTiler (check out the [How to Upload GeoJSON to MapTiler](/guides/maps-apis/maps-platform/prepare-geojson-with-attributes-for-choropleth-map-and-upload-geojson-to-maptiler-cloud#PrepareGeoJSONwithattributesforchoroplethmapanduploadGeoJSONtoMapTilerCloud-UploadGeoJSONtoMapTilerCloud){:target="_blank" rel="noopener"} tutorial). Publish the dataset and copy the link to the GeoJSON. Download the [Amphitheater Lake trail sample data](./Line_GeoJSON_example.geojson){:target="_blank" rel="noopener"}.

<pre class="line-numbers" data-start="24" data-line-offset="23" data-line="25-29"><code class="language-js">

map.on('load', async function() {

const geojson = await maptilersdk.data.get('YOUR_MAPTILER_DATASET_ID_HERE');

map.addSource('gps_tracks', {

'type': 'geojson',

'data': geojson

});

});

</code></pre>

1. Add the vector layer

<pre class="line-numbers" data-start="30" data-line-offset="29" data-line="30-99"><code class="language-js">

map.addLayer({

'id': 'grand_teton',

'type': 'line',

'source': 'gps_tracks',

'layout': {},

'paint': {

'line-color': '#e11',

'line-width': 4

}

});

</code></pre>

</div>

<div class="tab-content cdn-steps" markdown="1">

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element to render the map
        style: maptilersdk.MapStyle.OUTDOOR,
        center: [-110.75954, 43.72874], // starting position [lng, lat]
        zoom: 13.5, // starting zoom
      });
      map.on('load', async function() {
        const geojson = await maptilersdk.data.get('YOUR_MAPTILER_DATASET_ID_HERE');
        map.addSource('gps_tracks', {
          'type': 'geojson',
          'data': geojson
        });
        map.addLayer({
          'id': 'grand_teton',
          'type': 'line',
          'source': 'gps_tracks',
          'layout': {},
          'paint': {
            'line-color': '#e11',
            'line-width': 4
          }
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
    <title>Display a GeoJSON Line Layer</title>
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
            style: maptilersdk.MapStyle.OUTDOOR,
            center: [-110.75954, 43.72874],
            zoom: 13.5
        });

        container: 'map', // container's id or the HTML element to render the map
                style: maptilersdk.MapStyle.OUTDOOR,
                center: [-110.75954, 43.72874], // starting position [lng, lat]
                zoom: 13.5, // starting zoom
              });
              map.on('load', async function() {
                const geojson = await maptilersdk.data.get('YOUR_MAPTILER_DATASET_ID_HERE');
                map.addSource('gps_tracks', {
                  'type': 'geojson',
                  'data': geojson
                });
                map.addLayer({
                  'id': 'grand_teton',
                  'type': 'line',
                  'source': 'gps_tracks',
                  'layout': {},
                  'paint': {
                    'line-color': '#e11',
                    'line-width': 4
                  }
                });
              });
    </script>
</body>
</html>
```
