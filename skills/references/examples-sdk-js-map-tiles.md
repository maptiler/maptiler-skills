# Source: https://docs.maptiler.com/sdk-js/examples/map-tiles/

# Add a raster tile source

To enhance your map, you have the option to incorporate a third-party raster source into the map. This could involve integrating satellite maps or drone images, as well as other raster layers like historical maps, for example. By doing so, you can enrich the visual representation and expand the range of information provided on your map.

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
    <title>Add a raster tile source</title>
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
            style: {,
            center: [-74.5, 40],
            zoom: 2 // starting zoom
        });


    </script>
</body>
</html>
```
