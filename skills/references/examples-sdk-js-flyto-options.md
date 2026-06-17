# Source: https://docs.maptiler.com/sdk-js/examples/flyto-options/

# Slowly fly to a location

Use [`flyTo`](/sdk-js/api/map/#map#flyto) with flyOptions to slowly zoom to a location.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
let isAtStart = true;

    document.getElementById('fly').addEventListener('click', function () {
      // depending on whether we're currently at point a or b, aim for
      // point a or b
      const target = isAtStart ? end : start;

      // and now we're at the opposite point
      isAtStart = !isAtStart;

      map.flyTo({
        // These options control the ending camera position: centered at
        // the target, at zoom level 9, and north up.
        center: target,
        zoom: 9,
        bearing: 0,

        // These options control the flight curve, making it move
        // slowly and zoom out almost completely before starting
        // to pan.
        speed: 0.2, // make the flying slow
        curve: 1, // change the speed at which it zooms out

        // This can be any easing function: it takes a number between
        // 0 and 1 and returns another number between 0 and 1.
        easing: function (t) {
          return t;
        },

        // this animation is considered essential with respect to prefers-reduced-motion
        essential: true
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
    <title>Slowly fly to a location</title>
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
            zoom: 9,
            bearing: 0
        });

        let isAtStart = true;

            document.getElementById('fly').addEventListener('click', function () {
              // depending on whether we're currently at point a or b, aim for
              // point a or b
              const target = isAtStart ? end : start;

              // and now we're at the opposite point
              isAtStart = !isAtStart;

              map.flyTo({
                // These options control the ending camera position: centered at
                // the target, at zoom level 9, and north up.
                center: target,
                zoom: 9,
                bearing: 0,

                // These options control the flight curve, making it move
                // slowly and zoom out almost completely before starting
                // to pan.
                speed: 0.2, // make the flying slow
                curve: 1, // change the speed at which it zooms out

                // This can be any easing function: it takes a number between
                // 0 and 1 and returns another number between 0 and 1.
                easing: function (t) {
                  return t;
                },

                // this animation is considered essential with respect to prefers-reduced-motion
                essential: true
              });
            });
    </script>
</body>
</html>
```
