# Source: https://docs.maptiler.com/sdk-js/examples/weather-wind-temperature/

# MapTiler Wind + Temperature

Experience the power of visualizing weather conditions, including wind speed and temperature, with the help of MapTiler's Weather Wind dataset. By accessing this dataset, you can easily retrieve information about wind speed and temperature at any specific location.

To enhance the user experience, we have implemented a unique feature in this example. Utilizing the `ColorRamp.builtin.NULL` on the wind layer, we have ensured that only the wind direction particles are displayed above the temperature layer. Additionally, we have incorporated a convenient time control that allows you to select a specific date and time to view the corresponding data. The time control is generated using the `getAnimationStartDate()` and `getAnimationEndDate()` functions of the layer, which define the minimum and maximum dates available for exploration.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const layerBg = new maptilerweather.TemperatureLayer({
      opacity: 0.8,
    });

    const layer = new maptilerweather.WindLayer({
      id: "Wind Particles",
      colorramp: maptilerweather.ColorRamp.builtin.NULL,
      speed: 0.001,
      fadeFactor: 0.03,
      maxAmount: 256,
      density: 200,
      color: [0, 0, 0, 30],
      fastColor: [0, 0, 0, 100],
    });
    
    map.on('load', function () {
      // Darkening the water layer to make the land stand out
      map.setPaintProperty("Water", 'fill-color', "rgba(0, 0, 0, 0.6)");
      map.addLayer(layer);
      map.addLayer(layerBg, "Water");
      
    });

    timeSlider.addEventListener("input", (evt) => {
      layer.setAnimationTime(parseInt(timeSlider.value / 1000))
      layerBg.setAnimationTime(parseInt(timeSlider.value / 1000))
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
        layerBg.animateByFactor(0);
        playPauseButton.innerText = "Play 3600x";
      } else {
        layer.animateByFactor(3600);
        layerBg.animateByFactor(3600);
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
      const valueWind = layer.pickAt(lngLat.lng, lngLat.lat);
      const valueTemp = layerBg.pickAt(lngLat.lng, lngLat.lat);
      if (!valueWind) {
        pointerDataDiv.innerText = "";
        return;
      }
      pointerDataDiv.innerText = `${valueTemp.value.toFixed(1)}°C \n ${valueWind.speedKilometersPerHour.toFixed(1)} km/h`
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
    <title>MapTiler Wind + Temperature</title>
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

        const layerBg = new maptilerweather.TemperatureLayer({
              opacity: 0.8,
            });

            const layer = new maptilerweather.WindLayer({
              id: "Wind Particles",
              colorramp: maptilerweather.ColorRamp.builtin.NULL,
              speed: 0.001,
              fadeFactor: 0.03,
              maxAmount: 256,
              density: 200,
              color: [0, 0, 0, 30],
              fastColor: [0, 0, 0, 100],
            });

            map.on('load', function () {
              // Darkening the water layer to make the land stand out
              map.setPaintProperty("Water", 'fill-color', "rgba(0, 0, 0, 0.6)");
              map.addLayer(layer);
              map.addLayer(layerBg, "Water");

            });

            timeSlider.addEventListener("input", (evt) => {
              layer.setAnimationTime(parseInt(timeSlider.value / 1000))
              layerBg.setAnimationTime(parseInt(timeSlider.value / 1000))
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
                layerBg.animateByFactor(0);
                playPauseButton.innerText = "Play 3600x";
              } else {
                layer.animateByFactor(3600);
                layerBg.animateByFactor(3600);
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
              const valueWind = layer.pickAt(lngLat.lng, lngLat.lat);
              const valueTemp = layerBg.pickAt(lngLat.lng, lngLat.lat);
              if (!valueWind) {
                pointerDataDiv.innerText = "";
                return;
              }
              pointerDataDiv.innerText = `${valueTemp.value.toFixed(1)}°C \n ${valueWind.speedKilometersPerHour.toFixed(1)} km/h`
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
