# Source: https://docs.maptiler.com/sdk-js/examples/weather-temperature-color-ramp/

# Display a temperature layer with a custom color blind ramp

Experience the power of visualizing weather temperature data with the MapTiler Weather Temperature dataset. Utilize a personalized color scheme designed specifically for individuals with color blindness, and easily access temperature information for any location by simply hovering over it.

In the temperature layer, we use one of the color ramps built-in in the SDK. Using the `animateByFactor(3600)` function of the temperature layer, we can create a dynamic time-based animation for the next 4 days. Each second of animation corresponds to one hour.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element to render the map
        style: maptilersdk.MapStyle.BACKDROP,  // stylesheet location
        zoom: 3,
        center: [-94.77, 38.57],
        hash: true,
        projectionControl: true,
      }));

      const timeTextDiv = document.getElementById("time-text");
      const pointerDataDiv = document.getElementById("pointer-data");
      let pointerLngLat = null;

      // You can define a custom color ramp using an extensive definition such as this one:
      const customColoramp = new maptilerweather.ColorRamp({ 
        stops: [
          { value: -65, color: [49, 54, 149, 255] },
          { value: -40, color: [69, 117, 180, 255] },
          { value: -30, color: [116, 173, 209, 255] },
          { value: -20, color: [171, 217, 233, 255] },
          { value: -10, color: [224, 243, 248, 255] },
          { value: 0, color: [255, 255, 255, 255] },
          { value: 12, color: [255, 255, 191, 255] },
          { value: 20, color: [254, 224, 144, 255] },
          { value: 25, color: [253, 174, 97, 255] },
          { value: 30, color: [244, 109, 67, 255] },
          { value: 40, color: [215,48,39, 255] },
          { value: 55, color: [165, 0, 38, 255] },
        ],
      });

      const weatherLayer = new maptilerweather.TemperatureLayer({
        colorramp: customColoramp
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
        pointerDataDiv.innerText = `${value.value.toFixed(1)}°`;
      }

      map.on('mousemove', (e) => {
        updatePointerValue(e.lngLat);
      });

      class colorRampLegendControl {
        constructor(options) {
          this._options = {...options};
          this._container = document.createElement("div");
          this._container.classList.add("maplibregl-ctrl");
          this._container.classList.add("maplibregl-ctrl-color-ramp");
        }
        onAdd(map) {
          this._map = map;
          const colorramp = this._options.colorRamp;
          const canvas = colorramp.getCanvasStrip();
          canvas.style.height = "30px";
          canvas.style.width = "200px";
          canvas.style.border = "1px dashed #00000059";

          const bounds = colorramp.getBounds()

          const desc = document.createElement("div");
          desc.classList.add("color-ramp-label");
          desc.innerHTML = `(min: ${bounds.min}, max: ${bounds.max})`;
          
          this._container.appendChild(desc);
          this._container.appendChild(canvas);
          return this._container;
        }
        onRemove() {
          if (!this._map || !this._container) {
            return;
          }
          this._container.parentNode.removeChild(this._container);
          this._map = undefined;
          delete this._map;
        }
      }

      map.addControl(new colorRampLegendControl({colorRamp: customColoramp}), 'bottom-left');
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Display a temperature layer with a custom color blind ramp</title>
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
            center: [-94.77, 38.57],
            zoom: 3
        });

        container: 'map', // container's id or the HTML element to render the map
                style: maptilersdk.MapStyle.BACKDROP,  // stylesheet location
                zoom: 3,
                center: [-94.77, 38.57],
                hash: true,
                projectionControl: true,
              }));

              const timeTextDiv = document.getElementById("time-text");
              const pointerDataDiv = document.getElementById("pointer-data");
              let pointerLngLat = null;

              // You can define a custom color ramp using an extensive definition such as this one:
              const customColoramp = new maptilerweather.ColorRamp({ 
                stops: [
                  { value: -65, color: [49, 54, 149, 255] },
                  { value: -40, color: [69, 117, 180, 255] },
                  { value: -30, color: [116, 173, 209, 255] },
                  { value: -20, color: [171, 217, 233, 255] },
                  { value: -10, color: [224, 243, 248, 255] },
                  { value: 0, color: [255, 255, 255, 255] },
                  { value: 12, color: [255, 255, 191, 255] },
                  { value: 20, color: [254, 224, 144, 255] },
                  { value: 25, color: [253, 174, 97, 255] },
                  { value: 30, color: [244, 109, 67, 255] },
                  { value: 40, color: [215,48,39, 255] },
                  { value: 55, color: [165, 0, 38, 255] },
                ],
              });

              const weatherLayer = new maptilerweather.TemperatureLayer({
                colorramp: customColoramp
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
                pointerDataDiv.innerText = `${value.value.toFixed(1)}°`;
              }

              map.on('mousemove', (e) => {
                updatePointerValue(e.lngLat);
              });

              class colorRampLegendControl {
                constructor(options) {
                  this._options = {...options};
                  this._container = document.createElement("div");
                  this._container.classList.add("maplibregl-ctrl");
                  this._container.classList.add("maplibregl-ctrl-color-ramp");
                }
                onAdd(map) {
                  this._map = map;
                  const colorramp = this._options.colorRamp;
                  const canvas = colorramp.getCanvasStrip();
                  canvas.style.height = "30px";
                  canvas.style.width = "200px";
                  canvas.style.border = "1px dashed #00000059";

                  const bounds = colorramp.getBounds()

                  const desc = document.createElement("div");
                  desc.classList.add("color-ramp-label");
                  desc.innerHTML = `(min: ${bounds.min}, max: ${bounds.max})`;

                  this._container.appendChild(desc);
                  this._container.appendChild(canvas);
                  return this._container;
                }
                onRemove() {
                  if (!this._map || !this._container) {
                    return;
                  }
                  this._container.parentNode.removeChild(this._container);
                  this._map = undefined;
                  delete this._map;
                }
              }

              map.addControl(new colorRampLegendControl({colorRamp: customColoramp}), 'bottom-left');
    </script>
</body>
</html>
```
