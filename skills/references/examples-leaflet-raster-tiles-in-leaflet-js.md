# Source: https://docs.maptiler.com/leaflet/examples/raster-tiles-in-leaflet-js/

# Raster tiles in Leaflet JS

Raster map tiles are actually nothing else than raster images. Zoomable raster maps consist of many raster map tiles (in the .png or .jpg format) placed next to each other, ordered in a pyramid scheme. This clever trick allows you to browse just a small part of the map without loading it whole while maintaining a feeling of exploring a single large document. Read more about zoomable maps and the pyramid scheme in [this article](https://www.maptiler.com/google-maps-coordinates-tile-bounds-projection/).

For basemaps, it is recommended to use it with traditional raster tiles (Mercator XYZ). Use **recommended 512x512** raster tiles.

Next we will explain two ways how to create a map in Leaflet using your MapTiler maps.

The first way is to use the native L.tileLayer function; this is the most used way for basemaps and it doesn't need any plugin, but we have to configure the map options (initial view, zomm levels, etc.). In a second way we have to use the TileJSON plugin, which is in charge of interpreting the TileJson file and creating the map with all the options.

<iframe style="height: 400px; width: 100%" src="?key="></iframe>

## Raster tiles XYZ (Mercator XYZ)

Raster tiles (Mercator XYZ) are loaded with [L.tileLayer](https://leafletjs.com/reference.html#tilelayer) function. Start your code with following starter:



Use **256x256** raster tiles for compatibility with certain libraries. To use the 256px tiles you must use this URL in your layer

<pre><code class="language-http">
  `https://api.maptiler.com/maps/streets-v4/256/{z}/{x}/{y}.png?key=${key}`
</code></pre>

Example of 256x256 raster tiles

<pre><code class="language-js">
  L.tileLayer(`https://api.maptiler.com/maps/streets-v4/256/{z}/{x}/{y}.png?key=${key}`,{
    minZoom: 1,
    attribution: "\u003ca href=\"https://www.maptiler.com/copyright/\" target=\"_blank\"\u003e\u0026copy; MapTiler\u003c/a\u003e \u003ca href=\"https://www.openstreetmap.org/copyright\" target=\"_blank\"\u003e\u0026copy; OpenStreetMap contributors\u003c/a\u003e",
    crossOrigin: true
  }).addTo(map);
</code></pre>

## Raster tiles TileJSON (plugin)

It's possible to use directly TileJSON with [leaflet-tilejson plugin](https://github.com/kartena/leaflet-tilejson).

<pre><code class="language-js">
fetch(`https://api.maptiler.com/maps/streets-v4/256/tiles.json?key=${key}`)
  .then(response => response.json())
  .then(data => {
    const map = L.TileJSON.createMap('map', data);
  });
</code></pre>

### Summary

If we do not want to add an extra plugin to our application and we want to define the map options we must use the Raster tiles XYZ (**recommended option**). On the contrary we want to make a map without worrying about defining the map options we can use the TileJSON (plugin).

