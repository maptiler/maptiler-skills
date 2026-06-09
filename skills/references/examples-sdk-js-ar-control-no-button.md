# Source: https://docs.maptiler.com/sdk-js/examples/ar-control-no-button/

# MapTiler AR Control

Learn how to activate functions in the [Augmented reality (AR) control](/sdk-js/modules/ar/) by utilizing the keyboard. This method will enable you to generate a three-dimensional viewport model through augmented reality (AR), which includes not only a 3D terrain but also any additional layers you have incorporated. This feature is compatible with both **WebXR** and **Apple Quick Look** platforms.

<script>

document.addEventListener('keypress', async (event) => {

if (event.key === "a") {

document.getElementById('demo-ifr').contentWindow.postMessage({key: event.key, type: event.type});

}

if (event.key === "q") {

try{

document.getElementById('demo-ifr').contentWindow.postMessage({key: event.key, type: event.type});

} catch(e) {}

}

}, false);

document.getElementById('demo-ifr').focus();

</script>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
// Waiting for the map to be ready
      map.on("load", (e) => {
        const arControl = new maptilerarcontrol.MaptilerARControl({
          showButton: false,
        });

        document.addEventListener('keypress', async (event) => {
          console.log(event.key);

          if (event.key === "a") {
            await arControl.run()
          }

          if (event.key === "q") {
            try{
              await arControl.close();
            } catch(e) {}
          }

        }, false);

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
            style: maptilersdk.MapStyle.SATELLITE,
            center: [-116.22335, 51.4117],
            zoom: 12
        });

        // Waiting for the map to be ready
              map.on("load", (e) => {
                const arControl = new maptilerarcontrol.MaptilerARControl({
                  showButton: false,
                });

                document.addEventListener('keypress', async (event) => {
                  console.log(event.key);

                  if (event.key === "a") {
                    await arControl.run()
                  }

                  if (event.key === "q") {
                    try{
                      await arControl.close();
                    } catch(e) {}
                  }

                }, false);

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
