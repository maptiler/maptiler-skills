# Source: https://docs.maptiler.com/openlayers/examples/geojson-points/

# Display points from a GeoJSON Layer

This tutorial shows how to add a Point GeoJSON overlay to the map using OpenLayers.

<div class="tab-common-content" markdown="1">

1. To follow this tutorial you can use Airports from Natural Earth. [Download the Airports from Natural Earth](https://www.naturalearthdata.com/downloads/10m-cultural-vectors/airports/){:target="_blank" rel="noopener"}

1. Open the data tab on [MapTiler](https://cloud.maptiler.com/data/){:target="_blank" rel="noopener"} choose a new dataset - upload dataset and upload ne_10m_airports.shp.

1. Publish the dataset and copy the link to the geojson.

</div>

1. Create GeoJSON layer. The following snippet creates GeoJSON layer from an external file with point geometry.

<pre class="line-numbers" data-start="43" data-line-offset="42" data-line="43-59"><code class="language-js"><!--

const AirportLayer = new ol.layer.Vector({

source: new ol.source.Vector({

url: `https://api.maptiler.com/data/YOUR_MAPTILER_DATASET_ID_HERE/features.json?key=${key}`,

format: new ol.format.GeoJSON(),

}),

style: ...

})

--></code></pre>

1. Add style to this layer. Here you can get the example image [icon-plane-512.png](icon-plane-512.png)

<pre class="line-numbers" data-start="48" data-line-offset="47" data-line="48-54"><code class="language-js"><!--

style:  new ol.style.Style({

image: new ol.style.Icon({

src: './icon-plane-512.png',

size: [512, 512],

scale: 0.03

})

})

--></code></pre>

1. Display the layer.

<pre class="line-numbers" data-start="56" data-line-offset="55" data-line="56"><code class="language-js"><!--

map.addLayer(AirportLayer);

--></code></pre>

</div>

1. Import the new modules needed to add the new functionality.

<pre class="line-numbers" data-start="8" data-line-offset="7" data-line="8-12"><code class="language-js">

import VectorLayer from 'ol/layer/Vector.js';

import VectorSource from 'ol/source/Vector.js';

import Style from 'ol/style/Style.js';

import Icon from 'ol/style/Icon.js';

import GeoJSON from 'ol/format/GeoJSON.js';

</code></pre>

1. Create GeoJSON layer. The following snippet creates GeoJSON layer from an external file with point geometry.

<pre class="line-numbers" data-start="43" data-line-offset="42" data-line="43-59"><code class="language-js"><!--

const AirportLayer = new VectorLayer({

source: new VectorSource({

url: `https://api.maptiler.com/data/YOUR_MAPTILER_DATASET_ID_HERE/features.json?key=${key}`,

format: GeoJSON(),

}),

style: ...

})

--></code></pre>

1. Add style to this layer. Here you can get the example image [icon-plane-512.png](icon-plane-512.png)

<pre class="line-numbers" data-start="48" data-line-offset="47" data-line="48-54"><code class="language-js"><!--

style:  new Style({

image: new Icon({

src: './icon-plane-512.png',

size: [512, 512],

scale: 0.03

})

})

--></code></pre>

1. Display the layer.

<pre class="line-numbers" data-start="56" data-line-offset="55" data-line="56"><code class="language-js"><!--

map.addLayer(AirportLayer);

--></code></pre>

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const AirportLayer = new ol.layer.Vector({
      source: new ol.source.Vector({
        url: `https://api.maptiler.com/data/YOUR_MAPTILER_DATASET_ID_HERE/features.json?key=${key}`,
        format: new ol.format.GeoJSON(),
      }),
      style: new ol.style.Style({
        image: new ol.style.Icon({
          src: './icon-plane-512.png',
          size: [512, 512],
          scale: 0.03
        })
      })
    });

    map.addLayer(AirportLayer);
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Display points from a GeoJSON Layer</title>
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

            const AirportLayer = new ol.layer.Vector({
              source: new ol.source.Vector({
                url: `https://api.maptiler.com/data/YOUR_MAPTILER_DATASET_ID_HERE/features.json?key=${key}`,
                format: new ol.format.GeoJSON(),
              }),
              style: new ol.style.Style({
                image: new ol.style.Icon({
                  src: './icon-plane-512.png',
                  size: [512, 512],
                  scale: 0.03
                })
              })
            });

            map.addLayer(AirportLayer);
    </script>
</body>
</html>
```
