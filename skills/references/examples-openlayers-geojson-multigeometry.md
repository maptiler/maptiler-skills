# Source: https://docs.maptiler.com/openlayers/examples/geojson-multigeometry/

# Display a GeoJSON Layer

This tutorial shows how to add a MultiGeometry GeoJSON overlay to the map using OpenLayers.

1. Create GeoJSON source. The following snippet creates GeoJSON source hosted on MapTiler (check out the [How to Upload GeoJSON to MapTiler](/guides/maps-apis/maps-platform/prepare-geojson-with-attributes-for-choropleth-map-and-upload-geojson-to-maptiler-cloud#PrepareGeoJSONwithattributesforchoroplethmapanduploadGeoJSONtoMapTilerCloud-UploadGeoJSONtoMapTilerCloud){:target="_blank" rel="noopener"} tutorial). Publish the dataset and copy the link to the geojson. Download the [GeoJSON multigeometries sample data](/sdk-js/assets/geoJSON_multigeometries.geojson){:target="_blank" rel="noopener"}.

<pre class="line-numbers" data-start="52" data-line-offset="51" data-line="52-55"><code class="language-js">

const geojsonOverlay = new ol.source.Vector({

url: `https://api.maptiler.com/data/YOUR_MAPTILER_DATASET_ID_HERE/features.json?key=${key}`,

format: new ol.format.GeoJSON(),

});

</code></pre>

1. Create the styles. Create one style for each geometry type: point, line, polygon, etc.

<pre class="line-numbers" data-start="56" data-line-offset="55" data-line="56-126"><code class="language-js">

const styles = {

'Point': new ol.style.Style({

image: new ol.style.Circle({

radius: 7,

fill: new ol.style.Fill({

color: 'rgb(68, 138, 255)',

}),

stroke: new ol.style.Stroke({color: '#fff', width: 4}),

}),

}),

'LineString': new ol.style.Style({

stroke: new ol.style.Stroke({

color: 'rgb(68, 138, 255)',

width: 3,

}),

}),

'MultiLineString': new ol.style.Style({

stroke: new ol.style.Stroke({

color: 'rgb(68, 138, 255)',

width: 3,

}),

}),

'MultiPoint': new ol.style.Style({

image: new ol.style.Circle({

radius: 5,

fill: null,

stroke: new ol.style.Stroke({color: 'red', width: 1}),

}),

}),

'MultiPolygon': new ol.style.Style({

stroke: new ol.style.Stroke({

color: 'rgb(68, 138, 255)',

width: 3,

}),

fill: new ol.style.Fill({

color: 'rgba(255, 255, 255, 0.4)',

}),

}),

'Polygon': new ol.style.Style({

stroke: new ol.style.Stroke({

color: 'rgb(68, 138, 255)',

width: 3,

}),

fill: new ol.style.Fill({

color: 'rgba(255, 255, 255, 0.4)',

}),

}),

'GeometryCollection': new ol.style.Style({

stroke: new ol.style.Stroke({

color: 'rgb(68, 138, 255)',

width: 3,

}),

fill: new ol.style.Fill({

color: 'rgba(255, 255, 255, 0.4)',

}),

image: new ol.style.Circle({

radius: 5,

fill: null,

stroke: new ol.style.Stroke({color: 'red', width: 1}),

}),

}),

'Circle': new ol.style.Style({

stroke: new ol.style.Stroke({

color: 'rgb(68, 138, 255)',

width: 3,

}),

fill: new ol.style.Fill({

color: 'rgba(255, 255, 255, 0.4)',

}),

}),

};

</code></pre>

1. Create a function that returns the style depending on the type of geometry of the features in the GeoJSON

<pre class="line-numbers" data-start="127" data-line-offset="126" data-line="127-129"><code class="language-js">

const styleFunction = function (feature) {

return styles[feature.getGeometry().getType()];

};

</code></pre>

1. Add the vector layer.

<pre class="line-numbers" data-start="130" data-line-offset="129" data-line="130-134"><code class="language-js">

const geojsonOverlayLayer = new ol.layer.Vector({

source: geojsonOverlay,

style: styleFunction

});

map.addLayer(geojsonOverlayLayer);

</code></pre>

1. Fit the map view to the bounding box of the data.

<pre class="line-numbers" data-start="135" data-line-offset="134" data-line="135-137"><code class="language-js">

geojsonOverlay.once('featuresloadend', function() {

map.getView().fit(geojsonOverlay.getExtent());

});

</code></pre>

</div>

1. Import the new modules needed to add the new functionality.

<pre class="line-numbers" data-start="8" data-line-offset="7" data-line="8-14"><code class="language-js">

import VectorLayer from 'ol/layer/Vector.js';

import VectorSource from 'ol/source/Vector.js';

import Style from 'ol/style/Style.js';

import Stroke from 'ol/style/Stroke.js';

import Fill from 'ol/style/Fill.js';

import CircleStyle from 'ol/style/Circle.js';

import GeoJSON from 'ol/format/GeoJSON.js';

</code></pre>

1. Create GeoJSON source. The following snippet creates GeoJSON source hosted on MapTiler (check out the [How to Upload GeoJSON to MapTiler](/guides/maps-apis/maps-platform/prepare-geojson-with-attributes-for-choropleth-map-and-upload-geojson-to-maptiler-cloud#PrepareGeoJSONwithattributesforchoroplethmapanduploadGeoJSONtoMapTilerCloud-UploadGeoJSONtoMapTilerCloud){:target="_blank" rel="noopener"} tutorial). Publish the dataset and copy the link to the geojson. Download the [GeoJSON multigeometries sample data](/sdk-js/assets/geoJSON_multigeometries.geojson){:target="_blank" rel="noopener"}.

<pre class="line-numbers" data-start="44" data-line-offset="43" data-line="44-47"><code class="language-js">

const geojsonOverlay = new new VectorSource({

url: `https://api.maptiler.com/data/YOUR_MAPTILER_DATASET_ID_HERE/features.json?key=${key}`,

format: new GeoJSON(),

});

</code></pre>

1. Create the styles. Create one style for each geometry type: point, line, polygon, etc.

<pre class="line-numbers" data-start="49" data-line-offset="48" data-line="49-119"><code class="language-js">

const styles = {

'Point': new Style({

image: new Circle({

radius: 7,

fill: new Fill({

color: 'rgb(68, 138, 255)',

}),

stroke: new Stroke({color: '#fff', width: 4}),

}),

}),

'LineString': new Style({

stroke: new Stroke({

color: 'rgb(68, 138, 255)',

width: 3,

}),

}),

'MultiLineString': new Style({

stroke: new Stroke({

color: 'rgb(68, 138, 255)',

width: 3,

}),

}),

'MultiPoint': new Style({

image: new Circle({

radius: 5,

fill: null,

stroke: new Stroke({color: 'red', width: 1}),

}),

}),

'MultiPolygon': new Style({

stroke: new Stroke({

color: 'rgb(68, 138, 255)',

width: 3,

}),

fill: new Fill({

color: 'rgba(255, 255, 255, 0.4)',

}),

}),

'Polygon': new Style({

stroke: new Stroke({

color: 'rgb(68, 138, 255)',

width: 3,

}),

fill: new Fill({

color: 'rgba(255, 255, 255, 0.4)',

}),

}),

'GeometryCollection': new Style({

stroke: new Stroke({

color: 'rgb(68, 138, 255)',

width: 3,

}),

fill: new Fill({

color: 'rgba(255, 255, 255, 0.4)',

}),

image: new Circle({

radius: 5,

fill: null,

stroke: new Stroke({color: 'red', width: 1}),

}),

}),

'Circle': new Style({

stroke: new Stroke({

color: 'rgb(68, 138, 255)',

width: 3,

}),

fill: new Fill({

color: 'rgba(255, 255, 255, 0.4)',

}),

}),

};

</code></pre>

1. Create a function that returns the style depending on the type of geometry of the features in the GeoJSON

<pre class="line-numbers" data-start="121" data-line-offset="120" data-line="121-123"><code class="language-js">

const styleFunction = function (feature) {

return styles[feature.getGeometry().getType()];

};

</code></pre>

1. Add the vector layer.

<pre class="line-numbers" data-start="124" data-line-offset="123" data-line="124-128"><code class="language-js">

const geojsonOverlayLayer = new VectorLayer({

source: geojsonOverlay,

style: styleFunction

});

map.addLayer(geojsonOverlayLayer);

</code></pre>

1. Fit the map view to the bounding box of the data.

<pre class="line-numbers" data-start="129" data-line-offset="128" data-line="129-131"><code class="language-js">

geojsonOverlay.once('featuresloadend', function() {

map.getView().fit(geojsonOverlay.getExtent());

});

</code></pre>

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const geojsonOverlay = new ol.source.Vector({
      url: `https://api.maptiler.com/data/YOUR_MAPTILER_DATASET_ID_HERE/features.json?key=${key}`,
      format: new ol.format.GeoJSON(),
    });

    const styles = {
      'Point': new ol.style.Style({
        image: new ol.style.Circle({
          radius: 7,
          fill: new ol.style.Fill({
            color: 'rgb(68, 138, 255)',
          }),
          stroke: new ol.style.Stroke({ color: '#fff', width: 4 }),
        }),
      }),
      'LineString': new ol.style.Style({
        stroke: new ol.style.Stroke({
          color: 'rgb(68, 138, 255)',
          width: 3,
        }),
      }),
      'MultiLineString': new ol.style.Style({
        stroke: new ol.style.Stroke({
          color: 'rgb(68, 138, 255)',
          width: 3,
        }),
      }),
      'MultiPoint': new ol.style.Style({
        image: new ol.style.Circle({
          radius: 5,
          fill: null,
          stroke: new ol.style.Stroke({ color: 'red', width: 1 }),
        }),
      }),
      'MultiPolygon': new ol.style.Style({
        stroke: new ol.style.Stroke({
          color: 'rgb(68, 138, 255)',
          width: 3,
        }),
        fill: new ol.style.Fill({
          color: 'rgba(255, 255, 255, 0.4)',
        }),
      }),
      'Polygon': new ol.style.Style({
        stroke: new ol.style.Stroke({
          color: 'rgb(68, 138, 255)',
          width: 3,
        }),
        fill: new ol.style.Fill({
          color: 'rgba(255, 255, 255, 0.4)',
        }),
      }),
      'GeometryCollection': new ol.style.Style({
        stroke: new ol.style.Stroke({
          color: 'rgb(68, 138, 255)',
          width: 3,
        }),
        fill: new ol.style.Fill({
          color: 'rgba(255, 255, 255, 0.4)',
        }),
        image: new ol.style.Circle({
          radius: 5,
          fill: null,
          stroke: new ol.style.Stroke({ color: 'red', width: 1 }),
        }),
      }),
      'Circle': new ol.style.Style({
        stroke: new ol.style.Stroke({
          color: 'rgb(68, 138, 255)',
          width: 3,
        }),
        fill: new ol.style.Fill({
          color: 'rgba(255, 255, 255, 0.4)',
        }),
      }),
    };

    const styleFunction = function (feature) {
      return styles[feature.getGeometry().getType()];
    };

    const geojsonOverlayLayer = new ol.layer.Vector({
      source: geojsonOverlay,
      style: styleFunction
    });
    map.addLayer(geojsonOverlayLayer);

    geojsonOverlay.once('featuresloadend', function () {
      map.getView().fit(geojsonOverlay.getExtent());
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

            const geojsonOverlay = new ol.source.Vector({
              url: `https://api.maptiler.com/data/YOUR_MAPTILER_DATASET_ID_HERE/features.json?key=${key}`,
              format: new ol.format.GeoJSON(),
            });

            const styles = {
              'Point': new ol.style.Style({
                image: new ol.style.Circle({
                  radius: 7,
                  fill: new ol.style.Fill({
                    color: 'rgb(68, 138, 255)',
                  }),
                  stroke: new ol.style.Stroke({ color: '#fff', width: 4 }),
                }),
              }),
              'LineString': new ol.style.Style({
                stroke: new ol.style.Stroke({
                  color: 'rgb(68, 138, 255)',
                  width: 3,
                }),
              }),
              'MultiLineString': new ol.style.Style({
                stroke: new ol.style.Stroke({
                  color: 'rgb(68, 138, 255)',
                  width: 3,
                }),
              }),
              'MultiPoint': new ol.style.Style({
                image: new ol.style.Circle({
                  radius: 5,
                  fill: null,
                  stroke: new ol.style.Stroke({ color: 'red', width: 1 }),
                }),
              }),
              'MultiPolygon': new ol.style.Style({
                stroke: new ol.style.Stroke({
                  color: 'rgb(68, 138, 255)',
                  width: 3,
                }),
                fill: new ol.style.Fill({
                  color: 'rgba(255, 255, 255, 0.4)',
                }),
              }),
              'Polygon': new ol.style.Style({
                stroke: new ol.style.Stroke({
                  color: 'rgb(68, 138, 255)',
                  width: 3,
                }),
                fill: new ol.style.Fill({
                  color: 'rgba(255, 255, 255, 0.4)',
                }),
              }),
              'GeometryCollection': new ol.style.Style({
                stroke: new ol.style.Stroke({
                  color: 'rgb(68, 138, 255)',
                  width: 3,
                }),
                fill: new ol.style.Fill({
                  color: 'rgba(255, 255, 255, 0.4)',
                }),
                image: new ol.style.Circle({
                  radius: 5,
                  fill: null,
                  stroke: new ol.style.Stroke({ color: 'red', width: 1 }),
                }),
              }),
              'Circle': new ol.style.Style({
                stroke: new ol.style.Stroke({
                  color: 'rgb(68, 138, 255)',
                  width: 3,
                }),
                fill: new ol.style.Fill({
                  color: 'rgba(255, 255, 255, 0.4)',
                }),
              }),
            };

            const styleFunction = function (feature) {
              return styles[feature.getGeometry().getType()];
            };

            const geojsonOverlayLayer = new ol.layer.Vector({
              source: geojsonOverlay,
              style: styleFunction
            });
            map.addLayer(geojsonOverlayLayer);

            geojsonOverlay.once('featuresloadend', function () {
              map.getView().fit(geojsonOverlay.getExtent());
            });
    </script>
</body>
</html>
```
