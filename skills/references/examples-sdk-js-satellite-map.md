# Source: https://docs.maptiler.com/sdk-js/examples/satellite-map/

# Display a satellite map

Display a satellite map in your web mapping application. Our built-in styles (streets, satellite, hybrid, outdoor, winter, dark, etc.) are designed to make it easier for you to create beautiful maps. No need for extra coding or worrying about outdated versions. Check out the available [list of built-in styles](/sdk-js/api/map-styles/#mapstylelist).

[MapTiler's satellite](https://www.maptiler.com/maps/satellite/) map provides up-to-date satellite imagery for the whole world, high resolution detailed aerial imagery for many countries.

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
    <title>Display a satellite map</title>
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
            style: maptilersdk.MapStyle.SATELLITE,
            center: [17.100917, 48.142691],
            zoom: 15.71// starting zoom
        });


    </script>
</body>
</html>
```
