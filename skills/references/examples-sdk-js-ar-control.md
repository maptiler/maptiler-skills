# Source: https://docs.maptiler.com/sdk-js/examples/ar-control/

# MapTiler AR Control

The [Augmented reality (AR) control](/sdk-js/modules/ar/) adds a button on your map that enables you to generate a 3D model of the visible area, including 3D terrain and any additional layer you have put on top. This functionality is compatible with **WebXR** or **Apple Quick Look**, providing users with seamless integration and immersive experiences.

With just a click of a button, you can unlock a whole new dimension to map exploration, allowing for enhanced visualization and interaction. Whether you're navigating unfamiliar terrain or simply curious about the world around you, AR maps offer a unique way to discover and engage with your surroundings.

The control's `activateAR` option allows you to automatically activate the AR model as soon as the data is available. Currently only on iOS (Quick Look).

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
// Waiting for the map to be ready
      map.on("load", (e) => {
        const arControl = new maptilerarcontrol.MaptilerARControl({
          activateAR: true //When the platform allows automatically activates the AR mode as soon as the data is ready
        });

        arControl.on("computeStart", (e) => {
          overlay.style.display = "inherit";
        })

        arControl.on("computeEnd", (e) => {
          overlay.style.display = "none";
        })

        map.addControl(arControl, "top-left");
      })
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>MapTiler AR Control</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <script src="https://cdn.maptiler.com/maptiler-ar-control/3.0.4/maptiler-ar-control.umd.min.js"></script>
    <style>
        body { margin: 0; padding: 0; }
        #map { position: absolute; top: 0; bottom: 0; width: 100%; }
    </style>
</head>
<body>
    <div id="map"></div>
    <script>
        maptilersdk.config.apiKey = 'YOUR_MAPTILER_API_KEY';

        const map = new maptilersdk.Map({
            container: 'map',
            style: maptilersdk.MapStyle.OUTDOOR,
            center: [-116.22335, 51.4117],
            zoom: 12
        });

        // Waiting for the map to be ready
              map.on("load", (e) => {
                const arControl = new maptilerarcontrol.MaptilerARControl({
                  activateAR: true //When the platform allows automatically activates the AR mode as soon as the data is ready
                });

                arControl.on("computeStart", (e) => {
                  overlay.style.display = "inherit";
                })

                arControl.on("computeEnd", (e) => {
                  overlay.style.display = "none";
                })

                map.addControl(arControl, "top-left");
              })
    </script>
</body>
</html>
```
