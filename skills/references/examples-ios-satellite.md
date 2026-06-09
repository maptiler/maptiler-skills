# Source: https://docs.maptiler.com/mobile-sdk\ios\examples\satellite\

# 

Display a satellite map in your mapping application. Our built-in styles (streets, satellite, hybrid, outdoor, winter, dark, etc.) are designed to make it easier for you to create beautiful maps. No need for extra coding or worrying about outdated versions.

[MapTiler’s satellite](https://www.maptiler.com/maps/satellite/) map provides up-to-date satellite imagery for the whole world, high resolution detailed aerial imagery for many countries.

<div class="mobile-viewer p-1">
  <video height="100%" controls muted poster="./img/satellite-2.png">
    <source src="./img/satellite-2.mp4" type="video/mp4">
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
      center: CLLocationCoordinate2D(latitude: 48.142691, longitude: 17.100917),
      zoom: 15.71
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
  <video height="100%" controls muted poster="./img/satellite-1.png">
    <source src="./img/satellite-1.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <div class="mobile-case-portrait"></div>
</div>
</div>
