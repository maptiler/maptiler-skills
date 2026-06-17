# Source: https://docs.maptiler.com/sdk-js/examples/color-ramp-resample/

# Color ramp

This example shows how to resample a color ramp and use it to visualize a point layer. Download the sample data [here](../../assets/schools.geojson){:target="_blank" rel="noopener"}.

Select between different resampling methods or no resampling to compare point layer visualizations.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const ramp = maptilersdk.ColorRampCollection.PORTLAND.scale(300, 4000);
    const ramp_sqrt = maptilersdk.ColorRampCollection.PORTLAND.scale(300, 4000).resample("ease-out-sqrt");
    const ramp_exp = maptilersdk.ColorRampCollection.PORTLAND.scale(300, 4000).resample("ease-out-exp");

    let layers;

    map.on('load', async function () {
      await createColorRampLayer(ramp_sqrt, 'sqrt');
    });

    document.getElementById('resample-method').addEventListener('change', function(evt) {
      const method = this.value;
      mapRemoveLayers();
      switch (method) {
        case 'lineal':
          createColorRampLayer(ramp, method);
          break;
        case 'sqrt':
          createColorRampLayer(ramp_sqrt, method);
          break;
        case 'exp':
          createColorRampLayer(ramp_exp, method);
          break;
        default:
          createColorRampLayer(ramp, "lineal");
          break;
      }
    });

    async function createColorRampLayer(colorRamp, name) { 
      const rampLayers = await maptilersdk.helpers.addPoint(map, {
        layerId: `school_color_ramp_${name}`,
        data: 'schools.geojson',
        property: "students",
        pointColor: colorRamp,
        pointOpacity: 0.7,
        minPointRadius: 15,
        showLabel: true,
      });
      layers = rampLayers;
    }

    function mapRemoveLayers() {
      Object.keys(layers).forEach(item => {
        if (layers[item] !== "") {
          if (map.getLayer(layers[item])) map.removeLayer(layers[item]);
        } 
      })
    }
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Color ramp</title>
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
            center: [-73.97402, 40.73302],
            zoom: 11
        });

        const ramp = maptilersdk.ColorRampCollection.PORTLAND.scale(300, 4000);
            const ramp_sqrt = maptilersdk.ColorRampCollection.PORTLAND.scale(300, 4000).resample("ease-out-sqrt");
            const ramp_exp = maptilersdk.ColorRampCollection.PORTLAND.scale(300, 4000).resample("ease-out-exp");

            let layers;

            map.on('load', async function () {
              await createColorRampLayer(ramp_sqrt, 'sqrt');
            });

            document.getElementById('resample-method').addEventListener('change', function(evt) {
              const method = this.value;
              mapRemoveLayers();
              switch (method) {
                case 'lineal':
                  createColorRampLayer(ramp, method);
                  break;
                case 'sqrt':
                  createColorRampLayer(ramp_sqrt, method);
                  break;
                case 'exp':
                  createColorRampLayer(ramp_exp, method);
                  break;
                default:
                  createColorRampLayer(ramp, "lineal");
                  break;
              }
            });

            async function createColorRampLayer(colorRamp, name) { 
              const rampLayers = await maptilersdk.helpers.addPoint(map, {
                layerId: `school_color_ramp_${name}`,
                data: 'schools.geojson',
                property: "students",
                pointColor: colorRamp,
                pointOpacity: 0.7,
                minPointRadius: 15,
                showLabel: true,
              });
              layers = rampLayers;
            }

            function mapRemoveLayers() {
              Object.keys(layers).forEach(item => {
                if (layers[item] !== "") {
                  if (map.getLayer(layers[item])) map.removeLayer(layers[item]);
                } 
              })
            }
    </script>
</body>
</html>
```
