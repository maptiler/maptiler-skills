# Source: https://docs.maptiler.com/sdk-js/examples/3d-js-roll-pitch/

# Add a 3D model

Use the [MapTiler 3D JS module](/sdk-js/modules/3d/) to rotate a 3D model, setting the pitch and roll propertie. Thanks to the 3D JS module we can add 3D models to the map and configure it as we want, rotating it, animating it, scaling it, etc.

<p id="fn:1"><a href="https://skfb.ly/oG9qS">Low-Poly Biplane</a> by ElectrikGoat0395 is licensed under <a href="https://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution</a>&nbsp;<a href="#fnref:1" class="reversefootnote" role="doc-backlink">↩</a></p>

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
(async () => {
    await map.onReadyAsync();

    const layer3D = new maptiler3d.Layer3D("custom-3D-layer");
    map.addLayer(layer3D);

    const LNGLAT_OFFSET = 0.25;
    const PLANE_BASE_ALT = 6200;

    // Adding a point light
    layer3D.addPointLight("point-light", {
      intensity: 20,
      color: "#ffffff",
      lngLat: center.map(num => num + 0.0001),
      altitude: 2000,
      altitudeReference: maptiler3d.AltitudeReference.GROUND,
    });

    // Adding a mesh of a plane. 
    const originalPlaneID = "biplaneOne";
    const biplaneOne = await layer3D.addMeshFromURL(
      originalPlaneID,
      "https://docs-media.maptiler.com/docs/models/low_poly_biplane.glb",
      {
        lngLat: center,
        heading: 0,
        scale: 300,
        altitude: PLANE_BASE_ALT,
        altitudeReference: maptiler3d.AltitudeReference.GROUND,
        transform: {
          rotation: {
            y: Math.PI / 2,
          },
        }
      }
    );

    layer3D.cloneMesh("biplaneOne", "biplaneTwo");
    const biplaneTwo = layer3D.getItem3D("biplaneTwo");

    let progress = 0;
    let speed = 0.001;

    const startLngLat = maptilersdk.LngLat.convert(center.map(num => num - LNGLAT_OFFSET));
    const endLngLat = maptilersdk.LngLat.convert(center.map(num => num + LNGLAT_OFFSET));

    function updateBiPlaneOne() {
      const position = lerpLngLat(startLngLat, endLngLat, progress);
      const nextPosition = lerpLngLat(startLngLat, endLngLat, progress + 0.01);

      const currentAltitude = 2000 * Math.sin(progress * 8) + PLANE_BASE_ALT;
      const nextAltitude = 2000 * Math.sin(progress * 8 + 0.1) + PLANE_BASE_ALT;

      const pitchInRadians = getPitch(currentAltitude, nextAltitude, position.distanceTo(nextPosition));
      const pitch = radiansToDegrees(pitchInRadians);
      biplaneOne.setPitch(pitch);
      biplaneOne.setAltitude(currentAltitude);

      biplaneOne.setLngLat(position);

      biplaneOne.setHeading(radiansToDegrees(getHeading(startLngLat, endLngLat)));
      biplaneOne.setRoll(radiansToDegrees(50 * progress));
    }

    function updateBiPlaneTwo() {
      const position = orbitCenter(center, progress, 0.05);
      const nextPosition = orbitCenter(center, progress + 0.01, 0.05);

      biplaneTwo.setLngLat(position);
      biplaneTwo.setHeading(getHeading(position, nextPosition) * 180 / Math.PI);
      biplaneTwo.setRoll(45);

      const currentAltitude = 2000 * Math.sin(progress * Math.PI * 2) + PLANE_BASE_ALT;
      const nextAltitude = 2000 * Math.sin(progress * Math.PI * 2 + 0.1) + PLANE_BASE_ALT;
      const pitchInRadians = getPitch(currentAltitude, nextAltitude, position.distanceTo(nextPosition));
      const pitch = pitchInRadians * 180 / Math.PI;
      biplaneTwo.setPitch(pitch);
      biplaneTwo.setAltitude(currentAltitude);
    }

    function loop() {
      requestAnimationFrame(loop);

      updateBiPlaneOne();
      updateBiPlaneTwo();

      progress += 0.001;
      if (progress > 1) {
        progress = 0;
      }
    }

    loop();

  })()

  function orbitCenter(center, progress, radius) {
    return new maptilersdk.LngLat(
      center[0] + radius * Math.cos(progress * 2 * Math.PI),
      center[1] + radius * Math.sin(progress * 2 * Math.PI),
    );
  }

  function lerpLngLat(startLngLat, endLngLat, progress) {
    return new maptilersdk.LngLat(
      startLngLat.lng + (endLngLat.lng - startLngLat.lng) * progress,
      startLngLat.lat + (endLngLat.lat - startLngLat.lat) * progress,
    );
  }

  function getPitch(startAltitude, endAltitude, distance) {
    return Math.asin((endAltitude - startAltitude) / distance);
  }

  function getHeading(startLngLat, endLngLat) {
    return Math.atan2(endLngLat.lng - startLngLat.lng, endLngLat.lat - startLngLat.lat);
  }

  function radiansToDegrees(radians) {
    return radians * 180 / Math.PI;
  }
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
            zoom: 10,
            pitch: 65
        });

        (async () => {
            await map.onReadyAsync();

            const layer3D = new maptiler3d.Layer3D("custom-3D-layer");
            map.addLayer(layer3D);

            const LNGLAT_OFFSET = 0.25;
            const PLANE_BASE_ALT = 6200;

            // Adding a point light
            layer3D.addPointLight("point-light", {
              intensity: 20,
              color: "#ffffff",
              lngLat: center.map(num => num + 0.0001),
              altitude: 2000,
              altitudeReference: maptiler3d.AltitudeReference.GROUND,
            });

            // Adding a mesh of a plane. 
            const originalPlaneID = "biplaneOne";
            const biplaneOne = await layer3D.addMeshFromURL(
              originalPlaneID,
              "https://docs-media.maptiler.com/docs/models/low_poly_biplane.glb",
              {
                lngLat: center,
                heading: 0,
                scale: 300,
                altitude: PLANE_BASE_ALT,
                altitudeReference: maptiler3d.AltitudeReference.GROUND,
                transform: {
                  rotation: {
                    y: Math.PI / 2,
                  },
                }
              }
            );

            layer3D.cloneMesh("biplaneOne", "biplaneTwo");
            const biplaneTwo = layer3D.getItem3D("biplaneTwo");

            let progress = 0;
            let speed = 0.001;

            const startLngLat = maptilersdk.LngLat.convert(center.map(num => num - LNGLAT_OFFSET));
            const endLngLat = maptilersdk.LngLat.convert(center.map(num => num + LNGLAT_OFFSET));

            function updateBiPlaneOne() {
              const position = lerpLngLat(startLngLat, endLngLat, progress);
              const nextPosition = lerpLngLat(startLngLat, endLngLat, progress + 0.01);

              const currentAltitude = 2000 * Math.sin(progress * 8) + PLANE_BASE_ALT;
              const nextAltitude = 2000 * Math.sin(progress * 8 + 0.1) + PLANE_BASE_ALT;

              const pitchInRadians = getPitch(currentAltitude, nextAltitude, position.distanceTo(nextPosition));
              const pitch = radiansToDegrees(pitchInRadians);
              biplaneOne.setPitch(pitch);
              biplaneOne.setAltitude(currentAltitude);

              biplaneOne.setLngLat(position);

              biplaneOne.setHeading(radiansToDegrees(getHeading(startLngLat, endLngLat)));
              biplaneOne.setRoll(radiansToDegrees(50 * progress));
            }

            function updateBiPlaneTwo() {
              const position = orbitCenter(center, progress, 0.05);
              const nextPosition = orbitCenter(center, progress + 0.01, 0.05);

              biplaneTwo.setLngLat(position);
              biplaneTwo.setHeading(getHeading(position, nextPosition) * 180 / Math.PI);
              biplaneTwo.setRoll(45);

              const currentAltitude = 2000 * Math.sin(progress * Math.PI * 2) + PLANE_BASE_ALT;
              const nextAltitude = 2000 * Math.sin(progress * Math.PI * 2 + 0.1) + PLANE_BASE_ALT;
              const pitchInRadians = getPitch(currentAltitude, nextAltitude, position.distanceTo(nextPosition));
              const pitch = pitchInRadians * 180 / Math.PI;
              biplaneTwo.setPitch(pitch);
              biplaneTwo.setAltitude(currentAltitude);
            }

            function loop() {
              requestAnimationFrame(loop);

              updateBiPlaneOne();
              updateBiPlaneTwo();

              progress += 0.001;
              if (progress > 1) {
                progress = 0;
              }
            }

            loop();

          })()

          function orbitCenter(center, progress, radius) {
            return new maptilersdk.LngLat(
              center[0] + radius * Math.cos(progress * 2 * Math.PI),
              center[1] + radius * Math.sin(progress * 2 * Math.PI),
            );
          }

          function lerpLngLat(startLngLat, endLngLat, progress) {
            return new maptilersdk.LngLat(
              startLngLat.lng + (endLngLat.lng - startLngLat.lng) * progress,
              startLngLat.lat + (endLngLat.lat - startLngLat.lat) * progress,
            );
          }

          function getPitch(startAltitude, endAltitude, distance) {
            return Math.asin((endAltitude - startAltitude) / distance);
          }

          function getHeading(startLngLat, endLngLat) {
            return Math.atan2(endLngLat.lng - startLngLat.lng, endLngLat.lat - startLngLat.lat);
          }

          function radiansToDegrees(radians) {
            return radians * 180 / Math.PI;
          }
    </script>
</body>
</html>
```
