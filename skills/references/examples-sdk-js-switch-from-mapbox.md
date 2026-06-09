# Source: https://docs.maptiler.com/sdk-js/examples/switch-from-mapbox/

# 

This tutorial shows the process of how to migrate/switch from Mapbox to MapTiler. If you are using Mapbox GL JS in an existing application, it is a straightforward task to update it and incorporate the MapTiler SDK JS. 

In the majority of cases, you can easily accomplish this by uninstalling the `mapbox-gl` package and installing the `@maptiler/sdk` package within your node packages. Additionally, you may need to modify the CDN links and replace instances of `mapboxgl` with `maptilersdk` throughout your TypeScript, JavaScript, and HTML/CSS code.

<iframe style="height: 400px; width: 100%" src="?key=&position=//"></iframe>

Next, we will see the main changes that must be made to migrate your application from Mapbox to Maptiler.

## Installation



<div class="tab-content cdn-steps" markdown="1">
1. Replace the JS and CSS import from CDN references.

    <h5>Mapbox GL JS</h5>

    <pre><code class="language-html"><!--
    <script src='https://api.mapbox.com/mapbox-gl-js//mapbox-gl.js'></script>
    <link href='https://api.mapbox.com/mapbox-gl-js//mapbox-gl.css' rel='stylesheet' />
    --></code></pre>

    <h5>MapTiler SDK JS</h5>

    <pre><code class="language-html"><!--
    <script src="https://cdn.maptiler.com/maptiler-sdk-js//maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js//maptiler-sdk.css" rel="stylesheet" />
    --></code></pre>
</div>

<div class="tab-content bundler-steps" markdown="1">
1. Uninstall `mapbox-gl` and install `@maptiler/sdk`

    <pre><code class="language-bash"><!--
    npm uninstall --save mapbox-gl
    npm install --save @maptiler/sdk 
    --></code></pre>
</div>

## Replace mapboxgl with maptilersdk

Look in your application and replace `mapboxgl` with `maptilersdk` in your TypeScript, JavaScript and HTML/CSS files. Some examples below

<h5>Mapbox GL JS</h5>

