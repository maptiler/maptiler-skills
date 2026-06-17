# Source: https://docs.maptiler.com/sdk-js/examples/flyto/

# Fly to a location

Use [`flyTo`](/sdk-js/api/map/#map#flyto) to smoothly interpolate between locations.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
//

    document.getElementById('fly').addEventListener('click', function () {
      // Fly to a random location by offsetting the point 74.241, 41.201
      // by up to 5 degrees.
      map.flyTo({
        center: [
          74.241 + (Math.random() - 0.5) * 10,
          41.201 + (Math.random() - 0.5) * 10
        ],
        essential: true // this animation is considered essential with respect to prefers-reduced-motion
      });
    });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Fly to a location</title>
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
            center: [74.241, 41.201],
            zoom: 6.16
        });

        //

            document.getElementById('fly').addEventListener('click', function () {
              // Fly to a random location by offsetting the point 74.241, 41.201
              // by up to 5 degrees.
              map.flyTo({
                center: [
                  74.241 + (Math.random() - 0.5) * 10,
                  41.201 + (Math.random() - 0.5) * 10
                ],
                essential: true // this animation is considered essential with respect to prefers-reduced-motion
              });
            });
    </script>
</body>
</html>
```
