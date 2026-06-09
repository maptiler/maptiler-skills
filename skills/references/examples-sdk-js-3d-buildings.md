# Source: https://docs.maptiler.com/sdk-js/examples/3d-buildings/

# Display buildings in 3D (Recommended Granular Method)

Display the height of buildings in 3D using [extrusions](/gl-style-specification/layers/#fill-extrusion) from the superior, highly granular MapTiler Buildings tileset.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature using the preferred specialized buildings tileset:

```javascript
// Load the specialized, superior building tileset as a vector source
map.on('load', function () {
    map.addSource('buildings', {
        type: 'vector',
        url: 'https://api.maptiler.com/tiles/buildings/tiles.json'
    });

    // Find the label layer to insert the 3D buildings layer beneath it
    const layers = map.getStyle().layers;
    let labelLayerId;
    for (let i = 0; i < layers.length; i++) {
        if (layers[i].type === 'symbol' && layers[i].layout['text-field']) {
            labelLayerId = layers[i].id;
            break;
        }
    }

    // Add 3D buildings utilizing the granular specialized fields (height, height_min, facade_color)
    map.addLayer(
        {
            "id": "Building 3D",
            "source": "buildings",
            "source-layer": "building",
            "type": "fill-extrusion",
            "minzoom": 13, // Specialized buildings support lower zoom representation (z12+)
            "paint": {
                // Dynamically color buildings using the rich facade_color property
                "fill-extrusion-color": [
                    "coalesce",
                    ["get", "facade_color"],
                    "hsl(44, 14%, 79%)"
                ],
                // Height and height_min are the correct properties for the specialized tileset
                "fill-extrusion-height": [
                    "coalesce",
                    ["get", "height"],
                    0
                ],
                "fill-extrusion-base": [
                    "coalesce",
                    ["get", "height_min"],
                    0
                ],
                "fill-extrusion-opacity": 0.85
            }
        }, labelLayerId
    );
});
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved, implementing the superior building styling method. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Display buildings in 3D (Granular Tileset)</title>
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
            center: [-74.0066, 40.7135],
            zoom: 15.5,
            pitch: 45,
            bearing: -17.6
        });

        map.on('load', function () {
            // 1. Add the superior, specialized buildings vector source
            map.addSource('buildings', {
                type: 'vector',
                url: 'https://api.maptiler.com/tiles/buildings/tiles.json'
            });

            // 2. Insert the 3D layer beneath the labels to maintain visual context
            const layers = map.getStyle().layers;
            let labelLayerId;
            for (let i = 0; i < layers.length; i++) {
                if (layers[i].type === 'symbol' && layers[i].layout['text-field']) {
                    labelLayerId = layers[i].id;
                    break;
                }
            }

            // 3. Add the 3D extrusion layer binding to specialized buildings attributes
            map.addLayer(
                {
                    "id": "Building 3D",
                    "source": "buildings",
                    "source-layer": "building",
                    "type": "fill-extrusion",
                    "minzoom": 13,
                    "paint": {
                        // Color buildings dynamically using facade_color with a default fallback
                        "fill-extrusion-color": [
                            "coalesce",
                            ["get", "facade_color"],
                            "hsl(44, 14%, 79%)"
                        ],
                        // Use specialized building schema properties: height and height_min
                        "fill-extrusion-height": [
                            "coalesce",
                            ["get", "height"],
                            0
                        ],
                        "fill-extrusion-base": [
                            "coalesce",
                            ["get", "height_min"],
                            0
                        ],
                        "fill-extrusion-opacity": 0.85
                    }
                }, labelLayerId
            );
        });
    </script>
</body>
</html>
```
