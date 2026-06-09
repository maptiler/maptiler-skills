# Source: https://docs.maptiler.com/sdk-js/examples/3d-js-point-cloud-nmh/

# Add a 3D model

Use the [MapTiler 3D JS module](/sdk-js/modules/3d/) to display a point cloud 3D building model on a map. Thanks to the 3D JS module we can view the cloud point model and navigate inside the building.

This demonstration show a compact control interface that allows to modify diferent model parameters and observe their immediate impact on the model's behavior.

<p id="fn:1"><a href="https://skfb.ly/6sXWG">Hintze Hall, NHM London [point cloud]</a> by Thomas Flynn is licensed under <a href="https://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution</a>&nbsp;<a href="#fnref:1" class="reversefootnote" role="doc-backlink">↩</a></p>

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
(async () => {
    await map.onReadyAsync();

    map.setSky({
      "sky-color": "#b2ddfa",
      "horizon-color": "#FFFFFF",
      "fog-color": "#FFFFFF",
      "fog-ground-blend": 0.8,
      "horizon-fog-blend": 0.1,
      "sky-horizon-blend": 0.6,
      "atmosphere-blend": 0.5,
    })

    const layer3D = new maptiler3d.Layer3D("custom-3D-layer");
    map.addLayer(layer3D);

    // Increasing the intensity of the ambient light 
    layer3D.setAmbientLight({intensity: 2});

    // Adding a point light
    layer3D.addPointLight("point-light", {intensity: 30});

    const gui = new lil.GUI({ width: 200 });

    const meshId = "some-mesh";
    const mesh = await layer3D.addMeshFromURL(
      meshId,
      "https://docs-media.maptiler.com/docs/models/hintze_hall_nhm_london_point_cloud.glb",
      {
        lngLat: [-0.17642900347709656, 51.496198574865645],
        heading: 83.6,
        scale: 1,
        visible: true,
        altitude: 0,
        altitudeReference: maptiler3d.AltitudeReference.GROUND,
      }
    );

    const guiObj = {
      opacity: 1,
      pointSize: 1,
      fov: map.transform.fov,
    }

    gui.add( guiObj, 'opacity', 0, 1)
    .onChange((opacity) => {
      mesh.modify({opacity});
    });

    gui.add( guiObj, 'pointSize', 0, 20, 0.1 )
    .onChange((pointSize) => {
      mesh.modify({pointSize});
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
            style: maptilersdk.MapStyle.DATAVIZ,
            center: [-0.1765222, 51.4963662],
            zoom: 19.6,
            pitch: 63,
            bearing: -24.8
        });

        (async () => {
            await map.onReadyAsync();

            map.setSky({
              "sky-color": "#b2ddfa",
              "horizon-color": "#FFFFFF",
              "fog-color": "#FFFFFF",
              "fog-ground-blend": 0.8,
              "horizon-fog-blend": 0.1,
              "sky-horizon-blend": 0.6,
              "atmosphere-blend": 0.5,
            })

            const layer3D = new maptiler3d.Layer3D("custom-3D-layer");
            map.addLayer(layer3D);

            // Increasing the intensity of the ambient light 
            layer3D.setAmbientLight({intensity: 2});

            // Adding a point light
            layer3D.addPointLight("point-light", {intensity: 30});

            const gui = new lil.GUI({ width: 200 });

            const meshId = "some-mesh";
            const mesh = await layer3D.addMeshFromURL(
              meshId,
              "https://docs-media.maptiler.com/docs/models/hintze_hall_nhm_london_point_cloud.glb",
              {
                lngLat: [-0.17642900347709656, 51.496198574865645],
                heading: 83.6,
                scale: 1,
                visible: true,
                altitude: 0,
                altitudeReference: maptiler3d.AltitudeReference.GROUND,
              }
            );

            const guiObj = {
              opacity: 1,
              pointSize: 1,
              fov: map.transform.fov,
            }

            gui.add( guiObj, 'opacity', 0, 1)
            .onChange((opacity) => {
              mesh.modify({opacity});
            });

            gui.add( guiObj, 'pointSize', 0, 20, 0.1 )
            .onChange((pointSize) => {
              mesh.modify({pointSize});
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
