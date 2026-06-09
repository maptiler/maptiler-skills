# Source: https://docs.maptiler.com/sdk-js/examples/offset-vanishing-point-with-padding/

# Offset the vanishing point using padding

Offset the center or [vanishing point](https://en.wikipedia.org/wiki/Vanishing_point) of the map to reduce distortion when floating elements are displayed over the map.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
new maptilersdk.Marker().setLngLat(center).addTo(map);

    function toggleSidebar(id) {
      const elem = document.getElementById(id);
      const classes = elem.className.split(' ');
      const collapsed = classes.indexOf('collapsed') !== -1;

      const padding = {};

      if (collapsed) {
        // Remove the 'collapsed' class from the class list of the element, this sets it back to the expanded state.
        classes.splice(classes.indexOf('collapsed'), 1);

        padding[id] = 300; // In px, matches the width of the sidebars set in .sidebar CSS class
        map.easeTo({
          padding: padding,
          duration: 1000 // In ms, CSS transition duration property for the sidebar matches this value
        });
      } else {
        padding[id] = 0;
        // Add the 'collapsed' class to the class list of the element
        classes.push('collapsed');

        map.easeTo({
          padding: padding,
          duration: 1000
        });
      }

      // Update the class list on the element
      elem.className = classes.join(' ');
    }

    map.on('load', function () {
      toggleSidebar('left');
    });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Offset the vanishing point using padding</title>
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
            zoom: 12.5,
            pitch: 60
        });

        new maptilersdk.Marker().setLngLat(center).addTo(map);

            function toggleSidebar(id) {
              const elem = document.getElementById(id);
              const classes = elem.className.split(' ');
              const collapsed = classes.indexOf('collapsed') !== -1;

              const padding = {};

              if (collapsed) {
                // Remove the 'collapsed' class from the class list of the element, this sets it back to the expanded state.
                classes.splice(classes.indexOf('collapsed'), 1);

                padding[id] = 300; // In px, matches the width of the sidebars set in .sidebar CSS class
                map.easeTo({
                  padding: padding,
                  duration: 1000 // In ms, CSS transition duration property for the sidebar matches this value
                });
              } else {
                padding[id] = 0;
                // Add the 'collapsed' class to the class list of the element
                classes.push('collapsed');

                map.easeTo({
                  padding: padding,
                  duration: 1000
                });
              }

              // Update the class list on the element
              elem.className = classes.join(' ');
            }

            map.on('load', function () {
              toggleSidebar('left');
            });
    </script>
</body>
</html>
```
