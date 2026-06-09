# Source: https://docs.maptiler.com/mobile-sdk\android\examples\switch-from-mapbox\

# 

This tutorial provides guidance on transitioning from Mapbox Android SDK to the MapTiler Kotlin SDK. If you currently use Mapbox’s Android SDK, switching to MapTiler Kotlin is straightforward.

<div class="mobile-viewer p-1">
  
  <div class="mobile-case"></div>
</div>

In most cases, you only need to replace the Mapbox dependency with the MapTiler SDK Kotlin, set the API key once in `MTConfig`, and swap Mapbox-specific classes/usages for the typed MapTiler SDK Kotlin APIs (`MTMapView`, `MTMapOptions`, `MTMapReferenceStyle`, `MTMapViewController`, etc.). You’ll also replace style URIs/URLs with strong typed styles and language/terrain options.

Next, see the main changes to migrate your app from Mapbox to MapTiler Kotlin.

## Installation

Replace the Gradle dependency to use the MapTiler Kotlin SDK.

### Mapbox Android SDK (Gradle)

```kotlin
dependencies {
  implementation("com.mapbox.maps:android-ndk27:")
}
```

### MapTiler SDK Kotlin (Gradle)

```kotlin
dependencies {
  implementation("com.maptiler:maptiler-sdk-kotlin:")
}
```

