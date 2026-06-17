# Source: https://docs.maptiler.com/sdk-js/examples/3d-js-animated-flight/

# Add an animated 3D model

Use the MapTiler 3D JS module to play animations in a GLTF model and move the models to simulate a flight over the map

This demonstration showcases how to add a animated 3D model in a map and moved it acroos the map.

<p id="fn:1">

Model by <a href='https://mirada.com/' target='_blank'>Mirada</a> for <a href='https://experiments.withgoogle.com/3-dreams-of-black' target='_blank'>3 Dreams of Black</a>&nbsp;<a href="#fnref:1" class="reversefootnote" role="doc-backlink">↩</a></p>

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
// Waiting for the map to be ready
      map.on('ready', async () => {

        map.setSky({
          "sky-color": "#0C2E4B",
          "horizon-color": "#09112F",
          "fog-color": "#09112F",
          "fog-ground-blend": 0.5,
          "horizon-fog-blend": 0.1,
          "sky-horizon-blend": 1.0,
          "atmosphere-blend": 0.5,
        });

        // Create a Layer3D and add it
        const layer3D = new maptiler3d.Layer3D("custom-3D-layer");
        map.addLayer(layer3D);

         // Increasing the intensity of the ambient light
        layer3D.setAmbientLight({ intensity: 2 });

        // Adding a point light
        layer3D.addPointLight("point-light", { intensity: 30 });

        const flamingoIDOne = "flamingo";
        const flamingoIDTwo = "flamingo-clone";

        // The call can be awaited for the whole download of the mesh to complete
        await layer3D.addMeshFromURL(
          // ID to give to this mesh, unique within this Layer3D instance
          flamingoIDOne,

          // The URL of the mesh
          "https://docs-media.maptiler.com/docs/models/flamingo.glb",

          // A set of options, these can be modified later
          {
            lngLat: lakeNatron,
            heading: 12,
            scale: 100,
            animationMode: "continuous",
            altitudeReference: maptiler3d.AltitudeReference.MEAN_SEA_LEVEL,
            transform: {
              rotation: {
                x: 0,
                y: Math.PI / 2,
                z: 0,
              },
              offset: {
                x: 0,
                y: 0,
                z: -150,
              },
            },
          }
        );

        const fly = "fly!";
        const migrate = "migrate with the flamingo";
        const speed = "migration speed";

        const guiObj = {
          [fly]: true,
          [migrate]: true,
          [speed]: 0.0005,
        };

        const gui = new lil.GUI({ width: 250 });

        gui.add(guiObj, migrate);

        gui.add(guiObj, fly).onChange((play) => {
          if (play) {
            playAnimation();
          }
        });

        gui.add(guiObj, speed, 0, 0.001);

        const mesh = layer3D.getItem3D("flamingo");

        let progress = 0;

        const animationNames = mesh?.getAnimationNames();

        const animationName = animationNames?.[0];

        if (!animationName) {
          throw new Error(`No animation found with name '${animationName}'`);
        }
    
        layer3D.cloneMesh(flamingoIDOne, flamingoIDTwo, {
          animationMode: "manual",
          transform: {
            offset: {
              x: 0,
              y: 0,
              z: 300,
            },
          },
        });

        layer3D.getItem3D(flamingoIDOne)?.playAnimation(
          animationName,
          "loop",
        );

        layer3D.getItem3D(flamingoIDTwo)?.playAnimation(
          animationName,
          "loop",
        );

        const distance = maptilersdk.math.haversineDistanceWgs84(lakeNatron, makadikadi);

        const initialHeading = calculateHeading(makadikadi[1], makadikadi[0], lakeNatron[1], lakeNatron[0]);

        const flamingoOneMesh = layer3D.getItem3D(flamingoIDOne);
        const flamingoTwoMesh = layer3D.getItem3D(flamingoIDTwo);

        flamingoOneMesh.modify({ heading: initialHeading });
        flamingoTwoMesh.modify({ heading: initialHeading });

        function playAnimation() {
          progress += guiObj[speed];

          if (progress > 1) {
            progress = 0;
          }

          const nextPosition = maptilersdk.math.haversineIntermediateWgs84(lakeNatron, makadikadi, progress - (guiObj[speed] === 0 ? 0.001 : guiObj[speed]));
          const position = maptilersdk.math.haversineIntermediateWgs84(lakeNatron, makadikadi, progress);

          const roughHeading = calculateHeading(position[1], position[0], nextPosition[1], nextPosition[0]);

          // `updateAnimation` is only needed if you want to control the animation manually
          // to automatically play the animation independently of map updates, set the item
          // animationMode: "continuous"

          flamingoTwoMesh.updateAnimation(guiObj[speed] * 50);

          const distanceFromStart = maptilersdk.math.haversineDistanceWgs84(lakeNatron, [position[0], position[1]]);
          const progressPercentage = distanceFromStart / distance;

          flamingoOneMesh.modify({ lngLat: position, heading: roughHeading });
          flamingoTwoMesh.modify({ lngLat: position, heading: roughHeading });

          if (guiObj[migrate]) {
            map.setCenter(position);
            map.setZoom(10 - Math.sin(progressPercentage * Math.PI) * 2);
            map.setBearing(progressPercentage * -45);
          }

          if (guiObj[fly]) {
            requestAnimationFrame(playAnimation);
          }
        }

        if (guiObj[fly]) {
          playAnimation()
        }

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
            style: maptilersdk.MapStyle.AQUARELLE.VIVID,
            center: [0, 0],
            zoom: 10,
            pitch: 45,
            bearing: 0
        });

        // Waiting for the map to be ready
              map.on('ready', async () => {

                map.setSky({
                  "sky-color": "#0C2E4B",
                  "horizon-color": "#09112F",
                  "fog-color": "#09112F",
                  "fog-ground-blend": 0.5,
                  "horizon-fog-blend": 0.1,
                  "sky-horizon-blend": 1.0,
                  "atmosphere-blend": 0.5,
                });

                // Create a Layer3D and add it
                const layer3D = new maptiler3d.Layer3D("custom-3D-layer");
                map.addLayer(layer3D);

                 // Increasing the intensity of the ambient light
                layer3D.setAmbientLight({ intensity: 2 });

                // Adding a point light
                layer3D.addPointLight("point-light", { intensity: 30 });

                const flamingoIDOne = "flamingo";
                const flamingoIDTwo = "flamingo-clone";

                // The call can be awaited for the whole download of the mesh to complete
                await layer3D.addMeshFromURL(
                  // ID to give to this mesh, unique within this Layer3D instance
                  flamingoIDOne,

                  // The URL of the mesh
                  "https://docs-media.maptiler.com/docs/models/flamingo.glb",

                  // A set of options, these can be modified later
                  {
                    lngLat: lakeNatron,
                    heading: 12,
                    scale: 100,
                    animationMode: "continuous",
                    altitudeReference: maptiler3d.AltitudeReference.MEAN_SEA_LEVEL,
                    transform: {
                      rotation: {
                        x: 0,
                        y: Math.PI / 2,
                        z: 0,
                      },
                      offset: {
                        x: 0,
                        y: 0,
                        z: -150,
                      },
                    },
                  }
                );

                const fly = "fly!";
                const migrate = "migrate with the flamingo";
                const speed = "migration speed";

                const guiObj = {
                  [fly]: true,
                  [migrate]: true,
                  [speed]: 0.0005,
                };

                const gui = new lil.GUI({ width: 250 });

                gui.add(guiObj, migrate);

                gui.add(guiObj, fly).onChange((play) => {
                  if (play) {
                    playAnimation();
                  }
                });

                gui.add(guiObj, speed, 0, 0.001);

                const mesh = layer3D.getItem3D("flamingo");

                let progress = 0;

                const animationNames = mesh?.getAnimationNames();

                const animationName = animationNames?.[0];

                if (!animationName) {
                  throw new Error(`No animation found with name '${animationName}'`);
                }

                layer3D.cloneMesh(flamingoIDOne, flamingoIDTwo, {
                  animationMode: "manual",
                  transform: {
                    offset: {
                      x: 0,
                      y: 0,
                      z: 300,
                    },
                  },
                });

                layer3D.getItem3D(flamingoIDOne)?.playAnimation(
                  animationName,
                  "loop",
                );

                layer3D.getItem3D(flamingoIDTwo)?.playAnimation(
                  animationName,
                  "loop",
                );

                const distance = maptilersdk.math.haversineDistanceWgs84(lakeNatron, makadikadi);

                const initialHeading = calculateHeading(makadikadi[1], makadikadi[0], lakeNatron[1], lakeNatron[0]);

                const flamingoOneMesh = layer3D.getItem3D(flamingoIDOne);
                const flamingoTwoMesh = layer3D.getItem3D(flamingoIDTwo);

                flamingoOneMesh.modify({ heading: initialHeading });
                flamingoTwoMesh.modify({ heading: initialHeading });

                function playAnimation() {
                  progress += guiObj[speed];

                  if (progress > 1) {
                    progress = 0;
                  }

                  const nextPosition = maptilersdk.math.haversineIntermediateWgs84(lakeNatron, makadikadi, progress - (guiObj[speed] === 0 ? 0.001 : guiObj[speed]));
                  const position = maptilersdk.math.haversineIntermediateWgs84(lakeNatron, makadikadi, progress);

                  const roughHeading = calculateHeading(position[1], position[0], nextPosition[1], nextPosition[0]);

                  // `updateAnimation` is only needed if you want to control the animation manually
                  // to automatically play the animation independently of map updates, set the item
                  // animationMode: "continuous"

                  flamingoTwoMesh.updateAnimation(guiObj[speed] * 50);

                  const distanceFromStart = maptilersdk.math.haversineDistanceWgs84(lakeNatron, [position[0], position[1]]);
                  const progressPercentage = distanceFromStart / distance;

                  flamingoOneMesh.modify({ lngLat: position, heading: roughHeading });
                  flamingoTwoMesh.modify({ lngLat: position, heading: roughHeading });

                  if (guiObj[migrate]) {
                    map.setCenter(position);
                    map.setZoom(10 - Math.sin(progressPercentage * Math.PI) * 2);
                    map.setBearing(progressPercentage * -45);
                  }

                  if (guiObj[fly]) {
                    requestAnimationFrame(playAnimation);
                  }
                }

                if (guiObj[fly]) {
                  playAnimation()
                }

              });
    </script>
</body>
</html>
```
