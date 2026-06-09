# Source: https://docs.maptiler.com/sdk-js/examples/toggle-interaction-handlers/

# Toggle interactions

Enable or disable UI handlers on a map.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
document
        .getElementById('listing-group')
        .addEventListener('change', function (e) {
            const handler = e.target.id;
            if (e.target.checked) {
                map[handler].enable();
            } else {
                map[handler].disable();
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
    <title>Toggle interactions</title>
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
            center: [103.8382, 1.3565],
            zoom: 10.71
        });

        document
                .getElementById('listing-group')
                .addEventListener('change', function (e) {
                    const handler = e.target.id;
                    if (e.target.checked) {
                        map[handler].enable();
                    } else {
                        map[handler].disable();
                    }
                });
    </script>
</body>
</html>
```
