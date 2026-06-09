# Source: https://docs.maptiler.com/sdk-js/examples/weather-pressure/

# Display a pressure layer

Discover the visualization of the weather pressure layer through the MapTiler Weather Pressure dataset and obtain the pressure reading at the specific location indicated by the cursor.

By employing the `animateByFactor(3600)` function of the pressure layer, we can animate it over a period of time, specifically the upcoming four days. Each second of animation corresponds to an hour of real-time data.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element to render the map
        style: maptilersdk.MapStyle.BACKDROP,  // stylesheet location
        zoom: 1.5,
        center: [-15.5, 15.2],
        hash: true,
        projectionControl: true,
        projection: 'globe'
      }));

      const timeTextDiv = document.getElementById("time-text");
      const pointerDataDiv = document.getElementById("pointer-data");
      let pointerLngLat = null;

      const weatherLayer = new maptilerweather.PressureLayer({
        opacity: 0.8,
      });

      // Called when the animation is progressing
      weatherLayer.on("tick", event => {
        refreshTime();
        updatePointerValue(pointerLngLat);
      });

      map.on('load', function () {
        map.setPaintProperty("Water", 'fill-color', "rgba(0, 0, 0, 0.4)");
        map.addLayer(weatherLayer, 'Water');
        weatherLayer.animateByFactor(3600);
      });

      map.on('mouseout', function(evt) {
        if (!evt.originalEvent.relatedTarget) {
          pointerDataDiv.innerText = "";
          pointerLngLat = null;
        }
      });

      // Update the date time display
      function refreshTime() {
        const d = weatherLayer.getAnimationTimeDate();
        timeTextDiv.innerText = d.toString();
      }

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
    <title>Display a pressure layer</title>
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
            center: [-15.5, 15.2],
            zoom: 1.5
        });

        container: 'map', // container's id or the HTML element to render the map
                style: maptilersdk.MapStyle.BACKDROP,  // stylesheet location
                zoom: 1.5,
                center: [-15.5, 15.2],
                hash: true,
                projectionControl: true,
                projection: 'globe'
              }));

              const timeTextDiv = document.getElementById("time-text");
              const pointerDataDiv = document.getElementById("pointer-data");
              let pointerLngLat = null;

              const weatherLayer = new maptilerweather.PressureLayer({
                opacity: 0.8,
              });

              // Called when the animation is progressing
              weatherLayer.on("tick", event => {
                refreshTime();
                updatePointerValue(pointerLngLat);
              });

              map.on('load', function () {
                map.setPaintProperty("Water", 'fill-color', "rgba(0, 0, 0, 0.4)");
                map.addLayer(weatherLayer, 'Water');
                weatherLayer.animateByFactor(3600);
              });

              map.on('mouseout', function(evt) {
                if (!evt.originalEvent.relatedTarget) {
                  pointerDataDiv.innerText = "";
                  pointerLngLat = null;
                }
              });

              // Update the date time display
              function refreshTime() {
                const d = weatherLayer.getAnimationTimeDate();
                timeTextDiv.innerText = d.toString();
              }

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
