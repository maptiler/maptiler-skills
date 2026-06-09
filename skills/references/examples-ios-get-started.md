# Source: https://docs.maptiler.com/mobile-sdk\ios\examples\get-started\

# 

[MapTiler SDK iOS](/mobile-sdk/ios/) is a set of tools for creating and customizing maps on your mobile devices, using Swift language. In this guide you will learn how to add a custom map to your application, style it to your own liking, add points of interest and enable interaction.

<p align="center">
  
  
</p>

## First Steps

Open Xcode and create a new project or use existing one (Both UIKit and SwiftUI are supported).

MapTiler SDK is a Swift Package and can be added as dependency through **Swift Package Manager**.

<ul>
<li>File -> Add Package Dependencies</li>
<li> Add
  <p id="github-link" class="m-0 d-inline-block">
    <span>
    
    <a class="text-secondary mb-2" href="https://github.com/maptiler/maptiler-sdk-swift" target="_blank"
    rel="noopener noreferrer"> maptiler/maptiler-sdk-swift</a>
    </span> 
  </p>
</li>
</ul>

Once package is added to your project, make sure to set your [MapTiler API](https://cloud.maptiler.com/) key, either on app load in AppDelegate or where your project requires it:

```swift
Task {
  await MTConfig.shared.setAPIKey("YOUR_MAPTILER_API_KEY_HERE")
}
```

> [!NOTE]
> * Has to be called before map initialization
> * For Swift 6, make sure to call asynchronously


## Map Initialization

### UIKit

You can add a map to your `UIView` or `UIViewController` using `MTMapView`. Open your view controller and follow the next steps.

On top of your view add import statement:

```swift
import MapTilerSDK
```

Declare map options and map view:

```swift
let options = MTMapOptions(zoom: 2.0)
var map: MTMapView!
```

Initialize the map inside `viewDidLoad` method:

```swift
map = MTMapView(frame: view.frame, options: options, referenceStyle: .streets)
view.addSubview(map)
```

If you are using auto layout, you can call the helper function for anchors pinning. This ensures correct orientation updates.

```swift
map.pinToSuperviewEdges()
```

> [!INFO]
> Map view can also be added through xib or storyboard. Simply add MTMapView as views class in interface builder.

### SwiftUI

You can add a map to a SwiftUI view using `MTMapViewContainer`. Open your view and follow the next steps.

On top of your view add import statement:

```swift
import MapTilerSDK
```

Declare variables for your preferred style:

```swift
@State private var referenceStyle: MTMapReferenceStyle = .streets
@State private var styleVariant: MTMapStyleVariant? = .defaultVariant
```

Initialize the map view and add it to your view:

```swift
@State private var map = MTMapView(options: MTMapOptions(zoom: 2.0))

var body: some View {
  MTMapViewContainer(map: map) {}
    .referenceStyle(referenceStyle)
    .styleVariant(styleVariant)
}
```

### MapView Delegate

Set your class as delegate for MTMapView and implement the delegate methods:

```swift
map.delegate = self
```

Following methods are available in the delegate:

- `mapViewDidInitialize(_ mapView: MTMapView)` - use to set style and other customizations
- `mapView(_ mapView: MTMapView, didTriggerEvent event: MTEvent, with data: MTData?)` - respond to map data and interaction events
- `mapView(_ mapView: MTMapView, didUpdateLocation location: CLLocation)` - optionally receive current device location

## Interaction

You can interact with the map by calling the methods on the MTMapView object.

### Zooming

```swift
map.zoomIn()
map.zoomOut()
```

### Navigating

```swift
let coordinates = CLLocationCoordinate2D(latitude: 47.137765, longitude: 8.581651)

map.flyTo(coordinates, options: nil, animationOptions: nil)
map.easeTo(coordinates, options: options, animationOptions: nil)
```

> [!INFO]
> You can use these the methods with completion handler or in async/await style. For more details and additional interaction methods refer to the [iOS SDK documentation](/mobile-sdk/ios/).

## POIs

To add a point of interest on the map, use [`MTMarker`](/mobile-sdk/ios/Classes/MTMarker/) class.

### UIKit

```swift
let coordinates = CLLocationCoordinate2D(latitude: 47.137765, longitude: 8.581651)
let marker = MTMarker(coordinates: coordinates)

map.addMarker(marker)
```

### SwiftUI

```swift
@State private var mapView = MTMapView(options: MTMapOptions(zoom: 2.0))

let coordinates = CLLocationCoordinate2D(latitude: 47.137765, longitude: 8.581651)

var body: some View {
  MTMapViewContainer(map: mapView) {
    MTMarker(coordinates: coordinates)
  }
}
```

> [!INFO]
> In addition to [MTMarker](/mobile-sdk/ios/Classes/MTMarker/), you can use [MTCustomAnnotationView](/mobile-sdk/ios/Classes/MTCustomAnnotationView/) and [MTSource](/mobile-sdk/ios/Protocols/MTSource/) and [MTLayer](/mobile-sdk/ios/Protocols/MTLayer/) classes.

## Location Tracking

Optionally, you can enable location tracking by calling:

```swift
map.initLocationTracking()
```

Once location is enabled, you can implement `mapView(_ mapView: MTMapView, didUpdateLocation location: CLLocation)` delegate method as you see fit.

> [!INFO]
> If you plan to use location tracking feature, make sure to update your info.plist file with necessary fields:
>
> *   Privacy - Location When In Use Usage Description and
> *   Privacy - Location Temporary Usage Description Dictionary

## Learn more

To learn about more advanced functionalities of the SDK, refer to the [API reference](/mobile-sdk/ios/), or build your own documentation in Xcode: Product -> Build Documentation.

In addition to the documentation take a look at the plug and play examples provided in the SDK GitHub repository, as well as pre-made demo app:

<p id="github-link" class="m-0 d-inline-block">
  <span>
  
  <a class="text-secondary mb-2" href="https://github.com/maptiler/maptiler-sdk-swift/tree/main/Examples" target="_blank"
  rel="noopener noreferrer"> maptiler/maptiler-sdk-swift/Examples</a>
  </span> 
</p>

<script defer>
  setTimeout(() => {
    $("#toc").empty();
    $("#toc").toc({headings: "h2,h3"});
  }, 300);
</script>
