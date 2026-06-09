# Source: https://docs.maptiler.com/sdk-js/examples/add-3d-model-babylon/

# Add a 3D model with babylon.js

To add a 3D model to the map, employ a [custom style layer](/sdk-js/api/properties/#customlayerinterface) in conjunction with [babylon.js](https://www.babylonjs.com/).

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const BABYLON = window.BABYLON;

  // World matrix parameters
  const worldOrigin = [148.9819, -35.39847];
  const worldAltitude = 0;
  
  // MapTiler SDK JS default coordinate system (no rotations)
  // +x east, -y north, +z up
  //const worldRotate = [0, 0, 0];
  
  // Babylon.js default coordinate system
  // +x east, +y up, +z north
  const worldRotate = [Math.PI / 2, 0, 0];
  
  // Calculate mercator coordinates and scale
  const worldOriginMercator = maptilersdk.MercatorCoordinate.fromLngLat(
    worldOrigin,
    worldAltitude
  );
  const worldScale = worldOriginMercator.meterInMercatorCoordinateUnits();
  
  // Calculate world matrix
  const worldMatrix = BABYLON.Matrix.Compose(
    new BABYLON.Vector3(worldScale, worldScale, worldScale),
    BABYLON.Quaternion.FromEulerAngles(
      worldRotate[0],
      worldRotate[1],
      worldRotate[2]
    ),
    new BABYLON.Vector3(
      worldOriginMercator.x,
      worldOriginMercator.y,
      worldOriginMercator.z
    )
  );

  // configuration of the custom layer for a 3D model per the CustomLayerInterface
  const customLayer = {
    id: '3d-model',
    type: 'custom',
    renderingMode: '3d',
    onAdd: function (map, gl) {
      this.engine = new BABYLON.Engine(
        gl,
        true,
        {
          useHighPrecisionMatrix: true // Important to prevent jitter at mercator scale
        },
        true
      );
      this.scene = new BABYLON.Scene(this.engine);
      this.scene.autoClear = false;
      this.scene.detachControl();

      this.scene.beforeRender = () => {
        this.engine.wipeCaches(true);
      };

      // create simple camera (will have its project matrix manually calculated)
      this.camera = new BABYLON.Camera(
        'Camera',
        new BABYLON.Vector3(0, 0, 0),
        this.scene
      );

      // create simple light
      const light = new BABYLON.HemisphericLight(
        'light1',
        new BABYLON.Vector3(0, 0, 100),
        this.scene
      );
      light.intensity = 0.7;

      // Add debug axes viewer, positioned at origin, 10 meter axis lengths
      new BABYLON.AxesViewer(this.scene, 10);

      // load GLTF model in to the scene
      BABYLON.SceneLoader.LoadAssetContainerAsync(
        'https://docs.maptiler.com/sdk-js/assets/34M_17/34M_17.gltf',
        '',
        this.scene
      ).then((modelContainer) => {
        modelContainer.addAllToScene();

        const rootMesh = modelContainer.createRootMesh();

        // If using MapTiler SDK JS coordinate system (+z up)
        //rootMesh.rotation.x = Math.PI/2

        // Create a second mesh
        const rootMesh2 = rootMesh.clone();

        // Position in babylon.js coordinate system
        rootMesh2.position.x = 25; // +east, meters
        rootMesh2.position.z = 25; // +north, meters
      });

      this.map = map;
    },
    render: function (gl, args) {
      const cameraMatrix = BABYLON.Matrix.FromArray(args.defaultProjectionData.mainMatrix);

      // world-view-projection matrix
      const wvpMatrix = worldMatrix.multiply(cameraMatrix);

      this.camera.freezeProjectionMatrix(wvpMatrix);

      this.scene.render(false);
      this.map.triggerRepaint();
    }
  };

  map.on('style.load', function () {
      map.addLayer(customLayer);
  });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Add a 3D model with babylon.js</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <script src="https://unpkg.com/babylonjs@9.9.1/babylon.js"></script>
    <script src="https://unpkg.com/babylonjs-loaders@9.9.1/babylonjs.loaders.min.js"></script>
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
            center: [148.9819, -35.3981],
            zoom: 18,
            pitch: 60
        });

        const BABYLON = window.BABYLON;

          // World matrix parameters
          const worldOrigin = [148.9819, -35.39847];
          const worldAltitude = 0;

          // MapTiler SDK JS default coordinate system (no rotations)
          // +x east, -y north, +z up
          //const worldRotate = [0, 0, 0];

          // Babylon.js default coordinate system
          // +x east, +y up, +z north
          const worldRotate = [Math.PI / 2, 0, 0];

          // Calculate mercator coordinates and scale
          const worldOriginMercator = maptilersdk.MercatorCoordinate.fromLngLat(
            worldOrigin,
            worldAltitude
          );
          const worldScale = worldOriginMercator.meterInMercatorCoordinateUnits();

          // Calculate world matrix
          const worldMatrix = BABYLON.Matrix.Compose(
            new BABYLON.Vector3(worldScale, worldScale, worldScale),
            BABYLON.Quaternion.FromEulerAngles(
              worldRotate[0],
              worldRotate[1],
              worldRotate[2]
            ),
            new BABYLON.Vector3(
              worldOriginMercator.x,
              worldOriginMercator.y,
              worldOriginMercator.z
            )
          );

          // configuration of the custom layer for a 3D model per the CustomLayerInterface
          const customLayer = {
            id: '3d-model',
            type: 'custom',
            renderingMode: '3d',
            onAdd: function (map, gl) {
              this.engine = new BABYLON.Engine(
                gl,
                true,
                {
                  useHighPrecisionMatrix: true // Important to prevent jitter at mercator scale
                },
                true
              );
              this.scene = new BABYLON.Scene(this.engine);
              this.scene.autoClear = false;
              this.scene.detachControl();

              this.scene.beforeRender = () => {
                this.engine.wipeCaches(true);
              };

              // create simple camera (will have its project matrix manually calculated)
              this.camera = new BABYLON.Camera(
                'Camera',
                new BABYLON.Vector3(0, 0, 0),
                this.scene
              );

              // create simple light
              const light = new BABYLON.HemisphericLight(
                'light1',
                new BABYLON.Vector3(0, 0, 100),
                this.scene
              );
              light.intensity = 0.7;

              // Add debug axes viewer, positioned at origin, 10 meter axis lengths
              new BABYLON.AxesViewer(this.scene, 10);

              // load GLTF model in to the scene
              BABYLON.SceneLoader.LoadAssetContainerAsync(
                'https://docs.maptiler.com/sdk-js/assets/34M_17/34M_17.gltf',
                '',
                this.scene
              ).then((modelContainer) => {
                modelContainer.addAllToScene();

                const rootMesh = modelContainer.createRootMesh();

                // If using MapTiler SDK JS coordinate system (+z up)
                //rootMesh.rotation.x = Math.PI/2

                // Create a second mesh
                const rootMesh2 = rootMesh.clone();

                // Position in babylon.js coordinate system
                rootMesh2.position.x = 25; // +east, meters
                rootMesh2.position.z = 25; // +north, meters
              });

              this.map = map;
            },
            render: function (gl, args) {
              const cameraMatrix = BABYLON.Matrix.FromArray(args.defaultProjectionData.mainMatrix);

              // world-view-projection matrix
              const wvpMatrix = worldMatrix.multiply(cameraMatrix);

              this.camera.freezeProjectionMatrix(wvpMatrix);

              this.scene.render(false);
              this.map.triggerRepaint();
            }
          };

          map.on('style.load', function () {
              map.addLayer(customLayer);
          });
    </script>
</body>
</html>
```
