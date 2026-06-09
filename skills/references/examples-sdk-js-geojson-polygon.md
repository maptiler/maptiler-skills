# Source: https://docs.maptiler.com/sdk-js/examples/geojson-polygon/

# Display a GeoJSON Layer

In this tutorial, we will demonstrate the process of incorporating a GeoJSON polygon overlay onto the map. Through the following steps, you will learn how to seamlessly integrate this feature into your web mapping applications.

<div class="tab-common-content" markdown="1">

1. Add event handler for map load event. You will add code to create a GeoJSON source and a vector layer in this handler.

<pre class="line-numbers" data-start="24" data-line-offset="23" data-line="24-26"><code class="language-js">

map.on('load', async function() {

});

</code></pre>

1. Create GeoJSON source. The following snippet creates GeoJSON source hosted on MapTiler (check out the [How to Upload GeoJSON to MapTiler](/guides/maps-apis/maps-platform/prepare-geojson-with-attributes-for-choropleth-map-and-upload-geojson-to-maptiler-cloud#PrepareGeoJSONwithattributesforchoroplethmapanduploadGeoJSONtoMapTilerCloud-UploadGeoJSONtoMapTilerCloud){:target="_blank" rel="noopener"} tutorial). Publish the dataset and copy the link to the GeoJSON. Download the [Rio de Janeiro sample data](/sdk-js/assets/rio_cats.geojson){:target="_blank" rel="noopener"}.

<pre class="line-numbers" data-start="24" data-line-offset="23" data-line="25-29"><code class="language-js">

map.on('load', async function() {

const geojson = await maptilersdk.data.get('YOUR_MAPTILER_DATASET_ID_HERE');

map.addSource('rio_cats', {

type: 'geojson',

data: geojson

});

});

</code></pre>

1. Add the vector layer

<pre class="line-numbers" data-start="30" data-line-offset="29" data-line="30-99"><code class="language-js">

map.addLayer({

'id': 'rio_cats',

'type': 'fill',

'source': 'rio_cats',

'layout': {},

'paint': {

'fill-color': '#98b',

'fill-opacity': 0.8

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
            style: maptilersdk.MapStyle.STREETS,
            center: [-43.206091, -22.920387], // starting position [lng, lat]
            zoom: 11, // starting zoom
        });
        map.on('load', async function () {
            const geojson = await maptilersdk.data.get('YOUR_MAPTILER_DATASET_ID_HERE');
            map.addSource('rio_cats', {
                type: 'geojson',
                data: geojson
            });
            map.addLayer({
                'id': 'rio_cats',
                'type': 'fill',
                'source': 'rio_cats',
                'layout': {},
                'paint': {
                    'fill-color': '#98b',
                    'fill-opacity': 0.8
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
    <title>Display a GeoJSON Layer</title>
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
            center: [-43.206091, -22.920387],
            zoom: 11
        });

        container: 'map', // container's id or the HTML element to render the map
                    style: maptilersdk.MapStyle.STREETS,
                    center: [-43.206091, -22.920387], // starting position [lng, lat]
                    zoom: 11, // starting zoom
                });
                map.on('load', async function () {
                    const geojson = await maptilersdk.data.get('YOUR_MAPTILER_DATASET_ID_HERE');
                    map.addSource('rio_cats', {
                        type: 'geojson',
                        data: geojson
                    });
                    map.addLayer({
                        'id': 'rio_cats',
                        'type': 'fill',
                        'source': 'rio_cats',
                        'layout': {},
                        'paint': {
                            'fill-color': '#98b',
                            'fill-opacity': 0.8
                        }
                    });
                });
    </script>
</body>
</html>
```
