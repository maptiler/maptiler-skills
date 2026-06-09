# Source: https://docs.maptiler.com/sdk-js/examples/add-image-stretchable/

# Add a stretchable image to the map

Use a stretchable image as a background for text. Stretchable images allow some parts of the image to stretch while keeping other parts, such as corners, at a constant size. Set the `layout` property `'icon-text-fit': 'both'` to use the image as background for the text.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const images = {
        'popup': 'https://docs.maptiler.com/sdk-js/assets/popup.png',
        'popup-debug':
            'https://docs.maptiler.com/sdk-js/assets/popup_debug.png'
    };

    map.on('load', async () => {
        const debugPopup = await map.loadImage(images['popup-debug']);
        const popup = await map.loadImage(images['popup']);
        map.addImage('popup-debug', debugPopup.data, {
            // The two (blue) columns of pixels that can be stretched horizontally:
            //   - the pixels between x: 25 and x: 55 can be stretched
            //   - the pixels between x: 85 and x: 115 can be stretched.
            stretchX: [
                [25, 55],
                [85, 115]
            ],
            // The one (red) row of pixels that can be stretched vertically:
            //   - the pixels between y: 25 and y: 100 can be stretched
            stretchY: [[25, 100]],
            // This part of the image that can contain text ([x1, y1, x2, y2]):
            content: [25, 25, 115, 100],
            // This is a high-dpi image:
            pixelRatio: 2
        });
        map.addImage('popup', popup.data, {
            stretchX: [
                [25, 55],
                [85, 115]
            ],
            stretchY: [[25, 100]],
            content: [25, 25, 115, 100],
            pixelRatio: 2
        });

        map.addSource('points', {
            'type': 'geojson',
            'data': {
                'type': 'FeatureCollection',
                'features': [
                    {
                        'type': 'Feature',
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [40, -30]
                        },
                        'properties': {
                            'image-name': 'popup-debug',
                            'name': 'Line 1\nLine 2\nLine 3'
                        }
                    },
                    {
                        'type': 'Feature',
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [40, 30]
                        },
                        'properties': {
                            'image-name': 'popup',
                            'name': 'Line 1\nLine 2\nLine 3'
                        }
                    },
                    {
                        'type': 'Feature',
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [-40, -30]
                        },
                        'properties': {
                            'image-name': 'popup-debug',
                            'name': 'One longer line'
                        }
                    },
                    {
                        'type': 'Feature',
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [-40, 30]
                        },
                        'properties': {
                            'image-name': 'popup',
                            'name': 'One longer line'
                        }
                    }
                ]
            }
        });
        map.addLayer({
            'id': 'points',
            'type': 'symbol',
            'source': 'points',
            'layout': {
                'text-field': ['get', 'name'],
                'icon-text-fit': 'both',
                'icon-image': ['get', 'image-name'],
                'icon-overlap': 'always',
                'text-overlap': 'always'
            }
        });

        // the original, unstretched image for comparison
        map.addSource('original', {
            'type': 'geojson',
            'data': {
                'type': 'FeatureCollection',
                'features': [
                    {
                        'type': 'Feature',
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [0, -70]
                        }
                    }
                ]
            }
        });
        map.addLayer({
            'id': 'original',
            'type': 'symbol',
            'source': 'original',
            'layout': {
                'text-field': 'unstretched image',
                'icon-image': 'popup-debug',
                'icon-overlap': 'always',
                'text-overlap': 'always'
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
    <title>Add a stretchable image to the map</title>
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
            zoom: 0.1
        });

        const images = {
                'popup': 'https://docs.maptiler.com/sdk-js/assets/popup.png',
                'popup-debug':
                    'https://docs.maptiler.com/sdk-js/assets/popup_debug.png'
            };

            map.on('load', async () => {
                const debugPopup = await map.loadImage(images['popup-debug']);
                const popup = await map.loadImage(images['popup']);
                map.addImage('popup-debug', debugPopup.data, {
                    // The two (blue) columns of pixels that can be stretched horizontally:
                    //   - the pixels between x: 25 and x: 55 can be stretched
                    //   - the pixels between x: 85 and x: 115 can be stretched.
                    stretchX: [
                        [25, 55],
                        [85, 115]
                    ],
                    // The one (red) row of pixels that can be stretched vertically:
                    //   - the pixels between y: 25 and y: 100 can be stretched
                    stretchY: [[25, 100]],
                    // This part of the image that can contain text ([x1, y1, x2, y2]):
                    content: [25, 25, 115, 100],
                    // This is a high-dpi image:
                    pixelRatio: 2
                });
                map.addImage('popup', popup.data, {
                    stretchX: [
                        [25, 55],
                        [85, 115]
                    ],
                    stretchY: [[25, 100]],
                    content: [25, 25, 115, 100],
                    pixelRatio: 2
                });

                map.addSource('points', {
                    'type': 'geojson',
                    'data': {
                        'type': 'FeatureCollection',
                        'features': [
                            {
                                'type': 'Feature',
                                'geometry': {
                                    'type': 'Point',
                                    'coordinates': [40, -30]
                                },
                                'properties': {
                                    'image-name': 'popup-debug',
                                    'name': 'Line 1\nLine 2\nLine 3'
                                }
                            },
                            {
                                'type': 'Feature',
                                'geometry': {
                                    'type': 'Point',
                                    'coordinates': [40, 30]
                                },
                                'properties': {
                                    'image-name': 'popup',
                                    'name': 'Line 1\nLine 2\nLine 3'
                                }
                            },
                            {
                                'type': 'Feature',
                                'geometry': {
                                    'type': 'Point',
                                    'coordinates': [-40, -30]
                                },
                                'properties': {
                                    'image-name': 'popup-debug',
                                    'name': 'One longer line'
                                }
                            },
                            {
                                'type': 'Feature',
                                'geometry': {
                                    'type': 'Point',
                                    'coordinates': [-40, 30]
                                },
                                'properties': {
                                    'image-name': 'popup',
                                    'name': 'One longer line'
                                }
                            }
                        ]
                    }
                });
                map.addLayer({
                    'id': 'points',
                    'type': 'symbol',
                    'source': 'points',
                    'layout': {
                        'text-field': ['get', 'name'],
                        'icon-text-fit': 'both',
                        'icon-image': ['get', 'image-name'],
                        'icon-overlap': 'always',
                        'text-overlap': 'always'
                    }
                });

                // the original, unstretched image for comparison
                map.addSource('original', {
                    'type': 'geojson',
                    'data': {
                        'type': 'FeatureCollection',
                        'features': [
                            {
                                'type': 'Feature',
                                'geometry': {
                                    'type': 'Point',
                                    'coordinates': [0, -70]
                                }
                            }
                        ]
                    }
                });
                map.addLayer({
                    'id': 'original',
                    'type': 'symbol',
                    'source': 'original',
                    'layout': {
                        'text-field': 'unstretched image',
                        'icon-image': 'popup-debug',
                        'icon-overlap': 'always',
                        'text-overlap': 'always'
                    }
                });
            });
    </script>
</body>
</html>
```
