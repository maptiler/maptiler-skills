# Source: https://docs.maptiler.com/sdk-js/examples/3d-map/

# Display a 3D Map

This tutorial demonstrates how to create a 3D (three-dimensional) terrain map and display it on a web page using MapTiler.

Enhance the authenticity of your applications and data by incorporating terrain relief into your maps. This will provide a greater sense of realism and depth to your visuals.

<div class="tab-common-content" markdown="1">

1. Add options to the map to load the terrain elevation to the map.

<pre class="line-numbers" data-start="18" data-line-offset="17" data-line="23"><code class="language-js">

const map = new maptilersdk.Map({

container: 'map', // container id

style: ,

center: [, ], // starting position [lng, lat]

zoom: , // starting zoom

terrain: true,

});

</code></pre>

1. Add options to the map to load the terrain control to the map. The `terrainControl` shows a button to enable/disable the 3D terrain (does not tilt the map).

<pre class="line-numbers" data-start="18" data-line-offset="17" data-line="24"><code class="language-js">

const map = new maptilersdk.Map({

container: 'map', // container id

style: ,

center: [, ], // starting position [lng, lat]

zoom: , // starting zoom

terrain: true,

terrainControl: true,

});

</code></pre>

1. Add options to the map to load the map with a 3D view.

<pre class="line-numbers" data-start="18" data-line-offset="17" data-line="25-28"><code class="language-js">

const map = new maptilersdk.Map({

container: 'map', // container id

style: ,

center: [, ], // starting position [lng, lat]

zoom: , // starting zoom

terrain: true,

terrainControl: true,

pitch: 70,

bearing: -100.86,

maxPitch: 85,

maxZoom: 14

});

</code></pre>

</div>

<div class="tab-content cdn-steps" markdown="1">

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
    <title>Display a 3D Map</title>
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
            style: maptilersdk.MapStyle.OUTDOOR,
            center: [8.94738, 45.97812],
            zoom: 14,
            pitch: 70,
            bearing: -100.86
        });


    </script>
</body>
</html>
```
