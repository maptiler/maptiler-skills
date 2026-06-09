# Source: https://docs.maptiler.com/openlayers/examples/geojson-polygon/

# Display a GeoJSON Layer

This tutorial shows how to add a Polygon GeoJSON overlay to the map using OpenLayers.

1. Create GeoJSON source. The following snippet creates GeoJSON source hosted on MapTiler (check out the [How to Upload GeoJSON to MapTiler](/guides/maps-apis/maps-platform/prepare-geojson-with-attributes-for-choropleth-map-and-upload-geojson-to-maptiler-cloud#PrepareGeoJSONwithattributesforchoroplethmapanduploadGeoJSONtoMapTilerCloud-UploadGeoJSONtoMapTilerCloud){:target="_blank" rel="noopener"} tutorial). Publish the dataset and copy link to the geojson. Download the [Rio de Janeiro sample data](/sdk-js/assets/rio_cats.geojson){:target="_blank" rel="noopener"}.

<pre class="line-numbers" data-start="41" data-line-offset="40" data-line="42-87"><code class="language-js">

});

const layer = new ol.layer.Vector({

source: new ol.source.Vector({

url: `https://api.maptiler.com/data/YOUR_MAPTILER_DATASET_ID_HERE/features.json?key=${key}`,

format: new ol.format.GeoJSON(),

}),

style: new ol.style.Style({

stroke: new ol.style.Stroke({

color: 'rgba(0, 136, 136, 0.8)',

}),

fill: new ol.style.Fill({

color: 'rgba(0, 136, 136, 0.8)',

}),

})

});

map.addLayer(layer);

</code></pre>

</div>

1. Import the new modules needed to add the new functionality.

<pre class="line-numbers" data-start="8" data-line-offset="7" data-line="8-13"><code class="language-js">

import VectorLayer from 'ol/layer/Vector.js';

import VectorSource from 'ol/source/Vector.js';

import Style from 'ol/style/Style.js';

import Stroke from 'ol/style/Stroke.js';

import Fill from 'ol/style/Fill.js';

import GeoJSON from 'ol/format/GeoJSON.js';

</code></pre>

1. Create GeoJSON layer. The following snippet creates GeoJSON layer from an external file with polygon geometry. Check out the [How to Upload GeoJSON to MapTiler](/guides/maps-apis/maps-platform/prepare-geojson-with-attributes-for-choropleth-map-and-upload-geojson-to-maptiler-cloud#PrepareGeoJSONwithattributesforchoroplethmapanduploadGeoJSONtoMapTilerCloud-UploadGeoJSONtoMapTilerCloud){:target="_blank" rel="noopener"} tutorial. Publish the dataset and copy link to the geojson. Download the [Rio de Janeiro sample data](/sdk-js/assets/rio_cats.geojson){:target="_blank" rel="noopener"}.

<pre class="line-numbers" data-start="43" data-line-offset="42" data-line="43-57"><code class="language-js"><!--

const layer = new VectorLayer({

source: new VectorSource({

url: `https://api.maptiler.com/data/YOUR_MAPTILER_DATASET_ID_HERE/features.json?key=${key}`,

format: GeoJSON(),

}),

style: new Style({

stroke: new Stroke({

color: 'rgba(0, 136, 136, 0.8)',

}),

fill: new Fill({

color: 'rgba(0, 136, 136, 0.8)',

}),

})

});

map.addLayer(layer);

--></code></pre>

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const layer = new ol.layer.Vector({
      source: new ol.source.Vector({
        url: `https://api.maptiler.com/data/YOUR_MAPTILER_DATASET_ID_HERE/features.json?key=${key}`,
        format: new ol.format.GeoJSON(),
      }),
      style: new ol.style.Style({
        stroke: new ol.style.Stroke({
          color: 'rgba(0, 136, 136, 0.8)',
        }),
        fill: new ol.style.Fill({
          color: 'rgba(0, 136, 136, 0.8)',
        }),
      })
    });
    map.addLayer(layer);
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Display a GeoJSON Layer</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/ol@10.9.0/ol.css">
    <script src="https://cdn.jsdelivr.net/npm/ol@10.9.0/dist/ol.js"></script>
    <style>
        body { margin: 0; padding: 0; }
        #map { position: absolute; top: 0; bottom: 0; width: 100%; }
    </style>
</head>
<body>
    <div id="map"></div>
    <script>
        const key = 'YOUR_MAPTILER_API_KEY';

            const attribution = new ol.control.Attribution({
              collapsible: false,
            });

            const source = new ol.source.TileJSON({
              url: `https://api.maptiler.com/maps/streets-v4/tiles.json?key=${key}`,
              tileSize: 512,
              crossOrigin: 'anonymous'
            });

            const map = new ol.Map({
              layers: [
                new ol.layer.Tile({
                  source: source
                })
              ],
              controls: ol.control.defaults.defaults({ attribution: false }).extend([attribution]),
              target: 'map',
              view: new ol.View({
                constrainResolution: true,
                center: ol.proj.fromLonLat([16.62662018, 49.2125578]),
                zoom: 14
              })
            });

            const layer = new ol.layer.Vector({
              source: new ol.source.Vector({
                url: `https://api.maptiler.com/data/YOUR_MAPTILER_DATASET_ID_HERE/features.json?key=${key}`,
                format: new ol.format.GeoJSON(),
              }),
              style: new ol.style.Style({
                stroke: new ol.style.Stroke({
                  color: 'rgba(0, 136, 136, 0.8)',
                }),
                fill: new ol.style.Fill({
                  color: 'rgba(0, 136, 136, 0.8)',
                }),
              })
            });
            map.addLayer(layer);
    </script>
</body>
</html>
```
