# Source: https://docs.maptiler.com/mobile-sdk\ios\examples\controls\

# 

The term _control_ is commonly used for all sorts of buttons and information display that take place in one of the corner of the map area. The most well know are probably the zoom in `[+]` and zoom out `[-]` buttons as well as the attribution information.

This example shows how to add controls during your map initialization and enable most common map interactions instantly.

<div class="mobile-viewer p-1">
  <video height="100%" controls muted poster="./img/controls-2.png">
    <source src="./img/controls-2.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <div class="mobile-case"></div>
</div>
<br>

```swift
import SwiftUI
import CoreLocation
import MapTilerSDK

struct ContentView: View {
  init() {
    // Best practice: set the MapTiler API key on app startup instead on init
    // Replace with your MapTiler API key
    Task { await MTConfig.shared.setAPIKey("MY_API_KEY") }
  }

  @State private var mapView = MTMapView(
    options: MTMapOptions(
      center: CLLocationCoordinate2D(latitude: 46.8, longitude: 8.33),
      zoom: 6,
      // Built-in controls
      terrainControlIsVisible: true,
      navigationControlIsVisible: true,
      geolocateControlIsVisible: true,
      projectionControlIsVisible: true,
      scaleControlIsVisible: true,
      minimapIsVisible: true,
      attributionControlIsVisible: true,
      // Logo toggle and position
      maptilerLogoIsVisible: true, // false works for premium accounts
      logoPosition: .topLeft
    )
  )

  var body: some View {
    MTMapViewContainer(map: mapView)
      .referenceStyle(.streets)
  }
}
```

<div class="text-center">
<div class="mobile-viewer-portrait p-1">
  <video height="100%" controls muted poster="./img/controls-1.png">
    <source src="./img/controls-1.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <div class="mobile-case-portrait"></div>
</div>
</div>
