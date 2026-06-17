# Source: https://docs.maptiler.com/sdk-js/examples/ar-control-custom/

# MapTiler AR Control

Enhance the AR experience: The [Augmented reality (AR) control](/sdk-js/modules/ar/) accepts an option object to customize the look and feel. Compatible with both **WebXR** and **Apple Quick Look**.

Customize the AR control to deliver a personalized immersive experience. So why not give it a try and see the world from a different perspective?

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
// Waiting for the map to be ready
      map.on("load", (e) => {
        const arControl = new maptilerarcontrol.MaptilerARControl({
          background: `radial-gradient(circle, rgba(230,240,244,1) 1%, rgba(165,184,190,1) 73%, rgba(98,116,121,1) 100%)`,
          edgeColor: "#456992",
          arButtonContent: `<img src="/sdk-js/assets/box-icon.svg"/>`,
          closeButtonContent: `<img src="/sdk-js/assets/close-icon.svg"/>`,
          arButtonClassName: "maptiler-ar-enable-button",
          closeButtonClassName: "maptiler-ar-close-button",
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
            style: maptilersdk.MapStyle.STREETS.DARK,
            center: [-116.22335, 51.4117],
            zoom: 12
        });

        // Waiting for the map to be ready
              map.on("load", (e) => {
                const arControl = new maptilerarcontrol.MaptilerARControl({
                  background: `radial-gradient(circle, rgba(230,240,244,1) 1%, rgba(165,184,190,1) 73%, rgba(98,116,121,1) 100%)`,
                  edgeColor: "#456992",
                  arButtonContent: `<img src="/sdk-js/assets/box-icon.svg"/>`,
                  closeButtonContent: `<img src="/sdk-js/assets/close-icon.svg"/>`,
                  arButtonClassName: "maptiler-ar-enable-button",
                  closeButtonClassName: "maptiler-ar-close-button",
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
