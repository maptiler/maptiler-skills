# Source: https://docs.maptiler.com/sdk-js/examples/3d-js-point-cloud-lidar/

# Add a 3D model

Utilize the [MapTiler 3D JS module](/sdk-js/modules/3d/) to render LIDAR-based 3D urban visualizations on maps. The 3D JS module enables exploration of LIDAR point cloud data and detailed model examination. Users can view existing city structures and visualize proposed urban development concepts through interactive modeling.

This demonstration showcases a small control interface that allows to adjust various model parameters and instantly see their effects on the model's behavior.

<p id="fn:1"><a href="https://skfb.ly/o8qrG">Parque Copan (design proposal)</a> by Philipp Urech (Topostudio) is licensed under <a href="https://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution</a>&nbsp;<a href="#fnref:1" class="reversefootnote" role="doc-backlink">↩</a></p>

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
      "https://docs-media.maptiler.com/docs/models/parque_copan_design_proposal.glb",
      {
        lngLat: [-74.0839886924465, 40.5804232016599],
        scale: 1,
        visible: true,
        altitude: -752,
        altitudeReference: maptiler3d.AltitudeReference.GROUND,
      }
    );

    const guiObj = {
      opacity: 1,
      pointSize: 1,
    }

    gui.add( guiObj, 'opacity', 0, 1)
    .onChange((opacity) => {
      mesh.modify({opacity});
    });

    gui.add( guiObj, 'pointSize', 0, 20, 0.1 )
    .onChange((pointSize) => {
      mesh.modify({pointSize});
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
            style: maptilersdk.MapStyle.STREETS,
            center: [-74.076273, 40.58592],
            zoom: 15.5,
            pitch: 60
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
              "https://docs-media.maptiler.com/docs/models/parque_copan_design_proposal.glb",
              {
                lngLat: [-74.0839886924465, 40.5804232016599],
                scale: 1,
                visible: true,
                altitude: -752,
                altitudeReference: maptiler3d.AltitudeReference.GROUND,
              }
            );

            const guiObj = {
              opacity: 1,
              pointSize: 1,
            }

            gui.add( guiObj, 'opacity', 0, 1)
            .onChange((opacity) => {
              mesh.modify({opacity});
            });

            gui.add( guiObj, 'pointSize', 0, 20, 0.1 )
            .onChange((pointSize) => {
              mesh.modify({pointSize});
            });

          })()
    </script>
</body>
</html>
```
