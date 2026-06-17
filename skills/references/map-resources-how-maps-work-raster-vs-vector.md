# Source: https://docs.maptiler.com/guides/how-maps-work/raster-vector-tiles/

# Raster vs vector map tiles

This page explains the difference between raster and vector map tiles. You will learn about different MapTiler products that offer ready\-to\-use raster and vector tiles of the entire planet for your projects and applications. Also, you will find out how to create raster or vector map tiles from your own data with [MapTiler Engine](https://www.maptiler.com/engine/pricing/).

## Brief summary

- **Raster** map tiles are larger in size, less demanding on end\-users' hardware but more demanding on the server\-side performance.
 **Vector** map tiles are faster to load, and less demanding on the server\-side performance but more demanding on end\-users hardware.
- MapTiler uses both map data types. We provide [many standard tilesets](/guides/how-maps-work/maptiler-datasets/) with data for the whole world, as well as [tools](/guides/map-tiling-hosting/data-processing/) to create your own tilesets.

## Raster tiles

Web maps based on raster tiles technology are older but still widely used approach by many. In computer graphics, a raster graphic is a dot matrix data structure that represents a generally rectangular grid of pixels (points of color), viewable e.g. via a computer or mobile display. Raster images are stored in image files of varying formats.

Raster map tiles are essentially raster images. Zoomable raster maps consist of many raster map tiles (in the .png or .jpg format) placed next to each other, ordered in a pyramid scheme. This clever trick allows you to browse just a small part of the map without loading it whole while maintaining the feeling of exploring a single large document. Read more about zoomable maps and the [pyramid scheme](/google-maps-coordinates-tile-bounds-projection/).



As raster tiles are images stitched together, they can be zoomed and panned but do not provide styling capabilities on the user’s end. Raster tiles have fixed styles, defined at the time they are created (rendered). Rendering raster imagery is CPU\- and memory\-consuming. One solution, used by many web map providers, is to render tiles in advance before serving them from a server. So every time a user opens the map, the pre\-rendered tiles are simply shown on the screen which means that the requirements for end\-users' hardware are much lower while the server\-side hardware requirements are higher.

On the other hand, raster tiles are large in size, so the loading time during panning and zooming on the map may be longer, depending on the network connection speed.



### Vector map tiles

Vector tiles were introduced later, they also deliver data that are divided into roughly squared tiles. But these tiles do not consist of raster images, they are made of mathematical interpretations of geometric features such as points, curves, or polygons. Vector tiles are rendered on the client’s side with a style, which is a small text file that defines how certain map elements look and how they are displayed (e.g., a road can be defined as a solid red line placed on top of all map elements). The style also says whether the map element should be rendered at all, and what font and language are to be used for rendering the labels. So vector tiles make it easy to change the map's look & feel on the fly with minimum resources.

Vector tiles are transferred over the internet in the form of a geographic data package, which usually consists of individual tiles in the .pbf format. The map client on the end user's device will use a rendering engine to create the map in the form of an image that can be displayed to the end user to view. That is why the vector tiles are more demanding on the client’s hardware.

Vector tiles are about 20–50% of the size of raster tiles so they take less time to transmit, requiring fewer resources for processing. Moreover, they offer a high\-resolution display on all zoom levels without increasing the file size of the tiles.

Vector tiles are supported by many JavaScript libraries and SDKs for the web and mobile, such as:

* [MapLibre Open Maps SDKs](https://maplibre.org/) (JavaScript, Android, iOS)
* [Leaflet](https://leafletjs.com/) (JavaScript)
* [OpenLayers](https://openlayers.org/) (JavaScript)
* [QGIS](https://qgis.org/), [ArcGIS](https://www.arcgis.com/), and other GIS software tools



## Pros and cons

Both vector and raster map tiles have their advantages and disadvantages which impact what they are used for. Let’s take a look at the most important points:

### Vector tiles

#### Pros:

* Smaller size \- lower server space requirement
* Lower bandwidth consumption
* Faster loading time
* Smooth zooming experience
* Invisible zoom levels
* A high\-resolution display on all zoom levels without increasing the file size
* Easy and on\-the\-fly customization

#### Cons:

* Rendering on the end\-users device requires more powerful hardware

### Raster tiles

#### Pros:

* Rendering on the server \- lower requirements for end\-users hardware
* Suitable for some data types like satellite or aerial imagery

#### Cons:

* Larger size \- higher server space requirement
* Higher bandwidth consumption
* Slower loading time
* Step zooming (not smooth)
* Visible zoom levels
* Lower resolution on greater zoom levels

It is possible to mix raster with vector tiles and get the best out of both, e.g., a satellite map (raster tiles) with an overlay of streets with labels available in different languages (vector tiles). Check on the interactive map below.

## Create your own tiles 

To get started creating your own raster or vector tileset, simply [upload your files](/guides/map-data/upload-files/) into your MapTiler account and let us handle the processing, or check out [MapTiler Engine](/guides/map-tiling-hosting/data-processing/) if you prefer a powerful tool running on your own hardware.
