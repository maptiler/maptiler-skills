# Source: https://docs.maptiler.com/sdk-js/examples/image-viewer/

# ImageViewer

The MapTiler's SDK [`ImageViewer`](/sdk-js/api/image-viewer/) allows you to display tiled, non-georeferenced images while interacting with them similarly to how you would navigate a regular map. This functionality works well for zoomable non-georeferenced, geographically "inaccurate" maps such as hotel maps, golf courses, theme parks etc. Think in pixels instead of lattitudes and longtidues.

Check out the guide [How to convert large images into zoomable tiles (no map)](/guides/map-tiling-hosting/data-processing/raster-profile-convert-your-images-into-zoomable-raster-tiles/) to learn how to upload your image to your MapTiler account.

<sup>Image: <a href="https://commons.wikimedia.org/wiki/File:1932_Japanese_pictorial_world_map_game_board.jpg">1932 Japanese pictorial world map game board - World Adventure</a></sup>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const imageViewer = new maptilersdk.ImageViewer({
      container: 'map',
      imageUUID: 'YOUR_MAPTILER_TILESET_ID_HERE',
    });

    imageViewer.on('imageviewerready', () => {
      console.log('Image ready!');
    });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ImageViewer</title>
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
            center: [0, 0],
            zoom: 0
        });

        const imageViewer = new maptilersdk.ImageViewer({
              container: 'map',
              imageUUID: 'YOUR_MAPTILER_TILESET_ID_HERE',
            });

            imageViewer.on('imageviewerready', () => {
              console.log('Image ready!');
            });
    </script>
</body>
</html>
```
