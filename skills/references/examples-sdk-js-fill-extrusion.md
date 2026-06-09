# Source: https://docs.maptiler.com/sdk-js/examples/fill-extrusion/

# Create and style clusters

This map of Europe presents a 3D choropleth map representation, where countries are visually extruded based on data provided by an external dataset. The fill-extrusion-height paint property is employed to assign data-driven values to the polygons of different countries within the fill-extrusion layer.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', function () {
        map.addSource('countries', {
          'type': 'geojson',
          'data': 'https://docs.maptiler.com/sdk-js/assets/Mean_age_of_women_at_first_marriage_in_2019.geojson',
        });

        map.addLayer(
          {
            'id': 'eu-countries',
            'source': 'countries',
            'type': 'fill-extrusion',
            'paint': {
              'fill-extrusion-color': [
                'interpolate',
                ['linear'],
                ['get', 'age'],
                23.0,
                '#fff5eb',
                24.0,
                '#fee6ce',
                25.0,
                '#fdd0a2',
                26.0,
                '#fdae6b',
                27.0,
                '#fd8d3c',
                28.0,
                '#f16913',
                29.0,
                '#d94801',
                30.0,
                '#8c2d04'
              ],
              'fill-extrusion-opacity': 1,
              'fill-extrusion-height': ['*', ['get', 'age'], 5000]
            }
          }, 'Airport labels'
        );

        //Hide country borders for better visualization
        map.setLayoutProperty('Other border', 'visibility', 'none');
        map.setLayoutProperty('Disputed border', 'visibility', 'none');
        map.setLayoutProperty('Country border', 'visibility', 'none');

      });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Create and style clusters</title>
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
            center: [19.43, 49.49],
            zoom: 3,
            pitch: 60
        });

        map.on('load', function () {
                map.addSource('countries', {
                  'type': 'geojson',
                  'data': 'https://docs.maptiler.com/sdk-js/assets/Mean_age_of_women_at_first_marriage_in_2019.geojson',
                });

                map.addLayer(
                  {
                    'id': 'eu-countries',
                    'source': 'countries',
                    'type': 'fill-extrusion',
                    'paint': {
                      'fill-extrusion-color': [
                        'interpolate',
                        ['linear'],
                        ['get', 'age'],
                        23.0,
                        '#fff5eb',
                        24.0,
                        '#fee6ce',
                        25.0,
                        '#fdd0a2',
                        26.0,
                        '#fdae6b',
                        27.0,
                        '#fd8d3c',
                        28.0,
                        '#f16913',
                        29.0,
                        '#d94801',
                        30.0,
                        '#8c2d04'
                      ],
                      'fill-extrusion-opacity': 1,
                      'fill-extrusion-height': ['*', ['get', 'age'], 5000]
                    }
                  }, 'Airport labels'
                );

                //Hide country borders for better visualization
                map.setLayoutProperty('Other border', 'visibility', 'none');
                map.setLayoutProperty('Disputed border', 'visibility', 'none');
                map.setLayoutProperty('Country border', 'visibility', 'none');

              });
    </script>
</body>
</html>
```
