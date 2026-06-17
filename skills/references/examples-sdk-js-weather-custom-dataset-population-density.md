# Source: https://docs.maptiler.com/sdk-js/examples/weather-custom-dataset-population-density/

# Global Population Density From 2000 to 2020

In this tutorial, we will learn how to visualize and animate the evolution of the Global population density data with the MapTiler SDK Weather module.

Along with this tutorial, there is a news article about advanced data visualization and two more tutorials on preparing the data and processing it in MapTiler Engine:

1. [Visualizing population density on JavaScript Maps](https://www.maptiler.com/news/2024/08/visualizing-population-density-on-javascript-maps/)

2. [Preparing Gridded Data for visualization](/guides/map-design/preparing-gridded-raster-data-for-visualization)

3. [Global Population Density Data Processing](/guides/map-tiling-hosting/data-processing/global-population-density-data-processing-with-maptiler-engine)

At MapTiler, we have developed the [Weather library](/sdk-js/modules/weather/) and we provide data to create many different animated layer types (temperature, wind with particles, cloud coverage, etc.) in a super easy way. This library could also be used for non-weather raster data visualization, animated and interpolated over time. And this is exactly what we are going to do with the population density!

<div class="tab-content cdn-steps" markdown="1">

1. Since we are going to display the population data on a map, let's first create an instance of a map. Copy the following code, paste it into your favorite text editor, and save it as a `.html` file.

<pre class="line-numbers"><code class="language-html"><!--

<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Global Population Density From 2000 to 2020</title>

<script src="https://cdn.maptiler.com/maptiler-sdk-js//maptiler-sdk.umd.min.js"></script>

<link href="https://cdn.maptiler.com/maptiler-sdk-js//maptiler-sdk.css" rel="stylesheet" />

<script src="https://cdn.maptiler.com/maptiler-weather//maptiler-weather.umd.min.js"></script>

<style>

body { margin: 0; padding: 0; }

</style>

</head>

<body>

<div id="map"></div>

<script>

maptilersdk.config.apiKey = 'YOUR_MAPTILER_API_KEY_HERE';

const map = new maptilersdk.Map({

container: 'map', // container's id or the HTML element to render the map

style: maptilersdk.MapStyle.BACKDROP,

zoom: 9.71,

center: [85.4833, 27.6098],

hash: true,

});

</script>

</body>

</html>

--></code></pre>

</div>

<div class="tab-content bundler-steps" markdown="1">

1. Install the npm package.

<pre><code class="language-bash"><!--

npm install --save @maptiler/sdk @maptiler/weather

--></code></pre>

1. Include the CSS file.

If you have a bundler that can handle CSS, you can <a href="#" id="import-css-link"><code>import</code></a> the CSS or include it with a <a href="#"  id="cdn-css-link"><code>&lt;link&gt;</code></a> in the head of the document via the CDN

<pre id="import-css-code"><code class="language-js"><!--

import "@maptiler/sdk/dist/maptiler-sdk.css";

--></code></pre>

<pre id="cdn-css-code" class="hidden"><code class="language-html"><!--

<link href='https://cdn.maptiler.com/maptiler-sdk-js//maptiler-sdk.css' rel='stylesheet' />

--></code></pre>

1. Since we are going to display the population data on a map, let's first create an instance of a map. Include the following code in your JavaScript file (Example: app.js).

<pre class="line-numbers"><code class="language-js"><!--

import { Map, MapStyle, config } from '@maptiler/sdk';

import '@maptiler/sdk/dist/maptiler-sdk.css';

import { ColorRamp, TileLayer, GradientColoringFragment } from '@maptiler/weather';

config.apiKey = 'YOUR_MAPTILER_API_KEY_HERE';

const map = Map({

container: 'map', // container's id or the HTML element to render the map

style: ,

center: [, ], // starting position [lng, lat]

zoom: , // starting zoom

hash: true,

});

--></code></pre>

</div>

<div class="tab-common-content" markdown="1">

1.

</div>

<div class="tab-content cdn-steps" markdown="1">

1. Create a custom layer using the MapTiler Weather `Tilelayer`. The [TileLayer](/sdk-js/modules/weather/api/intensity/) consists of multiple timeframes, every frame is a tile pyramid at a different moment in time. The individual frames are smoothly animated.

<pre class="line-numbers" data-start="27" data-line-offset="26" data-line="27-46"><code class="language-js"><!--

const customLayer = new maptilerweather.TileLayer('population', {minZoom: 0, maxZoom: 7},

[

new maptilerweather.GradientColoringFragment({

decode: {

// We use the red (`r`) channel but in this case, the same value is repeated on green and blue

// so it does not really matter which channel we chose.

channel: 'r',

// Since we have encoded the square root of the density, the min and max are [0, 255]

// which in terms of density means from 0 to 255*255 (65025)

min: 0,

max: 255,

},

// We scale the TURBO color ramp to go from `0` to `sqrt(45000)`

// so that the max color of the color ramp represents a density of 45k people per sqkm

stops: maptilerweather.ColorRamp.builtin.TURBO.scale(0, Math.sqrt(45000)),

smooth: true,

opacity: 1

}),

]

);

--></code></pre>

</div>

<div class="tab-content bundler-steps" markdown="1">

1. Create a custom layer using the MapTiler Weather `Tilelayer`. The [TileLayer](/sdk-js/modules/weather/api/intensity/) consists of multiple timeframes, every frame is a tile pyramid at a different moment in time. The individual frames are smoothly animated.

<pre class="line-numbers" data-start="13" data-line-offset="12" data-line="13-32"><code class="language-js"><!--

const customLayer = new TileLayer('population', {minZoom: 0, maxZoom: 7},

[

new GradientColoringFragment({

decode: {

// We use the red (`r`) channel but in this case, the same value is repeated on green and blue

// so it does not really matter which channel we chose.

channel: 'r',

// Since we have encoded the square root of the density, the min and max are [0, 255]

// which in terms of density means from 0 to 255*255 (65025)

min: 0,

max: 255,

},

// We scale the TURBO color ramp to go from `0` to `sqrt(45000)`

// so that the max color of the color ramp represents a density of 45k people per sqkm

stops: ColorRamp.builtin.TURBO.scale(0, Math.sqrt(45000)),

smooth: true,

opacity: 1

}),

]

);

--></code></pre>

</div>

<div class="tab-common-content" markdown="1">

We use the `TURBO` color ramp because it has a linear luminance, but there are more colorblind-friendly alternatives if your application requires it (for example, `CIVIDIS`).

Here is what the `TURBO` color ramp looks like:

<script src="https://cdn.maptiler.com/maptiler-weather//maptiler-weather.umd.min.js"></script>

<div id="colorramp-contain"></div>

<script>

const colorrampContainer = document.getElementById("colorramp-contain");

const colorramp = maptilerweather.ColorRamp.builtin.TURBO;

const canvas = colorramp.getCanvasStrip();

canvas.style.height = "30px";

canvas.style.width = "100%";

canvas.style.border = "1px dashed #00000059";

colorrampContainer.appendChild( canvas );

</script>

</div>

<div class="tab-common-content" markdown="1">

1. Adding the tilesets from MapTiler as sources. In this example, we will use the population density tilesets generated in the [Global Population Density Data Processing](/guides/map-tiling-hosting/data-processing/global-population-density-data-processing-with-maptiler-engine) tutorial.

<pre class="line-numbers" data-start="48" data-line-offset="47" data-line="48-79"><code class="language-js"><!--

// Description of the tileset per year

const sources = [

{

year: 2000,

tilesetID: "YOUR_MAPTILER_YEAR_2000_DATASET_ID_HERE"

},

{

year: 2005,

tilesetID: "YOUR_MAPTILER_YEAR_2005_DATASET_ID_HERE"

},

{

year: 2010,

tilesetID: "YOUR_MAPTILER_YEAR_2010_DATASET_ID_HERE"

},

{

year: 2015,

tilesetID: "YOUR_MAPTILER_YEAR_2015_DATASET_ID_HERE"

},

{

year: 2020,

tilesetID: "YOUR_MAPTILER_YEAR_2020_DATASET_ID_HERE"

},

];

sources.forEach((src) => {

customLayer.addSource(

// We use the first of January for each year

Date.parse(`${src.year}-01-01T00:00:00.000Z`),

// Note the usage of the {zxy} pattern

`https://api.maptiler.com/tiles/${src.tilesetID}/{zxy}.png`

);

});

--></code></pre>

1. Add the custom layer to the map

<pre class="line-numbers" data-start="81" data-line-offset="80" data-line="81-84"><code class="language-js"><!--

map.on('load', function () {

map.setPaintProperty("Water", 'fill-color', "rgba(0, 0, 0, 0.4)");

map.addLayer(customLayer, 'Water');

});

--></code></pre>

1. If we reload the map, we can see the population layer corresponding to the first dataset (year 2000). Next, we are going to add a time bar to our application so we can animate the population layer.

</div>

<div class="tab-content cdn-steps" markdown="1">

1. Create a slider bar to animate the population layer by years.

<pre class="line-numbers" data-start="16" data-line-offset="15" data-line="16-19"><code class="language-html"><!--

<div id="time-info">

<span id="time-text"></span>

<input type="range" id="time-slider" min="0" max="0" step="1">

</div>

--></code></pre>

1. Add the functionality to the slide bar to select dates between the years 2000 and 2020.

<pre class="line-numbers" data-start="31" data-line-offset="30" data-line="31-43"><code class="language-html"><!--

const timeInfoContainer = document.getElementById("time-info");

const timeTextDiv = document.getElementById("time-text");

const timeSlider = document.getElementById("time-slider");

timeSlider.min = Date.parse("2000-01-01T00:00:00.000Z");

timeSlider.max = Date.parse("2020-01-01T00:00:00.000Z");

timeSlider.addEventListener("input", etv => {

customLayer.setAnimationTime(parseInt(timeSlider.value));

timeTextDiv.innerText = (new Date(parseInt(timeSlider.value)).toLocaleDateString("en", {year: "numeric"}));

})

timeTextDiv.innerText = (new Date("2000-01-01T00:00:00.000Z").toLocaleDateString("en", {year: "numeric"}));

--></code></pre>

1. Style the slide bar.

<pre class="line-numbers" data-start="14" data-line-offset="13" data-line="14-44"><code class="language-css"><!--

position: fixed;

width: 60vw;

bottom: 0;

z-index: 1;

margin: 10px;

text-shadow: 0px 0px 5px black;

color: white;

font-size: 18px;

font-weight: 500;

text-align: center;

left: 0;

right: 0;

margin: auto;

padding: 20px;

}

