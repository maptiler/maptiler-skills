# Source: https://docs.maptiler.com/sdk-js/examples/add-3d-model-terrain/

# Add a 3D model

To incorporate a 3D model into a map with 3D terrain, employ a [custom style layer](/sdk-js/api/properties/#customlayerinterface) in conjunction with [three.js](https://threejs.org).

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
let model1, model2;

    function calculateDistanceMercatorToMeters(from, to) {
        const mercatorPerMeter = from.meterInMercatorCoordinateUnits();
        // mercator x: 0=west, 1=east
        const dEast = to.x - from.x;
        const dEastMeter = dEast / mercatorPerMeter;
        // mercator y: 0=north, 1=south
        const dNorth = from.y - to.y;
        const dNorthMeter = dNorth / mercatorPerMeter;
        return {dEastMeter, dNorthMeter};
    }

    async function loadModel() {
        const loader = new GLTFLoader();
        const gltf = await loader.loadAsync('https://docs.maptiler.com/sdk-js/assets/34M_17/34M_17.gltf');
        const model = gltf.scene;
        return model;
    }

    // Known locations. We'll infer the elevation of those locations once terrain is loaded.
    const sceneOrigin = new maptilersdk.LngLat(11.5255, 47.6677);
    const model1Location = new maptilersdk.LngLat(11.527, 47.6678);
    const model2Location = new maptilersdk.LngLat(11.5249, 47.6676);

    // Configuration of the custom layer for a 3D model, implementing `CustomLayerInterface`.
    const customLayer = {
        id: '3d-model',
        type: 'custom',
        renderingMode: '3d',

        onAdd(map, gl) {
            /**
             * Setting up three.js scene.
             * We're placing model1 and model2 in such a way that the whole scene fits over the terrain.
             */

            this.camera = new THREE.Camera();
            this.scene = new THREE.Scene();
            // In threejs, y points up - we're rotating the scene such that it's y points along MapTiler SDK JS up.
            this.scene.rotateX(Math.PI / 2);
            // In threejs, z points toward the viewer - mirroring it such that z points along MapTiler SDK JS north.
            this.scene.scale.multiply(new THREE.Vector3(1, 1, -1));
            // We now have a scene with (x=east, y=up, z=north)

            const light = new THREE.DirectionalLight(0xffffff);
            // Making it just before noon - light coming from south-east.
            light.position.set(50, 70, -30).normalize();
            this.scene.add(light);

            // Axes helper to show how threejs scene is oriented.
            const axesHelper = new THREE.AxesHelper(60);
            this.scene.add(axesHelper);

            // Getting model elevations (in meters) relative to scene origin from MapTiler's terrain.
            const sceneElevation = map.queryTerrainElevation(sceneOrigin) || 0;
            const model1Elevation = map.queryTerrainElevation(model1Location) || 0;
            const model2Elevation = map.queryTerrainElevation(model2Location) || 0;
            const model1up = model1Elevation - sceneElevation;
            const model2up = model2Elevation - sceneElevation;

            // Getting model x and y (in meters) relative to scene origin.
            const sceneOriginMercator = maptilersdk.MercatorCoordinate.fromLngLat(sceneOrigin);
            const model1Mercator = maptilersdk.MercatorCoordinate.fromLngLat(model1Location);
            const model2Mercator = maptilersdk.MercatorCoordinate.fromLngLat(model2Location);
            const {dEastMeter: model1east, dNorthMeter: model1north} = calculateDistanceMercatorToMeters(sceneOriginMercator, model1Mercator);
            const {dEastMeter: model2east, dNorthMeter: model2north} = calculateDistanceMercatorToMeters(sceneOriginMercator, model2Mercator);

            model1.position.set(model1east, model1up, model1north);
            model2.position.set(model2east, model2up, model2north);

            this.scene.add(model1);
            this.scene.add(model2);

            // Use the MapTiler SDK JS map canvas for three.js.
            this.renderer = new THREE.WebGLRenderer({
                canvas: map.getCanvas(),
                context: gl,
                antialias: true
            });

            this.renderer.autoClear = false;
        },

        render(gl, args) {

            // `queryTerrainElevation` gives us the elevation of a point on the terrain
            // **relative to the elevation of `center`**,
            // where `center` is the point on the terrain that the middle of the camera points at.
            // If we didn't account for that offset, and the scene lay on a point on the terrain that is
            // below `center`, then the scene would appear to float in the air.
            const offsetFromCenterElevation = map.queryTerrainElevation(sceneOrigin) || 0;
            const sceneOriginMercator = maptilersdk.MercatorCoordinate.fromLngLat(sceneOrigin, offsetFromCenterElevation);

            const sceneTransform = {
                translateX: sceneOriginMercator.x,
                translateY: sceneOriginMercator.y,
                translateZ: sceneOriginMercator.z,
                scale: sceneOriginMercator.meterInMercatorCoordinateUnits()
            };

            const m = new THREE.Matrix4().fromArray(args.defaultProjectionData.mainMatrix);
            const l = new THREE.Matrix4()
                .makeTranslation(sceneTransform.translateX, sceneTransform.translateY, sceneTransform.translateZ)
                .scale(new THREE.Vector3(sceneTransform.scale, -sceneTransform.scale, sceneTransform.scale));

            this.camera.projectionMatrix = m.multiply(l);
            this.renderer.resetState();
            this.renderer.render(this.scene, this.camera);
            map.triggerRepaint();
        }
    };

    map.once('loadWithTerrain', async function () {
        model1 = await loadModel();
        model2 = model1.clone();

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
            style: maptilersdk.MapStyle.OUTDOOR,
            center: [11.5257, 47.668],
            zoom: 16.27,
            pitch: 60
        });

        let model1, model2;

            function calculateDistanceMercatorToMeters(from, to) {
                const mercatorPerMeter = from.meterInMercatorCoordinateUnits();
                // mercator x: 0=west, 1=east
                const dEast = to.x - from.x;
                const dEastMeter = dEast / mercatorPerMeter;
                // mercator y: 0=north, 1=south
                const dNorth = from.y - to.y;
                const dNorthMeter = dNorth / mercatorPerMeter;
                return {dEastMeter, dNorthMeter};
            }

            async function loadModel() {
                const loader = new GLTFLoader();
                const gltf = await loader.loadAsync('https://docs.maptiler.com/sdk-js/assets/34M_17/34M_17.gltf');
                const model = gltf.scene;
                return model;
            }

            // Known locations. We'll infer the elevation of those locations once terrain is loaded.
            const sceneOrigin = new maptilersdk.LngLat(11.5255, 47.6677);
            const model1Location = new maptilersdk.LngLat(11.527, 47.6678);
            const model2Location = new maptilersdk.LngLat(11.5249, 47.6676);

            // Configuration of the custom layer for a 3D model, implementing `CustomLayerInterface`.
            const customLayer = {
                id: '3d-model',
                type: 'custom',
                renderingMode: '3d',

                onAdd(map, gl) {
                    /**
                     * Setting up three.js scene.
                     * We're placing model1 and model2 in such a way that the whole scene fits over the terrain.
                     */

                    this.camera = new THREE.Camera();
                    this.scene = new THREE.Scene();
                    // In threejs, y points up - we're rotating the scene such that it's y points along MapTiler SDK JS up.
                    this.scene.rotateX(Math.PI / 2);
                    // In threejs, z points toward the viewer - mirroring it such that z points along MapTiler SDK JS north.
                    this.scene.scale.multiply(new THREE.Vector3(1, 1, -1));
                    // We now have a scene with (x=east, y=up, z=north)

                    const light = new THREE.DirectionalLight(0xffffff);
                    // Making it just before noon - light coming from south-east.
                    light.position.set(50, 70, -30).normalize();
                    this.scene.add(light);

                    // Axes helper to show how threejs scene is oriented.
                    const axesHelper = new THREE.AxesHelper(60);
                    this.scene.add(axesHelper);

                    // Getting model elevations (in meters) relative to scene origin from MapTiler's terrain.
                    const sceneElevation = map.queryTerrainElevation(sceneOrigin) || 0;
                    const model1Elevation = map.queryTerrainElevation(model1Location) || 0;
                    const model2Elevation = map.queryTerrainElevation(model2Location) || 0;
                    const model1up = model1Elevation - sceneElevation;
                    const model2up = model2Elevation - sceneElevation;

                    // Getting model x and y (in meters) relative to scene origin.
                    const sceneOriginMercator = maptilersdk.MercatorCoordinate.fromLngLat(sceneOrigin);
                    const model1Mercator = maptilersdk.MercatorCoordinate.fromLngLat(model1Location);
                    const model2Mercator = maptilersdk.MercatorCoordinate.fromLngLat(model2Location);
                    const {dEastMeter: model1east, dNorthMeter: model1north} = calculateDistanceMercatorToMeters(sceneOriginMercator, model1Mercator);
                    const {dEastMeter: model2east, dNorthMeter: model2north} = calculateDistanceMercatorToMeters(sceneOriginMercator, model2Mercator);

                    model1.position.set(model1east, model1up, model1north);
                    model2.position.set(model2east, model2up, model2north);

                    this.scene.add(model1);
                    this.scene.add(model2);

                    // Use the MapTiler SDK JS map canvas for three.js.
                    this.renderer = new THREE.WebGLRenderer({
                        canvas: map.getCanvas(),
                        context: gl,
                        antialias: true
                    });

                    this.renderer.autoClear = false;
                },

                render(gl, args) {

                    // `queryTerrainElevation` gives us the elevation of a point on the terrain
                    // **relative to the elevation of `center`**,
                    // where `center` is the point on the terrain that the middle of the camera points at.
                    // If we didn't account for that offset, and the scene lay on a point on the terrain that is
                    // below `center`, then the scene would appear to float in the air.
                    const offsetFromCenterElevation = map.queryTerrainElevation(sceneOrigin) || 0;
                    const sceneOriginMercator = maptilersdk.MercatorCoordinate.fromLngLat(sceneOrigin, offsetFromCenterElevation);

                    const sceneTransform = {
                        translateX: sceneOriginMercator.x,
                        translateY: sceneOriginMercator.y,
                        translateZ: sceneOriginMercator.z,
                        scale: sceneOriginMercator.meterInMercatorCoordinateUnits()
                    };

                    const m = new THREE.Matrix4().fromArray(args.defaultProjectionData.mainMatrix);
                    const l = new THREE.Matrix4()
                        .makeTranslation(sceneTransform.translateX, sceneTransform.translateY, sceneTransform.translateZ)
                        .scale(new THREE.Vector3(sceneTransform.scale, -sceneTransform.scale, sceneTransform.scale));

                    this.camera.projectionMatrix = m.multiply(l);
                    this.renderer.resetState();
                    this.renderer.render(this.scene, this.camera);
                    map.triggerRepaint();
                }
            };

            map.once('loadWithTerrain', async function () {
                model1 = await loadModel();
                model2 = model1.clone();

                map.addLayer(customLayer);
            });
    </script>
</body>
</html>
```
