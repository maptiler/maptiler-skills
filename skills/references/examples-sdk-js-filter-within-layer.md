# Source: https://docs.maptiler.com/sdk-js/examples/filter-within-layer/

# Filter within a Layer

This example shows how to filter a layer based on user input using `setFilter()`. Download the [earthquake sample data](../../assets/earthquakes.geojson){:target="_blank" rel="noopener"}.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', async function () {
      await maptilersdk.helpers.addPoint(map, {
        layerId: 'earthquakes',
        data: 'YOUR_MAPTILER_DATASET_ID_HERE',
        pointColor: '#FB3A1B',
        pointRadius: 40
      });

    });

    document.getElementById('nav-filter').addEventListener('change', (e) => {
      let filterOnValue = ['all'];
      let operator = '==';

      switch (e.target.id) {
        /// example: `map.setFilter("earthquakes", ["any", [">", "felt", 16.0]])`
        case 'felt':
          operatorFelt = document.getElementById('operator-felt');
          felt = document.getElementById('range-felt');
          operator = operatorFelt.value;

          // eslint-disable-next-line no-unused-expressions
          e.target.checked ? data.felt = Number(felt.value) : delete data['felt'];

          break;

        /// example: `map.setFilter("earthquakes", ["any", [">", "mag", 5.0]])`
        case 'mag':
          operatorMag = document.getElementById('operator-mag');
          mag = document.getElementById('range-mag');
          operator = operatorMag.value;

          // eslint-disable-next-line no-unused-expressions
          e.target.checked ? data.mag = Number(mag.value) : delete data['mag'];

          break;

        /// example: `map.setFilter("earthquakes", ["any", [">", "tsunami", 0]])`
        case 'tsunami':
          // eslint-disable-next-line @typescript-eslint/quotes
          tsunami = document.querySelector("input[type='radio'][name=tsunami]:checked");
          operator = '==';

          // eslint-disable-next-line no-unused-expressions
          e.target.checked ? data.tsunami = Number(tsunami.value) : delete data['tsunami'];

          break;
        default:
          console.log('default');
      }

      filterOnValue = Object.keys(data);

      mapLibreFilterSpread = ['all', ...filterOnValue.map(id => [operator, id, data[id]])];
      mapLibreFilter = mapLibreFilterSpread;

      document.getElementById('filter-result').textContent = JSON.stringify(mapLibreFilter);

      map.setFilter('earthquakes', mapLibreFilter);
    });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Filter within a Layer</title>
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
            style: maptilersdk.MapStyle.DATAVIZ.DARK,
            center: [-156.6, 44],
            zoom: 1.6
        });

        map.on('load', async function () {
              await maptilersdk.helpers.addPoint(map, {
                layerId: 'earthquakes',
                data: 'YOUR_MAPTILER_DATASET_ID_HERE',
                pointColor: '#FB3A1B',
                pointRadius: 40
              });

            });

            document.getElementById('nav-filter').addEventListener('change', (e) => {
              let filterOnValue = ['all'];
              let operator = '==';

              switch (e.target.id) {
                /// example: `map.setFilter("earthquakes", ["any", [">", "felt", 16.0]])`
                case 'felt':
                  operatorFelt = document.getElementById('operator-felt');
                  felt = document.getElementById('range-felt');
                  operator = operatorFelt.value;

                  // eslint-disable-next-line no-unused-expressions
                  e.target.checked ? data.felt = Number(felt.value) : delete data['felt'];

                  break;

                /// example: `map.setFilter("earthquakes", ["any", [">", "mag", 5.0]])`
                case 'mag':
                  operatorMag = document.getElementById('operator-mag');
                  mag = document.getElementById('range-mag');
                  operator = operatorMag.value;

                  // eslint-disable-next-line no-unused-expressions
                  e.target.checked ? data.mag = Number(mag.value) : delete data['mag'];

                  break;

                /// example: `map.setFilter("earthquakes", ["any", [">", "tsunami", 0]])`
                case 'tsunami':
                  // eslint-disable-next-line @typescript-eslint/quotes
                  tsunami = document.querySelector("input[type='radio'][name=tsunami]:checked");
                  operator = '==';

                  // eslint-disable-next-line no-unused-expressions
                  e.target.checked ? data.tsunami = Number(tsunami.value) : delete data['tsunami'];

                  break;
                default:
                  console.log('default');
              }

              filterOnValue = Object.keys(data);

              mapLibreFilterSpread = ['all', ...filterOnValue.map(id => [operator, id, data[id]])];
              mapLibreFilter = mapLibreFilterSpread;

              document.getElementById('filter-result').textContent = JSON.stringify(mapLibreFilter);

              map.setFilter('earthquakes', mapLibreFilter);
            });
    </script>
</body>
</html>
```
