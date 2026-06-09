# Source: https://docs.maptiler.com/mobile-sdk\android\examples\point-helper-cluster\

# 

This example showcases how to generate a cluster map using the point layer helper with its default configurations.

If your map contains a layer with a significant number of points, you have the option to configure clustering, which aids in visually extracting valuable information from your data. This is where a cluster map, also referred to as a bubble map, proves to be beneficial.

When you activate clustering, point features that are a certain distance apart on the screen are grouped into a cluster. The size of the cluster or bubble corresponds to the number of markers it contains. By zooming in closer on your map, you can view the individual points and interact with them.

By default, the label is displayed, indicating the number of elements contained within each cluster.

<div class="mobile-viewer p-1">
  <video height="100%" controls muted poster="./img/cluster-2.png">
    <source src="./img/cluster-2.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <div class="mobile-case"></div>
</div>

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
import com.maptiler.maptilersdk.map.style.MTMapReferenceStyle
import com.maptiler.maptilersdk.helpers.MTPointLayerHelper
import com.maptiler.maptilersdk.helpers.MTPointLayerOptions

class PointHelperActivity : ComponentActivity() {
  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)

    // Replace with your MapTiler API key
    MTConfig.apiKey = "MY_API_KEY"

    setContent {
      PointHelperMap()
    }
  }
}

@Composable
fun PointHelperMap() {
  val controller = remember { MTMapViewController(baseContext) }

  LaunchedEffect(controller) {
    controller.delegate = object : MTMapViewDelegate {
      override fun onMapViewInitialized() {
        controller.style?.let { style ->
          MTPointLayerHelper(style).addPoint(
            MTPointLayerOptions(
              data = "https://docs.maptiler.com/sdk-js/assets/earthquakes.geojson",
              cluster = true,
            ),
          )
        }
      }

      override fun onEventTriggered(event: MTEvent, data: MTData?) { /* no-op */ }
    }
  }


  MTMapView(
    referenceStyle = MTMapReferenceStyle.DATAVIZ,
    options = MTMapOptions(),
    controller = controller,
    modifier = Modifier.fillMaxSize(),
    styleVariant = MTMapStyleVariant.DARK,
  )
}
```

<div class="text-center">
<div class="mobile-viewer-portrait p-1">
  <video height="100%" controls muted poster="./img/cluster-1.png">
    <source src="./img/cluster-1.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <div class="mobile-case-portrait"></div>
</div>
</div>
