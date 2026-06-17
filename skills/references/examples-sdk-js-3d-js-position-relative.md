# Source: https://docs.maptiler.com/sdk-js/examples/3d-js-position-relative/

# MapTiler 3D | moveBy and setPositionRelativeTo

Use the [MapTiler 3D JS module](/sdk-js/modules/3d/) to set the position of una 3D model relative to another 3D model or a 3D position.

Apply a offset: `offset.x` = longitude direction, `offset.y` = altitude, `offset.z` = latitude.

Define the units: `"meters"` (default), `"feet"`, `"km"`, `"miles"`.

<p id="fn:1"><a href="https://skfb.ly/oG9qS">Low-Poly Biplane</a> by ElectrikGoat0395 is licensed under <a href="https://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution</a>&nbsp;<a href="#fnref:1" class="reversefootnote" role="doc-backlink">↩</a></p>

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
(async () => {
      await map.onReadyAsync();

      const layer3D = new maptiler3d.Layer3D("layer3d");
      map.addLayer(layer3D);


      layer3D.setAmbientLight({ intensity: 1 });
      layer3D.addPointLight("point-light", {
        intensity: 30,
        lngLat: center,
        altitude: 1000,
        altitudeReference: maptiler3d.AltitudeReference.MEAN_SEA_LEVEL,
      });

      // First Item3D at center (anchor)
      const anchor = layer3D.addMesh("anchor", createAxesMeshes(), {
        lngLat: center,
        altitude: modelAltitude,
        altitudeReference: maptiler3d.AltitudeReference.MEAN_SEA_LEVEL,
        scale: 5,
        sourceOrientation: maptiler3d.SourceOrientation.Y_UP,
      });

      let mousedown = false;
      let startLngLat = new maptilersdk.LngLat(0, 0);

      anchor.on("mousedown", (e) => {
        map.dragPan.disable();
        map.dragRotate.disable();
        mousedown = true;
        startLngLat = e.lngLat;
      });

      // we need to disable the drag pan and rotate when the mouse is up, otherwise the map will continue to pan and rotate when the mouse is released.
      map.on("mouseup", (e) => {
        if (mousedown) {
          mousedown = false;
          map.dragPan.enable();
          map.dragRotate.enable();
        }
      });

      // re-enable the drag pan and rotate when the mouse is up
      anchor.on("mouseup", () => {
        mousedown = false;
        map.dragPan.enable();
        map.dragRotate.enable();
      });

      map.on("mousemove", (e) => {
        if (mousedown) {
          // this is not an exact calculation but will suffice for the purposes of the demo.
          const eventLngLat = e.lngLat;

          const diff = new maptilersdk.LngLat(eventLngLat.lng - startLngLat.lng, eventLngLat.lat - startLngLat.lat);
          const newLngLat = new maptilersdk.LngLat(anchor.lngLat.lng + diff.lng, anchor.lngLat.lat + diff.lat);

          anchor.setLngLat(newLngLat);
          shadowingAnchor.setPositionRelativeTo(anchor, { x: 100, y: 100, z: 100 }, "meters");

          startLngLat = eventLngLat;
        }
      });

      const shadowingAnchor = anchor.clone();
      shadowingAnchor.setPositionRelativeTo(anchor, { x: 100, y: 100, z: 100 }, "meters");
      shadowingAnchor.setRelativeScale(0.4);

      addForm({ anchor, shadowingAnchor });
    })()

    function createAxesMeshes() {
      const directions = ["x", "y", "z"];
      const group = new THREE.Group();

      for (const direction of directions) {
        const arrow = new THREE.Group();
        const color = direction === "x" ? 0xff0000 : direction === "y" ? 0x00ff00 : 0x0000ff;
        const stem = new THREE.Mesh(new THREE.CylinderGeometry(0.1, 0.1, 1), new THREE.MeshStandardMaterial({ color: color }));

        stem.position.set(0, 0.5, 0);

        const head = new THREE.Mesh(new THREE.ConeGeometry(0.2, 1), new THREE.MeshStandardMaterial({ color: color }));

        head.position.set(0, 1.5, 0);

        arrow.add(stem);
        arrow.add(head);
        arrow.name = direction;
        arrow.rotation.set(direction === "x" ? Math.PI / 2 : 0, direction === "y" ? Math.PI / 2 : 0, direction === "z" ? Math.PI / 2 : 0);

        group.add(arrow);
      }

      const centralSphere = new THREE.Mesh(new THREE.SphereGeometry(0.25), new THREE.MeshStandardMaterial({ color: 0xffffff }));
      group.add(centralSphere);

      group.scale.set(10, 10, 10);

      return group;
    }

    function addForm({ anchor, shadowingAnchor }) {
      const form = document.getElementById("form");

      form.addEventListener("submit", function (e) {
        e.preventDefault();
        const formData = new FormData(form);
        const x = Number(formData.get("x"));
        const y = Number(formData.get("y"));
        const z = Number(formData.get("z"));
        const units = formData.get("units");
        anchor.moveBy({ x, y, z }, units);
        shadowingAnchor.setPositionRelativeTo(anchor, { x: 100, y: 100, z: 100 }, units);
      });
    }
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>MapTiler 3D | moveBy and setPositionRelativeTo</title>
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
            style: maptilersdk.MapStyle.SATELLITE,
            center: [2.35872, 48.86306],
            zoom: 14.48,
            pitch: 63,
            bearing: 31.9
        });

        (async () => {
              await map.onReadyAsync();

              const layer3D = new maptiler3d.Layer3D("layer3d");
              map.addLayer(layer3D);


              layer3D.setAmbientLight({ intensity: 1 });
              layer3D.addPointLight("point-light", {
                intensity: 30,
                lngLat: center,
                altitude: 1000,
                altitudeReference: maptiler3d.AltitudeReference.MEAN_SEA_LEVEL,
              });

              // First Item3D at center (anchor)
              const anchor = layer3D.addMesh("anchor", createAxesMeshes(), {
                lngLat: center,
                altitude: modelAltitude,
                altitudeReference: maptiler3d.AltitudeReference.MEAN_SEA_LEVEL,
                scale: 5,
                sourceOrientation: maptiler3d.SourceOrientation.Y_UP,
              });

              let mousedown = false;
              let startLngLat = new maptilersdk.LngLat(0, 0);

              anchor.on("mousedown", (e) => {
                map.dragPan.disable();
                map.dragRotate.disable();
                mousedown = true;
                startLngLat = e.lngLat;
              });

              // we need to disable the drag pan and rotate when the mouse is up, otherwise the map will continue to pan and rotate when the mouse is released.
              map.on("mouseup", (e) => {
                if (mousedown) {
                  mousedown = false;
                  map.dragPan.enable();
                  map.dragRotate.enable();
                }
              });

              // re-enable the drag pan and rotate when the mouse is up
              anchor.on("mouseup", () => {
                mousedown = false;
                map.dragPan.enable();
                map.dragRotate.enable();
              });

              map.on("mousemove", (e) => {
                if (mousedown) {
                  // this is not an exact calculation but will suffice for the purposes of the demo.
                  const eventLngLat = e.lngLat;

                  const diff = new maptilersdk.LngLat(eventLngLat.lng - startLngLat.lng, eventLngLat.lat - startLngLat.lat);
                  const newLngLat = new maptilersdk.LngLat(anchor.lngLat.lng + diff.lng, anchor.lngLat.lat + diff.lat);

                  anchor.setLngLat(newLngLat);
                  shadowingAnchor.setPositionRelativeTo(anchor, { x: 100, y: 100, z: 100 }, "meters");

                  startLngLat = eventLngLat;
                }
              });

              const shadowingAnchor = anchor.clone();
              shadowingAnchor.setPositionRelativeTo(anchor, { x: 100, y: 100, z: 100 }, "meters");
              shadowingAnchor.setRelativeScale(0.4);

              addForm({ anchor, shadowingAnchor });
            })()

            function createAxesMeshes() {
              const directions = ["x", "y", "z"];
              const group = new THREE.Group();

              for (const direction of directions) {
                const arrow = new THREE.Group();
                const color = direction === "x" ? 0xff0000 : direction === "y" ? 0x00ff00 : 0x0000ff;
                const stem = new THREE.Mesh(new THREE.CylinderGeometry(0.1, 0.1, 1), new THREE.MeshStandardMaterial({ color: color }));

                stem.position.set(0, 0.5, 0);

                const head = new THREE.Mesh(new THREE.ConeGeometry(0.2, 1), new THREE.MeshStandardMaterial({ color: color }));

                head.position.set(0, 1.5, 0);

                arrow.add(stem);
                arrow.add(head);
                arrow.name = direction;
                arrow.rotation.set(direction === "x" ? Math.PI / 2 : 0, direction === "y" ? Math.PI / 2 : 0, direction === "z" ? Math.PI / 2 : 0);

                group.add(arrow);
              }

              const centralSphere = new THREE.Mesh(new THREE.SphereGeometry(0.25), new THREE.MeshStandardMaterial({ color: 0xffffff }));
              group.add(centralSphere);

              group.scale.set(10, 10, 10);

              return group;
            }

            function addForm({ anchor, shadowingAnchor }) {
              const form = document.getElementById("form");

              form.addEventListener("submit", function (e) {
                e.preventDefault();
                const formData = new FormData(form);
                const x = Number(formData.get("x"));
                const y = Number(formData.get("y"));
                const z = Number(formData.get("z"));
                const units = formData.get("units");
                anchor.moveBy({ x, y, z }, units);
                shadowingAnchor.setPositionRelativeTo(anchor, { x: 100, y: 100, z: 100 }, units);
              });
            }
    </script>
</body>
</html>
```
