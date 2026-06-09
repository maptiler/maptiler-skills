# Source: https://docs.maptiler.com/guides/how-maps-work/map-resolution/

# 

Map **resolution** defines the level of detail visible on a map at a specific **zoom level**. MapTiler uses a tiling system based on the Spherical Mercator projection (EPSG:3857), where the world is divided into a [pyramid of tiles](/google-maps-coordinates-tile-bounds-projection/) across different zoom levels. As you increase the zoom level, the resolution also increases, providing more detail for a smaller geographic area.

## Zoom levels explained

As resolution is directly tied to zoom level, it's necessary to understand what are the zoom levels, what's visible on each, and also how they behave depending on data type:

* **Raster tiles**: Pre-rendered images with a fixed resolution per tile. If you zoom beyond the maximum available tile zoom, the map will appear pixelated as the device stretches the existing pixels.
* **Vector tiles**: Contain mathematical points and lines, making them resolution-independent. Labels and features remain sharp at any scale, though the *density of data* is managed by the zoom level to maintain readability and performance.

The table below lists the zoom levels with clickable examples for both types of data. 

| Zoom | View | What's visible | Raster map | Vector map |
| :--- | :--- | :--- | :--- | :--- |
| **0–3** | Global | Entire Earth, continents, and oceans. | <a href="./0-3-satellite.webp" target="_blank"></a> | <a href="./0-3-vector.webp" target="_blank"></a>
| **4–5** | Continental | Large-scale geographical features and broad weather patterns. | <a href="./4-5-satellite.webp" target="_blank"></a> | <a href="./4-5-vector.webp" target="_blank"></a>
| **6–9** | Regional | Extensive river systems, mountain ranges, and large metropolitan areas. | <a href="./6-9-satellite.webp" target="_blank"></a> | <a href="./6-9-vector.webp" target="_blank"></a>
| **<span style="white-space: nowrap;">10–14</span>** | City view | City layouts, major highways, and significant urban features. | <a href="./10-14-satellite.webp" target="_blank"></a> | <a href="./10-14-vector.webp" target="_blank"></a>
| **15–16** | Streets | Neighborhood views where individual buildings become recognizable. | <a href="./15-16-satellite.webp" target="_blank"></a> | <a href="./15-16-vector.webp" target="_blank"></a>
| **17–18** | Street blocks | Highly detailed views of street layouts, parking lots, and vehicles. | <a href="./17-18-satellite.webp" target="_blank"></a> | <a href="./17-18-vector.webp" target="_blank"></a>
| **19–20** | Buildings | Building features, roof structures, and architectural details. | <a href="./19-20-satellite.webp" target="_blank"></a> | <a href="./19-20-vector.webp" target="_blank"></a>
| **21+** | Details | Fine details such as street furniture. Typically only available for areas of particular interest. | <a href="./21-satellite.webp" target="_blank"></a> | <a href="./21-vector.webp" target="_blank"></a>

**Note:** At zoom levels 15–16, aerial imagery typically replaces satellite imagery to provide higher clarity. Extreme zoom levels (21+) often use drone imagery.

## Resolution and tile size

The resolution (meters per pixel) is determined by the zoom level and tile size. While the industry historically used 256&nbsp;px tiles, MapTiler uses&nbsp;512 px tiles as the standard for both vector and raster data. 

- **256×256 px: legacy standard**
- **512×512 px: MapTiler standard**

A 512&nbsp;px tile covers the same geographic area as four 256&nbsp;px tiles, which means that MapTiler's zoom levels appear one level sharper than the legacy industry standard and work well also on hi-res displays like Retina.

## Resolution and scales {#table}

The values below represent the resolution at the equator for our **standard 512&nbsp;px tiles**. Note that for the 512&nbsp;px tiles, the resolution at a given zoom level is equivalent to the next zoom level in the 256&nbsp;px standard. To explore map tiles at different resolutions and zoom levels, <a href="https://labs.maptiler.com/showcase/tiles-map-demo/" target="_blank">see our interactive demo</a>.

<!-- Resolution table  start -->
<div class="row">
  <div class="col-sm-12 text-center pb-2">
    <div id="raster_size" class="form-check form-switch d-flex align-items-center justify-content-center p-0">
      <label for="raster_size_512">256&times;256&nbsp;px</label>
      <input type="checkbox" class="form-check-input m-0 mx-1 switch-equal tilesizeInput" id="raster_size_512" checked>
      <label for="raster_size_512">512&times;512&nbsp;px</label>
    </div>
  </div>
</div>
<div class="row">
  <div class="col-sm-12">
    <div id="expandTable">
      <div class="table-responsive border border-light border-bottom-0">
      
| Zoom level | Resolution (meters/pixel) | Map scale at&nbsp;96&nbsp;DPI/PPI | Map width and height (pixels) |
| --- | --- | --- | --- |


    </div>
  </div>
</div>



<!-- Resolution table  end -->
