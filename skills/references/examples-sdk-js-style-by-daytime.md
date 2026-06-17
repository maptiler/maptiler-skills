# Source: https://docs.maptiler.com/sdk-js/examples/style-by-daytime/

# How to change the style (light/dark) of the map based on the time of day

This example demonstrates the process of altering the map display from a light to a dark mode, depending on the current time of day.

To achieve this, the [MapTiler Geolocation API](https://docs.maptiler.com/cloud/api/geolocation/){:target="_blank" rel="noopener"} is utilized to acquire the user's location data, while the [SunCalc library](https://github.com/mourner/suncalc){:target="_blank" rel="noopener"} is employed to compute the sunrise and sunset timings based on the user's location.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
});

    document.getElementById("appt").addEventListener('change', function() {
      const hours = dateFromHours(this.value);
      if (isDay(hours) && activeMode == "dark") {
        switchMode("light");
      } else if (!isDay(hours) && activeMode == "light") {
        switchMode("dark");
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
    <title>How to change the style (light/dark) of the map based on the time of day</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.13.1/font/bootstrap-icons.css" rel="stylesheet" />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/suncalc/1.9.0/suncalc.min.js"></script>
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
            center: [0, 0],
            zoom: 12
        });

        });

            document.getElementById("appt").addEventListener('change', function() {
              const hours = dateFromHours(this.value);
              if (isDay(hours) && activeMode == "dark") {
                switchMode("light");
              } else if (!isDay(hours) && activeMode == "light") {
                switchMode("dark");
              }
            });
    </script>
</body>
</html>
```
