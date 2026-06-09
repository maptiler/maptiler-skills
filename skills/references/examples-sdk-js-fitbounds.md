# Source: https://docs.maptiler.com/sdk-js/examples/fitbounds/

# Fit a map to a bounding box

Use [`fitBounds`](/sdk-js/api/map/#map#fitbounds) to show a specific area of the map in view, regardless of the pixel size of the map.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
document.getElementById('fit').addEventListener('click', function () {
      map.fitBounds([
        [32.958984, -5.353521],
        [43.50585, 5.615985]
      ]);
    });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Fit a map to a bounding box</title>
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
            style: maptilersdk.MapStyle.STREETS,
            center: [-74.5, 40],
            zoom: 9
        });

        document.getElementById('fit').addEventListener('click', function () {
              map.fitBounds([
                [32.958984, -5.353521],
                [43.50585, 5.615985]
              ]);
            });
    </script>
</body>
</html>
```
