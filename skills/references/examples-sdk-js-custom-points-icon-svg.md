# Source: https://docs.maptiler.com/sdk-js/examples/custom-points-icon-svg/

# Add custom icon (SVG) to a point layer

This example illustrates how to make a map with pins to display a point layer from a [MapTiler Tileset](https://cloud.maptiler.com/tiles/) using a custom SVG icon.

<span class="api-key-inline">Replace `YOUR_MAPTILER_TILESET_ID_HERE` with your actual [MapTiler Tileset ID](https://cloud.maptiler.com/tiles/).</span>

<span class="api-key-inline">Replace `YOUR_TILESET_LAYER_HERE` with your actual **Layer ID**. [How to get the Layer ID](/guides/general/how-to-get-tileset-layer-id/).</span>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
// Create an image from SVG
  const svgImage = new Image(35, 42);
  svgImage.onload = () => {
      map.addImage('svg', svgImage)
  }
  function svgStringToImageSrc (svgString) {
      return 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svgString)
  }

  const pin = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 70 85" fill="#0000ff">
    <path stroke-width="4" d="M 5,33.103579 C 5,17.607779 18.457,5 35,5 C 51.543,5 65,17.607779 65,33.103579 C 65,56.388679 40.4668,76.048179 36.6112,79.137779 C 36.3714,79.329879 36.2116,79.457979 36.1427,79.518879 C 35.8203,79.800879 35.4102,79.942779 35,79.942779 C 34.5899,79.942779 34.1797,79.800879 33.8575,79.518879 C 33.7886,79.457979 33.6289,79.330079 33.3893,79.138079 C 29.5346,76.049279 5,56.389379 5,33.103579 Z M 35.0001,49.386379 C 43.1917,49.386379 49.8323,42.646079 49.8323,34.331379 C 49.8323,26.016779 43.1917,19.276479 35.0001,19.276479 C 26.8085,19.276479 20.1679,26.016779 20.1679,34.331379 C 20.1679,42.646079 26.8085,49.386379 35.0001,49.386379 Z"></path>
  </svg>`;

  svgImage.src = svgStringToImageSrc(pin);

  map.on('load', function() {
    
    map.addSource('points', {
      type: 'vector',
      url: "https://api.maptiler.com/tiles/YOUR_MAPTILER_TILESET_ID_HERE/tiles.json"
    });

    map.addLayer({
      'id': 'points',
      'type': 'symbol',
      'source': 'points',
      'source-layer': 'YOUR_TILESET_LAYER_HERE',
      'layout': {
        'icon-image': 'svg',
        'icon-size': 1.0,
      },
      'paint': {}
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
    <title>Add custom icon (SVG) to a point layer</title>
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
            style: maptilersdk.MapStyle.BASE,
            center: [-73.9066, 40.7314],
            zoom: 10.21
        });

        // Create an image from SVG
          const svgImage = new Image(35, 42);
          svgImage.onload = () => {
              map.addImage('svg', svgImage)
          }
          function svgStringToImageSrc (svgString) {
              return 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svgString)
          }

          const pin = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 70 85" fill="#0000ff">
            <path stroke-width="4" d="M 5,33.103579 C 5,17.607779 18.457,5 35,5 C 51.543,5 65,17.607779 65,33.103579 C 65,56.388679 40.4668,76.048179 36.6112,79.137779 C 36.3714,79.329879 36.2116,79.457979 36.1427,79.518879 C 35.8203,79.800879 35.4102,79.942779 35,79.942779 C 34.5899,79.942779 34.1797,79.800879 33.8575,79.518879 C 33.7886,79.457979 33.6289,79.330079 33.3893,79.138079 C 29.5346,76.049279 5,56.389379 5,33.103579 Z M 35.0001,49.386379 C 43.1917,49.386379 49.8323,42.646079 49.8323,34.331379 C 49.8323,26.016779 43.1917,19.276479 35.0001,19.276479 C 26.8085,19.276479 20.1679,26.016779 20.1679,34.331379 C 20.1679,42.646079 26.8085,49.386379 35.0001,49.386379 Z"></path>
          </svg>`;

          svgImage.src = svgStringToImageSrc(pin);

          map.on('load', function() {

            map.addSource('points', {
              type: 'vector',
              url: "https://api.maptiler.com/tiles/YOUR_MAPTILER_TILESET_ID_HERE/tiles.json"
            });

            map.addLayer({
              'id': 'points',
              'type': 'symbol',
              'source': 'points',
              'source-layer': 'YOUR_TILESET_LAYER_HERE',
              'layout': {
                'icon-image': 'svg',
                'icon-size': 1.0,
              },
              'paint': {}
            });

          });
    </script>
</body>
</html>
```
