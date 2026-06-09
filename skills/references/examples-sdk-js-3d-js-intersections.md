# Source: https://docs.maptiler.com/sdk-js/examples/3d-js-intersections/

# MapTiler 3D | Item3D Intersections

Use the [MapTiler 3D JS module](/sdk-js/modules/3d/) test whether a 3D model intersects another 3D model.

<p id="fn:1"><a href="https://github.com/KhronosGroup/glTF-Sample-Assets/tree/main">COLLADA duck</a> One texture Credit: © 2006, Sony. <a href="https://spdx.org/licenses/SCEA.html">SCEA Shared Source License, Version 1.0</a>&nbsp;<a href="#fnref:1" class="reversefootnote" role="doc-backlink">↩</a></p>

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
(async () => {
      await map.onReadyAsync();

      const layer3D = new maptiler3d.Layer3D("item3d-intersections");
      map.addLayer(layer3D);

      // Adding a point light
      layer3D.addPointLight("light", {
        lngLat: [
          center[0],
          center[1],
        ],
        intensity: 10,
        decay: 0.1,
        color: "#ffffff",
        altitude: 6000,
      });

      // Adding a mesh. 
      const leftCubeMesh = new THREE.Mesh(new THREE.BoxGeometry(400, 400, 400), new THREE.MeshStandardMaterial({ color: "red", metalness: 0.25, roughness: 0.5 }));
      leftCubeMesh.name = "static-cube-1";
      const leftCubeItem3D = layer3D.addMesh("mesh1", leftCubeMesh, {
        altitudeReference: maptiler3d.AltitudeReference.MEAN_SEA_LEVEL,
        lngLat: [
          center[0] - 0.02,
          center[1],
        ],
      });

      leftCubeItem3D.modify({
        heading: 45,
        altitude: 1000,
      });

      const movingItem3D = await layer3D.addMeshFromURL("duck", "https://docs-media.maptiler.com/docs/models/duck.glb", {
        lngLat: center,
        heading: 0,
        scale: 180,
        altitude: 950,
        altitudeReference: maptiler3d.AltitudeReference.MEAN_SEA_LEVEL,
      });

      const sphereRightMesh = new THREE.Mesh(new THREE.SphereGeometry(250, 32, 32), new THREE.MeshStandardMaterial({ color: "red", roughness: 0.5 }));
      sphereRightMesh.name = "static-sphere";
      const sphereRightItem3D = layer3D.addMesh("sphere", sphereRightMesh, {
        lngLat: [
          center[0] + 0.02,
          center[1],
        ],
        altitude: 1000,
        altitudeReference: maptiler3d.AltitudeReference.MEAN_SEA_LEVEL,
      });


      const itemLngLat = movingItem3D.lngLat;
      let progress = 0;

      addDebugCheckBox([leftCubeItem3D, movingItem3D, sphereRightItem3D]);

      function loop() {
        requestAnimationFrame(loop);
        progress += 0.0005;

        leftCubeItem3D.modify({
          heading: 45,
          altitude: 1000,
        });

        movingItem3D.modify({
          lngLat: [
            itemLngLat.lng + Math.sin(progress * Math.PI * 2) * 0.025,
            itemLngLat.lat,
          ],
          heading: progress * Math.PI * 100,
        });


        const mesh2IntersectsMesh1 = movingItem3D.intersects(leftCubeItem3D, "low");
        const mesh2IntersectsMesh3 = movingItem3D.intersects(sphereRightItem3D, "low");

        if (mesh2IntersectsMesh1) {
          recursivelySetMaterialColor(leftCubeMesh, "green");
        } else if (mesh2IntersectsMesh3) {
          recursivelySetMaterialColor(sphereRightMesh, "blue");
        } else {
          recursivelySetMaterialColor(leftCubeMesh, "red");
          recursivelySetMaterialColor(sphereRightMesh, "red");
        }
      }

      loop();

    })()

    function recursivelySetMaterialColor(mesh, color) {
      if (mesh instanceof THREE.Mesh) {
        mesh.material.userData.oldMap = mesh.material.map;
        mesh.material.map = null;
        mesh.material.color.set(color);
      } else if (mesh instanceof Group) {
        mesh.traverse((node) => {
          if (node instanceof THREE.Mesh) {
            console.log(node);
            node.material.userData.oldMap = node.material.map;
            node.material.map = null;
            node.material.color.set(color);
          }
        });
      }
    }

    function addDebugCheckBox(objects) {
      const checkbox = document.createElement("input");
      checkbox.type = "checkbox";
      const label = document.createElement("label");
      label.style.position = "absolute";
      label.style.top = "10px";
      label.style.left = "10px";
      label.style.zIndex = "1000";
      label.style.background = "rgba(255,255,255,0.7)";
      label.style.padding = "4px 8px";
      label.style.borderRadius = "3px";
      label.style.fontSize = "14px";
      label.appendChild(checkbox);
      label.appendChild(document.createTextNode(" Show debug bounds"));
      checkbox.addEventListener("change", () => {
        objects.forEach((object) => {
          object.debug = checkbox.checked;
        });
      });
      document.body.appendChild(label);
    }
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>MapTiler 3D | Item3D Intersections</title>
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
            center: [0, 0],
            zoom: 12.63,
            pitch: 47
        });

        (async () => {
              await map.onReadyAsync();

              const layer3D = new maptiler3d.Layer3D("item3d-intersections");
              map.addLayer(layer3D);

              // Adding a point light
              layer3D.addPointLight("light", {
                lngLat: [
                  center[0],
                  center[1],
                ],
                intensity: 10,
                decay: 0.1,
                color: "#ffffff",
                altitude: 6000,
              });

              // Adding a mesh. 
              const leftCubeMesh = new THREE.Mesh(new THREE.BoxGeometry(400, 400, 400), new THREE.MeshStandardMaterial({ color: "red", metalness: 0.25, roughness: 0.5 }));
              leftCubeMesh.name = "static-cube-1";
              const leftCubeItem3D = layer3D.addMesh("mesh1", leftCubeMesh, {
                altitudeReference: maptiler3d.AltitudeReference.MEAN_SEA_LEVEL,
                lngLat: [
                  center[0] - 0.02,
                  center[1],
                ],
              });

              leftCubeItem3D.modify({
                heading: 45,
                altitude: 1000,
              });

              const movingItem3D = await layer3D.addMeshFromURL("duck", "https://docs-media.maptiler.com/docs/models/duck.glb", {
                lngLat: center,
                heading: 0,
                scale: 180,
                altitude: 950,
                altitudeReference: maptiler3d.AltitudeReference.MEAN_SEA_LEVEL,
              });

              const sphereRightMesh = new THREE.Mesh(new THREE.SphereGeometry(250, 32, 32), new THREE.MeshStandardMaterial({ color: "red", roughness: 0.5 }));
              sphereRightMesh.name = "static-sphere";
              const sphereRightItem3D = layer3D.addMesh("sphere", sphereRightMesh, {
                lngLat: [
                  center[0] + 0.02,
                  center[1],
                ],
                altitude: 1000,
                altitudeReference: maptiler3d.AltitudeReference.MEAN_SEA_LEVEL,
              });


              const itemLngLat = movingItem3D.lngLat;
              let progress = 0;

              addDebugCheckBox([leftCubeItem3D, movingItem3D, sphereRightItem3D]);

              function loop() {
                requestAnimationFrame(loop);
                progress += 0.0005;

                leftCubeItem3D.modify({
                  heading: 45,
                  altitude: 1000,
                });

                movingItem3D.modify({
                  lngLat: [
                    itemLngLat.lng + Math.sin(progress * Math.PI * 2) * 0.025,
                    itemLngLat.lat,
                  ],
                  heading: progress * Math.PI * 100,
                });


                const mesh2IntersectsMesh1 = movingItem3D.intersects(leftCubeItem3D, "low");
                const mesh2IntersectsMesh3 = movingItem3D.intersects(sphereRightItem3D, "low");

                if (mesh2IntersectsMesh1) {
                  recursivelySetMaterialColor(leftCubeMesh, "green");
                } else if (mesh2IntersectsMesh3) {
                  recursivelySetMaterialColor(sphereRightMesh, "blue");
                } else {
                  recursivelySetMaterialColor(leftCubeMesh, "red");
                  recursivelySetMaterialColor(sphereRightMesh, "red");
                }
              }

              loop();

            })()

            function recursivelySetMaterialColor(mesh, color) {
              if (mesh instanceof THREE.Mesh) {
                mesh.material.userData.oldMap = mesh.material.map;
                mesh.material.map = null;
                mesh.material.color.set(color);
              } else if (mesh instanceof Group) {
                mesh.traverse((node) => {
                  if (node instanceof THREE.Mesh) {
                    console.log(node);
                    node.material.userData.oldMap = node.material.map;
                    node.material.map = null;
                    node.material.color.set(color);
                  }
                });
              }
            }

            function addDebugCheckBox(objects) {
              const checkbox = document.createElement("input");
              checkbox.type = "checkbox";
              const label = document.createElement("label");
              label.style.position = "absolute";
              label.style.top = "10px";
              label.style.left = "10px";
              label.style.zIndex = "1000";
              label.style.background = "rgba(255,255,255,0.7)";
              label.style.padding = "4px 8px";
              label.style.borderRadius = "3px";
              label.style.fontSize = "14px";
              label.appendChild(checkbox);
              label.appendChild(document.createTextNode(" Show debug bounds"));
              checkbox.addEventListener("change", () => {
                objects.forEach((object) => {
                  object.debug = checkbox.checked;
                });
              });
              document.body.appendChild(label);
            }
    </script>
</body>
</html>
```
