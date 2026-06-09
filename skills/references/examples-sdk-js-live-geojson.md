# Source: https://docs.maptiler.com/sdk-js/examples/live-geojson/

# Add live realtime data

Use live real-time GeoJSON data streams to move a [`symbol`](/gl-style-specification/layers/#symbol) on your map.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const url = 'https://api.wheretheiss.at/v1/satellites/25544';
    map.on('load', function () {
        const request = new XMLHttpRequest();
        window.setInterval(function () {
            // make a GET request to parse the GeoJSON at the url
            request.open('GET', url, true);
            request.onload = function () {
                if (this.status >= 200 && this.status < 400) {
                    // retrieve the JSON from the response
                    const json = JSON.parse(this.response);

                    const { latitude, longitude } = json;
                    const data = {
                        'type': 'FeatureCollection',
                        'features': [
                            {
                            'type': 'Feature',
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [longitude, latitude]
                            }
                            }
                        ]
                    }

                    // update the drone symbol's location on the map
                    map.getSource('drone').setData(data);

                    // fly the map to the drone's current location
                    map.flyTo({
                        center: [longitude, latitude],
                        zoom: 7, 
                        speed: 0.5
                    });
                }
            };
            request.send();
        }, 2000);

        map.addSource('drone', { type: 'geojson', data: url });
        map.addLayer({
            'id': 'drone',
            'type': 'symbol',
            'source': 'drone',
            'layout': {
                'icon-image': 'aquarium'
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
    <title>Add live realtime data</title>
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
            center: [longitude, latitude],
            zoom: 0
        });

        const url = 'https://api.wheretheiss.at/v1/satellites/25544';
            map.on('load', function () {
                const request = new XMLHttpRequest();
                window.setInterval(function () {
                    // make a GET request to parse the GeoJSON at the url
                    request.open('GET', url, true);
                    request.onload = function () {
                        if (this.status >= 200 && this.status < 400) {
                            // retrieve the JSON from the response
                            const json = JSON.parse(this.response);

                            const { latitude, longitude } = json;
                            const data = {
                                'type': 'FeatureCollection',
                                'features': [
                                    {
                                    'type': 'Feature',
                                    'geometry': {
                                        'type': 'Point',
                                        'coordinates': [longitude, latitude]
                                    }
                                    }
                                ]
                            }

                            // update the drone symbol's location on the map
                            map.getSource('drone').setData(data);

                            // fly the map to the drone's current location
                            map.flyTo({
                                center: [longitude, latitude],
                                zoom: 7, 
                                speed: 0.5
                            });
                        }
                    };
                    request.send();
                }, 2000);

                map.addSource('drone', { type: 'geojson', data: url });
                map.addLayer({
                    'id': 'drone',
                    'type': 'symbol',
                    'source': 'drone',
                    'layout': {
                        'icon-image': 'aquarium'
                    }
                });
            });
    </script>
</body>
</html>
```
