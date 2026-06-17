# Source: https://docs.maptiler.com/openlayers/examples/raster-layer/

# Display a raster image

This OpenLayers tutorial demonstrates how to add a raster image overlay to a map. You will learn how to load and display a single image on specific map areas

1. Create a static image layer using the ImageStatic source. Set the image imageExtent Lng/Lat bounds. Here you can get the example image [aerial_wgs84.png](img/aerial_wgs84.png)

<pre class="line-numbers" data-start="43" data-line-offset="42" data-line="43-50"><code class="language-js">

const layer = new ol.layer.Image({

source: new ol.source.ImageStatic({

url: './aerial_wgs84.png',

projection: 'EPSG:4326',

imageExtent: [4.639663696289062, 50.89935199434383, 4.642066955566406, 50.900867668253724],

}),

})

map.addLayer(layer);

</code></pre>

</div>

1. Import the new modules needed to add the new functionality.

<pre class="line-numbers" data-start="1" data-line-offset="0" data-line="4, 6"><code class="language-js">

import Map from 'ol/Map.js';

import View from 'ol/View.js';

import TileLayer from 'ol/layer/Tile.js';

import ImageLayer from 'ol/layer/Image.js';

import TileJSON from 'ol/source/TileJSON.js';

import Static from 'ol/source/ImageStatic.js';

import Attribution from 'ol/control/Attribution.js';

import { defaults as defaultControls } from 'ol/control/defaults.js';

import { fromLonLat } from 'ol/proj.js';

</code></pre>

1. Create a static image layer using the ImageStatic source. Set the image imageExtent Lng/Lat bounds. Here you can get the example image [aerial_wgs84.png](img/aerial_wgs84.png)

<pre class="line-numbers" data-start="38" data-line-offset="37" data-line="38-45"><code class="language-js">

const layer = new Image({

source: new Static({

url: './aerial_wgs84.png',

projection: 'EPSG:4326',

imageExtent: [4.639663696289062, 50.89935199434383, 4.642066955566406, 50.900867668253724],

}),

})

map.addLayer(layer);

</code></pre>

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const layer = new ol.layer.Image({
      source: new ol.source.ImageStatic({
        url: './aerial_wgs84.png',
        projection: 'EPSG:4326',
        imageExtent: [4.639663696289062, 50.89935199434383, 4.642066955566406, 50.900867668253724],
      }),
    })
    map.addLayer(layer);
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Display a raster image</title>
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

            const source = new ol.source.TileJSON({
              url: `https://api.maptiler.com/maps/streets-v4/tiles.json?key=${key}`,
              tileSize: 512,
              crossOrigin: 'anonymous'
            });

            const attribution = new ol.control.Attribution({
              collapsible: false,
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
                center: ol.proj.fromLonLat([4.64086758, 50.9001362]),
                zoom: 18
              })
            });
            const layer = new ol.layer.Image({
              source: new ol.source.ImageStatic({
                url: './aerial_wgs84.png',
                projection: 'EPSG:4326',
                imageExtent: [4.639663696289062, 50.89935199434383, 4.642066955566406, 50.900867668253724],
              }),
            })
            map.addLayer(layer);
    </script>
</body>
</html>
```
