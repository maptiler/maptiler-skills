# Source: https://docs.maptiler.com/sdk-js/examples/3d-js-plane/

# Add a 3D model

Use the [MapTiler 3D JS module](/sdk-js/modules/3d/) to add a airplane model to the map. Thanks to the 3D JS module we can add 3D models to the map (flying) at the height above sea level that we want.

This demonstration showcases a compact control interface that allows us to modify various model parameters and observe their immediate impact on the model's behavior.

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


    const gui = new lil.GUI({ width: 200 });

    // Adding a mesh of a plane.

    const guiObj = {
      heading: 0,
      scale: 1,
      altitude: 3000,
      opacity: 1,
      wireframe: false,
      altitudeReference: "MEAN_SEA_LEVEL",
      removePlane: () => {
        layer3D.removeMesh(originalPlaneID);
      }
    }
  
    const originalPlaneID = "plane";
    const mesh = await layer3D.addMeshFromURL(
      originalPlaneID,
      "https://docs-media.maptiler.com/docs/models/plane_a340.glb",
      {
        scale: guiObj.scale,
        altitude: guiObj.altitude,
        altitudeReference: maptiler3d.AltitudeReference.MEAN_SEA_LEVEL,
        wireframe: guiObj.wireframe,
        lngLat: [7.22, 46.18]
      }
    );

    let planeCanMove = false;

    // Adding mesh of a plane
    map.on("mousemove", (e) => {
      if (!planeCanMove) return;
      mesh.modify({lngLat: e.lngLat})
    });

    map.on("click", (e) => {
      planeCanMove = !planeCanMove;
    });

    gui.add( guiObj, 'heading', 0, 360, 0.1 )
    .onChange((heading) => {
      mesh.modify({heading});
    });

    gui.add( guiObj, 'scale', 0.01, 5, 0.01 )
    .onChange((scale) => {
      mesh.modify({scale});
    });

    gui.add( guiObj, 'altitude', 0, 10000, 1 )
    .onChange((altitude) => {
      mesh.modify({altitude});
    });

    gui.add( guiObj, 'opacity', 0, 1)
    .onChange((opacity) => {
      mesh.modify({opacity});
    });

    gui.add( guiObj, 'altitudeReference', ["MEAN_SEA_LEVEL", "GROUND"])
    .onChange((altRef) => {
      mesh.modify({altitudeReference: maptiler3d.AltitudeReference[altRef]});
    });

    gui.add( guiObj, "wireframe" )
    .onChange((wireframe) => {
      mesh.modify({wireframe});
    });

    gui.add( guiObj, "removePlane" );

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
            style: maptilersdk.MapStyle.OUTDOOR.DARK,
            center: [7.22, 46.18],
            zoom: 11,
            pitch: 60
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


            const gui = new lil.GUI({ width: 200 });

            // Adding a mesh of a plane.

            const guiObj = {
              heading: 0,
              scale: 1,
              altitude: 3000,
              opacity: 1,
              wireframe: false,
              altitudeReference: "MEAN_SEA_LEVEL",
              removePlane: () => {
                layer3D.removeMesh(originalPlaneID);
              }
            }

            const originalPlaneID = "plane";
            const mesh = await layer3D.addMeshFromURL(
              originalPlaneID,
              "https://docs-media.maptiler.com/docs/models/plane_a340.glb",
              {
                scale: guiObj.scale,
                altitude: guiObj.altitude,
                altitudeReference: maptiler3d.AltitudeReference.MEAN_SEA_LEVEL,
                wireframe: guiObj.wireframe,
                lngLat: [7.22, 46.18]
              }
            );

            let planeCanMove = false;

            // Adding mesh of a plane
            map.on("mousemove", (e) => {
              if (!planeCanMove) return;
              mesh.modify({lngLat: e.lngLat})
            });

            map.on("click", (e) => {
              planeCanMove = !planeCanMove;
            });

            gui.add( guiObj, 'heading', 0, 360, 0.1 )
            .onChange((heading) => {
              mesh.modify({heading});
            });

            gui.add( guiObj, 'scale', 0.01, 5, 0.01 )
            .onChange((scale) => {
              mesh.modify({scale});
            });

            gui.add( guiObj, 'altitude', 0, 10000, 1 )
            .onChange((altitude) => {
              mesh.modify({altitude});
            });

            gui.add( guiObj, 'opacity', 0, 1)
            .onChange((opacity) => {
              mesh.modify({opacity});
            });

            gui.add( guiObj, 'altitudeReference', ["MEAN_SEA_LEVEL", "GROUND"])
            .onChange((altRef) => {
              mesh.modify({altitudeReference: maptiler3d.AltitudeReference[altRef]});
            });

            gui.add( guiObj, "wireframe" )
            .onChange((wireframe) => {
              mesh.modify({wireframe});
            });

            gui.add( guiObj, "removePlane" );

          })()
    </script>
</body>
</html>
```
