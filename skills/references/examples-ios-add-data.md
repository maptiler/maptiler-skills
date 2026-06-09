# Source: https://docs.maptiler.com/mobile-sdk\ios\examples\add-data\

# 

This example shows how you can add earthquake data from GeoJSON onto the map, and use circle layer and markers to visualize it. User can tap each marker to get the title of the earthquake.

In addition to markers and circle layer, you can use symbol, line and fill layers to visualize your data.

<div class="mobile-viewer p-1">
  <video height="100%" controls muted poster="./img/connect-2.png">
    <source src="./img/connect-2.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <div class="mobile-case"></div>
</div>

<br>

```swift
import SwiftUI
import CoreLocation
import MapTilerSDK

struct EarthquakesPopupsView: View {
  private enum Constants {
    static let sourceId = "significant-earthquakes-2015"
    static let circlesLayerId = "significant-earthquakes-circles"
    static let geojsonURL = URL(string: "https://docs.maptiler.com/sdk-js/assets/significant-earthquakes-2015.geojson")!
    static let defaultZoom = 1.8
  }

  @State private var mapView = MTMapView(
    options: MTMapOptions(
      center: CLLocationCoordinate2D(latitude: 0, longitude: 0),
      zoom: Constants.defaultZoom
    )
  )

  // Note: Best practice is to set the API key at app startup (App/Scene or AppDelegate).
  // It's set here for standalone copy-paste convenience.
  init() {
    Task { await MTConfig.shared.setAPIKey("YOUR_API_KEY") }
  }

  var body: some View {
    MTMapViewContainer(map: mapView) {
      // Ensure the source exists before we add the layer in didInitialize.
      MTGeoJSONSource(identifier: Constants.sourceId, url: Constants.geojsonURL)
    }
    .referenceStyle(.satellite)
    .styleVariant(.defaultVariant)
    .didInitialize { Task { await setupEarthquakesAndStyle() } }
  }

  // MARK: - Setup
  private func setupEarthquakesAndStyle() async {
    guard let style = mapView.style else { return }

    let layer = MTCircleLayer(identifier: Constants.circlesLayerId, sourceIdentifier: Constants.sourceId)
    layer.color = .color(UIColor(hex: "#FF5722") ?? .systemOrange) // deep orange
    layer.radius = .number(6.0)
    try? await style.addLayer(layer)

    do {
      let (data, _) = try await URLSession.shared.data(from: Constants.geojsonURL)
      let collection = try JSONDecoder().decode(FeatureCollection.self, from: data)

      for feature in collection.features {
        guard
          feature.geometry.type == "Point",
          feature.geometry.coordinates.count >= 2
        else { continue }

        let lon = feature.geometry.coordinates[0]
        let lat = feature.geometry.coordinates[1]
        guard let title = feature.properties.title else { continue }

        let coord = CLLocationCoordinate2D(latitude: lat, longitude: lon)
        let popup = MTTextPopup(coordinates: coord, text: title, offset: 10.0)
        let marker = MTMarker(coordinates: coord, popup: popup)
        await mapView.addMarker(marker)
      }
    } catch {
      print("Failed to load earthquakes GeoJSON: \(error)")
    }
  }
}

private struct FeatureCollection: Decodable {
  let features: [Feature]
}

private struct Feature: Decodable {
  let geometry: Geometry
  let properties: Properties
}

private struct Geometry: Decodable {
  let type: String
  let coordinates: [Double]
}

private struct Properties: Decodable {
  let title: String?
}
```

<div class="text-center">
<div class="mobile-viewer-portrait p-1">
  <video height="100%" controls muted poster="./img/connect-1.png">
    <source src="./img/connect-1.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <div class="mobile-case-portrait"></div>
</div>
</div>
