# Source: https://docs.maptiler.com/sdk-js/examples/set-popup/

# Attach a popup to a marker instance

Attach a [`Popup`](/sdk-js/api/markers/#popup) to a [Marker](/sdk-js/api/markers/#marker) and display it when the user clicks on the Marker.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
// create the popup
    const popup = new maptilersdk.Popup({ offset: 25 }).setText(
        'Construction on the Washington Monument began in 1848.'
    );

    // create DOM element for the marker
    const el = document.createElement('div');
    el.id = 'marker';

    // create the marker
    new maptilersdk.Marker({element: el})
        .setLngLat(monument)
        .setPopup(popup) // sets a popup on this marker
        .addTo(map);
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Attach a popup to a marker instance</title>
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
            zoom: 15
        });

        // create the popup
            const popup = new maptilersdk.Popup({ offset: 25 }).setText(
                'Construction on the Washington Monument began in 1848.'
            );

            // create DOM element for the marker
            const el = document.createElement('div');
            el.id = 'marker';

            // create the marker
            new maptilersdk.Marker({element: el})
                .setLngLat(monument)
                .setPopup(popup) // sets a popup on this marker
                .addTo(map);
    </script>
</body>
</html>
```