font-size: 22px;

font-weight: 600;

}

width: 100%;

height: fit-content;

left: 0;

right: 0;

z-index: 1;

filter: drop-shadow(0 0 7px #000a);

margin-top: 10px;

}

--></code></pre>

1. Finally, we will add the functionality of showing the population density corresponding to the cursor position.

1. Create the `HTML` elements to display the population density values.

<pre class="line-numbers" data-start="52" data-line-offset="51" data-line="52-53"><code class="language-html"><!--

<div id="variable-name">Population</div>

<div id="pointer-data"></div>

--></code></pre>

1. Style the text that displays population density values.

<pre class="line-numbers" data-start="14" data-line-offset="13" data-line="14-32"><code class="language-css"><!--

z-index: 1;

position: fixed;

font-size: 20px;

font-weight: 900;

margin: 27px 0px 0px 10px;

color: #fff;

text-shadow: 0px 0px 10px #0007;

}

z-index: 1;

position: fixed;

font-size: 20px;

font-weight: 500;

margin: 5px 0px 0px 10px;

color: #fff;

text-shadow: 0px 0px 10px #0007;

}

--></code></pre>

1. Select the HTML element where to display the information related to the population density and create the variable where to save the cursor position.

<pre class="line-numbers" data-start="88" data-line-offset="87" data-line="88-89"><code class="language-js"><!--

