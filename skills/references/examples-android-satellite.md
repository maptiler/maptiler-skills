# Source: https://docs.maptiler.com/mobile-sdk\android\examples\satellite\

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

```kotlin
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import com.maptiler.maptilersdk.MTConfig
import com.maptiler.maptilersdk.map.LngLat
import com.maptiler.maptilersdk.map.MTMapOptions
import com.maptiler.maptilersdk.map.MTMapView
import com.maptiler.maptilersdk.map.MTMapViewController
import com.maptiler.maptilersdk.map.style.MTMapReferenceStyle

class SatelliteComposeActivity : ComponentActivity() {
  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)

    // Replace with your MapTiler API key
    MTConfig.apiKey = "MY_API_KEY"

    setContent {
      SatelliteMap()
    }
  }
}

@Composable
fun SatelliteMap() {
  val controller = remember { MTMapViewController(baseContext) }

  MTMapView(
    referenceStyle = MTMapReferenceStyle.SATELLITE,
    options = MTMapOptions(
      center = LngLat(17.100917, 48.142691),
      zoom = 15.71,
    ),
    controller = controller,
    modifier = Modifier.fillMaxSize(),
  )
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
