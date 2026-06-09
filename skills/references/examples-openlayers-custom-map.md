# Source: https://docs.maptiler.com/openlayers/examples/custom-map/

# Display a custom map

This example demonstrates how to display a custom map from MapTiler on a web page using OpenLayers.

To create your first custom map, check out the [How to create a custom map](/guides/general/how-to-create-custom-map/) tutorial.

2. Replace the TileJSON source URL with your custom map style. Check the [Publish the map](/guides/general/how-to-create-custom-map/#publish-the-map) section to get the URL of your custom style.

<pre class="line-numbers" data-start="18" data-line-offset="17" data-line="19"><code class="language-js">

const source = new ol.source.TileJSON({

url: `https://api.maptiler.com/maps/YOUR_CUSTOM_MAP_ID/tiles.json?key=${key}`, // source URL

tileSize: 512,

crossOrigin: 'anonymous'

});

</code></pre>

</div>

2. Replace the TileJSON source URL with your custom map style. Check the [Publish the map](/guides/general/how-to-create-custom-map/#publish-the-map) section to get the URL of your custom style.

<pre class="line-numbers" data-start="16" data-line-offset="15" data-line="17"><code class="language-js">

const source = new TileJSON({

url: `https://api.maptiler.com/maps/YOUR_CUSTOM_MAP_ID/tiles.json?key=${key}`, // source URL

tileSize: 512,

crossOrigin: 'anonymous'

});

</code></pre>

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript

```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Display a custom map</title>
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
                url: `https://api.maptiler.com/maps/YOUR_CUSTOM_MAP_ID/tiles.json?key=${key}`, // source URL
                tileSize: 512,
                crossOrigin: 'anonymous'
              });

              const map = new ol.Map({
                layers: [
                  new ol.layer.Tile({
                    source: source
                  })
                ],
                controls: ol.control.defaults.defaults({attribution: false}).extend([attribution]),
                target: 'map',
                view: new ol.View({
                  constrainResolution: true,
                  center: ol.proj.fromLonLat([10.989249486220501, 46.948652944430734]), // starting position [lng, lat]
                  zoom: 12 // starting zoom
                })
              });
    </script>
</body>
</html>
```
