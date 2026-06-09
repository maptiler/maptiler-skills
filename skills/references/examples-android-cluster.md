# Source: https://docs.maptiler.com/mobile-sdk\android\examples\cluster\

# 

The following Jetpack Compose example demonstrates how to use the built-in Kotlin SDK functions to generate and visualize a cluster map of points.

<div class="mobile-viewer p-1">
  <video height="100%" controls muted poster="./img/cluster-2.png">
    <source src="./img/cluster-2.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <div class="mobile-case"></div>
</div>

Add an `MTGeoJSONSource` to the map's style with `isCluster: true`. Adjust the `clusterRadius` and `clusterMaxZoom` parameters as needed.

To render clusters, create an `MTCircleLayer` for the cluster bubbles. Use step expressions based on point count to determine color and size, and apply a cluster filter. Add an `MTSymbolLayer` above to display the cluster count using `MTTextToken.pointCountAbbreviated`. Finally, create another `MTCircleLayer` for individual (unclustered) points, and apply an unclustered filter to show only those.

```kotlin
import android.graphics.Color
import android.os.Bundle
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
import com.maptiler.maptilersdk.map.MTMapOptions
import com.maptiler.maptilersdk.map.MTMapView
import com.maptiler.maptilersdk.map.MTMapViewController
import com.maptiler.maptilersdk.map.MTMapViewDelegate
import com.maptiler.maptilersdk.map.style.MTMapReferenceStyle
import com.maptiler.maptilersdk.map.style.MTMapStyleVariant
import com.maptiler.maptilersdk.map.style.MTStyle
import com.maptiler.maptilersdk.map.style.dsl.MTExpression
import com.maptiler.maptilersdk.map.style.dsl.MTFilter
import com.maptiler.maptilersdk.map.style.dsl.MTFeatureKey
import com.maptiler.maptilersdk.map.style.dsl.PropertyValue
import com.maptiler.maptilersdk.map.style.layer.circle.MTCircleLayer
import com.maptiler.maptilersdk.map.style.layer.circle.colorConst
import com.maptiler.maptilersdk.map.style.layer.circle.colorExpr
import com.maptiler.maptilersdk.map.style.layer.circle.radiusConst
import com.maptiler.maptilersdk.map.style.layer.circle.radiusExpr
import com.maptiler.maptilersdk.map.style.layer.symbol.MTSymbolLayer
import com.maptiler.maptilersdk.map.style.layer.symbol.textAllowOverlap
import com.maptiler.maptilersdk.map.style.layer.symbol.MTTextAnchor
import com.maptiler.maptilersdk.map.style.layer.symbol.textAnchor
import com.maptiler.maptilersdk.map.style.layer.symbol.textColorConst
import com.maptiler.maptilersdk.map.style.layer.symbol.textField
import com.maptiler.maptilersdk.map.style.layer.symbol.textFont
import com.maptiler.maptilersdk.map.style.layer.symbol.textSize
import com.maptiler.maptilersdk.map.style.dsl.MTTextToken
import com.maptiler.maptilersdk.map.style.source.MTGeoJSONSource
import com.maptiler.maptilersdk.map.types.MTData
import java.net.URL

@Composable
fun ClusteringCompose() {
  val controller = remember { MTMapViewController(baseContext) }

  LaunchedEffect(controller) {
    controller.delegate = object : MTMapViewDelegate {
      override fun onMapViewInitialized() {
        setupClusters(controller.style!!)
      }

      override fun onEventTriggered(event: MTEvent, data: MTData?) {
        // no-op
      }
    }
  }

  DisposableEffect(controller) { onDispose { controller.delegate = null } }

  MTMapView(
    referenceStyle = MTMapReferenceStyle.DATAVIZ,
    options = MTMapOptions(),
    controller = controller,
    modifier = Modifier.fillMaxSize(),
    styleVariant = MTMapStyleVariant.DARK,
  )
}

private fun setupClusters(style: MTStyle) {
  // 1) Source with clustering
  val src = MTGeoJSONSource.fromUrl(
    identifier = "earthquakes",
    url = URL("https://docs.maptiler.com/sdk-js/assets/earthquakes.geojson"),
  ).apply {
    isCluster = true
    clusterRadius = 50.0
    clusterMaxZoom = 14.0
  }
  style.addSource(src)

  // 2) Cluster circles (inline config)
  val clusters =
    MTCircleLayer(identifier = "clusters", sourceIdentifier = src.identifier)
      .apply {
        withFilter(MTFilter.clusters())
        colorExpr(
          MTExpression.step(
            input = MTExpression.get(MTFeatureKey.POINT_COUNT),
            default = PropertyValue.Color(Color.parseColor("#51bbd6")),
            stops = listOf(
              100.0 to PropertyValue.Color(Color.parseColor("#f1f075")),
              750.0 to PropertyValue.Color(Color.parseColor("#f28cb1")),
            ),
          ),
        )
        radiusExpr(
          MTExpression.step(
            input = MTExpression.get(MTFeatureKey.POINT_COUNT),
            default = PropertyValue.Num(20.0),
            stops = listOf(
              100.0 to PropertyValue.Num(30.0),
              750.0 to PropertyValue.Num(40.0),
            ),
          ),
        )
      }
  style.addLayer(clusters)

  // 3) Cluster count labels (inline config)
  val labels =
    MTSymbolLayer(identifier = "clusterCount", sourceIdentifier = src.identifier)
      .apply {
        withFilter(MTFilter.clusters())
        textField(MTTextToken.POINT_COUNT_ABBREVIATED)
        textSize(12.0)
        textAllowOverlap(true)
        textAnchor(MTTextAnchor.CENTER)
        textFont(listOf("DIN Offc Pro Medium", "Arial Unicode MS Bold"))
        textColorConst(Color.WHITE)
      }
  style.addLayer(labels)

  // 4) Unclustered points (inline config)
  val unclustered =
    MTCircleLayer(identifier = "unclusteredPoint", sourceIdentifier = src.identifier)
      .apply {
        withFilter(MTFilter.unclustered())
        colorConst(Color.parseColor("#11b4da"))
        radiusConst(4.0)
      }
  style.addLayer(unclustered)
}

/** Optional Activity wrapper to run the composable. */
class ClusteringComposeActivity : ComponentActivity() {
  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    MTConfig.apiKey = "YOUR_API_KEY"
    setContent { ClusteringCompose() }
  }
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

## XML in Kotlin

If you are working with XML in Kotlin refer to the [Kotlin XML clustering example](https://github.com/maptiler/maptiler-sdk-kotlin/blob/main/Examples/ClusteringClassic.kt)
