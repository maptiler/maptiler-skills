# Source: https://docs.maptiler.com/sdk-js/examples/queryrenderedfeatures/

# Get features under the mouse pointer

Use the [`queryRenderedFeatures`](/sdk-js/api/map/#map#queryrenderedfeatures) function to display the attributes of map elements when they are hovered over.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('mousemove', function (e) {
      const features = map.queryRenderedFeatures(e.point);

      // Limit the number of properties we're displaying for
      // legibility and performance
      const displayProperties = [
        'type',
        'properties',
        'id',
        'layer',
        'source',
        'sourceLayer',
        'state'
      ];

      const displayFeatures = features.map(function (feat) {
        const displayFeat = {};
        displayProperties.forEach(function (prop) {
          displayFeat[prop] = feat[prop];
        });
        return displayFeat;
      });

      document.getElementById('features').innerHTML = JSON.stringify(
        displayFeatures,
        null,
        2
      );
    });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Get features under the mouse pointer</title>
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
            center: [-96, 37.8],
            zoom: 3
        });

        map.on('mousemove', function (e) {
              const features = map.queryRenderedFeatures(e.point);

              // Limit the number of properties we're displaying for
              // legibility and performance
              const displayProperties = [
                'type',
                'properties',
                'id',
                'layer',
                'source',
                'sourceLayer',
                'state'
              ];

              const displayFeatures = features.map(function (feat) {
                const displayFeat = {};
                displayProperties.forEach(function (prop) {
                  displayFeat[prop] = feat[prop];
                });
                return displayFeat;
              });

              document.getElementById('features').innerHTML = JSON.stringify(
                displayFeatures,
                null,
                2
              );
            });
    </script>
</body>
</html>
```
