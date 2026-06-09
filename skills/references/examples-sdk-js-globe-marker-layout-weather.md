# Source: https://docs.maptiler.com/sdk-js/examples/globe-marker-layout-weather/

# MapTiler Globe projection

Create a weather globe map using the [Marker Layout](/sdk-js/modules/marker-layout/) to show your custom weather markers icons, animated SVGs or Lotties. In this example, we use the MapTiler SDK together with the [MapTiler Weather library](/sdk-js/modules/weather/).

This example shows how to obtain the information from the MapTiler Weather layers to create a weather map where the icons corresponding to the current state of the weather in the main cities are shown. This example demonstrates the use of custom markers with content sourced from external data.

For this demo, we used [Meteocons](https://bas.dev/work/meteocons), a weather icon pack designed by Bas Milius also available on [GitHub](https://github.com/basmilius/weather-icons).

**Lottie** is a file format for vector graphics animation. They can be scaled without pixelation or loss of quality, just like an SVG file. It is intended as a lighter alternative to animated GIFs and APNG files for use in the web and mobile and desktop applications. Read more about [Lottie file format](https://en.wikipedia.org/wiki/Lottie_(file_format)).

> [!WARNING]

> The Weather JS module **can only** be used with the [MapTiler SDK](/sdk-js/).

> To **visualize** the layers of the Weather JS module, you must use the **[MapTiler SDK v2.x](/sdk-js/)**.

> We are working on adapting the weather module to work with v3 of the SDK and to be able to have weather visualizations on a 3D globe.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const appContainer = document.getElementById('map');
      container: appContainer, // container's id or the HTML element to render the map
      style:  maptilersdk.MapStyle.BASIC,
      center: [45, 25], // starting position [lng, lat]
      zoom: 2.5, // starting zoom
      projection: 'globe' //enable globe projection
    });

    // Creating the div that will contain all the markers
    const markerContainer = document.createElement("div");
    appContainer.appendChild(markerContainer);

    (async () => {
      // Waiting that the map is "loaded"
      // (this is equivalent to putting the rest of the code the "load" event callback)
      await map.onReadyAsync();

      // The marker manager is in charge of computing the positions where markers
      // should be, sort them by POI rank and select non-overlaping places.
      // (it does not actually create DOM elements, it just uses logical points and bounding boxes)
      const markerManager = new maptilermarkerlayout.MarkerLayout(map, {
        layers: ["Country labels", "City labels", "Place labels"],
        markerSize: [40, 70],
        offset: [0, -10],
        markerAnchor: "center",
        filter: (feature) => {
          return ["country", "city", "village", "town"].includes(
            feature.properties.class
          );
        },
      });

      // Creating the weather layers...
      // Temperature will be using the NULL color ramp
      const temperatureLayer = new maptilerweather.TemperatureLayer({
        colorramp: maptilerweather.ColorRamp.builtin.NULL,
      });

      // Radar will be using the NULL color ramp
      const radarLayer = new maptilerweather.RadarLayer({
        colorramp: maptilerweather.ColorRamp.builtin.NULL,
      });

      // From the wind layer, we only display the particles (the background is using the NULL color ramp, which is transparent).
      // The particles are transparent
      const windLayer = new maptilerweather.WindLayer({
        colorramp: maptilerweather.ColorRamp.builtin.NULL,
        color: [255, 255, 255, 0],
        fastColor: [255, 255, 255, 0],
      });

      // The precispitation layer is created but actually not displayed.
      // It will only be used for picking precipitation metrics at the locations of the markers
      const precipitationLayer = new maptilerweather.PrecipitationLayer({
        colorramp: maptilerweather.ColorRamp.builtin.NULL,
      });

      // Setting the water layer partially transparent to increase the visual separation between land and water
      //map.setPaintProperty("Water", "fill-color", "rgba(0, 0, 0, 0.7)");
      map.addLayer(temperatureLayer, "Place labels");
      map.addLayer(windLayer);
      map.addLayer(radarLayer);
      map.addLayer(precipitationLayer);

      // Waiting for weather data readyness
      await temperatureLayer.onSourceReadyAsync();
      await radarLayer.onSourceReadyAsync();
      await windLayer.onSourceReadyAsync();
      await precipitationLayer.onSourceReadyAsync();

      // This object contains the marker DIV so that they can be updated rather than fully recreated every time
      const markerLogicContainer = {};

      let markerStatus = null;
      // This function will be used as the callback for some map events
      const updateMarkers = () => {
        markerStatus = markerManager.update();

        if (!markerStatus) return;

        // Remove the div that corresponds to removed markers
        markerStatus.removed.forEach((pb) => {
          const markerDiv = markerLogicContainer[pb.id];
          delete markerLogicContainer[pb.id];
          markerContainer.removeChild(markerDiv);
        });

        // Update the div that corresponds to updated markers
        markerStatus.updated.forEach((pb) => {
          const markerDiv = markerLogicContainer[pb.id];
          updateMarkerDiv(pb, markerDiv);
        });

        // Create the div that corresponds to the new markers
        markerStatus.new.forEach((pb) => {
          const markerDiv = makeMarker(
            pb,
            temperatureLayer,
            radarLayer,
            precipitationLayer,
            new Date()
          );
          markerLogicContainer[pb.id] = markerDiv;
          markerContainer.appendChild(markerDiv);
        });
      };

      const softUpdateMarkers = () => {
        // A previous run of .update() yieding no result or not being ran at all
        // would stop the soft update
        if (!markerStatus) return;

        markerStatus.updated.forEach((abstractMarker) => {
          markerManager.softUpdateAbstractMarker(abstractMarker);
          const markerDiv = markerLogicContainer[abstractMarker.id];
          updateMarkerDiv(abstractMarker, markerDiv);
        });

        markerStatus.new.forEach((abstractMarker) => {
          markerManager.softUpdateAbstractMarker(abstractMarker);
          const markerDiv = markerLogicContainer[abstractMarker.id];
          updateMarkerDiv(abstractMarker, markerDiv);
        });
      };

      // The "idle" event is triggered every second because of the particle layer being refreshed,
      // even though their is no new data loaded, so this approach proved to be the best for this scenario
      map.on("move", softUpdateMarkers);

      map.on("moveend", updateMarkers);

      map.once("idle", () => {
        setTimeout(() => {
          updateMarkers();
        }, 300);
      });
    })();

    function makeMarker(
      abstractMarker,
      temperatureLayer,
      radarLayer,
      precipitationLayer,
      date
    ) {
      const marker = document.createElement("div");
      marker.classList.add("marker");
      marker.classList.add("fade-in-animation");
      marker.style.setProperty("width", `${abstractMarker.size[0]}px`);
      marker.style.setProperty("height", `${abstractMarker.size[1]}px`);
      marker.style.setProperty(
        "transform",
        `translate(${abstractMarker.position[0]}px, ${abstractMarker.position[1]}px)`
      );

      const lonLat = abstractMarker.features[0].geometry.coordinates;
      const temperatureData = temperatureLayer.pickAt(lonLat[0], lonLat[1]);
      const precipitationData = precipitationLayer.pickAt(
        lonLat[0],
        lonLat[1]
      );

      const radarData = radarLayer.pickAt(lonLat[0], lonLat[1]);

      let mainWeatherIconURL = "https://docs.maptiler.com/sdk-js/examples/marker-layout-weather/weather-icons/";
      const radarDBz = radarData?.value || -20;
      const precipMmH = precipitationData?.value || 0;
      const temperatureDeg = temperatureData?.value || 0;
      const temperature = temperatureData?.value.toFixed(1);

      const sunPosition = SunCalc.getPosition(date, lonLat[1], lonLat[0]);

      if (sunPosition.altitude < 0) {
        mainWeatherIconURL += "night-";
      } else {
        mainWeatherIconURL += "day-";
      }

      if (radarDBz < 0) {
        if (precipMmH > 0.2) {
          mainWeatherIconURL += "cloudy-";
        } else {
          mainWeatherIconURL += "clear-";
        }
      } else if (radarDBz < 10) {
        mainWeatherIconURL += "cloudy-";
      } else if (radarDBz < 20) {
        mainWeatherIconURL += "overcast-";
      } else {
        mainWeatherIconURL += "extreme-";
      }

      if (precipMmH > 5) {
        mainWeatherIconURL += temperatureDeg < -1 ? "snow" : "rain";
      } else if (precipMmH > 0.2) {
        mainWeatherIconURL += temperatureDeg < -1 ? "snow" : "drizzle";
      } else {
        mainWeatherIconURL += "none";
      }

      mainWeatherIconURL += ".svg";

      marker.innerHTML = `
      <img class="markerMainWeatherIcon" src=${mainWeatherIconURL}></img>
      <div class="markerTemperature">${temperature ? `${temperature}°` : ''}</div>
      `;
      return marker;
    }

    function updateMarkerDiv(abstractMarker, marker) {
      marker.style.setProperty("width", `${abstractMarker.size[0]}px`);
      marker.style.setProperty("height", `${abstractMarker.size[1]}px`);
      marker.style.setProperty(
        "transform",
        `translate(${abstractMarker.position[0]}px, ${abstractMarker.position[1]}px)`
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
    <title>MapTiler Globe projection</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <script src="https://cdn.maptiler.com/maptiler-marker-layout/v2.0.1/maptiler-marker-layout.umd.min.js"></script>
    <script src="https://cdn.maptiler.com/maptiler-weather/3.1.1/maptiler-weather.umd.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/suncalc@1.9.0/suncalc.min.js"></script>
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
            style: maptilersdk.MapStyle.BASE,
            center: [45, 25],
            zoom: 2.5
        });

        const appContainer = document.getElementById('map');
              container: appContainer, // container's id or the HTML element to render the map
              style:  maptilersdk.MapStyle.BASIC,
              center: [45, 25], // starting position [lng, lat]
              zoom: 2.5, // starting zoom
              projection: 'globe' //enable globe projection
            });

            // Creating the div that will contain all the markers
            const markerContainer = document.createElement("div");
            appContainer.appendChild(markerContainer);

            (async () => {
              // Waiting that the map is "loaded"
              // (this is equivalent to putting the rest of the code the "load" event callback)
              await map.onReadyAsync();

              // The marker manager is in charge of computing the positions where markers
              // should be, sort them by POI rank and select non-overlaping places.
              // (it does not actually create DOM elements, it just uses logical points and bounding boxes)
              const markerManager = new maptilermarkerlayout.MarkerLayout(map, {
                layers: ["Country labels", "City labels", "Place labels"],
                markerSize: [40, 70],
                offset: [0, -10],
                markerAnchor: "center",
                filter: (feature) => {
                  return ["country", "city", "village", "town"].includes(
                    feature.properties.class
                  );
                },
              });

              // Creating the weather layers...
              // Temperature will be using the NULL color ramp
              const temperatureLayer = new maptilerweather.TemperatureLayer({
                colorramp: maptilerweather.ColorRamp.builtin.NULL,
              });

              // Radar will be using the NULL color ramp
              const radarLayer = new maptilerweather.RadarLayer({
                colorramp: maptilerweather.ColorRamp.builtin.NULL,
              });

              // From the wind layer, we only display the particles (the background is using the NULL color ramp, which is transparent).
              // The particles are transparent
              const windLayer = new maptilerweather.WindLayer({
                colorramp: maptilerweather.ColorRamp.builtin.NULL,
                color: [255, 255, 255, 0],
                fastColor: [255, 255, 255, 0],
              });

              // The precispitation layer is created but actually not displayed.
              // It will only be used for picking precipitation metrics at the locations of the markers
              const precipitationLayer = new maptilerweather.PrecipitationLayer({
                colorramp: maptilerweather.ColorRamp.builtin.NULL,
              });

              // Setting the water layer partially transparent to increase the visual separation between land and water
              //map.setPaintProperty("Water", "fill-color", "rgba(0, 0, 0, 0.7)");
              map.addLayer(temperatureLayer, "Place labels");
              map.addLayer(windLayer);
              map.addLayer(radarLayer);
              map.addLayer(precipitationLayer);

              // Waiting for weather data readyness
              await temperatureLayer.onSourceReadyAsync();
              await radarLayer.onSourceReadyAsync();
              await windLayer.onSourceReadyAsync();
              await precipitationLayer.onSourceReadyAsync();

              // This object contains the marker DIV so that they can be updated rather than fully recreated every time
              const markerLogicContainer = {};

              let markerStatus = null;
              // This function will be used as the callback for some map events
              const updateMarkers = () => {
                markerStatus = markerManager.update();

                if (!markerStatus) return;

                // Remove the div that corresponds to removed markers
                markerStatus.removed.forEach((pb) => {
                  const markerDiv = markerLogicContainer[pb.id];
                  delete markerLogicContainer[pb.id];
                  markerContainer.removeChild(markerDiv);
                });

                // Update the div that corresponds to updated markers
                markerStatus.updated.forEach((pb) => {
                  const markerDiv = markerLogicContainer[pb.id];
                  updateMarkerDiv(pb, markerDiv);
                });

                // Create the div that corresponds to the new markers
                markerStatus.new.forEach((pb) => {
                  const markerDiv = makeMarker(
                    pb,
                    temperatureLayer,
                    radarLayer,
                    precipitationLayer,
                    new Date()
                  );
                  markerLogicContainer[pb.id] = markerDiv;
                  markerContainer.appendChild(markerDiv);
                });
              };

              const softUpdateMarkers = () => {
                // A previous run of .update() yieding no result or not being ran at all
                // would stop the soft update
                if (!markerStatus) return;

                markerStatus.updated.forEach((abstractMarker) => {
                  markerManager.softUpdateAbstractMarker(abstractMarker);
                  const markerDiv = markerLogicContainer[abstractMarker.id];
                  updateMarkerDiv(abstractMarker, markerDiv);
                });

                markerStatus.new.forEach((abstractMarker) => {
                  markerManager.softUpdateAbstractMarker(abstractMarker);
                  const markerDiv = markerLogicContainer[abstractMarker.id];
                  updateMarkerDiv(abstractMarker, markerDiv);
                });
              };

              // The "idle" event is triggered every second because of the particle layer being refreshed,
              // even though their is no new data loaded, so this approach proved to be the best for this scenario
              map.on("move", softUpdateMarkers);

              map.on("moveend", updateMarkers);

              map.once("idle", () => {
                setTimeout(() => {
                  updateMarkers();
                }, 300);
              });
            })();

            function makeMarker(
              abstractMarker,
              temperatureLayer,
              radarLayer,
              precipitationLayer,
              date
            ) {
              const marker = document.createElement("div");
              marker.classList.add("marker");
              marker.classList.add("fade-in-animation");
              marker.style.setProperty("width", `${abstractMarker.size[0]}px`);
              marker.style.setProperty("height", `${abstractMarker.size[1]}px`);
              marker.style.setProperty(
                "transform",
                `translate(${abstractMarker.position[0]}px, ${abstractMarker.position[1]}px)`
              );

              const lonLat = abstractMarker.features[0].geometry.coordinates;
              const temperatureData = temperatureLayer.pickAt(lonLat[0], lonLat[1]);
              const precipitationData = precipitationLayer.pickAt(
                lonLat[0],
                lonLat[1]
              );

              const radarData = radarLayer.pickAt(lonLat[0], lonLat[1]);

              let mainWeatherIconURL = "https://docs.maptiler.com/sdk-js/examples/marker-layout-weather/weather-icons/";
              const radarDBz = radarData?.value || -20;
              const precipMmH = precipitationData?.value || 0;
              const temperatureDeg = temperatureData?.value || 0;
              const temperature = temperatureData?.value.toFixed(1);

              const sunPosition = SunCalc.getPosition(date, lonLat[1], lonLat[0]);

              if (sunPosition.altitude < 0) {
                mainWeatherIconURL += "night-";
              } else {
                mainWeatherIconURL += "day-";
              }

              if (radarDBz < 0) {
                if (precipMmH > 0.2) {
                  mainWeatherIconURL += "cloudy-";
                } else {
                  mainWeatherIconURL += "clear-";
                }
              } else if (radarDBz < 10) {
                mainWeatherIconURL += "cloudy-";
              } else if (radarDBz < 20) {
                mainWeatherIconURL += "overcast-";
              } else {
                mainWeatherIconURL += "extreme-";
              }

              if (precipMmH > 5) {
                mainWeatherIconURL += temperatureDeg < -1 ? "snow" : "rain";
              } else if (precipMmH > 0.2) {
                mainWeatherIconURL += temperatureDeg < -1 ? "snow" : "drizzle";
              } else {
                mainWeatherIconURL += "none";
              }

              mainWeatherIconURL += ".svg";

              marker.innerHTML = `
              <img class="markerMainWeatherIcon" src=${mainWeatherIconURL}></img>
              <div class="markerTemperature">${temperature ? `${temperature}°` : ''}</div>
              `;
              return marker;
            }

            function updateMarkerDiv(abstractMarker, marker) {
              marker.style.setProperty("width", `${abstractMarker.size[0]}px`);
              marker.style.setProperty("height", `${abstractMarker.size[1]}px`);
              marker.style.setProperty(
                "transform",
                `translate(${abstractMarker.position[0]}px, ${abstractMarker.position[1]}px)`
              );
            }
    </script>
</body>
</html>
```
