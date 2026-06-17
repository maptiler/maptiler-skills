# Source: https://docs.maptiler.com/sdk-js/examples/ar-control-qr/

# MapTiler AR Control

To enhance the user experience, it is possible to incorporate a QR code picture alongside the three-dimensional model. This will enable users to effortlessly access the augmented reality model on their mobile device or AR viewer.

The [Augmented reality (AR) control](/sdk-js/modules/ar/) adds a button on your map that enables the creation of a 3D representation of the current view, complete with 3D terrain and any additional layers you have applied. This functionality is compatible with **WebXR** or **Apple Quick Look**.

In this example, we employed the `qrcode-generator` library to produce the QR code. However, you have the flexibility to utilize your preferred approach for generating the QR code image.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
// Waiting for the map to be ready
      map.on("load", (e) => {
        const qrCodeOptions = isMobile ? {activateAR: true} : {
          logo: generateQRCode(),
          logoClass: "qr-code",
          activateAR: true
        }

        const arControl = new maptilerarcontrol.MaptilerARControl(qrCodeOptions);

        arControl.on("computeStart", (e) => {
          overlay.style.display = "inherit";

          if (!isMobile) {
            arControl.updateLogo(generateQRCode())
          }
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
    <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcode-generator/1.4.4/qrcode.min.js"></script>
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
                const qrCodeOptions = isMobile ? {activateAR: true} : {
                  logo: generateQRCode(),
                  logoClass: "qr-code",
                  activateAR: true
                }

                const arControl = new maptilerarcontrol.MaptilerARControl(qrCodeOptions);

                arControl.on("computeStart", (e) => {
                  overlay.style.display = "inherit";

                  if (!isMobile) {
                    arControl.updateLogo(generateQRCode())
                  }
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
