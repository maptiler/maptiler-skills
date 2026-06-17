# Source: https://docs.maptiler.com/sdk-js/examples/camera-animation/

# Customize camera animations

Customize camera animations using [`AnimationOptions`](/sdk-js/api/properties/#animationoptions).

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', function () {
      // add a layer to display the map's center point
      map.addSource('center', {
        'type': 'geojson',
        'data': {
          'type': 'Point',
          'coordinates': [-94, 40]
        }
      });
      map.addLayer({
        'id': 'center',
        'type': 'symbol',
        'source': 'center',
        'layout': {
          'icon-image': 'marker-15',
          'text-field': 'Center: [-94, 40]',
          'text-font': ['Open Sans Semibold', 'Arial Unicode MS Bold'],
          'text-offset': [0, 0.6],
          'text-anchor': 'top'
        }
      });

      const animateButton = document.getElementById('animateButton');
      animateButton.addEventListener('click', function () {
        const easingInput = document.getElementById('easing');
        const easingFn =
          easingFunctions[
          easingInput.options[easingInput.selectedIndex].value
          ];
        const duration = parseInt(durationInput.value, 10);
        const animate = animateValue.checked;
        const offsetX = parseInt(
          document.getElementById('offset-x').value,
          10
        );
        const offsetY = parseInt(
          document.getElementById('offset-y').value,
          10
        );

        const animationOptions = {
          duration: duration,
          easing: easingFn,
          offset: [offsetX, offsetY],
          animate: animate,
          essential: true // animation will happen even if user has `prefers-reduced-motion` setting on
        };

        // Create a random location to fly to by offsetting the map's
        // initial center point by up to 10 degrees.
        const center = [
          -95 + (Math.random() - 0.5) * 20,
          40 + (Math.random() - 0.5) * 20
        ];

        // merge animationOptions with other flyTo options
        animationOptions.center = center;

        map.flyTo(animationOptions);
        // update 'center' source and layer to show our new map center
        // compare this center point to where the camera ends up when an offset is applied
        map.getSource('center').setData({
          'type': 'Point',
          'coordinates': center
        });
        map.setLayoutProperty(
          'center',
          'text-field',
          'Center: [' +
          center[0].toFixed(1) +
          ', ' +
          center[1].toFixed(1) +
          ']'
        );
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
    <title>Customize camera animations</title>
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
            center: [-95, 40],
            zoom: 3
        });

        map.on('load', function () {
              // add a layer to display the map's center point
              map.addSource('center', {
                'type': 'geojson',
                'data': {
                  'type': 'Point',
                  'coordinates': [-94, 40]
                }
              });
              map.addLayer({
                'id': 'center',
                'type': 'symbol',
                'source': 'center',
                'layout': {
                  'icon-image': 'marker-15',
                  'text-field': 'Center: [-94, 40]',
                  'text-font': ['Open Sans Semibold', 'Arial Unicode MS Bold'],
                  'text-offset': [0, 0.6],
                  'text-anchor': 'top'
                }
              });

              const animateButton = document.getElementById('animateButton');
              animateButton.addEventListener('click', function () {
                const easingInput = document.getElementById('easing');
                const easingFn =
                  easingFunctions[
                  easingInput.options[easingInput.selectedIndex].value
                  ];
                const duration = parseInt(durationInput.value, 10);
                const animate = animateValue.checked;
                const offsetX = parseInt(
                  document.getElementById('offset-x').value,
                  10
                );
                const offsetY = parseInt(
                  document.getElementById('offset-y').value,
                  10
                );

                const animationOptions = {
                  duration: duration,
                  easing: easingFn,
                  offset: [offsetX, offsetY],
                  animate: animate,
                  essential: true // animation will happen even if user has `prefers-reduced-motion` setting on
                };

                // Create a random location to fly to by offsetting the map's
                // initial center point by up to 10 degrees.
                const center = [
                  -95 + (Math.random() - 0.5) * 20,
                  40 + (Math.random() - 0.5) * 20
                ];

                // merge animationOptions with other flyTo options
                animationOptions.center = center;

                map.flyTo(animationOptions);
                // update 'center' source and layer to show our new map center
                // compare this center point to where the camera ends up when an offset is applied
                map.getSource('center').setData({
                  'type': 'Point',
                  'coordinates': center
                });
                map.setLayoutProperty(
                  'center',
                  'text-field',
                  'Center: [' +
                  center[0].toFixed(1) +
                  ', ' +
                  center[1].toFixed(1) +
                  ']'
                );
              });
            });
    </script>
</body>
</html>
```
