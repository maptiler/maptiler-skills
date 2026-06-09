# Source: https://docs.maptiler.com/sdk-js/examples/maptiler-animation/

# MaptilerAnimation with MapTiler 3D Module

This example demonstrates how to use the `MaptilerAnimation` class in combination with the `@maptiler/3d` module. It features a UFO model orbiting the Burj Khalifa, with controls to pause, play, adjust the playback rate, and advance frame by frame. The animation linearly interpolates the position (longitude, latitude, and altitude) of the UFO based on a set of defined keyframes.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
function getElementsByIds(ids) {
      return ids.map((id) => document.getElementById(id));
    }

    map.on('load', async function () {
      const animation = new maptilersdk.MaptilerAnimation({
        keyframes: getKeyframes(),
        duration: 2500,
        iterations: Infinity,
      });

      const layer3D = new maptiler3d.Layer3D("3d-scene");
      map.addLayer(layer3D);

      await layer3D.addMeshFromURL(
        // ID to give to this mesh, unique within this Layer3D instance
        "khalifa",

        // The URL of the mesh
        "https://docs-media.maptiler.com/docs/models/burj_khalifa/scene.gltf",

        // A set of options, these can be modified later
        {
          lngLat: [55.2743164, 25.1973882],
          heading: -2,
          scale: 0.013,
        },
      );

      await layer3D.addMeshFromURL(
        // ID to give to this mesh, unique within this Layer3D instance
        "ufo",

        // The URL of the mesh
        "https://docs-media.maptiler.com/docs/models/ufo/scene.gltf",

        // A set of options, these can be modified later
        {
          lngLat: [55.273, 25.197],
          altitude: 500,
          scale: 10,
        },
      );

      animation.addEventListener("timeupdate", (e) => {
        map.setBearing(map.getBearing() + 0.1);
        const ufo = layer3D.getItem3D("ufo");
        if (ufo) {
          ufo.modify({
            lngLat: [e.props.lng, e.props.lat],
            altitude: e.props.altitude,
          });
        }
      });

      animation.addEventListener("playbackratechange", (e) => {
        const playbackRateElement = document.getElementById("playbackRate");
        if (!playbackRateElement) return;
        playbackRateElement.innerText = e.playbackRate.toFixed(1) + "x";
      });

      const [playButton, pauseButton, fasterButton, slowerButton, frameAdvanceButton] = getElementsByIds(["play", "pause", "faster", "slower", "frame-advance"]);

      playButton?.addEventListener("click", () => {
        animation.play();
      });

      pauseButton?.addEventListener("click", () => {
        animation.pause();
      });

      fasterButton?.addEventListener("click", () => {
        const currentSpeed = animation.getPlaybackRate();
        animation.setPlaybackRate(currentSpeed + 0.2);
      });

      slowerButton?.addEventListener("click", () => {
        const currentSpeed = animation.getPlaybackRate();
        animation.setPlaybackRate(currentSpeed - 0.2);
      });

      frameAdvanceButton?.addEventListener("click", () => {
        animation.setCurrentDelta(animation.getCurrentDelta() + 0.01);
      });

      // Start animation by default
      animation.play();
    });

    function getKeyframes() {
      return [
        {
          delta: 0,
          easing: "ElasticInOut",
          props: {
            lng: 55.273,
            lat: 25.197,
            altitude: 300,
          },
        },
        {
          delta: 0.33333,
          easing: "ElasticInOut",
          props: {
            lng: 55.27439873444448,
            lat: 25.198719685352263,
            altitude: 250,
          },
        },
        {
          delta: 0.666666,
          easing: "ElasticInOut",
          props: {
            lng: 55.2753633312754,
            lat: 25.195489657613702,
            altitude: 350,
          },
        },
        {
          delta: 1.0,
          easing: "ElasticInOut",
          props: {
            lng: 55.273,
            lat: 25.197,
            altitude: 300,
          },
        },
      ];
    }
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>MaptilerAnimation with MapTiler 3D Module</title>
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
            style: maptilersdk.MapStyle.STREETS.DARK,
            center: [55.273056, 25.199267],
            zoom: 15.3,
            pitch: 60,
            bearing: -30
        });

        function getElementsByIds(ids) {
              return ids.map((id) => document.getElementById(id));
            }

            map.on('load', async function () {
              const animation = new maptilersdk.MaptilerAnimation({
                keyframes: getKeyframes(),
                duration: 2500,
                iterations: Infinity,
              });

              const layer3D = new maptiler3d.Layer3D("3d-scene");
              map.addLayer(layer3D);

              await layer3D.addMeshFromURL(
                // ID to give to this mesh, unique within this Layer3D instance
                "khalifa",

                // The URL of the mesh
                "https://docs-media.maptiler.com/docs/models/burj_khalifa/scene.gltf",

                // A set of options, these can be modified later
                {
                  lngLat: [55.2743164, 25.1973882],
                  heading: -2,
                  scale: 0.013,
                },
              );

              await layer3D.addMeshFromURL(
                // ID to give to this mesh, unique within this Layer3D instance
                "ufo",

                // The URL of the mesh
                "https://docs-media.maptiler.com/docs/models/ufo/scene.gltf",

                // A set of options, these can be modified later
                {
                  lngLat: [55.273, 25.197],
                  altitude: 500,
                  scale: 10,
                },
              );

              animation.addEventListener("timeupdate", (e) => {
                map.setBearing(map.getBearing() + 0.1);
                const ufo = layer3D.getItem3D("ufo");
                if (ufo) {
                  ufo.modify({
                    lngLat: [e.props.lng, e.props.lat],
                    altitude: e.props.altitude,
                  });
                }
              });

              animation.addEventListener("playbackratechange", (e) => {
                const playbackRateElement = document.getElementById("playbackRate");
                if (!playbackRateElement) return;
                playbackRateElement.innerText = e.playbackRate.toFixed(1) + "x";
              });

              const [playButton, pauseButton, fasterButton, slowerButton, frameAdvanceButton] = getElementsByIds(["play", "pause", "faster", "slower", "frame-advance"]);

              playButton?.addEventListener("click", () => {
                animation.play();
              });

              pauseButton?.addEventListener("click", () => {
                animation.pause();
              });

              fasterButton?.addEventListener("click", () => {
                const currentSpeed = animation.getPlaybackRate();
                animation.setPlaybackRate(currentSpeed + 0.2);
              });

              slowerButton?.addEventListener("click", () => {
                const currentSpeed = animation.getPlaybackRate();
                animation.setPlaybackRate(currentSpeed - 0.2);
              });

              frameAdvanceButton?.addEventListener("click", () => {
                animation.setCurrentDelta(animation.getCurrentDelta() + 0.01);
              });

              // Start animation by default
              animation.play();
            });

            function getKeyframes() {
              return [
                {
                  delta: 0,
                  easing: "ElasticInOut",
                  props: {
                    lng: 55.273,
                    lat: 25.197,
                    altitude: 300,
                  },
                },
                {
                  delta: 0.33333,
                  easing: "ElasticInOut",
                  props: {
                    lng: 55.27439873444448,
                    lat: 25.198719685352263,
                    altitude: 250,
                  },
                },
                {
                  delta: 0.666666,
                  easing: "ElasticInOut",
                  props: {
                    lng: 55.2753633312754,
                    lat: 25.195489657613702,
                    altitude: 350,
                  },
                },
                {
                  delta: 1.0,
                  easing: "ElasticInOut",
                  props: {
                    lng: 55.273,
                    lat: 25.197,
                    altitude: 300,
                  },
                },
              ];
            }
    </script>
</body>
</html>
```
