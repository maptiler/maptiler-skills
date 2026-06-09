# Source: https://docs.maptiler.com/sdk-js/examples/rich-text-format/

# Display a map

Use the [`Formatted`](/gl-style-specification/types/#formatted) type to display visually appealing text labels featuring both text and icons sourced from image URLs. This versatile type enables the presentation of rich content in a visually engaging manner.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element to render the map
        style: maptilersdk.MapStyle.DATAVIZ.LIGHT,
        center: [-93.96, 38.14],
        zoom: 4.58
      });

      map.on('load', async function () {

        map.addSource('states', {
          'type': 'geojson',
          'data': 'https://docs.maptiler.com/sdk-js/assets/us_states.geojson'
        });
      
        map.addLayer({
          'id': 'state-fills',
          'type': 'fill',
          'source': 'states',
          'layout': {},
          'paint': {
              'fill-color': "#D3DBEC",
              'fill-opacity': 0.8,
              'fill-outline-color': "rgba(255, 255, 255, 1)"
          }
        });

        map.addLayer({
          'id': 'labels',
          'type': 'symbol',
          'source': 'states',
          'layout': {
            'text-field': ["format",
              ["image", ['downcase', ['get', 'ABBREVIATION']]],
              '\n',
              ['get', 'STATE_NAME'], { "font-scale": 0.8 },
              '\n',
              ['get', 'ABBREVIATION'], { "font-scale": 0.7, "text-color": "#444952" },
              '\n',
              "People/Km2: ", { "font-scale": 0.6 },
              ['get', 'DENSITY'], { "font-scale": 0.6, "text-color": "#0E61C6", "text-font": [
                    'literal',
                    ['Noto Sans Bold', 'Arial Unicode MS Bold']
                ]},
            ]
          }
        });
      });

      map.on("styleimagemissing", async function (evt) {
        const usid = evt.id;
        const image = await map.loadImage(`https://docs.maptiler.com/sdk-js/examples/rich-text-format/img/${usid}.webp`);
        if (!map.hasImage(`${usid}`)) map.addImage(`${usid}`, image.data);
      });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Display a map</title>
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
            style: maptilersdk.MapStyle.DATAVIZ.LIGHT,
            center: [-93.96, 38.14],
            zoom: 4.58
        });

        container: 'map', // container's id or the HTML element to render the map
                style: maptilersdk.MapStyle.DATAVIZ.LIGHT,
                center: [-93.96, 38.14],
                zoom: 4.58
              });

              map.on('load', async function () {

                map.addSource('states', {
                  'type': 'geojson',
                  'data': 'https://docs.maptiler.com/sdk-js/assets/us_states.geojson'
                });

                map.addLayer({
                  'id': 'state-fills',
                  'type': 'fill',
                  'source': 'states',
                  'layout': {},
                  'paint': {
                      'fill-color': "#D3DBEC",
                      'fill-opacity': 0.8,
                      'fill-outline-color': "rgba(255, 255, 255, 1)"
                  }
                });

                map.addLayer({
                  'id': 'labels',
                  'type': 'symbol',
                  'source': 'states',
                  'layout': {
                    'text-field': ["format",
                      ["image", ['downcase', ['get', 'ABBREVIATION']]],
                      '\n',
                      ['get', 'STATE_NAME'], { "font-scale": 0.8 },
                      '\n',
                      ['get', 'ABBREVIATION'], { "font-scale": 0.7, "text-color": "#444952" },
                      '\n',
                      "People/Km2: ", { "font-scale": 0.6 },
                      ['get', 'DENSITY'], { "font-scale": 0.6, "text-color": "#0E61C6", "text-font": [
                            'literal',
                            ['Noto Sans Bold', 'Arial Unicode MS Bold']
                        ]},
                    ]
                  }
                });
              });

              map.on("styleimagemissing", async function (evt) {
                const usid = evt.id;
                const image = await map.loadImage(`https://docs.maptiler.com/sdk-js/examples/rich-text-format/img/${usid}.webp`);
                if (!map.hasImage(`${usid}`)) map.addImage(`${usid}`, image.data);
              });
    </script>
</body>
</html>
```
