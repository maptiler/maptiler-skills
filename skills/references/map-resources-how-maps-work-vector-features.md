# Source: https://docs.maptiler.com/guides/how-maps-work/vector-feature/

# 

Vector data is one of the most common types of map data. It consists of **vector features** which represent real-life objects as geometric shapes: **points, lines, and polygons**. That's different from [raster data](/guides/general/raster-vs-vector-map-tiles-what-is-the-difference-between-the-two-data-types/) which uses images and pixels. Overall, vector features are more lightweight, easier to create and style, and suitable for [adding your own map data](/guides/map-data/use-vector-data/). 

## Geometry

Vector features consist of two parts: **geometry** and **properties**. Geometry is the shape that represents an object:

- **Point** geometry (vertex) represents objects that occupy a single spot, for example lamps, traffic lights, single trees, or bus stops.
- **Line** geometries (edges) represent linear objects such as roads, highways, electric wires, and similar objects.
- **Polygons** are enclosed lines that represent areal objects like buildings, forests, crop fields, and so on.

Here's what raw, unstyled vector features look like:



As you can see, the basic three geometries are sufficient to show pretty much anything on a map. Of course, sometimes you need to combine them to get the best representation of an object. For example, a river stream can use lines for the banks, and a polygon for the water body itself.

## Properties

Properties are attribute values that hold additional information about the object they represent. For example, for a road object (which is represented as line geometry) you can add properties such as road ID, owner, or last date of snow cleaning – whatever you need.

## Working with vector features

Every point, line, and polygon counts as one vector feature. So, if you have data with 5 points of interest (POI), 10 roads, and 5 buildings, it is in total 20 vector features. This is important to understand because the number of vector features affects how the vector data is stored and handled.

Vector data come in two formats, which you can both create with our tools: 

- As a **single file** (typically GeoJSON). You can create, edit, and export such file in our [**Vector data editor**](/guides/vector-data-editor/).

- As a **vector tileset**. In this case, vector features are split into multiple map tiles and stored in a container file, which is handy when a single file becomes too large. At MapTiler, we set specific [size limits](/guides/maps-apis/maps-platform/dataset-upload-formats-and-limits/) for vector features that you can upload as a single file – if your file is larger than these limits, you can tile it up using [**MapTiler Engine**](/guides/map-tiling-hosting/data-processing/).
