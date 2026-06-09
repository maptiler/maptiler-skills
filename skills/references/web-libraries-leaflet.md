# Source: https://docs.maptiler.com/leaflet/index/

# 

[Leaflet](https://www.leafletjs.com) is a lightweight open-source library for online maps. It works efficiently across all major desktop and mobile platforms and can be extended with lots of [plugins](#maptiler-leaflet-plugins).

You can use your MapTiler maps in Leaflet as vector tiles or the more traditional raster tiles. You can also add a geocoding control to your map with one line of code.

## Get started

This is the way to use your MapTiler maps in Leaflet JS. Simply use the code below the map.

<iframe style="height: 400px; width: 100%" src="?key="></iframe>



## Vector Tiles and Geocoding with MapTiler Leaflet plugins

Leaflet is meant to be as lightweight as possible and focuses on a core set of features. An easy way to extend its functionality is to use plugins.

* Check out the [**Use Leaflet JS with Vector Tiles**](/leaflet/examples/vector-tiles-in-leaflet-js/) example.
* Check out the [**Leaflet geocoding control how to search places**](/leaflet/examples/geocoding-control/) example.

###  Maptiler SDK layer (Vector Tiles layer)

{:#github-link}
{: width="24" height="24" data-aspect-ratio="1.00" }[Leaflet Vector Tiles basemap plugin](https://github.com/maptiler/leaflet-maptilersdk)

The [L.maptiler.maptilerLayer()](https://github.com/maptiler/leaflet-maptilersdk) plugin is how you display vector tiles in Leaflet JS.

Using the **L.maptiler.maptilerLayer** you have:

* All the power of [MapTiler SDK JS](/sdk-js/) to use vector tile layers (for data overlays) in your applications without any kind of limitation (show millions of geometries, choropleth maps, etc).
* Multi-lingual vector tiles basemaps for Leaflet using the MapTiler SDK.
* Use any of the many [professional looking basemaps](/sdk-js/api/map-styles/) created by MapTiler or use a map with your own custom basemap. 
* Easily change the language of your map without having to create a new basemap.
* Locate the user and center the map accordingly.

<pre><code class="language-js"><!--
const mtLayer = L.maptiler.maptilerLayer({ apiKey: `YOUR_MAPTILER_API_KEY_HERE` }).addTo(map);
--></code></pre>

### Geocoding control

{:#github-link}
[Leaflet geocoding control](https://github.com/maptiler/maptiler-geocoding-control#example-for-leaflet-using-module-bundler)

The [L.control.maptilerGeocoding()](https://github.com/maptiler/maptiler-geocoding-control#example-for-leaflet-using-module-bundler) plugin for Leaflet utilizes [MapTiler Geocoding API](https://www.maptiler.com/cloud/geocoding/). With this control, users of your application can find any place on Earth (States, Cities, Streets, ...) down to the address level, restrict the search area to a specific country, highlight search results on the map, autocomplete words while typing, and much more.

<pre><code class="language-js"><!--
L.control.maptilerGeocoding({ apiKey: `YOUR_MAPTILER_API_KEY_HERE` }).addTo(map);
--></code></pre>

## Learn more

If you want to learn how to initialize a map and load the style see the [Learn the basics - How to use Leaflet JS](./examples/how-to-use-leaflet/) tutorial.

Unlock your Leaflet mapping potential now! Look at the [Leaflet JS examples](/leaflet/examples/) we have prepared, from a quick start with Leaflet to advanced examples of how to load millions of points or use vector tiles with Leaflet JS.
