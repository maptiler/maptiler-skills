# Source: https://docs.maptiler.com/sdk-js/examples/3d-js-flight/

# Add a 3D model

Use the [MapTiler 3D JS module](/sdk-js/modules/3d/) to simulate and animate a plane flight between two cities. Thanks to the 3D JS module we can track the flight position of a airplane.

This demonstration showcases a compact control interface that allows us to animate the plane flight and track the position.

<p id="fn:1"><a href="https://skfb.ly/oJWGw">plane a340</a> by mamont nikita is licensed under <a href="https://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution</a>&nbsp;<a href="#fnref:1" class="reversefootnote" role="doc-backlink">↩</a></p>

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
(async () => {
    await map.onReadyAsync();

    map.setSky({
      "sky-color": "#0C2E4B",
      "horizon-color": "#09112F",
      "fog-color": "#09112F",
      "fog-ground-blend": 0.5,
      "horizon-fog-blend": 0.1,
      "sky-horizon-blend": 1.0,
      "atmosphere-blend": 0.5,
    })

    const layer3D = new maptiler3d.Layer3D("custom-3D-layer");
    map.addLayer(layer3D);

    // Increasing the intensity of the ambient light 
    layer3D.setAmbientLight({intensity: 2});

    // Adding a point light
    layer3D.addPointLight("point-light", {intensity: 30});

    // Adding a mesh of a plane.
    const originalPlaneID = "plane";
    const mesh = await layer3D.addMeshFromURL(
      originalPlaneID,
      "https://docs-media.maptiler.com/docs/models/plane_a340.glb",
      {
        lngLat: paris,
        heading: 12,
        scale: 5,
        altitude: 5000,
        altitudeReference: maptiler3d.AltitudeReference.MEAN_SEA_LEVEL,
      }
    );

    const guiObj = {
      play: false,
      trackFlight: true,
      speed: 0.0001,
    }
  
    const gui = new lil.GUI({ width: 200 });

    gui.add( guiObj, 'trackFlight')

    gui.add( guiObj, 'play')
    .onChange((play) => {
      if (play) {
        playAnimation();
      }
    });

    gui.add( guiObj, 'speed', 0, 0.001);
    
    let progress = 0;

    function playAnimation() {
      progress += guiObj.speed;

      if (progress > 1) {
        progress = 0;
      }

      const position = maptilersdk.math.haversineIntermediateWgs84(paris, ankara, progress);
      mesh.modify({lngLat: position});

      if (guiObj.trackFlight) {
        map.setCenter(position);
        // map.setBearing(360 * progress * 2);
      }

      if (guiObj.play) {
        requestAnimationFrame(playAnimation);
      }
    }

  })()
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Add a 3D model</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <script src="https://cdn.jsdelivr.net/npm/lil-gui@0.19"></script>
    <script src="https://cdn.maptiler.com/maptiler-3d/4.0.1/maptiler-3d.umd.min.js"></script>
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
            center: [0, 0],
            zoom: 9
        });

        (async () => {
            await map.onReadyAsync();

            map.setSky({
              "sky-color": "#0C2E4B",
              "horizon-color": "#09112F",
              "fog-color": "#09112F",
              "fog-ground-blend": 0.5,
              "horizon-fog-blend": 0.1,
              "sky-horizon-blend": 1.0,
              "atmosphere-blend": 0.5,
            })

            const layer3D = new maptiler3d.Layer3D("custom-3D-layer");
            map.addLayer(layer3D);

            // Increasing the intensity of the ambient light 
            layer3D.setAmbientLight({intensity: 2});

            // Adding a point light
            layer3D.addPointLight("point-light", {intensity: 30});

            // Adding a mesh of a plane.
            const originalPlaneID = "plane";
            const mesh = await layer3D.addMeshFromURL(
              originalPlaneID,
              "https://docs-media.maptiler.com/docs/models/plane_a340.glb",
              {
                lngLat: paris,
                heading: 12,
                scale: 5,
                altitude: 5000,
                altitudeReference: maptiler3d.AltitudeReference.MEAN_SEA_LEVEL,
              }
            );

            const guiObj = {
              play: false,
              trackFlight: true,
              speed: 0.0001,
            }

            const gui = new lil.GUI({ width: 200 });

            gui.add( guiObj, 'trackFlight')

            gui.add( guiObj, 'play')
            .onChange((play) => {
              if (play) {
                playAnimation();
              }
            });

            gui.add( guiObj, 'speed', 0, 0.001);

            let progress = 0;

            function playAnimation() {
              progress += guiObj.speed;

              if (progress > 1) {
                progress = 0;
              }

              const position = maptilersdk.math.haversineIntermediateWgs84(paris, ankara, progress);
              mesh.modify({lngLat: position});

              if (guiObj.trackFlight) {
                map.setCenter(position);
                // map.setBearing(360 * progress * 2);
              }

              if (guiObj.play) {
                requestAnimationFrame(playAnimation);
              }
            }

          })()
    </script>
</body>
</html>
```
