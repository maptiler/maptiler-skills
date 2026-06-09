# Source: https://docs.maptiler.com/sdk-js/examples/cadastre/

# Add a map to a webpage

In this detailed example, you will learn how to interact with **cadastral map** information effectively. You will learn how to highlight specific parcels by hovering over them and displaying a pop-up window to access more complete details when you click on a parcel. Check out the [**MapTiler Cadastre schema**](/schema/cadastre/) for more details on the available information (layers, attributes, etc.).

In this example, clicking on the map displays the information about the plot and the building. For demonstration purposes, we have implemented a link to access and download official plot information (only for the **Canton of Bern**) in PDF format.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
let hoveredStateId = null;
    const popup = new maptilersdk.Popup({closeOnClick: false});

    map.on('ready', async () => {
      
      map.addLayer({
        "id": "parcel",
        "source": "cadastre",
        "source-layer": "parcel",
        "type": "fill",
        "layout": {},
        "paint": {
          "fill-color": "#ffffff",
          "fill-opacity": [
              'case',
              ['boolean', ['feature-state', 'hover'], false],
              0.5,
              0
          ]
        }
      }, "Parcel border");

      map.on('click', 'Building', (e) => {
        const features = map.queryRenderedFeatures(e.point, {
          layers: ['Building', 'parcel']
        });

        if (features.length !== 0) {
          const description = createPopupContent(features);
          popup.setLngLat(e.lngLat).setHTML(description).addTo(map);
        }
      });

      map.on('mousemove', 'Building', function (e) {
        map.getCanvas().style.cursor = 'pointer';
      });

      map.on('mouseleave', 'Building', function () {
        map.getCanvas().style.cursor = '';
      });

      map.on('mousemove', 'Building', function (e) {
        if (e.features.length > 0) {
          const features = map.queryRenderedFeatures(e.point, {
            layers: ['parcel']
          });

          if (hoveredStateId) {
            map.setFeatureState(
              { source: 'cadastre', sourceLayer: 'parcel', id: hoveredStateId },
              { hover: false }
            );
          }
          if (features) {
            hoveredStateId = features[0].id;
            map.setFeatureState(
              { source: 'cadastre', sourceLayer: 'parcel', id: hoveredStateId },
              { hover: true }
            );
          }
        }
      });

      map.on('mouseleave', 'Building', function () {
        if (hoveredStateId) {
          map.setFeatureState(
            { source: 'cadastre', sourceLayer: 'parcel', id: hoveredStateId },
            { hover: false }
          );
        }
        hoveredStateId = null;
      });

    });
    }

    loadMap();

    function createPopupContent(features) {
      const data = features.reduce((agg, feat) => {
        if (feat.layer.id == "parcel") {
          agg.parcel = feat.properties.id;
          agg.parcel_number = feat.properties.number;
          agg.zone = feat.properties.zone;
        } else if (feat.layer.id == "Building") {
          agg.building = feat.properties.id;
        }
        return agg;
      }, {});

      return `<div><strong>Parcel number</strong>: ${data.parcel_number}</div>
      <div><strong>Building</strong>: ${data.building}</div>
      <div><a href="https://www.oereb2.apps.be.ch/extract/pdf/?EGRID=${data.parcel}">${data.parcel}</a></div>
      `;
    }
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Add a map to a webpage</title>
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
            style: style,
            center: [lng, lat],
            zoom: zoom
        });

        let hoveredStateId = null;
            const popup = new maptilersdk.Popup({closeOnClick: false});

            map.on('ready', async () => {

              map.addLayer({
                "id": "parcel",
                "source": "cadastre",
                "source-layer": "parcel",
                "type": "fill",
                "layout": {},
                "paint": {
                  "fill-color": "#ffffff",
                  "fill-opacity": [
                      'case',
                      ['boolean', ['feature-state', 'hover'], false],
                      0.5,
                      0
                  ]
                }
              }, "Parcel border");

              map.on('click', 'Building', (e) => {
                const features = map.queryRenderedFeatures(e.point, {
                  layers: ['Building', 'parcel']
                });

                if (features.length !== 0) {
                  const description = createPopupContent(features);
                  popup.setLngLat(e.lngLat).setHTML(description).addTo(map);
                }
              });

              map.on('mousemove', 'Building', function (e) {
                map.getCanvas().style.cursor = 'pointer';
              });

              map.on('mouseleave', 'Building', function () {
                map.getCanvas().style.cursor = '';
              });

              map.on('mousemove', 'Building', function (e) {
                if (e.features.length > 0) {
                  const features = map.queryRenderedFeatures(e.point, {
                    layers: ['parcel']
                  });

                  if (hoveredStateId) {
                    map.setFeatureState(
                      { source: 'cadastre', sourceLayer: 'parcel', id: hoveredStateId },
                      { hover: false }
                    );
                  }
                  if (features) {
                    hoveredStateId = features[0].id;
                    map.setFeatureState(
                      { source: 'cadastre', sourceLayer: 'parcel', id: hoveredStateId },
                      { hover: true }
                    );
                  }
                }
              });

              map.on('mouseleave', 'Building', function () {
                if (hoveredStateId) {
                  map.setFeatureState(
                    { source: 'cadastre', sourceLayer: 'parcel', id: hoveredStateId },
                    { hover: false }
                  );
                }
                hoveredStateId = null;
              });

            });
            }

            loadMap();

            function createPopupContent(features) {
              const data = features.reduce((agg, feat) => {
                if (feat.layer.id == "parcel") {
                  agg.parcel = feat.properties.id;
                  agg.parcel_number = feat.properties.number;
                  agg.zone = feat.properties.zone;
                } else if (feat.layer.id == "Building") {
                  agg.building = feat.properties.id;
                }
                return agg;
              }, {});

              return `<div><strong>Parcel number</strong>: ${data.parcel_number}</div>
              <div><strong>Building</strong>: ${data.building}</div>
              <div><a href="https://www.oereb2.apps.be.ch/extract/pdf/?EGRID=${data.parcel}">${data.parcel}</a></div>
              `;
            }
    </script>
</body>
</html>
```
