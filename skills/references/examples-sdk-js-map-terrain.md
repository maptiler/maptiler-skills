# Source: https://docs.maptiler.com/sdk-js/examples/map-terrain/

# Enable/disable map terrain

This tutorial demonstrates how to programmatically enabling or disabling the 3D terrain map using SDK functions `map.enableTerrain()` and `map.disableTerrain()`.

The easiest and fastest way to create a map with 3D terrain is through the map options. Check out the tutorial [Display a 3D terrain map](../3d-map/) to learn more about it.

<sup>Click on the map to enable/disable the map terrain</sup>

<div class="tab-common-content" markdown="1">

1. Capture when the user clicks on the map. Add an event handler for the map click event. You will add the code to enable/disable the terrain in this handler.

<pre class="line-numbers" data-start="24" data-line-offset="23" data-line="24-26"><code class="language-js"><!--

map.on('click', async function() {

});

--></code></pre>

1. Check whether or not the terrain is enabled.

<pre class="line-numbers" data-start="24" data-line-offset="23" data-line="25-29"><code class="language-js"><!--

map.on('click', async function() {

if (map.hasTerrain()) {

} else {

}

});

--></code></pre>

1. Toggle the map terrain.

<pre class="line-numbers" data-start="24" data-line-offset="23" data-line="25-29"><code class="language-js"><!--

map.on('click', async function() {

if (map.hasTerrain()) {

map.disableTerrain();

} else {

map.enableTerrain();

}

});

--></code></pre>

1. Exaggerate the terrain. The `enableTerrain` function by default enables terrain with an exaggeration factor of 1 (actual values). This function also allows you to activate the terrain with a certain exaggeration factor. In this example, we will apply a factor of 1.5 to accentuate the terrain volume.

<pre class="line-numbers" data-start="24" data-line-offset="23" data-line="28"><code class="language-js"><!--

map.on('click', async function() {

if (map.hasTerrain()) {

map.disableTerrain();

} else {

map.enableTerrain(1.5);

}

});

--></code></pre>

1. Add an event handler for map terrain events. You will add the code to tilt/untilt the map in this handler.

<pre class="line-numbers" data-start="31" data-line-offset="30" data-line="31-33"><code class="language-js"><!--

map.on('terrain', async function() {

});

--></code></pre>

1. Toggle the map pitch.

<pre class="line-numbers" data-start="31" data-line-offset="30" data-line="32-36"><code class="language-js"><!--

map.on('terrain', async function() {

if (map.hasTerrain()) {

map.easeTo({ pitch: map.getMaxPitch(), duration: 2000 });

} else {

map.easeTo({ pitch: 0, duration: 2000 });

}

});

--></code></pre>

</div>

<div class="tab-content cdn-steps" markdown="1">

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element to render the map
        style: maptilersdk.MapStyle.WINTER,
        center: [-106.44336, 39.12108], // starting position [lng, lat]
        zoom: 11, // starting zoom
      });

      map.on('click', function() {
        if (map.hasTerrain()) {
          map.disableTerrain();
        } else {
          map.enableTerrain(1.5);
        }
      });

      map.on('terrain', function() {
        if (map.hasTerrain()) {
          map.easeTo({ pitch: map.getMaxPitch(), duration: 2000 });
        } else {
          map.easeTo({ pitch: 0, duration: 2000 });
        }
      });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Enable/disable map terrain</title>
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
            style: maptilersdk.MapStyle.WINTER,
            center: [-106.44336, 39.12108],
            zoom: 11,
            pitch: map.getMaxPitch()
        });

        container: 'map', // container's id or the HTML element to render the map
                style: maptilersdk.MapStyle.WINTER,
                center: [-106.44336, 39.12108], // starting position [lng, lat]
                zoom: 11, // starting zoom
              });

              map.on('click', function() {
                if (map.hasTerrain()) {
                  map.disableTerrain();
                } else {
                  map.enableTerrain(1.5);
                }
              });

              map.on('terrain', function() {
                if (map.hasTerrain()) {
                  map.easeTo({ pitch: map.getMaxPitch(), duration: 2000 });
                } else {
                  map.easeTo({ pitch: 0, duration: 2000 });
                }
              });
    </script>
</body>
</html>
```
