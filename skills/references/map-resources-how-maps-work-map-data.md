# Source: https://docs.maptiler.com/guides/how-maps-work/map-data/

# 

**Map data** is the building material for a map. If this sounds unclear, see the beginner intro [What a map consists of](/guides/getting-started/how-maps-work/#what-a-map-consists-of).

## Types of map data

Map data comes in **datasets** of various types. There are these key types: 

#### Tilesets

A tileset is a container with **map tiles**, which is map data cut into roughly square tiles and [organized into a pyramid](/google-maps-coordinates-tile-bounds-projection/) for fast and easy access. Map tiles inside a tileset can be in different formats: 

- **Raster tilesets** contain map tiles in regular image formats (PNG, JPG, WEBP...). Raster tiles are the traditional format used to store satellite and aerial imagery.

- **Vector tilesets** contain [vector features](/guides/map-tiling-hosting/data-processing/vector-feature/). These represent objects on a map as geometric shapes – points, lines, and polygons. Vector tiles are more modern, lightweight, and can be styled on the fly. See [Raster vs vector map tiles](/guides/general/raster-vs-vector-map-tiles-what-is-the-difference-between-the-two-data-types/) to learn more.

#### Vector data files 

Vector data files contain [vector features](/guides/map-tiling-hosting/data-processing/vector-feature/), just like **vector tilesets**. The difference is that a vector data file is *not tiled*. It's a single file, usually in GeoJSON format. A vector data file needs to get tiled when it's too big to be accessed as one object.

#### Other types

The mentioned dataset types (raster tilesets, vector tilesets, vector data files) are the most common, but there are other types as well, for example **raster-DEM tilesets** that contain various additional values (like elevation) encoded as standard RGB colors, or **3D quantized polygon mesh** representing 3D terrain. 

Usually, these special formats are already embedded in ready-made maps and you won't need to work with them directly.

## How to use map data

To make your final map, you'll typically need:

1. A ready-made [MapTiler map](https://www.maptiler.com/maps/){:target="_blank" rel="noopener"} as a base. All our maps contain up-to-date global map data of the right types, and you don't need to do anything special [to use them](/guides/getting-started/use-map/).

2. Your own **custom data** that you want to add to the map. See 👉 [how to add your own map data](/guides/getting-started/add-data/) to learn all about how to prepare and integrate it.

3. To build a specialized map, you may need to combine your selected MapTiler basemap with **additional MapTiler data**. See 👉 [Map data by MapTiler](/guides/map-data/maptiler-datasets/) to get more details about the individual tilesets we offer.

Both MapTiler data and your custom data can be also self-hosted. Check out [MapTiler Server](/guides/self-hosting/map-server/) if you're looking to host your map data on-prem.


