# Source: https://docs.maptiler.com/sdk-js/examples/cooperative-gestures/

# Cooperative gestures

This example shows how to enable cooperative gestures with a specific language.

<sup>See how it behaves: on desktop, zoom using the mouse wheel. On mobile, touch and move the map.</sup>

<div class="mt-n2"><sup>Windows: Use Ctrl + scroll to zoom the map.</sup></div>

<div><sup>Mac: Use ⌘ + scroll to zoom the map.</sup></div>

<div><sup>Mobile: Use two fingers to move the map.</sup></div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript

```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Cooperative gestures</title>
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
            center: [-77.04, 38.907],
            zoom: 11.15
        });


    </script>
</body>
</html>
```
