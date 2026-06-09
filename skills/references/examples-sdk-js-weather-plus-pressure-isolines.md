# Source: https://docs.maptiler.com/sdk-js/examples/weather-plus-pressure-isolines/

# Display a pressure isolines layer

Visualize the weather [pressure isolines layer](/sdk-js/modules/weather/api/pressure-isolines/) from [MapTiler Weather Plus](https://www.maptiler.com/weather/) Pressure dataset. Gain insights into the atmospheric pressure patterns and visualize them in a visually captivating manner.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element to render the map
        style: maptilersdk.MapStyle.BACKDROP,  // stylesheet location
        projectionControl: true,
        projection: 'globe',
        zoom: 2,
        center: [-2.2, 37.8],
      }));

      const weatherLayer = new maptilerweatherplus.PressureIsolineLayer();

      map.on('load', function () {
        map.setPaintProperty("Water", 'fill-color', "rgba(0, 0, 0, 0.4)");
        map.addLayer(weatherLayer, 'Water');  
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
            center: [-2.2, 37.8],
            zoom: 2
        });

        container: 'map', // container's id or the HTML element to render the map
                style: maptilersdk.MapStyle.BACKDROP,  // stylesheet location
                projectionControl: true,
                projection: 'globe',
                zoom: 2,
                center: [-2.2, 37.8],
              }));

              const weatherLayer = new maptilerweatherplus.PressureIsolineLayer();

              map.on('load', function () {
                map.setPaintProperty("Water", 'fill-color', "rgba(0, 0, 0, 0.4)");
                map.addLayer(weatherLayer, 'Water');  
              });
    </script>
</body>
</html>
```
