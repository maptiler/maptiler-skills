# Source: https://docs.maptiler.com/sdk-js/examples/globe-projection/

# MapTiler Globe projection

This example shows how to turn on the globe projection. Creating a 3D globe view of your map requires only a single line of code. Simply include the `projection` option within the map constructor, specifying the **globe** projection.

The choice between Mercator and Globe can be done at different levels and moments in the lifecycle of the map, yet, unless stated otherwise, **Mercator remains the default**.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element to render the map
        style:  maptilersdk.MapStyle.SATELLITE,
        center: [-70.8, 0], // starting position [lng, lat]
        zoom: 1, // starting zoom
        projection: 'globe' //enable globe projection
      });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>MapTiler Globe projection</title>
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
            center: [-70.8, 0],
            zoom: 1
        });

        container: 'map', // container's id or the HTML element to render the map
                style:  maptilersdk.MapStyle.SATELLITE,
                center: [-70.8, 0], // starting position [lng, lat]
                zoom: 1, // starting zoom
                projection: 'globe' //enable globe projection
              });
    </script>
</body>
</html>
```
