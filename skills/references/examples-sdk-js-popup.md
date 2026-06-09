# Source: https://docs.maptiler.com/sdk-js/examples/popup/

# Display a popup

Add a [`Popup`](/sdk-js/api/markers/#popup) to the map.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const popup = new maptilersdk.Popup({ closeOnClick: false })
        .setLngLat([-96, 37.8])
        .setHTML('<h1>Hello World!</h1>')
        .addTo(map);
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Display a popup</title>
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
            center: [-96, 37.8],
            zoom: 3
        });

        const popup = new maptilersdk.Popup({ closeOnClick: false })
                .setLngLat([-96, 37.8])
                .setHTML('<h1>Hello World!</h1>')
                .addTo(map);
    </script>
</body>
</html>
```
