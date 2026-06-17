# Source: https://docs.maptiler.com/sdk-js/examples/point-filtering/

# Point filtering

Filter thousands of features in real time to quickly and easily find those with a property that meets your search criteria.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
let studentMax = 0;

    map.on('load', async () => {
      const dataRes = await fetch('https://docs.maptiler.com/sdk-js/assets/Public_School_Characteristics_2020-21_los_angeles_name_number.geojson');
      const data = await dataRes.json();
      
      for (let i = 0; i < data.features.length; i += 1) {
          studentMax = Math.max(studentMax, data.features[i].properties.students);
      }


      $("#sampleSlider").ionRangeSlider({
        type: "double",
        skin: "round",
        hide_min_max: false,
        force_edges: true,
        min: 0,
        max: studentMax,
        grid: false,
        onChange: function (values) {
          const source = map.getSource('school_source');
          const {from, to} = values;
          if (!source) return;
          filterBy(from, to);
          //const filteredData = filterData(data, from, to);
          //source.setData(filteredData);
        },
      });

      // add a clustered GeoJSON source for a sample set of earthquakes
      map.addSource('school_source', {
        'type': 'geojson',
        'data': data,
      });

      map.addLayer({
        'id': 'school_point',
        'type': 'circle',
        'source': 'school_source',
        'minzoom': 0,
        'paint': {
          'circle-pitch-alignment': "map",
          // Size circle radius by earthquake magnitude and zoom level
          'circle-radius': [
            'interpolate',
            ['linear'],
            ['zoom'],
            // 0, ['interpolate', ['linear'], ['get', 'students'], 10, 0.1, 4000, 0.01],
            4, [
              'interpolate',['linear'], ['get', 'students'], 
              10, 0.01,
              4000, 0.1
            ],
            8, [
              'interpolate',['linear'], ['get', 'students'], 
              10, 1,
              4000, 4
            ],
            16, [
              'interpolate', ['linear'], ['get', 'students'],
              10, 5,
              4000, 50
            ]
          ],
          // Color circle by earthquake magnitude
          'circle-color': [
            'interpolate',
            ['linear'],
            ['get', 'students'],
            0, "rgba(255, 255, 0, 0)",
            50, "rgba(255, 255, 0, 1)",
            2000, "rgba(255, 0, 0, 1)",
            5000, "rgba(50, 0, 0, 1)",
          ],
          // 'circle-stroke-color': 'white',
          'circle-stroke-width': 0,
          // Transition from heatmap to circle layer by zoom level
          'circle-opacity': [
            'interpolate',
            ['linear'],
            ['zoom'],
            3, 0, // zoom, opacity
            5, 0.3,
            8, 0.8,
          ]
        }
      });

    });

    map.on("mouseenter", "school_point", (e) => {
      if (!e.features) return;
      if (!e.features.length) return;
      if (!e.features[0].properties) return;
      if (!e.features[0].properties.name) return;
      if (!e.features[0].properties.students) return;

      const display = `${e.features[0].properties.name} (${e.features[0].properties.students} students)`

      document.querySelector(".infoContainer").innerHTML = display;
      document.querySelector(".infoContainer").style.display = "block";
    });

    map.on("mouseleave", "school_point", (e) => {
      document.querySelector(".infoContainer").innerHTML = "";
      document.querySelector(".infoContainer").style.display = "none";
    });

    function filterBy(min, max) {
        const filters = [
          'all', 
          [">=", 'students', min],
          ["<=", 'students', max]
        ];
        map.setFilter('school_point', filters);
    }
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Point filtering</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <link href="https://cdnjs.cloudflare.com/ajax/libs/ion-rangeslider/2.3.1/css/ion.rangeSlider.min.css" rel="stylesheet" />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/ion-rangeslider/2.3.1/js/ion.rangeSlider.min.js"></script>
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
            center: [-118, 34],
            zoom: 10
        });

        let studentMax = 0;

            map.on('load', async () => {
              const dataRes = await fetch('https://docs.maptiler.com/sdk-js/assets/Public_School_Characteristics_2020-21_los_angeles_name_number.geojson');
              const data = await dataRes.json();

              for (let i = 0; i < data.features.length; i += 1) {
                  studentMax = Math.max(studentMax, data.features[i].properties.students);
              }


              $("#sampleSlider").ionRangeSlider({
                type: "double",
                skin: "round",
                hide_min_max: false,
                force_edges: true,
                min: 0,
                max: studentMax,
                grid: false,
                onChange: function (values) {
                  const source = map.getSource('school_source');
                  const {from, to} = values;
                  if (!source) return;
                  filterBy(from, to);
                  //const filteredData = filterData(data, from, to);
                  //source.setData(filteredData);
                },
              });

              // add a clustered GeoJSON source for a sample set of earthquakes
              map.addSource('school_source', {
                'type': 'geojson',
                'data': data,
              });

              map.addLayer({
                'id': 'school_point',
                'type': 'circle',
                'source': 'school_source',
                'minzoom': 0,
                'paint': {
                  'circle-pitch-alignment': "map",
                  // Size circle radius by earthquake magnitude and zoom level
                  'circle-radius': [
                    'interpolate',
                    ['linear'],
                    ['zoom'],
                    // 0, ['interpolate', ['linear'], ['get', 'students'], 10, 0.1, 4000, 0.01],
                    4, [
                      'interpolate',['linear'], ['get', 'students'], 
                      10, 0.01,
                      4000, 0.1
                    ],
                    8, [
                      'interpolate',['linear'], ['get', 'students'], 
                      10, 1,
                      4000, 4
                    ],
                    16, [
                      'interpolate', ['linear'], ['get', 'students'],
                      10, 5,
                      4000, 50
                    ]
                  ],
                  // Color circle by earthquake magnitude
                  'circle-color': [
                    'interpolate',
                    ['linear'],
                    ['get', 'students'],
                    0, "rgba(255, 255, 0, 0)",
                    50, "rgba(255, 255, 0, 1)",
                    2000, "rgba(255, 0, 0, 1)",
                    5000, "rgba(50, 0, 0, 1)",
                  ],
                  // 'circle-stroke-color': 'white',
                  'circle-stroke-width': 0,
                  // Transition from heatmap to circle layer by zoom level
                  'circle-opacity': [
                    'interpolate',
                    ['linear'],
                    ['zoom'],
                    3, 0, // zoom, opacity
                    5, 0.3,
                    8, 0.8,
                  ]
                }
              });

            });

            map.on("mouseenter", "school_point", (e) => {
              if (!e.features) return;
              if (!e.features.length) return;
              if (!e.features[0].properties) return;
              if (!e.features[0].properties.name) return;
              if (!e.features[0].properties.students) return;

              const display = `${e.features[0].properties.name} (${e.features[0].properties.students} students)`

              document.querySelector(".infoContainer").innerHTML = display;
              document.querySelector(".infoContainer").style.display = "block";
            });

            map.on("mouseleave", "school_point", (e) => {
              document.querySelector(".infoContainer").innerHTML = "";
              document.querySelector(".infoContainer").style.display = "none";
            });

            function filterBy(min, max) {
                const filters = [
                  'all', 
                  [">=", 'students', min],
                  ["<=", 'students', max]
                ];
                map.setFilter('school_point', filters);
            }
    </script>
</body>
</html>
```
