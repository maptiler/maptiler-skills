# Source: https://docs.maptiler.com/sdk-js/examples/3d-js-pitch/

# Add a 3D model

Use the [MapTiler 3D JS module](/sdk-js/modules/3d/) to rotate a 3D model, setting the pitch property. Set the model's tilt (pitch) in degrees, either positive or negative. Thanks to the 3D JS module we can add 3D models to the map and configure it as we want, rotating it, animating it, scaling it, etc.

<p id="fn:1"><a href="https://skfb.ly/oG9qS">Low-Poly Biplane</a> by ElectrikGoat0395 is licensed under <a href="https://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution</a>&nbsp;<a href="#fnref:1" class="reversefootnote" role="doc-backlink">↩</a></p>

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
(async () => {
    await map.onReadyAsync();

    const layer3D = new maptiler3d.Layer3D("custom-3D-layer");
    map.addLayer(layer3D);

    const LNGLAT_OFFSET = 0.25;
    const PLANE_BASE_ALT = 2200;

    // Adding a point light
    layer3D.addPointLight("point-light", {
      intensity: 20,
      color: "#ffffff",
      lngLat: center.map(num => num + 0.0001),
      altitude: 2000,
      altitudeReference: maptiler3d.AltitudeReference.GROUND,
    });

    // Adding a mesh of a plane. 
    const originalPlaneID = "biplaneOne";
    const biplaneOne = await layer3D.addMeshFromURL(
      originalPlaneID,
      "https://docs-media.maptiler.com/docs/models/low_poly_biplane.glb",
      {
        lngLat: center,
        heading: 0,
        scale: 300,
        altitude: PLANE_BASE_ALT,
        altitudeReference: maptiler3d.AltitudeReference.GROUND,
        transform: {
          rotation: {
            y: Math.PI / 2,
          },
        }
      }
    );

    layer3D.cloneMesh("biplaneOne", "biplaneTwo");
    layer3D.cloneMesh("biplaneOne", "biplaneThree");
    layer3D.cloneMesh("biplaneOne", "biplaneFour");
    layer3D.cloneMesh("biplaneOne", "biplaneFive");
    const biplaneTwo = layer3D.getItem3D("biplaneTwo");
    biplaneTwo.setLngLat([center[0]+0.05, center[1]]);
    biplaneTwo.setPitch(45);
    const biplaneThree = layer3D.getItem3D("biplaneThree");
    biplaneThree.setLngLat([center[0]+(0.05*2), center[1]]);
    biplaneThree.setPitch(120);
    const biplaneFour = layer3D.getItem3D("biplaneFour");
    biplaneFour.setLngLat([center[0]+(0.05*3), center[1]]);
    biplaneFour.setPitch(-45);
    const biplaneFive = layer3D.getItem3D("biplaneFive");
    biplaneFive.setLngLat([center[0]+(0.05*4), center[1]]);
    biplaneFive.setPitch(-90);

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
            style: maptilersdk.MapStyle.DATAVIZ.LIGHT,
            center: [2.4444, 48.8785],
            zoom: 11,
            pitch: 65,
            bearing: 44
        });

        (async () => {
            await map.onReadyAsync();

            const layer3D = new maptiler3d.Layer3D("custom-3D-layer");
            map.addLayer(layer3D);

            const LNGLAT_OFFSET = 0.25;
            const PLANE_BASE_ALT = 2200;

            // Adding a point light
            layer3D.addPointLight("point-light", {
              intensity: 20,
              color: "#ffffff",
              lngLat: center.map(num => num + 0.0001),
              altitude: 2000,
              altitudeReference: maptiler3d.AltitudeReference.GROUND,
            });

            // Adding a mesh of a plane. 
            const originalPlaneID = "biplaneOne";
            const biplaneOne = await layer3D.addMeshFromURL(
              originalPlaneID,
              "https://docs-media.maptiler.com/docs/models/low_poly_biplane.glb",
              {
                lngLat: center,
                heading: 0,
                scale: 300,
                altitude: PLANE_BASE_ALT,
                altitudeReference: maptiler3d.AltitudeReference.GROUND,
                transform: {
                  rotation: {
                    y: Math.PI / 2,
                  },
                }
              }
            );

            layer3D.cloneMesh("biplaneOne", "biplaneTwo");
            layer3D.cloneMesh("biplaneOne", "biplaneThree");
            layer3D.cloneMesh("biplaneOne", "biplaneFour");
            layer3D.cloneMesh("biplaneOne", "biplaneFive");
            const biplaneTwo = layer3D.getItem3D("biplaneTwo");
            biplaneTwo.setLngLat([center[0]+0.05, center[1]]);
            biplaneTwo.setPitch(45);
            const biplaneThree = layer3D.getItem3D("biplaneThree");
            biplaneThree.setLngLat([center[0]+(0.05*2), center[1]]);
            biplaneThree.setPitch(120);
            const biplaneFour = layer3D.getItem3D("biplaneFour");
            biplaneFour.setLngLat([center[0]+(0.05*3), center[1]]);
            biplaneFour.setPitch(-45);
            const biplaneFive = layer3D.getItem3D("biplaneFive");
            biplaneFive.setLngLat([center[0]+(0.05*4), center[1]]);
            biplaneFive.setPitch(-90);

          })()
    </script>
</body>
</html>
```
