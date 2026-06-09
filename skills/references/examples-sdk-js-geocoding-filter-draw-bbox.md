# Source: https://docs.maptiler.com/sdk-js/examples/geocoding-filter-draw-bbox/

# MapTiler Geocoding limit results by a drawn area

To ensure that search results are limited to the specific area drawn on the map, utilize the geocode control's `bbox` (bounding box) feature. By drawing a polygon on the map, you can filter the search results to only include data within the bounds of the polygon. For a comprehensive list of geocoding control options, refer to the [Geocoding control's reference documentation](/sdk-js/modules/geocoding/api/api-reference/#options).

In this example, we use the [mapbox-gl-draw-rectangle-restrict-area](https://github.com/dqunbp/mapbox-gl-draw-rectangle-restrict-area) plugin to draw rectangles on the map.

<sup>Click outside the rectangle when you draw the final vertex to complete the polygon.</sup>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const draw = new MapboxDraw({
      displayControlsDefault: false,
      controls: {
        polygon: true,
        trash: true
      },
      modes: Object.assign(MapboxDraw.modes, {
        draw_rectangle: DrawRectangle,
      }),
    });

    map.addControl(draw, 'top-right');

    map.on('draw.create', updateFilterArea);
    map.on('draw.delete', deleteFilterArea);
    map.on('draw.update', updateFilterArea);

    //set geocoding control filter search results to the Paris area
    const gc = new maptilerGeocoder.GeocodingControl({
      bbox: bbox
    });

    map.addControl(gc, 'top-left');

    function updateFilterArea(e) {
      const data = draw.getAll();
      const drawBbox = turf.bbox(data);
      gc.setOptions({ bbox: drawBbox });
    }

    function deleteFilterArea(e) {
      gc.setOptions({ bbox: null });
    }

    //initial load London area polygon.
    map.on('load', function () {
      const feature = turf.bboxPolygon(bbox);
      draw.add(feature);
    });

    map.on('draw.modechange', function (e) {
      if (e.mode === "draw_polygon") {
        draw.deleteAll();
        draw.changeMode("draw_rectangle");
      }
    });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>MapTiler Geocoding limit results by a drawn area</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <script src="https://cdn.maptiler.com/maptiler-geocoding-control/v3.0.0/maptilersdk.umd.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@turf/turf@7.3.5/turf.min.js"></script>
    <script src="https://api.mapbox.com/mapbox-gl-js/plugins/mapbox-gl-draw/v1.4.2/mapbox-gl-draw.js"></script>
    <link href="https://api.mapbox.com/mapbox-gl-js/plugins/mapbox-gl-draw/v1.4.2/mapbox-gl-draw.css" rel="stylesheet" />
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
            style: maptilersdk.MapStyle.STREETS.LIGHT,
            center: [0, 0],
            zoom: 0
        });

        const draw = new MapboxDraw({
              displayControlsDefault: false,
              controls: {
                polygon: true,
                trash: true
              },
              modes: Object.assign(MapboxDraw.modes, {
                draw_rectangle: DrawRectangle,
              }),
            });

            map.addControl(draw, 'top-right');

            map.on('draw.create', updateFilterArea);
            map.on('draw.delete', deleteFilterArea);
            map.on('draw.update', updateFilterArea);

            //set geocoding control filter search results to the Paris area
            const gc = new maptilerGeocoder.GeocodingControl({
              bbox: bbox
            });

            map.addControl(gc, 'top-left');

            function updateFilterArea(e) {
              const data = draw.getAll();
              const drawBbox = turf.bbox(data);
              gc.setOptions({ bbox: drawBbox });
            }

            function deleteFilterArea(e) {
              gc.setOptions({ bbox: null });
            }

            //initial load London area polygon.
            map.on('load', function () {
              const feature = turf.bboxPolygon(bbox);
              draw.add(feature);
            });

            map.on('draw.modechange', function (e) {
              if (e.mode === "draw_polygon") {
                draw.deleteAll();
                draw.changeMode("draw_rectangle");
              }
            });
    </script>
</body>
</html>
```