const pointerDataDiv = document.getElementById("pointer-data");

let pointerLngLat = null;

--></code></pre>

1. Capture the `mousemove` event to display the population density values ​​corresponding to the cursor position.

<pre class="line-numbers" data-start="160" data-line-offset="159" data-line="160-180"><code class="language-js"><!--

map.on('mouseout', function(evt) {

if (!evt.originalEvent.relatedTarget) {

pointerDataDiv.innerText = "";

pointerLngLat = null;

}

});

function updatePointerValue(lngLat) {

if (!lngLat) return;

pointerLngLat = lngLat;

const value = customLayer.pick(lngLat.lng, lngLat.lat);

if (!value) {

pointerDataDiv.innerText = "";

return;

}

pointerDataDiv.innerText = `${value[0].toFixed(1)} people/km²`

}

map.on('mousemove', (e) => {

updatePointerValue(e.lngLat);

});

--></code></pre>

1. We already have our map working, now we are going to add a button to play/pause the map animation.

<pre class="line-numbers" data-start="69" data-line-offset="68" data-line="69-72,74"><code class="language-html"><!--

<div class="slider-container">

<button id="play-pause-bt" class="button"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-play-fill" viewBox="0 0 16 16">

<path d="m11.596 8.697-6.363 3.692c-.54.313-1.233-.066-1.233-.697V4.308c0-.63.692-1.01 1.233-.696l6.363 3.692a.802.802 0 0 1 0 1.393"/>

