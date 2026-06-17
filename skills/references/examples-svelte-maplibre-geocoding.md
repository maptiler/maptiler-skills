# Source: https://docs.maptiler.com/svelte/maplibre-gl-js/geocoding-control/

# 

This tutorial shows how to search for places using the [Geocoding control](https://www.npmjs.com/package/@maptiler/geocoding-control){:target="\_blank" rel="noopener"}. The geocoder component facilitates the use of the [MapTiler Geocoding API](https://www.maptiler.com/cloud/geocoding/){:target="\_blank" rel="noopener"}.



1. Follow the [How to display a map in Svelte using MapLibre GL JS](../how-to-use-maplibre-gl-js/) tutorial to create a simple full-screen map application. You **do not need** to add the marker to the map.

1. Install the Geocoding control module

   ```bash
   npm install --save @maptiler/geocoding-control
   ```

1. Import the Geocoding control. Add these lines on top of `Map.Svelte` file.

    <pre class="line-numbers" data-start="2" data-line-offset="1" data-line="3"><code class="language-js"><!--
    import { onMount, onDestroy } from 'svelte';
    import { GeocodingControl } from "@maptiler/geocoding-control/maplibregl";
    import maplibregl, { Map, NavigationControl } from 'maplibre-gl';
    import 'maplibre-gl/dist/maplibre-gl.css';
    --></code></pre>

1. Create the geocoderControl variable

    <pre class="line-numbers" data-start="9" data-line-offset="8" data-line="10"><code class="language-js"><!--
    let mapContainer;
    let geocoderControl;
    --></code></pre>

1. Create the apiKey variable

    <pre class="line-numbers" data-start="11" data-line-offset="10" data-line="12"><code class="language-js"><!--
      let geocoderControl;
      const apiKey = 'YOUR_MAPTILER_API_KEY_HERE';
    --></code></pre>

1. Add the `GeocodingControl` component to the map. Use the current MapTiler SDK JS map.

    <pre class="line-numbers" data-start="14" data-line-offset="13" data-line="25-29"><code class="language-js"><!--
    onMount(() => {
      const initialState = { lng: 139.753, lat: 35.6844, zoom: 14 };
    
      map = new Map({
        container: mapContainer,
        style: `https://api.maptiler.com/maps/streets-v4/style.json?key=${apiKey}`,
        center: [initialState.lng, initialState.lat],
        zoom: initialState.zoom
      });
    
      map.addControl(new NavigationControl(), 'top-right');
      geocoderControl = new GeocodingControl({ apiKey: apiKey });
      geocoderControl.on("select", (data) => {
        console.log("select", data);
      });
      map.addControl(geocoderControl);
    });
    --></code></pre>

We are finished, your `Map.Svelte` file should look like this:

<pre class="line-numbers" data-start="1" data-line-offset="0"><code class="language-html"><!--
<script>
  import { onMount, onDestroy } from 'svelte';
  import { GeocodingControl } from "@maptiler/geocoding-control/maplibregl";
  import maplibregl, { Map, NavigationControl } from 'maplibre-gl';
  import 'maplibre-gl/dist/maplibre-gl.css';

  let map;
  let mapContainer;
  let geocoderControl;
  const apiKey = 'YOUR_MAPTILER_API_KEY_HERE';

  onMount(() => {
    const initialState = { lng: 139.753, lat: 35.6844, zoom: 14 };

    map = new Map({
      container: mapContainer,
      style: `https://api.maptiler.com/maps/streets-v4/style.json?key=${apiKey}`,
      center: [initialState.lng, initialState.lat],
      zoom: initialState.zoom
    });

    map.addControl(new NavigationControl(), 'top-right');
    geocoderControl = new GeocodingControl({ apiKey: apiKey });
    geocoderControl.on("select", (data) => {
      console.log("select", data);
    });
    map.addControl(geocoderControl);
  });

  onDestroy(() => {
    map.remove();
  });
</script>

<div class="map-wrap">
  <a href="https://www.maptiler.com" class="watermark"></a>
  <div class="map" bind:this={mapContainer}></div>
</div>

<style>
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

  .watermark {
    position: absolute;
    left: 10px;
    bottom: 10px;
    z-index: 999;
  }
</style>

--></code></pre>

> [!NOTE]
> The library also has types defined to be used in **TypeScript**.

{:#github-link}
[MapTiler Geocoding control on GitHub](https://github.com/maptiler/maptiler-geocoding-control){:target="\_blank" rel="noopener"}

## Learn more

Visit the [MapTiler Geocoding API reference](https://docs.maptiler.com/cloud/api/geocoding/) for all search options. For example specifying the language of the results, etc.
