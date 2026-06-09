# Source: https://docs.maptiler.com/mobile-sdk\ios\examples\point-helper\

# 

This example show how to render point features as circles with clustering and labels.

The vector layer helpers take your data and styling options and create the right source + layers on the current map style with minimal code. Helpers normalize sensible defaults like zoom range, outlines, etc. so you can get results quickly.



## Basic flow

This example show how to render point features as circles

```swift
import MapTilerSDK

// Assume you have an MTMapView already on screen
let mapView: MTMapView = ...

Task { @MainActor in
    guard let style = mapView.style else { return }

    // 1) Pick the helper for your geometry type
    let pointHelper = MTPointLayerHelper(style)

    // 2) Provide data + options
    let options = MTPointLayerOptions(
        data: "https://docs.maptiler.com/sdk-js/assets/earthquakes.geojson",
        pointColor: "#1e90ff",
        pointRadius: 6,
        outline: true,
        outlineColor: "white",
        outlineWidth: 1
    )

    // 3) Add the layer
    await pointHelper.addPoint(options)
}
```

## Points with clustering and labels

```swift
import MapTilerSDK

// Assume you have an MTMapView already on screen
let mapView: MTMapView = ...

Task { @MainActor in
    guard let style = mapView.style else { return }

    let helper = MTPointLayerHelper(style)

    // Simple points
    let points = MTPointLayerOptions(
        data: "https://docs.maptiler.com/sdk-js/assets/earthquakes.geojson",
        pointColor: "#1e90ff",
        pointRadius: 6,
        pointOpacity: 0.9,
        outline: true,
        outlineColor: "white",
        outlineWidth: 1
    )
    await helper.addPoint(points)

    // With labels and clustering
    let clustered = MTPointLayerOptions(
        data: "https://docs.maptiler.com/sdk-js/assets/earthquakes.geojson",
        cluster: true,
        showLabel: true,
        labelColor: "#111111"
    )
    await helper.addPoint(clustered)
}
```

## Learn more

Check the [MTPointLayerHelper](/mobile-sdk/ios/api/Classes/MTPointLayerHelper/) reference to understand how to create and manage point layers.

Review [MTPointLayerOptions](/mobile-sdk/ios/api/Structs/MTPointLayerOptions/) to explore all available configuration options.
