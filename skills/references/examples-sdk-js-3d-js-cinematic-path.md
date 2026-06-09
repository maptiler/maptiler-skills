# Source: https://docs.maptiler.com/sdk-js/examples/3d-js-cinematic-path/

# MapTiler 3D | Globe Travel Example

Animate multidimensional routes with a dynamic camera that follows the journey in real-time. Whether it’s a high-altitude flight or a ground-level drive, provide clear spatial and temporal context by syncing 3D transport models with precise path data.

This demonstration showcases how to animate multidimensional routes in a map.

<p id="fn:1"><a href="https://skfb.ly/oJWGw">plane a340</a> by mamont nikita is licensed under <a href="https://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution</a>&nbsp;<a href="#fnref:1" class="reversefootnote" role="doc-backlink">↩</a></p>

<p id="fn:1">

Model by <a href='https://sketchfab.com/scailman' target='_blank'>scailman</a> for <a href='https://sketchfab.com/3d-models/low-poly-small-car-ebe7c5e98a7448b5abb2eaf0cb22b766' target='_blank'>Low Poly Small car</a>&nbsp;<a href="#fnref:1" class="reversefootnote" role="doc-backlink">↩</a></p>

<p id="fn:1">

Model by <a href='https://sketchfab.com/pedrosvalero' target='_blank'>pedrosvalero</a> for <a href='https://sketchfab.com/3d-models/main-boat-from-over-the-seas-ggj17-260bd2ab5e574ce796aec5df1eb2866d' target='_blank'>Main Boat From Over The Seas GGJ'17</a>&nbsp;<a href="#fnref:1" class="reversefootnote" role="doc-backlink">↩</a></p>

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
// Waiting for the map to be ready
    map.on('ready', async () => {

      // Add 3D layer for the plane
      //#region Plane 3D Model
      const layer3D = new maptiler3d.Layer3D("3d-layer");

      map.addLayer(layer3D);

      const plane = await layer3D.addMeshFromURL("plane", "https://docs-media.maptiler.com/docs/models/plane_a340.glb", {
        lngLat: MADRID,
        altitude: 0,
        scale: 1,
        altitudeReference: maptiler3d.AltitudeReference.GROUND,
        transform: {
          rotation: {
            y: Math.PI / 2,
          },
        },
      });

      plane.setHeading(
        turf.bearing([MADRID[0], MADRID[1]], [RIO_DE_JANEIRO[0], RIO_DE_JANEIRO[1]])
      );

      //#region Boat 3D Model
      const boat = await layer3D.addMeshFromURL("boat", "https://docs-media.maptiler.com/docs/models/boat/scene.gltf", {
        lngLat: RIO_DE_JANEIRO,
        altitude: 0,
        scale: 1,
        altitudeReference: maptiler3d.AltitudeReference.MEAN_SEA_LEVEL,
        transform: {
          rotation: {
            y: Math.PI / 2,
          },
        },
      });

      boat.setHeading(
        turf.bearing([MADRID[0], MADRID[1]], [RIO_DE_JANEIRO[0], RIO_DE_JANEIRO[1]])
      );

      //#region Car 3D Model
      const car = await layer3D.addMeshFromURL("car", "https://docs-media.maptiler.com/docs/models/car/scene.gltf", {
        lngLat: LISBOA,
        altitude: 0,
        altitudeReference: maptiler3d.AltitudeReference.GROUND,
        scale: 1000,
      });

      car.setHeading(turf.bearing([LISBOA[0], LISBOA[1]], [MADRID[0], MADRID[1]]));
      // Add markers for the airports
      //#region Markers
      const lisboaMarker = new maptilersdk.Marker({
        element: document.getElementById("lisboa-marker"),
        subpixelPositioning: true,
      });

      lisboaMarker.setLngLat(LISBOA);
      lisboaMarker.addTo(map);

      const rioMarker = new maptilersdk.Marker({
        element: document.getElementById("rio-marker"),
        subpixelPositioning: true,
      });

      rioMarker.setLngLat(RIO_DE_JANEIRO);
      rioMarker.addTo(map);

      const madridMarker = new maptilersdk.Marker({
        element: document.getElementById("madrid-marker"),
        subpixelPositioning: true,
      });

      madridMarker.setLngLat(MADRID);
      madridMarker.addTo(map);

      //#region Plane Animation
      const planeAnimation = new maptilersdk.MaptilerAnimation({
        iterations: 1,
        keyframes: KEYFRAMES,
        duration: animationDuration,
      });

      //#region fetch data and add layers
      const boatJourneyData = await fetchGeoJSONAndAddAsLayer(
        "boat-route",
        "../data/boat.geojson",
        map
      );
      const carJourneyData = await fetchGeoJSONAndAddAsLayer(
        "car-route",
        "../data/car.geojson",
        map
      );

      //#region Boat and Car AnimatedRouteLayerSetup
      const boatAnimatedRouteLayer = new maptilersdk.AnimatedRouteLayer({
        source: {
          id: "boat-route",
          layerID: "boat-route-layer",
        },
        pathStrokeAnimation: {
          activeColor: [0, 255, 255, 0.5],
          inactiveColor: [0, 0, 0, 0],
        },
        cameraAnimation: {
          pathSmoothing: {
            resolution: 1,
            epsilon: 3,
          },
        },
        duration: animationDuration * 4,
        iterations: 1,
        delay: 1000,
      });

      const carAnimatedRouteLayer = new maptilersdk.AnimatedRouteLayer({
        source: {
          id: "car-route",
          layerID: "car-route-layer",
        },
        pathStrokeAnimation: {
          activeColor: [0, 255, 255, 0.5],
          inactiveColor: [0, 0, 0, 0],
        },
        cameraAnimation: {
          pathSmoothing: {
            resolution: 0.1,
            epsilon: 5,
          },
        },
        iterations: 1,
        duration: animationDuration * 2,
        delay: 1000,
      });

      let currentAnimation =
        planeAnimation;
      //#region "chaining" of animations
      planeAnimation.addEventListener("animationend", (e) => {
        planeAnimation.pause();
        map.addLayer(boatAnimatedRouteLayer);
        boatAnimatedRouteLayer.play();
        currentAnimation = boatAnimatedRouteLayer;
      });

      boatAnimatedRouteLayer.addEventListener("animationend", (e) => {
        map.removeLayer(boatAnimatedRouteLayer.id);
        boatAnimatedRouteLayer.pause();
        boatAnimatedRouteLayer.animationInstance?.reset();
        map.addLayer(carAnimatedRouteLayer);
        carAnimatedRouteLayer.play();
        currentAnimation = carAnimatedRouteLayer;
      });

      carAnimatedRouteLayer.addEventListener("animationend", (e) => {
        carAnimatedRouteLayer.pause();
        carAnimatedRouteLayer.animationInstance?.reset();
        map.removeLayer(carAnimatedRouteLayer.id);
        planeAnimation.play();
        currentAnimation = planeAnimation;
      });

      carAnimatedRouteLayer.addEventListener("timeupdate", frameCallback);
      boatAnimatedRouteLayer.addEventListener("timeupdate", frameCallback);
      planeAnimation.addEventListener("timeupdate", frameCallback);

      const carJourneyLength = turf.length(carJourneyData, { units: "kilometers" });
      const boatJourneyLength = turf.length(boatJourneyData, {
        units: "kilometers",
      });

      //#region Frame
      function frameCallback(e) {
        const isBoatAnimation =
          e.target === boatAnimatedRouteLayer.animationInstance;
        const isCarAnimation = e.target === carAnimatedRouteLayer.animationInstance;
        const isPlaneAnimation = e.target === planeAnimation;

        map.setCenter(new maptilersdk.LngLat(e.props.lng, e.props.lat));

        const previousLngLat = [
          e.previousProps.lng,
          e.previousProps.lat,
        ];
        const nextLngLat = [e.props.lng, e.props.lat];

        const heading = turf.bearing(previousLngLat, nextLngLat);

        if (isPlaneAnimation) {
          const previousStop = [
            e.keyframe?.props.lng,
            e.keyframe?.props.lat,
          ];
          const nextStop = [
            e.nextKeyframe?.props.lng,
            e.nextKeyframe?.props.lat,
          ];

          const legDistance = turf.rhumbDistance(previousStop, nextStop);

          const currentPosition = [e.props.lng, e.props.lat];

          const percentLeftToNextStop =
            turf.rhumbDistance(currentPosition, nextStop) / legDistance;

          const scale = Math.sin(percentLeftToNextStop * Math.PI) * 500;

          const zoomAlpha = Math.sin(percentLeftToNextStop * Math.PI);
          const zoom = lerp(atAirportZoom, midAirZoom, zoomAlpha);

          map.setZoom(zoom || map.getZoom());

          map.setBearing((1 - e.currentDelta) * 360);

          plane.modify({
            heading,
            lngLat: currentPosition,
            scale,
            altitude: 1000 * scale,
          });
        }

        if (isBoatAnimation) {
          map.setCenter(new maptilersdk.LngLat(e.props.lng, e.props.lat));
          const boatPosition = turf.along(
            boatJourneyData.features[0],
            boatJourneyLength * e.currentDelta,
            { units: "kilometers" }
          );
          const nextBoatPosition = turf.along(
            boatJourneyData.features[0],
            boatJourneyLength * (e.currentDelta + 0.005),
            { units: "kilometers" }
          );

          const boatHeading =
            turf.bearing(
              [
                boatPosition.geometry.coordinates[0],
                boatPosition.geometry.coordinates[1],
              ],
              [
                nextBoatPosition.geometry.coordinates[0],
                nextBoatPosition.geometry.coordinates[1],
              ]
            ) + 180;

          const scale = Math.sin(e.currentDelta * Math.PI) * 1000;

          boat.modify({
            heading: boatHeading,
            lngLat: [
              boatPosition.geometry.coordinates[0],
              boatPosition.geometry.coordinates[1],
            ],
            scale,
          });
        }

        if (isCarAnimation) {
          map.setCenter(new maptilersdk.LngLat(e.props.lng, e.props.lat));

          const carPosition = turf.along(
            carJourneyData.features[0].geometry,
            carJourneyLength * e.currentDelta,
            { units: "kilometers" }
          );
          const nextCarPosition = turf.along(
            carJourneyData.features[0].geometry,
            carJourneyLength * (e.currentDelta + 0.01),
            { units: "kilometers" }
          );

          const carHeading =
            turf.bearing(
              [
                carPosition.geometry.coordinates[0],
                carPosition.geometry.coordinates[1],
              ],
              [
                nextCarPosition.geometry.coordinates[0],
                nextCarPosition.geometry.coordinates[1],
              ]
            ) + 180;

          const scale = Math.sin(e.currentDelta * Math.PI) * 1000;

          car.modify({
            heading: carHeading, // because the car model is 180
            lngLat: [
              carPosition.geometry.coordinates[0],
              carPosition.geometry.coordinates[1],
            ],
            scale,
          });
        }
      }

      let isPlaying = false;
      document.getElementById("play-button")?.addEventListener("click", () => {
        if (isPlaying) {
          currentAnimation?.pause();
          isPlaying = false;
        } else {
          currentAnimation?.play();
          isPlaying = true;
        }
      });

    });

    //#region Helper Functions / types
    function lerp(a, b, t) {
      return a + (b - a) * t;
    }

    async function fetchGeoJSONAndAddAsLayer(id, url, map) {
      try {
        const data = await fetch(url).then((response) => response.json());
        addSourceAndLayer(map, id, {
          type: "geojson",
          data,
          lineMetrics: true,
        });
        return data;
      } catch (error) {
        throw error;
      }
    }

    function addSourceAndLayer(
      map,
      id,
      source
    ) {
      map.addSource(id, source);
      map.addLayer(
        {
          source: id,
          id: `${id}-layer`,
          type: "line",
          layout: {
            visibility: "visible",
            "line-sort-key": 1,
          },
          paint: {
            "line-color": "transparent",
            "line-width": 10,
          },
        },
        "3d-layer"
      );
    }
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>MapTiler 3D | Globe Travel Example</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <script src="https://cdn.maptiler.com/maptiler-3d/4.0.1/maptiler-3d.umd.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@turf/turf@7.3.5/turf.min.js"></script>
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
            style: maptilersdk.MapStyle.HYBRID,
            center: [0, 0],
            zoom: 7,
            pitch: 60
        });

        // Waiting for the map to be ready
            map.on('ready', async () => {

              // Add 3D layer for the plane
              //#region Plane 3D Model
              const layer3D = new maptiler3d.Layer3D("3d-layer");

              map.addLayer(layer3D);

              const plane = await layer3D.addMeshFromURL("plane", "https://docs-media.maptiler.com/docs/models/plane_a340.glb", {
                lngLat: MADRID,
                altitude: 0,
                scale: 1,
                altitudeReference: maptiler3d.AltitudeReference.GROUND,
                transform: {
                  rotation: {
                    y: Math.PI / 2,
                  },
                },
              });

              plane.setHeading(
                turf.bearing([MADRID[0], MADRID[1]], [RIO_DE_JANEIRO[0], RIO_DE_JANEIRO[1]])
              );

              //#region Boat 3D Model
              const boat = await layer3D.addMeshFromURL("boat", "https://docs-media.maptiler.com/docs/models/boat/scene.gltf", {
                lngLat: RIO_DE_JANEIRO,
                altitude: 0,
                scale: 1,
                altitudeReference: maptiler3d.AltitudeReference.MEAN_SEA_LEVEL,
                transform: {
                  rotation: {
                    y: Math.PI / 2,
                  },
                },
              });

              boat.setHeading(
                turf.bearing([MADRID[0], MADRID[1]], [RIO_DE_JANEIRO[0], RIO_DE_JANEIRO[1]])
              );

              //#region Car 3D Model
              const car = await layer3D.addMeshFromURL("car", "https://docs-media.maptiler.com/docs/models/car/scene.gltf", {
                lngLat: LISBOA,
                altitude: 0,
                altitudeReference: maptiler3d.AltitudeReference.GROUND,
                scale: 1000,
              });

              car.setHeading(turf.bearing([LISBOA[0], LISBOA[1]], [MADRID[0], MADRID[1]]));
              // Add markers for the airports
              //#region Markers
              const lisboaMarker = new maptilersdk.Marker({
                element: document.getElementById("lisboa-marker"),
                subpixelPositioning: true,
              });

              lisboaMarker.setLngLat(LISBOA);
              lisboaMarker.addTo(map);

              const rioMarker = new maptilersdk.Marker({
                element: document.getElementById("rio-marker"),
                subpixelPositioning: true,
              });

              rioMarker.setLngLat(RIO_DE_JANEIRO);
              rioMarker.addTo(map);

              const madridMarker = new maptilersdk.Marker({
                element: document.getElementById("madrid-marker"),
                subpixelPositioning: true,
              });

              madridMarker.setLngLat(MADRID);
              madridMarker.addTo(map);

              //#region Plane Animation
              const planeAnimation = new maptilersdk.MaptilerAnimation({
                iterations: 1,
                keyframes: KEYFRAMES,
                duration: animationDuration,
              });

              //#region fetch data and add layers
              const boatJourneyData = await fetchGeoJSONAndAddAsLayer(
                "boat-route",
                "../data/boat.geojson",
                map
              );
              const carJourneyData = await fetchGeoJSONAndAddAsLayer(
                "car-route",
                "../data/car.geojson",
                map
              );

              //#region Boat and Car AnimatedRouteLayerSetup
              const boatAnimatedRouteLayer = new maptilersdk.AnimatedRouteLayer({
                source: {
                  id: "boat-route",
                  layerID: "boat-route-layer",
                },
                pathStrokeAnimation: {
                  activeColor: [0, 255, 255, 0.5],
                  inactiveColor: [0, 0, 0, 0],
                },
                cameraAnimation: {
                  pathSmoothing: {
                    resolution: 1,
                    epsilon: 3,
                  },
                },
                duration: animationDuration * 4,
                iterations: 1,
                delay: 1000,
              });

              const carAnimatedRouteLayer = new maptilersdk.AnimatedRouteLayer({
                source: {
                  id: "car-route",
                  layerID: "car-route-layer",
                },
                pathStrokeAnimation: {
                  activeColor: [0, 255, 255, 0.5],
                  inactiveColor: [0, 0, 0, 0],
                },
                cameraAnimation: {
                  pathSmoothing: {
                    resolution: 0.1,
                    epsilon: 5,
                  },
                },
                iterations: 1,
                duration: animationDuration * 2,
                delay: 1000,
              });

              let currentAnimation =
                planeAnimation;
              //#region "chaining" of animations
              planeAnimation.addEventListener("animationend", (e) => {
                planeAnimation.pause();
                map.addLayer(boatAnimatedRouteLayer);
                boatAnimatedRouteLayer.play();
                currentAnimation = boatAnimatedRouteLayer;
              });

              boatAnimatedRouteLayer.addEventListener("animationend", (e) => {
                map.removeLayer(boatAnimatedRouteLayer.id);
                boatAnimatedRouteLayer.pause();
                boatAnimatedRouteLayer.animationInstance?.reset();
                map.addLayer(carAnimatedRouteLayer);
                carAnimatedRouteLayer.play();
                currentAnimation = carAnimatedRouteLayer;
              });

              carAnimatedRouteLayer.addEventListener("animationend", (e) => {
                carAnimatedRouteLayer.pause();
                carAnimatedRouteLayer.animationInstance?.reset();
                map.removeLayer(carAnimatedRouteLayer.id);
                planeAnimation.play();
                currentAnimation = planeAnimation;
              });

              carAnimatedRouteLayer.addEventListener("timeupdate", frameCallback);
              boatAnimatedRouteLayer.addEventListener("timeupdate", frameCallback);
              planeAnimation.addEventListener("timeupdate", frameCallback);

              const carJourneyLength = turf.length(carJourneyData, { units: "kilometers" });
              const boatJourneyLength = turf.length(boatJourneyData, {
                units: "kilometers",
              });

              //#region Frame
              function frameCallback(e) {
                const isBoatAnimation =
                  e.target === boatAnimatedRouteLayer.animationInstance;
                const isCarAnimation = e.target === carAnimatedRouteLayer.animationInstance;
                const isPlaneAnimation = e.target === planeAnimation;

                map.setCenter(new maptilersdk.LngLat(e.props.lng, e.props.lat));

                const previousLngLat = [
                  e.previousProps.lng,
                  e.previousProps.lat,
                ];
                const nextLngLat = [e.props.lng, e.props.lat];

                const heading = turf.bearing(previousLngLat, nextLngLat);

                if (isPlaneAnimation) {
                  const previousStop = [
                    e.keyframe?.props.lng,
                    e.keyframe?.props.lat,
                  ];
                  const nextStop = [
                    e.nextKeyframe?.props.lng,
                    e.nextKeyframe?.props.lat,
                  ];

                  const legDistance = turf.rhumbDistance(previousStop, nextStop);

                  const currentPosition = [e.props.lng, e.props.lat];

                  const percentLeftToNextStop =
                    turf.rhumbDistance(currentPosition, nextStop) / legDistance;

                  const scale = Math.sin(percentLeftToNextStop * Math.PI) * 500;

                  const zoomAlpha = Math.sin(percentLeftToNextStop * Math.PI);
                  const zoom = lerp(atAirportZoom, midAirZoom, zoomAlpha);

                  map.setZoom(zoom || map.getZoom());

                  map.setBearing((1 - e.currentDelta) * 360);

                  plane.modify({
                    heading,
                    lngLat: currentPosition,
                    scale,
                    altitude: 1000 * scale,
                  });
                }

                if (isBoatAnimation) {
                  map.setCenter(new maptilersdk.LngLat(e.props.lng, e.props.lat));
                  const boatPosition = turf.along(
                    boatJourneyData.features[0],
                    boatJourneyLength * e.currentDelta,
                    { units: "kilometers" }
                  );
                  const nextBoatPosition = turf.along(
                    boatJourneyData.features[0],
                    boatJourneyLength * (e.currentDelta + 0.005),
                    { units: "kilometers" }
                  );

                  const boatHeading =
                    turf.bearing(
                      [
                        boatPosition.geometry.coordinates[0],
                        boatPosition.geometry.coordinates[1],
                      ],
                      [
                        nextBoatPosition.geometry.coordinates[0],
                        nextBoatPosition.geometry.coordinates[1],
                      ]
                    ) + 180;

                  const scale = Math.sin(e.currentDelta * Math.PI) * 1000;

                  boat.modify({
                    heading: boatHeading,
                    lngLat: [
                      boatPosition.geometry.coordinates[0],
                      boatPosition.geometry.coordinates[1],
                    ],
                    scale,
                  });
                }

                if (isCarAnimation) {
                  map.setCenter(new maptilersdk.LngLat(e.props.lng, e.props.lat));

                  const carPosition = turf.along(
                    carJourneyData.features[0].geometry,
                    carJourneyLength * e.currentDelta,
                    { units: "kilometers" }
                  );
                  const nextCarPosition = turf.along(
                    carJourneyData.features[0].geometry,
                    carJourneyLength * (e.currentDelta + 0.01),
                    { units: "kilometers" }
                  );

                  const carHeading =
                    turf.bearing(
                      [
                        carPosition.geometry.coordinates[0],
                        carPosition.geometry.coordinates[1],
                      ],
                      [
                        nextCarPosition.geometry.coordinates[0],
                        nextCarPosition.geometry.coordinates[1],
                      ]
                    ) + 180;

                  const scale = Math.sin(e.currentDelta * Math.PI) * 1000;

                  car.modify({
                    heading: carHeading, // because the car model is 180
                    lngLat: [
                      carPosition.geometry.coordinates[0],
                      carPosition.geometry.coordinates[1],
                    ],
                    scale,
                  });
                }
              }

              let isPlaying = false;
              document.getElementById("play-button")?.addEventListener("click", () => {
                if (isPlaying) {
                  currentAnimation?.pause();
                  isPlaying = false;
                } else {
                  currentAnimation?.play();
                  isPlaying = true;
                }
              });

            });

            //#region Helper Functions / types
            function lerp(a, b, t) {
              return a + (b - a) * t;
            }

            async function fetchGeoJSONAndAddAsLayer(id, url, map) {
              try {
                const data = await fetch(url).then((response) => response.json());
                addSourceAndLayer(map, id, {
                  type: "geojson",
                  data,
                  lineMetrics: true,
                });
                return data;
              } catch (error) {
                throw error;
              }
            }

            function addSourceAndLayer(
              map,
              id,
              source
            ) {
              map.addSource(id, source);
              map.addLayer(
                {
                  source: id,
                  id: `${id}-layer`,
                  type: "line",
                  layout: {
                    visibility: "visible",
                    "line-sort-key": 1,
                  },
                  paint: {
                    "line-color": "transparent",
                    "line-width": 10,
                  },
                },
                "3d-layer"
              );
            }
    </script>
</body>
</html>
```
