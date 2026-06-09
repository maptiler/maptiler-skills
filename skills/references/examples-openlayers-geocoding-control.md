# Source: https://docs.maptiler.com/openlayers/examples/geocoding-control/

# MapTiler Geocoding control

This tutorial shows how to search for places using MapTiler geocoding control in [OpenLayers](/openlayers/){:target="\_blank" rel="noopener"}. The geocoding control facilitates the use of the [MapTiler Geocoding API](https://www.maptiler.com/cloud/geocoding/){:target="\_blank" rel="noopener"}.

1. Include the geocoder component JavaScript and CSS files in the `<head>` of your HTML file.

<pre class="line-numbers" data-start="8" data-line-offset="7" data-line="8"><code class="language-html"><!--

<script src="https://cdn.maptiler.com/maptiler-geocoding-control//openlayers.umd.js"></script>

--></code></pre>

1. Instantiate the geocoding control and add it to the map.

<pre class="line-numbers" data-start="51" data-line-offset="50" data-line="51-55"><code class="language-js"><!--

const gc = new maptilerGeocoder.GeocodingControl({

apiKey: key,

});

map.addControl(gc);

--></code></pre>

1. Create the `GeocodingControl` CSS style. Add the GeocodingControl style to your stylesheet.

<pre class="line-numbers" data-start="12" data-line-offset="11" data-line="12-16"><code class="language-css"><!--

.openlayers-ctrl-geocoder {

position: absolute;

right: 0.5em;

top: 0.5em;

}

--></code></pre>

</div>

1. Include the geocoder component JavaScript and CSS files in your JS file.

<pre class="line-numbers" data-start="8" data-line-offset="7" data-line="8"><code class="language-js"><!--

import { GeocodingControl } from "@maptiler/geocoding-control/openlayers";

--></code></pre>

1. Instantiate the geocoding control and add it to the map.

<pre class="line-numbers" data-start="38" data-line-offset="37" data-line="38-42"><code class="language-js"><!--

const gc = new GeocodingControl({

apiKey: key,

});

map.addControl(gc);

--></code></pre>

1. Create the `GeocodingControl` CSS style. Add the GeocodingControl style to your stylesheet.

<pre><code class="language-css"><!--

.openlayers-ctrl-geocoder {

position: absolute;

right: 0.5em;

top: 0.5em;

}

--></code></pre>

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const gc = new maptilerGeocoder.GeocodingControl({
      apiKey: key,
    });

    map.addControl(gc);
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>MapTiler Geocoding control</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/ol@10.9.0/ol.css">
    <script src="https://cdn.jsdelivr.net/npm/ol@10.9.0/dist/ol.js"></script>
    <script src="https://cdn.maptiler.com/maptiler-geocoding-control/v3.0.0/openlayers.umd.js"></script>
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
              url: `https://api.maptiler.com/maps/streets-v4/tiles.json?key=${key}`, // source URL
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
                center: ol.proj.fromLonLat([16.62662018, 49.2125578]), // starting position [lng, lat]
                zoom: 14 // starting zoom
              })
            });

            const gc = new maptilerGeocoder.GeocodingControl({
              apiKey: key,
            });

            map.addControl(gc);
    </script>
</body>
</html>
```
