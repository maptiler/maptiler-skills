# Source: https://docs.maptiler.com/cesium/examples/how-to-use-cesium/

# Display a map in Cesium JS

In this step-by-step tutorial, you’ll learn how to create a [3D map](https://www.maptiler.com/maps/3d/){:target="\_blank" rel="noopener"} and display it on a web page. Together we will make a simple full-screen map application, serving as a practical example of how to seamlessly integrate MapTiler maps with Cesium into your web mapping application.

By the end of this tutorial, you will be able to develop a full-screen 3D globe map. Your final map will resemble the following example:

1. Create a basic HTML file.

<pre class="line-numbers"><code class="language-html"><!--

<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title></title>

<style>

body {

margin: 0;

padding: 0;

}

</style>

</head>

<body>

</body>

<script>

</script>

</html>

--></code></pre>

1. Include the Cesium JavaScript and CSS files in the `<head>` of your HTML file.

<pre class="line-numbers" data-start="6" data-line-offset="5" data-line="7,8"><code class="language-html"><!--

<title></title>

<script src="https://cesium.com/downloads/cesiumjs/releases//Build/Cesium/Cesium.js"></script>

<link href="https://cesium.com/downloads/cesiumjs/releases//Build/Cesium/Widgets/widgets.css" rel="stylesheet">

<style>

body {

margin: 0;

padding: 0;

}

</style>

--></code></pre>

1. Create a `<div>` element with a certain id where you want your map to be.

Add `<div>` tag to your page. This div will be the container where the map will be loaded.

<pre class="line-numbers" data-start="16" data-line-offset="15" data-line="17-19"><code class="language-html"><!--

<body>

<div id="cesiumContainer">

</div>

</body>

--></code></pre>

1. The div must have a non-zero height.

<pre class="line-numbers" data-start="10" data-line-offset="9" data-line="14"><code class="language-css">

body {

margin: 0;

padding: 0;

}

</code></pre>

1. Add the MapTiler logo to the map. Check the [MapTiler map data licenses](https://www.maptiler.com/copyright/)

<pre class="line-numbers" data-start="16" data-line-offset="15" data-line="17-19"><code class="language-html"><!--

<body>

<div id="cesiumContainer">

<a href="https://www.maptiler.com" style="position:absolute;right:10px;bottom:10px;z-index:999;"></a>

</div>

</body>

--></code></pre>

1. Initialize the Cesium Viewer in the HTML element with the id `cesiumContainer` and add attribution.

<pre class="line-numbers" data-start="22" data-line-offset="21" data-line="23-32"><code class="language-html"><!--

<script>

const viewer = new Cesium.Viewer('cesiumContainer', {

animation: false,

baseLayerPicker: false,

navigationHelpButton: false,

sceneModePicker: false,

homeButton: false,

geocoder: false,

fullscreenButton: false,

timeline: false,

});

const credit = new Cesium.Credit(`<a href="https://www.maptiler.com/copyright/" target="_blank">&copy; MapTiler</a> <a href="https://www.openstreetmap.org/copyright" target="_blank">&copy; OpenStreetMap contributors</a>`, true)

viewer.creditDisplay.addStaticCredit(credit);

</script>

--></code></pre>

1. Set the initial camera view to the given longitude, latitude, and height.

<pre class="line-numbers" data-start="23" data-line-offset="22" data-line="33-38"><code class="language-js"><!--

const viewer = new Cesium.Viewer('cesiumContainer', {

animation: false,

baseLayerPicker: false,

navigationHelpButton: false,

sceneModePicker: false,

homeButton: false,

geocoder: false,

fullscreenButton: false,

timeline: false,

});

viewer.camera.setView({

destination: Cesium.Cartesian3.fromDegrees(8.67, 46.72, 4500),

orientation: {

pitch: Cesium.Math.toRadians(-20)

}

});

--></code></pre>

1. Add the MapTier API Key.

<pre class="line-numbers" data-start="23" data-line-offset="22" data-line="23"><code class="language-js"><!--

const key = 'YOUR_MAPTILER_API_KEY_HERE';

const viewer = new Cesium.Viewer('cesiumContainer', {

animation: false,

baseLayerPicker: false,

navigationHelpButton: false,

sceneModePicker: false,

homeButton: false,

geocoder: false,

fullscreenButton: false,

timeline: false,

});

--></code></pre>

1. Add the [terrain](https://cesium.com/learn/cesiumjs/ref-doc/Terrain.html){:target="\_blank" rel="noopener"} to see the terrain in 3D. We will use the [Terrain 3D - Cesium quantized mesh](https://cloud.maptiler.com/tiles/terrain-quantized-mesh-v2/){:target="\_blank" rel="noopener"} as geometry for the terrain surface.

<pre class="line-numbers" data-start="24" data-line-offset="23" data-line="33-36"><code class="language-js"><!--

const viewer = new Cesium.Viewer('cesiumContainer', {

animation: false,

baseLayerPicker: false,

navigationHelpButton: false,

sceneModePicker: false,

homeButton: false,

geocoder: false,

fullscreenButton: false,

timeline: false,

terrain: new Cesium.Terrain(Cesium.CesiumTerrainProvider.fromUrl(`https://api.maptiler.com/tiles/terrain-quantized-mesh-v2/?key=${key}`, {

requestVertexNormals: true

}))

});

--></code></pre>

1. Add the [ImageryLayer](https://cesium.com/learn/cesiumjs/ref-doc/ImageryLayer.html){:target="\_blank" rel="noopener"} to provide the images to display on the terrain surface. We will use the [MapTiler Satellite services](https://www.maptiler.com/satellite/){:target="\_blank" rel="noopener"}. You can use any other map you have on [MapTiler maps](https://cloud.maptiler.com/maps/){:target="\_blank" rel="noopener"} as an imageProvider.

<pre class="line-numbers" data-start="24" data-line-offset="23" data-line="37-44"><code class="language-js"><!--

const viewer = new Cesium.Viewer('cesiumContainer', {

animation: false,

baseLayerPicker: false,

navigationHelpButton: false,

sceneModePicker: false,

homeButton: false,

geocoder: false,

fullscreenButton: false,

timeline: false,

terrain: new Cesium.Terrain(Cesium.CesiumTerrainProvider.fromUrl(`https://api.maptiler.com/tiles/terrain-quantized-mesh-v2/?key=${key}`, {

requestVertexNormals: true

}))

baseLayer: new Cesium.ImageryLayer( new Cesium.UrlTemplateImageryProvider({

url: `https://api.maptiler.com/maps/satellite-v4/{z}/{x}/{y}.jpg?key=${key}`,

minimumLevel: 0,

maximumLevel: 20,

tileWidth: 512,

tileHeight: 512,

})),

});

--></code></pre>

</div>

1. Install the npm package.

<pre><code class="language-bash"><!--

npm install --save cesium

--></code></pre>

1. Create the cesiumContainer style. Add the cesiumContainer style to your stylesheet. The div must have non-zero height.

<pre id="import-css-code"><code class="language-css"><!--

body {

margin: 0;

padding: 0;

}

--></code></pre>

1. Create a `<div>` element with a certain id where you want your map to be.

Add `<div>` tag into your page. This div will be the container where the map will be loaded.

<pre><code class="language-html"><!--

<div id="cesiumContainer"></div>

--></code></pre>

1. Include the CSS file.

If you have a bundler that can handle CSS, you can import the CSS from ol/ol.css.

<pre><code class="language-js"><!--

import 'cesium/Build/Cesium/Widgets/widgets.css';

--></code></pre>

> [!INFO]

> Including the CSS file using a `<link>` in the head of the document via the CDN is the easiest way.

> >

> ```html liquid

> <link href="https://cesium.com/downloads/cesiumjs/releases//Build/Cesium/Widgets/widgets.css" rel="stylesheet">

> ```

>

1. Add the MapTiler logo to the map. Check the [MapTiler map data licenses](https://www.maptiler.com/copyright/)

<pre><code class="language-html"><!--

<div id="cesiumContainer">

<a href="https://www.maptiler.com" style="position:absolute;right:10px;bottom:10px;z-index:999;"></a>

</div>

--></code></pre>

1. Initialize the Cesium Viewer in the HTML element with the id `cesiumContainer` and add attribution.

<pre class="line-numbers"><code class="language-js"><!--

import { Viewer } from 'cesium';

import 'cesium/Build/Cesium/Widgets/widgets.css';

const viewer = new Viewer('cesiumContainer', {

animation: false,

baseLayerPicker: false,

navigationHelpButton: false,

sceneModePicker: false,

homeButton: false,

geocoder: false,

fullscreenButton: false,

timeline: false,

});

const credit = new Cesium.Credit(`<a href="https://www.maptiler.com/copyright/" target="_blank">&copy; MapTiler</a> <a href="https://www.openstreetmap.org/copyright" target="_blank">&copy; OpenStreetMap contributors</a>`, true)

viewer.creditDisplay.addStaticCredit(credit);

--></code></pre>

1. Update imports

<pre class="line-numbers" data-start="1" data-line-offset="0" data-line="1"><code class="language-js"><!--

import { Viewer, Cartesian3, Math as CesiumMath } from 'cesium';

--></code></pre>

1. Set the initial camera view to the given longitude, latitude, and height.

<pre class="line-numbers" data-start="15" data-line-offset="14" data-line="15-20"><code class="language-js"><!--

viewer.camera.setView({

destination: Cartesian3.fromDegrees(8.67, 46.72, 4500),

orientation: {

pitch: CesiumMath.toRadians(-20)

}

});

--></code></pre>

1. Add the MapTier API Key.

<pre class="line-numbers" data-start="3" data-line-offset="2" data-line="3"><code class="language-js"><!--

const key = 'YOUR_MAPTILER_API_KEY_HERE';

const viewer = new Viewer('cesiumContainer', {

animation: false,

baseLayerPicker: false,

navigationHelpButton: false,

sceneModePicker: false,

homeButton: false,

geocoder: false,

fullscreenButton: false,

timeline: false,

});

--></code></pre>

1. Update imports

<pre class="line-numbers" data-start="1" data-line-offset="0" data-line="1"><code class="language-js"><!--

import { Viewer, Cartesian3, Math as CesiumMath, Terrain, CesiumTerrainProvider, Credit } from 'cesium';

--></code></pre>

1. Add the [terrain](https://cesium.com/learn/cesiumjs/ref-doc/Terrain.html){:target="\_blank" rel="noopener"} to see the terrain in 3D. We will use the [Terrain 3D - Cesium quantized mesh](https://cloud.maptiler.com/tiles/terrain-quantized-mesh-v2/){:target="\_blank" rel="noopener"} as geometry for the terrain surface.

<pre class="line-numbers" data-start="4" data-line-offset="3" data-line="13-16"><code class="language-js"><!--

const viewer = new Viewer('cesiumContainer', {

animation: false,

baseLayerPicker: false,

navigationHelpButton: false,

sceneModePicker: false,

homeButton: false,

geocoder: false,

fullscreenButton: false,

timeline: false,

terrain: new Terrain(CesiumTerrainProvider.fromUrl(`https://api.maptiler.com/tiles/terrain-quantized-mesh-v2/?key=${key}`, {

requestVertexNormals: true

})),

});

--></code></pre>

1. Update imports

<pre class="line-numbers" data-start="1" data-line-offset="0" data-line="1"><code class="language-js"><!--

import { Viewer, Cartesian3, Math as CesiumMath, Terrain, CesiumTerrainProvider, Credit, ImageryLayer, UrlTemplateImageryProvider } from 'cesium';

--></code></pre>

1. Add the [ImageryLayer](https://cesium.com/learn/cesiumjs/ref-doc/ImageryLayer.html){:target="\_blank" rel="noopener"} to provide the images to display on the terrain surface. We will use the [MapTiler Satellite services](https://www.maptiler.com/satellite/){:target="\_blank" rel="noopener"}. You can use any other map you have on [MapTiler maps](https://cloud.maptiler.com/maps/){:target="\_blank" rel="noopener"} as an imageProvider.

<pre class="line-numbers" data-start="4" data-line-offset="3" data-line="17-24"><code class="language-js"><!--

const viewer = new Viewer('cesiumContainer', {

animation: false,

baseLayerPicker: false,

navigationHelpButton: false,

sceneModePicker: false,

homeButton: false,

geocoder: false,

fullscreenButton: false,

timeline: false,

terrain: new Terrain(CesiumTerrainProvider.fromUrl(`https://api.maptiler.com/tiles/terrain-quantized-mesh-v2/?key=${key}`, {

requestVertexNormals: true

})),

baseLayer: new ImageryLayer( new UrlTemplateImageryProvider({

url: `https://api.maptiler.com/maps/satellite-v4/{z}/{x}/{y}.jpg?key=${key}`,

minimumLevel: 0,

maximumLevel: 20,

tileWidth: 512,

tileHeight: 512,

})),

});

--></code></pre>

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
    <title>Display a map in Cesium JS</title>
    <script src="https://cesium.com/downloads/cesiumjs/releases/1.141.0/Build/Cesium/Cesium.js"></script>
    <link href="https://cesium.com/downloads/cesiumjs/releases/1.141.0/Build/Cesium/Widgets/widgets.css" rel="stylesheet">
    <style>
        body { margin: 0; padding: 0; }
        #cesiumContainer { position: absolute; top: 0; bottom: 0; width: 100%; }
    </style>
</head>
<body>
    <div id="cesiumContainer"></div>
    <script>
        const key = 'YOUR_MAPTILER_API_KEY';
          const viewer = new Cesium.Viewer('cesiumContainer', {
            animation: false,
            baseLayerPicker: false,
            navigationHelpButton: false,
            sceneModePicker: false,
            homeButton: false,
            geocoder: false,
            fullscreenButton: false,
            timeline: false,
            terrain: new Cesium.Terrain(Cesium.CesiumTerrainProvider.fromUrl(`https://api.maptiler.com/tiles/terrain-quantized-mesh-v2/?key=${key}`, {
              requestVertexNormals: true
            })),
            baseLayer: new Cesium.ImageryLayer(new Cesium.UrlTemplateImageryProvider({
              url: `https://api.maptiler.com/maps/satellite-v4/{z}/{x}/{y}.jpg?key=${key}`,
              minimumLevel: 0,
              maximumLevel: 20,
              tileWidth: 512,
              tileHeight: 512,
            })),
          });
          const credit = new Cesium.Credit(`<a href="https://www.maptiler.com/copyright/" target="_blank">&copy; MapTiler</a> <a href="https://www.openstreetmap.org/copyright" target="_blank">&copy; OpenStreetMap contributors</a>`, true)
          viewer.creditDisplay.addStaticCredit(credit);
          viewer.camera.setView({
            destination: Cesium.Cartesian3.fromDegrees(8.67, 46.72, 4500),
            orientation: {
              pitch: Cesium.Math.toRadians(-20)
            }
          });
    </script>
</body>
</html>
```
