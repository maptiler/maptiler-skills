# Source: https://docs.maptiler.com/sdk-js/examples/switch-from-maplibre/

# 

This tutorial provides guidance on transitioning or changing from MapLibre to MapTiler. If you currently utilize MapLibre GL JS in your application, updating it to use the MapTiler SDK JS is a straightforward process.

In most cases, you can simply uninstall `maplibre-gl` and install `@maptiler/sdk` in your node packages or change the CDN links. Additionally, you will need to replace all instances of `maplibregl` with `maptilersdk` in your TypeScript, JavaScript, and HTML/CSS code. This ensures a seamless integration of the MapTiler SDK JS into your existing application.

<iframe style="height: 400px; width: 100%" src="?key=&position=//"></iframe>

Next, we will see the main changes that must be made to migrate your application from MapLibre to MapTiler.

## Installation



<div class="tab-content cdn-steps" markdown="1">
1. Replace the JS and CSS import from CDN references.

    <h5>MapLibre GL JS</h5>

    <pre><code class="language-html"><!--
    <script src='https://unpkg.com/maplibre-gl@/dist/maplibre-gl.js'></script>
    <link href='https://unpkg.com/maplibre-gl@/dist/maplibre-gl.css' rel='stylesheet' />
    --></code></pre>

    <h5>MapTiler SDK JS</h5>

    <pre><code class="language-html"><!--
    <script src="https://cdn.maptiler.com/maptiler-sdk-js//maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js//maptiler-sdk.css" rel="stylesheet" />
    --></code></pre>

</div>

<div class="tab-content bundler-steps" markdown="1">
1. Uninstall `maplibre-gl` and install `@maptiler/sdk`

    <pre><code class="language-bash"><!--
    npm uninstall --save maplibre-gl
    npm install --save @maptiler/sdk
    --></code></pre>

</div>

## Replace maplibregl with maptilersdk

Look in your application and replace `maplibregl` with `maptilersdk` in your TypeScript, JavaScript and HTML/CSS files. Some examples below

<h5>MapLibre GL JS</h5>

