# Source: https://docs.maptiler.com/sdk-js/examples/3d-js-multi/

# Add a 3D model

Use the [MapTiler 3D JS module](/sdk-js/modules/3d/) to incorporate multiple 3D models into your map. The 3D JS module enables you to integrate multiple 3D objects onto the map surface. You can adjust model sizes, create duplicates, position models at specific elevations above sea level, and more. This offers complete flexibility in manipulating your 3D models.

This demonstration showcases a compact control interface that allows us to select diferents models and modify various model parameters and observe their immediate impact on the model's behavior.

<sup>To add a model to the map, select a model from the list in the control panel and then click on the map.</sup>

<p id="fn:1">

<ul class="mb-0">

<li><a href="https://skfb.ly/oJWGw">plane a340</a> by mamont nikita is licensed under <a href="https://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution</a></li>

<li><a href="https://github.com/KhronosGroup/glTF-Sample-Assets/tree/main">COLLADA duck</a> One texture Credit: © 2006, Sony. <a href="https://spdx.org/licenses/SCEA.html">SCEA Shared Source License, Version 1.0</a></li>

<li><a href="https://github.com/KhronosGroup/glTF-Sample-Assets/tree/main">Old wooden street light</a> © 2018, Frank Galligan. <a href="https://creativecommons.org/publicdomain/zero/1.0/legalcode">CC0 1.0 Universal</a></li>

<li><a href="https://skfb.ly/otyzN">Stanford Dragon PBR</a>  by hackmans is licensed under <a href="https://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution</a></li>

</ul>

&nbsp;<a href="#fnref:1" class="reversefootnote" role="doc-backlink">↩</a>

