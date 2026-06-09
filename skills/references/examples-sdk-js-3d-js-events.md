# Source: https://docs.maptiler.com/sdk-js/examples/3d-js-events/

# Add events on 3D models

Add event listeners to your 3D models to improve interaction with objects added to your maps.

This demonstration showcases how to add user interactivity to 3D models, click, doubleclick, mouseenter, mouseleave.

<sup>Click or move the mouse over the 3D models to get to event information</sup>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const shapes = [
        {
          lngLat: [-119.65308666229248, 37.738277034695685],
            mesh: (
              new THREE.Mesh(
                new THREE.BoxGeometry(10, 10, 10),
                new THREE.MeshStandardMaterial({ color: "red", roughness: 0.5, metalness: 0.5 })
              )
          ),
          name: "box",
          altitude: 120,
        },
        {
          lngLat: [-119.61553573, 37.723071209025974],
          mesh: (
            new THREE.Mesh(
              new THREE.SphereGeometry(10),
              new THREE.MeshStandardMaterial({ color: "blue", roughness: 0.5, metalness: 0.5 })
            )
          ),
          name: "sphere",
          altitude: 120,
        },
        {
          lngLat: [-119.63008403778076, 37.735154664553534],
          altitude: 260,
          mesh: (
              new THREE.Mesh(
                new THREE.TorusGeometry(10, 5, 32, 32),
                new THREE.MeshStandardMaterial({ color: "green", roughness: 0.5, metalness: 0.5 })
              )
          ),
          name: "torus"
        },
        {
          lngLat: [-119.65128421783447, 37.72208679574618],
          altitude: 300,
          mesh: (
              new THREE.Mesh(
                new THREE.TorusKnotGeometry(10, 2, 32, 32),
                new THREE.MeshStandardMaterial({ color: "rebeccapurple", roughness: 0.5, metalness: 0.5 })
              )
          ),
          name: "torusKnot"
        },
      ];

      const info = document.getElementById("event-info");

      function setInfo(text) {
        info.innerHTML = text;
      }

      // Waiting for the map to be ready
      map.on('ready', async () => {
        // Create a Layer3D and add it
        const layer3D = new maptiler3d.Layer3D("custom-3D-layer");
        map.addLayer(layer3D);

         // Increasing the intensity of the ambient light
        layer3D.setAmbientLight({ intensity: 2 });

        // Adding a point light
        layer3D.addPointLight("point-light", { intensity: 30 });

        shapes.forEach((shape) => {
          const initialScale = 20;

          layer3D.addMesh(shape.name, shape.mesh, {
            lngLat: new maptilersdk.LngLat(shape.lngLat[0], shape.lngLat[1]),
            heading: 0,
            scale: initialScale,
            altitude: shape.altitude,
          });
          const mesh = layer3D.getItem3D(shape.name);

          const threeMesh = mesh?.mesh;

          const originalMaterial = threeMesh?.material;
          const swapMaterial = new THREE.MeshBasicMaterial({ color: "dodgerblue" });

          mesh?.on("mouseenter", (event) => {
            const mesh = layer3D.getItem3D(shape.name);
            const threeMesh = mesh?.mesh;
            if (threeMesh && "material" in threeMesh) {
              threeMesh.material = swapMaterial;
            }
            setInfo(`mouseenter! \n
              name: ${shape.name}\n
              lng: ${shape.lngLat[0]} \n
              lat: ${shape.lngLat[1]} \n
              x, y: ${event.point.x}, ${event.point.y} \n
            `);
          });
          mesh?.on("mouseleave", (event) => {
            const mesh = layer3D.getItem3D(shape.name);
            const internalMesh = mesh?.mesh;
            if (internalMesh && "material" in internalMesh) {
              internalMesh.material = originalMaterial;
            }
            setInfo(`mouseleave! \n
              name: ${shape.name}\n
              lng: ${shape.lngLat[0]} \n
              lat: ${shape.lngLat[1]} \n
              x, y: ${event.point.x}, ${event.point.y} \n
            `);
          });
          
          mesh?.on("click", (event) => {
            if (mesh?.scale[0] === initialScale) {
              mesh?.setScale(initialScale * 1.5);
            } else {
              mesh?.setScale(initialScale);
            }
            setInfo(`click! \n
              name: ${shape.name}\n
              lng: ${shape.lngLat[0]} \n
              lat: ${shape.lngLat[1]} \n
              x, y: ${event.point.x}, ${event.point.y} \n
            `);
          });

          mesh?.on("dblclick", (event) => {
            setInfo(`dblclick! \n
              name: ${shape.name}\n
              lng: ${shape.lngLat[0]} \n
              lat: ${shape.lngLat[1]} \n
              x, y: ${event.point.x}, ${event.point.y} \n
            `);
          });
        });

        let heading = 0;

        function loop() {
          requestAnimationFrame(loop);
          for (const { name: meshName } of shapes) {
            layer3D.getItem3D(meshName)?.modify({
              heading: heading,
            });
          }
          heading += 0.5;
        }

        loop();
      });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Add events on 3D models</title>
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
            center: [-119.63553428649902, 37.728162793005595],
            zoom: 12.5,
            pitch: 45,
            bearing: 0
        });

        const shapes = [
                {
                  lngLat: [-119.65308666229248, 37.738277034695685],
                    mesh: (
                      new THREE.Mesh(
                        new THREE.BoxGeometry(10, 10, 10),
                        new THREE.MeshStandardMaterial({ color: "red", roughness: 0.5, metalness: 0.5 })
                      )
                  ),
                  name: "box",
                  altitude: 120,
                },
                {
                  lngLat: [-119.61553573, 37.723071209025974],
                  mesh: (
                    new THREE.Mesh(
                      new THREE.SphereGeometry(10),
                      new THREE.MeshStandardMaterial({ color: "blue", roughness: 0.5, metalness: 0.5 })
                    )
                  ),
                  name: "sphere",
                  altitude: 120,
                },
                {
                  lngLat: [-119.63008403778076, 37.735154664553534],
                  altitude: 260,
                  mesh: (
                      new THREE.Mesh(
                        new THREE.TorusGeometry(10, 5, 32, 32),
                        new THREE.MeshStandardMaterial({ color: "green", roughness: 0.5, metalness: 0.5 })
                      )
                  ),
                  name: "torus"
                },
                {
                  lngLat: [-119.65128421783447, 37.72208679574618],
                  altitude: 300,
                  mesh: (
                      new THREE.Mesh(
                        new THREE.TorusKnotGeometry(10, 2, 32, 32),
                        new THREE.MeshStandardMaterial({ color: "rebeccapurple", roughness: 0.5, metalness: 0.5 })
                      )
                  ),
                  name: "torusKnot"
                },
              ];

              const info = document.getElementById("event-info");

              function setInfo(text) {
                info.innerHTML = text;
              }

              // Waiting for the map to be ready
              map.on('ready', async () => {
                // Create a Layer3D and add it
                const layer3D = new maptiler3d.Layer3D("custom-3D-layer");
                map.addLayer(layer3D);

                 // Increasing the intensity of the ambient light
                layer3D.setAmbientLight({ intensity: 2 });

                // Adding a point light
                layer3D.addPointLight("point-light", { intensity: 30 });

                shapes.forEach((shape) => {
                  const initialScale = 20;

                  layer3D.addMesh(shape.name, shape.mesh, {
                    lngLat: new maptilersdk.LngLat(shape.lngLat[0], shape.lngLat[1]),
                    heading: 0,
                    scale: initialScale,
                    altitude: shape.altitude,
                  });
                  const mesh = layer3D.getItem3D(shape.name);

                  const threeMesh = mesh?.mesh;

                  const originalMaterial = threeMesh?.material;
                  const swapMaterial = new THREE.MeshBasicMaterial({ color: "dodgerblue" });

                  mesh?.on("mouseenter", (event) => {
                    const mesh = layer3D.getItem3D(shape.name);
                    const threeMesh = mesh?.mesh;
                    if (threeMesh && "material" in threeMesh) {
                      threeMesh.material = swapMaterial;
                    }
                    setInfo(`mouseenter! \n
                      name: ${shape.name}\n
                      lng: ${shape.lngLat[0]} \n
                      lat: ${shape.lngLat[1]} \n
                      x, y: ${event.point.x}, ${event.point.y} \n
                    `);
                  });
                  mesh?.on("mouseleave", (event) => {
                    const mesh = layer3D.getItem3D(shape.name);
                    const internalMesh = mesh?.mesh;
                    if (internalMesh && "material" in internalMesh) {
                      internalMesh.material = originalMaterial;
                    }
                    setInfo(`mouseleave! \n
                      name: ${shape.name}\n
                      lng: ${shape.lngLat[0]} \n
                      lat: ${shape.lngLat[1]} \n
                      x, y: ${event.point.x}, ${event.point.y} \n
                    `);
                  });

                  mesh?.on("click", (event) => {
                    if (mesh?.scale[0] === initialScale) {
                      mesh?.setScale(initialScale * 1.5);
                    } else {
                      mesh?.setScale(initialScale);
                    }
                    setInfo(`click! \n
                      name: ${shape.name}\n
                      lng: ${shape.lngLat[0]} \n
                      lat: ${shape.lngLat[1]} \n
                      x, y: ${event.point.x}, ${event.point.y} \n
                    `);
                  });

                  mesh?.on("dblclick", (event) => {
                    setInfo(`dblclick! \n
                      name: ${shape.name}\n
                      lng: ${shape.lngLat[0]} \n
                      lat: ${shape.lngLat[1]} \n
                      x, y: ${event.point.x}, ${event.point.y} \n
                    `);
                  });
                });

                let heading = 0;

                function loop() {
                  requestAnimationFrame(loop);
                  for (const { name: meshName } of shapes) {
                    layer3D.getItem3D(meshName)?.modify({
                      heading: heading,
                    });
                  }
                  heading += 0.5;
                }

                loop();
              });
    </script>
</body>
</html>
```
