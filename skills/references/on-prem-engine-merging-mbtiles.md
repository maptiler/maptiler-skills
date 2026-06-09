# Source: https://docs.maptiler.com/engine/utilities/

# Merge MBTiles utility

*This CLI utility is only available in [MapTiler Engine editions](https://www.maptiler.com/engine/pricing/) that include command line automation. Alternatively, you can merge your MBTiles [in a visual interface](/guides/map-tiling-hosting/data-processing/how-to-merge-tilesets-mbtiles/).* 

The utility enables you to merge multiple MBTiles into one file. This is useful if you need to update a previously rendered dataset, replacing a small existing area in a large dataset with a different, newly rendered raster data. 

## Basic usage

``` bash
  maptiler-merge-mbtiles [OPTION] BASE.mbtiles DETAIL.mbtiles [DETAIL_2.mbtiles]...
```

## Example

A typical usage scenario would consist of these steps:

1. **Render a large dataset with MapTiler Engine.** Merge several smaller input files into one large MBTiles file (with JPEG or PNG tiles internally) named `large.mbtiles`.

2. **Update one of the previously rendered input files.** Render just this one updated file into MBTiles, with the PNG32 format and zoom levels on which you want it to appear in the existing dataset. Save the new input file as `patch.mbtiles`.

3. **Update the large dataset with the new input file.** With the original dataset `large.mbtiles` and updated file `patch.mbtiles` ready, run the merge command:

``` bash
  maptiler-merge-mbtiles large.mbtiles patch.mbtiles
```

Existing tiles available in both sets will be merged. On the zoom levels that both tilesets contain, `patch.mbtiles` will replace the original `large.mbtiles`. The `large.mbtiles` file will be updated in place.

## Options

##### [-P [n]](#-p-n)
Set limit on the defined number of cores.

##### [-no_sparse](#-no_sparse)  
Fills the empty space between separate maps (if there is some) with empty tiles in a background color. This option can take longer to render, if there are huge areas between maps, as these have to be created. In case the maps overlap each other, there is no extra action involved. Default behavior without this option does not fill the empty space between separate maps.

##### [-reencode](#-reencode)
This option is useful when the 2 merged maps have a different format (e.g. jpeg and png). By default, the result is a hybrid format (combination of both of them). If reencode option is used, the chosen file is encoded to the actual format (which can slow down the process).
