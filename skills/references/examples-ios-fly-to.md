# Source: https://docs.maptiler.com/mobile-sdk\ios\examples\fly-to\

# 

This example leverages the mobile SDKs to animate transitions between major U.S. locations and visualize school distribution using a single, high-performance cluster layer. The FlyTo feature ensures smooth, clear movement between locations.

<div class="mobile-viewer p-1">
  <video height="100%" controls muted poster="./img/flyto-2.png">
    <source src="./img/flyto-2.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <div class="mobile-case"></div>
</div>

<br>

```swift
import SwiftUI
import MapTilerSDK
import CoreLocation

struct FlyToAnimationView: View {
  @State public var mapView = MTMapView(
    options: MTMapOptions(center: CLLocationCoordinate2D(latitude: 38.17, longitude: -97.04),
      zoom: 3.9)
  )

  private let sourceId = "schools"
  private let clustersLayerId = "schools-clusters"

  @State private var animationTask: Task<Void, Never>? = nil

  // Note: Best practice is to set the API key at app startup (App/Scene or AppDelegate).
  // It's set here for standalone copy-paste convenience.
  init() {
    Task { await MTConfig.shared.setAPIKey("YOUR_API_KEY") }
  }

  var body: some View {
    MTMapViewContainer(map: mapView) {
      MTGeoJSONSource(
        identifier: sourceId,
        url: URL(string: "https://docs.maptiler.com/sdk-js/assets/Public_School_Characteristics_2020-21_no_prop.geojson")!,
        isCluster: true,
        clusterMaxZoom: 12,
        clusterRadius: 90
      )
    }
    .referenceStyle(.dataviz)
    .styleVariant(.light)
    .didInitialize {
      Task {
        await setupSchoolLayers()
        startLocationAnimation()
      }
    }
    .onDisappear { animationTask?.cancel() }
  }

  @MainActor
  private func setupSchoolLayers() async {
    guard let style = mapView.style else { return }

    let clusters = MTCircleLayer(identifier: clustersLayerId, sourceIdentifier: sourceId)
    clusters.maxZoom = 10.5
    clusters.filterExpression = MTFilter.all([
      MTFilter.clusters(),
      .array([.string(">="), MTExpression.get(.pointCount), .number(100)])
    ])

    clusters.radius = .expression(
      MTExpression.step(
        input: MTExpression.get(.pointCount),
        default: .number(16.0),
        stops: [
          (100.0, .number(22.0)),
          (750.0, .number(30.0))
        ]
      )
    )

    let yellow = UIColor(hex: "#f1f075") ?? .systemYellow
    let orange = UIColor(hex: "#f59e0b") ?? .systemOrange
    let red = UIColor(hex: "#ef4444") ?? .systemRed
    clusters.color = .expression(
      MTExpression.step(
        input: MTExpression.get(.pointCount),
        default: .color(yellow),
        stops: [
          (100.0, .color(orange)),
          (750.0, .color(red))
        ]
      )
    )

    try? await style.addLayer(clusters)

    await mapView.setPaintProperty(
      forLayerId: clustersLayerId,
      property: .opacity,
      value: .array([
        .string("interpolate"),
        .array([.string("linear")]),
        .array([.string("zoom")]),
        .number(3.0), .number(0.85),
        .number(10.0), .number(0.85),
        .number(10.5), .number(0.0)
      ])
    )
  }

  @MainActor
  private func startLocationAnimation() {
    struct Location { let zoom: Double; let center: CLLocationCoordinate2D }

    let locations: [Location] = [
      Location(zoom: 11.37, center: CLLocationCoordinate2D(latitude: 40.7684, longitude: -73.9757)), // NYC
      Location(zoom: 11.82, center: CLLocationCoordinate2D(latitude: 42.37131, longitude: -71.07515)), // Boston
      Location(zoom: 11.48, center: CLLocationCoordinate2D(latitude: 41.8699, longitude: -87.6922)), // Chicago
      Location(zoom: 3.9,  center: CLLocationCoordinate2D(latitude: 38.17, longitude: -97.04)), // USA overview
      Location(zoom: 10.62, center: CLLocationCoordinate2D(latitude: 47.6127, longitude: -122.3241)), // Seattle
      Location(zoom: 10.3,  center: CLLocationCoordinate2D(latitude: 37.6689, longitude: -122.3634)), // SF Bay
      Location(zoom: 11.15, center: CLLocationCoordinate2D(latitude: 29.75, longitude: -95.3843)), // Houston
      Location(zoom: 3.9,  center: CLLocationCoordinate2D(latitude: 38.17, longitude: -97.04)) // USA overview
    ]

    var idx = 0

    let fly = MTFlyToOptions(curve: nil, minZoom: nil, speed: 0.2, screenSpeed: nil, maxDuration: nil)

    animationTask?.cancel()
    animationTask = Task { @MainActor in
      // Initial delay to ensure map is fully idle
      try? await Task.sleep(nanoseconds: 2_500_000_000)

      while !Task.isCancelled {
        let loc = locations[idx % locations.count]

        await mapView.flyTo(loc.center, options: fly, animationOptions: nil)

        idx += 1
        try? await Task.sleep(nanoseconds: 2_000_000_000)
      }
    }
  }
}
```

<div class="text-center">
<div class="mobile-viewer-portrait p-1">
  <video height="100%" controls muted poster="./img/flyto-1.png">
    <source src="./img/flyto-1.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <div class="mobile-case-portrait"></div>
</div>
</div>