<pre><code class="language-js"><!--
const map = new maplibregl.Map({
  ....

const marker = new maplibregl.Marker()
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

Find the variable where you store your actual [MapTiler API key](https://cloud.maptiler.com/account/keys/) in the code and replace it with `maptilersdk.config.apiKey`.

<h5>MapLibre GL JS</h5>

<pre><code class="language-js"><!--
const key = YOUR_MAPTILER_API_KEY_HERE;
--></code></pre>

<h5>MapTiler SDK JS</h5>

<pre><code class="language-js"><!--
maptilersdk.config.apiKey = YOUR_MAPTILER_API_KEY_HERE;
--></code></pre>

## Initialize the web map

<h5>MapLibre GL JS</h5>

With MapLibre GL JS, you initialize a new map like this:

<pre><code class="language-js"><!--
const map = new maplibregl.Map({
  container: 'map', // container's id or the HTML element to render the map
  style: `https://api.maptiler.com/maps/streets-v4/style.json?key=${key}`, // style URL
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

You can use the [MapTiler](https://www.maptiler.com/cloud/) service to provide the basemap for your application. There are different [Map styles](/sdk-js/api/map-styles/) to choose from such as streets, satellite imagery, outdoor, dataviz, OpenStreetMap, etc. Each style offers a range of variants that contain the same level of information and have the same purpose but use different color schemes like dark, light, etc. You can also create and use your own custom basemap styles by using the [customize tool](https://www.maptiler.com/cloud/customize/) style editor.

Checkout the list of [MapTiler SDK JS Map styles](/sdk-js/api/map-styles/#mapstylelist)

<h5>MapLibre GL JS</h5>

You need to write the full URL of the style. If we make an update to a style (new version), you have to modify your codebase to have the latest version of styles. You must put the API key in every URL.

<pre><code class="language-js"><!--
`https://api.maptiler.com/maps/streets-v4/style.json?key=${key}` // style URL
--></code></pre>

<h5>MapTiler SDK JS</h5>

Always use the latest version of styles. No need to type along style URL. No more putting the API key in every URL.

<pre><code class="language-js"><!--
`maptilersdk.MapStyle.STREETS` // style URL
--></code></pre>

## Map controls

### Zoom and rotate controls

<h5>MapLibre GL JS</h5>

To display zoom and rotate controls, you must add the `NavigationControl` to the map.

<pre><code class="language-js"><!--
// Add zoom and rotation controls to the map.
map.addControl(new maplibregl.NavigationControl());
--></code></pre>

<h5>MapTiler SDK JS</h5>

The zoom and rotate controls are **displayed by default** on the map. So there is **no need to add the `NavigationControl` to the map**.

### Geolocate control

<h5>MapLibre GL JS</h5>

To display the `GeolocateControl`, you must add the control to the map.

<pre><code class="language-js"><!--
// Add geolocate control to the map.
map.addControl(
  new maplibregl.GeolocateControl({
    positionOptions: {
      enableHighAccuracy: true
    }
  })
);
--></code></pre>

<h5>MapTiler SDK JS</h5>

The geolocate control is **displayed by default** on the map. So there is **no need to add the `GeolocateControl` to the map**.

## Support for right-to-left languages

<h5>MapLibre GL JS</h5>

To support right-to-left languages such as Arabic and Hebrew you need to add and use the `mapbox-gl-rtl-text` plugin.

<pre><code class="language-js"><!--
maplibregl.setRTLTextPlugin(
  'https://api.mapbox.com/mapbox-gl-js/plugins/mapbox-gl-rtl-text//mapbox-gl-rtl-text.js',
  null,
  true // Lazy load the plugin
);
--></code></pre>

<h5>MapTiler SDK JS</h5>

Right-to-left languages are **supported by default** so there is **no need to add any plugins**.

## Change the map's language

<h5>MapLibre GL JS</h5>

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

To change the default map language (or initial map language), you have to go into the [MapTiler Map design tool](https://www.maptiler.com/cloud/customize/) and modify the map style. You have to do this for each style.

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

<h5>MapLibre GL JS</h5>

To add the 3D terrain to a map you have to first add a data source of type `raster-dem` and then call the map's `setTerrain` function.

To activate and deactivate the terrain dynamically you have to use the `TerrainControl`.

<pre><code class="language-js"><!--
map.on('style.load', () => {
  map.addSource('terrainSource', {
    'type': 'raster-dem',
    'url': `https://api.maptiler.com/tiles/terrain-rgb-v2/tiles.json?key=${key}`,
    'tileSize': 512,
    'maxzoom': 14
  });
  // add the DEM source as a terrain layer with exaggerated height
  map.setTerrain({ 'source': 'terrainSource', 'exaggeration': 1.5 });
  // add the TerrainControl
  map.addControl(
    new maplibregl.TerrainControl({
    source: 'terrainSource',
    exaggeration: 1
    })
  });
});
--></code></pre>

<h5>MapTiler SDK JS</h5>

To add the 3D terrain to a map just set the `terrain: true` in the **map constructor options**. To activate and deactivate the terrain dynamically add the `terrainControl: true` in the map constructor options. There's **no need** to add a data source or add the terrain control.

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

## MapTiler logo attribution

Free plan maps require the logo. It is required to place the MapTiler logo, with a link to https://maptiler.com/, on all maps in case you are not subscribed to any of the commercial plans of the Service. The MapTiler logo must be visible, readable and should appear in the left bottom corner of the map.

<h5>MapLibre GL JS</h5>

You **must have** something like this in your application to **comply** with the MapTiler **Terms and Conditions**.

<pre><code class="language-html"><!--
<div id="map">
  <a href="https://www.maptiler.com" style="position:absolute;left:10px;bottom:10px;z-index:999;">
    
  </a>
</div>
--></code></pre>

<h5>MapTiler SDK JS</h5>

The MapTiler logo attribution is **automatically added** to the map.

