# Source: https://docs.maptiler.com/sdk-js/examples/custom-controls-programmatic/

# MapTiler custom controls

Adding a custom control programmatically allows developers to have more control is ideal for applications that require dynamic logic, event-driven behaviour, or a deeper integration with a framework like React.

Programmatic controls allow developers to register custom control elements manually by calling `map.addControl()` and providing a control implementation. Custom controls are instantiated using the `MaptilerCustomControl` class. The element that should be used can be provided either as the **element itself**, or as its **CSS selector**.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element to render the map
      style: maptilersdk.MapStyle.STREETS,
      navigationControl: false,
      geolocateControl: false,
      terrainExaggeration: 4,
    });
    
    //custom navigation controls
    const compassControlElement = document.querySelector(".compass-control");
    const navigationControl = new maptilersdk.MaptilerCustomControl(
      ".navigation-controls",
      (map, _, event) => {
        if ((event.target).closest(".zoom-in-control")) {
          map.zoomIn();
        }
      },
      (map) => {
        (compassControlElement.firstElementChild).style.transform = `rotateX(${String(map.getPitch())}deg) rotateZ(${String(-map.getBearing())}deg)`;
      },
    );
    map.addControl(navigationControl);
    document.querySelector(".zoom-out-control")?.addEventListener("click", () => map.zoomOut());
    compassControlElement.addEventListener("click", () => map.resetNorthPitch());

    //custom projection control
    function toggleProjection() {
      if (map.isGlobeProjection()) {
        map.setProjection({ type: "mercator" });
      } else {
        map.setProjection({ type: "globe" });
      }
    }
    const projectionControlElement = document.querySelector(".projection-control");
    const projectionControl = new maptilersdk.MaptilerCustomControl(projectionControlElement, toggleProjection, (map, element) => {
      element.firstElementChild.textContent = map.isGlobeProjection() ? "map" : "globe";
      element.title = map.isGlobeProjection() ? "Switch to Mercator projection" : "Switch to Globe projection";
    });
    map.addControl(projectionControl, "top-left");

    //custom terrain control
    function toggleTerrain() {
      if (map.hasTerrain()) {
        map.disableTerrain();
      } else {
        map.enableTerrain();
      }
    }
    const terrainControlElement = document.createElement("div");
    terrainControlElement.className = "btn btn-success m-2 terrain-control";
    const terrainControlIcon = document.createElement("span");
    terrainControlIcon.textContent = "terrain";
    terrainControlIcon.classList.add("material-symbols-outlined");
    terrainControlElement.appendChild(terrainControlIcon);
    const terrainControl = new maptilersdk.MaptilerCustomControl(terrainControlElement, toggleTerrain, (map) => {
      terrainControlIcon.classList.toggle("icon-fill", map.hasTerrain());
      terrainControlElement.title = map.hasTerrain() ? "Turn off Terrain" : "Turn on Terrain";
    });
    map.addControl(terrainControl, "top-left");

    //custom control (center map)
    const home = { lng: 15.4, lat: 49.8 };
    map.addControl(
      new maptilersdk.MaptilerCustomControl(
        ".home-button",
        (map) => {
          map.easeTo({ center: home, zoom: 7 });
        },
        (map, element) => {
          const center = map.getCenter();
          const zoom = map.getZoom();
          (element.firstElementChild).classList.toggle(
            "icon-fill",
            Math.abs(center.lng - home.lng) < Math.max(0, zoom - 6.8) * 1.5 && Math.abs(center.lat - home.lat) < Math.max(0, zoom - 6.8) / 2,
          );
        },
      ),
      "bottom-right",
    );
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>MapTiler custom controls</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" />
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:FILL@0..1" rel="stylesheet" />
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
            center: [0, 0],
            zoom: 7 });
        });

        container: 'map', // container's id or the HTML element to render the map
              style: maptilersdk.MapStyle.STREETS,
              navigationControl: false,
              geolocateControl: false,
              terrainExaggeration: 4,
            });

            //custom navigation controls
            const compassControlElement = document.querySelector(".compass-control");
            const navigationControl = new maptilersdk.MaptilerCustomControl(
              ".navigation-controls",
              (map, _, event) => {
                if ((event.target).closest(".zoom-in-control")) {
                  map.zoomIn();
                }
              },
              (map) => {
                (compassControlElement.firstElementChild).style.transform = `rotateX(${String(map.getPitch())}deg) rotateZ(${String(-map.getBearing())}deg)`;
              },
            );
            map.addControl(navigationControl);
            document.querySelector(".zoom-out-control")?.addEventListener("click", () => map.zoomOut());
            compassControlElement.addEventListener("click", () => map.resetNorthPitch());

            //custom projection control
            function toggleProjection() {
              if (map.isGlobeProjection()) {
                map.setProjection({ type: "mercator" });
              } else {
                map.setProjection({ type: "globe" });
              }
            }
            const projectionControlElement = document.querySelector(".projection-control");
            const projectionControl = new maptilersdk.MaptilerCustomControl(projectionControlElement, toggleProjection, (map, element) => {
              element.firstElementChild.textContent = map.isGlobeProjection() ? "map" : "globe";
              element.title = map.isGlobeProjection() ? "Switch to Mercator projection" : "Switch to Globe projection";
            });
            map.addControl(projectionControl, "top-left");

            //custom terrain control
            function toggleTerrain() {
              if (map.hasTerrain()) {
                map.disableTerrain();
              } else {
                map.enableTerrain();
              }
            }
            const terrainControlElement = document.createElement("div");
            terrainControlElement.className = "btn btn-success m-2 terrain-control";
            const terrainControlIcon = document.createElement("span");
            terrainControlIcon.textContent = "terrain";
            terrainControlIcon.classList.add("material-symbols-outlined");
            terrainControlElement.appendChild(terrainControlIcon);
            const terrainControl = new maptilersdk.MaptilerCustomControl(terrainControlElement, toggleTerrain, (map) => {
              terrainControlIcon.classList.toggle("icon-fill", map.hasTerrain());
              terrainControlElement.title = map.hasTerrain() ? "Turn off Terrain" : "Turn on Terrain";
            });
            map.addControl(terrainControl, "top-left");

            //custom control (center map)
            const home = { lng: 15.4, lat: 49.8 };
            map.addControl(
              new maptilersdk.MaptilerCustomControl(
                ".home-button",
                (map) => {
                  map.easeTo({ center: home, zoom: 7 });
                },
                (map, element) => {
                  const center = map.getCenter();
                  const zoom = map.getZoom();
                  (element.firstElementChild).classList.toggle(
                    "icon-fill",
                    Math.abs(center.lng - home.lng) < Math.max(0, zoom - 6.8) * 1.5 && Math.abs(center.lat - home.lat) < Math.max(0, zoom - 6.8) / 2,
                  );
                },
              ),
              "bottom-right",
            );
    </script>
</body>
</html>
```
