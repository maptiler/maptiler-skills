# Source: https://docs.maptiler.com/guides/how-maps-work/coordinate-systems/

# Map coordinate systems

A coordinate system is the first important thing that you face when making a map from scratch. A map without it is subjected to oblivion in the geospatial world as it cannot be located. Coordinate systems are what make ordinary data *geospatial*. Thanks to them, we can navigate through maps reliably and with great accuracy.

There is no coordinate system or projection that would preserve areas, angles, distances and directions of the Earth precisely. You always have to think about the purpose of your maps, scale, and type of data to choose the most fitting one.

## Flattening the Earth

We, of course, cannot replicate the Earth’s surface as it is on our maps. To transform it from a 3D to a 2D map layout, **map projections** are being used. These are mathematical algorithms within the coordinate systems. **Coordinate systems** define how to bind your map to the real locations on the Earth.

As the Earth is not flat, there will always be a distortion to some level when transforming it into the map. The important thing is what precision we need the most. Map projections can either preserve **areas, angles, distances, directions,** or **compensate** for all the distortions together.

Once we have the Earth's surface transformed into a map, coordinate systems ensure that we can navigate through it with a set of defined numbers – coordinates. When looking for a coordinate system, you may come across two terms – **geographic or projected coordinate systems**.

In the **geographic coordinate system**, the coordinates are related to an ellipsoid representing the Earth and are in the form of latitude and longitude. The most popular one is the World Geodetic System defined in 1984 (WGS84\) which is used by GPS devices.



The **projected coordinate system**, on the other hand, is flat, represented by two axes with coordinates in meters or other linear units. Web Mercator is the most commonly used one. Adopted by Google Maps in 2005, it quickly became a de\-facto standard for web mapping applications.



## Web Mercator

Web Mercator, also known as **Google Web Mercator**, **Spherical Mercator**, **WGS 84 Web Mercator,** or **Pseudo\-Mercator**, is the coordinate system that you will see on MapTiler maps.

The original Mercator projection was mainly used for **navigation purposes** as it preserves angles and pictures loxodromes as straight lines. This helped the sailors to keep a steady course during their travels.

Web Mercator differs from the original Mercator projection in a far **easier computation,** which is done on a sphere instead of an ellipsoid. The entire world is **shaped like a square,** making it easy to work with on the web. The **north is always up** on the maps and it reduces the area distortion on large scales, making it **suited for seamless zooming** with interactive world maps.

Despite its popularity in the online mapping world, Web Mercator also has its drawbacks. It **distorts areas with distance from the equator**, making Greenland almost the same size as Africa. Poles are not present on the Web Mercator maps and Antarctica is infinite in size. Therefore, it is **not usable for polar areas** at all.

## Search or trasform coordinates

To look up a coordinate system or integrate transformation coordinates into your workflow, use the [Coordinates API](https://docs.maptiler.com/cloud/api/coordinates/). 

## Local coordinate systems

The coordinate system for MapTiler base maps is the **Web Mercator**. MapTiler, however, can host documents in other map projections too. This is useful for integrating with some sources of data and to conform to region\-specific expectations of how maps should look. 

Many countries have national standards for collecting geographic information that use local coordinate systems. Each system is then usually displayed in a specific map projection. The use of local coordinates and projections predates the modern era of GPS measurements in the global WGS84 coordinate system and the ubiquity of online maps. Cadastre maps, road maps, and building plans are examples of documents that are usually available only in local coordinates. People are also used to the way their country or region looks on a map in the local projection. The Mercator projection notoriously distorts regions close to the north and south poles, and even regions further away might look unnatural.

We offer hosting for both raster and vector tilesets in custom coordinate systems. The MBTiles format of tileset container files is specified to always be in web Mercator. To upload a tileset in any other coordinate system, you have to use the GeoPackage format. MapTiler Engine is capable of producing raster GeoPackage tilesets in any projection. However, note that it can only produce vector GeoPackage tilesets in web Mercator for now.

We store vector features in WGS84 and publish them in the GeoJSON format. Due to internal limitations, it is not possible to add datasets as sources to maps operating in local coordinate systems.
