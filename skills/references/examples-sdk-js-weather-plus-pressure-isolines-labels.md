# Source: https://docs.maptiler.com/sdk-js/examples/weather-plus-pressure-isolines-labels/

# Display a pressure isolines layer

Experience the visualization of weather [pressure isolines](/sdk-js/modules/weather/api/pressure-isolines/) on the [MapTiler Weather Plus](https://www.maptiler.com/weather/). Utilize the Pressure dataset to access this layer and observe the extreme values of high and low pressure.

By employing the [`showPressureLabels` function](/sdk-js/modules/weather/api/isolines/#methods#showPressureLabels) within the pressure layer, these extreme Hi/Lo pressure values are prominently displayed for easy reference.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element to render the map
        style: maptilersdk.MapStyle.BACKDROP,  // stylesheet location
        projectionControl: true,
        projection: 'globe',
        zoom: 1.5,
        center: [-15.5, 15.2],
      }));

      const labelsButton = document.getElementById("show-labels");
      let hasLabels = false;

      const weatherLayer = new maptilerweatherplus.PressureIsolineLayer({
        opacity: 0.8,
      });

      map.on('load', function () {
        map.setPaintProperty("Water", 'fill-color', "rgba(0, 0, 0, 0.4)");
        map.addLayer(weatherLayer, 'Water');  
      });

      labelsButton.addEventListener("click", () => {
        hasLabels = !hasLabels;
        labelsButton.innerText = hasLabels ? "Hide labels" : "Show labels";
        if (hasLabels) {
          weatherLayer.showPressureLabels();
        } else {
          weatherLayer.hidePressureLabels();
        }
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
            zoom: 1.5
        });

        container: 'map', // container's id or the HTML element to render the map
                style: maptilersdk.MapStyle.BACKDROP,  // stylesheet location
                projectionControl: true,
                projection: 'globe',
                zoom: 1.5,
                center: [-15.5, 15.2],
              }));

              const labelsButton = document.getElementById("show-labels");
              let hasLabels = false;

              const weatherLayer = new maptilerweatherplus.PressureIsolineLayer({
                opacity: 0.8,
              });

              map.on('load', function () {
                map.setPaintProperty("Water", 'fill-color', "rgba(0, 0, 0, 0.4)");
                map.addLayer(weatherLayer, 'Water');  
              });

              labelsButton.addEventListener("click", () => {
                hasLabels = !hasLabels;
                labelsButton.innerText = hasLabels ? "Hide labels" : "Show labels";
                if (hasLabels) {
                  weatherLayer.showPressureLabels();
                } else {
                  weatherLayer.hidePressureLabels();
                }
              });
    </script>
</body>
</html>
```
