# Source: https://docs.maptiler.com/sdk-js/examples/weather-layer-switcher/

# Maptiler weather layers

Switch the display of various weather layers within MapTiler Weather dataset and access the data details at the location indicated by the cursor.

By utilizing the `animateByFactor(3600)` function, we can create a time-based animation that spans the next four days. Each second of the animation represents an hour.

Utilize the provided time animation bar to explore the weather forecast for the upcoming four-day period.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const weatherLayers = {
        "precipitation": {
          "layer": null,
          "value": "value",
          "units": " mm"
        },
        "pressure": {
          "layer": null,
          "value": "value",
          "units": " hPa"
        },
        "radar": {
          "layer": null,
          "value": "value",
          "units": " dBZ"
        },
        "temperature": {
          "layer": null,
          "value": "value",
          "units": "°"
        },
        "wind": {
          "layer": null,
          "value": "speedMetersPerSecond",
          "units": " m/s"
        }
      };
      
        container: 'map', // container's id or the HTML element to render the map
        style: maptilersdk.MapStyle.BACKDROP,  // stylesheet location
        zoom: 2,
        center: [-42.66, 37.63],
        hash: true,
        projectionControl: true,
        projection: 'globe'
      }));

      const initWeatherLayer = "wind";
      const timeInfoContainer = document.getElementById("time-info");
      const timeTextDiv = document.getElementById("time-text");
      const timeSlider = document.getElementById("time-slider");
      const playPauseButton = document.getElementById("play-pause-bt");
      const pointerDataDiv = document.getElementById("pointer-data");
      let pointerLngLat = null;
      let activeLayer = null;
      let isPlaying = false;
      let currentTime = null;

      timeSlider.addEventListener("input", (evt) => {
        const weatherLayer = weatherLayers[activeLayer]?.layer;
        if (weatherLayer) {
          weatherLayer.setAnimationTime(parseInt(timeSlider.value / 1000));
        }
      });

      // When clicking on the play/pause
      playPauseButton.addEventListener("click", () => {
        const weatherLayer = weatherLayers[activeLayer]?.layer;
        if (weatherLayer) {
          if (isPlaying) {
            pauseAnimation(weatherLayer);
          } else {
            playAnimation(weatherLayer);
          }
        }
      });

      function pauseAnimation(weatherLayer) {
        weatherLayer.animateByFactor(0);
        playPauseButton.innerText = "Play 3600x";
        isPlaying = false;
      }

      function playAnimation(weatherLayer) {
        weatherLayer.animateByFactor(3600);
        playPauseButton.innerText = "Pause";
        isPlaying = true;
      }

      map.on('load', function () {
        map.setPaintProperty("Water", 'fill-color', "rgba(0, 0, 0, 0.4)");
        initWeatherMap(initWeatherLayer);
      });

      map.on('mouseout', function(evt) {
        if (!evt.originalEvent.relatedTarget) {
          pointerDataDiv.innerText = "";
          pointerLngLat = null;
        }
      });

      function updatePointerValue(lngLat) {
        if (!lngLat) return;
        pointerLngLat = lngLat;
        const weatherLayer = weatherLayers[activeLayer]?.layer;
        const weatherLayerValue = weatherLayers[activeLayer]?.value;
        const weatherLayerUnits = weatherLayers[activeLayer]?.units;
        if (weatherLayer) {
          const value = weatherLayer.pickAt(lngLat.lng, lngLat.lat);
          if (!value) {
            pointerDataDiv.innerText = "";
            return;
          }
          pointerDataDiv.innerText = `${value[weatherLayerValue].toFixed(1)}${weatherLayerUnits}`
        }
      }

      map.on('mousemove', (e) => {
        updatePointerValue(e.lngLat);
      });

      document.getElementById('buttons').addEventListener('click', function (event) {
        // Change layer based on button id
        changeWeatherLayer(event.target.id);
      });

      function changeWeatherLayer(type) {
        if (type !== activeLayer) {
          if (map.getLayer(activeLayer)) {
            const activeWeatherLayer = weatherLayers[activeLayer]?.layer;
            if (activeWeatherLayer) {
              currentTime = activeWeatherLayer.getAnimationTime();
              map.setLayoutProperty(activeLayer, 'visibility', 'none');
            }
          }
          activeLayer = type;
          const weatherLayer = weatherLayers[activeLayer].layer || createWeatherLayer(activeLayer);
          if (map.getLayer(activeLayer)) {
            map.setLayoutProperty(activeLayer, 'visibility', 'visible');
          } else {
            map.addLayer(weatherLayer, 'Water');
          }
          changeLayerLabel(activeLayer);
          activateButton(activeLayer);
          changeLayerAnimation(weatherLayer);
          return weatherLayer;
        }
      }

      function activateButton(activeLayer) {
        const buttons = document.getElementsByClassName('button');
        for (let i = 0; i < buttons.length; i++) {
          const btn = buttons[i];
          if (btn.id === activeLayer) {
            btn.classList.add('active');
          } else {
            btn.classList.remove('active');
          }
        }
      }

      function changeLayerAnimation(weatherLayer) {
        weatherLayer.setAnimationTime(parseInt(timeSlider.value / 1000));
        if (isPlaying) {
          playAnimation(weatherLayer);
        } else {
          pauseAnimation(weatherLayer);
        }
      }

      function createWeatherLayer(type){
        let weatherLayer = null;
        switch (type) {
          case 'precipitation':
            weatherLayer = new maptilerweather.PrecipitationLayer({id: 'precipitation'});
            break;
          case 'pressure':
            weatherLayer = new maptilerweather.PressureLayer({
              opacity: 0.8,
              id: 'pressure'
            });
            break;
          case 'radar':
            weatherLayer = new maptilerweather.RadarLayer({
              opacity: 0.8,
              id: 'radar'
            });
            break;
          case 'temperature':
            weatherLayer = new maptilerweather.TemperatureLayer({
              colorramp: maptilerweather.ColorRamp.builtin.TEMPERATURE_3,
              id: 'temperature'
            });
            break;  
          case 'wind':
            weatherLayer = new maptilerweather.WindLayer({id: 'wind'});
            break;
        }

        // Called when the animation is progressing
        weatherLayer.on("tick", event => {
          refreshTime();
          updatePointerValue(pointerLngLat);
        });

        // Called when the time is manually set
        weatherLayer.on("animationTimeSet", event => {
          refreshTime();
        });

        // Event called when all the datasource for the next days are added and ready.
        // From now on, the layer nows the start and end dates.
        weatherLayer.on("sourceReady", event => {
          const startDate = weatherLayer.getAnimationStartDate();
          const endDate = weatherLayer.getAnimationEndDate();      
          if (timeSlider.min > 0){
            weatherLayer.setAnimationTime(currentTime);
            changeLayerAnimation(weatherLayer);
          } else {
            const currentDate = weatherLayer.getAnimationTimeDate();
            timeSlider.min = +startDate;
            timeSlider.max = +endDate;
            timeSlider.value = +currentDate;
          }
        });

        weatherLayers[type].layer = weatherLayer;
        return weatherLayer;
      }

      // Update the date time display
      function refreshTime() {
        const weatherLayer = weatherLayers[activeLayer]?.layer;
        if (weatherLayer) {
          const d = weatherLayer.getAnimationTimeDate();
          timeTextDiv.innerText = d.toString();
          timeSlider.value = +d;
        }
      }

      function changeLayerLabel(type) {
        document.getElementById("variable-name").innerText = type;
      }

      function initWeatherMap(type) {
        const weatherLayer = changeWeatherLayer(type);
      }
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Maptiler weather layers</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" />
    <script src="https://cdn.maptiler.com/maptiler-weather/3.1.1/maptiler-weather.umd.min.js"></script>
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
            style: maptilersdk.MapStyle.BACKDROP,
            center: [-42.66, 37.63],
            zoom: 2
        });

        const weatherLayers = {
                "precipitation": {
                  "layer": null,
                  "value": "value",
                  "units": " mm"
                },
                "pressure": {
                  "layer": null,
                  "value": "value",
                  "units": " hPa"
                },
                "radar": {
                  "layer": null,
                  "value": "value",
                  "units": " dBZ"
                },
                "temperature": {
                  "layer": null,
                  "value": "value",
                  "units": "°"
                },
                "wind": {
                  "layer": null,
                  "value": "speedMetersPerSecond",
                  "units": " m/s"
                }
              };

                container: 'map', // container's id or the HTML element to render the map
                style: maptilersdk.MapStyle.BACKDROP,  // stylesheet location
                zoom: 2,
                center: [-42.66, 37.63],
                hash: true,
                projectionControl: true,
                projection: 'globe'
              }));

              const initWeatherLayer = "wind";
              const timeInfoContainer = document.getElementById("time-info");
              const timeTextDiv = document.getElementById("time-text");
              const timeSlider = document.getElementById("time-slider");
              const playPauseButton = document.getElementById("play-pause-bt");
              const pointerDataDiv = document.getElementById("pointer-data");
              let pointerLngLat = null;
              let activeLayer = null;
              let isPlaying = false;
              let currentTime = null;

              timeSlider.addEventListener("input", (evt) => {
                const weatherLayer = weatherLayers[activeLayer]?.layer;
                if (weatherLayer) {
                  weatherLayer.setAnimationTime(parseInt(timeSlider.value / 1000));
                }
              });

              // When clicking on the play/pause
              playPauseButton.addEventListener("click", () => {
                const weatherLayer = weatherLayers[activeLayer]?.layer;
                if (weatherLayer) {
                  if (isPlaying) {
                    pauseAnimation(weatherLayer);
                  } else {
                    playAnimation(weatherLayer);
                  }
                }
              });

              function pauseAnimation(weatherLayer) {
                weatherLayer.animateByFactor(0);
                playPauseButton.innerText = "Play 3600x";
                isPlaying = false;
              }

              function playAnimation(weatherLayer) {
                weatherLayer.animateByFactor(3600);
                playPauseButton.innerText = "Pause";
                isPlaying = true;
              }

              map.on('load', function () {
                map.setPaintProperty("Water", 'fill-color', "rgba(0, 0, 0, 0.4)");
                initWeatherMap(initWeatherLayer);
              });

              map.on('mouseout', function(evt) {
                if (!evt.originalEvent.relatedTarget) {
                  pointerDataDiv.innerText = "";
                  pointerLngLat = null;
                }
              });

              function updatePointerValue(lngLat) {
                if (!lngLat) return;
                pointerLngLat = lngLat;
                const weatherLayer = weatherLayers[activeLayer]?.layer;
                const weatherLayerValue = weatherLayers[activeLayer]?.value;
                const weatherLayerUnits = weatherLayers[activeLayer]?.units;
                if (weatherLayer) {
                  const value = weatherLayer.pickAt(lngLat.lng, lngLat.lat);
                  if (!value) {
                    pointerDataDiv.innerText = "";
                    return;
                  }
                  pointerDataDiv.innerText = `${value[weatherLayerValue].toFixed(1)}${weatherLayerUnits}`
                }
              }

              map.on('mousemove', (e) => {
                updatePointerValue(e.lngLat);
              });

              document.getElementById('buttons').addEventListener('click', function (event) {
                // Change layer based on button id
                changeWeatherLayer(event.target.id);
              });

              function changeWeatherLayer(type) {
                if (type !== activeLayer) {
                  if (map.getLayer(activeLayer)) {
                    const activeWeatherLayer = weatherLayers[activeLayer]?.layer;
                    if (activeWeatherLayer) {
                      currentTime = activeWeatherLayer.getAnimationTime();
                      map.setLayoutProperty(activeLayer, 'visibility', 'none');
                    }
                  }
                  activeLayer = type;
                  const weatherLayer = weatherLayers[activeLayer].layer || createWeatherLayer(activeLayer);
                  if (map.getLayer(activeLayer)) {
                    map.setLayoutProperty(activeLayer, 'visibility', 'visible');
                  } else {
                    map.addLayer(weatherLayer, 'Water');
                  }
                  changeLayerLabel(activeLayer);
                  activateButton(activeLayer);
                  changeLayerAnimation(weatherLayer);
                  return weatherLayer;
                }
              }

              function activateButton(activeLayer) {
                const buttons = document.getElementsByClassName('button');
                for (let i = 0; i < buttons.length; i++) {
                  const btn = buttons[i];
                  if (btn.id === activeLayer) {
                    btn.classList.add('active');
                  } else {
                    btn.classList.remove('active');
                  }
                }
              }

              function changeLayerAnimation(weatherLayer) {
                weatherLayer.setAnimationTime(parseInt(timeSlider.value / 1000));
                if (isPlaying) {
                  playAnimation(weatherLayer);
                } else {
                  pauseAnimation(weatherLayer);
                }
              }

              function createWeatherLayer(type){
                let weatherLayer = null;
                switch (type) {
                  case 'precipitation':
                    weatherLayer = new maptilerweather.PrecipitationLayer({id: 'precipitation'});
                    break;
                  case 'pressure':
                    weatherLayer = new maptilerweather.PressureLayer({
                      opacity: 0.8,
                      id: 'pressure'
                    });
                    break;
                  case 'radar':
                    weatherLayer = new maptilerweather.RadarLayer({
                      opacity: 0.8,
                      id: 'radar'
                    });
                    break;
                  case 'temperature':
                    weatherLayer = new maptilerweather.TemperatureLayer({
                      colorramp: maptilerweather.ColorRamp.builtin.TEMPERATURE_3,
                      id: 'temperature'
                    });
                    break;  
                  case 'wind':
                    weatherLayer = new maptilerweather.WindLayer({id: 'wind'});
                    break;
                }

                // Called when the animation is progressing
                weatherLayer.on("tick", event => {
                  refreshTime();
                  updatePointerValue(pointerLngLat);
                });

                // Called when the time is manually set
                weatherLayer.on("animationTimeSet", event => {
                  refreshTime();
                });

                // Event called when all the datasource for the next days are added and ready.
                // From now on, the layer nows the start and end dates.
                weatherLayer.on("sourceReady", event => {
                  const startDate = weatherLayer.getAnimationStartDate();
                  const endDate = weatherLayer.getAnimationEndDate();      
                  if (timeSlider.min > 0){
                    weatherLayer.setAnimationTime(currentTime);
                    changeLayerAnimation(weatherLayer);
                  } else {
                    const currentDate = weatherLayer.getAnimationTimeDate();
                    timeSlider.min = +startDate;
                    timeSlider.max = +endDate;
                    timeSlider.value = +currentDate;
                  }
                });

                weatherLayers[type].layer = weatherLayer;
                return weatherLayer;
              }

              // Update the date time display
              function refreshTime() {
                const weatherLayer = weatherLayers[activeLayer]?.layer;
                if (weatherLayer) {
                  const d = weatherLayer.getAnimationTimeDate();
                  timeTextDiv.innerText = d.toString();
                  timeSlider.value = +d;
                }
              }

              function changeLayerLabel(type) {
                document.getElementById("variable-name").innerText = type;
              }

              function initWeatherMap(type) {
                const weatherLayer = changeWeatherLayer(type);
              }
    </script>
</body>
</html>
```
