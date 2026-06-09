# Source: https://docs.maptiler.com/sdk-js/examples/weather-radar-cloud/

# Cloud coverage displayed from radar data

Explore the weather cloud coverage on a weather radar map using the MapTiler Weather Radar dataset and get the radar reflectivity in dBZ at the point under the cursor.

This example, illustrates the process of visualizing cloud cover, using the built-in `RADAR_CLOUD` color ramp.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element to render the map
        style: maptilersdk.MapStyle.BACKDROP.LIGHT,
        zoom: 1,
        center: [-15.5, 15.2],
        hash: true,
        projectionControl: true,
      }));

      const timeInfoContainer = document.getElementById("time-info");
      const timeTextDiv = document.getElementById("time-text");
      const timeSlider = document.getElementById("time-slider");
      const playPauseButton = document.getElementById("play-pause-bt");
      const pointerDataDiv = document.getElementById("pointer-data");
      let pointerLngLat = null;

      const weatherLayer = new maptilerweather.RadarLayer({
        opacity: 0.8,
        colorramp: maptilerweather.ColorRamp.builtin.RADAR_CLOUD,
      });

      // Event called when all the datasource for the next days are added and ready.
      // From now on, the layer nows the start and end dates.
      weatherLayer.on("sourceReady", event => {
        const startDate = weatherLayer.getAnimationStartDate();
        const endDate = weatherLayer.getAnimationEndDate();
        const currentDate = weatherLayer.getAnimationTimeDate();
        refreshTime()

        timeSlider.min = +startDate;
        timeSlider.max = +endDate;
        timeSlider.value = +currentDate;
      })

      timeSlider.addEventListener("input", (evt) => {
        weatherLayer.setAnimationTime(parseInt(timeSlider.value / 1000))
      });

      // Called when the animation is progressing
      weatherLayer.on("tick", event => {
        refreshTime();
        updatePointerValue(pointerLngLat);
      });

      map.on('load', function () {
        map.setPaintProperty("Water", 'fill-color', "rgba(0, 0, 0, 0.4)");
        map.addLayer(weatherLayer, 'Water');
      });

      map.on('mouseout', function(evt) {
        if (!evt.originalEvent.relatedTarget) {
          pointerDataDiv.innerText = "";
          pointerLngLat = null;
        }
      });

      // Called when the time is manually set
      weatherLayer.on("animationTimeSet", event => {
        refreshTime()
      })

      // When clicking on the play/pause
      let isPlaying = false;
      playPauseButton.addEventListener("click", () => {
        if (isPlaying) {
          weatherLayer.animateByFactor(0);
          playPauseButton.innerText = "Play 3600x";
        } else {
          weatherLayer.animateByFactor(3600);
          playPauseButton.innerText = "Pause";
        }

        isPlaying = !isPlaying;
      })

      // Update the date time display
      function refreshTime() {
        const d = weatherLayer.getAnimationTimeDate();
        timeTextDiv.innerText = d.toString();
        timeSlider.value = +d;
      }

      function updatePointerValue(lngLat) {
        if (!lngLat) return;
        pointerLngLat = lngLat;
        const value = weatherLayer.pickAt(lngLat.lng, lngLat.lat);
        if (!value) {
          pointerDataDiv.innerText = "";
          return;
        }
        pointerDataDiv.innerText = `${value.value.toFixed(1)} dBZ`
      }

      timeInfoContainer.addEventListener("mouseenter", () => {
        pointerDataDiv.innerText = "";
      });

      map.on('mousemove', (e) => {
        updatePointerValue(e.lngLat);
      });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Cloud coverage displayed from radar data</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
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
            style: maptilersdk.MapStyle.BACKDROP.LIGHT,
            center: [-15.5, 15.2],
            zoom: 1
        });

        container: 'map', // container's id or the HTML element to render the map
                style: maptilersdk.MapStyle.BACKDROP.LIGHT,
                zoom: 1,
                center: [-15.5, 15.2],
                hash: true,
                projectionControl: true,
              }));

              const timeInfoContainer = document.getElementById("time-info");
              const timeTextDiv = document.getElementById("time-text");
              const timeSlider = document.getElementById("time-slider");
              const playPauseButton = document.getElementById("play-pause-bt");
              const pointerDataDiv = document.getElementById("pointer-data");
              let pointerLngLat = null;

              const weatherLayer = new maptilerweather.RadarLayer({
                opacity: 0.8,
                colorramp: maptilerweather.ColorRamp.builtin.RADAR_CLOUD,
              });

              // Event called when all the datasource for the next days are added and ready.
              // From now on, the layer nows the start and end dates.
              weatherLayer.on("sourceReady", event => {
                const startDate = weatherLayer.getAnimationStartDate();
                const endDate = weatherLayer.getAnimationEndDate();
                const currentDate = weatherLayer.getAnimationTimeDate();
                refreshTime()

                timeSlider.min = +startDate;
                timeSlider.max = +endDate;
                timeSlider.value = +currentDate;
              })

              timeSlider.addEventListener("input", (evt) => {
                weatherLayer.setAnimationTime(parseInt(timeSlider.value / 1000))
              });

              // Called when the animation is progressing
              weatherLayer.on("tick", event => {
                refreshTime();
                updatePointerValue(pointerLngLat);
              });

              map.on('load', function () {
                map.setPaintProperty("Water", 'fill-color', "rgba(0, 0, 0, 0.4)");
                map.addLayer(weatherLayer, 'Water');
              });

              map.on('mouseout', function(evt) {
                if (!evt.originalEvent.relatedTarget) {
                  pointerDataDiv.innerText = "";
                  pointerLngLat = null;
                }
              });

              // Called when the time is manually set
              weatherLayer.on("animationTimeSet", event => {
                refreshTime()
              })

              // When clicking on the play/pause
              let isPlaying = false;
              playPauseButton.addEventListener("click", () => {
                if (isPlaying) {
                  weatherLayer.animateByFactor(0);
                  playPauseButton.innerText = "Play 3600x";
                } else {
                  weatherLayer.animateByFactor(3600);
                  playPauseButton.innerText = "Pause";
                }

                isPlaying = !isPlaying;
              })

              // Update the date time display
              function refreshTime() {
                const d = weatherLayer.getAnimationTimeDate();
                timeTextDiv.innerText = d.toString();
                timeSlider.value = +d;
              }

              function updatePointerValue(lngLat) {
                if (!lngLat) return;
                pointerLngLat = lngLat;
                const value = weatherLayer.pickAt(lngLat.lng, lngLat.lat);
                if (!value) {
                  pointerDataDiv.innerText = "";
                  return;
                }
                pointerDataDiv.innerText = `${value.value.toFixed(1)} dBZ`
              }

              timeInfoContainer.addEventListener("mouseenter", () => {
                pointerDataDiv.innerText = "";
              });

              map.on('mousemove', (e) => {
                updatePointerValue(e.lngLat);
              });
    </script>
</body>
</html>
```
