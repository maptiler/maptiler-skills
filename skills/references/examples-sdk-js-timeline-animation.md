# Source: https://docs.maptiler.com/sdk-js/examples/timeline-animation/

# Create a time slider

Present seismic activities using a slider that spans a specific time range. Utilizing the [`Map#setFilter`](/sdk-js/api/map/#map#setfilter) function and the [D3.js](https://d3js.org/) library, construct a timeline slider to visually represent earthquakes that occurred in the year 2015 and had a magnitude greater than 5.9. Use the slider bar to filter earthquakes by month.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const months = [
      'January',
      'February',
      'March',
      'April',
      'May',
      'June',
      'July',
      'August',
      'September',
      'October',
      'November',
      'December'
    ];

    function filterBy(month) {
      const filters = ['==', 'month', month];
      map.setFilter('earthquake-circles', filters);
      map.setFilter('earthquake-labels', filters);

      // Set the label to the month
      document.getElementById('month').textContent = months[month];
    }

    map.on('load', function () {
      // Data courtesy of http://earthquake.usgs.gov/
      // Query for significant earthquakes in 2015 URL request looked like this:
      // http://earthquake.usgs.gov/fdsnws/event/1/query
      //    ?format=geojson
      //    &starttime=2015-01-01
      //    &endtime=2015-12-31
      //    &minmagnitude=6'
      //
      // Here we're using d3 to help us make the ajax request but you can use
      // Any request method (library or otherwise) you wish.
      d3.json(
        'https://docs.maptiler.com/sdk-js/assets/significant-earthquakes-2015.geojson',
        function (err, data) {
          if (err) throw err;

          // Create a month property value based on time
          // used to filter against.
          data.features = data.features.map(function (d) {
            d.properties.month = new Date(d.properties.time).getMonth();
            return d;
          });

          map.addSource('earthquakes', {
            'type': 'geojson',
            data: data
          });

          map.addLayer({
            'id': 'earthquake-circles',
            'type': 'circle',
            'source': 'earthquakes',
            'paint': {
              'circle-color': [
                'interpolate',
                ['linear'],
                ['get', 'mag'],
                6,
                '#FCA107',
                8,
                '#7F3121'
              ],
              'circle-opacity': 0.75,
              'circle-radius': [
                'interpolate',
                ['linear'],
                ['get', 'mag'],
                6,
                20,
                8,
                40
              ]
            }
          });

          map.addLayer({
            'id': 'earthquake-labels',
            'type': 'symbol',
            'source': 'earthquakes',
            'layout': {
              'text-field': [
                'concat',
                ['to-string', ['get', 'mag']],
                'm'
              ],
              'text-font': [
                'Open Sans Bold',
                'Arial Unicode MS Bold'
              ],
              'text-size': 12
            },
            'paint': {
              'text-color': 'rgba(0,0,0,0.5)'
            }
          });

          // Set filter to first month of the year
          // 0 = January
          filterBy(0);

          document
            .getElementById('slider')
            .addEventListener('input', function (e) {
              const month = parseInt(e.target.value, 10);
              filterBy(month);
            });
        }
      );
    });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Create a time slider</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <script src="https://d3js.org/d3.v3.min.js"></script>
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
            center: [31.4606, 20.7927],
            zoom: 0.5
        });

        const months = [
              'January',
              'February',
              'March',
              'April',
              'May',
              'June',
              'July',
              'August',
              'September',
              'October',
              'November',
              'December'
            ];

            function filterBy(month) {
              const filters = ['==', 'month', month];
              map.setFilter('earthquake-circles', filters);
              map.setFilter('earthquake-labels', filters);

              // Set the label to the month
              document.getElementById('month').textContent = months[month];
            }

            map.on('load', function () {
              // Data courtesy of http://earthquake.usgs.gov/
              // Query for significant earthquakes in 2015 URL request looked like this:
              // http://earthquake.usgs.gov/fdsnws/event/1/query
              //    ?format=geojson
              //    &starttime=2015-01-01
              //    &endtime=2015-12-31
              //    &minmagnitude=6'
              //
              // Here we're using d3 to help us make the ajax request but you can use
              // Any request method (library or otherwise) you wish.
              d3.json(
                'https://docs.maptiler.com/sdk-js/assets/significant-earthquakes-2015.geojson',
                function (err, data) {
                  if (err) throw err;

                  // Create a month property value based on time
                  // used to filter against.
                  data.features = data.features.map(function (d) {
                    d.properties.month = new Date(d.properties.time).getMonth();
                    return d;
                  });

                  map.addSource('earthquakes', {
                    'type': 'geojson',
                    data: data
                  });

                  map.addLayer({
                    'id': 'earthquake-circles',
                    'type': 'circle',
                    'source': 'earthquakes',
                    'paint': {
                      'circle-color': [
                        'interpolate',
                        ['linear'],
                        ['get', 'mag'],
                        6,
                        '#FCA107',
                        8,
                        '#7F3121'
                      ],
                      'circle-opacity': 0.75,
                      'circle-radius': [
                        'interpolate',
                        ['linear'],
                        ['get', 'mag'],
                        6,
                        20,
                        8,
                        40
                      ]
                    }
                  });

                  map.addLayer({
                    'id': 'earthquake-labels',
                    'type': 'symbol',
                    'source': 'earthquakes',
                    'layout': {
                      'text-field': [
                        'concat',
                        ['to-string', ['get', 'mag']],
                        'm'
                      ],
                      'text-font': [
                        'Open Sans Bold',
                        'Arial Unicode MS Bold'
                      ],
                      'text-size': 12
                    },
                    'paint': {
                      'text-color': 'rgba(0,0,0,0.5)'
                    }
                  });

                  // Set filter to first month of the year
                  // 0 = January
                  filterBy(0);

                  document
                    .getElementById('slider')
                    .addEventListener('input', function (e) {
                      const month = parseInt(e.target.value, 10);
                      filterBy(month);
                    });
                }
              );
            });
    </script>
</body>
</html>
```
