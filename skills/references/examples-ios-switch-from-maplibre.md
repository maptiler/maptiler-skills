# Source: https://docs.maptiler.com/mobile-sdk\ios\examples\switch-from-maplibre\

# 

This tutorial provides guidance on transitioning from MapLibre iOS to the MapTiler SDK Swift. If you currently use MapLibre’s iOS SDK, switching to MapTiler Swift is straightforward.

<div class="mobile-viewer p-1">
  
  <div class="mobile-case"></div>
</div>

In most cases, you only need to replace the MapLibre dependency with the MapTiler SDK Swift, set the API key once via `MTConfig.shared.setAPIKey`, and swap MapLibre-specific classes/usages for the typed MapTiler SDK Swift APIs (`MTMapView`, `MTMapOptions`, `MTMapReferenceStyle`, `MTMapViewContainer` for SwiftUI, etc.). You’ll also replace style URLs containing ?key=... with strong-typed styles and optional language/terrain/globe/space options.

Next, see the main changes to migrate your app from MapLibre iOS to MapTiler Swift.

## Installation

Replace the package dependency to use the MapTiler SDK Swift.

### MapLibre iOS (Swift Package Manager)

```swift
// Xcode: File > Add Packages…
// URL: https://github.com/maplibre/maplibre-gl-native-distribution

// Package.swift example
dependencies: [
.package(url: "https://github.com/maplibre/maplibre-gl-native-distribution ", from: "X.Y.Z")
],
targets: [
.target(
    name: "YourApp",
    dependencies: ["MapLibre"]
)
]
```

### MapTiler SDK Swift (Swift Package Manager)

```swift
// Xcode: File > Add Packages…
// URL: https://github.com/maptiler/maptiler-sdk-swift
// Product: MapTilerSDK
// Package.swift example
dependencies: [
.package(url: "https://github.com/maptiler/maptiler-sdk-swift ", from: "A.B.C") // use latest
],
targets: [
.target(
    name: "YourApp",
    dependencies: ["MapTilerSDK"]
)
]
// Set API key once (e.g., at app startup)
Task { await MTConfig.shared.setAPIKey("YOUR_API_KEY") }
```

