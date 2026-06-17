# Source: https://docs.maptiler.com/sdk-js/examples/geojson-point/

# Display a GeoJSON Point Layer

This tutorial offers a comprehensive walkthrough on integrating a GeoJSON point overlay onto a map. You will be guided through the following steps to achieve this.

<div class="tab-common-content" markdown="1">

1. To follow this tutorial you can use Airports from Natural Earth. Download the [Airports sample data](https://www.naturalearthdata.com/downloads/10m-cultural-vectors/airports/){:target="_blank" rel="noopener"}

1. Add event handler for map load event. You will add code to create a GeoJSON source and a vector layer in this handler.

<pre class="line-numbers" data-start="24" data-line-offset="23" data-line="24-26"><code class="language-js">

map.on('load', async function() {

});

</code></pre>

1.  Add a custom image to the map. You can use any image or download the [airport image](./icon-plane-512.png) we used in the tutorial. In the example the image is in the same folder as the index.html file

<pre class="line-numbers" data-start="24" data-line-offset="23" data-line="25-26"><code class="language-js">

map.on('load', async function() {

const image = await map.loadImage('./icon-plane-512.png');

map.addImage('plane', image.data);

});

</code></pre>

1. Create GeoJSON source. The following snippet creates GeoJSON source hosted on MapTiler (check out the [How to Upload GeoJSON to MapTiler](/guides/maps-apis/maps-platform/prepare-geojson-with-attributes-for-choropleth-map-and-upload-geojson-to-maptiler-cloud#PrepareGeoJSONwithattributesforchoroplethmapanduploadGeoJSONtoMapTilerCloud-UploadGeoJSONtoMapTilerCloud){:target="_blank" rel="noopener"} tutorial). Publish the dataset and copy the link to the GeoJSON. Download the sample data [here](https://www.naturalearthdata.com/downloads/10m-cultural-vectors/airports/){:target="_blank" rel="noopener"}.

<pre class="line-numbers" data-start="28" data-line-offset="27" data-line="28-32"><code class="language-js">

const geojson = await maptilersdk.data.get('YOUR_MAPTILER_DATASET_ID_HERE');

map.addSource('airports', {

type: 'geojson',

data: geojson

});

</code></pre>

1. Add the vector layer

<pre class="line-numbers" data-start="33" data-line-offset="32" data-line="33-42"><code class="language-js">

map.addLayer({

'id': 'airports',

'type': 'symbol',

'source': 'airports',

'layout': {

'icon-image': 'plane',

'icon-size': ['*', ['get', 'scalerank'], 0.01]

},

'paint': {}

});

</code></pre>

</div>

<div class="tab-content cdn-steps" markdown="1">

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element to render the map
      style: maptilersdk.MapStyle.BASIC,
      center: [-110.75954, 43.72874], // starting position [lng, lat]
      zoom: 4, // starting zoom
    });
    map.on('load', async function () {
      const image = await map.loadImage('./icon-plane-512.png');
      map.addImage('plane', image.data);
      const geojson = await maptilersdk.data.get('YOUR_MAPTILER_DATASET_ID_HERE');
      map.addSource('airports', {
        type: 'geojson',
        data: geojson
      });
      map.addLayer({
        'id': 'airports',
        'type': 'symbol',
        'source': 'airports',
        'layout': {
          'icon-image': 'plane',
          'icon-size': ['*', ['get', 'scalerank'], 0.01]
        },
        'paint': {}
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
    <title>Display a GeoJSON Point Layer</title>
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
            style: maptilersdk.MapStyle.BASE,
            center: [-110.75954, 43.72874],
            zoom: 4
        });

        container: 'map', // container's id or the HTML element to render the map
              style: maptilersdk.MapStyle.BASIC,
              center: [-110.75954, 43.72874], // starting position [lng, lat]
              zoom: 4, // starting zoom
            });
            map.on('load', async function () {
              const image = await map.loadImage('./icon-plane-512.png');
              map.addImage('plane', image.data);
              const geojson = await maptilersdk.data.get('YOUR_MAPTILER_DATASET_ID_HERE');
              map.addSource('airports', {
                type: 'geojson',
                data: geojson
              });
              map.addLayer({
                'id': 'airports',
                'type': 'symbol',
                'source': 'airports',
                'layout': {
                  'icon-image': 'plane',
                  'icon-size': ['*', ['get', 'scalerank'], 0.01]
                },
                'paint': {}
              });
            });
    </script>
</body>
</html>
```
