# Source: https://docs.maptiler.com/mobile-sdk\ios\examples\custom-style\

# 

[MapTiler SDK iOS](/mobile-sdk/ios/) is a set of tools for creating and customizing maps on your mobile devices, using Swift language. In this guide you will learn how to add a custom map style, created in your MapTiler Cloud, to your mobile application in a few simple steps. If you haven’t already, read through our [Getting Started](/mobile-sdk/ios/examples/get-started/) guide to set up your project and initialize the map view.

<p align="center">
  
</p>

## Create your own map

If you haven’t already, follow the [How to make custom map design in MapTiler](/guides/map-design/how-to-make-custom-map-design-in-maptiler-cloud/) guide and create your own map. Once your map is ready, open it, scroll down to the Use Vector Style section and copy the style json url.

## Load your custom map

Getting your custom map style loaded can be done in only couple of steps.

1. Prepare you project and set up the map using our [Getting Started](/mobile-sdk/ios/examples/get-started/) guide.
1. Set the *referenceStyle* to *.custom* and use the style link you copied previously as a string, replacing `YOUR_CUSTOM_MAP_URL`:
    
#### UIKit

```swift
  if let url = URL(string: "YOUR_CUSTOM_MAP_URL") {
  let map = MTMapView(frame: view.frame, options: MTMapOptions(), referenceStyle: .custom(url))
}
```

#### SwiftUI

```swift
MTMapViewContainer(map: map) {}
  .referenceStyle(.custom(URL(string: "YOUR_CUSTOM_MAP_URL)))
```

And that is it! Your custom map is ready. Build and start your app.

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