> [!INFO]
> Find the latest version of MapTiler SDK Swift at [maptiler/maptiler-sdk-swift](https://github.com/maptiler/maptiler-sdk-swift/releases)

## Replace MapLibre Classes With MapTiler SDK Types

Search your app and replace MapLibre classes and helpers with MapTiler Swift equivalents. Some examples below.

### MapLibre iOS (UIKit)

```swift
import MapLibre
import UIKit

class ViewController: UIViewController, MGLMapViewDelegate {
var mapView: MGLMapView!

  override func viewDidLoad() {
    super.viewDidLoad()

    let styleURL = URL(string: "https://api.maptiler.com/maps/streets-v4/style.json?key=YOUR_API_KEY")!

    mapView = MGLMapView(frame: view.bounds, styleURL: styleURL)
    mapView.autoresizingMask = [.flexibleWidth, .flexibleHeight]
    mapView.delegate = self

    view.addSubview(mapView)
  }
}
```

### MapTiler SDK Swift — SwiftUI

```swift
import SwiftUI
import CoreLocation
import MapTilerSDK
struct MyMapView: View {
  @State private var mapView = MTMapView(
    options: MTMapOptions(
      center: CLLocationCoordinate2D(latitude: 47.3799, longitude: 8.5419),
      zoom: 10.68
    )
  )
  var body: some View {
    MTMapViewContainer(map: mapView)
      .referenceStyle(.streets)
      .styleVariant(.defaultVariant)
  }
}
```

### MapTiler SDK Swift — UIKit

```swift
import UIKit
import CoreLocation
import MapTilerSDK
class ViewController: UIViewController, MTMapViewDelegate {
  var mapView: MTMapView!
  override func viewDidLoad() {
    super.viewDidLoad()
    let options = MTMapOptions(
      center: CLLocationCoordinate2D(latitude: 47.3799, longitude: 8.5419),
      zoom: 10.68
    )
    mapView = MTMapView(frame: view.bounds, options: options, referenceStyle: .streets)
    mapView.autoresizingMask = [.flexibleWidth, .flexibleHeight]
    mapView.delegate = self
    view.addSubview(mapView)
  }
}
```

## Migrate The Basemap Styles

Use MapTiler’s predefined styles without embedding ?key=... or hardcoding style versions.

### MapLibre iOS

```swift
let styleUrl = URL(string: "https://api.maptiler.com/maps/streets-v4/style.json?key=YOUR_API_KEY")!

mapView.styleURL = styleUrl
```

### MapTiler SDK Swift — SwiftUI

```swift
MTMapViewContainer(map: mapView)
.referenceStyle(.streets)           // typed style, always latest
.styleVariant(.dark)                // optional: .light/.pastel/etc.
```

### MapTiler SDK Swift — UIKit

```swift
// Either pick reference style at init:
let mapView = MTMapView(frame: view.bounds, options: options, referenceStyle: .streets)
// Or set/change after initialization (e.g., in delegate didInitialize):
func mapViewDidInitialize(_ mapView: MTMapView) {
  mapView.style?.setStyle(.streets, styleVariant: .dark)
}
//Optional: Language
// Set label language (e.g., device default or a specific country language)
await mapView.setLanguage(.special(.auto))
// or
// optional: .light/.pastel/etc.
```

## Camera Animation

### MapLibre iOS

```swift
// Move camera
let camera = MGLMapCamera(lookingAtCenter: nextCoord, altitude: 4500, pitch: 30, heading: 0)
mapView.setCamera(camera, animated: false)

// Animate camera
let animated = MGLMapCamera(lookingAtCenter: nextCoord, altitude: 4500, pitch: tilt, heading: bearing)
mapView.setCamera(animated, withDuration: 7.5, animationTimingFunction: CAMediaTimingFunction(name: .easeInEaseOut))
```

### MapTiler SDK Swift

```swift
// Jump / Ease / Fly
await mapView.jumpTo(
nextCoord, options:
  MTCameraOptions(
    zoom: 11.0,
    bearing: 0.0,
    pitch: 30.0
  )
)
await mapView.easeTo(
  nextCoord,
  options: MTCameraOptions(zoom: 12.0),
  animationOptions: nil
)
let fly = MTFlyToOptions(curve: nil, minZoom: nil, speed: 0.5, screenSpeed: nil, maxDuration: nil)
await mapView.flyTo(
  nextCoord,
  options: fly,
  animationOptions: nil
)
```

## Add Sources and Layers

### MapLibre iOS

```swift
let source = MGLShapeSource(identifier: "mySource", url: URL(string: "https://example.com/example.geojson")!, options: nil)

let line = MGLLineStyleLayer(identifier: "myLayer", source: source)
line.lineColor = NSExpression(forConstantValue: UIColor.red)
line.lineWidth = NSExpression(forConstantValue: 1.5)

if let style = mapView.style {
  style.addSource(source)
  style.addLayer(line)
}
```

### MapTiler SDK Swift — SwiftUI

```swift
MTMapViewContainer(map: mapView) {
  MTGeoJSONSource(identifier: "mySource", url: URL(string: "https://example.com/example.geojson")!)
  MTLineLayer(identifier: "myLayer", sourceIdentifier: "mySource")
    .color(.red)
    .width(1.5)
}
.referenceStyle(.basic)
.styleVariant(.defaultVariant)
```

### MapTiler SDK Swift — UIKit

```swift
let source = MTGeoJSONSource(identifier: "mySource", url: URL(string: "https://example.com/example.geojson")!)
let line = MTLineLayer(identifier: "myLayer", sourceIdentifier: source.identifier)
line.color = .red
line.width = 1.5
try await mapView.style?.addSource(source)
```

## Custom Annotations

While MapLibre iOS uses `MGLPointAnnotation` and `MGLAnnotationView` for overlays, MapTiler SDK Swift provides `MTMarker`, `MTTextPopup`, and `MTCustomAnnotationView` for fully custom UIKit views.

```swift
import MapTilerSDK
import CoreLocation
import UIKit
final class MyCalloutView: MTCustomAnnotationView {
  init(coord: CLLocationCoordinate2D) {
    super.init(size: CGSize(width: 120, height: 48), coordinates: coord)
    // Build your view hierarchy (add subviews, labels, etc.)
    backgroundColor = .systemBackground
    layer.cornerRadius = 8
  }
  required init?(coder: NSCoder) { super.init(coder: coder) }
}
// Add to map (after map initialized)
let callout = MyCalloutView(
  coord: CLLocationCoordinate2D(latitude: 50.08804, longitude: 14.42076)
)
await callout.addTo(mapView)
```

For more info take a look at our [custom annotations example](/mobile-sdk/ios/examples/custom-annotations/).

## Markers, Globe and Space

MapTiler SDK Swift also gives you options to change map projection to Globe, add space background behind it and annotate your data with markers.

### SwiftUI

```swift
@State private var mapView = MTMapView(
options: MTMapOptions(
    center: CLLocationCoordinate2D(latitude: 50.08804, longitude: 14.42076),
    zoom: 3.2,
    projection: .globe,                                 
    space: .config(MTSpace(preset: .milkywayColored)) 
  )
)
var body: some View {
MTMapViewContainer(map: mapView)
    .referenceStyle(.aquarelle)
    .didInitialize {
      Task {
        await mapView.addMarker(MTMarker(coordinates: CLLocationCoordinate2D(latitude: 50.08804, longitude: 14.42076)))
      }
    }
}
```

### UIKit

```swift
let options = MTMapOptions(
  center: CLLocationCoordinate2D(latitude: 50.08804, longitude: 14.42076),
  zoom: 3.2,
  projection: .globe,
  space: .config(MTSpace(preset: .milkywayColored))
)
let mapView = MTMapView(frame: view.bounds, options: options, referenceStyle: .aquarelle)
mapView.delegate = self
view.addSubview(mapView)
func mapViewDidInitialize(_ mapView: MTMapView) {
  let pin = MTMarker(coordinates: CLLocationCoordinate2D(latitude: 50.08804, longitude: 14.42076))
  mapView.addMarker(pin)
}
```

<div class="text-center">
<div class="mobile-viewer-portrait p-1">
  
  <div class="mobile-case-portrait"></div>
</div>
</div>
