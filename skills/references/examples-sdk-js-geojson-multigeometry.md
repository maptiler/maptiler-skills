# Source: https://docs.maptiler.com/sdk-js/examples/geojson-multigeometry/

# Display a GeoJSON Layer

In this tutorial, we will demonstrate the process of incorporating a GeoJSON MultiGeometry overlay onto the map. Throughout this tutorial, we will explore the steps to view a GeoJSON and learn how to customize the style for the layers of point, line, and polygon geometries.

<div class="tab-common-content" markdown="1">

1. Add event handler for map load event. You will add code to create a GeoJSON source and a vector layer in this handler.

<pre class="line-numbers" data-start="24" data-line-offset="23" data-line="24-26"><code class="language-js">

map.on('load', async function() {

});

</code></pre>

1. Create GeoJSON source. The following snippet creates GeoJSON source hosted on MapTiler (check out the [How to Upload GeoJSON to MapTiler](/guides/maps-apis/maps-platform/prepare-geojson-with-attributes-for-choropleth-map-and-upload-geojson-to-maptiler-cloud#PrepareGeoJSONwithattributesforchoroplethmapanduploadGeoJSONtoMapTilerCloud-UploadGeoJSONtoMapTilerCloud){:target="_blank" rel="noopener"} tutorial). Publish the dataset and copy the link to the GeoJSON. Download the [GeoJSON multi-geometries sample data](/sdk-js/assets/geoJSON_multigeometries.geojson){:target="_blank" rel="noopener"}.

<pre class="line-numbers" data-start="24" data-line-offset="23" data-line="25-29"><code class="language-js">

map.on('load', async function() {

const geojson = await maptilersdk.data.get('YOUR_MAPTILER_DATASET_ID_HERE');

map.addSource('geojson-overlay', {

'type': 'geojson',

'data': geojson

});

});

</code></pre>

1. Add the vector layer. Add a layer for each type of geometry: point, line and polygon

<pre class="line-numbers" data-start="30" data-line-offset="29" data-line="30-63"><code class="language-js">

map.addLayer({

'id': 'geojson-overlay-fill',

'type': 'fill',

'source': 'geojson-overlay',

'filter': ['==', '$type', 'Polygon'],

'layout': {},

'paint': {

'fill-color': '#fff',

'fill-opacity': 0.4

}

});

map.addLayer({

'id': 'geojson-overlay-line',

'type': 'line',

'source': 'geojson-overlay',

'layout': {},

'paint': {

'line-color': 'rgb(68, 138, 255)',

'line-width': 3

}

});

map.addLayer({

'id': 'geojson-overlay-point',

'type': 'circle',

'source': 'geojson-overlay',

'filter': ['==', '$type', 'Point'],

'layout': {},

'paint': {

'circle-color': 'rgb(68, 138, 255)',

'circle-stroke-color': '#fff',

'circle-stroke-width': 6,

'circle-radius': 7

}

});

</code></pre>

1. Fit the map view to the bounding box of the data.

<pre class="line-numbers" data-start="64" data-line-offset="63" data-line="64-82"><code class="language-js">

const bounds = [Infinity, Infinity, -Infinity, -Infinity];

const processCoordinates = function(coords) {

if (Array.isArray(coords[0])) {

coords.map(c=>processCoordinates(c));

} else {

bounds[0] = Math.min(bounds[0], coords[0]);

bounds[1] = Math.min(bounds[1], coords[1]);

bounds[2] = Math.max(bounds[2], coords[0]);

bounds[3] = Math.max(bounds[3], coords[1]);

}

};

geojson.features.forEach(function(f) {

if (f.geometry && f.geometry.coordinates) {

processCoordinates(f.geometry.coordinates);

}

});

map.fitBounds(bounds, {

padding: 20

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
      center: [-52.32, 32.91], // starting position [lng, lat]
      zoom: 2, // starting zoom
    });
    map.on('load', async function() {
        const result = await maptilersdk.data.get('YOUR_MAPTILER_DATASET_ID_HERE');
        map.addSource('geojson-overlay', {
            'type': 'geojson',
            'data': result
        });
        map.addLayer({
            'id': 'geojson-overlay-fill',
            'type': 'fill',
            'source': 'geojson-overlay',
            'filter': ['==', '$type', 'Polygon'],
            'layout': {},
            'paint': {
                'fill-color': '#fff',
                'fill-opacity': 0.4
            }
        });
        map.addLayer({
            'id': 'geojson-overlay-line',
            'type': 'line',
            'source': 'geojson-overlay',
            'layout': {},
            'paint': {
                'line-color': 'rgb(68, 138, 255)',
                'line-width': 3
            }
        });
        map.addLayer({
            'id': 'geojson-overlay-point',
            'type': 'circle',
            'source': 'geojson-overlay',
            'filter': ['==', '$type', 'Point'],
            'layout': {},
            'paint': {
                'circle-color': 'rgb(68, 138, 255)',
                'circle-stroke-color': '#fff',
                'circle-stroke-width': 6,
                'circle-radius': 7
            }
        });
        const bounds = [Infinity, Infinity, -Infinity, -Infinity];
        const processCoordinates = function(coords) {
            if (Array.isArray(coords[0])) {
                coords.map(c=>processCoordinates(c));
            } else {
                bounds[0] = Math.min(bounds[0], coords[0]);
                bounds[1] = Math.min(bounds[1], coords[1]);
                bounds[2] = Math.max(bounds[2], coords[0]);
                bounds[3] = Math.max(bounds[3], coords[1]);
            }
        };
        geojson.features.forEach(function(f) {
            if (f.geometry && f.geometry.coordinates) {
                processCoordinates(f.geometry.coordinates);
            }
        });
        map.fitBounds(bounds, {
            padding: 20
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
            center: [-52.32, 32.91],
            zoom: 2
        });

        container: 'map', // container's id or the HTML element to render the map
              style: maptilersdk.MapStyle.STREETS,
              center: [-52.32, 32.91], // starting position [lng, lat]
              zoom: 2, // starting zoom
            });
            map.on('load', async function() {
                const result = await maptilersdk.data.get('YOUR_MAPTILER_DATASET_ID_HERE');
                map.addSource('geojson-overlay', {
                    'type': 'geojson',
                    'data': result
                });
                map.addLayer({
                    'id': 'geojson-overlay-fill',
                    'type': 'fill',
                    'source': 'geojson-overlay',
                    'filter': ['==', '$type', 'Polygon'],
                    'layout': {},
                    'paint': {
                        'fill-color': '#fff',
                        'fill-opacity': 0.4
                    }
                });
                map.addLayer({
                    'id': 'geojson-overlay-line',
                    'type': 'line',
                    'source': 'geojson-overlay',
                    'layout': {},
                    'paint': {
                        'line-color': 'rgb(68, 138, 255)',
                        'line-width': 3
                    }
                });
                map.addLayer({
                    'id': 'geojson-overlay-point',
                    'type': 'circle',
                    'source': 'geojson-overlay',
                    'filter': ['==', '$type', 'Point'],
                    'layout': {},
                    'paint': {
                        'circle-color': 'rgb(68, 138, 255)',
                        'circle-stroke-color': '#fff',
                        'circle-stroke-width': 6,
                        'circle-radius': 7
                    }
                });
                const bounds = [Infinity, Infinity, -Infinity, -Infinity];
                const processCoordinates = function(coords) {
                    if (Array.isArray(coords[0])) {
                        coords.map(c=>processCoordinates(c));
                    } else {
                        bounds[0] = Math.min(bounds[0], coords[0]);
                        bounds[1] = Math.min(bounds[1], coords[1]);
                        bounds[2] = Math.max(bounds[2], coords[0]);
                        bounds[3] = Math.max(bounds[3], coords[1]);
                    }
                };
                geojson.features.forEach(function(f) {
                    if (f.geometry && f.geometry.coordinates) {
                        processCoordinates(f.geometry.coordinates);
                    }
                });
                map.fitBounds(bounds, {
                    padding: 20
                });
            });
    </script>
</body>
</html>
```
