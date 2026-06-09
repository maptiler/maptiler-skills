# Source: https://docs.maptiler.com/sdk-js/examples/sky-fog-terrain/

# Set Sky, Fog, Terrain

This tutorial shows how to create a map with sky, fog, and terrain and display it on a web page using MapTiler.

These features help improve the visual quality of your maps and create a more realistic environment. Adding fog and a dynamic sky enhances depth, while terrain makes elevation more visible, resulting in a more engaging map experience.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element in which the SDK will render the map
      style: maptilersdk.MapStyle.HYBRID,
      center: [8.02912, 46.53248], // starting position [lng, lat]
      zoom: 13.16, // starting zoom
      bearing: 0,
      pitch: 76,
      hash: true,
      maxPitch: 85,
      terrainControl: true,
      terrain: true
    });

    function setSkyFromUi() {
      // if sky should not be enabled set sky to undefined
      if (!document.getElementById('sky-enabled').checked) {
        map.setSky(undefined);
        return;
      }
      // setSky from UI (takes values from sliders)
      map.setSky({
        'sky-color': document.getElementById('sky-color-picker').value,
        'sky-horizon-blend': +document.getElementById('sky-horizon-blend-slider').value,
        'horizon-color': document.getElementById('horizon-color-picker').value,
        'horizon-fog-blend': +document.getElementById('horizon-fog-blend-slider').value,
        'fog-color': document.getElementById('fog-color-picker').value,
        'fog-ground-blend': +document.getElementById('fog-ground-blend-slider').value
      });
    }

    map.on('load', () => {
      document.getElementById('sky-color-picker').addEventListener('change', setSkyFromUi);
      document.getElementById('horizon-color-picker').addEventListener('change', setSkyFromUi);
      document.getElementById('fog-color-picker').addEventListener('change', setSkyFromUi);
      document.getElementById('sky-horizon-blend-slider').addEventListener('change', setSkyFromUi);
      document.getElementById('horizon-fog-blend-slider').addEventListener('change', setSkyFromUi);
      document.getElementById('fog-ground-blend-slider').addEventListener('change', setSkyFromUi);
      document.getElementById('sky-enabled').addEventListener('change', setSkyFromUi);
      setSkyFromUi();
    });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Set Sky, Fog, Terrain</title>
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
            style: maptilersdk.MapStyle.HYBRID,
            center: [8.02912, 46.53248],
            zoom: 13.16,
            pitch: 76,
            bearing: 0
        });

        container: 'map', // container's id or the HTML element in which the SDK will render the map
              style: maptilersdk.MapStyle.HYBRID,
              center: [8.02912, 46.53248], // starting position [lng, lat]
              zoom: 13.16, // starting zoom
              bearing: 0,
              pitch: 76,
              hash: true,
              maxPitch: 85,
              terrainControl: true,
              terrain: true
            });

            function setSkyFromUi() {
              // if sky should not be enabled set sky to undefined
              if (!document.getElementById('sky-enabled').checked) {
                map.setSky(undefined);
                return;
              }
              // setSky from UI (takes values from sliders)
              map.setSky({
                'sky-color': document.getElementById('sky-color-picker').value,
                'sky-horizon-blend': +document.getElementById('sky-horizon-blend-slider').value,
                'horizon-color': document.getElementById('horizon-color-picker').value,
                'horizon-fog-blend': +document.getElementById('horizon-fog-blend-slider').value,
                'fog-color': document.getElementById('fog-color-picker').value,
                'fog-ground-blend': +document.getElementById('fog-ground-blend-slider').value
              });
            }

            map.on('load', () => {
              document.getElementById('sky-color-picker').addEventListener('change', setSkyFromUi);
              document.getElementById('horizon-color-picker').addEventListener('change', setSkyFromUi);
              document.getElementById('fog-color-picker').addEventListener('change', setSkyFromUi);
              document.getElementById('sky-horizon-blend-slider').addEventListener('change', setSkyFromUi);
              document.getElementById('horizon-fog-blend-slider').addEventListener('change', setSkyFromUi);
              document.getElementById('fog-ground-blend-slider').addEventListener('change', setSkyFromUi);
              document.getElementById('sky-enabled').addEventListener('change', setSkyFromUi);
              setSkyFromUi();
            });
    </script>
</body>
</html>
```
