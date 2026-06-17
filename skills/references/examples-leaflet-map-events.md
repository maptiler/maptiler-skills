# Source: https://docs.maptiler.com/leaflet/examples/map-events/

# Vector Tiles in Leaflet JS

This example shows how to handle events of both the Leaflet map and the L.maptiler.maptilerLayer map together with a vector tiles layer. Discover how to incorporate interactivity and responsiveness into your map applications.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const leafletMap = L.map('map').setView([38.912753, -77.032194], 4);
      const mtLayer = L.maptiler.maptilerLayer({
        apiKey: key,
        style: L.maptiler.MapStyle.STREETS, // optional
        interactive: true
      }).addTo(leafletMap);

      const maptilerMap = mtLayer.getMaptilerSDKMap();

      // control that shows events info
      const info = L.control();

      info.onAdd = function (map) {
        this._div = L.DomUtil.create('div', 'info');
        this.events = {};
        return this._div;
      };

      info.update = function (event) {
        const currentevents = this.events;
        this.events = {...currentevents, ...event};
        this._div.innerHTML = `<div>Last <b>Leaflet</b> event: ${this.events.leaflet || ""}</div>
        <div>Last <b>MapTiler SDK</b> event: ${this.events.sdk || ""}</div>
        <div>Last <b>Vector layer</b> event: ${this.events.layer || ""}</div>
        `;
      };

      info.addTo(leafletMap);

      maptilerMap.on('load', () => {
        info.update({sdk:'load'});

        // let's see events on MapTiler SDK map
        maptilerMap.on('mousemove', () => { info.update({sdk:'mousemove'}) });
        maptilerMap.on('mouseenter', () => { info.update({sdk:'mouseenter'}) });
        maptilerMap.on('mouseout', () => { info.update({sdk:'mouseout'}) });
        maptilerMap.on('mouseleave', () => { info.update({sdk:'mouseleave'}) });
        maptilerMap.on('mouseover', () => { info.update({sdk:'mouseover'}) });

        // let's add some layer and fire events on it
        maptilerMap.addSource('states', {
          'type': 'geojson',
          'data': 'https://docs.maptiler.com/sdk-js/assets/us_states.geojson'
        });
        maptilerMap.addLayer({
          'id': 'state-fills',
          'type': 'fill',
          'source': 'states',
          'layout': {},
          'paint': {
            'fill-color': '#627BC1',
            'fill-opacity': ['case', ['boolean', ['feature-state', 'hover'], false], 1, 0.5 ]
          }
        });

        maptilerMap.on('mouseenter', 'state-fills', (e) => {info.update({layer:'mouseenter'}) });
        maptilerMap.on('mouseleave', 'state-fills', (e) => {info.update({layer:'mouseleave'}) });
      });

      // now let's see on leaflet map events
      leafletMap.on('mousemove', () => { info.update({leaflet:'mousemove'}) });
      leafletMap.on('mouseenter', () => { info.update({leaflet:'mouseenter'}) });
      leafletMap.on('mouseout', () => { info.update({leaflet:'mouseout'}) });
      leafletMap.on('mouseleave', () => { info.update({leaflet:'mouseleave'}) });
      leafletMap.on('mouseover', () => { info.update({leaflet:'mouseover'}) });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Vector Tiles in Leaflet JS</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <script src="https://cdn.maptiler.com/leaflet-maptilersdk/v4.1.0/leaflet-maptilersdk.umd.min.js"></script>
    <style>
        body { margin: 0; padding: 0; }
        #map { position: absolute; top: 0; bottom: 0; width: 100%; }
    </style>
</head>
<body>
    <div id="map"></div>
    <script>
        const key = 'YOUR_MAPTILER_API_KEY';

              const leafletMap = L.map('map').setView([38.912753, -77.032194], 4);
              const mtLayer = L.maptiler.maptilerLayer({
                apiKey: key,
                style: L.maptiler.MapStyle.STREETS, // optional
                interactive: true
              }).addTo(leafletMap);

              const maptilerMap = mtLayer.getMaptilerSDKMap();

              // control that shows events info
              const info = L.control();

              info.onAdd = function (map) {
                this._div = L.DomUtil.create('div', 'info');
                this.events = {};
                return this._div;
              };

              info.update = function (event) {
                const currentevents = this.events;
                this.events = {...currentevents, ...event};
                this._div.innerHTML = `<div>Last <b>Leaflet</b> event: ${this.events.leaflet || ""}</div>
                <div>Last <b>MapTiler SDK</b> event: ${this.events.sdk || ""}</div>
                <div>Last <b>Vector layer</b> event: ${this.events.layer || ""}</div>
                `;
              };

              info.addTo(leafletMap);

              maptilerMap.on('load', () => {
                info.update({sdk:'load'});

                // let's see events on MapTiler SDK map
                maptilerMap.on('mousemove', () => { info.update({sdk:'mousemove'}) });
                maptilerMap.on('mouseenter', () => { info.update({sdk:'mouseenter'}) });
                maptilerMap.on('mouseout', () => { info.update({sdk:'mouseout'}) });
                maptilerMap.on('mouseleave', () => { info.update({sdk:'mouseleave'}) });
                maptilerMap.on('mouseover', () => { info.update({sdk:'mouseover'}) });

                // let's add some layer and fire events on it
                maptilerMap.addSource('states', {
                  'type': 'geojson',
                  'data': 'https://docs.maptiler.com/sdk-js/assets/us_states.geojson'
                });
                maptilerMap.addLayer({
                  'id': 'state-fills',
                  'type': 'fill',
                  'source': 'states',
                  'layout': {},
                  'paint': {
                    'fill-color': '#627BC1',
                    'fill-opacity': ['case', ['boolean', ['feature-state', 'hover'], false], 1, 0.5 ]
                  }
                });

                maptilerMap.on('mouseenter', 'state-fills', (e) => {info.update({layer:'mouseenter'}) });
                maptilerMap.on('mouseleave', 'state-fills', (e) => {info.update({layer:'mouseleave'}) });
              });

              // now let's see on leaflet map events
              leafletMap.on('mousemove', () => { info.update({leaflet:'mousemove'}) });
              leafletMap.on('mouseenter', () => { info.update({leaflet:'mouseenter'}) });
              leafletMap.on('mouseout', () => { info.update({leaflet:'mouseout'}) });
              leafletMap.on('mouseleave', () => { info.update({leaflet:'mouseleave'}) });
              leafletMap.on('mouseover', () => { info.update({leaflet:'mouseover'}) });
    </script>
</body>
</html>
```
