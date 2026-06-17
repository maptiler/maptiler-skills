# Source: https://docs.maptiler.com/sdk-js/examples/marker-layout-many/

# MapTiler Marker Layout

Create custom non-colliding marker overlays on your map using the [Marker Layout](/sdk-js/modules/marker-layout/) on top of MapTiler SDK.

This example shows how to display the information from the city and town label layers. In this case, we are not applying any filters because we want to create as many markers as possible. To improve performance, we will *soft update* the markers when the user moves the map and complete the update once the user stops moving the map.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
// Creating the div that will contain all the markers
      const markerContainer = document.createElement("div");
      appContainer.appendChild(markerContainer);

      (async () => {
        await map.onReadyAsync();

        const markerManager = new maptilermarkerlayout.MarkerLayout(map, {
          layers: ["Capital city labels", "City labels", "Place labels", "Town labels"],
          markerSize: [140, 80],
          markerAnchor: "top",
          offset: [0, -8], // so that the tip of the marker bottom pin lands on the city dot
          sortingProperty: "rank",

          // no filtering so that we get as many features as possible
        });

        // This object contains the marker DIV so that they can be updated rather than fully recreated every time
        const markerLogicContainer = {};

        let markerStatus = null;

        // This function will be used as the callback for some map events
        const updateMarkers = () => {
          markerStatus = markerManager.update();

          if (!markerStatus) return;

          // Remove the div that corresponds to removed markers
          markerStatus.removed.forEach((abstractMarker) => {
            const markerDiv = markerLogicContainer[abstractMarker.id];
            delete markerLogicContainer[abstractMarker.id];
            markerContainer.removeChild(markerDiv);
          });

          // Update the div that corresponds to updated markers
          markerStatus.updated.forEach((abstractMarker) => {
            const markerDiv = markerLogicContainer[abstractMarker.id];
            updateMarkerDiv(abstractMarker, markerDiv);
          });

          // Create the div that corresponds to the new markers
          markerStatus.new.forEach((abstractMarker) => {
            const markerDiv = makeMarker(abstractMarker);
            markerLogicContainer[abstractMarker.id] = markerDiv;
            markerContainer.appendChild(markerDiv);
          });
        }

        const softUpdateMarkers = () => {
          // A previous run of .update() yieding no result or not being ran at all
          // would stop the soft update
          if (!markerStatus) return;

          markerStatus.updated.forEach((abstractMarker) => {
            markerManager.softUpdateAbstractMarker(abstractMarker);
            const markerDiv = markerLogicContainer[abstractMarker.id];
            updateMarkerDiv(abstractMarker, markerDiv);
          })

          markerStatus.new.forEach((abstractMarker) => {
            markerManager.softUpdateAbstractMarker(abstractMarker);
            const markerDiv = markerLogicContainer[abstractMarker.id];
            updateMarkerDiv(abstractMarker, markerDiv);
          })
        }

        // While moving the map, this event is triggered many times per seconds
        // so we only perform a soft update (that could be debounced)
        map.on("move", softUpdateMarkers);

        // When done moving, we perform a full update
        map.on("moveend", updateMarkers)

        // Full update at init
        updateMarkers();
      })()


    function makeMarker(abstractMarker) {

      const marker = document.createElement("div");
      marker.classList.add("marker");
      marker.classList.add('fade-in-animation');
      marker.style.setProperty("width", `${abstractMarker.size[0]}px`);
      marker.style.setProperty("height", `${abstractMarker.size[1]}px`);
      marker.style.setProperty("transform", `translate(${abstractMarker.position[0]}px, ${abstractMarker.position[1]}px)`);

      const feature = abstractMarker.features[0];

      marker.innerHTML = `
        <div class="markerPointy"></div>
        <div class="markerBody">
          
          <div class="markerTop">
            ${feature.properties["name:en"] || feature.properties["name"]}
          </div>
          
          <div class="markerBottom">
            <ul>
              <li><b>Name:</b> ${feature.properties.name}</li>
              <li><b>Class:</b> ${feature.properties.class}</li>
              <li><b>Rank:</b> ${feature.properties.rank}</li>
            </ul>
          </div>
        </div>
      `
      return marker;
    }

    function updateMarkerDiv(abstractMarker, marker) {
      marker.style.setProperty("width", `${abstractMarker.size[0]}px`);
      marker.style.setProperty("height", `${abstractMarker.size[1]}px`);
      marker.style.setProperty("transform", `translate(${abstractMarker.position[0]}px, ${abstractMarker.position[1]}px)`);
    }
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>MapTiler Marker Layout</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <script src="https://cdn.maptiler.com/maptiler-marker-layout/v2.0.1/maptiler-marker-layout.umd.min.js"></script>
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
            center: [13.3608, 52.5478],
            zoom: 9.14
        });

        // Creating the div that will contain all the markers
              const markerContainer = document.createElement("div");
              appContainer.appendChild(markerContainer);

              (async () => {
                await map.onReadyAsync();

                const markerManager = new maptilermarkerlayout.MarkerLayout(map, {
                  layers: ["Capital city labels", "City labels", "Place labels", "Town labels"],
                  markerSize: [140, 80],
                  markerAnchor: "top",
                  offset: [0, -8], // so that the tip of the marker bottom pin lands on the city dot
                  sortingProperty: "rank",

                  // no filtering so that we get as many features as possible
                });

                // This object contains the marker DIV so that they can be updated rather than fully recreated every time
                const markerLogicContainer = {};

                let markerStatus = null;

                // This function will be used as the callback for some map events
                const updateMarkers = () => {
                  markerStatus = markerManager.update();

                  if (!markerStatus) return;

                  // Remove the div that corresponds to removed markers
                  markerStatus.removed.forEach((abstractMarker) => {
                    const markerDiv = markerLogicContainer[abstractMarker.id];
                    delete markerLogicContainer[abstractMarker.id];
                    markerContainer.removeChild(markerDiv);
                  });

                  // Update the div that corresponds to updated markers
                  markerStatus.updated.forEach((abstractMarker) => {
                    const markerDiv = markerLogicContainer[abstractMarker.id];
                    updateMarkerDiv(abstractMarker, markerDiv);
                  });

                  // Create the div that corresponds to the new markers
                  markerStatus.new.forEach((abstractMarker) => {
                    const markerDiv = makeMarker(abstractMarker);
                    markerLogicContainer[abstractMarker.id] = markerDiv;
                    markerContainer.appendChild(markerDiv);
                  });
                }

                const softUpdateMarkers = () => {
                  // A previous run of .update() yieding no result or not being ran at all
                  // would stop the soft update
                  if (!markerStatus) return;

                  markerStatus.updated.forEach((abstractMarker) => {
                    markerManager.softUpdateAbstractMarker(abstractMarker);
                    const markerDiv = markerLogicContainer[abstractMarker.id];
                    updateMarkerDiv(abstractMarker, markerDiv);
                  })

                  markerStatus.new.forEach((abstractMarker) => {
                    markerManager.softUpdateAbstractMarker(abstractMarker);
                    const markerDiv = markerLogicContainer[abstractMarker.id];
                    updateMarkerDiv(abstractMarker, markerDiv);
                  })
                }

                // While moving the map, this event is triggered many times per seconds
                // so we only perform a soft update (that could be debounced)
                map.on("move", softUpdateMarkers);

                // When done moving, we perform a full update
                map.on("moveend", updateMarkers)

                // Full update at init
                updateMarkers();
              })()


            function makeMarker(abstractMarker) {

              const marker = document.createElement("div");
              marker.classList.add("marker");
              marker.classList.add('fade-in-animation');
              marker.style.setProperty("width", `${abstractMarker.size[0]}px`);
              marker.style.setProperty("height", `${abstractMarker.size[1]}px`);
              marker.style.setProperty("transform", `translate(${abstractMarker.position[0]}px, ${abstractMarker.position[1]}px)`);

              const feature = abstractMarker.features[0];

              marker.innerHTML = `
                <div class="markerPointy"></div>
                <div class="markerBody">

                  <div class="markerTop">
                    ${feature.properties["name:en"] || feature.properties["name"]}
                  </div>

                  <div class="markerBottom">
                    <ul>
                      <li><b>Name:</b> ${feature.properties.name}</li>
                      <li><b>Class:</b> ${feature.properties.class}</li>
                      <li><b>Rank:</b> ${feature.properties.rank}</li>
                    </ul>
                  </div>
                </div>
              `
              return marker;
            }

            function updateMarkerDiv(abstractMarker, marker) {
              marker.style.setProperty("width", `${abstractMarker.size[0]}px`);
              marker.style.setProperty("height", `${abstractMarker.size[1]}px`);
              marker.style.setProperty("transform", `translate(${abstractMarker.position[0]}px, ${abstractMarker.position[1]}px)`);
            }
    </script>
</body>
</html>
```
