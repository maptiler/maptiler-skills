# Source: https://docs.maptiler.com/mobile-sdk\android\examples\add-data\

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

```kotlin
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.runtime.Composable
import androidx.compose.runtime.DisposableEffect
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.ui.Modifier
import com.maptiler.maptilersdk.MTConfig
import com.maptiler.maptilersdk.annotations.MTTextPopup
import com.maptiler.maptilersdk.annotations.MTMarker
import com.maptiler.maptilersdk.map.LngLat
import com.maptiler.maptilersdk.map.MTMapOptions
import com.maptiler.maptilersdk.map.MTMapView
import com.maptiler.maptilersdk.map.MTMapViewController
import com.maptiler.maptilersdk.map.MTMapViewDelegate
import com.maptiler.maptilersdk.map.style.MTMapReferenceStyle
import com.maptiler.maptilersdk.map.style.MTMapStyleVariant
import com.maptiler.maptilersdk.map.style.MTStyle
import com.maptiler.maptilersdk.map.types.MTData
import com.maptiler.maptilersdk.map.style.source.MTGeoJSONSource
import com.maptiler.maptilersdk.map.style.layer.circle.MTCircleLayer
import com.maptiler.maptilersdk.map.style.layer.circle.colorConst
import com.maptiler.maptilersdk.map.style.layer.circle.radiusConst
import com.maptiler.maptilersdk.events.MTEvent
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import org.json.JSONArray
import org.json.JSONObject
import java.net.URL

class EarthquakesPopupsComposeActivity : ComponentActivity() {
  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    // Replace with your MapTiler API key
    MTConfig.apiKey = "MY_API_KEY"
    setContent {
      EarthquakesPopupsComposeMap()
    }
  }
}

@Composable
fun EarthquakesPopupsComposeMap(context: Context) {
  val controller = remember { MTMapViewController(context) }
  val scope = rememberCoroutineScope()

  LaunchedEffect(controller) {
    controller.delegate = object : MTMapViewDelegate {
      override fun onMapViewInitialized() {
        scope.launch { loadEarthquakesAndStyle(controller) }
        controller.setZoom(1.8)
      }

      override fun onEventTriggered(event: MTEvent, data: MTData?) { /* no-op */ }
    }
  }

  DisposableEffect(controller) { onDispose { controller.delegate = null } }

  MTMapView(
    referenceStyle = MTMapReferenceStyle.SATELLITE,
    options = MTMapOptions(),
    controller = controller,
    modifier = Modifier.fillMaxSize(),
  )
}

private suspend fun loadEarthquakesAndStyle(controller: MTMapViewController) {
  val style = controller.style ?: return

  val url = URL("https://docs.maptiler.com/sdk-js/assets/significant-earthquakes-2015.geojson")
  val jsonString = withContext(Dispatchers.IO) { url.readText() }

  runCatching {
    val source = MTGeoJSONSource.fromJsonString(
      identifier = "significant-earthquakes-2015",
      json = jsonString,
    )
    style.addSource(source)
  }

  addEarthquakesCircleLayer(style)

  val features = JSONObject(jsonString).optJSONArray("features") ?: JSONArray()
  for (i in 0 until features.length()) {
    val feature = features.optJSONObject(i) ?: continue
    val properties = feature.optJSONObject("properties") ?: continue
    val title = properties.optString("title", null) ?: continue
    val geometry = feature.optJSONObject("geometry") ?: continue
    if (geometry.optString("type") != "Point") continue
    val coords = geometry.optJSONArray("coordinates") ?: continue
    if (coords.length() < 2) continue
    val lon = coords.optDouble(0)
    val lat = coords.optDouble(1)
    val ll = LngLat(lon, lat)

    val popup = MTTextPopup(ll, title, offset = 10.0)
    val marker = com.maptiler.maptilersdk.annotations.MTMarker(ll).apply { this.popup = popup }
    style.addMarker(marker)
  }
}

private fun addEarthquakesCircleLayer(style: MTStyle) {
  val layer = MTCircleLayer(
    identifier = "significant-earthquakes-circles",
    sourceIdentifier = "significant-earthquakes-2015",
  ).apply {
    colorConst(0xFF5722) // deep orange
    radiusConst(6.0)
  }

  style.addLayer(layer)
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
