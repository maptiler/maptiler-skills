# Source: https://docs.maptiler.com/openlayers/index/

# 

[OpenLayers](https://openlayers.org) is a high-performance, full-featured web mapping library that displays maps from various sources and formats. If you need to develop a web application that interacts with most OGC standards, this is your tool, whether connecting to a WFS or reprojecting a raster.

You can use your MapTiler maps in OpenLayers as vector tiles or the more traditional raster tiles. You can also add a geocoding control to your map with one line of code.

## Get started

This is the easiest and fastest way to use your MapTiler maps in OpenLayers. Simply use the code below the map.

<iframe style="height: 400px; width: 100%" src="?key="></iframe>



## Geocoding with MapTiler OpenLayers plugins
### Geocoding control

{:#github-link}
[OpenLayers geocoding control](https://github.com/maptiler/maptiler-geocoding-control#example-for-openlayers-using-module-bundler)

The [GeocodingControl()](https://github.com/maptiler/maptiler-geocoding-control#example-for-openlayers-using-module-bundler) plugin for OpenLayers utilizes [MapTiler Geocoding API](https://www.maptiler.com/cloud/geocoding/). With this control, users of your application can find any place on Earth (States, Cities, Streets, ...) down to the address level, restrict the search area to a specific country, highlight search results on the map, autocomplete words while typing, and much more.

<div class="tab-content cdn-steps" markdown="1">
<pre><code class="language-js"><!--
map.addControl(new openlayersMaptilerGeocoder.GeocodingControl({ apiKey: `YOUR_MAPTILER_API_KEY_HERE` }));
--></code></pre>
</div>

<div class="tab-content bundler-steps" markdown="1">
<pre><code class="language-js"><!--
import { GeocodingControl } from "@maptiler/geocoding-control/openlayers";
import "@maptiler/geocoding-control/style.css";

...

map.addControl(new GeocodingControl({ apiKey: `YOUR_MAPTILER_API_KEY_HERE` }));
--></code></pre>
</div>

Check out the [OpenLayers geocoding control how to search places](./examples/geocoding-control/) example.

## Learn more

If you want to learn how to initialize a map and load the style, see the [Learn the basics - How to use OpenLayers](./how-to-use-openlayers/) tutorial.

Unlock your OpenLayers mapping potential now! Look at the [OpenLayers JS examples](/openlayers/examples/) we have prepared, from a quick start with OpenLayers to advanced examples like using vector tiles with OpenLayers.
