# Source: https://docs.maptiler.com/sdk-js/examples/animate-marker/

# Animate a marker

Update the location of a [`Marker`](/sdk-js/api/markers/#marker) on each frame to animate its position.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const marker = new maptilersdk.Marker();

    function animateMarker(timestamp) {
        const radius = 20;

        // Update the data to a new position based on the animation timestamp. The
        // divisor in the expression `timestamp / 1000` controls the animation speed.
        marker.setLngLat([
            Math.cos(timestamp / 1000) * radius,
            Math.sin(timestamp / 1000) * radius
        ]);

        // Ensure it's added to the map. This is safe to call if it's already added.
        marker.addTo(map);

        // Request the next frame of the animation.
        requestAnimationFrame(animateMarker);
    }

    // Start the animation.
    requestAnimationFrame(animateMarker);
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Animate a marker</title>
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

        const marker = new maptilersdk.Marker();

            function animateMarker(timestamp) {
                const radius = 20;

                // Update the data to a new position based on the animation timestamp. The
                // divisor in the expression `timestamp / 1000` controls the animation speed.
                marker.setLngLat([
                    Math.cos(timestamp / 1000) * radius,
                    Math.sin(timestamp / 1000) * radius
                ]);

                // Ensure it's added to the map. This is safe to call if it's already added.
                marker.addTo(map);

                // Request the next frame of the animation.
                requestAnimationFrame(animateMarker);
            }

            // Start the animation.
            requestAnimationFrame(animateMarker);
    </script>
</body>
</html>
```
