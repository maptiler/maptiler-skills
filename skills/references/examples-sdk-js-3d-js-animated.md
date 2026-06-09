# Source: https://docs.maptiler.com/sdk-js/examples/3d-js-animated/

# Add an animated 3D model

With animation, your 3D models take on a whole new dimension. You can bring them to life and display them on a map. If your 3D model has animations you can play these animations with the 3D JS module of the MapTiler SDK.

This demonstration showcases how to add a animated 3D model in a map.

<p id="fn:1">

Model by <a href='https://mirada.com/' target='_blank'>Mirada</a> for <a href='https://experiments.withgoogle.com/3-dreams-of-black' target='_blank'>3 Dreams of Black</a>&nbsp;<a href="#fnref:1" class="reversefootnote" role="doc-backlink">↩</a></p>

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
// Waiting for the map to be ready
  map.on('ready', async () => {
    // Create a Layer3D and add it
    const layer3D = new maptiler3d.Layer3D("custom-3D-layer");
    map.addLayer(layer3D);

      // Increasing the intensity of the ambient light
    layer3D.setAmbientLight({ intensity: 2 });

    // Adding a point light
    layer3D.addPointLight("point-light", { intensity: 30 });

    // The call can be awaited for the whole download of the mesh to complete
    await layer3D.addMeshFromURL(
      // ID to give to this mesh, unique within this Layer3D instance
      "flamingo",

      // The URL of the mesh
      "https://docs-media.maptiler.com/docs/models/flamingo.glb",

      // A set of options, these can be modified later
      {
        lngLat: [-3.0615632, 56.4547039],
        heading: 150,
        scale: 10,
        animationMode: "continuous",
      }
    );

    const mesh = layer3D.getItem3D("flamingo");

    const animationNames = mesh?.getAnimationNames();

    const animationName = animationNames?.[0];

    if (!animationName) {
      throw new Error(`No animation found with name '${animationName}'`);
    }

    mesh?.playAnimation(
      animationName,
      "loop",
    );
  });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Add an animated 3D model</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
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
            center: [-3.0615632, 56.4547039],
            zoom: 13,
            pitch: 60,
            bearing: 90.1
        });

        // Waiting for the map to be ready
          map.on('ready', async () => {
            // Create a Layer3D and add it
            const layer3D = new maptiler3d.Layer3D("custom-3D-layer");
            map.addLayer(layer3D);

              // Increasing the intensity of the ambient light
            layer3D.setAmbientLight({ intensity: 2 });

            // Adding a point light
            layer3D.addPointLight("point-light", { intensity: 30 });

            // The call can be awaited for the whole download of the mesh to complete
            await layer3D.addMeshFromURL(
              // ID to give to this mesh, unique within this Layer3D instance
              "flamingo",

              // The URL of the mesh
              "https://docs-media.maptiler.com/docs/models/flamingo.glb",

              // A set of options, these can be modified later
              {
                lngLat: [-3.0615632, 56.4547039],
                heading: 150,
                scale: 10,
                animationMode: "continuous",
              }
            );

            const mesh = layer3D.getItem3D("flamingo");

            const animationNames = mesh?.getAnimationNames();

            const animationName = animationNames?.[0];

            if (!animationName) {
              throw new Error(`No animation found with name '${animationName}'`);
            }

            mesh?.playAnimation(
              animationName,
              "loop",
            );
          });
    </script>
</body>
</html>
```
