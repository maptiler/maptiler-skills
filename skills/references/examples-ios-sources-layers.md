# Source: https://docs.maptiler.com/mobile-sdk\ios\examples\sources-layers\

# 

[MapTiler SDK iOS](/mobile-sdk/ios/) is a set of tools for creating and customizing maps on your mobile devices, using Swift language. In this guide you will learn how to add different types of sources and layers to your map as well as how to customize them. If you haven’t already, read through our [Getting Started](/mobile-sdk/ios/examples/get-started/) guide to set up your project and initialize the map view.

<p align="center">
  
</p>

## Source Types

Sources state which data the map should display. Currently available sources are *VectorTile* and *GeoJSON*.

### VectorTile

VectorTile source must be in vector tile format. You can supply a direct url to the source or tiles and it will fetch the proper resources. All layers that use this source must specify **sourceLayer** property.

```swift
if let sourceURL = URL(string: "https://api.maptiler.com/tiles/countries/{z}/{x}/{y}.pbf?key=YOUR_MAPTILER_API_KEY_HERE"), let style = mapView.style {
  let source = MTVectorTileSource(identifier: "myVectorTileSource", tiles: [sourceURL])
  style.addSource(source)
}
```

You can customize it with additional options:

* *bounds* - An array containing the longitude and latitude of the southwest and northeast corners of the source’s bounding box in the following order: [sw.lng, sw.lat, ne.lng, ne.lat].
* *maxZoom* - Maximum zoom level for which tiles are available.
* *minZoom* - Minimum zoom level for which tiles are available.
* *scheme* - Influences the y direction of the tile coordinates. 

### GeoJSON

Any valid GeoJSON file can be used as a source, you can provide remote or local urls as well as JSON string.

```swift
if let sourceURL = URL(string: "https://docs.maptiler.com/sdk-js/assets/earthquakes.geojson"), let style = mapView.style {
  let source = MTGeoJSONSource(identifier: "myGeoJSONSource", url: sourceURL)
  style.addSource(source)
}
```

You can customize it with additional options:

* *buffer* - Size of the tile buffer on each side. Larger values produce fewer rendering artifacts near tile edges and slower performance.
* *isCluster* - If the data is a collection of point features, sets the points by radius into groups.
* *clusterMaxZoom* - Max zoom on which to cluster points if clustering is enabled.
* *clusterRadius* - Radius of each cluster if clustering is enabled. 
* *maxZoom* - Maximum zoom level for which tiles are available.
* *tolerance* - Douglas-Peucker simplification tolerance.
* *lineMetrics* - Specifies whether to calculate line distance metrics.

## Layer Types

A layer provides style instructions that describe the visual properties that apply when rendering the layer on a map. Currently available layers are *Fill*, *Symbol* and *Line*.

### Fill

The fill style layer renders one or more filled (and optionally stroked) polygons on a map.

```swift
if let sourceURL = URL(string: "https://api.maptiler.com/tiles/countries/{z}/{x}/{y}.pbf?key=YOUR_MAPTILER_API_KEY_HERE"), let style = mapView.style {
  let source = MTVectorTileSource(identifier: "myVectorTileSource", tiles: [sourceURL])
  style.addSource(source)

  let layer = MTFillLayer(identifier: "myFilLayer", sourceIdentifier: source.identifier)
  layer.color = .blue
  layer.sourceLayer = "administrative"
  style.addLayer(layer)
}
```

You can customize it with additional options:

* *maxZoom* - The maximum zoom level for the layer.
* *minZoom* - The minimum zoom level for the layer.
* *shouldBeAntialised* - Boolean indicating whether or not the fill should be antialiased.
* *color* - The color of the filled part of this layer.
* *opacity* - The opacity of the entire fill layer.
* *outlineColor* - The outline color of the fill.
* *translate* - The geometry’s offset. Units in pixels. Values are [x, y] where negatives indicate left and up, respectively.
* *translateAnchor* - Enum controlling the frame of reference for translate.
* *sortKey* - Features with a higher sort key will appear above features with a lower sort key.
* *visibility* - Enum controlling whether this layer is displayed.

### Symbol

The symbol style layer renders icon and text labels at points or along lines on a map.

```swift
if let sourceURL = URL(string: "https://docs.maptiler.com/sdk-js/assets/earthquakes.geojson"), let style = mapView.style {
  let source = MTGeoJSONSource(identifier: "myGeoJSONSource", url: sourceURL)
  style.addSource(source)

  let layer = MTSymbolLayer(identifier: "mySymbolLayer", sourceIdentifier: source.identifier)
  layer.icon = UIImage.checkmark
  style.addLayer(layer)
}
```

You can customize it with additional options:

* *maxZoom* - The maximum zoom level for the layer.
* *minZoom* - The minimum zoom level for the layer.
* *visibility* - Enum controlling whether this layer is displayed.

### Line

The line style layer renders one or more stroked polylines on the map.

