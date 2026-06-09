# Source: https://docs.maptiler.com/sdk-js/examples/add-3d-model/

# Add a 3D model

To incorporate a 3D model into the map, employ a [custom style layer](/sdk-js/api/properties/#customlayerinterface) in conjunction with [three.js](https://threejs.org).

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
// parameters to ensure the model is georeferenced correctly on the map
  const modelOrigin = [148.9819, -35.39847];
  const modelAltitude = 0;
  const modelRotate = [Math.PI / 2, 0, 0];

  const modelAsMercatorCoordinate = maptilersdk.MercatorCoordinate.fromLngLat(
    modelOrigin,
    modelAltitude
  );

  // transformation parameters to position, rotate and scale the 3D model onto the map
  const modelTransform = {
    translateX: modelAsMercatorCoordinate.x,
    translateY: modelAsMercatorCoordinate.y,
    translateZ: modelAsMercatorCoordinate.z,
    rotateX: modelRotate[0],
    rotateY: modelRotate[1],
    rotateZ: modelRotate[2],
    /* Since our 3D model is in real world meters, a scale transform needs to be
      * applied since the CustomLayerInterface expects units in MercatorCoordinates.
      */
    scale: modelAsMercatorCoordinate.meterInMercatorCoordinateUnits()
  };

  // configuration of the custom layer for a 3D model per the CustomLayerInterface
  const customLayer = {
    id: '3d-model',
    type: 'custom',
    renderingMode: '3d',
    onAdd: function (map, gl) {
      this.camera = new THREE.Camera();
      this.scene = new THREE.Scene();

      // create two three.js lights to illuminate the model
      const directionalLight = new THREE.DirectionalLight(0xffffff);
      directionalLight.position.set(0, -70, 100).normalize();
      this.scene.add(directionalLight);

      const directionalLight2 = new THREE.DirectionalLight(0xffffff);
      directionalLight2.position.set(0, 70, 100).normalize();
      this.scene.add(directionalLight2);

      // use the three.js GLTF loader to add the 3D model to the three.js scene
      const loader = new GLTFLoader();
      loader.load(
        'https://docs.maptiler.com/sdk-js/assets/34M_17/34M_17.gltf',
        (gltf) => {
            this.scene.add(gltf.scene);
        }
      );
      this.map = map;

      // use the MapTiler SDK JS map canvas for three.js
      this.renderer = new THREE.WebGLRenderer({
        canvas: map.getCanvas(),
        context: gl,
        antialias: true
      });

      this.renderer.autoClear = false;
    },
    render: function (gl, args) {
      const rotationX = new THREE.Matrix4().makeRotationAxis(
        new THREE.Vector3(1, 0, 0),
        modelTransform.rotateX
      );
      const rotationY = new THREE.Matrix4().makeRotationAxis(
        new THREE.Vector3(0, 1, 0),
        modelTransform.rotateY
      );
      const rotationZ = new THREE.Matrix4().makeRotationAxis(
        new THREE.Vector3(0, 0, 1),
        modelTransform.rotateZ
      );

      const m = new THREE.Matrix4().fromArray(args.defaultProjectionData.mainMatrix);
      const l = new THREE.Matrix4()
        .makeTranslation(
          modelTransform.translateX,
          modelTransform.translateY,
          modelTransform.translateZ
        )
        .scale(
          new THREE.Vector3(
            modelTransform.scale,
            -modelTransform.scale,
            modelTransform.scale
          )
        )
        .multiply(rotationX)
        .multiply(rotationY)
        .multiply(rotationZ);

      this.camera.projectionMatrix = m.multiply(l);
      this.renderer.resetState();
      this.renderer.render(this.scene, this.camera);
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
    <title>Add a 3D model</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
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

        // parameters to ensure the model is georeferenced correctly on the map
          const modelOrigin = [148.9819, -35.39847];
          const modelAltitude = 0;
          const modelRotate = [Math.PI / 2, 0, 0];

          const modelAsMercatorCoordinate = maptilersdk.MercatorCoordinate.fromLngLat(
            modelOrigin,
            modelAltitude
          );

          // transformation parameters to position, rotate and scale the 3D model onto the map
          const modelTransform = {
            translateX: modelAsMercatorCoordinate.x,
            translateY: modelAsMercatorCoordinate.y,
            translateZ: modelAsMercatorCoordinate.z,
            rotateX: modelRotate[0],
            rotateY: modelRotate[1],
            rotateZ: modelRotate[2],
            /* Since our 3D model is in real world meters, a scale transform needs to be
              * applied since the CustomLayerInterface expects units in MercatorCoordinates.
              */
            scale: modelAsMercatorCoordinate.meterInMercatorCoordinateUnits()
          };

          // configuration of the custom layer for a 3D model per the CustomLayerInterface
          const customLayer = {
            id: '3d-model',
            type: 'custom',
            renderingMode: '3d',
            onAdd: function (map, gl) {
              this.camera = new THREE.Camera();
              this.scene = new THREE.Scene();

              // create two three.js lights to illuminate the model
              const directionalLight = new THREE.DirectionalLight(0xffffff);
              directionalLight.position.set(0, -70, 100).normalize();
              this.scene.add(directionalLight);

              const directionalLight2 = new THREE.DirectionalLight(0xffffff);
              directionalLight2.position.set(0, 70, 100).normalize();
              this.scene.add(directionalLight2);

              // use the three.js GLTF loader to add the 3D model to the three.js scene
              const loader = new GLTFLoader();
              loader.load(
                'https://docs.maptiler.com/sdk-js/assets/34M_17/34M_17.gltf',
                (gltf) => {
                    this.scene.add(gltf.scene);
                }
              );
              this.map = map;

              // use the MapTiler SDK JS map canvas for three.js
              this.renderer = new THREE.WebGLRenderer({
                canvas: map.getCanvas(),
                context: gl,
                antialias: true
              });

              this.renderer.autoClear = false;
            },
            render: function (gl, args) {
              const rotationX = new THREE.Matrix4().makeRotationAxis(
                new THREE.Vector3(1, 0, 0),
                modelTransform.rotateX
              );
              const rotationY = new THREE.Matrix4().makeRotationAxis(
                new THREE.Vector3(0, 1, 0),
                modelTransform.rotateY
              );
              const rotationZ = new THREE.Matrix4().makeRotationAxis(
                new THREE.Vector3(0, 0, 1),
                modelTransform.rotateZ
              );

              const m = new THREE.Matrix4().fromArray(args.defaultProjectionData.mainMatrix);
              const l = new THREE.Matrix4()
                .makeTranslation(
                  modelTransform.translateX,
                  modelTransform.translateY,
                  modelTransform.translateZ
                )
                .scale(
                  new THREE.Vector3(
                    modelTransform.scale,
                    -modelTransform.scale,
                    modelTransform.scale
                  )
                )
                .multiply(rotationX)
                .multiply(rotationY)
                .multiply(rotationZ);

              this.camera.projectionMatrix = m.multiply(l);
              this.renderer.resetState();
              this.renderer.render(this.scene, this.camera);
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
