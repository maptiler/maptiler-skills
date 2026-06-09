# Source: https://docs.maptiler.com/sdk-js/examples/animate-point-along-line/

# Animate a point

Animate the position of a point by updating a GeoJSON source on each frame.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const radius = 20;

    function pointOnCircle(angle) {
        return {
            'type': 'Point',
            'coordinates': [Math.cos(angle) * radius, Math.sin(angle) * radius]
        };
    }

    map.on('load', function () {
        // Add a source and layer displaying a point which will be animated in a circle.
        map.addSource('point', {
            'type': 'geojson',
            'data': pointOnCircle(0)
        });

        map.addLayer({
            'id': 'point',
            'source': 'point',
            'type': 'circle',
            'paint': {
                'circle-radius': 10,
                'circle-color': '#007cbf'
            }
        });

        function animateMarker(timestamp) {
            // Update the data to a new position based on the animation timestamp. The
            // divisor in the expression `timestamp / 1000` controls the animation speed.
            map.getSource('point').setData(pointOnCircle(timestamp / 1000));

            // Request the next frame of the animation.
            requestAnimationFrame(animateMarker);
        }

        // Start the animation.
        animateMarker(0);
    });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Animate a point</title>
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
            zoom: 2
        });

        const radius = 20;

            function pointOnCircle(angle) {
                return {
                    'type': 'Point',
                    'coordinates': [Math.cos(angle) * radius, Math.sin(angle) * radius]
                };
            }

            map.on('load', function () {
                // Add a source and layer displaying a point which will be animated in a circle.
                map.addSource('point', {
                    'type': 'geojson',
                    'data': pointOnCircle(0)
                });

                map.addLayer({
                    'id': 'point',
                    'source': 'point',
                    'type': 'circle',
                    'paint': {
                        'circle-radius': 10,
                        'circle-color': '#007cbf'
                    }
                });

                function animateMarker(timestamp) {
                    // Update the data to a new position based on the animation timestamp. The
                    // divisor in the expression `timestamp / 1000` controls the animation speed.
                    map.getSource('point').setData(pointOnCircle(timestamp / 1000));

                    // Request the next frame of the animation.
                    requestAnimationFrame(animateMarker);
                }

                // Start the animation.
                animateMarker(0);
            });
    </script>
</body>
</html>
```
