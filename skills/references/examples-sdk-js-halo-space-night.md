# Source: https://docs.maptiler.com/sdk-js/examples/halo-space-night/

# Globe with halo

Use a custom map of the Earth's satellite image at night and display it on a globe with a space background.

In this example, we'll use a custom map (night satellite) along with the `halo` and `space` options to create the effect of the Earth seen from space. Additionally, we'll rotate the Earth and shift the central view of the map so that the Earth appears in the lower left corner of the map area.

To make the custom map download the images from [Earth at Night](https://earthobservatory.nasa.gov/features/NightLights/page3.php) and generat the tiles using the [MapTiler Engine](https://www.maptiler.com/engine/)

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element in which the SDK will render the map
      style: 'YOUR_CUSTOM_MAP_ID',
      projection: "globe",
      center: [115.0293, 32.6789], // starting position [lng, lat]
      zoom: 2, // starting zoom
      geolocateControl: false,
      navigationControl: false,
      terrain: true,
        space: {
        preset: 'milkyway'
      },
      halo: true,
    });

    map.easeTo({
      padding: {
        right: 500, // push the visual center to the left
        top: 300, // push the globe down
      }
    });

    function loop() {
      requestAnimationFrame(loop);
      const currentCenter = map.getCenter();

      map.flyTo({ // create globe rotation animation
        center:[
          currentCenter.lng - 0.05,
          currentCenter.lat
        ]
      });
    }

    map.on('ready', async () => {

      map.setSky({
        "sky-color": "#87CEEB",
        "fog-color": "#87CEEB",
        "horizon-color": "#FFFFFF",
        "atmosphere-blend": 0.7
      });

      // polygon used to add haze / opacity to the night side of the globe
      map.addSource('world-cover', {
        'type': 'geojson',
        'data': {
          'type': 'Polygon',
          'coordinates': [
            [
              [-180, -90],
              [180, -90],
              [180, 90],
              [-180, 90],
              [-180, -90]
            ]
          ]
        }
      });

      map.addLayer({
        'id': 'global-atmosphere-tint',
        'type': 'fill',
        'source': 'world-cover', // Use the existing full-globe polygon source
        'paint': {
          // A semi-transparent atmospheric blue color
          'fill-color': 'rgba(135, 206, 235, 1)', 
          // Ensure it's always visible
          'fill-opacity': [
            'interpolate',
            ['linear'],
            ['zoom'],
            1, 0.15, // At zoom 1, opacity is 15%
            5, 0.0   // By zoom 4, opacity is 0% (fully transparent)
          ]
        }
      });
      
      loop();
    });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Globe with halo</title>
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
            style: 'YOUR_CUSTOM_MAP_ID',
            center: [115.0293, 32.6789],
            zoom: 2
        });

        container: 'map', // container's id or the HTML element in which the SDK will render the map
              style: 'YOUR_CUSTOM_MAP_ID',
              projection: "globe",
              center: [115.0293, 32.6789], // starting position [lng, lat]
              zoom: 2, // starting zoom
              geolocateControl: false,
              navigationControl: false,
              terrain: true,
                space: {
                preset: 'milkyway'
              },
              halo: true,
            });

            map.easeTo({
              padding: {
                right: 500, // push the visual center to the left
                top: 300, // push the globe down
              }
            });

            function loop() {
              requestAnimationFrame(loop);
              const currentCenter = map.getCenter();

              map.flyTo({ // create globe rotation animation
                center:[
                  currentCenter.lng - 0.05,
                  currentCenter.lat
                ]
              });
            }

            map.on('ready', async () => {

              map.setSky({
                "sky-color": "#87CEEB",
                "fog-color": "#87CEEB",
                "horizon-color": "#FFFFFF",
                "atmosphere-blend": 0.7
              });

              // polygon used to add haze / opacity to the night side of the globe
              map.addSource('world-cover', {
                'type': 'geojson',
                'data': {
                  'type': 'Polygon',
                  'coordinates': [
                    [
                      [-180, -90],
                      [180, -90],
                      [180, 90],
                      [-180, 90],
                      [-180, -90]
                    ]
                  ]
                }
              });

              map.addLayer({
                'id': 'global-atmosphere-tint',
                'type': 'fill',
                'source': 'world-cover', // Use the existing full-globe polygon source
                'paint': {
                  // A semi-transparent atmospheric blue color
                  'fill-color': 'rgba(135, 206, 235, 1)', 
                  // Ensure it's always visible
                  'fill-opacity': [
                    'interpolate',
                    ['linear'],
                    ['zoom'],
                    1, 0.15, // At zoom 1, opacity is 15%
                    5, 0.0   // By zoom 4, opacity is 0% (fully transparent)
                  ]
                }
              });

              loop();
            });
    </script>
</body>
</html>
```
