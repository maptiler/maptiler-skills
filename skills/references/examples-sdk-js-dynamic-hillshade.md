# Source: https://docs.maptiler.com/sdk-js/examples/dynamic-hillshade/

# Create dynamic hillshade

Changes in lightning of hills and mountains can easily simulate the movement of the sun during the day. You can achieve this by changing the [paint properties](/gl-style-specification/layers/#hillshade) of the "Hillshade" layer from [MapTiler Terrain RGB](/guides/map-tiling-hosting/data-hosting/rgb-terrain-by-maptiler/), which is included in Outdoor map style. Here is an [example how to add a hillshading layer](/sdk-js/api/layers/#hillshade) to any map style.

If you do not need dynamic lighting, you can add and [set hillshading values](/guides/map-design/layer-styling/#raster-styling) directly in the MapTiler  tool.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
// Update hillshade layer once the map style is loaded
    map.once('styledata', function () {
      update();
    });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Create dynamic hillshade</title>
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
            center: [9.0144, 46.5664],
            zoom: 8
        });

        // Update hillshade layer once the map style is loaded
            map.once('styledata', function () {
              update();
            });
    </script>
</body>
</html>
```
