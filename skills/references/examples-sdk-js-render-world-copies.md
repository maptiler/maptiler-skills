# Source: https://docs.maptiler.com/sdk-js/examples/render-world-copies/

# Render world copies

Toggle between rendering a single world and multiple copies of the world using [`setRenderWorldCopies`](/sdk-js/api/map/#map#setrenderworldcopies). If `true`, multiple copies of the world will be rendered side by side beyond -180 and 180 degrees longitude.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const renderOptions = document.getElementById('menu');
    const inputs = renderOptions.getElementsByTagName('input');

    function switchRenderOption(option) {
      const status = option.target.id;
      map.setRenderWorldCopies(status === 'true');
    }

    for (let i = 0; i < inputs.length; i++) {
      inputs[i].onclick = switchRenderOption;
    }
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Render world copies</title>
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
            center: [179, 0],
            zoom: 0.01 // starting zoom
        });

        const renderOptions = document.getElementById('menu');
            const inputs = renderOptions.getElementsByTagName('input');

            function switchRenderOption(option) {
              const status = option.target.id;
              map.setRenderWorldCopies(status === 'true');
            }

            for (let i = 0; i < inputs.length; i++) {
              inputs[i].onclick = switchRenderOption;
            }
    </script>
</body>
</html>
```
