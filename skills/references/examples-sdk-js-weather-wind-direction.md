# Source: https://docs.maptiler.com/sdk-js/examples/weather-wind-direction/

# Display a wind layer direction

Witness the awe-inspiring display of the weather wind layer in MapTiler Weather Wind dataset. Explore the wind speed and direction at any desired location by simply following the cursor. Immerse yourself in the captivating wind animation, boasting a remarkable 60 frames per second.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const layer = new maptilerweather.WindLayer();
    
    map.on('load', function () {
      // Darkening the water layer to make the land stand out
      map.setPaintProperty("Water", 'fill-color', "rgba(0, 0, 0, 0.4)");
      map.addLayer(layer, 'Water');
    });

    timeSlider.addEventListener("input", (evt) => {
      layer.setAnimationTime(parseInt(timeSlider.value / 1000))
    })

    // Event called when all the datasource for the next days are added and ready.
    // From now on, the layer nows the start and end dates.
    layer.on("sourceReady", event => {
      const startDate = layer.getAnimationStartDate();
      const endDate = layer.getAnimationEndDate();
      const currentDate = layer.getAnimationTimeDate();
      refreshTime()

      timeSlider.min = +startDate;
      timeSlider.max = +endDate;
      timeSlider.value = +currentDate;
    })

    // Called when the animation is progressing
    layer.on("tick", event => {
      refreshTime();
      updatePointerValue(pointerLngLat);
    })

    // Called when the time is manually set
    layer.on("animationTimeSet", event => {
      refreshTime()
    })

    // When clicking on the play/pause
    let isPlaying = false;
    playPauseButton.addEventListener("click", () => {
      if (isPlaying) {
        layer.animateByFactor(0);
        playPauseButton.innerText = "Play 3600x";
      } else {
        layer.animateByFactor(3600);
        playPauseButton.innerText = "Pause";
      }

      isPlaying = !isPlaying;
    })

    // Update the date time display
    function refreshTime() {
      const d = layer.getAnimationTimeDate();
      timeTextDiv.innerText = d.toString();
      timeSlider.value = +d;
    }

    function updatePointerValue(lngLat) {
      if (!lngLat) return;
      pointerLngLat = lngLat;
      const value = layer.pickAt(lngLat.lng, lngLat.lat);
      if (!value) {
        pointerDataDiv.innerText = "";
        return;
      }
      pointerDataDiv.innerHTML = `<div id="arrow" style="transform: rotate(${value.directionAngle}deg);">↑</div>
      ${value.compassDirection} ${value.speedKilometersPerHour.toFixed(1)} km/h`;
    }

    timeInfoContainer.addEventListener("mouseenter", () => {
      pointerDataDiv.innerText = "";
    })

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
    <title>Display a wind layer direction</title>
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

        const layer = new maptilerweather.WindLayer();

            map.on('load', function () {
              // Darkening the water layer to make the land stand out
              map.setPaintProperty("Water", 'fill-color', "rgba(0, 0, 0, 0.4)");
              map.addLayer(layer, 'Water');
            });

            timeSlider.addEventListener("input", (evt) => {
              layer.setAnimationTime(parseInt(timeSlider.value / 1000))
            })

            // Event called when all the datasource for the next days are added and ready.
            // From now on, the layer nows the start and end dates.
            layer.on("sourceReady", event => {
              const startDate = layer.getAnimationStartDate();
              const endDate = layer.getAnimationEndDate();
              const currentDate = layer.getAnimationTimeDate();
              refreshTime()

              timeSlider.min = +startDate;
              timeSlider.max = +endDate;
              timeSlider.value = +currentDate;
            })

            // Called when the animation is progressing
            layer.on("tick", event => {
              refreshTime();
              updatePointerValue(pointerLngLat);
            })

            // Called when the time is manually set
            layer.on("animationTimeSet", event => {
              refreshTime()
            })

            // When clicking on the play/pause
            let isPlaying = false;
            playPauseButton.addEventListener("click", () => {
              if (isPlaying) {
                layer.animateByFactor(0);
                playPauseButton.innerText = "Play 3600x";
              } else {
                layer.animateByFactor(3600);
                playPauseButton.innerText = "Pause";
              }

              isPlaying = !isPlaying;
            })

            // Update the date time display
            function refreshTime() {
              const d = layer.getAnimationTimeDate();
              timeTextDiv.innerText = d.toString();
              timeSlider.value = +d;
            }

            function updatePointerValue(lngLat) {
              if (!lngLat) return;
              pointerLngLat = lngLat;
              const value = layer.pickAt(lngLat.lng, lngLat.lat);
              if (!value) {
                pointerDataDiv.innerText = "";
                return;
              }
              pointerDataDiv.innerHTML = `<div id="arrow" style="transform: rotate(${value.directionAngle}deg);">↑</div>
              ${value.compassDirection} ${value.speedKilometersPerHour.toFixed(1)} km/h`;
            }

            timeInfoContainer.addEventListener("mouseenter", () => {
              pointerDataDiv.innerText = "";
            })

            map.on('mousemove', (e) => {
              updatePointerValue(e.lngLat);
            });
    </script>
</body>
</html>
```