</svg></button>

<input type="range" id="time-slider" min="0" max="0" step="1">

</div>

--></code></pre>

1. Style the button and position it next to the time slider

<pre class="line-numbers" data-start="65" data-line-offset="64" data-line="65-80"><code class="language-css"><!--

.slider-container {

display: flex;

}

.button {

cursor: pointer;

width: auto;

padding: 8px;

border-radius: 25px;

font-size: 10px;

text-align: center;

font-family: sans-serif;

font-weight: bold;

margin-right: 8px;

border-width: 0;

}

--></code></pre>

1. Get the button to add some events so you can animate the map.

<pre class="line-numbers" data-start="109" data-line-offset="108" data-line="110"><code class="language-js"><!--

const pointerDataDiv = document.getElementById("pointer-data");

const playPauseButton = document.getElementById("play-pause-bt");

let pointerLngLat = null;

--></code></pre>

1. Play/pause the animation when the button is clicked.

<pre class="line-numbers" data-start="204" data-line-offset="203" data-line="204-220"><code class="language-js"><!--

// When clicking on the play/pause

let isPlaying = false;

playPauseButton.addEventListener("click", () => {

if (isPlaying) {

customLayer.animateByFactor(0);

playPauseButton.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-play-fill" viewBox="0 0 16 16">

<path d="m11.596 8.697-6.363 3.692c-.54.313-1.233-.066-1.233-.697V4.308c0-.63.692-1.01 1.233-.696l6.363 3.692a.802.802 0 0 1 0 1.393"/>

</svg>`;

} else {

customLayer.animateByFactor((3.154e+10)*2); //aprox millisecond in a year

playPauseButton.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pause-fill" viewBox="0 0 16 16">

<path d="M5.5 3.5A1.5 1.5 0 0 1 7 5v6a1.5 1.5 0 0 1-3 0V5a1.5 1.5 0 0 1 1.5-1.5m5 0A1.5 1.5 0 0 1 12 5v6a1.5 1.5 0 0 1-3 0V5a1.5 1.5 0 0 1 1.5-1.5"/>

</svg>`;

}

isPlaying = !isPlaying;

});

--></code></pre>

1. Update the time slider and date based on the animation time.

<pre class="line-numbers" data-start="189" data-line-offset="188" data-line="189-200"><code class="language-js"><!--

// Called when the animation is progressing

customLayer.on("tick", () => {

refreshTime();

updatePointerValue(pointerLngLat);

});

// Update the date time display

function refreshTime() {

const d = Number.parseInt(customLayer.getAnimationTime().toFixed(0));

timeTextDiv.innerText = (new Date(d).toLocaleDateString("en", {year: "numeric"}));

timeSlider.value = d.toString();

}

--></code></pre>

1. Congratulations, you have created an animated map that shows global population density between the years 2000 and 2020.

</div>

<div class="tab-content bundler-steps" markdown="1">

1. Create a slider bar to animate the population layer by years. Add this to your `html` file.

<pre><code class="language-html"><!--

<div id="time-info">

<span id="time-text"></span>

<input type="range" id="time-slider" min="0" max="0" step="1">

</div>

--></code></pre>

1. Add the functionality to the slide bar to select dates between the years 2000 and 2020.

<pre class="line-numbers" data-start="13" data-line-offset="12" data-line="13-25"><code class="language-html"><!--

const timeInfoContainer = document.getElementById("time-info");

const timeTextDiv = document.getElementById("time-text");

const timeSlider = document.getElementById("time-slider");

timeSlider.min = Date.parse("2000-01-01T00:00:00.000Z");

timeSlider.max = Date.parse("2020-01-01T00:00:00.000Z");

