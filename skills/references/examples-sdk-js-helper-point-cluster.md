# Source: https://docs.maptiler.com/sdk-js/examples/helper-point-cluster/

# Point helper

This example showcases how to generate a cluster map using the point layer helper with its default configurations. To replicate

this example, download the [US schools sample data](../../assets/schools.geojson){:target="_blank" rel="noopener"}.

If your map contains a layer with a significant number of points, you have the option to configure clustering, which aids in visually extracting valuable information from your data. This is where a **cluster map**, also referred to as a bubble map, proves to be beneficial.

When you activate clustering, point features that are a certain distance apart on the screen are grouped into a cluster. The size of the cluster or bubble corresponds to the number of markers it contains. By zooming in closer on your map, you can view the individual points and interact with them.

Cluster maps are an excellent tool for determining the quantity of data points located within a specific region. If you need to measure density, a [heat map](/sdk-js/examples/helper-heatmap-minimal/) is also highly effective and can incorporate your numeric values.

By default, the label is displayed, indicating the number of elements contained within each cluster.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', async function () {
      await maptilersdk.helpers.addPoint(map, {
        data: 'schools.geojson',
        cluster: true,
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
    <title>Point helper</title>
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
            center: [-98.84, 38.28],
            zoom: 3.2
        });

        map.on('load', async function () {
              await maptilersdk.helpers.addPoint(map, {
                data: 'schools.geojson',
                cluster: true,
              });
            });
    </script>
</body>
</html>
```
