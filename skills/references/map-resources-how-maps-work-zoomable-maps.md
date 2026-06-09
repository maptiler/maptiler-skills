# Source: https://docs.maptiler.com/guides/general/google-maps-coordinates-tile-bounds-projection/

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/ol@/ol.css">


<link href="https://cdn.maptiler.com/maptiler-geocoding-control//style.css" rel="stylesheet">


<div class="row align-items-center justify-content-center justify-content-md-between text-center text-md-start">
  <div class="col-md-6 order-2 order-md-0 mb-2 mb-md0">
    <h1 class="text-primary">Tiles à la Google maps</h1>
    <h2>Coordinates, tile bounds, projection</h2>
    <p class="my-3 text-darker">Learn how zoomable maps works, why they're typically in Mercator projection, and what coordinate systems they can use.</p>
  </div>
  <div class="col-sm-8 col-md-6">
    
  </div>
</div>

<iframe allow="fullscreen" src="https://labs.maptiler.com/showcase/tiles-map-demo/" width="100%" 
  height="400px" title="MapTiler Showcase Demo"></iframe>

<p><a href="https://labs.maptiler.com/showcase/tiles-map-demo/" target="_blank">Explore map tiles in full screen</a></p>

<div class="row justify-content-center justify-content-md-between">
  <div class="col-md-12">
    <h2 class="my-2">How a zoomable map works</h2>
  </div>
  <p>People have been using coordinate systems and map projections to transform the shape of Earth into usable flat maps for centuries.</p>
  <p>A map of the entire world is too big to be directly displayed on a computer. Therefore, there is a clever mechanism for quick browsing and zooming on maps: the map tiles.</p>
  <p>The world is divided into small squares, each with a fixed geographic area and scale. This clever trick allows you to browse just a small part of the planet without loading the whole map, and you still get an illusion of exploring a single huge document.</p>
</div>

<div class="row justify-content-center justify-content-md-between">
  <div class="text-center text-md-start order-2 order-md-0">
    <h2>Spherical Mercator</h2>
    <p class="my-3 bigger text-darker">Map projection pioneered by Google, now standardized.</p>
    <p>Google Maps was one of the first systems for displaying dynamic maps on the web. They chose a Spherical Mercator projection because it preserves shape and angles. The entire world looks like a square, making it easy to work with on a computer.</p>
      <picture>
      <source type="image/webp" srcset="https://media.maptiler.com/old/img/tools/mercator-epsg-img.webp">
        
    </picture>
    <p>Almost every open source (like OpenStreetMap) and commercial Maps API provider (like MapTiler) are now using this projection and tiling profile. The tiles are therefore compatible with each other.
    </p>
  </div>
</div>

<div class="row">
  <div class="col-sm-12">
    <h2>Coordinate systems for using global map tiles</h2>
  </div>
</div>
<div class="row py-3 justify-content-center align-items-center">
  <div class="col-sm-7 col-md-3 text-center">
    
  </div>
  <div class="col-md-9">
    <h3 class="my-2"><b>Degrees</b> Geodetic coordinates WGS84 (EPSG:4326)</h3>
    <div class="row">
        <p><b>Longitude and latitude</b> coordinates are used by GPS devices for defining position on Earth using World Geodetic System defined in 1984 (WGS84).</p>
        <p class="p-1 bg-lighter"><i>WGS84 geodetic datum specifies lon/lat (lambda/phi) coordinates on defined ellipsoid shape with defined origin ([0,0] on a prime meridian).</i></p>
    </div>
  </div>
</div>
<div class="row py-3 justify-content-center align-items-center">
  <div class="col-sm-7 col-md-3 text-center">
    
  </div>
  <div class="col-md-9">
    <h3 class="my-2"><b>Meters</b> Projected coordinates Spherical Mercator (EPSG:3857)</h3>
    <div class="row">
        <p><b>Global projected coordinates</b> in meters for the entire planet. Used for raster tile generation in GIS and WM(T)S services.</p>
        <p class="p-1 bg-lighter"><i>Simpler spherical calculations are used instead of ellipsoidal. Mercator map projection deforms size (Greenland vs. Africa) and never shows poles.</i></p>
    </div>
  </div>
</div>
<div class="row py-3 justify-content-center align-items-center">
  <div class="col-sm-7 col-md-3 text-center">
    
  </div>
  <div class="col-md-9">
    <h3 class="my-2"> <b>Pixels</b> Screen coordinates XY pixels at zoom</h3>
    <div class="row">
        <p>Zoom-specific <b>pixel coordinates</b> for each level of the pyramid. Top level (zoom=0) has usually 256x256 pixels, next level 512x512, etc.</p>
        <p class="p-1 bg-lighter"><i>Devices calculate pixel coordinates at defined zoom level and determine visible viewport for an area which should be loaded from servers.</i> </p>
    </div>
  </div>
</div>
<div class="row py-3 justify-content-center align-items-center">
  <div class="col-sm-7 col-md-3 text-center">
    
  </div>
  <div class="col-md-9">
    <h3 class="my-2"><b>Tiles</b> Tile coordinates Tile Map Service (ZXY)</h3>
    <div class="row">
        <p>Coordinates of a <b>tile in the pyramid.</b> There is one tile on the top of the pyramid, then 4 tiles, 16 tiles, etc. All raster tiles have the same size, usually 256x256 or 512x512 pixels. <a href="/guides/general/raster-vs-vector-map-tiles-what-is-the-difference-between-the-two-data-types">Vector tiles work a bit differently</a>.</p>
        <p class="p-1 bg-lighter"><i>Only relevant tiles are loaded and displayed for the area of interest (viewport).</i> </p>
    </div>
  </div>
</div>



