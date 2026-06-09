# Source: https://docs.maptiler.com/sdk-js/examples/space-milkyway/

# Globe with space background

Use the `space` **preset** option in the map constructor to provide a more realistic space background for your maps.

This option **only takes effect** when used in conjunction with the `projection: 'globe'` parameter.

In this example, we'll use a Milky Way background, but you can choose: star backgrounds, space backgrounds, and more. See all the [predefined presets backgrounds](/sdk-js/api/types/#predefined-presets-usage).

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element in which the SDK will render the map
      style: maptilersdk.MapStyle.SATELLITE,
      projection: "globe",
      zoom: 1,
      center: [75.9, 26.9],
      space: {
        preset: "milkyway-bright"
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
            center: [75.9, 26.9],
            zoom: 1
        });

        container: 'map', // container's id or the HTML element in which the SDK will render the map
              style: maptilersdk.MapStyle.SATELLITE,
              projection: "globe",
              zoom: 1,
              center: [75.9, 26.9],
              space: {
                preset: "milkyway-bright"
              }
            });
    </script>
</body>
</html>
```
