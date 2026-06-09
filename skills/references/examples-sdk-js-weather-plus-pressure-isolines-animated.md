# Source: https://docs.maptiler.com/sdk-js/examples/weather-plus-pressure-isolines-animated/

# Display a pressure isolines layer

Explore the weather [pressure isolines layer](/sdk-js/modules/weather/api/pressure-isolines/) from [MapTiler Weather Plus](https://www.maptiler.com/weather/) Pressure dataset. By accessing the Pressure dataset, you can visualize the distribution of pressure across different locations. With just a simple cursor movement, you can retrieve the precise pressure value at any given point.

The [`showPressureLabels` function](/sdk-js/modules/weather/api/isolines/#methods#showPressureLabels), allows you to view the highest and lowest pressure extremes on the map. This provides valuable insights into the atmospheric conditions and helps you understand the dynamics of weather patterns.

To enhance your experience, we have incorporated an animation bar that illustrates the movement of isobars over a four-day time period. This dynamic representation allows you to track changes in pressure over time and gain a deeper understanding of weather trends. Additionally, we have included a button that enables the display of Hi/Lo pressure extreme values labels, ensuring that you have all the necessary information at your fingertips.

<!-- <lite-vimeo class="rounded shadow" videoid="860922999" autoload="" background="" title=""></lite-vimeo> -->

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element to render the map
        style: maptilersdk.MapStyle.BACKDROP,  // stylesheet location
        projectionControl: true,
        zoom: 1,
        center: [-15.5, 15.2],
        hash: true,
      }));

      const timeInfoContainer = document.getElementById("time-info");
      const timeTextDiv = document.getElementById("time-text");
      const timeSlider = document.getElementById("time-slider");
      const playPauseButton = document.getElementById("play-pause-bt");
      const labelsButton = document.getElementById("show-labels");
      const pointerDataDiv = document.getElementById("pointer-data");
      let pointerLngLat = null;
      let hasLabels = false;

      const weatherLayer = new maptilerweatherplus.PressureIsolineLayer({
        opacity: 0.8,
      });

      map.on('load', function () {
        map.setPaintProperty("Water", 'fill-color', "rgba(0, 0, 0, 0.4)");
        map.addLayer(weatherLayer, 'Water');  
      });

      timeSlider.addEventListener("input", (evt) => {
        weatherLayer.setAnimationTime(parseInt(timeSlider.value / 1000));
        hideLabels();
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
      });

      // Called when the animation is progressing
      weatherLayer.on("tick", event => {
        refreshTime();
        updatePointerValue(pointerLngLat);
      });

      // Called when the time is manually set
      weatherLayer.on("animationTimeSet", event => {
        refreshTime();
      });

      // When clicking on the play/pause
      let isPlaying = false;
      playPauseButton.addEventListener("click", () => {
        if (isPlaying) {
          weatherLayer.animateByFactor(0);
          playPauseButton.innerText = "Play 3600x";
          labelsButton.disabled = false;
        } else {
          weatherLayer.animateByFactor(3600);
          playPauseButton.innerText = "Pause";
          hideLabels();
          labelsButton.disabled = true;
        }
        isPlaying = !isPlaying;
      });

      labelsButton.addEventListener("click", () => {
        if (!isPlaying && !hasLabels) {
          weatherLayer.showPressureLabels();
          hasLabels = true;
          labelsButton.innerText = "Hide labels";
        } else {
          hideLabels();
        }
      });

      function hideLabels() {
        weatherLayer.hidePressureLabels();
        hasLabels = false;
        labelsButton.innerText = "Show labels";
      }

      // Update the date time display
      function refreshTime() {
        const d = weatherLayer.getAnimationTimeDate();
        timeTextDiv.innerText = d.toString();
        timeSlider.value = +d;
      }

      map.on('mouseout', function(evt) {
        if (!evt.originalEvent.relatedTarget) {
          pointerDataDiv.innerText = "";
          pointerLngLat = null;
        }
      });

      function updatePointerValue(lngLat) {
        if (!lngLat) return;
        pointerLngLat = lngLat;
        const value = weatherLayer.pickAt(lngLat.lng, lngLat.lat);
        if (!value) {
          pointerDataDiv.innerText = "";
          return;
        }
        pointerDataDiv.innerText = `${value.value.toFixed(1)} hPa`
      }

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
    <title>Display a pressure isolines layer</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <script src="./maptiler-weather-plus.umd.js"></script>
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
            center: [-15.5, 15.2],
            zoom: 1
        });

        container: 'map', // container's id or the HTML element to render the map
                style: maptilersdk.MapStyle.BACKDROP,  // stylesheet location
                projectionControl: true,
                zoom: 1,
                center: [-15.5, 15.2],
                hash: true,
              }));

              const timeInfoContainer = document.getElementById("time-info");
              const timeTextDiv = document.getElementById("time-text");
              const timeSlider = document.getElementById("time-slider");
              const playPauseButton = document.getElementById("play-pause-bt");
              const labelsButton = document.getElementById("show-labels");
              const pointerDataDiv = document.getElementById("pointer-data");
              let pointerLngLat = null;
              let hasLabels = false;

              const weatherLayer = new maptilerweatherplus.PressureIsolineLayer({
                opacity: 0.8,
              });

              map.on('load', function () {
                map.setPaintProperty("Water", 'fill-color', "rgba(0, 0, 0, 0.4)");
                map.addLayer(weatherLayer, 'Water');  
              });

              timeSlider.addEventListener("input", (evt) => {
                weatherLayer.setAnimationTime(parseInt(timeSlider.value / 1000));
                hideLabels();
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
              });

              // Called when the animation is progressing
              weatherLayer.on("tick", event => {
                refreshTime();
                updatePointerValue(pointerLngLat);
              });

              // Called when the time is manually set
              weatherLayer.on("animationTimeSet", event => {
                refreshTime();
              });

              // When clicking on the play/pause
              let isPlaying = false;
              playPauseButton.addEventListener("click", () => {
                if (isPlaying) {
                  weatherLayer.animateByFactor(0);
                  playPauseButton.innerText = "Play 3600x";
                  labelsButton.disabled = false;
                } else {
                  weatherLayer.animateByFactor(3600);
                  playPauseButton.innerText = "Pause";
                  hideLabels();
                  labelsButton.disabled = true;
                }
                isPlaying = !isPlaying;
              });

              labelsButton.addEventListener("click", () => {
                if (!isPlaying && !hasLabels) {
                  weatherLayer.showPressureLabels();
                  hasLabels = true;
                  labelsButton.innerText = "Hide labels";
                } else {
                  hideLabels();
                }
              });

              function hideLabels() {
                weatherLayer.hidePressureLabels();
                hasLabels = false;
                labelsButton.innerText = "Show labels";
              }

              // Update the date time display
              function refreshTime() {
                const d = weatherLayer.getAnimationTimeDate();
                timeTextDiv.innerText = d.toString();
                timeSlider.value = +d;
              }

              map.on('mouseout', function(evt) {
                if (!evt.originalEvent.relatedTarget) {
                  pointerDataDiv.innerText = "";
                  pointerLngLat = null;
                }
              });

              function updatePointerValue(lngLat) {
                if (!lngLat) return;
                pointerLngLat = lngLat;
                const value = weatherLayer.pickAt(lngLat.lng, lngLat.lat);
                if (!value) {
                  pointerDataDiv.innerText = "";
                  return;
                }
                pointerDataDiv.innerText = `${value.value.toFixed(1)} hPa`
              }

              map.on('mousemove', (e) => {
                updatePointerValue(e.lngLat);
              });
    </script>
</body>
</html>
```
