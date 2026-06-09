# Source: https://docs.maptiler.com/mobile-sdk\ios\examples\point-helper-cluster\

# 

This example showcases how to generate a cluster map using the point layer helper with its default configurations.

If your map contains a layer with a significant number of points, you have the option to configure clustering, which aids in visually extracting valuable information from your data. This is where a cluster map, also referred to as a bubble map, proves to be beneficial.

When you activate clustering, point features that are a certain distance apart on the screen are grouped into a cluster. The size of the cluster or bubble corresponds to the number of markers it contains. By zooming in closer on your map, you can view the individual points and interact with them.

By default, the label is displayed, indicating the number of elements contained within each cluster.

<div class="mobile-viewer p-1">
  <video height="100%" controls muted poster="./img/cluster-2.png">
    <source src="./img/cluster-2.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <div class="mobile-case"></div>
</div>

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
    options: MTMapOptions()
  )

  var body: some View {
    MTMapViewContainer(map: mapView)
      .referenceStyle(.dataviz)
      .styleVariant(.dark)
      .didInitialize {
        Task {
          if let style = mapView.style {
            await MTPointLayerHelper(style).addPoint(
              MTPointLayerOptions(
                data: "https://docs.maptiler.com/sdk-js/assets/earthquakes.geojson",
                cluster: true
              )
            )
          }
        }
      }
  }
}
```

<div class="text-center">
<div class="mobile-viewer-portrait p-1">
  <video height="100%" controls muted poster="./img/cluster-1.png">
    <source src="./img/cluster-1.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <div class="mobile-case-portrait"></div>
</div>
</div>