```swift
if let sourceURL = URL(string: "https://api.maptiler.com/tiles/landcover/{z}/{x}/{y}.pbf?key=YOUR_MAPTILER_API_KEY_HERE"), let style = mapView.style {
  let source = MTVectorTileSource(identifier: "myVectorTileSource", tiles: [sourceURL])
  style.addSource(source)

  let layer = MTLineLayer(identifier: "myLineLayer", sourceIdentifier: source.identifier)
  layer.width = 2.0
  layer.color = .blue
  layer.sourceLayer = "globallandcover"
  style.addLayer(layer)
}
```

You can customize it with additional options:

* *maxZoom* - The maximum zoom level for the layer.
* *minZoom* - The minimum zoom level for the layer.
* *blur* - Blur of the line.
* *cap* - The display of line endings.
* *color* - The color with which the line will be drawn.
* *dashArray* - The lengths of the alternating dashes and gaps that form the dash pattern.
* *gapWidth* - Line casing outside of a line’s actual path.
* *gradient* - The gradient with which to color a line feature.
* *join* - The display of lines when joining.
* *miterLimit* - Used to automatically convert miter joins to bevel joins for sharp angles.
* *offset* - The line’s offset.
* *opacity* - Optional number between 0 and 1 inclusive.
* *roundLimit* - Used to automatically convert round joins to miter joins for shallow angles.
* *sortKey* - Features with a higher sort key will appear above features with a lower sort key.
* *translate* - The geometry’s offset.
* *translateAnchor* - Controls the frame of reference for translate.
* *width* - Width of the line.
* *visibility* - Enum controlling whether this layer is displayed.

## Demo - Add Contours

Follow our [Getting Started](/mobile-sdk/ios/examples/get-started/) guide to set up a map, implement `MTMapViewDelegate` and add contours source and layer inside `mapViewDidInitialize` method or as content of `MTMapViewContainer` (SwiftUI).

### UIKit

```swift
guard let style = mapView.style else {
  return
}

if let contoursTilesURL = URL(string: "https://api.maptiler.com/tiles/contours-v2/{z}/{x}/{y}.pbf?key=YOUR_MAPTILER_API_KEY_HERE") {
  let contoursDataSource = MTVectorTileSource(identifier: "contoursSource", tiles: [contoursTilesURL])
  style.addSource(contoursDataSource)

  let contoursLayer = MTLineLayer(identifier: "contoursLayer", sourceIdentifier: contoursDataSource.identifier, sourceLayer: "contour_ft")
  contoursLayer.color = .brown
  contoursLayer.width = 2.0

  style.addLayer(contoursLayer)
}
```

### SwiftUI

```swift
@State private var mapView = MTMapView(options: MTMapOptions(zoom: 2.0))

var body: some View {
  MTMapViewContainer(map: mapView) {
    MTVectorTileSource(identifier: "countoursSource", tiles: [URL(string: "https://api.maptiler.com/tiles/contours-v2/{z}/{x}/{y}.pbf?key=YOUR_MAPTILER_API_KEY_HERE")])

    MTLineLayer(identifier: "contoursLayer", sourceIdentifier: "countoursSource", sourceLayer: "contour_ft")
      .color(.brown)
      .width(2.0)

  }
}
```

Alternatively add content on custom actions:

```swift
@State private var mapView = MTMapView(options: MTMapOptions(zoom: 2.0))

let coordinates = CLLocationCoordinate2D(latitude: 47.137765, longitude: 8.581651)

var body: some View {
  MTMapViewContainer(map: mapView) {
  }
  .didInitialize {
    if let contoursTilesURL = URL(string: "https://api.maptiler.com/tiles/contours-v2/{z}/{x}/{y}.pbf?key=YOUR_MAPTILER_API_KEY_HERE") {
      let contoursDataSource = MTVectorTileSource(identifier: "contoursSource", tiles: [contoursTilesURL])
      style.addSource(contoursDataSource)
  
      let contoursLayer = MTLineLayer(identifier: "contoursLayer", sourceIdentifier: contoursDataSource.identifier, sourceLayer: "contour_ft")
      contoursLayer.color = .brown
      contoursLayer.width = 2.0
  
      style.addLayer(contoursLayer)
    }
  }
}
```



Run the app.

## Learn more

To learn about more advanced functionalities of the SDK, refer to the [API reference](/mobile-sdk/ios/), or build your own documentation in Xcode: Product -> Build Documentation.

In addition to the documentation take a look at the plug and play examples provided in the SDK GitHub repository, as well as pre-made demo app:

<p id="github-link" class="m-0 d-inline-block">
  <span>
  
  <a class="text-secondary mb-2" href="https://github.com/maptiler/maptiler-sdk-swift/tree/main/Examples" target="_blank"
  rel="noopener noreferrer"> maptiler/maptiler-sdk-swift/Examples</a>
  </span> 
</p>

<script defer>
  setTimeout(() => {
    $("#toc").empty();
    $("#toc").toc({headings: "h2,h3"});
  }, 300);
</script>
