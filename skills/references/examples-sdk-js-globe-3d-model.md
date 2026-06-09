# Source: https://docs.maptiler.com/sdk-js/examples/globe-3d-model/

# MapTiler Globe projection

This example shows how to add a 3D model to globe using [MapTiler 3D JS module](/sdk-js/modules/3d/). The 3D JS module enables you to integrate multiple 3D objects onto the globe surface. You can adjust model sizes, create duplicates, position models at specific elevations above sea level, and more. This offers complete flexibility in manipulating your 3D models.

<p id="fn:1">

<ul class="mb-0">

<li><a href="https://skfb.ly/oJWGw">plane a340</a> by mamont nikita is licensed under <a href="https://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution</a></li>

<li><a href="https://github.com/KhronosGroup/glTF-Sample-Assets/tree/main">COLLADA duck</a> One texture Credit: © 2006, Sony. <a href="https://spdx.org/licenses/SCEA.html">SCEA Shared Source License, Version 1.0</a></li>

</ul>

&nbsp;<a href="#fnref:1" class="reversefootnote" role="doc-backlink">↩</a>

</p>

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element to render the map
        style:  maptilersdk.MapStyle.SATELLITE,
        center: [-15.45, -21.27], // starting position [lng, lat]
        zoom: 0.75, // starting zoom
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

        const originalPlaneID = "plane";
        await layer3D.addMeshFromURL(
          originalPlaneID,
          "https://docs-media.maptiler.com/docs/models/plane_a340.glb",
          {
            scale: 1000,
            altitude: 1000000,
            heading: 55,
            altitudeReference: maptiler3d.AltitudeReference.MEAN_SEA_LEVEL,
            lngLat: [-2.548828,42.617791]
          }
        );

        const originalDuckID = "duck";
        await layer3D.addMeshFromURL(
          originalDuckID,
          "https://docs-media.maptiler.com/docs/models/duck.glb",
          {
            scale: 1000000,
            heading: 155,
            lngLat: [-43.857422,24.447150]
          }
        );

        layer3D.cloneMesh(originalDuckID, `${originalDuckID}_1`, {lngLat: [-26.298828,28.226970], scale: 400000});

      })();
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>MapTiler Globe projection</title>
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
            style: maptilersdk.MapStyle.SATELLITE,
            center: [-15.45, -21.27],
            zoom: 0.75
        });

        container: 'map', // container's id or the HTML element to render the map
                style:  maptilersdk.MapStyle.SATELLITE,
                center: [-15.45, -21.27], // starting position [lng, lat]
                zoom: 0.75, // starting zoom
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

                const originalPlaneID = "plane";
                await layer3D.addMeshFromURL(
                  originalPlaneID,
                  "https://docs-media.maptiler.com/docs/models/plane_a340.glb",
                  {
                    scale: 1000,
                    altitude: 1000000,
                    heading: 55,
                    altitudeReference: maptiler3d.AltitudeReference.MEAN_SEA_LEVEL,
                    lngLat: [-2.548828,42.617791]
                  }
                );

                const originalDuckID = "duck";
                await layer3D.addMeshFromURL(
                  originalDuckID,
                  "https://docs-media.maptiler.com/docs/models/duck.glb",
                  {
                    scale: 1000000,
                    heading: 155,
                    lngLat: [-43.857422,24.447150]
                  }
                );

                layer3D.cloneMesh(originalDuckID, `${originalDuckID}_1`, {lngLat: [-26.298828,28.226970], scale: 400000});

              })();
    </script>
</body>
</html>
```
