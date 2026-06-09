# Source: https://docs.maptiler.com/sdk-js/examples/style-by-settings/

# How to change the style (light/dark) of the map based on system settings

This example shows how to change the map mode (light/dark) of the map based on the system settings.

The dark mode become more and more popular. To determine whether the system settings are normal or dark, we employ the matchMedia function that allows checking programmatically whether a CSS media query (prefers-color-scheme) has been fulfilled or not.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
document.getElementById("modeSwitch").addEventListener('change', function() {
    if (this.checked && activeMode == "light") {
      switchMode("dark");
    } else if (!this.checked && activeMode == "dark") {
      switchMode("light");
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
    <title>How to change the style (light/dark) of the map based on system settings</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.13.1/font/bootstrap-icons.css" rel="stylesheet" />
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
            style: getStyleByMode(activeMode),
            center: [2.31632, 48.86239],
            zoom: 6
        });

        document.getElementById("modeSwitch").addEventListener('change', function() {
            if (this.checked && activeMode == "light") {
              switchMode("dark");
            } else if (!this.checked && activeMode == "dark") {
              switchMode("light");
            }
          });
    </script>
</body>
</html>
```
