# Source: https://docs.maptiler.com/mobile-sdk\ios\examples\polygon-helper\

# 

This example show how to render Polygon/Multipolygon features with styles options like fill, optional pattern, and outline.

The vector layer helpers take your data and styling options and create the right source + layers on the current map style with minimal code. Helpers normalize sensible defaults like zoom range, outlines, etc. so you can get results quickly.



## Basic flow

This example show how to render Polygon/Multipolygon features with fill, optional pattern, and outline.

```swift
import MapTilerSDK

// Assume you have an MTMapView already on screen
let mapView: MTMapView = ...

Task { @MainActor in
    guard let style = mapView.style else { return }

    let helper = MTPolygonLayerHelper(style)

    let polygonOptions = MTPolygonLayerOptions(
        data: "...GeoJSON polygon(s)...", // URL or inline string
        fillColor: "#1e90ff",
        fillOpacity: 0.5,
        outline: true,
        outlineColor: "white",
        outlineWidth: 1.2,
        outlineOpacity: 0.9
    )

    await helper.addPolygon(polygonOptions)
}
```

## Learn more

Check the [MTPolygonLayerHelper](/mobile-sdk/ios/api/Classes/MTPolygonLayerHelper/) reference to understand how to create and manage point layers.

Review [MTPolygonLayerOptions](/mobile-sdk/ios/api/Structs/MTPolygonLayerOptions/) to explore all available configuration options.