<pre><code class="language-js"><!--
const map = new mapboxgl.Map({
  ....

const marker = new mapboxgl.Marker()
  ....
--></code></pre>

<h5>MapTiler SDK JS</h5>

<pre><code class="language-js"><!--
const map = new maptilersdk.Map({
  ....

const marker = new maptilersdk.Marker()
  ....
--></code></pre>

## Replace the api key or accessToken

Find `mapboxgl.accessToken` in the code and replace it with `maptilersdk.config.apiKey`. Replace your Mapbox accessToken with your actual [MapTiler API key](https://cloud.maptiler.com/account/keys/). 

<h5>Mapbox GL JS</h5>

<pre><code class="language-js"><!--
mapboxgl.accessToken = YOUR_MAPBOX_API_KEY_HERE;
--></code></pre>

<h5>MapTiler SDK JS</h5>

<pre><code class="language-js"><!--
maptilersdk.config.apiKey = YOUR_MAPTILER_API_KEY_HERE;
--></code></pre>

## Initialize the web map

<h5>Mapbox GL JS</h5>

With Mapbox GL JS, you initialize a new map like this:

<pre><code class="language-js"><!--
const map = new mapboxgl.Map({
  container: 'map', // container's id or the HTML element to render the map
  style: 'mapbox://styles/mapbox/streets-v12', // style URL
  center: [, ], // starting position [lng, lat]
  zoom:  // starting zoom
});
--></code></pre>

<h5>MapTiler SDK JS</h5>

You can initialize a map in a similar way using the MapTiler SDK JS

<pre><code class="language-js"><!--
const map = new maptilersdk.Map({
  container: 'map', // container's id or the HTML element to render the map
  style: maptilersdk.MapStyle.STREETS, // style URL
  center: [, ], // starting position [lng, lat]
  zoom: , // starting zoom
});
--></code></pre>

## Migrate the basemap styles

You can use the [MapTiler](https://www.maptiler.com/cloud/) service to provide the basemap for your application. There are different [Map styles](/sdk-js/api/map-styles/) to choose from such as streets, satellite imagery, outdoor, dataviz, OpenStreetMap, etc. Each style offers a range of variants that contain the same level of information and has the same purpose but use different color schemes like dark, light, etc. You can also create and use your custom basemap styles by using the [customize tool](https://www.maptiler.com/cloud/customize/) style editor.

##### Style equivalence

| **Mapbox**                                       | **MapTiler**                     |
|----------------------------------------------|------------------------------|
| `mapbox://styles/mapbox/streets-v12`           | `maptilersdk.MapStyle.STREETS` |
| `mapbox://styles/mapbox/outdoors-v12`          | `maptilersdk.MapStyle.OUTDOOR`             |
| `mapbox://styles/mapbox/light-v11`             | `maptilersdk.MapStyle.DATAVIZ.LIGHT`       |
| `mapbox://styles/mapbox/dark-v11`              | `maptilersdk.MapStyle.DATAVIZ.DARK`        |
| `mapbox://styles/mapbox/satellite-v9`          | `maptilersdk.MapStyle.SATELLITE`           |
| `mapbox://styles/mapbox/satellite-streets-v12` | `maptilersdk.MapStyle.HYBRID`              |

Checkout the list of [MapTiler SDK JS Map styles](/sdk-js/api/map-styles/#mapstylelist)

## Map controls

### Zoom and rotate controls

<h5>Mapbox GL JS</h5>

To display zoom and rotate controls, you must add the `NavigationControl` to the map.

<pre><code class="language-js"><!--
// Add zoom and rotation controls to the map.
map.addControl(new mapboxgl.NavigationControl());
--></code></pre>

<h5>MapTiler SDK JS</h5>

The zoom and rotate controls are **displayed by default** on the map. So there is **no need to add the `NavigationControl` to the map**.

### Geolocate control

<h5>Mapbox GL JS</h5>

To display the `GeolocateControl`, you must add the control to the map.

<pre><code class="language-js"><!--
// Add geolocate control to the map.
map.addControl(
  new mapboxgl.GeolocateControl({
    positionOptions: {
      enableHighAccuracy: true
    }
  })
);
--></code></pre>

<h5>MapTiler SDK JS</h5>

The geolocate control is **displayed by default** on the map. So there is **no need to add the `GeolocateControl` to the map**.

## Support for right-to-left languages

<h5>Mapbox GL JS</h5>

To support right-to-left languages such as Arabic and Hebrew you need to add and use the `mapbox-gl-rtl-text` plugin.

<pre><code class="language-js"><!--
mapboxgl.setRTLTextPlugin(
  'https://api.mapbox.com/mapbox-gl-js/plugins/mapbox-gl-rtl-text//mapbox-gl-rtl-text.js',
  null,
  true // Lazy load the plugin
);
--></code></pre>

<h5>MapTiler SDK JS</h5>

Right-to-left languages are **supported by default** so there is **no need to add any plugins**.

## Change the map's language

<h5>Mapbox GL JS</h5>

<h6>Change the map language dynamically</h6>

To change the map language dynamically you have to use the `setLayoutProperty` method for each of the text layers you have on the map and change the `text-field` property. This forces you to review the style, find the IDs of the text layers and execute the function for each layer. To avoid doing this you can use the `mapbox-gl-language` plugin.

<pre><code class="language-js"><!--
// Use setLayoutProperty to set the value of a layout property in a style layer.
// The three arguments are the id of the layer, the name of the layout property,
// and the new property value.
map.setLayoutProperty('country-label', 'text-field', [
  'get',
  `name_${language}`
]);
map.setLayoutProperty('continent-label', 'text-field', [
  'get',
  `name_${language}`
]);
map.setLayoutProperty('state-label', 'text-field', [
  'get',
  `name_${language}`
]);
...
--></code></pre>

<h6>Change the default map language</h6>

By default, will not set a language so that the language of Mapbox tiles will be determined by the vector tile source's TileJSON. To change the default map language (or initial map language), you have to go into Mapbox Studio and modify the map style. You have to do this for each style.

If you want to force the initial language of the map you can do it in the map constructor.

<pre class="line-numbers" data-start="1" data-line-offset="0" data-line="7"><code class="language-js"><!--
//change the map language to German
const map = new mapboxgl.Map({
  container: 'map', // container's id or the HTML element to render the map
  style: 'mapbox://styles/mapbox/streets-v12', // style URL
  center: [, ], // starting position [lng, lat]
  zoom:  // starting zoom
  language: "de"
});
--></code></pre>

<h5>MapTiler SDK JS</h5>

<h6>Change the map language dynamically</h6>

To change the map language dynamically just call the method `setLanguage`. There's **no need to add any plugins** or search for all text layers and change the `text-filed` property. The **SDK does all this automatically** for you.

<pre><code class="language-js"><!--
//change the map language to French
map.setLanguage(maptilersdk.Language.FRENCH);
--></code></pre>

<h6>Change the default map language</h6>

The SDK detects the language of the browser and displays the map in that language. There is **no need to modify the style or load any plugin**. Check the documentation about [languages](/sdk-js/api/languages/). If you want to define the initial language of the map, just set the language in the **map constructor options**.

<pre class="line-numbers" data-start="1" data-line-offset="0" data-line="7"><code class="language-js"><!--
//change the map language to German
const map = new maptilersdk.Map({
  container: 'map', // container's id or the HTML element to render the map
  style: maptilersdk.MapStyle.STREETS,
  center: [, ], // starting position [lng, lat]
  zoom: , // starting zoom
  language: maptilersdk.Language.GERMAN
});
--></code></pre>

## Add 3D terrain to a map

<h5>Mapbox GL JS</h5>

To add the 3D terrain to a map you have to first add a data source of type `raster-dem` and then call the map's `setTerrain` function.

To activate and deactivate the terrain dynamically you have to **create your own control** or **add some plugin**.

<pre><code class="language-js"><!--
map.on('style.load', () => {
  map.addSource('mapbox-dem', {
    'type': 'raster-dem',
    'url': 'mapbox://mapbox.mapbox-terrain-dem-v1',
    'tileSize': 512,
    'maxzoom': 14
  });
  // add the DEM source as a terrain layer with exaggerated height
  map.setTerrain({ 'source': 'mapbox-dem', 'exaggeration': 1.5 });
});
--></code></pre>

<h5>MapTiler SDK JS</h5>

To add the 3D terrain to a map just set the `terrain: true` in the **map constructor options**. To activate and deactivate the terrain dynamically add the `terrainControl: true` in the map constructor options. There's **no need** to add a data source, add some plugin or create your own terrain control.

<pre class="line-numbers" data-start="1" data-line-offset="0" data-line="7, 8"><code class="language-js"><!--
//add the 3D terrain and the terrainControl
const map = new maptilersdk.Map({
  container: 'map', // container's id or the HTML element to render the map
  style: maptilersdk.MapStyle.STREETS,
  center: [, ], // starting position [lng, lat]
  zoom: , // starting zoom
  terrain: true, 
  terrainControl: true,
});
--></code></pre>

## Geocoding control

How to easily switch to MapTiler Geocoding from any other provider.

<h5>Mapbox GL JS</h5>

<pre><code class="language-html"><!--
<link href="https://api.mapbox.com/mapbox-gl-js//mapbox-gl.css" rel="stylesheet">
<script src="https://api.mapbox.com/mapbox-gl-js//mapbox-gl.js"></script>
--></code></pre>

<pre><code class="language-js"><!--
// Add the control to the map.
map.addControl(
    new MapboxGeocoder({
        accessToken: mapboxgl.accessToken,
        mapboxgl: mapboxgl
    })
);
--></code></pre>

<h5>MapTiler SDK JS</h5>

Check out the [MapTiler Geocoding control](https://docs.maptiler.com/sdk-js/modules/geocoding/) documentation to see all the usage options such as React, Svelte, MapLibre, etc.

<pre><code class="language-html"><!--
<script src="https://cdn.maptiler.com/maptiler-geocoding-control//maptilersdk.umd.js"></script>
<link href="https://cdn.maptiler.com/maptiler-geocoding-control//style.css" rel="stylesheet">
--></code></pre>

<pre><code class="language-js"><!--
// Add the control to the map.
const gc = new maptilersdkMaptilerGeocoder.GeocodingControl();
map.addControl(gc);
--></code></pre>

## Geocoding API

<h5>Mapbox</h5>

Check out the official Mapbox Geocoding API documentation to see all the options.

<h6>Forward</h6>

<div class="card">
  <div class="card-body">
    <span class="badge bg-success fw-bolder text-uppercase">get</span> <code class="language-plaintext"><!--
https://api.mapbox.com/search/geocode/v6/forward?q={query}
--></code>
  </div>
</div>

<h6>Reverse</h6>

<div class="card">
  <div class="card-body">
    <span class="badge bg-success fw-bolder text-uppercase">get</span> <code class="language-plaintext"><!--
https://api.mapbox.com/search/geocode/v6/reverse?longitude={longitude}&latitude={latitude}
--></code>
  </div>
</div>

<h5>MapTiler</h5>

Check out the official [MapTiler Geocoding API](/cloud/api/geocoding/) documentation to see all the options.

<h6>Forward</h6>

<div class="card">
  <div class="card-body">
    <span class="badge bg-success fw-bolder text-uppercase">get</span> <code class="language-plaintext"><!--
https://api.maptiler.com/geocoding/{query}.json
--></code>
  </div>
</div>

<h6>Reverse</h6>

<div class="card">
  <div class="card-body">
    <span class="badge bg-success fw-bolder text-uppercase">get</span> <code class="language-plaintext"><!--
https://api.maptiler.com/geocoding/{longitude},{latitude}.json
--></code>
  </div>
</div>