> [!INFO]
> Find the latest version of MapTiler SDK Kotlin at [maptiler/maptiler-sdk-kotlin](https://github.com/maptiler/maptiler-sdk-kotlin/releases)

## Replace Mapbox Classes With MapTiler SDK Types

Search your app and replace Mapbox classes and helpers with MapTiler Kotlin equivalents. Some examples below.

### Mapbox Android SDK

```kotlin
MapboxMap(
  Modifier.fillMaxSize(),
  mapViewportState = rememberMapViewportState {
    setCameraOptions {
      zoom(10.68)
      center(Point.fromLngLat(8.5419, 47.3799))
      pitch(0.0)
      bearing(0.0)
    }
  },
)
```

### MapTiler SDK Kotlin - Compose

```kotlin
MTConfig.apiKey = "YOUR_API_KEY"
val controller = MTMapViewController(context)
MTMapView(
  referenceStyle = MTMapReferenceStyle.STREETS,
  options = MTMapOptions(center = LngLat(8.5419, 47.3799), zoom = 10.68),
  controller = controller
)
```

### MapTiler SDK Kotlin - XML

```kotlin
MTConfig.apiKey = "YOUR_API_KEY"
val controller = MTMapViewController(context)
findViewById<MTMapViewClassic>(R.id.classicMapView).initialize(
  referenceStyle = MTMapReferenceStyle.STREETS,
  options = MTMapOptions(center = LngLat(8.5419, 47.3799), zoom = 10.68),
  controller = controller
)
```

## Migrate The Basemap Styles

Use MapTiler’s predefined styles.

### Mapbox Android SDK

```kotlin
MapboxMap(
  style = { MapboxStandardStyle() }
)
```

### MapTiler SDK Kotlin

```kotlin
// Always latest style; no URL or key in the string
val reference = MTMapReferenceStyle.STREETS
// Optional variant:
styleVariant = MTMapStyleVariant.DARK
```

## Camera Animation

### Mapbox Android SDK

```kotlin
// define camera position
val cameraPosition = CameraOptions.Builder()
  .zoom(zoom)
    .center(it.point)
    .build()

// set camera position
mapView.mapboxMap.setCamera(cameraPosition)

// fly to
mapboxMap.flyTo(
  target,
   mapAnimationOptions {
      duration(12_000)
    }
)
```

### MapTiler SDK Kotlin

```kotlin
val controller = MTMapViewController(context)
val cameraOptions = MTCameraOptions(center, zoom, bearing, pitch)
controller.jumpTo(cameraOptions)
controller.easeTo(cameraOptions)
controller.flyTo(cameraOptions)
```

## Add Sources and Layers

### Mapbox Android SDK

```kotlin
LineLayer(
  sourceState = rememberGeoJsonSourceState {
    data = GeoJSONData("https://example.com/example.geojson")
  }
) {
  lineColor = ColorValue(Color.Red)
  lineWidth = DoubleValue(1.5)
 }
```

### MapTiler SDK Kotlin

```kotlin
val source = MTGeoJSONSource(identifier = "mySource", url = URL("https://example.com/example.geojson"))
val lineLayer = MTLineLayer(identifier = "myLayer", sourceIdentifier = source.identifier)
lineLayer.sourceLayer = "contour"
lineLayer.color = Color.RED
lineLayer.width = 1.5
controller.style?.addSource(source)
controller.style?.addLayer(lineLayer)
```

## Custom Annotations

While Mapbox Android uses annotations API to add map overlays, MapTiler SDK Kotlin uses `MTCustomAnnotationView` and `MTCustomAnnotationViewClassic` for Compose and XML respectively.

```kotlin
// Compose: Place MTCustomAnnotationView as a sibling composable above MTMapView
// inside a stacking container (e.g., Box)
MTCustomAnnotationView(
  controller = controller,
  coordinates = LngLat(14.42076, 50.08804),
  modifier = Modifier
) {
  // Your composable (e.g., Card/Text/Icon)
}
// XML: MTCustomAnnotationViewClassic is a container: add your own child Android Views
// into it to render custom UI.
val annotation = MTCustomAnnotationViewClassic(
  context = this,
  widthPx = 120, heightPx = 48,
  initialCoordinates = LngLat(14.42076, 50.08804)
)
// Inflate your custom layout into the container
LayoutInflater.from(this).inflate(R.layout.my_custom_layout, annotation, true)
annotation.addTo(mapView, controller)
```

For more info take a look at our [custom annotations example](/mobile-sdk/android/examples/custom-annotations/).

## Markers, Globe and Space

MapTiler SDK Kotlin also gives you options to change map projection to Globe, add space background behind it and annotate your data with markers.

### Compose

```kotlin
// Set once in your app (e.g., Application.onCreate)
MTConfig.apiKey = "YOUR_API_KEY"
val controller = MTMapViewController(context).apply {
  // Add marker only after the map is ready
  delegate = object : MTMapViewDelegate {
    override fun onMapViewInitialized() {
      // Map is initialized
    }
    override fun onEventTriggered(event: MTEvent, data: MTData?) {
      if (event == MTEvent.ON_READY) {
        val location = LngLat(14.42076, 50.08804)
        style?.addMarker(MTMarker(location))
      }
    }
  }
}
// Enable globe projection and add space background behind it
val options = MTMapOptions(
  projection = MTProjectionType.GLOBE,
  space = MTSpaceOption.Config(
    MTSpace(preset = MTSpacePreset.MILKYWAY_COLORED)
  )
)
MTMapView(
  referenceStyle = MTMapReferenceStyle.AQUARELLE,
  options = options,
  controller = controller,
  modifier = Modifier.fillMaxSize()
)
```

### XML

```kotlin
// XML layout contains: <com.maptiler.maptilersdk.map.MTMapViewClassic android:id="@+id/classicMapView" ... />
MTConfig.apiKey = "YOUR_API_KEY"
val controller = MTMapViewController(this).apply {
  delegate = object : MTMapViewDelegate {
    override fun onMapViewInitialized() {
      // Map is initialized
    }
    override fun onEventTriggered(event: MTEvent, data: MTData?) {
      if (event == MTEvent.ON_READY) {
        style?.addMarker(MTMarker(LngLat(14.42076, 50.08804)))
      }
    }
  }
}
val options = MTMapOptions(
  projection = MTProjectionType.GLOBE,
  space = MTSpaceOption.Config(MTSpace(preset = MTSpacePreset.MILKYWAY_COLORED))
)
val classic = findViewById<MTMapViewClassic>(R.id.classicMapView)
classic.initialize(
  referenceStyle = MTMapReferenceStyle.AQUARELLE,
  options = options,
  controller = controller
)
```

<div class="text-center">
<div class="mobile-viewer-portrait p-1">
  
  <div class="mobile-case-portrait"></div>
</div>
</div>