timeSlider.addEventListener("input", etv => {

customLayer.setAnimationTime(parseInt(timeSlider.value));

timeTextDiv.innerText = (new Date(parseInt(timeSlider.value)).toLocaleDateString("en", {year: "numeric"}));

})

timeTextDiv.innerText = (new Date("2000-01-01T00:00:00.000Z").toLocaleDateString("en", {year: "numeric"}));

--></code></pre>

1. Style the slide bar. Add this lines to your `css` file

<pre><code class="language-css"><!--

position: fixed;

width: 60vw;

bottom: 0;

z-index: 1;

margin: 10px;

text-shadow: 0px 0px 5px black;

color: white;

font-size: 18px;

font-weight: 500;

text-align: center;

left: 0;

right: 0;

margin: auto;

padding: 20px;

}

font-size: 22px;

font-weight: 600;

}

width: 100%;

height: fit-content;

left: 0;

right: 0;

z-index: 1;

filter: drop-shadow(0 0 7px #000a);

margin-top: 10px;

}

--></code></pre>

1. Finally, we will add the functionality of showing the population density corresponding to the cursor position.

1. Create the `HTML` elements to display the population density values. Add this lines in the `html` file

<pre><code class="language-html"><!--

<div id="variable-name">Population</div>

<div id="pointer-data"></div>

--></code></pre>

1. Style the text that displays population density values. Add into the `css` file

<pre><code class="language-css"><!--

z-index: 1;

position: fixed;

font-size: 20px;

font-weight: 900;

margin: 27px 0px 0px 10px;

color: #fff;

text-shadow: 0px 0px 10px #0007;

}

z-index: 1;

position: fixed;

font-size: 20px;

font-weight: 500;

margin: 5px 0px 0px 10px;

color: #fff;

text-shadow: 0px 0px 10px #0007;

}

--></code></pre>

1. Select the HTML element where to display the information related to the population density and create the variable where to save the cursor position.

<pre class="line-numbers" data-start="16" data-line-offset="15" data-line="16-17"><code class="language-js"><!--

const pointerDataDiv = document.getElementById("pointer-data");

let pointerLngLat = null;

--></code></pre>

1. Capture the `mousemove` event to display the population density values ​​corresponding to the cursor position.

<pre class="line-numbers" data-start="76" data-line-offset="75" data-line="76-96"><code class="language-js"><!--

map.on('mouseout', function(evt) {

if (!evt.originalEvent.relatedTarget) {

pointerDataDiv.innerText = "";

pointerLngLat = null;

}

});

function updatePointerValue(lngLat) {

if (!lngLat) return;

pointerLngLat = lngLat;

const value = customLayer.pick(lngLat.lng, lngLat.lat);

if (!value) {

pointerDataDiv.innerText = "";

return;

}

pointerDataDiv.innerText = `${value[0].toFixed(1)} people/km²`

}

map.on('mousemove', (e) => {

updatePointerValue(e.lngLat);

});

--></code></pre>

1. We already have our map working, now we are going to add a button into the `html` to play/pause the map animation.

<pre class="line-numbers"><code class="language-html"><!--

<div class="slider-container">

<button id="play-pause-bt" class="button"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-play-fill" viewBox="0 0 16 16">

<path d="m11.596 8.697-6.363 3.692c-.54.313-1.233-.066-1.233-.697V4.308c0-.63.692-1.01 1.233-.696l6.363 3.692a.802.802 0 0 1 0 1.393"/>

</svg></button>

<input type="range" id="time-slider" min="0" max="0" step="1">

</div>

--></code></pre>

1. Style the button and position it next to the time slider. Add this lines to your `css` file.

<pre><code class="language-css"><!--

.slider-container {

display: flex;

}

.button {

cursor: pointer;

width: auto;

padding: 8px;

border-radius: 25px;

font-size: 10px;

text-align: center;

font-family: sans-serif;

font-weight: bold;

margin-right: 8px;

border-width: 0;

}

--></code></pre>

1. Get the button to add some events so you can animate the map.

<pre class="line-numbers" data-start="17" data-line-offset="16" data-line="18"><code class="language-js"><!--

const pointerDataDiv = document.getElementById("pointer-data");

const playPauseButton = document.getElementById("play-pause-bt");

let pointerLngLat = null;

--></code></pre>

1. Play/pause the animation when the button is clicked.

<pre class="line-numbers" data-start="97" data-line-offset="96" data-line="97-113"><code class="language-js"><!--

