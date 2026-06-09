# Source: https://docs.maptiler.com/mobile-sdk\android\examples\globe\

# 

The following example demonstrates how to create a globe map, customize the map background to achieve a Milky Way effect, and add a halo around the Earth.

This option **applies only** when used with the globe projection.

<div class="mobile-viewer p-1">
  <video height="100%" controls muted poster="./img/space-2.png">
    <source src="./img/space-2.mp4" type="video/mp4">
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
import com.maptiler.maptilersdk.map.MTMapOptions
import com.maptiler.maptilersdk.map.MTMapView
import com.maptiler.maptilersdk.map.MTMapViewController
import com.maptiler.maptilersdk.map.options.MTHaloOption
import com.maptiler.maptilersdk.map.options.MTSpace
import com.maptiler.maptilersdk.map.options.MTSpaceOption
import com.maptiler.maptilersdk.map.options.MTSpacePreset
import com.maptiler.maptilersdk.map.style.MTMapReferenceStyle
import com.maptiler.maptilersdk.map.types.MTProjectionType

class GlobeSpaceHaloActivity : ComponentActivity() {
  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)

    // Replace with your MapTiler API key
    MTConfig.apiKey = "MY_API_KEY"

    setContent {
      GlobeSpaceHaloMap()
    }
  }
}

@Composable
fun GlobeSpaceHaloMap() {
  val controller = remember { MTMapViewController(baseContext) }

  MTMapView(
    referenceStyle = MTMapReferenceStyle.SATELLITE,
    options = MTMapOptions(
      projection = MTProjectionType.GLOBE,
      space = MTSpaceOption.Config(
        MTSpace(
          preset = MTSpacePreset.MILKYWAY_COLORED
        )
      ),
      halo = MTHaloOption.Enabled
    ),
    controller = controller,
    modifier = Modifier.fillMaxSize(),
  )
}
```

<div class="text-center">
<div class="mobile-viewer-portrait p-1">
  <video height="100%" controls muted poster="./img/space-1.png">
    <source src="./img/space-1.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <div class="mobile-case-portrait"></div>
</div>
</div>
