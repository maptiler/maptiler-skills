# Source: https://docs.maptiler.com/engine/output-options/

# Available output options

The default behaviour of MapTiler Engine is to write tiles each into its own file, under the directory structure:

&emsp; `output_directory/z/x/y.ext`

Where z is the zoom level, and x and y tile coordinates on relevant zoom level in the tiling profile.

The produced directory structure contains also a simple HTML viewer and description of the dataset in metadata.json, compatible with mb-util and [MapTiler Server](https://www.maptiler.com/server/) project.

MapTiler Engine supports direct output of the rendered map tiles into an SQLite database (MBTiles or GeoPackage format). This simplifies transfer and management of the tilesets and is practical for mobile applications.

## [Tiling profile / Tile Matrix Set](#tiling-profile--tile-matrix-set)

A global option defining the
output system of tiles - the target coordinate system, tile pixel size, etc. MapTiler Engine comes with these predefined most popular systems and possibility to specify a custom profile.

##### [-mercator](#-mercator)  
DEFAULT. The spherical Mercator tile profile compatible with Google, Bing, Yahoo Maps, MapQuest, OpenStreetMap, and mobile maps on iOS and Android. This is the most commonly used profile. It uses coordinate system defined as EPSG:3857 or EPSG:900913. Details [available here](https://www.maptiler.com/google-maps-coordinates-tile-bounds-projection/).

In case you wish to use different tiling system, you must specify it as the first command on the command line. These are the alternatives:

##### [-gearth](#-gearth)  
Tile profile specific for Google Earth according to the KML SuperOverlay definition.

##### [-raster](#-raster)  
Rendering raster files without a need of georeferencing is also possible.

##### [-garmin](#-garmin)  
To produce the format for Garmin GPS devices, with a size 1024x1024 pixels and output to .kml file. Afterwards, pack the tiles and the .kml tiles into a .zip archive, change its extension to .kmz and save it into the device.

##### [-custom](#-custom)  
You can specify your own tiling system. See the appropriate section under the Advanced options chapter for more information.

Example: command for producing tiles for use with Google Earth:

``` bash
  maptiler-engine -gearth -o tiles map.tif
```

Example: command for producing tiles for use with Geodetic WGS84 Plate Caree:

``` bash
  maptiler-engine -raster -o raster-tiles map.tif
```

## [Custom tiling presets](#custom-tiling-presets)

MapTiler Engine offers predefined custom tiling presets (custom tile grids) for Advanced customers. Each custom tiling preset has its own
area coverage, some are for World, other covers only specifical States or group of States.

##### [-preset geodetic](#-preset-geodetic)  
WGS84 Plate Caree / Unprojected. Compatible with most existing WMS servers, OpenLayers base map.

Example:

``` bash
  maptiler-engine -preset geodetic -o wgs84-tiles map.tif
```

##### [-preset standard_grid](#-preset-standard_grid)  
Standard global tilegrid with a selected Coordinate system. This tiling preset keeps the original coordinate system (SRS), and cuts the input map into tiles according to the spherical mercator tile profile. **Note** this is not compatible with Google Mercator profile `mercator`!

Example:

``` bash
  maptiler-engine -preset standard_grid -o st-grid-tiles map.tif
```

##### [-preset baidu](#-preset-baidu)
Tilegrid defined for China customers. This preset cover only China region and is compatible with Baidu Maps service.

Example:

``` bash
  maptiler-engine -preset baidu -o tiles map-china.tif
```

##### [-preset yandex](#-preset-yandex)  
Custom tiling preset used in Russian web mapping service, compatible with Yandex.Maps. Coverage is limitted to Russia and Ukraine.

Example:

``` bash
  maptiler-engine -preset yandex -o tiles map-russia.tif
```

##### [-preset cz_jtsk](#-preset-cz_jtsk)  
National tiling grid for Czechia and Slovakia with a precision up to 1 meter per pixel.

Example:

``` bash
  maptiler-engine -preset cz_jtsk -o cz-tiles map-czechia.tif
```

##### [-preset fr_rgf93](#-preset-fr_rgf93)
Tilegrid defined for precise overlay of maps in France, using Lambert 93 conic projection.

Example:

``` bash
  maptiler-engine -preset fr_rgf93 -o fr-tiles map-france.tif
```

##### [-preset nl_rdnew](#-preset-nl_rdnew)
National tiling grid for Netherlands - Rijksdriehoekstelsel New / Amersfoort.

Example:

``` bash
  maptiler-engine -preset nl_rdnew -o netherlands-map map-amsterdam.tif
```

##### [-preset uk_osgb [zoom_group]](#-preset-uk_osgb-zoom_group)
National tiling grid for the United Kingdom using Ordnance Survey projection. This custom preset requires a specific zoom_group, which limits output zoom levels of this grid. Supported values with zoom levels in the bracket are: `0` (z0), `1` (z1 - z2), `2` (z3 - z6), `3` (z7 - z8), `4` (z9 - z10).

Example:

``` bash
  maptiler-engine -preset uk_osgb 1 -o gb-z1 map-london.tif -zoom 1 2
  maptiler-engine -preset uk_osgb 2 -o gb-z3 map-london.tif -zoom 3 6
```

##### [-preset ch_lv03 [zoom_group]](#-preset-ch_lv03-zoom_group)
Swiss national tiling grid used in Switzerland and Liechtenstein with high precision. This custom preset requires a specific zoom group, with values from 0 to 21. These values are mostly represented for the specific zoom level. Output tiles could be combined and are compatible with SwissTopo maps.

Example:

``` bash
  maptiler-engine -preset ch_lv03 3 -o ch-z3 map-zurich.tif -zoom 3 3
  maptiler-engine -preset ch_lv03 4 -o ch-z4 map-zurich.tif -zoom 4 4
```

Note that, `-zoom 3 3` is not required and it is automatically limited as defined for this zoom group.

##### [-preset nz_nztm [zoom_group]](#-preset-nz_nztm-zoom_group)  
New Zealand Geodetic Datum (NZGD2000), official geodetic datum for New Zealand and its offshore islands. This custom preset requires a specific zoom group, which limits output zoom levels of this grid. Supported values with zoom levels in the bracket are: `0` (z0-z7), `1` (z8-z10), `2` (z11-z13), `3` (z14-z16).

Example:

``` bash
  maptiler-engine -preset nz_nztm 1 -o nz-z8 map-new-zealand.tif
```

## [Retina / HiDPI tiles](#retina--hidpi-tiles)

##### [-scale [value]](#-scale-value)  
To create high-resolution Retina / HiDPI tiles with variable floating scale. Retina tiles are available for each profile and custom tiling presets listed above. Important note, the scale value cannot exceeded max allowed tile size in pixels: 4096 x 4096. It means, max available value for `-scale` is 16.0.

Example: the command for producing standard Retina tiles in Mercator profile

``` bash
  maptiler-engine -mercator -scale 2.0 -o tiles@2x map.tif
```

Example: the command for producing Retina tiles at 1.5 scale in raster profile

``` bash
  maptiler-engine -raster -scale 1.5 -o tiles-retina map.tif
```

## [Zoom levels](#zoom-levels)

##### [-zoom [min] [max]](#-zoom-min-max)  
This option determines which layers of the tile pyramid will be generated. The default is the "native" level calculated from image resolution. In case you need to add additional zoom levels, you can either define them as absolute numeric values or as relative numbers to the “native” levels with prefix + and -.
Each input file can have its own explicit option for zoom levels.

Example: zoom levels are automatically calculated as eg. 1 - 5

``` bash
  maptiler-engine -o tiles map.tif
```

Example: zoom levels are explicitly set to be 3 - 5

``` bash
  maptiler-engine -o tiles map.tif -zoom 3 5
```

Example: zoom levels are set to be 1 - 6 with relative value to native zoom levels

``` bash
  maptiler-engine -o tiles map.tif -zoom +0 +1
```

Example: zoom levels are set to be 2 - 4 with relative value to native zoom levels

``` bash
  maptiler-engine -o tiles map.tif -zoom +1 -1
```

Example: zoom levels are set to 0 - 4, as explicit minimum, relative maximum to native zoom level

``` bash
  maptiler-engine -o tiles map.tif -zoom 0 -1
```

## [Tile formats](#tile-formats)

The produced tiles can be saved in one of several image format. MapTiler Engine includes optimization of the final filesize and used a number of colors (quantization), to minimize the disk size occupied by the rendered maps as well as the time necessary to transfer the maps to clients once the tiles are online.

### [Formats with support for transparency](#formats-with-support-for-transparency)

##### [-f png8a](#-f-png8a)
DEFAULT. Paletted RGBA PNG image optimized for rendering speed and output size

##### [-f png8qa](#-f-png8qa)
Paletted RGBA PNG image

##### [-f png or -f png32](#-f-png-or--f-png32)  
RGBA PNG image

##### [-f webp or -f webp32](#-f-webp-or--f-webp32)  
RGBA WebP image

### [Non-transparent formats](#non-transparent-formats)

##### [-f jpg or -f jpeg](#-f-jpg-or--f-jpeg)
Progressive JPEG image in the YCbCr color space

##### [-f png8](#-f-png8)
Paletted RGB PNG image optimized for rendering speed and output size

##### [-f png8q](#-f-png8q)
Paletted RGB PNG image

##### [-f png24](#-f-png24)
RGB PNG image

##### [-f webp24](#-f-webp24)  
RGB WebP image

## [Tile transparency or a background color](#tile-transparency-or-a-background-color)

No matter what input datasets you specify, after transforming them into the tiling profile projection, MapTiler Engine will handle them as RGBA images. The transparency can come from the image itself as an alpha channel (with support for partly transparent areas), it can be derived from a selected color (so-called NODATA color), or can be just a result of the transformation with the GDAL warping algorithm - for areas without available input data.

If the tile is completely transparent it is never saved to the disk to save the storage space.

If all of the pixels are fully visible (eg. opaque, maximum alpha is 255), the alpha channel is discarded and the tile is marked as non-transparent / opaque. Otherwise, the tile is marked as partly transparent with alpha.

If partly transparent tiles are saved in a tile format without support for transparency (such as JPEG specified with -f jpg option) then the background color is applied. Default background color is white (255,255,255), but you can specify your own with the option:

##### [-bg [r] [g] [b]](#-bg-r-g-b)  
The color of the background replacing transparency in the non-transparent tile formats.

For example:

``` bash
  maptiler-engine -f png8 -bg 0 128 0 ...
```

##### [-ignore_alpha](#-ignore_alpha)  
If your dataset contains four channels, but the fourth channel is not alpha channel, you can use this option to ignore this channel.

For example:

``` bash
  maptiler-engine -f png32 -ignore_alpha input_4bands.tif ...
```

## [Tile store format](#tile-store-format)

##### [-store dir|mbtiles|geopackage](#-store-dirmbtilesgeopackage)  
This option enforces the form of storage which is used for saving the rendered tiles. Possible options are the directory (dir), the MBTiles (mbtiles) and the GeoPackage (geopackage). The default is the directory, but in case the -o parameter ends with .mbtiles or .gpkg then rendering into MBTiles or GeoPackage is selected, respectively. This option specifies the store form explicitly.
**Note:** for more details on this subject read the section [Output](#output) in the chapter Usage above.

##### [-sparse](#-sparse)  
Skip the empty space between separate maps and don't create empty tiles. This option can improve the speed of rendering if there are huge areas between maps. This is the default option for `-store dir`.

##### [-no_sparse](#-no_sparse)
Fills the empty space between separate maps (if there is some) with empty tiles in the background colour. This option can take longer to render and take more disk space, if there are huge areas between maps, as these have to be created. This is a default option for `-store mbtiles` and `-store geopackage`.

Setting the sparse option in GUI is in [Advanced options dialog](https://www.maptiler.com/how-to/advanced-image-settings/).

## [MBTiles compatibility for GeoPackage](#mbtiles-compatibility-for-geopackage)

MapTiler Engine provides a toggle to make the generated GeoPackage conform to the MBTiles specification. The options to control it are:

##### [-mbtiles_compatible](#-mbtiles_compatible)
DEFAULT. The generated GeoPackage will be MBTiles-compatible. <small class="badge bg-light text-dark">>= 11.2</small>

##### [-no_mbtiles_compatible](#no_mbtiles_compatible)
MBTiles compatibility turned off. <small class="badge bg-light text-dark">>= 11.2</small>

As providing compliance with the MBTiles specification requires creating additional structures in the output GeoPackage file, its size will be slightly larger than that of the one generated without MBTiles compatibility.

## [Hybrid tile format](#hybrid-tile-format)

MapTiler Engine allows rendering into a hybrid tile format which allows transparent tiles using transparent format (such as PNG) and tiles without any transparency at all are saved in a different format (such as JPEG). For aerial photos overlays or other datasets, this can mean a significant saving of the storage. Generated files are without extensions. This is done to simplify the generated OpenLayers viewer.

Example of usage:

``` bash
  maptiler-engine -f hybrid <opaque> <transparent> ...
  maptiler-engine -f hybrid jpg png8a ...
```
## [Tile quality](#tile-quality)

There are some options to specify parameters of the conversion into
image formats, which can significantly reduce the size of produced tiles
by degrading the output.

##### [-jpg_quality [value]](#-jpg_quality-value)  
The quality of JPEG compression. A number between 10 and 95. The default is 85.

##### [-quant_quality [value]](#-quant_quality-value)
The quality of quantization. A number between 1 and 100. The default is 100.

##### [-quant_speed [value]](#-quant_speed-value)
Higher speed levels disable expensive algorithms and reduce quantization precision. Speed 1 gives marginally better quality at significant CPU cost. Speed 10 has usually 5% lower quality but is 8 times faster than speed 8. The default is 10.
*If you experience issues with the visual quality of generated tiles with quantization involved try to set -quant_speed to lower values.*

##### [-webp_quality [value]](#-webp_quality-value)  
The quality of WebP compression. A number between 1 and 100. Level 100 means lossless compression. The default is 75.

##### [-webp_alpha_quality [value]](#-webp_alpha_quality-value)  
The quality of WebP alpha channel compression. A number between 1 and 100. Level 100 means lossless compression. The default is 100.

##### [-webp_lossless](#-webp_lossless)
Lossless WebP compression switch. <small class="badge bg-light text-dark">>= 11.1</small>

##### [-webp_lossy](#-webp_lossy)  
Lossy WebP compression switch. <small class="badge bg-light text-dark">>= 11.1</small>

##### [-webp_preset [default|picture|photo|drawing|icon|text]](#-webp_preset-defaultpicturephotodrawingicontext)  
WebP compression presets that use optimal algorithm parameters for a given data type. <small class="badge bg-light text-dark">>= 11.1</small>

Example of the rendering of a seamless map out of file map1.tif and map2.tif into tiles with an internal palette with optimal colors with higher visual:

``` bash
  maptiler-engine -o tiles -f png8a -quant_quality 90 -quant_speed 4 map1.tif map2.tif
```

## [Watermark](#watermark)

##### [-watermark [image_file.png]](#-watermark-image_filepng)  
It is possible to place your own watermark over rendered tiles to protect the online maps. The file should be smaller than a size of tiles. It is placed in a random position and burned into tiles.

A nice watermark file can be easily generated online by calling the Google Chart API:
[https://placehold.co/300x50/ffffff/000000?text=%C2%A9+ABC](https://placehold.co/300x50/ffffff/000000?text=%C2%A9+ABC)

By replacing ABC at the end of this URL a custom text phrase can be specified. We recommend setting the transparency of such watermark file by using a Photoshop or similar tool before applying it with MapTiler Engine.

##### [-watermark_opacity [value]](#-watermark-opacity_value)  
Set the opacity percentage that will be applied to the watermark image. Use the integer number in range from 1 (almost transparent) to 100 (fully visible). When applying the opacity to the image that is already opaque, these opacities will be combined. The default value is 100. <small class="badge bg-light text-dark">>= 12.1</small>

Example of applying the watermark image with 70% opacity:

``` bash
  maptiler-engine -o tiles -watermark watermark_image.png -watermark_opacity 70 map.tif
```
