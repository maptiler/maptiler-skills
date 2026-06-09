# Source: https://docs.maptiler.com/sdk-js/examples/weather-plus-wind-arrow/

# Display a wind arrow layer

You can access the wind arrows layer on [MapTiler Weather Plus](https://www.maptiler.com/weather/) Wind dataset to view weather conditions. This layer provides an animated display of wind direction using arrows.

<pre data-src="./code1/index.html"></pre>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element to render the map
        style: maptilersdk.MapStyle.BACKDROP,
        projectionControl: true,
        projection: 'globe',
        zoom: 2,
        center: [-2.2, 37.8],
      }));

      const weatherLayer = new maptilerweatherplus.WindArrowLayer();
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
    <title>Display a wind arrow layer</title>
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
                style: maptilersdk.MapStyle.BACKDROP,
                projectionControl: true,
                projection: 'globe',
                zoom: 2,
                center: [-2.2, 37.8],
              }));

              const weatherLayer = new maptilerweatherplus.WindArrowLayer();
              map.on('load', function () {
                map.setPaintProperty("Water", 'fill-color', "rgba(0, 0, 0, 0.4)");
                map.addLayer(weatherLayer, 'Water');
              });
    </script>
</body>
</html>
```
