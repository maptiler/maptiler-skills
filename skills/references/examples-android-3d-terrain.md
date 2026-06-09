# Source: https://docs.maptiler.com/mobile-sdk\android\examples\3d-terrain\

# 

This example demonstrates how to create a 3D (three-dimensional) terrain map and display it on your mobile device using MapTiler.

Enhance the authenticity of your applications and data by incorporating terrain relief into your maps. This will provide a greater sense of realism and depth to your visuals.

<div class="mobile-viewer p-1">
  <video height="100%" controls muted poster="./img/terrain-2.png">
    <source src="./img/terrain-2.mp4" type="video/mp4">
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

class TerrainComposeActivity : ComponentActivity() {
  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)

    // Replace with your MapTiler API key
    MTConfig.apiKey = "MY_API_KEY"

    setContent {
      TerrainMap()
    }
  }
}

@Composable
fun TerrainMap() {
  val controller = remember { MTMapViewController(baseContext) }

  MTMapView(
    referenceStyle = MTMapReferenceStyle.OUTDOOR,
    options = MTMapOptions(
      center = LngLat(8.94738, 45.97812),
      zoom = 14.0,
      terrainIsEnabled = true,
      pitch = 70.0,
      bearing = -100.86,
      maxPitch = 85.0,
      maxZoom = 14.0
    ),
    controller = controller,
    modifier = Modifier.fillMaxSize(),
  )
}
```

<div class="text-center">
<div class="mobile-viewer-portrait p-1">
  <video height="100%" controls muted poster="./img/terrain-1.png">
    <source src="./img/terrain-1.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <div class="mobile-case-portrait"></div>
</div>
</div>