</p>

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
(async () => {
    await map.onReadyAsync();

    const layer3D = new maptiler3d.Layer3D("custom-3D-layer");
    map.addLayer(layer3D);

    // Increasing the intensity of the ambient light 
    layer3D.setAmbientLight({intensity: 2});

    // Adding a point light
    layer3D.addPointLight("point-light", {intensity: 30});

    const gui = new lil.GUI({ width: 200 });

    // Adding a mesh of a lantern.
    // We make this first mesh invisible because we will only use it to be cloned
    const originalLanternID = "lantern";
    await layer3D.addMeshFromURL(
      originalLanternID,
      "https://docs-media.maptiler.com/docs/models/lantern.glb",
      {
        scale: 1,
        visible: true,
        heading: 215,
        lngLat: [2.34090194106102, 48.856414043180365]
      }
    );

    const originalDuckID = "duck";
    await layer3D.addMeshFromURL(
      originalDuckID,
      "https://docs-media.maptiler.com/docs/models/duck.glb",
      {
        scale: 10,
        visible: true,
        heading: 155,
        lngLat: [2.341223806142807, 48.85620756643411]
      }
    );

    const originalPlaneID = "plane";
    await layer3D.addMeshFromURL(
      originalPlaneID,
      "https://docs-media.maptiler.com/docs/models/plane_a340.glb",
      {
        scale: 1,
        visible: false,
        altitude: 0,
        altitudeReference: maptiler3d.AltitudeReference.MEAN_SEA_LEVEL,
      }
    );

    const originalDragonID = "dragon";
    await layer3D.addMeshFromURL(
      originalDragonID,
      "https://docs-media.maptiler.com/docs/models/stanford_dragon_pbr.glb",
      {
        scale: 0.20,
        visible: true,
        heading: 215.7,
        lngLat: [2.340295761823654, 48.85677758136464]
      }
    );

    const guiObj = {
      model: originalLanternID,
      heading: 0,
      scale: 1,
      altitude: 0,
    }
    
    let meshCounter = 0;
    let latestMeshID = originalLanternID

    // Clones of this mesh will be added as we click on the map.
    // The lantern model that is used for the clone is the latest mesh added,
    // so that we can benefit from the latest heading we defined
    map.on("click", (e) => {
      meshCounter += 1;
      const newCloneID = `${originalLanternID}_${meshCounter}`;
      console.log(e.lngLat);
      layer3D.cloneMesh(guiObj.model, newCloneID, {lngLat: e.lngLat, visible: true, heading: guiObj.heading, scale: guiObj.scale})
      latestMeshID = newCloneID;
    })
    
    gui.add(guiObj, "model", [originalLanternID, originalDuckID, originalPlaneID, originalDragonID])

    // We can change the heading of the latest mesh added
    gui.add( guiObj, 'heading', 0, 360, 0.1 )
    .onChange((heading) => {
      const mesh = layer3D.getItem3D(latestMeshID);
      mesh.modify({heading});
    });

    gui.add( guiObj, 'scale', 0.01, 10, 0.01 )
    .onChange((scale) => {
      const mesh = layer3D.getItem3D(latestMeshID);
      mesh.modify({scale});
    })

    gui.add( guiObj, 'altitude', -100, 1000, 1 )
    .onChange((altitude) => {
      const mesh = layer3D.getItem3D(latestMeshID);
      mesh.modify({altitude});
    })

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
            style: maptilersdk.MapStyle.OUTDOOR,
            center: [2.340862, 48.8565787],
            zoom: 18,
            pitch: 60
        });

        (async () => {
            await map.onReadyAsync();

            const layer3D = new maptiler3d.Layer3D("custom-3D-layer");
            map.addLayer(layer3D);

            // Increasing the intensity of the ambient light 
            layer3D.setAmbientLight({intensity: 2});

            // Adding a point light
            layer3D.addPointLight("point-light", {intensity: 30});

            const gui = new lil.GUI({ width: 200 });

            // Adding a mesh of a lantern.
            // We make this first mesh invisible because we will only use it to be cloned
            const originalLanternID = "lantern";
            await layer3D.addMeshFromURL(
              originalLanternID,
              "https://docs-media.maptiler.com/docs/models/lantern.glb",
              {
                scale: 1,
                visible: true,
                heading: 215,
                lngLat: [2.34090194106102, 48.856414043180365]
              }
            );

            const originalDuckID = "duck";
            await layer3D.addMeshFromURL(
              originalDuckID,
              "https://docs-media.maptiler.com/docs/models/duck.glb",
              {
                scale: 10,
                visible: true,
                heading: 155,
                lngLat: [2.341223806142807, 48.85620756643411]
              }
            );

            const originalPlaneID = "plane";
            await layer3D.addMeshFromURL(
              originalPlaneID,
              "https://docs-media.maptiler.com/docs/models/plane_a340.glb",
              {
                scale: 1,
                visible: false,
                altitude: 0,
                altitudeReference: maptiler3d.AltitudeReference.MEAN_SEA_LEVEL,
              }
            );

            const originalDragonID = "dragon";
            await layer3D.addMeshFromURL(
              originalDragonID,
              "https://docs-media.maptiler.com/docs/models/stanford_dragon_pbr.glb",
              {
                scale: 0.20,
                visible: true,
                heading: 215.7,
                lngLat: [2.340295761823654, 48.85677758136464]
              }
            );

            const guiObj = {
              model: originalLanternID,
              heading: 0,
              scale: 1,
              altitude: 0,
            }

            let meshCounter = 0;
            let latestMeshID = originalLanternID

            // Clones of this mesh will be added as we click on the map.
            // The lantern model that is used for the clone is the latest mesh added,
            // so that we can benefit from the latest heading we defined
            map.on("click", (e) => {
              meshCounter += 1;
              const newCloneID = `${originalLanternID}_${meshCounter}`;
              console.log(e.lngLat);
              layer3D.cloneMesh(guiObj.model, newCloneID, {lngLat: e.lngLat, visible: true, heading: guiObj.heading, scale: guiObj.scale})
              latestMeshID = newCloneID;
            })

            gui.add(guiObj, "model", [originalLanternID, originalDuckID, originalPlaneID, originalDragonID])

            // We can change the heading of the latest mesh added
            gui.add( guiObj, 'heading', 0, 360, 0.1 )
            .onChange((heading) => {
              const mesh = layer3D.getItem3D(latestMeshID);
              mesh.modify({heading});
            });

            gui.add( guiObj, 'scale', 0.01, 10, 0.01 )
            .onChange((scale) => {
              const mesh = layer3D.getItem3D(latestMeshID);
              mesh.modify({scale});
            })

            gui.add( guiObj, 'altitude', -100, 1000, 1 )
            .onChange((altitude) => {
              const mesh = layer3D.getItem3D(latestMeshID);
              mesh.modify({altitude});
            })

          })()
    </script>
</body>
</html>
```
