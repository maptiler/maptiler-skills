# Source: https://docs.maptiler.com/mobile-sdk\android\examples\heatmap-helper\

# 

This example show how to aggregate point features into a heatmap. Control style options like weight, radius, intensity, opacity, and optionally use a color ramp.

The vector layer helpers take your data and styling options and create the right source + layers on the current map style with minimal code. Helpers normalize sensible defaults like zoom range, outlines, etc. so you can get results quickly.



## Basic flow

```kotlin
import com.maptiler.maptilersdk.map.MTMapView
import com.maptiler.maptilersdk.map.MTMapOptions
import com.maptiler.maptilersdk.map.MTMapViewController
import com.maptiler.maptilersdk.map.style.MTMapReferenceStyle
import com.maptiler.maptilersdk.helpers.MTHeatmapLayerOptions
import com.maptiler.maptilersdk.helpers.MTHeatmapLayerHelper

// After your MTMapView is on screen (Compose example)
val controller = MTMapViewController(context)
MTMapView(
    referenceStyle = MTMapReferenceStyle.DATAVIZ,
    options = MTMapOptions(),
    controller = controller,
)

// 1) Get the style once available
controller.style?.let { style ->
    val helper = style.heatmapHelper()
    val options = MTHeatmapLayerOptions(
        data = "https://docs.maptiler.com/sdk-js/assets/earthquakes.geojson",
        property = "mag", // optional weight property
        weight = 1.0,
        radius = 20.0,
        intensity = 1.0,
        opacity = 0.8,
    )
    helper.addHeatmap(options)
}
```

## Create a hetmap using a color ramp

```kotlin
import com.maptiler.maptilersdk.map.MTMapView
import com.maptiler.maptilersdk.map.MTMapOptions
import com.maptiler.maptilersdk.map.MTMapViewController
import com.maptiler.maptilersdk.map.style.MTMapReferenceStyle
import com.maptiler.maptilersdk.helpers.MTHeatmapLayerOptions
import com.maptiler.maptilersdk.helpers.MTHeatmapLayerHelper
import com.maptiler.maptilersdk.colorramp.MTColorRamp
import kotlinx.coroutines.launch

// After your MTMapView is on screen (Compose example)
val controller = MTMapViewController(context)
MTMapView(
    referenceStyle = MTMapReferenceStyle.DATAVIZ,
    options = MTMapOptions(),
    controller = controller,
)

val scope = rememberCoroutineScope()
scope.launch {
    val style = controller.style ?: return@launch
    val rampCollection = style.colorRampCollection()
    val ramp: MTColorRamp = rampCollection.turbo()
    val helper = style.heatmapHelper()
    val options = MTHeatmapLayerOptions(
        data = "https://docs.maptiler.com/sdk-js/assets/earthquakes.geojson",
        property = "mag",
        radius = 20.0,
    )
    helper.addHeatmap(options, ramp)
}
```

## Learn more

Check the [MTHeatmapLayerHelper](/mobile-sdk/android/api/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-heatmap-layer-helper/) reference to understand how to create and manage point layers.

Review [MTHeatmapLayerOptions](/mobile-sdk/android/api/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-heatmap-layer-options/) to explore all available configuration options.
