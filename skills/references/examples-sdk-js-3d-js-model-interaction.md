# Source: https://docs.maptiler.com/sdk-js/examples/3d-js-model-interaction/

# MapTiler 3D | Item3D UI States

Explore a dynamic 3D urban environment where buildings come to life. Hover over architectural layers to see smooth animations, highlighting, and detailed information in this advanced MapTiler 3D SDK demonstration.

This demonstration showcases the advanced capabilities of the MapTiler 3D SDK in creating immersive and reactive urban environments.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
// Waiting for the map to be ready
    map.on('ready', async () => {

      // Hide default 3D buildings to replace them with our models
      hideBuildingsInPolygon(map);

      // Add 3D Layer
      const layer3D = new maptiler3d.Layer3D("xx-dev");
      map.addLayer(layer3D);

      // Lights
      layer3D.setAmbientLight({ intensity: 8 });
      layer3D.addPointLight("point-light", {
        intensity: 10,
        altitude: 5000,
        lngLat: center,
        altitudeReference: maptiler3d.AltitudeReference.MEAN_SEA_LEVEL,
      });
      layer3D.addPointLight("point-light-2", {
        intensity: 10,
        altitude: 5000,
        lngLat: [-0.016979498863220217, -0.05109624562642054],
        altitudeReference: maptiler3d.AltitudeReference.MEAN_SEA_LEVEL,
      });

      // Load general buildings
      for (const building of buildings) {
        const buildingItem3D = await layer3D.addMeshFromURL(
          building.model,
          `https://docs-media.maptiler.com/docs/models/buildings/${building.model}`,
          {
            lngLat: building.center,
            altitude: building.altitude || 0,
            heading: 20,
            scale: 0.6,
            altitudeReference: maptiler3d.AltitudeReference.GROUND,
          }
        );

        // Add Markers
        const markerElement = document.getElementById(building.markerId);

        const buildingMarker = new maptilersdk.Marker({ element: markerElement, subpixelPositioning: true, })
          .setLngLat(building.center)
          .setPopup(new maptilersdk.Popup({ offset: [0, -30] })
            .setHTML(`<h3>${building.title}</h3><p>${building.description}</p>`))
          .addTo(map);

        // Interaction
        buildingItem3D.mesh?.traverse((child) => {
          if (child.isMesh) {
            child.material.map = null;
            child.material.color.set(originalColor);
          }
        });

        buildingItem3D.on("mouseenter", () => {
          buildingItem3D.mesh?.traverse((child) => {
            if (child.isMesh) {
              child.material.color.set(new THREE.Color(building.hoverColor));
            }
          });
        });

        buildingItem3D.on("mouseleave", () => {
          buildingItem3D.mesh?.traverse((child) => {
            if (child.isMesh) child.material.color.set(originalColor);
          });
        });

      }

      // Special: Luxury Apartment with animated floors
      const numFloorsInApartment = 10;
      const floorAnimationManager = new FloorAnimationManager();

      const apartmentFloorBase = await layer3D.addMeshFromURL(
        "apartment-floor",
        `https://docs-media.maptiler.com/docs/models/buildings/apartment-floor.glb`,
        {
          lngLat: [16.978970468042007, 51.09669537637524],
          altitude: 0,
          heading: 20,
          scale: 0.75,
          altitudeReference: maptiler3d.AltitudeReference.GROUND,
          opacity: 0.5,
        }
      );

      // Marker for Luxury Apartment
      new maptilersdk.Marker({ element: document.getElementById("luxury-apartment-marker") })
        .setLngLat([16.978656377757375, 51.09634493829725])
        .setPopup(new maptilersdk.Popup({ offset: [0, -30] })
          .setHTML(`<h3>Luxury Apartment</h3><p>A luxury apartment with 3 bedrooms and 2 bathrooms.</p>`))
        .addTo(map);

      // Create floors
      for (let i = 0; i < numFloorsInApartment; i++) {
        const newFloor = apartmentFloorBase.clone(`apartment-floor-${i}`);
        newFloor.setAltitude(0.65 * i * 10);
        floorAnimationManager.addFloor(newFloor);

        newFloor.on("mouseenter", () => floorAnimationManager.setActiveFloor(newFloor));
        newFloor.on("mouseleave", () => {
          if (floorAnimationManager.getActiveFloor() === newFloor) {
            floorAnimationManager.setActiveFloor(null);
          }
        });
      }

      // Add Roof
      await layer3D.addMeshFromURL(
        "apartment-roof",
        `https://docs-media.maptiler.com/docs/models/buildings/apartment-roof.glb`,
        {
          lngLat: [16.978962032459123, 51.09671170177478],
          altitude: numFloorsInApartment * 0.65 * 10 - 1,
          heading: 20,
          scale: 0.76,
          opacity: 0.2,
          altitudeReference: maptiler3d.AltitudeReference.GROUND,
        }
      );

      floorAnimationManager.animate();
    });

    function replaceLayerSource(map, layerId, newSourceId) {
      const style = map.getStyle();

      const layer = style.layers.find(l => l.id === layerId);
      if (!layer) {
        throw new Error(`Layer ${layerId} no existe`);
      }

      const layerIndex = style.layers.findIndex(l => l.id === layerId);
      const beforeLayerId = style.layers[layerIndex + 1]?.id;

      const newLayer = JSON.parse(JSON.stringify(layer));

      newLayer.source = newSourceId;

      map.removeLayer(layerId);

      map.addLayer(newLayer, beforeLayerId);
    }

    function hideBuildingsInPolygon(map) {

      //use MapTiler building source for buildings IDs
      map.addSource("buildings", {
        type: "vector",
        url: "https://api.maptiler.com/tiles/buildings/tiles.json",
      });

      replaceLayerSource(map, "Building 3D", "buildings");

      // Simple building filter to hide existing map buildings in this area
      const internalBuildingIds = ["3229742242", "3229937730", "3229844962", "3230119458",
        "3230021218", "3229314786", "3229333346", "3229530402", "3229295266", "3229567618",
        "3229911586", "3229729666", "3229348162", "3229797666", "3229905506", "3229957698",
        "3229844066"];
      map.setFilter("Building 3D", [
        "match",
        ["to-string", ["id"]],
        internalBuildingIds,
        false,
        true,
      ]);
    }
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>MapTiler 3D | Item3D UI States</title>
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
            style: maptilersdk.MapStyle.STREETS,
            center: [16.980518102645874, 51.09648818873717],
            zoom: 18,
            pitch: 60,
            bearing: 55
        });

        // Waiting for the map to be ready
            map.on('ready', async () => {

              // Hide default 3D buildings to replace them with our models
              hideBuildingsInPolygon(map);

              // Add 3D Layer
              const layer3D = new maptiler3d.Layer3D("xx-dev");
              map.addLayer(layer3D);

              // Lights
              layer3D.setAmbientLight({ intensity: 8 });
              layer3D.addPointLight("point-light", {
                intensity: 10,
                altitude: 5000,
                lngLat: center,
                altitudeReference: maptiler3d.AltitudeReference.MEAN_SEA_LEVEL,
              });
              layer3D.addPointLight("point-light-2", {
                intensity: 10,
                altitude: 5000,
                lngLat: [-0.016979498863220217, -0.05109624562642054],
                altitudeReference: maptiler3d.AltitudeReference.MEAN_SEA_LEVEL,
              });

              // Load general buildings
              for (const building of buildings) {
                const buildingItem3D = await layer3D.addMeshFromURL(
                  building.model,
                  `https://docs-media.maptiler.com/docs/models/buildings/${building.model}`,
                  {
                    lngLat: building.center,
                    altitude: building.altitude || 0,
                    heading: 20,
                    scale: 0.6,
                    altitudeReference: maptiler3d.AltitudeReference.GROUND,
                  }
                );

                // Add Markers
                const markerElement = document.getElementById(building.markerId);

                const buildingMarker = new maptilersdk.Marker({ element: markerElement, subpixelPositioning: true, })
                  .setLngLat(building.center)
                  .setPopup(new maptilersdk.Popup({ offset: [0, -30] })
                    .setHTML(`<h3>${building.title}</h3><p>${building.description}</p>`))
                  .addTo(map);

                // Interaction
                buildingItem3D.mesh?.traverse((child) => {
                  if (child.isMesh) {
                    child.material.map = null;
                    child.material.color.set(originalColor);
                  }
                });

                buildingItem3D.on("mouseenter", () => {
                  buildingItem3D.mesh?.traverse((child) => {
                    if (child.isMesh) {
                      child.material.color.set(new THREE.Color(building.hoverColor));
                    }
                  });
                });

                buildingItem3D.on("mouseleave", () => {
                  buildingItem3D.mesh?.traverse((child) => {
                    if (child.isMesh) child.material.color.set(originalColor);
                  });
                });

              }

              // Special: Luxury Apartment with animated floors
              const numFloorsInApartment = 10;
              const floorAnimationManager = new FloorAnimationManager();

              const apartmentFloorBase = await layer3D.addMeshFromURL(
                "apartment-floor",
                `https://docs-media.maptiler.com/docs/models/buildings/apartment-floor.glb`,
                {
                  lngLat: [16.978970468042007, 51.09669537637524],
                  altitude: 0,
                  heading: 20,
                  scale: 0.75,
                  altitudeReference: maptiler3d.AltitudeReference.GROUND,
                  opacity: 0.5,
                }
              );

              // Marker for Luxury Apartment
              new maptilersdk.Marker({ element: document.getElementById("luxury-apartment-marker") })
                .setLngLat([16.978656377757375, 51.09634493829725])
                .setPopup(new maptilersdk.Popup({ offset: [0, -30] })
                  .setHTML(`<h3>Luxury Apartment</h3><p>A luxury apartment with 3 bedrooms and 2 bathrooms.</p>`))
                .addTo(map);

              // Create floors
              for (let i = 0; i < numFloorsInApartment; i++) {
                const newFloor = apartmentFloorBase.clone(`apartment-floor-${i}`);
                newFloor.setAltitude(0.65 * i * 10);
                floorAnimationManager.addFloor(newFloor);

                newFloor.on("mouseenter", () => floorAnimationManager.setActiveFloor(newFloor));
                newFloor.on("mouseleave", () => {
                  if (floorAnimationManager.getActiveFloor() === newFloor) {
                    floorAnimationManager.setActiveFloor(null);
                  }
                });
              }

              // Add Roof
              await layer3D.addMeshFromURL(
                "apartment-roof",
                `https://docs-media.maptiler.com/docs/models/buildings/apartment-roof.glb`,
                {
                  lngLat: [16.978962032459123, 51.09671170177478],
                  altitude: numFloorsInApartment * 0.65 * 10 - 1,
                  heading: 20,
                  scale: 0.76,
                  opacity: 0.2,
                  altitudeReference: maptiler3d.AltitudeReference.GROUND,
                }
              );

              floorAnimationManager.animate();
            });

            function replaceLayerSource(map, layerId, newSourceId) {
              const style = map.getStyle();

              const layer = style.layers.find(l => l.id === layerId);
              if (!layer) {
                throw new Error(`Layer ${layerId} no existe`);
              }

              const layerIndex = style.layers.findIndex(l => l.id === layerId);
              const beforeLayerId = style.layers[layerIndex + 1]?.id;

              const newLayer = JSON.parse(JSON.stringify(layer));

              newLayer.source = newSourceId;

              map.removeLayer(layerId);

              map.addLayer(newLayer, beforeLayerId);
            }

            function hideBuildingsInPolygon(map) {

              //use MapTiler building source for buildings IDs
              map.addSource("buildings", {
                type: "vector",
                url: "https://api.maptiler.com/tiles/buildings/tiles.json",
              });

              replaceLayerSource(map, "Building 3D", "buildings");

              // Simple building filter to hide existing map buildings in this area
              const internalBuildingIds = ["3229742242", "3229937730", "3229844962", "3230119458",
                "3230021218", "3229314786", "3229333346", "3229530402", "3229295266", "3229567618",
                "3229911586", "3229729666", "3229348162", "3229797666", "3229905506", "3229957698",
                "3229844066"];
              map.setFilter("Building 3D", [
                "match",
                ["to-string", ["id"]],
                internalBuildingIds,
                false,
                true,
              ]);
            }
    </script>
</body>
</html>
```
