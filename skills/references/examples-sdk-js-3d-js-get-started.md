# Source: https://docs.maptiler.com/sdk-js/examples/3d-js-get-started/

# MapTiler AR Control

Use the MapTiler SDK 3D JS module to add 3D objects to your map from glTF/glb files! These can be meshes, groups of meshes, point clouds, or a mix of all these.

<div class="tab-common-content" markdown="1">

1. Once created and added, a mesh can be added. In this version any glTF and their binary counterpart glb files can be added. Add a mesh to the layer. In this example we will use the model [The COLLADA duck. One texture. Credit: © 2006, Sony. SCEA Shared Source License, Version 1.0](https://github.com/KhronosGroup/glTF-Sample-Assets/tree/main)

<pre class="line-numbers" data-start="30" data-line-offset="29" data-line="30-62"><code class="language-js"><!--

// The call can be awaited for the whole download of the mesh to complete

await layer3D.addMeshFromURL(

// ID to give to this mesh, unique within this Layer3D instance

"duck",

// The URL of the mesh

"https://docs-media.maptiler.com/docs/models/duck.glb",

// A set of options, these can be modified later

{

lngLat: [-3.0615632, 56.4547039],

heading: 150,

scale: 10

}

);

layer3D.cloneMesh("duck", "duck-baby", {

lngLat: [-3.0617744, 56.4545475],

heading: 45,

scale: 3,

});

layer3D.cloneMesh("duck", "duck-baby-1", {

lngLat: [-3.0613331, 56.4546995],

heading: 180,

scale: 4,

});

layer3D.cloneMesh("duck", "duck-baby-2", {

lngLat: [-3.0611772, 56.4546843],

heading: 190,

scale: 3,

});

--></code></pre>

</div>

<div class="tab-content cdn-steps" markdown="1">

</div>

<div class="tab-content bundler-steps">

</div>

<p id="fn:1"><a href="https://github.com/KhronosGroup/glTF-Sample-Assets/tree/main">COLLADA duck</a> One texture Credit: © 2006, Sony. <a href="https://spdx.org/licenses/SCEA.html">SCEA Shared Source License, Version 1.0</a>&nbsp;<a href="#fnref:1" class="reversefootnote" role="doc-backlink">↩</a></p>

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
        layer3D.setAmbientLight({intensity: 2});

        // Adding a point light
        layer3D.addPointLight("point-light", {intensity: 30});

        /*
        "Duck, © 2006, Sony. SCEA Shared Source License, Version 1.0 - https://github.com/KhronosGroup/glTF-Sample-Assets/tree/main
        */

        // The call can be awaited for the whole download of the mesh to complete
        await layer3D.addMeshFromURL(
          // ID to give to this mesh, unique within this Layer3D instance
          "duck",

          // The URL of the mesh
          "https://docs-media.maptiler.com/docs/models/duck.glb",

          // A set of options, these can be modified later
          {
            lngLat: [-3.0615632, 56.4547039],
            heading: 150,
            scale: 10
          }
        );

        layer3D.cloneMesh("duck", "duck-baby", {
          lngLat: [-3.0617744, 56.4545475],
          heading: 45,
          scale: 3,
        });

        layer3D.cloneMesh("duck", "duck-baby-1", {
          lngLat: [-3.0613331, 56.4546995],
          heading: 180,
          scale: 4,
        });

        layer3D.cloneMesh("duck", "duck-baby-2", {
          lngLat: [-3.0611772, 56.4546843],
          heading: 190,
          scale: 3,
        });

      });
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
            center: [-3.0615632, 56.4547039],
            zoom: 18
        });

        // Waiting for the map to be ready
              map.on('ready', async () => {
                // Create a Layer3D and add it
                const layer3D = new maptiler3d.Layer3D("custom-3D-layer");
                map.addLayer(layer3D);

                // Increasing the intensity of the ambient light
                layer3D.setAmbientLight({intensity: 2});

                // Adding a point light
                layer3D.addPointLight("point-light", {intensity: 30});

                /*
                "Duck, © 2006, Sony. SCEA Shared Source License, Version 1.0 - https://github.com/KhronosGroup/glTF-Sample-Assets/tree/main
                */

                // The call can be awaited for the whole download of the mesh to complete
                await layer3D.addMeshFromURL(
                  // ID to give to this mesh, unique within this Layer3D instance
                  "duck",

                  // The URL of the mesh
                  "https://docs-media.maptiler.com/docs/models/duck.glb",

                  // A set of options, these can be modified later
                  {
                    lngLat: [-3.0615632, 56.4547039],
                    heading: 150,
                    scale: 10
                  }
                );

                layer3D.cloneMesh("duck", "duck-baby", {
                  lngLat: [-3.0617744, 56.4545475],
                  heading: 45,
                  scale: 3,
                });

                layer3D.cloneMesh("duck", "duck-baby-1", {
                  lngLat: [-3.0613331, 56.4546995],
                  heading: 180,
                  scale: 4,
                });

                layer3D.cloneMesh("duck", "duck-baby-2", {
                  lngLat: [-3.0611772, 56.4546843],
                  heading: 190,
                  scale: 3,
                });

              });
    </script>
</body>
</html>
```
