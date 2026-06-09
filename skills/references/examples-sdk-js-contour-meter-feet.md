# Source: https://docs.maptiler.com/sdk-js/examples/contour-meter-feet/

# Switch between meters and feet

Change the units for the altitude of the contour lines, converting from meters to feet. For additional technical information, refer to the [Contours schema](https://docs.maptiler.com/schema/contours/) provided by MapTiler.

The Global Contours schema, created by MapTiler, contains contour lines for locations all around the globe in two widely used unit systems: meters and feet. With its global coverage, MapTiler's contour lines can be utilized for various purposes, such as outdoor recreation planning, landscape analysis, and cartographic visualization.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
// switching contours units
    const changeLayerSource = function(layer_id, source) {
      // get layer definition, remove layer, add layer
      const oldLayers = map.getStyle().layers;
      const layerIndex =  oldLayers.findIndex(l => l.id === layer_id);
      const contourDef = oldLayers[layerIndex];
      const before = oldLayers[layerIndex + 1] && oldLayers[layerIndex +1].id;
      contourDef['source-layer'] = source;
      map.removeLayer(layer_id);
      map.addLayer(contourDef, before);
    };
    
    // switch units handler
    const units = document.getElementById('units');
    units.addEventListener('change', function() {
      changeLayerSource('Contour', this.value);
      changeLayerSource('Contour index', this.value);
      changeLayerSource('Contour labels', this.value);
      changeLayerSource('Glacier contour', this.value);
      changeLayerSource('Glacier contour index', this.value);
      changeLayerSource('Glacier contour labels', this.value);
    });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Switch between meters and feet</title>
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
            style: maptilersdk.MapStyle.OUTDOOR,
            center: [-148.63567, 62.03381],
            zoom: 13.42
        });

        // switching contours units
            const changeLayerSource = function(layer_id, source) {
              // get layer definition, remove layer, add layer
              const oldLayers = map.getStyle().layers;
              const layerIndex =  oldLayers.findIndex(l => l.id === layer_id);
              const contourDef = oldLayers[layerIndex];
              const before = oldLayers[layerIndex + 1] && oldLayers[layerIndex +1].id;
              contourDef['source-layer'] = source;
              map.removeLayer(layer_id);
              map.addLayer(contourDef, before);
            };

            // switch units handler
            const units = document.getElementById('units');
            units.addEventListener('change', function() {
              changeLayerSource('Contour', this.value);
              changeLayerSource('Contour index', this.value);
              changeLayerSource('Contour labels', this.value);
              changeLayerSource('Glacier contour', this.value);
              changeLayerSource('Glacier contour index', this.value);
              changeLayerSource('Glacier contour labels', this.value);
            });
    </script>
</body>
</html>
```
