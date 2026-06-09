# Source: https://docs.maptiler.com/sdk-js/examples/marker-layout-basic/

# MapTiler Marker Layout

Create non-colliding marker overlays to display the information from the city and town label layers. The [Marker Layout](/sdk-js/modules/marker-layout/) is a helper to create non-colliding marker overlays on top of MapTiler SDK.

In this example, we are using the `filter` function to only create markers in features of type `"city"`, `"village"` or `"town"`.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
// Creating the div that will contain all the markers
    const markerContainer = document.createElement("div");
    appContainer.appendChild(markerContainer);

    (async () => {
      await map.onReadyAsync();

      const markerManager = new maptilermarkerlayout.MarkerLayout(map, {
        layers: ["City labels", "Place labels", "Town labels"],
        markerSize: [140, 80],
        markerAnchor: "top",
        offset: [0, -8], // so that the tip of the marker bottom pin lands on the city dot
        sortingProperty: "rank",

        // With `sortingProperty` option as a function, the following is equivalent to the above
        // sortingProperty: (feature) => {
        //   return feature.properties.rank;
        // },

        filter: ((feature) => {
          if (["City labels", "Town labels"].includes(feature.layer.id)) {
            return true;
          } else {
            return ["village"].includes(feature.properties.class)
          }
        })
      });


      // This object contains the marker DIV so that they can be updated rather than fully recreated every time
      const markerLogicContainer = {};

      // This function will be used as the callback for some map events
      const updateMarkers = () => {
        const markerStatus = markerManager.update();

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

      // The "idle" event is triggered every second because of the particle layer being refreshed,
      // even though their is no new data loaded, so this approach proved to be the best for this scenario
      map.on("move", updateMarkers);

      map.on("moveend", () => {
        map.once("idle", updateMarkers);
      })

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
            center: [0, 0],
            zoom: 0
        });

        // Creating the div that will contain all the markers
            const markerContainer = document.createElement("div");
            appContainer.appendChild(markerContainer);

            (async () => {
              await map.onReadyAsync();

              const markerManager = new maptilermarkerlayout.MarkerLayout(map, {
                layers: ["City labels", "Place labels", "Town labels"],
                markerSize: [140, 80],
                markerAnchor: "top",
                offset: [0, -8], // so that the tip of the marker bottom pin lands on the city dot
                sortingProperty: "rank",

                // With `sortingProperty` option as a function, the following is equivalent to the above
                // sortingProperty: (feature) => {
                //   return feature.properties.rank;
                // },

                filter: ((feature) => {
                  if (["City labels", "Town labels"].includes(feature.layer.id)) {
                    return true;
                  } else {
                    return ["village"].includes(feature.properties.class)
                  }
                })
              });


              // This object contains the marker DIV so that they can be updated rather than fully recreated every time
              const markerLogicContainer = {};

              // This function will be used as the callback for some map events
              const updateMarkers = () => {
                const markerStatus = markerManager.update();

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

              // The "idle" event is triggered every second because of the particle layer being refreshed,
              // even though their is no new data loaded, so this approach proved to be the best for this scenario
              map.on("move", updateMarkers);

              map.on("moveend", () => {
                map.once("idle", updateMarkers);
              })

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
