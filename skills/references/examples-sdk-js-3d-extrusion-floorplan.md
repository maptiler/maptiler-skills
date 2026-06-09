# Source: https://docs.maptiler.com/sdk-js/examples/3d-extrusion-floorplan/

# Extrude polygons for 3D indoor mapping

Create a 3D indoor map with the [`fill-extrude-height`](/gl-style-specification/layers/#paint-fill-extrusion-fill-extrusion-height) paint property.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', function() {
        map.addSource('floorplan', {
            // GeoJSON Data source used in vector tiles, documented at
            // https://gist.github.com/ryanbaumann/a7d970386ce59d11c16278b90dde094d
            'type': 'geojson',
            'data': 'https://docs.maptiler.com/sdk-js/assets/indoor-3d-map.geojson'
        });
        map.addLayer({
            'id': 'room-extrusion',
            'type': 'fill-extrusion',
            'source': 'floorplan',
            'paint': {
                // See the Style Specification for details on data expressions.
                // https://docs.maptiler.com/gl-style-specification/expressions/

                // Get the fill-extrusion-color from the source 'color' property.
                'fill-extrusion-color': ['get', 'color'],

                // Get fill-extrusion-height from the source 'height' property.
                'fill-extrusion-height': ['get', 'height'],

                // Get fill-extrusion-base from the source 'base_height' property.
                'fill-extrusion-base': ['get', 'base_height'],

                // Make extrusions slightly opaque for see through indoor walls.
                'fill-extrusion-opacity': 0.5
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
    <title>Extrude polygons for 3D indoor mapping</title>
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
            center: [-87.61694, 41.86625],
            zoom: 15.99,
            pitch: 40,
            bearing: 20
        });

        map.on('load', function() {
                map.addSource('floorplan', {
                    // GeoJSON Data source used in vector tiles, documented at
                    // https://gist.github.com/ryanbaumann/a7d970386ce59d11c16278b90dde094d
                    'type': 'geojson',
                    'data': 'https://docs.maptiler.com/sdk-js/assets/indoor-3d-map.geojson'
                });
                map.addLayer({
                    'id': 'room-extrusion',
                    'type': 'fill-extrusion',
                    'source': 'floorplan',
                    'paint': {
                        // See the Style Specification for details on data expressions.
                        // https://docs.maptiler.com/gl-style-specification/expressions/

                        // Get the fill-extrusion-color from the source 'color' property.
                        'fill-extrusion-color': ['get', 'color'],

                        // Get fill-extrusion-height from the source 'height' property.
                        'fill-extrusion-height': ['get', 'height'],

                        // Get fill-extrusion-base from the source 'base_height' property.
                        'fill-extrusion-base': ['get', 'base_height'],

                        // Make extrusions slightly opaque for see through indoor walls.
                        'fill-extrusion-opacity': 0.5
                    }
                });
            });
    </script>
</body>
</html>
```
