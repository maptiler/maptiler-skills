# Source: https://docs.maptiler.com/mobile-sdk\ios\examples\3d-terrain\

# 

This example demonstrates how to create a 3D (three-dimensional) terrain map and display it on your mobile device using MapTiler.

Enhance the authenticity of your applications and data by incorporating terrain relief into your maps. This will provide a greater sense of realism and depth to your visuals.

<div class="mobile-viewer p-1">
  <video height="100%" controls muted poster="./img/terrain-2.png">
    <source src="./img/terrain-2.mp4" type="video/mp4">
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
      center: CLLocationCoordinate2D(latitude: 8.94738, longitude: 45.97812),
      zoom: 14,
      maxZoom: 14,
      pitch: 70,
      maxPitch: 85,
      bearing: -100.86,
      terrainIsEnabled: true
    )
  )

  var body: some View {
    MTMapViewContainer(map: mapView)
      .referenceStyle(.outdoor)
  }
}
```

<div class="text-center">
<div class="mobile-viewer-portrait p-1">
  <video height="100%" controls muted poster="./img/terrain-1.png">
    <source src="./img/terrain-1.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <div class="mobile-case-portrait"></div>
</div>
</div>
