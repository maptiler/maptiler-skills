# Source: https://docs.maptiler.com/sdk-js/examples/space-simple/

# Globe with space background

Use the `space:true` option in the map constructor to simulating a deep space background. This feature allows customizing the background environment of the globe, simulating deep space or skybox effects.

This option **only takes effect** when used in conjunction with the `projection: 'globe'` parameter.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element in which the SDK will render the map
      style: maptilersdk.MapStyle.SATELLITE,
      projection: "globe",
      space: true
    });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Globe with space background</title>
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
            center: [0, 0],
            zoom: 0
        });

        container: 'map', // container's id or the HTML element in which the SDK will render the map
              style: maptilersdk.MapStyle.SATELLITE,
              projection: "globe",
              space: true
            });
    </script>
</body>
</html>
```
