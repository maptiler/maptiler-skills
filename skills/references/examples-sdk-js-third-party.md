# Source: https://docs.maptiler.com/sdk-js/examples/third-party/

# Add a third party vector tile source

To enrich your map, you have the option to incorporate a third-party vector data source into the map.

In this particular example, we are rendering vector data provided by [Mapillary](https://www.mapillary.com/developer/tiles-documentation/#sequence-layer).

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', function () {
        // Add Mapillary sequence layer.
        // https://www.mapillary.com/developer/tiles-documentation/#sequence-layer
        map.addSource('mapillary', {
            'type': 'vector',
            'tiles': [
                'https://tiles.mapillary.com/maps/vtp/mly1_public/2/{z}/{x}/{y}?access_token=YOUR_MAPILLARY_TOKEN'
            ],
            'minzoom': 6,
            'maxzoom': 14
        });
        map.addLayer(
            {
                'id': 'mapillary',
                'type': 'line',
                'source': 'mapillary',
                'source-layer': 'sequence',
                'layout': {
                    'line-cap': 'round',
                    'line-join': 'round'
                },
                'paint': {
                    'line-opacity': 0.6,
                    'line-color': 'rgb(53, 175, 109)',
                    'line-width': 2
                }
            },
            'River labels'
        );
    });

    map.addControl(new maptilersdk.NavigationControl());
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Add a third party vector tile source</title>
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
            center: [-87.622088, 41.878781],
            zoom: 12
        });

        map.on('load', function () {
                // Add Mapillary sequence layer.
                // https://www.mapillary.com/developer/tiles-documentation/#sequence-layer
                map.addSource('mapillary', {
                    'type': 'vector',
                    'tiles': [
                        'https://tiles.mapillary.com/maps/vtp/mly1_public/2/{z}/{x}/{y}?access_token=YOUR_MAPILLARY_TOKEN'
                    ],
                    'minzoom': 6,
                    'maxzoom': 14
                });
                map.addLayer(
                    {
                        'id': 'mapillary',
                        'type': 'line',
                        'source': 'mapillary',
                        'source-layer': 'sequence',
                        'layout': {
                            'line-cap': 'round',
                            'line-join': 'round'
                        },
                        'paint': {
                            'line-opacity': 0.6,
                            'line-color': 'rgb(53, 175, 109)',
                            'line-width': 2
                        }
                    },
                    'River labels'
                );
            });

            map.addControl(new maptilersdk.NavigationControl());
    </script>
</body>
</html>
```
