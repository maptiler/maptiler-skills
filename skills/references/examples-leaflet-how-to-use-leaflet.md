# Source: https://docs.maptiler.com/leaflet/examples/how-to-use-leaflet/

# Display a map

This tutorial shows how to create a Leaflet map and display it on a web page using MapTiler. This tutorial explains how to use Leaflet with basic JavaScript from a **CDN**. To use Leaflet from **NPM**, see the step-by-step tutorial [How to use Leaflet with **NPM**](/leaflet/examples/npm-get-started/).

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

1. Include the Leaflet JavaScript and CSS files in the `<head>` of your HTML file.

<pre class="line-numbers" data-start="6" data-line-offset="5" data-line="7,8"><code class="language-html"><!--

<title></title>

<link rel="stylesheet" href="https://unpkg.com/leaflet@/dist/leaflet.css" />

<script src="https://unpkg.com/leaflet@/dist/leaflet.js"></script>

<style>

--></code></pre>

1. Create a `<div>` element with a certain id where you want your map to be.

Add `<div>` tag into your page. This div will be the container where the map will be loaded.

<pre class="line-numbers" data-start="16" data-line-offset="15" data-line="17"><code class="language-html"><!--

<body>

<div id="map"></div>

</body>

--></code></pre>

1. The div must have non-zero height.

<pre class="line-numbers" data-start="10" data-line-offset="9" data-line="14-20"><code class="language-css">

body {

margin: 0;

padding: 0;

}

position: absolute;

top: 0;

bottom: 0;

width: 100%;

}

</code></pre>

1. Finally, load the map with the style

<pre class="line-numbers" data-start="27" data-line-offset="26" data-line="27-37"><code class="language-js">

const key = 'YOUR_MAPTILER_API_KEY_HERE';

const map = L.map('map').setView([, ], );

L.tileLayer(`https://api.maptiler.com/maps/streets-v4/{z}/{x}/{y}.png?key=${key}`,{

tileSize: 512,

zoomOffset: -1,

minZoom: 1,

attribution: "\u003ca href=\"https://www.maptiler.com/copyright/\" target=\"_blank\"\u003e\u0026copy; MapTiler\u003c/a\u003e \u003ca href=\"https://www.openstreetmap.org/copyright\" target=\"_blank\"\u003e\u0026copy; OpenStreetMap contributors\u003c/a\u003e",

crossOrigin: true

}).addTo(map);

</code></pre>

1.

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
    <title>Display a map</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <script src="https://cdn.maptiler.com/leaflet-maptilersdk/v4.1.0/leaflet-maptilersdk.umd.min.js"></script>
    <style>
        body { margin: 0; padding: 0; }
        #map { position: absolute; top: 0; bottom: 0; width: 100%; }
    </style>
</head>
<body>
    <div id="map"></div>
    <script>
        const key = 'YOUR_MAPTILER_API_KEY';

          const map = L.map('map').setView([0, 0], 2);
          const layer = L.tileLayer(`https://api.maptiler.com/maps/streets-v4/{z}/{x}/{y}.png?key=${key}`, {
            tileSize: 512,
            zoomOffset: -1,
            minZoom: 1,
            attribution: "\u003ca href=\"https://www.maptiler.com/copyright/\" target=\"_blank\"\u003e\u0026copy; MapTiler\u003c/a\u003e \u003ca href=\"https://www.openstreetmap.org/copyright\" target=\"_blank\"\u003e\u0026copy; OpenStreetMap contributors\u003c/a\u003e",
            crossOrigin: true
          }).addTo(map);
    </script>
</body>
</html>
```
