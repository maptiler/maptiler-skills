# Source: https://docs.maptiler.com/sdk-js/examples/change-building-color-based-on-zoom-level/

# Change building color based on zoom level

Use the [`interpolate` expression](/gl-style-specification/expressions/#interpolate) to ease-in the building layer and smoothly fade from one color to the next.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', function () {
      map.setPaintProperty('Building', 'fill-color', [
        'interpolate',
        ['exponential', 0.5],
        ['zoom'],
        15,
        '#e2714b',
        22,
        '#eee695'
      ]);

      map.setPaintProperty('Building', 'fill-opacity', [
        'interpolate',
        ['exponential', 0.5],
        ['zoom'],
        15,
        0,
        22,
        1
      ]);
    });

    document.getElementById('zoom').addEventListener('click', function () {
      map.zoomTo(19, { duration: 9000 });
    });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Change building color based on zoom level</title>
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
            center: [-90.73414, 14.55524],
            zoom: 13
        });

        map.on('load', function () {
              map.setPaintProperty('Building', 'fill-color', [
                'interpolate',
                ['exponential', 0.5],
                ['zoom'],
                15,
                '#e2714b',
                22,
                '#eee695'
              ]);

              map.setPaintProperty('Building', 'fill-opacity', [
                'interpolate',
                ['exponential', 0.5],
                ['zoom'],
                15,
                0,
                22,
                1
              ]);
            });

            document.getElementById('zoom').addEventListener('click', function () {
              map.zoomTo(19, { duration: 9000 });
            });
    </script>
</body>
</html>
```
