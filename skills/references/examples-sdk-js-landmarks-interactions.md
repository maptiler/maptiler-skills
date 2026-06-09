# Source: https://docs.maptiler.com/sdk-js/examples/landmarks-interactions/

# Landmark interactions

In this tutorial, you'll learn how to create a map with custom landmarks and add interactions to it.

<sup>Click on a landmark to open a popup with the landmark information</sup>

1. Check out the step-by-step guide on [Creating a Custom Dataset (GeoJSON)](/guides/map-design/creating-a-custom-vector-dataset-geojson) to create your desired landmarks.

1. Follow the tutorial [How to Add Custom Landmarks to Your Map](/guides/map-design/how-to-add-custom-landmarks-to-your-map), to create a map with the desired landmarks.

1. We already have our map designed, now we are going to use it to create an interactive web map with our landmarks and get their information when you click on them. Just copy the below code:

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', function () {
      const layerName = 'NAME_OF_YOUR_LANDMARKS_LAYER' // Replace with the name of the layer containing your landmarks.

      // When a click event occurs on a feature in the places layer, open a popup at the
      // location of the feature, with description HTML from its properties.
      map.on('click', layerName, function (e) {
        const coordinates = e.features[0].geometry.coordinates.slice();
        const description = e.features[0].properties.description;

        // Ensure that if the map is zoomed out such that multiple
        // copies of the feature are visible, the popup appears
        // over the copy being pointed to.
        while (Math.abs(e.lngLat.lng - coordinates[0]) > 180) {
          coordinates[0] += e.lngLat.lng > coordinates[0] ? 360 : -360;
        }

        // Update the popup content to display properties of the feature created in step 1.
        const content = `
          <h3>${e.features[0].properties.title}</h3>
          <p>${description.slice(0, 300)}...</p>
          <a href="${e.features[0].properties.link}" target="_blank">More info</a>
        `;

        // Adjust the offset as needed based on the styling of the landmark layer.
        new maptilersdk.Popup({ offset: 40 })
          .setLngLat(coordinates)
          .setHTML(content)
          .addTo(map);
      });

      // Change the cursor to a pointer when the mouse is over the places layer.
      map.on('mouseenter', layerName, function () {
        map.getCanvas().style.cursor = 'pointer';
      });

      // Change it back to a pointer when it leaves.
      map.on('mouseleave', layerName, function () {
        map.getCanvas().style.cursor = '';
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
    <title>Landmark interactions</title>
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
            center: [12.5, 41.9],
            zoom: 14
        });

        map.on('load', function () {
              const layerName = 'NAME_OF_YOUR_LANDMARKS_LAYER' // Replace with the name of the layer containing your landmarks.

              // When a click event occurs on a feature in the places layer, open a popup at the
              // location of the feature, with description HTML from its properties.
              map.on('click', layerName, function (e) {
                const coordinates = e.features[0].geometry.coordinates.slice();
                const description = e.features[0].properties.description;

                // Ensure that if the map is zoomed out such that multiple
                // copies of the feature are visible, the popup appears
                // over the copy being pointed to.
                while (Math.abs(e.lngLat.lng - coordinates[0]) > 180) {
                  coordinates[0] += e.lngLat.lng > coordinates[0] ? 360 : -360;
                }

                // Update the popup content to display properties of the feature created in step 1.
                const content = `
                  <h3>${e.features[0].properties.title}</h3>
                  <p>${description.slice(0, 300)}...</p>
                  <a href="${e.features[0].properties.link}" target="_blank">More info</a>
                `;

                // Adjust the offset as needed based on the styling of the landmark layer.
                new maptilersdk.Popup({ offset: 40 })
                  .setLngLat(coordinates)
                  .setHTML(content)
                  .addTo(map);
              });

              // Change the cursor to a pointer when the mouse is over the places layer.
              map.on('mouseenter', layerName, function () {
                map.getCanvas().style.cursor = 'pointer';
              });

              // Change it back to a pointer when it leaves.
              map.on('mouseleave', layerName, function () {
                map.getCanvas().style.cursor = '';
              });
            });
    </script>
</body>
</html>
```
