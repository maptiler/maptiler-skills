# Source: https://docs.maptiler.com/sdk-js/examples/3d-js-point-cad/

# Add a 3D model

Use the [MapTiler 3D JS module](/sdk-js/modules/3d/) to display the wireframe of a building 3D model based on point cloud data on a map. Thanks to the 3D JS module we can view the model wireframe or the solid model.

This demonstration show a compact control interface that allows to modify diferent model parameters and observe their immediate impact on the model's behavior.

<p id="fn:1"><a href="https://skfb.ly/oCRuD">Building F, AGU Sagamihara Campus (LOD2-3)</a> by ibukilego is licensed under <a href="https://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution</a>&nbsp;<a href="#fnref:1" class="reversefootnote" role="doc-backlink">↩</a></p>

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

    const layer3D = new maptiler3d.Layer3D("custom-3D-layer", {antiaslias: true});
    map.addLayer(layer3D);

    // Increasing the intensity of the ambient light 
    layer3D.setAmbientLight({intensity: 2});

    // Adding a point light
    layer3D.addPointLight("point-light-1", {intensity: 30, lngLat: [40, 0], color: 0xdbf8ff, altitude: 1_000_000});
    layer3D.addPointLight("point-light-2", {intensity: 30, lngLat: [-120, 80], color: 0xfff7db});

    const gui = new lil.GUI({ width: 200 });

    const guiObj = {
      heading: 320.5,
      scale: 1,
      altitude: 0.16,
      altitudeReference: "GROUND",
      opacity: 1,
      wireframe: true,
      fov: map.transform.fov,
    }

    const meshId = "some-mesh";
    const mesh = await layer3D.addMeshFromURL(
      meshId,
      "https://docs-media.maptiler.com/docs/models/building_f_agu_sagamihara_campus_lod2-3.glb",
      {
        lngLat: [139.401378125492, 35.567323827763786],
        heading: guiObj.heading,
        scale: guiObj.scale,
        visible: true,
        altitude: guiObj.altitude,
        altitudeReference: maptiler3d.AltitudeReference.GROUND,
        wireframe: guiObj.wireframe,
      }
    );

    gui.add( guiObj, 'heading', 0, 360, 0.1 )
    .onChange((heading) => {
      mesh.modify({heading});
    });

    gui.add( guiObj, 'scale', 0.01, 5, 0.01 )
    .onChange((scale) => {
      mesh.modify({scale});
    });

    gui.add( guiObj, 'altitude', -100, 100, 0.01 )
    .onChange((altitude) => {
      mesh.modify({altitude});
    });

    gui.add( guiObj, 'opacity', 0, 1)
    .onChange((opacity) => {
      mesh.modify({opacity});
    });

    gui.add( guiObj, 'altitudeReference', ["GROUND", "MEAN_SEA_LEVEL"])
    .onChange((altRef) => {
      mesh.modify({altitudeReference: maptiler3d.AltitudeReference[altRef]});
    });

    gui.add( guiObj, 'wireframe')
    .onChange((wireframe) => {
      mesh.modify({wireframe});
    });

    gui.add( guiObj, 'fov', 0, 60)
    .onChange((fov) => {
      map.transform.fov = fov;
      map.triggerRepaint();
    });

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
            style: maptilersdk.MapStyle.DATAVIZ.DARK,
            center: [139.401378125492, 35.567323827763786],
            zoom: 18,
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

            const layer3D = new maptiler3d.Layer3D("custom-3D-layer", {antiaslias: true});
            map.addLayer(layer3D);

            // Increasing the intensity of the ambient light 
            layer3D.setAmbientLight({intensity: 2});

            // Adding a point light
            layer3D.addPointLight("point-light-1", {intensity: 30, lngLat: [40, 0], color: 0xdbf8ff, altitude: 1_000_000});
            layer3D.addPointLight("point-light-2", {intensity: 30, lngLat: [-120, 80], color: 0xfff7db});

            const gui = new lil.GUI({ width: 200 });

            const guiObj = {
              heading: 320.5,
              scale: 1,
              altitude: 0.16,
              altitudeReference: "GROUND",
              opacity: 1,
              wireframe: true,
              fov: map.transform.fov,
            }

            const meshId = "some-mesh";
            const mesh = await layer3D.addMeshFromURL(
              meshId,
              "https://docs-media.maptiler.com/docs/models/building_f_agu_sagamihara_campus_lod2-3.glb",
              {
                lngLat: [139.401378125492, 35.567323827763786],
                heading: guiObj.heading,
                scale: guiObj.scale,
                visible: true,
                altitude: guiObj.altitude,
                altitudeReference: maptiler3d.AltitudeReference.GROUND,
                wireframe: guiObj.wireframe,
              }
            );

            gui.add( guiObj, 'heading', 0, 360, 0.1 )
            .onChange((heading) => {
              mesh.modify({heading});
            });

            gui.add( guiObj, 'scale', 0.01, 5, 0.01 )
            .onChange((scale) => {
              mesh.modify({scale});
            });

            gui.add( guiObj, 'altitude', -100, 100, 0.01 )
            .onChange((altitude) => {
              mesh.modify({altitude});
            });

            gui.add( guiObj, 'opacity', 0, 1)
            .onChange((opacity) => {
              mesh.modify({opacity});
            });

            gui.add( guiObj, 'altitudeReference', ["GROUND", "MEAN_SEA_LEVEL"])
            .onChange((altRef) => {
              mesh.modify({altitudeReference: maptiler3d.AltitudeReference[altRef]});
            });

            gui.add( guiObj, 'wireframe')
            .onChange((wireframe) => {
              mesh.modify({wireframe});
            });

            gui.add( guiObj, 'fov', 0, 60)
            .onChange((fov) => {
              map.transform.fov = fov;
              map.triggerRepaint();
            });

          })()
    </script>
</body>
</html>
```
