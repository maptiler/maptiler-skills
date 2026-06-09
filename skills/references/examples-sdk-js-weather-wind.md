# Source: https://docs.maptiler.com/sdk-js/examples/weather-wind/

# Display a wind layer

Experience viewing the weather wind layer from the MapTiler Weather Wind dataset and get the wind speed at the specific location indicated by the cursor. View the wind animation up to 60 frames per second.

To display data for the next four days in an animated format, you can use the layer's `animateByFactor` function.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element to render the map
        style: maptilersdk.MapStyle.BACKDROP,
        zoom: 2,
        center: [0, 40],
        projection: 'globe',
        projectionControl: true
      }));

      const timeInfoContainer = document.getElementById("time-info");
      const timeTextDiv = document.getElementById("time-text");
      const timeSlider = document.getElementById("time-slider");
      const playPauseButton = document.getElementById("play-pause-bt");
      const pointerDataDiv = document.getElementById("pointer-data");
      let pointerLngLat = null;

      const weatherLayer = new maptilerweather.WindLayer();

      map.on('load', function () {
        map.setPaintProperty("Water", 'fill-color', "rgba(0, 0, 0, 0.4)");
        map.addLayer(weatherLayer, 'Water');
      });

      timeSlider.addEventListener("input", (evt) => {
        weatherLayer.setAnimationTime(parseInt(timeSlider.value / 1000))
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
        refreshTime()
      });

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
      });

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
        pointerDataDiv.innerText = `${value.speedMetersPerSecond.toFixed(1)} m/s`
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
    <title>Display a wind layer</title>
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
            style: maptilersdk.MapStyle.BACKDROP,
            center: [0, 40],
            zoom: 2
        });

        container: 'map', // container's id or the HTML element to render the map
                style: maptilersdk.MapStyle.BACKDROP,
                zoom: 2,
                center: [0, 40],
                projection: 'globe',
                projectionControl: true
              }));

              const timeInfoContainer = document.getElementById("time-info");
              const timeTextDiv = document.getElementById("time-text");
              const timeSlider = document.getElementById("time-slider");
              const playPauseButton = document.getElementById("play-pause-bt");
              const pointerDataDiv = document.getElementById("pointer-data");
              let pointerLngLat = null;

              const weatherLayer = new maptilerweather.WindLayer();

              map.on('load', function () {
                map.setPaintProperty("Water", 'fill-color', "rgba(0, 0, 0, 0.4)");
                map.addLayer(weatherLayer, 'Water');
              });

              timeSlider.addEventListener("input", (evt) => {
                weatherLayer.setAnimationTime(parseInt(timeSlider.value / 1000))
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
                refreshTime()
              });

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
              });

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
                pointerDataDiv.innerText = `${value.speedMetersPerSecond.toFixed(1)} m/s`
              }

              map.on('mousemove', (e) => {
                updatePointerValue(e.lngLat);
              });
    </script>
</body>
</html>
```
