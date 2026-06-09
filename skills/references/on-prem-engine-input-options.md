# Source: https://docs.maptiler.com/engine/input-options/

# The input files and related options

## [Supported input file formats](#supported-input-file-formats)

MapTiler Engine is able to open and process a large number of raster geodata formats, including: GeoTIFF, Erdas Imagine, ECW, MrSID, JPEG2000, SDTS, DTED, NITF, HDF4/5, BSB/KAP, OziExplorer, etc.

The complete list of [supported formats is available online here](https://support.maptiler.com/i279-supported-formats).

## [Spatial reference system](#spatial-reference-system)

Practically any modern existing georeferencing coordinate system (SRS - spatial reference system, e.g. geodetic datum + map projection with parameters) is supported, which means the software can process almost any geodata you may have available from all over the world.

In case the input files contain already the definition of a used coordinate system (SRS) then MapTiler Engine is able to load it and directly use this information for the transformation of the maps. In case this information is missing in the supplied file or it is incorrect (the maptiler place the maps on a wrong location, you can still assign the information about the spatial reference system with an option:

##### [-srs [definition]](#-srs-definition)  
Dataset projection. Can be WKT, EPSG code in the form of 'epsg:XXXX', PROJ.4 string. Beware of escaping. To search for identifiers or definitions use [EPSG.io](https://epsg.io/) or [spatialreference.org](https://spatialreference.org/).

Example of assigning the United Kingdom spatial reference OSGB to a GeoTIFF file before rendering:

``` bash
  maptiler-engine -o tiles -srs EPSG:27700 map_in_osgb.tif
```

## [Transparency from a color](#transparency-from-a-color)

##### [-nodata [r] [g] [b]](#-nodata-r-g-b)  
This command is typically used to eliminate borders of multiple map sheets that are stitched together. You can set a specific color of the map to be considered fully transparent during rendering.

Example for removing fully black border around a map:

``` bash
  maptiler-engine -o tiles map.tif -nodata 0 0 0
```

## [Georeference / calibration](#georeference--calibration)

Georeferencing can also be done visually using [GUI](https://www.maptiler.com/how-to/georeferencing/) or [online tool](https://www.georeferencer.com/).

For proper rendering of the maps the location of supplied input files in the known coordinate system (SRS) must be available. MapTiler Engine is loading the geolocation automatically from the internal headers of the input files (such as GeoTIFF) or from external supportive files (such as ESRI WorldFile) if they are available.

To enforce a custom selected georeference information or loading from external files these options are available:

##### [-bbox [minx] [miny] [maxx] [maxy]](#-bbox-minx-miny-maxx-maxy)
To manually set bounds of a file in the specified spatial reference system.

##### [-geotransform [posX] [scaleX] [rotX] [posY] [rotY] [scaleY]](#-geotransform-posx-scalex-rotx-posy-roty-scaley)  
To assign affine transformation directly. This option can be also used with its short name `-gt`.

##### [-georeference [path_to_file]](#-georeference-path_to_file)
An option to load external georeference from World File, Tab File, OziExplorer Map File or .prj file.

##### [-corners [east1] [north1] [east2] [north2] [east3] [north3]](#-corners-east1-north1-east2-north2-east3-north3)  
To assign affine transformation with 3 corner points: [0, 0], [width, 0], [width, height]. This option can be used with WGS84 Coordinate System (EPSG:4326) as arguments `lng1 lat1 lng2 lat2 lng3 lat3`, which will set up -srs EPSG:4326 for files without a specified Coordinate system.

The geolocation can be specified using three or more control points - GCP (Ground Control Point). Each GCP is defined by the position on the raster (pixel_x and pixel_y), which is associated with a georeferenced location (easting northing [elevation]). The last element (elevation) is mostly zero.

##### [-gcp [x_pixel] [y_pixel] [easting] [northing] [elevation]](#-gcp-x_pixel-y_pixel-easting-northing-elevation)  
To assign a ground control point. At least three control points are required. The last elemet `[elevation]` is optional value.

##### [-order [value]](#-order-value)  
An option to set the polynomial order for transformation method of assigned GCPs. Supported orders are 0 (auto), 1 (affine) and 2 (polynomial of second order). By default, the automatic order is selected based on a number of GCP points.

##### [-tps](#-tps)
Force the use of Thin Plate Spline transformer based on assigned GCP points. This option cannot be used with `-order`. This option is recommended for more than 10 assigned GCPs.

Example for using TPS transformation with assigned GCPs:

``` bash
  maptiler-engine -o tiles map.tif -srs EPSG:26712 -tps -gcp 0 0 386638.171 3999090.834 -gcp 5400 0 399627.528 3999090.834 -gcp 5400 6800 399627.528 3982553.605
```

## [Cutline (Crop)](#cutline-crop)

There are two command line options for cutline: `-cutline` and `-cutline_proj`. They specify the cutline (a clipping path) for an input image in pixels or in projected coordinates. They both expect a file name. The file can be either CSV or an OGR dataset (such as ESRI ShapeFile .shp).

From an OGR file, MapTiler Engine will load all polygons and multi-polygons from all features of the first layer.

The CSV format with pixel coordinates of nodes of a triangle, more lines will create polygon:

``` csv
  X1,Y1
  X2,Y2
  X3,Y3
```

##### [-cutline [path]](#-cutline-path)  
A pixel-based cutline is specific for each input file - so the parameter should be used after a filename (see section [MapTiler Engine Command Structure](#maptiler-engine-command-structure)).

Example of use of such a pixel-based cutline:

``` bash
  maptiler-engine -o outputdir input.tif -cutline polygon.csv
```

##### [-cutline_proj [path]](#-cutline_proj-path)  
A cutline with geocoordinates can be used for multiple files if it is specified before the first input file.

Another example of cutline with geocoordinates stored in a .shp file (may require accompanying .prj file with a coordinate system):

``` bash  
  maptiler-engine -o outputdir input.tif -cutline_proj shape.shp
```

##### [-cutline IGNORE](#-cutline-ignore)
Ignore embedded cutline of the file.

Example:

``` bash
  maptiler-engine -o outputdir input_with_cutline.tif -cutline IGNORE
```

## [Color correction](#color-correction)

MapTiler Engine allows you to specify several parameters in order to improve the colors of the output map. The MapTiler Engine Pro (GUI) is able to estimate these values interactively, but you can also use the following options to specify them manually.

##### [-color_gamma [r] [g] [b]](#-color_gamma-r-g-b)
Specify gamma correction of the individual channels, higher values result in brighter pixels (1 = unchanged).

##### [-color_contrast [contrast] [bias]](#-color_contrast-contrast-bias)
Higher values of "contrast" result in bigger different between dark and light areas (0 = unchanged).

Use "bias" if you want to keep more details in the dark/light areas (0.5 = equal, <0.5 = details in light areas, >0.5 = details in dark areas)

##### [-color_saturation [saturation]](#-color_saturation-saturation)
Modify saturation of the map (1 = unchanged, 0 = grayscale, >1 = colorful)

## [Multiple files into multiple MBTiles or Folders](#multiple-files-into-multiple-mbtiles-or-folders)

MapTiler Engine is designed to produce a single merged layer from multiple input files. If you need to process multiple files and for each produce separate tileset then a batch processing is recommended.

Example:

This command processes every .tif file in a local directory and creates .mbtiles from each in the output directory. If .mbtiles is removed from the command, it produces separate directories instead. The command differs on operating systems:

Windows

``` bash
  for %f in (*.tif) do ( echo %f && maptiler-engine -o output/%f.mbtiles %f )
```

When used in a batch file the %f must be %%f.

Linux / macOS

``` bash
  for %f in *tif; do echo $f; maptiler-engine -o output/`basename $f .tif`.mbtiles $f; done;
```
