# Source: https://docs.maptiler.com/react/sdk-js/geocoding-component/

# 

This tutorial shows how to search for places using the [Geocoding control](https://www.npmjs.com/package/@maptiler/geocoding-control){:target="\_blank" rel="noopener"}. The geocoder component facilitates the use of the [MapTiler Geocoding API](https://www.maptiler.com/cloud/geocoding/){:target="\_blank" rel="noopener"}.



1. Follow the [React JS with MapTiler maps](/react/) tutorial to create a simple fullscreen map application. You **do not need** to add the marker to the map.

1. Install the Geocoding control module

    ```bash
    npm install --save @maptiler/geocoding-control
    ```

1. Import the Geocoding control and the required React functions. Add these lines on top of `map.jsx` file.

    <pre class="line-numbers" data-start="1" data-line-offset="0" data-line="3"><code class="language-jsx"><!--
    import React, { useRef, useEffect, useState } from 'react'; 
    import * as maptilersdk from '@maptiler/sdk';
    import { GeocodingControl } from "@maptiler/geocoding-control/maptilersdk";
    import "@maptiler/sdk/dist/maptiler-sdk.css"; 
    import './map.css';
    --></code></pre>

1. Create the `GeocodingControl` ref

  <pre class="line-numbers" data-start="12" data-line-offset="11" data-line="12"><code class="language-jsx"><!--
  const control = useRef<GeocodingControl>(null);
  --></code></pre>

1.  Add the `GeocodingControl` to the map. Use the current MapTiler SDK map.

    <pre class="line-numbers" data-start="17" data-line-offset="16" data-line="27-28"><code class="language-jsx"><!--
    useEffect(() => {
        if (map.current) return; // stops map from intializing more than once
        
        map.current = new maptilersdk.Map({
          container: mapContainer.current,
          style: maptilersdk.MapStyle.STREETS,
          center: [tokyo.lng, tokyo.lat],
          zoom: zoom
        });
    
        control.current = new GeocodingControl();
        map.current.addControl(control.current);
      
      }, [tokyo.lng, tokyo.lat, zoom]);
    --></code></pre>

We are finished, your `map.jsx` file should look like this:

<pre class="line-numbers" data-start="1" data-line-offset="0"><code class="language-jsx"><!--
import React, { useRef, useEffect, useState } from 'react';
import * as maptilersdk from '@maptiler/sdk';
import { GeocodingControl } from "@maptiler/geocoding-control/maptilersdk";
import "@maptiler/sdk/dist/maptiler-sdk.css";
import './map.css';

export default function Map() {
  const mapContainer = useRef(null);
  const map = useRef(null);
  const control = useRef<GeocodingControl>(null);
  const tokyo = { lng: 139.753, lat: 35.6844 };
  const zoom = 14;
  maptilersdk.config.apiKey = 'YOUR_MAPTILER_API_KEY_HERE';

  useEffect(() => {
    if (map.current) return; // stops map from intializing more than once
  
    map.current = new maptilersdk.Map({
      container: mapContainer.current,
      style: maptilersdk.MapStyle.STREETS,
      center: [tokyo.lng, tokyo.lat],
      zoom: zoom
    });

    control.current = new GeocodingControl();
    map.current.addControl(control.current);
  
  }, [tokyo.lng, tokyo.lat, zoom]);

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
