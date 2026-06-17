# Source: https://docs.maptiler.com/sdk-js/examples/animate-images/

# Animate a series of images

Create an animation by utilizing a collection of [image sources](/gl-style-specification/sources/#image) to form a sequence.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const frameCount = 5;
    let currentImage = 0;

    function getPath() {
        return (
            'https://docs.maptiler.com/sdk-js/assets/radar' +
            currentImage +
            '.gif'
        );
    }

    map.on('load', function () {
        map.addSource('radar', {
            type: 'image',
            url: getPath(),
            coordinates: [
                [-80.425, 46.437],
                [-71.516, 46.437],
                [-71.516, 37.936],
                [-80.425, 37.936]
            ]
        });
        map.addLayer({
            id: 'radar-layer',
            'type': 'raster',
            'source': 'radar',
            'paint': {
                'raster-fade-duration': 0
            }
        });

        setInterval(function () {
            currentImage = (currentImage + 1) % frameCount;
            map.getSource('radar').updateImage({ url: getPath() });
        }, 200);
    });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Animate a series of images</title>
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
            center: [-75.789, 41.874],
            zoom: 5
        });

        const frameCount = 5;
            let currentImage = 0;

            function getPath() {
                return (
                    'https://docs.maptiler.com/sdk-js/assets/radar' +
                    currentImage +
                    '.gif'
                );
            }

            map.on('load', function () {
                map.addSource('radar', {
                    type: 'image',
                    url: getPath(),
                    coordinates: [
                        [-80.425, 46.437],
                        [-71.516, 46.437],
                        [-71.516, 37.936],
                        [-80.425, 37.936]
                    ]
                });
                map.addLayer({
                    id: 'radar-layer',
                    'type': 'raster',
                    'source': 'radar',
                    'paint': {
                        'raster-fade-duration': 0
                    }
                });

                setInterval(function () {
                    currentImage = (currentImage + 1) % frameCount;
                    map.getSource('radar').updateImage({ url: getPath() });
                }, 200);
            });
    </script>
</body>
</html>
```
