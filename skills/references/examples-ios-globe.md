# Source: https://docs.maptiler.com/mobile-sdk\ios\examples\globe\

# 

The following example demonstrates how to create a globe map, customize the map background to achieve a Milky Way effect, and add a halo around the Earth.

This option **applies only** when used with the globe projection.

<div class="mobile-viewer p-1">
  <video height="100%" controls muted poster="./img/space-2.png">
    <source src="./img/space-2.mp4" type="video/mp4">
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
      center: CLLocationCoordinate2D(latitude: 20, longitude: 0),
      zoom: 1.2,
      projection: .globe,
      space: .config(MTSpace(preset: .milkywayColored)),
      halo: .enabled(true)
    )
  )

  var body: some View {
    MTMapViewContainer(map: mapView)
      .referenceStyle(.satellite)
  }
}
```

<div class="text-center">
<div class="mobile-viewer-portrait p-1">
  <video height="100%" controls muted poster="./img/space-1.png">
    <source src="./img/space-1.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <div class="mobile-case-portrait"></div>
</div>
</div>
