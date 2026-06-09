# Source: https://docs.maptiler.com/sdk-js/examples/game-controls/

# Navigate the map with game-like controls

Use the keyboard's arrow keys to move around the map with game-like controls.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
// pixels the map pans when the up or down arrow is clicked
    const deltaDistance = 100;

    // degrees the map rotates when the left or right arrow is clicked
    const deltaDegrees = 25;

    function easing(t) {
        return t * (2 - t);
    }

    map.on('load', function () {
        map.getCanvas().focus();

        map.getCanvas().addEventListener(
            'keydown',
            function (e) {
                e.preventDefault();
                if (e.which === 38) {
                    // up
                    map.panBy([0, -deltaDistance], {
                        easing: easing
                    });
                } else if (e.which === 40) {
                    // down
                    map.panBy([0, deltaDistance], {
                        easing: easing
                    });
                } else if (e.which === 37) {
                    // left
                    map.easeTo({
                        bearing: map.getBearing() - deltaDegrees,
                        easing: easing
                    });
                } else if (e.which === 39) {
                    // right
                    map.easeTo({
                        bearing: map.getBearing() + deltaDegrees,
                        easing: easing
                    });
                }
            },
            true
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
    <title>Navigate the map with game-like controls</title>
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
            style: maptilersdk.MapStyle.TOPO,
            center: [-87.6298, 41.8781],
            zoom: 17,
            pitch: 60,
            bearing: -12
        });

        // pixels the map pans when the up or down arrow is clicked
            const deltaDistance = 100;

            // degrees the map rotates when the left or right arrow is clicked
            const deltaDegrees = 25;

            function easing(t) {
                return t * (2 - t);
            }

            map.on('load', function () {
                map.getCanvas().focus();

                map.getCanvas().addEventListener(
                    'keydown',
                    function (e) {
                        e.preventDefault();
                        if (e.which === 38) {
                            // up
                            map.panBy([0, -deltaDistance], {
                                easing: easing
                            });
                        } else if (e.which === 40) {
                            // down
                            map.panBy([0, deltaDistance], {
                                easing: easing
                            });
                        } else if (e.which === 37) {
                            // left
                            map.easeTo({
                                bearing: map.getBearing() - deltaDegrees,
                                easing: easing
                            });
                        } else if (e.which === 39) {
                            // right
                            map.easeTo({
                                bearing: map.getBearing() + deltaDegrees,
                                easing: easing
                            });
                        }
                    },
                    true
                );
            });
    </script>
</body>
</html>
```
