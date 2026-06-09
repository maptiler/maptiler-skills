# Source: https://docs.maptiler.com/sdk-js/examples/globe-bathymetry/

# MapTiler Globe projection

Show a detailed 3D globe map of the ocean’s seafloor and its bathymetry.

Increase the authenticity of your web mapping applications and data by using the globe projection and incorporating ocean relief into your maps. This will provide a greater sense of realism and depth to your visuals.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element to render the map
        style:  'ocean',
        maxPitch: 85,
        center: [165.9043, 54.7078], // starting position [lng, lat]
        zoom: 10.04, // starting zoom
        bearing: -33.2,
        pitch: 72,
        projection: 'globe' //enable globe projection
      });

      map.on('load', function() {
        map.addSource("bathymetry", {
          type: 'raster-dem',
          url: 'https://api.maptiler.com/tiles/ocean-rgb/tiles.json',
        });
        map.setTerrain({ source: 'bathymetry', exaggeration: 1.5 });
      });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>MapTiler Globe projection</title>
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
            style: 'ocean',
            center: [165.9043, 54.7078],
            zoom: 10.04,
            pitch: 72,
            bearing: -33.2
        });

        container: 'map', // container's id or the HTML element to render the map
                style:  'ocean',
                maxPitch: 85,
                center: [165.9043, 54.7078], // starting position [lng, lat]
                zoom: 10.04, // starting zoom
                bearing: -33.2,
                pitch: 72,
                projection: 'globe' //enable globe projection
              });

              map.on('load', function() {
                map.addSource("bathymetry", {
                  type: 'raster-dem',
                  url: 'https://api.maptiler.com/tiles/ocean-rgb/tiles.json',
                });
                map.setTerrain({ source: 'bathymetry', exaggeration: 1.5 });
              });
    </script>
</body>
</html>
```
