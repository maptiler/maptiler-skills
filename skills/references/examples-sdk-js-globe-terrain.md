# Source: https://docs.maptiler.com/sdk-js/examples/globe-terrain/

# MapTiler Globe projection

Show a detailed 3D (three-dimensional) globe map with terrain elevation. Creating a 3D terrain globe view of your map requires only two lines of code. Simply include the projection and the terrain option within the map constructor.

Enhance the authenticity of your web mapping applications and data by using the globe projection and incorporating terrain relief into your maps. This will provide a greater sense of realism and depth to your visuals.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element to render the map
        style:  'ocean',
        maxPitch: 85,
        center: [-115.54098, 51.2018],
        zoom: 14,
        pitch: 83,
        bearing: 37.1,
        projection: 'globe', //enable globe projection
        terrain: true, //add terrain elevation
        terrainExageration: 1.5
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
            center: [-115.54098, 51.2018],
            zoom: 14,
            pitch: 83,
            bearing: 37.1
        });

        container: 'map', // container's id or the HTML element to render the map
                style:  'ocean',
                maxPitch: 85,
                center: [-115.54098, 51.2018],
                zoom: 14,
                pitch: 83,
                bearing: 37.1,
                projection: 'globe', //enable globe projection
                terrain: true, //add terrain elevation
                terrainExageration: 1.5
              });
    </script>
</body>
</html>
```
