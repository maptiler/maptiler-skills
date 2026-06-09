# Source: https://docs.maptiler.com/sdk-js/examples/mapbox-gl-draw/

# Show drawn polygon area

Use [mapbox-gl-draw](https://github.com/mapbox/mapbox-gl-draw) to draw a polygon and [Turf.js](https://turfjs.org/) to calculate its area in square meters.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const draw = new MapboxDraw({
      displayControlsDefault: false,
      controls: {
        polygon: true,
        trash: true
      }
    });
    map.addControl(draw);

    //fix conytrols style
    const drawControls = document.querySelectorAll(".mapboxgl-ctrl-group.mapboxgl-ctrl");
    drawControls.forEach((elem) => {
      elem.classList.add('maplibregl-ctrl', 'maplibregl-ctrl-group');
    });

    map.on('draw.create', updateArea);
    map.on('draw.delete', updateArea);
    map.on('draw.update', updateArea);

    function updateArea(e) {
      const data = draw.getAll();
      const answer = document.getElementById('calculated-area');
      if (data.features.length > 0) {
        const area = turf.area(data);
        // restrict to area to 2 decimal points
        const rounded_area = Math.round(area * 100) / 100;
        answer.innerHTML =
          '<p><strong>' +
          rounded_area +
          '</strong></p><p>square meters</p>';
      } else {
        answer.innerHTML = '';
        if (e.type !== 'draw.delete')
          alert('Use the draw tools to draw a polygon!');
      }
    }
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Show drawn polygon area</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
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
            style: maptilersdk.MapStyle.STREETS,
            center: [-91.874, 42.76],
            zoom: 12 // starting zoom
        });

        const draw = new MapboxDraw({
              displayControlsDefault: false,
              controls: {
                polygon: true,
                trash: true
              }
            });
            map.addControl(draw);

            //fix conytrols style
            const drawControls = document.querySelectorAll(".mapboxgl-ctrl-group.mapboxgl-ctrl");
            drawControls.forEach((elem) => {
              elem.classList.add('maplibregl-ctrl', 'maplibregl-ctrl-group');
            });

            map.on('draw.create', updateArea);
            map.on('draw.delete', updateArea);
            map.on('draw.update', updateArea);

            function updateArea(e) {
              const data = draw.getAll();
              const answer = document.getElementById('calculated-area');
              if (data.features.length > 0) {
                const area = turf.area(data);
                // restrict to area to 2 decimal points
                const rounded_area = Math.round(area * 100) / 100;
                answer.innerHTML =
                  '<p><strong>' +
                  rounded_area +
                  '</strong></p><p>square meters</p>';
              } else {
                answer.innerHTML = '';
                if (e.type !== 'draw.delete')
                  alert('Use the draw tools to draw a polygon!');
              }
            }
    </script>
</body>
</html>
```
