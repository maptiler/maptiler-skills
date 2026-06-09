# Source: https://docs.maptiler.com/sdk-js/examples/color-switcher/

# Change a layer's color with buttons

Use [`setPaintProperty`](/sdk-js/api/map/#map#setpaintproperty) to change a layer's fill color.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const swatches = document.getElementById('swatches');
    const layer = document.getElementById('layer');
    const colors = [
      '#ffffcc',
      '#a1dab4',
      '#41b6c4',
      '#2c7fb8',
      '#253494',
      '#fed976',
      '#feb24c',
      '#fd8d3c',
      '#f03b20',
      '#bd0026'
    ];

    colors.forEach(function (color) {
      const swatch = document.createElement('button');
      swatch.style.backgroundColor = color;
      swatch.addEventListener('click', function () {
        map.setPaintProperty(layer.value, 'fill-color', color);
      });
      swatches.appendChild(swatch);
    });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Change a layer's color with buttons</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
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
            style: maptilersdk.MapStyle.BASE,
            center: [12.338, 45.4385],
            zoom: 17.4
        });

        const swatches = document.getElementById('swatches');
            const layer = document.getElementById('layer');
            const colors = [
              '#ffffcc',
              '#a1dab4',
              '#41b6c4',
              '#2c7fb8',
              '#253494',
              '#fed976',
              '#feb24c',
              '#fd8d3c',
              '#f03b20',
              '#bd0026'
            ];

            colors.forEach(function (color) {
              const swatch = document.createElement('button');
              swatch.style.backgroundColor = color;
              swatch.addEventListener('click', function () {
                map.setPaintProperty(layer.value, 'fill-color', color);
              });
              swatches.appendChild(swatch);
            });
    </script>
</body>
</html>
```
