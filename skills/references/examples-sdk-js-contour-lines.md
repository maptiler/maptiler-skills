# Source: https://docs.maptiler.com/sdk-js/examples/contour-lines/

# Add Contour Lines

This example shows how to add contour lines to your map from a raster-dem source. In this particular case, the contour lines are generated dynamically on the client side, specifically in the browser, through the utilization of the maplibre-contour plugin.

If you require accurate and precise contour lines, it is advisable to utilize the data derived from the [Global Contours offered by MapTiler](https://cloud.maptiler.com/tiles/contours/).

The Global Contours, created by MapTiler, contains contour lines for locations all around the globe in two widely used unit systems: meters and feet. With its global coverage, MapTiler's contour lines can be utilized for various purposes, such as outdoor recreation planning, landscape analysis, and cartographic visualization.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const demSource = new mlcontour.DemSource({
      url: `https://api.maptiler.com/tiles/terrain-rgb-v2/{z}/{x}/{y}.webp?key=${maptilersdk.config.apiKey}`,
      encoding: 'mapbox',
      maxzoom: 12,
      // offload contour line computation to a web worker
      worker: true
    });

    // calls maplibregl.addProtocol to register a dynamic vector tile provider that
    // downloads raster-dem tiles, computes contour lines, and encodes as a vector
    // tile for each tile request from maplibre
    demSource.setupMaplibre(maptilersdk);

    map.on('load', function () {
      map.addSource("hillshadeSource", {
        "type": "raster-dem",
        // share cached raster-dem tiles with the contour source
        tiles: [demSource.sharedDemProtocolUrl],
        maxzoom: 14
      });

      map.addSource("contourSourceFeet", {
        type: 'vector',
        tiles: [
          demSource.contourProtocolUrl({
            // meters to feet
            multiplier: 3.28084,
            overzoom: 1,
            thresholds: {
              // zoom: [minor, major]
              11: [200, 1000],
              12: [100, 500],
              13: [100, 500],
              14: [50, 200],
              15: [20, 100]
            },
            elevationKey: 'ele',
            levelKey: 'level',
            contourLayer: 'contours'
          })
        ],
        maxzoom: 15
      });

      map.addLayer({
        id: 'hills',
        type: 'hillshade',
        source: 'hillshadeSource',
        layout: { visibility: 'visible' },
        paint: { 'hillshade-exaggeration': 0.25 }
      });

      map.addLayer({
        id: 'contours',
        type: 'line',
        source: 'contourSourceFeet',
        'source-layer': 'contours',
        paint: {
          'line-opacity': 0.5,
          // "major" contours have level=1, "minor" have level=0
          'line-width': ['match', ['get', 'level'], 1, 1, 0.5]
        }
      });

      map.addLayer({
        id: 'contour-text',
        type: 'symbol',
        source: 'contourSourceFeet',
        'source-layer': 'contours',
        filter: ['>', ['get', 'level'], 0],
        paint: {
          'text-halo-color': 'white',
          'text-halo-width': 1
        },
        layout: {
          'symbol-placement': 'line',
          'text-size': 10,
          'text-field': [
            'concat',
            ['number-format', ['get', 'ele'], {}],
            '\''
          ],
          'text-font': ['Noto Sans Bold']
        }
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
    <title>Add Contour Lines</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <script src="https://unpkg.com/maplibre-contour@0.0.5/dist/index.min.js"></script>
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
            style: DATAVIZ.LIGHT,
            center: [-148.63567, 62.03381],
            zoom: 13.42
        });

        const demSource = new mlcontour.DemSource({
              url: `https://api.maptiler.com/tiles/terrain-rgb-v2/{z}/{x}/{y}.webp?key=${maptilersdk.config.apiKey}`,
              encoding: 'mapbox',
              maxzoom: 12,
              // offload contour line computation to a web worker
              worker: true
            });

            // calls maplibregl.addProtocol to register a dynamic vector tile provider that
            // downloads raster-dem tiles, computes contour lines, and encodes as a vector
            // tile for each tile request from maplibre
            demSource.setupMaplibre(maptilersdk);

            map.on('load', function () {
              map.addSource("hillshadeSource", {
                "type": "raster-dem",
                // share cached raster-dem tiles with the contour source
                tiles: [demSource.sharedDemProtocolUrl],
                maxzoom: 14
              });

              map.addSource("contourSourceFeet", {
                type: 'vector',
                tiles: [
                  demSource.contourProtocolUrl({
                    // meters to feet
                    multiplier: 3.28084,
                    overzoom: 1,
                    thresholds: {
                      // zoom: [minor, major]
                      11: [200, 1000],
                      12: [100, 500],
                      13: [100, 500],
                      14: [50, 200],
                      15: [20, 100]
                    },
                    elevationKey: 'ele',
                    levelKey: 'level',
                    contourLayer: 'contours'
                  })
                ],
                maxzoom: 15
              });

              map.addLayer({
                id: 'hills',
                type: 'hillshade',
                source: 'hillshadeSource',
                layout: { visibility: 'visible' },
                paint: { 'hillshade-exaggeration': 0.25 }
              });

              map.addLayer({
                id: 'contours',
                type: 'line',
                source: 'contourSourceFeet',
                'source-layer': 'contours',
                paint: {
                  'line-opacity': 0.5,
                  // "major" contours have level=1, "minor" have level=0
                  'line-width': ['match', ['get', 'level'], 1, 1, 0.5]
                }
              });

              map.addLayer({
                id: 'contour-text',
                type: 'symbol',
                source: 'contourSourceFeet',
                'source-layer': 'contours',
                filter: ['>', ['get', 'level'], 0],
                paint: {
                  'text-halo-color': 'white',
                  'text-halo-width': 1
                },
                layout: {
                  'symbol-placement': 'line',
                  'text-size': 10,
                  'text-field': [
                    'concat',
                    ['number-format', ['get', 'ele'], {}],
                    '\''
                  ],
                  'text-font': ['Noto Sans Bold']
                }
              });

            });
    </script>
</body>
</html>
```
