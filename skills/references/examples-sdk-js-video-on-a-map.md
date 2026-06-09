# Source: https://docs.maptiler.com/sdk-js/examples/video-on-a-map/

# Add a video

Display a video on top of a satellite raster baselayer. Click the map to play and pause the video.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
let playingVideo = true;

    map.on('click', function () {
        playingVideo = !playingVideo;

        if (playingVideo) map.getSource('video').play();
        else map.getSource('video').pause();
    });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Add a video</title>
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
            style: videoStyle,
            center: [-122.514426, 37.562984],
            zoom: 17,
            bearing: -96
        });

        let playingVideo = true;

            map.on('click', function () {
                playingVideo = !playingVideo;

                if (playingVideo) map.getSource('video').play();
                else map.getSource('video').pause();
            });
    </script>
</body>
</html>
```
