# Source: https://docs.maptiler.com/mobile-sdk\android\examples\fly-to\

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

```kotlin
import android.graphics.Color
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.runtime.Composable
import androidx.compose.runtime.DisposableEffect
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import com.maptiler.maptilersdk.MTConfig
import com.maptiler.maptilersdk.events.MTEvent
import com.maptiler.maptilersdk.map.LngLat
import com.maptiler.maptilersdk.map.MTMapOptions
import com.maptiler.maptilersdk.map.MTMapView
import com.maptiler.maptilersdk.map.MTMapViewController
import com.maptiler.maptilersdk.map.MTMapViewDelegate
import com.maptiler.maptilersdk.map.options.MTCameraOptions
import com.maptiler.maptilersdk.map.options.MTFlyToOptions
import com.maptiler.maptilersdk.map.style.MTMapReferenceStyle
import com.maptiler.maptilersdk.map.style.MTMapStyleVariant
import com.maptiler.maptilersdk.map.style.MTStyle
import com.maptiler.maptilersdk.map.style.dsl.Expression
import com.maptiler.maptilersdk.map.style.dsl.Filter
import com.maptiler.maptilersdk.map.style.dsl.MTFeatureKey
import com.maptiler.maptilersdk.map.style.dsl.PropertyValue
import com.maptiler.maptilersdk.map.style.layer.circle.MTCircleLayer
import com.maptiler.maptilersdk.map.style.layer.circle.colorExpr
import com.maptiler.maptilersdk.map.style.layer.circle.radiusExpr
import com.maptiler.maptilersdk.map.style.source.MTGeoJSONSource
import com.maptiler.maptilersdk.map.types.MTData
import java.net.URL

class FlyToAnimationsComposeActivity : ComponentActivity() {
  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    // Replace with your MapTiler API key
    MTConfig.apiKey = "MY_API_KEY"
    setContent {
      FlyToAnimationsComposeMap()
    }
  }
}

@Composable
fun FlyToAnimationsComposeMap() {
  val controller = remember { MTMapViewController(baseContext) }

  LaunchedEffect(controller) {
    controller.delegate =
      object : MTMapViewDelegate {
        override fun onMapViewInitialized() {
          setupSchoolLayers(controller.style!!)

          // Start simple camera animation after layers are added
          startLocationAnimation(controller)
        }

        override fun onEventTriggered(event: MTEvent, data: MTData?) {
          // no-op for this example
        }
      }
  }

  DisposableEffect(controller) { onDispose { controller.delegate = null } }

  MTMapView(
    referenceStyle = MTMapReferenceStyle.DATAVIZ,
    options = MTMapOptions(),
    controller = controller,
    modifier = Modifier.fillMaxSize(),
    styleVariant = MTMapStyleVariant.LIGHT,
  )
}

private fun setupSchoolLayers(style: MTStyle) {
  val src =
      MTGeoJSONSource.fromUrl(
          identifier = "schools",
          url = URL("https://docs.maptiler.com/sdk-js/assets/Public_School_Characteristics_2020-21_no_prop.geojson"),
      ).apply {
          isCluster = true
          clusterRadius = 90.0
          clusterMaxZoom = 12.0
      }
  style.addSource(src)

  val clusters =
    MTCircleLayer(identifier = "schools-clusters", sourceIdentifier = src.identifier)
      .apply {
        withFilter(
          PropertyValue.array(
            PropertyValue.Str("all"),
            Filter.clusters(),
            PropertyValue.array(
              PropertyValue.Str(">="),
              Expression.get(MTFeatureKey.POINT_COUNT),
              PropertyValue.Num(100.0),
            ),
          ),
        )
        maxZoom = 10.5
        radiusExpr(
          Expression.step(
            input = Expression.get(MTFeatureKey.POINT_COUNT),
            default = PropertyValue.Num(16.0),
            stops = listOf(
              100.0 to PropertyValue.Num(22.0),
              750.0 to PropertyValue.Num(30.0),
            ),
          ),
        )
        colorExpr(
          Expression.step(
            input = Expression.get(MTFeatureKey.POINT_COUNT),
            default = PropertyValue.Color(Color.parseColor("#f1f075")), // yellow (low)
            stops = listOf(
              100.0 to PropertyValue.Color(Color.parseColor("#f59e0b")), // orange (mid)
              750.0 to PropertyValue.Color(Color.parseColor("#ef4444")), // red (high)
            ),
          ),
        )
      }
  style.addLayer(clusters)

  style.setPaintProperty(
    layerId = clusters.identifier,
    name = "circle-opacity",
    value =
      PropertyValue.array(
        PropertyValue.Str("interpolate"),
        PropertyValue.array(PropertyValue.Str("linear")),
        PropertyValue.array(PropertyValue.Str("zoom")),
        PropertyValue.Num(3.0), PropertyValue.Num(0.85),
        PropertyValue.Num(10.0), PropertyValue.Num(0.85),
        PropertyValue.Num(10.5), PropertyValue.Num(0.0),
      ),
  )
}

private fun startLocationAnimation(controller: MTMapViewController) {
  data class Location(val zoom: Double, val center: LngLat)

  val locations = listOf(
    Location(11.37, LngLat(-73.9757, 40.7684)), // NYC
    Location(11.82, LngLat(-71.07515, 42.37131)), // Boston
    Location(11.48, LngLat(-87.6922, 41.8699)), // Chicago
    Location(3.9, LngLat(-97.04, 38.17)), // USA overview
    Location(10.62, LngLat(-122.3241, 47.6127)), // Seattle
    Location(10.3, LngLat(-122.3634, 37.6689)), // SF Bay
    Location(11.15, LngLat(-95.3843, 29.75)), // Houston
    Location(3.9, LngLat(-97.04, 38.17)), // USA overview
  )

  val handler = Handler(Looper.getMainLooper())
  var idx = 0

  val flyOptions = MTFlyToOptions(curve = null, minZoom = null, speed = 0.2, screenSpeed = null, maxDuration = null)

  val runnable = object : Runnable {
    override fun run() {
      val loc = locations[idx % locations.size]
      controller.flyTo(
        cameraOptions = MTCameraOptions(center = loc.center, zoom = loc.zoom),
        flyToOptions = flyOptions,
      )
      idx++

      handler.postDelayed(this, 5000L)
    }
  }

  // Initial delay to ensure map is fully idle
  handler.postDelayed(runnable, 2500L)
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
