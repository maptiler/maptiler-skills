# Source: https://docs.maptiler.com/sdk-js/examples/animate-a-line/

# Animate a line

Animate a line by updating a GeoJSON source on each frame.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
// Create a GeoJSON source with an empty lineString.
    const geojson = {
        'type': 'FeatureCollection',
        'features': [
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'LineString',
                    'coordinates': [[0, 0]]
                }
            }
        ]
    };

    const speedFactor = 30; // number of frames per longitude degree
    let animation; // to store and cancel the animation
    let startTime = 0;
    let progress = 0; // progress = timestamp - startTime
    let resetTime = false; // indicator of whether time reset is needed for the animation
    const pauseButton = document.getElementById('pause');

    map.on('load', function () {
        map.addSource('line', {
            'type': 'geojson',
            'data': geojson
        });

        // add the line which will be modified in the animation
        map.addLayer({
            'id': 'line-animation',
            'type': 'line',
            'source': 'line',
            'layout': {
                'line-cap': 'round',
                'line-join': 'round'
            },
            'paint': {
                'line-color': '#ed6498',
                'line-width': 5,
                'line-opacity': 0.8
            }
        });

        startTime = performance.now();

        animateLine();

        // click the button to pause or play
        pauseButton.addEventListener('click', function () {
            pauseButton.classList.toggle('pause');
            if (pauseButton.classList.contains('pause')) {
                cancelAnimationFrame(animation);
            } else {
                resetTime = true;
                animateLine();
            }
        });

        // reset startTime and progress once the tab loses or gains focus
        // requestAnimationFrame also pauses on hidden tabs by default
        document.addEventListener('visibilitychange', function () {
            resetTime = true;
        });

        // animated in a circle as a sine wave along the map.
        function animateLine(timestamp) {
            if (resetTime) {
                // resume previous progress
                startTime = performance.now() - progress;
                resetTime = false;
            } else {
                progress = timestamp - startTime;
            }

            // restart if it finishes a loop
            if (progress > speedFactor * 360) {
                startTime = timestamp;
                geojson.features[0].geometry.coordinates = [];
            } else {
                const  x = progress / speedFactor;
                // draw a sine wave with some math.
                const  y = Math.sin((x * Math.PI) / 90) * 40;
                // append new coordinates to the lineString
                geojson.features[0].geometry.coordinates.push([x, y]);
                // then update the map
                map.getSource('line').setData(geojson);
            }
            // Request the next frame of the animation.
            animation = requestAnimationFrame(animateLine);
        }
    });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Animate a line</title>
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
            zoom: 0.5
        });

        // Create a GeoJSON source with an empty lineString.
            const geojson = {
                'type': 'FeatureCollection',
                'features': [
                    {
                        'type': 'Feature',
                        'geometry': {
                            'type': 'LineString',
                            'coordinates': [[0, 0]]
                        }
                    }
                ]
            };

            const speedFactor = 30; // number of frames per longitude degree
            let animation; // to store and cancel the animation
            let startTime = 0;
            let progress = 0; // progress = timestamp - startTime
            let resetTime = false; // indicator of whether time reset is needed for the animation
            const pauseButton = document.getElementById('pause');

            map.on('load', function () {
                map.addSource('line', {
                    'type': 'geojson',
                    'data': geojson
                });

                // add the line which will be modified in the animation
                map.addLayer({
                    'id': 'line-animation',
                    'type': 'line',
                    'source': 'line',
                    'layout': {
                        'line-cap': 'round',
                        'line-join': 'round'
                    },
                    'paint': {
                        'line-color': '#ed6498',
                        'line-width': 5,
                        'line-opacity': 0.8
                    }
                });

                startTime = performance.now();

                animateLine();

                // click the button to pause or play
                pauseButton.addEventListener('click', function () {
                    pauseButton.classList.toggle('pause');
                    if (pauseButton.classList.contains('pause')) {
                        cancelAnimationFrame(animation);
                    } else {
                        resetTime = true;
                        animateLine();
                    }
                });

                // reset startTime and progress once the tab loses or gains focus
                // requestAnimationFrame also pauses on hidden tabs by default
                document.addEventListener('visibilitychange', function () {
                    resetTime = true;
                });

                // animated in a circle as a sine wave along the map.
                function animateLine(timestamp) {
                    if (resetTime) {
                        // resume previous progress
                        startTime = performance.now() - progress;
                        resetTime = false;
                    } else {
                        progress = timestamp - startTime;
                    }

                    // restart if it finishes a loop
                    if (progress > speedFactor * 360) {
                        startTime = timestamp;
                        geojson.features[0].geometry.coordinates = [];
                    } else {
                        const  x = progress / speedFactor;
                        // draw a sine wave with some math.
                        const  y = Math.sin((x * Math.PI) / 90) * 40;
                        // append new coordinates to the lineString
                        geojson.features[0].geometry.coordinates.push([x, y]);
                        // then update the map
                        map.getSource('line').setData(geojson);
                    }
                    // Request the next frame of the animation.
                    animation = requestAnimationFrame(animateLine);
                }
            });
    </script>
</body>
</html>
```
