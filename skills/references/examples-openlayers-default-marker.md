# Source: https://docs.maptiler.com/openlayers/examples/default-marker/

# Display a marker

This tutorial shows how to add the default marker to the map using OpenLayers.

1. To create a new marker using a Vector layer. The layer's data source will be a feature set. Create a feature of the type point at the Lng/Lat coordinates of the marker. Create a Style to load the marker image and finally add it to the current map using .addLayer() function. Download the [sample marker image](./marker-icon.png)

<pre class="line-numbers" data-start="42" data-line-offset="41" data-line="42-58"><code class="language-js">

const layer = new ol.layer.Vector({

source: new ol.source.Vector({

features: [

new ol.Feature({

geometry: new ol.geom.Point(ol.proj.fromLonLat([, ])),

})

]

}),

style: new ol.style.Style({

image: new ol.style.Icon({

anchor: [0.5, 1],

crossOrigin: 'anonymous',

src: 'marker-icon.png',

})

})

});

map.addLayer(layer);

</code></pre>

</div>

1. Import the new modules needed to add the new functionality.

<pre class="line-numbers" data-start="8" data-line-offset="7" data-line="8-13"><code class="language-js">

import VectorLayer from 'ol/layer/Vector.js';

import VectorSource from 'ol/source/Vector.js';

import Point from 'ol/geom/Point.js';

import Style from 'ol/style/Style.js';

import Icon from 'ol/style/Icon.js';

import Feature from 'ol/Feature.js';

</code></pre>

1. To create a new marker using a Vector layer. The layer's data source will be a feature set. Create a feature of the type point at the Lng/Lat coordinates of the marker. Create a Style to load the marker image and finally add it to the current map using .addLayer() function. Download the [sample marker image](./marker-icon.png)

<pre class="line-numbers" data-start="43" data-line-offset="42" data-line="43-59"><code class="language-js">

const layer = new VectorLayer({

source: new VectorSource({

features: [

new Feature({

geometry: new Point(fromLonLat([, ])),

})

]

}),

style: new Style({

image: new Icon({

anchor: [0.5, 1],

crossOrigin: 'anonymous',

src: 'marker-icon.png',

})

})

});

map.addLayer(layer);

</code></pre>

</div>

</div>

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const layer = new ol.layer.Vector({
      source: new ol.source.Vector({
        features: [
          new ol.Feature({
            geometry: new ol.geom.Point(ol.proj.fromLonLat([12.550343, 55.665957])),
          })
        ]
      }),
      style: new ol.style.Style({
        image: new ol.style.Icon({
          anchor: [0.5, 1],
          crossOrigin: 'anonymous',
          src: 'marker-icon.png',
        })
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
    <title>Display a marker</title>
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
                center: ol.proj.fromLonLat([12.550343, 55.665957]),
                zoom: 10
              })
            });

            const layer = new ol.layer.Vector({
              source: new ol.source.Vector({
                features: [
                  new ol.Feature({
                    geometry: new ol.geom.Point(ol.proj.fromLonLat([12.550343, 55.665957])),
                  })
                ]
              }),
              style: new ol.style.Style({
                image: new ol.style.Icon({
                  anchor: [0.5, 1],
                  crossOrigin: 'anonymous',
                  src: 'marker-icon.png',
                })
              })
            });
            map.addLayer(layer);
    </script>
</body>
</html>
```
