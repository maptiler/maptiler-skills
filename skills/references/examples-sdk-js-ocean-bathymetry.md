# Source: https://docs.maptiler.com/sdk-js/examples/ocean-bathymetry/

# Add a map to a webpage

Show a detailed 3D map of the ocean's seafloor and its bathymetry.

Increase the authenticity of your web mapping applications and data by incorporating ocean relief into your maps. This will provide a greater sense of realism and depth to your visuals.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
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
    <title>Add a map to a webpage</title>
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
            center: [126.419, 10.2021],
            zoom: 9.12,
            pitch: 77,
            bearing: -20
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
