# Source: https://docs.maptiler.com/react/maplibre-gl-js/geocoding-control/

# 

This tutorial shows how to search for places using the [Geocoding control](https://www.npmjs.com/package/@maptiler/geocoding-control){:target="\_blank" rel="noopener"}. The geocoder component facilitates the use of the [MapTiler Geocoding API](https://www.maptiler.com/cloud/geocoding/){:target="\_blank" rel="noopener"}.



1. Follow the [How to display MapLibre GL JS map using React JS](../how-to-use-maplibre-gl-js/) tutorial to create a simple fullscreen map application. You **do not need** to add the marker to the map.

1. Install the Geocoding control module

    ```bash
    npm install --save @maptiler/geocoding-control
    ```

1. Import the Geocoding control and the required React functions. Add these lines on top of `map.jsx` file.

    <pre class="line-numbers" data-start="1" data-line-offset="0" data-line="3"><code class="language-jsx"><!--
    import React, { useRef, useEffect, useState } from 'react'; 
    import maplibregl from 'maplibre-gl';
    import { GeocodingControl } from "@maptiler/geocoding-control/maplibregl";
    import 'maplibre-gl/dist/maplibre-gl.css'; 
    import './map.css';
    --></code></pre>

1. Create the `GeocodingControl` ref

    <pre class="line-numbers" data-start="15" data-line-offset="14" data-line="16"><code class="language-jsx"><!--
    const [API_KEY] = useState('YOUR_MAPTILER_API_KEY_HERE');
    const control = useRef<GeocodingControl>(null);
    --></code></pre>

1. Add the `GeocodingControl` to the map. Use the current MapLibre map.

    <pre class="line-numbers" data-start="18" data-line-offset="17" data-line="29-30"><code class="language-jsx"><!--
    useEffect(() => {
        if (map.current) return; // stops map from intializing more than once
        
        map.current = new maplibregl.Map({
          container: mapContainer.current,
          style: `https://api.maptiler.com/maps/streets-v4/style.json?key=${API_KEY}`,
          center: [lng, lat],
          zoom: zoom
        });
    
        map.current.addControl(new maplibregl.NavigationControl(), 'top-right');
        control.current = new GeocodingControl({apiKey: API_KEY});
        map.current.addControl(control.current);
      
      }, [API_KEY, lng, lat, zoom]);
    --></code></pre>

We are finished, your `map.jsx` file should look like this:

<pre class="line-numbers" data-start="1" data-line-offset="0"><code class="language-jsx"><!--
import React, { useRef, useEffect, useState } from 'react';
import maplibregl from 'maplibre-gl';
import { GeocodingControl } from "@maptiler/geocoding-control/maplibregl";
import 'maplibre-gl/dist/maplibre-gl.css';
import './map.css';

export default function Map() {
  const mapContainer = useRef(null);
  const map = useRef(null);
  const lng = 139.753;
  const lat = 35.6844;
  const zoom = 14;
  const API_KEY = 'YOUR_MAPTILER_API_KEY_HERE';
  const control = useRef<GeocodingControl>(null);

  useEffect(() => {
    if (map.current) return; // stops map from intializing more than once
    
    map.current = new maplibregl.Map({
      container: mapContainer.current,
      style: `https://api.maptiler.com/maps/streets-v4/style.json?key=${API_KEY}`,
      center: [lng, lat],
      zoom: zoom
    });

    map.current.addControl(new maplibregl.NavigationControl(), 'top-right');
    control.current = new GeocodingControl({apiKey: API_KEY});
    map.current.addControl(control.current);
  
  }, [API_KEY, lng, lat, zoom]);

  return (
    <div className="map-wrap">
      <div ref={mapContainer} className="map" />
    </div>
  );
}
--></code></pre>

your `map.ccs` file should look like this:

<pre class="line-numbers" data-start="1" data-line-offset="0"><code class="language-css"><!--
.map-wrap {
  position: relative;
  width: 100%;
  height: calc(100vh - 77px); /* calculate height of the screen minus the heading */
}

.map {
  position: absolute;
  width: 100%;
  height: 100%;
}
--></code></pre>

> [!NOTE]
> The library also has types defined to be used in **TypeScript**.

{:#github-link}
[MapTiler Geocoding control on GitHub](https://github.com/maptiler/maptiler-geocoding-control){:target="\_blank" rel="noopener"}

## Learn more

Visit the [MapTiler Geocoding API reference](https://docs.maptiler.com/cloud/api/geocoding/) for all search options. For example specifying the language of the results, etc.
