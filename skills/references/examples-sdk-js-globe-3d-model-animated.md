# Source: https://docs.maptiler.com/sdk-js/examples/globe-3d-model-animated/

# Add a 3D model

This example shows how to simulate and animate a airplane flight in a globe using [MapTiler 3D JS module](/sdk-js/modules/3d/). Thanks to the 3D JS module we can track the flight position of a 3D model.

This demonstration showcases a compact control interface that allows us to animate the plane flight and track the position.

<p id="fn:1"><a href="https://skfb.ly/oJWGw">plane a340</a> by mamont nikita is licensed under <a href="https://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution</a>&nbsp;<a href="#fnref:1" class="reversefootnote" role="doc-backlink">↩</a></p>

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const paris = [2.3120283730734648, 48.8556923989924];
      const sydney = [151.174622,-33.940619];

        container: 'map', // container's id or the HTML element to render the map
        style: maptilersdk.MapStyle.STREETS.DARK,
        zoom: 2,
        center: paris,
        maptilerLogo: true,
        maxPitch: 85,
        pitch: 71,
        hash: false,
        projection: 'globe' //enable globe projection
      });

      (async () => {
    await map.onReadyAsync();

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
        heading: 45,
        scale: 1000,
        altitude: 0,
        altitudeReference: maptiler3d.AltitudeReference.MEAN_SEA_LEVEL,
      }
    );

    const guiObj = {
      play: false,
      trackFlight: true,
      speed: 0.0005,
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

      const position = maptilersdk.math.haversineIntermediateWgs84(paris, sydney, progress);
      if (progress < 0.2) { //taking off
        mesh.modify({lngLat: position, altitude: progress*5000000});
      } else if (progress > 0.8) { //landing
        mesh.modify({lngLat: position, altitude: 1000000 - ((progress - 0.80) * 5000000)});
      } else {
        mesh.modify({lngLat: position, altitude: 1000000});
      }
      
      if (guiObj.trackFlight) {
        map.flyTo({
          center: position,
          pitch: 71,
        });
      }

      if (guiObj.play) {
        requestAnimationFrame(playAnimation);
      }
    }

  })();
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
            zoom: 2,
            pitch: 71
        });

        const paris = [2.3120283730734648, 48.8556923989924];
              const sydney = [151.174622,-33.940619];

                container: 'map', // container's id or the HTML element to render the map
                style: maptilersdk.MapStyle.STREETS.DARK,
                zoom: 2,
                center: paris,
                maptilerLogo: true,
                maxPitch: 85,
                pitch: 71,
                hash: false,
                projection: 'globe' //enable globe projection
              });

              (async () => {
            await map.onReadyAsync();

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
                heading: 45,
                scale: 1000,
                altitude: 0,
                altitudeReference: maptiler3d.AltitudeReference.MEAN_SEA_LEVEL,
              }
            );

            const guiObj = {
              play: false,
              trackFlight: true,
              speed: 0.0005,
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

              const position = maptilersdk.math.haversineIntermediateWgs84(paris, sydney, progress);
              if (progress < 0.2) { //taking off
                mesh.modify({lngLat: position, altitude: progress*5000000});
              } else if (progress > 0.8) { //landing
                mesh.modify({lngLat: position, altitude: 1000000 - ((progress - 0.80) * 5000000)});
              } else {
                mesh.modify({lngLat: position, altitude: 1000000});
              }

              if (guiObj.trackFlight) {
                map.flyTo({
                  center: position,
                  pitch: 71,
                });
              }

              if (guiObj.play) {
                requestAnimationFrame(playAnimation);
              }
            }

          })();
    </script>
</body>
</html>
```