// When clicking on the play/pause

let isPlaying = false;

playPauseButton.addEventListener("click", () => {

if (isPlaying) {

customLayer.animateByFactor(0);

playPauseButton.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-play-fill" viewBox="0 0 16 16">

<path d="m11.596 8.697-6.363 3.692c-.54.313-1.233-.066-1.233-.697V4.308c0-.63.692-1.01 1.233-.696l6.363 3.692a.802.802 0 0 1 0 1.393"/>

</svg>`;

} else {

customLayer.animateByFactor((3.154e+10)*2); //aprox millisecond in a year

playPauseButton.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pause-fill" viewBox="0 0 16 16">

<path d="M5.5 3.5A1.5 1.5 0 0 1 7 5v6a1.5 1.5 0 0 1-3 0V5a1.5 1.5 0 0 1 1.5-1.5m5 0A1.5 1.5 0 0 1 12 5v6a1.5 1.5 0 0 1-3 0V5a1.5 1.5 0 0 1 1.5-1.5"/>

</svg>`;

}

isPlaying = !isPlaying;

});

--></code></pre>

1. Update the time slider and date based on the animation time.

<pre class="line-numbers" data-start="97" data-line-offset="96" data-line="97-108"><code class="language-js"><!--

// Called when the animation is progressing

customLayer.on("tick", () => {

refreshTime();

updatePointerValue(pointerLngLat);

});

// Update the date time display

function refreshTime() {

const d = Number.parseInt(customLayer.getAnimationTime().toFixed(0));

timeTextDiv.innerText = (new Date(d).toLocaleDateString("en", {year: "numeric"}));

timeSlider.value = d.toString();

}

--></code></pre>

