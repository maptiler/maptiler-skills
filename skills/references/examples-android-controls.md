# Source: https://docs.maptiler.com/mobile-sdk\android\examples\controls\

# 

The term _control_ is commonly used for all sorts of buttons and information display that take place in one of the corner of the map area. The most well know are probably the zoom in `[+]` and zoom out `[-]` buttons as well as the attribution information.

This example shows how to add controls during your map initialization and enable most common map interactions instantly.

<div class="mobile-viewer p-1">
  <video height="100%" controls muted poster="./img/controls-2.png">
    <source src="./img/controls-2.mp4" type="video/mp4">
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
import com.maptiler.maptilersdk.map.types.MTMapCorner

class ControlsComposeActivity : ComponentActivity() {
  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)

    // Replace with your MapTiler API key
    MTConfig.apiKey = "MY_API_KEY"

    setContent {
      ControlsMap()
    }
  }
}

@Composable
fun ControlsMap() {
  val controller = remember { MTMapViewController(baseContext) }

  MTMapView(
    referenceStyle = MTMapReferenceStyle.STREETS,
    options = MTMapOptions(
      center = LngLat(8.94738, 45.97812),
      zoom = 12.0,

      // Built-in controls
      terrainControlIsVisible = true,
      navigationControlIsVisible = true,
      projectionControlIsVisible = true,
      scaleControlIsVisible = true,
      geolocateControlIsVisible = true,
      attributionControlIsVisible = true,
      minimapIsVisible = true,
      // Logo toggle and position
      maptilerLogoIsVisible = true, // false works for premium accounts
      logoPosition = MTMapCorner.TOP_LEFT
    ),
    controller = controller,
    modifier = Modifier.fillMaxSize(),
  )
}
```

<div class="text-center">
<div class="mobile-viewer-portrait p-1">
  <video height="100%" controls muted poster="./img/controls-1.png">
    <source src="./img/controls-1.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <div class="mobile-case-portrait"></div>
</div>
</div>
