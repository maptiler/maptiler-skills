# Source: https://docs.maptiler.com/sdk-js/examples/weather-custom-popup/

# MapTiler Marker Layout

Let's create the custom non-colliding popups using the [Marker Layout](/sdk-js/modules/marker-layout/) on top of MapTiler SDK. The example uses the custom Marker Layout because it allows complete freedom of customization, which we can't do with the original MapLibre popups due to their limited design.

We gather the weather data (including wind, temperature and precipitation) displayed in the popup from various layers of the [MapTiler Weather JS module](/sdk-js/modules/weather/).

For this demo, we used [Meteocons](https://bas.dev/work/meteocons), a weather icon pack designed by Bas Milius also available on [GitHub](https://github.com/basmilius/weather-icons).

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
        filter: ((feature) => {
          if (["City labels", "Town labels"].includes(feature.layer.id)) {
            return true;
          } else {
            return ["village"].includes(feature.properties.class)
          }
        }),
      });

      // Creating the weather layers...
      // Temperature will be used as the main overlay
      const temperatureLayer = new maptilerweather.TemperatureLayer({
        opacity: 0.7,
      });

      // Radar will be using the cloud color ramp and used as a cloud overlay
      const radarLayer = new maptilerweather.RadarLayer({
        colorramp: maptilerweather.ColorRamp.builtin.RADAR_CLOUD,
      });

      // From the wind layer, we only display the particles (the background is using the NULL color ramp, which is transparent).
      // The slower particles are transparent, the fastest are opaque white
      const windLayer = new maptilerweather.WindLayer({
        colorramp: maptilerweather.ColorRamp.builtin.NULL,
        color: [255, 255, 255, 0],
        fastColor: [255, 255, 255, 100],
      });

      // The precispitation layer is created but actually not displayed.
      // It will only be used for picking precipitation metrics at the locations of the markers
      const precipitationLayer = new maptilerweather.PrecipitationLayer({
        colorramp: maptilerweather.ColorRamp.builtin.NULL,
      });

      // Setting the water layer partially transparent to increase the visual separation between land and water
      map.setPaintProperty("Water", "fill-color", "rgba(0, 0, 0, 0.7)");
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
          const markerDiv = makeMarker(abstractMarker,
            temperatureLayer,
            radarLayer,
            precipitationLayer,
            windLayer,
            new Date()
          );
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

      map.once("idle", () => {
        updateMarkers();
      });

    })()


    function makeMarker(abstractMarker,
      temperatureLayer, radarLayer,
      precipitationLayer, windLayer, date) {

      const marker = document.createElement("div");
      marker.classList.add("marker");
      marker.classList.add('fade-in-animation');
      marker.style.setProperty("width", `${abstractMarker.size[0]}px`);
      marker.style.setProperty("height", `${abstractMarker.size[1]}px`);
      marker.style.setProperty("transform", `translate(${abstractMarker.position[0]}px, ${abstractMarker.position[1]}px)`);

      const feature = abstractMarker.features[0];
      const lonLat = feature.geometry.coordinates;
      const temperatureData = temperatureLayer.pickAt(lonLat[0], lonLat[1]);
      const precipitationData = precipitationLayer.pickAt(lonLat[0], lonLat[1]);
      const windData = windLayer.pickAt(lonLat[0], lonLat[1]);
      const radarData = radarLayer.pickAt(lonLat[0], lonLat[1]);

      let mainWeatherIconURL = "./weather-icons/";
      const radarDBz = radarData?.value || -20;
      const precipMmH = precipitationData?.value || 0;
      const temperatureDeg = temperatureData?.value || 0;
      const windSpeed = windData?.speedKilometersPerHour || 0;
      const compassDirection = windData?.compassDirection || 0;
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
        mainWeatherIconURL += (temperatureDeg < -1 ? "snow" : "rain");
      } else if (precipMmH > 0.2) {
        mainWeatherIconURL += (temperatureDeg < -1 ? "snow" : "drizzle");
      } else {
        mainWeatherIconURL += "none";
      }

      mainWeatherIconURL += ".svg";

      let windDiv = "";
      if (windSpeed > 5) {
        windDiv = `
        <div
          class="markerWind"
        >
          <img class="markerWindIcon" src="./weather-icons/wind.svg"></img>${windSpeed.toFixed(0)} <span style="font-weight: 600; margin-left: 4px">${compassDirection}</span>
        </div>
        `
      }

      let precipDiv = "";
      if (precipMmH > 0.1) {
        precipDiv = `
        <div
          class="markerPrecipitation"
        >
          ${precipMmH.toFixed(1)} mm/h
        </div>
        `
      }

      marker.innerHTML = `
        <div class="markerPointy"></div>
        <div class="markerBody">

          <div class="markerTop">
            ${feature.properties["name:en"] || feature.properties["name"]}
          </div>

          <div class="markerBottom">
            <div class="markerBottomLeft">
              ${temperature ? `<div class="markerTemperature">${temperature}°</div>` : `<div class="markerTemperature"></div>`}
              ${windDiv}
            </div>

            <div class="markerBottomRight">
              <img class="markerMainWeatherIcon" src=${mainWeatherIconURL}></img>
              ${precipDiv}
            </div>
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
    <script src="https://cdn.maptiler.com/maptiler-weather/3.1.1/maptiler-weather.umd.min.js"></script>
    <script src="https://cdn.maptiler.com/maptiler-marker-layout/v2.0.1/maptiler-marker-layout.umd.min.js"></script>
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
            style: maptilersdk.MapStyle.STREETS,
            center: [2, 40],
            zoom: 4.5
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
                filter: ((feature) => {
                  if (["City labels", "Town labels"].includes(feature.layer.id)) {
                    return true;
                  } else {
                    return ["village"].includes(feature.properties.class)
                  }
                }),
              });

              // Creating the weather layers...
              // Temperature will be used as the main overlay
              const temperatureLayer = new maptilerweather.TemperatureLayer({
                opacity: 0.7,
              });

              // Radar will be using the cloud color ramp and used as a cloud overlay
              const radarLayer = new maptilerweather.RadarLayer({
                colorramp: maptilerweather.ColorRamp.builtin.RADAR_CLOUD,
              });

              // From the wind layer, we only display the particles (the background is using the NULL color ramp, which is transparent).
              // The slower particles are transparent, the fastest are opaque white
              const windLayer = new maptilerweather.WindLayer({
                colorramp: maptilerweather.ColorRamp.builtin.NULL,
                color: [255, 255, 255, 0],
                fastColor: [255, 255, 255, 100],
              });

              // The precispitation layer is created but actually not displayed.
              // It will only be used for picking precipitation metrics at the locations of the markers
              const precipitationLayer = new maptilerweather.PrecipitationLayer({
                colorramp: maptilerweather.ColorRamp.builtin.NULL,
              });

              // Setting the water layer partially transparent to increase the visual separation between land and water
              map.setPaintProperty("Water", "fill-color", "rgba(0, 0, 0, 0.7)");
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
                  const markerDiv = makeMarker(abstractMarker,
                    temperatureLayer,
                    radarLayer,
                    precipitationLayer,
                    windLayer,
                    new Date()
                  );
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

              map.once("idle", () => {
                updateMarkers();
              });

            })()


            function makeMarker(abstractMarker,
              temperatureLayer, radarLayer,
              precipitationLayer, windLayer, date) {

              const marker = document.createElement("div");
              marker.classList.add("marker");
              marker.classList.add('fade-in-animation');
              marker.style.setProperty("width", `${abstractMarker.size[0]}px`);
              marker.style.setProperty("height", `${abstractMarker.size[1]}px`);
              marker.style.setProperty("transform", `translate(${abstractMarker.position[0]}px, ${abstractMarker.position[1]}px)`);

              const feature = abstractMarker.features[0];
              const lonLat = feature.geometry.coordinates;
              const temperatureData = temperatureLayer.pickAt(lonLat[0], lonLat[1]);
              const precipitationData = precipitationLayer.pickAt(lonLat[0], lonLat[1]);
              const windData = windLayer.pickAt(lonLat[0], lonLat[1]);
              const radarData = radarLayer.pickAt(lonLat[0], lonLat[1]);

              let mainWeatherIconURL = "./weather-icons/";
              const radarDBz = radarData?.value || -20;
              const precipMmH = precipitationData?.value || 0;
              const temperatureDeg = temperatureData?.value || 0;
              const windSpeed = windData?.speedKilometersPerHour || 0;
              const compassDirection = windData?.compassDirection || 0;
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
                mainWeatherIconURL += (temperatureDeg < -1 ? "snow" : "rain");
              } else if (precipMmH > 0.2) {
                mainWeatherIconURL += (temperatureDeg < -1 ? "snow" : "drizzle");
              } else {
                mainWeatherIconURL += "none";
              }

              mainWeatherIconURL += ".svg";

              let windDiv = "";
              if (windSpeed > 5) {
                windDiv = `
                <div
                  class="markerWind"
                >
                  <img class="markerWindIcon" src="./weather-icons/wind.svg"></img>${windSpeed.toFixed(0)} <span style="font-weight: 600; margin-left: 4px">${compassDirection}</span>
                </div>
                `
              }

              let precipDiv = "";
              if (precipMmH > 0.1) {
                precipDiv = `
                <div
                  class="markerPrecipitation"
                >
                  ${precipMmH.toFixed(1)} mm/h
                </div>
                `
              }

              marker.innerHTML = `
                <div class="markerPointy"></div>
                <div class="markerBody">

                  <div class="markerTop">
                    ${feature.properties["name:en"] || feature.properties["name"]}
                  </div>

                  <div class="markerBottom">
                    <div class="markerBottomLeft">
                      ${temperature ? `<div class="markerTemperature">${temperature}°</div>` : `<div class="markerTemperature"></div>`}
                      ${windDiv}
                    </div>

                    <div class="markerBottomRight">
                      <img class="markerMainWeatherIcon" src=${mainWeatherIconURL}></img>
                      ${precipDiv}
                    </div>
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