1. Congratulations, you have created an animated map that shows global population density between the years 2000 and 2020.

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element to render the map
        style: maptilersdk.MapStyle.BACKDROP,  // stylesheet location
        zoom: 9.71,
        center: [85.4833, 27.6098],
        hash: true,
      }));

      const timeInfoContainer = document.getElementById("time-info");
      const timeTextDiv = document.getElementById("time-text");
      const timeSlider = document.getElementById("time-slider");
      const pointerDataDiv = document.getElementById("pointer-data");
      const playPauseButton = document.getElementById("play-pause-bt");
      let pointerLngLat = null;

      timeSlider.min = Date.parse("2000-01-01T00:00:00.000Z");
      timeSlider.max = Date.parse("2020-01-01T00:00:00.000Z");

      timeSlider.addEventListener("input", etv => {
        customLayer.setAnimationTime(parseInt(timeSlider.value));
        timeTextDiv.innerText = (new Date(parseInt(timeSlider.value)).toLocaleDateString("en", {year: "numeric"}));
      })

      timeTextDiv.innerText = (new Date("2000-01-01T00:00:00.000Z").toLocaleDateString("en", {year: "numeric"}));

      const customLayer = new maptilerweather.TileLayer('population', {minZoom: 0, maxZoom: 7},
        [
          new maptilerweather.GradientColoringFragment({
            decode: {
              // We use the red (`r`) channel but in this case, the same value is repeated on green and blue
              // so it does not really matter which channel we chose.
              channel: 'r',
              // Since we have encoded the square root of the density, the min and max are [0, 255]
              // which in terms of density means from 0 to 255*255 (65025)
              min: 0,
              max: 255,
            },
            // We scale the TURBO color ramp to go from `0` to `sqrt(45000)`
            // so that the max color of the color ramp represents a density of 45k people per sqkm
            stops: maptilerweather.ColorRamp.builtin.TURBO.scale(0, Math.sqrt(45000)),
            smooth: true,
            opacity: 1
          }),
        ]
      );

      // Description of the tileset per year
      const sources = [
        {
          year: 2000,
          tilesetID: "YOUR_MAPTILER_YEAR_2000_DATASET_ID_HERE"
        },
        {
          year: 2005,
          tilesetID: "YOUR_MAPTILER_YEAR_2005_DATASET_ID_HERE"
        },
        {
          year: 2010,
          tilesetID: "YOUR_MAPTILER_YEAR_2010_DATASET_ID_HERE"
        },
        {
          year: 2015,
          tilesetID: "YOUR_MAPTILER_YEAR_2015_DATASET_ID_HERE"
        },
        {
          year: 2020,
          tilesetID: "YOUR_MAPTILER_YEAR_2020_DATASET_ID_HERE"
        },
      ];

      sources.forEach((src) => {
        customLayer.addSource(
          // We use the first of January for each year
          Date.parse(`${src.year}-01-01T00:00:00.000Z`), 
          // Note the usage of the {zxy} pattern
          `https://api.maptiler.com/tiles/${src.tilesetID}/{zxy}.png`
        ); 
      });

      map.on('load', function () {
        map.setPaintProperty("Water", 'fill-color', "rgba(0, 0, 0, 0.4)");
        map.addLayer(customLayer, 'Water');
      });

      map.on('mouseout', function(evt) {
        if (!evt.originalEvent.relatedTarget) {
          pointerDataDiv.innerText = "";
          pointerLngLat = null;
        }
      });

      // Called when the animation is progressing
      customLayer.on("tick", () => {
        refreshTime();
        updatePointerValue(pointerLngLat);
      });

      // Update the date time display
      function refreshTime() {
        const d = Number.parseInt(customLayer.getAnimationTime().toFixed(0));
        timeTextDiv.innerText = (new Date(d).toLocaleDateString("en", {year: "numeric"}));
        timeSlider.value = d.toString();
      }

      function updatePointerValue(lngLat) {
        if (!lngLat) return;
        pointerLngLat = lngLat;
        const value = customLayer.pick(lngLat.lng, lngLat.lat);
        if (!value) {
          pointerDataDiv.innerText = "";
          return;
        }
        pointerDataDiv.innerText = `${value[0].toFixed(1)} people/km²`
      }

      map.on('mousemove', (e) => {
        updatePointerValue(e.lngLat);
      });

      // When clicking on the play/pause
      let isPlaying = false;
      playPauseButton.addEventListener("click", () => {
        if (isPlaying) {
          customLayer.animateByFactor(0);
          playPauseButton.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-play-fill" viewBox="0 0 16 16">
            <path d="m11.596 8.697-6.363 3.692c-.54.313-1.233-.066-1.233-.697V4.308c0-.63.692-1.01 1.233-.696l6.363 3.692a.802.802 0 0 1 0 1.393"/>
          </svg>`;
        } else {
          customLayer.animateByFactor((3.154e+10)*2); //aprox millisecond in a year
          playPauseButton.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pause-fill" viewBox="0 0 16 16">
            <path d="M5.5 3.5A1.5 1.5 0 0 1 7 5v6a1.5 1.5 0 0 1-3 0V5a1.5 1.5 0 0 1 1.5-1.5m5 0A1.5 1.5 0 0 1 12 5v6a1.5 1.5 0 0 1-3 0V5a1.5 1.5 0 0 1 1.5-1.5"/>
          </svg>`;
        }

        isPlaying = !isPlaying;
      });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Global Population Density From 2000 to 2020</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <script src="https://cdn.maptiler.com/maptiler-weather/3.1.1/maptiler-weather.umd.min.js"></script>
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
            style: maptilersdk.MapStyle.BACKDROP,
            center: [85.4833, 27.6098],
            zoom: 9.71
        });

        container: 'map', // container's id or the HTML element to render the map
                style: maptilersdk.MapStyle.BACKDROP,  // stylesheet location
                zoom: 9.71,
                center: [85.4833, 27.6098],
                hash: true,
              }));

              const timeInfoContainer = document.getElementById("time-info");
              const timeTextDiv = document.getElementById("time-text");
              const timeSlider = document.getElementById("time-slider");
              const pointerDataDiv = document.getElementById("pointer-data");
              const playPauseButton = document.getElementById("play-pause-bt");
              let pointerLngLat = null;

              timeSlider.min = Date.parse("2000-01-01T00:00:00.000Z");
              timeSlider.max = Date.parse("2020-01-01T00:00:00.000Z");

              timeSlider.addEventListener("input", etv => {
                customLayer.setAnimationTime(parseInt(timeSlider.value));
                timeTextDiv.innerText = (new Date(parseInt(timeSlider.value)).toLocaleDateString("en", {year: "numeric"}));
              })

              timeTextDiv.innerText = (new Date("2000-01-01T00:00:00.000Z").toLocaleDateString("en", {year: "numeric"}));

              const customLayer = new maptilerweather.TileLayer('population', {minZoom: 0, maxZoom: 7},
                [
                  new maptilerweather.GradientColoringFragment({
                    decode: {
                      // We use the red (`r`) channel but in this case, the same value is repeated on green and blue
                      // so it does not really matter which channel we chose.
                      channel: 'r',
                      // Since we have encoded the square root of the density, the min and max are [0, 255]
                      // which in terms of density means from 0 to 255*255 (65025)
                      min: 0,
                      max: 255,
                    },
                    // We scale the TURBO color ramp to go from `0` to `sqrt(45000)`
                    // so that the max color of the color ramp represents a density of 45k people per sqkm
                    stops: maptilerweather.ColorRamp.builtin.TURBO.scale(0, Math.sqrt(45000)),
                    smooth: true,
                    opacity: 1
                  }),
                ]
              );

              // Description of the tileset per year
              const sources = [
                {
                  year: 2000,
                  tilesetID: "YOUR_MAPTILER_YEAR_2000_DATASET_ID_HERE"
                },
                {
                  year: 2005,
                  tilesetID: "YOUR_MAPTILER_YEAR_2005_DATASET_ID_HERE"
                },
                {
                  year: 2010,
                  tilesetID: "YOUR_MAPTILER_YEAR_2010_DATASET_ID_HERE"
                },
                {
                  year: 2015,
                  tilesetID: "YOUR_MAPTILER_YEAR_2015_DATASET_ID_HERE"
                },
                {
                  year: 2020,
                  tilesetID: "YOUR_MAPTILER_YEAR_2020_DATASET_ID_HERE"
                },
              ];

              sources.forEach((src) => {
                customLayer.addSource(
                  // We use the first of January for each year
                  Date.parse(`${src.year}-01-01T00:00:00.000Z`), 
                  // Note the usage of the {zxy} pattern
                  `https://api.maptiler.com/tiles/${src.tilesetID}/{zxy}.png`
                ); 
              });

              map.on('load', function () {
                map.setPaintProperty("Water", 'fill-color', "rgba(0, 0, 0, 0.4)");
                map.addLayer(customLayer, 'Water');
              });

              map.on('mouseout', function(evt) {
                if (!evt.originalEvent.relatedTarget) {
                  pointerDataDiv.innerText = "";
                  pointerLngLat = null;
                }
              });

              // Called when the animation is progressing
              customLayer.on("tick", () => {
                refreshTime();
                updatePointerValue(pointerLngLat);
              });

              // Update the date time display
              function refreshTime() {
                const d = Number.parseInt(customLayer.getAnimationTime().toFixed(0));
                timeTextDiv.innerText = (new Date(d).toLocaleDateString("en", {year: "numeric"}));
                timeSlider.value = d.toString();
              }

              function updatePointerValue(lngLat) {
                if (!lngLat) return;
                pointerLngLat = lngLat;
                const value = customLayer.pick(lngLat.lng, lngLat.lat);
                if (!value) {
                  pointerDataDiv.innerText = "";
                  return;
                }
                pointerDataDiv.innerText = `${value[0].toFixed(1)} people/km²`
              }

              map.on('mousemove', (e) => {
                updatePointerValue(e.lngLat);
              });

              // When clicking on the play/pause
              let isPlaying = false;
              playPauseButton.addEventListener("click", () => {
                if (isPlaying) {
                  customLayer.animateByFactor(0);
                  playPauseButton.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-play-fill" viewBox="0 0 16 16">
                    <path d="m11.596 8.697-6.363 3.692c-.54.313-1.233-.066-1.233-.697V4.308c0-.63.692-1.01 1.233-.696l6.363 3.692a.802.802 0 0 1 0 1.393"/>
                  </svg>`;
                } else {
                  customLayer.animateByFactor((3.154e+10)*2); //aprox millisecond in a year
                  playPauseButton.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pause-fill" viewBox="0 0 16 16">
                    <path d="M5.5 3.5A1.5 1.5 0 0 1 7 5v6a1.5 1.5 0 0 1-3 0V5a1.5 1.5 0 0 1 1.5-1.5m5 0A1.5 1.5 0 0 1 12 5v6a1.5 1.5 0 0 1-3 0V5a1.5 1.5 0 0 1 1.5-1.5"/>
                  </svg>`;
                }

                isPlaying = !isPlaying;
              });
    </script>
</body>
</html>
```
