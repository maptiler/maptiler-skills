# Source: https://docs.maptiler.com/svelte/sdk-js/geocoding-control/

# 

This tutorial shows how to search for places using the [Geocoding control](https://www.npmjs.com/package/@maptiler/geocoding-control){:target="\_blank" rel="noopener"}. The geocoder component facilitates the use of the [MapTiler Geocoding API](https://www.maptiler.com/cloud/geocoding/){:target="\_blank" rel="noopener"}.



1. Follow the [How to display a map in Svelte using MapTile SDK JS](/svelte/) tutorial to create a simple full-screen map application. You **do not need** to add the marker to the map.

1. Install the Geocoding control module

    ```bash
    npm install --save @maptiler/geocoding-control
    ```

1. Import the Geocoding control. Add these lines on top of `Map.Svelte` file.

    <pre class="line-numbers" data-start="2" data-line-offset="1" data-line="3"><code class="language-js"><!--
    import { onMount, onDestroy } from 'svelte';
    import { GeocodingControl } from "@maptiler/geocoding-control/maptilersdk";
    import * as maptilersdk from '@maptiler/sdk';
    import {Map, MapStyle, config} from '@maptiler/sdk';
    import "@maptiler/sdk/dist/maptiler-sdk.css";
    --></code></pre>

1. Create the geocoderControl variable

    <pre class="line-numbers" data-start="10" data-line-offset="9" data-line="11"><code class="language-js"><!--
      let mapContainer;
      let geocoderControl;
    --></code></pre>

1. Create the apiKey variable

    <pre class="line-numbers" data-start="11" data-line-offset="10" data-line="12-14"><code class="language-js"><!--
      let geocoderControl;
      const apiKey = 'YOUR_MAPTILER_API_KEY_HERE';
    
      config.apiKey = apiKey;
    --></code></pre>

1. Add the `GeocodingControl` component to the map. Use the current MapTiler SDK JS map.

    <pre class="line-numbers" data-start="16" data-line-offset="15" data-line="26-30"><code class="language-js"><!--
    onMount(() => {
      const initialState = { lng: 139.753, lat: 35.6844, zoom: 14 };
    
      map = new Map({
        container: mapContainer,
        style: MapStyle.STREETS,
        center: [initialState.lng, initialState.lat],
        zoom: initialState.zoom
      });
    
      geocoderControl = new GeocodingControl();
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
  import { GeocodingControl } from "@maptiler/geocoding-control/maptilersdk";
  import * as maptilersdk from '@maptiler/sdk';
  import {Map, MapStyle, config} from '@maptiler/sdk';
  import "@maptiler/sdk/dist/maptiler-sdk.css";

  let map;
  let mapContainer;
  let geocoderControl;
  const apiKey = 'YOUR_MAPTILER_API_KEY_HERE';

  config.apiKey = apiKey;

  onMount(() => {
    const initialState = { lng: 139.753, lat: 35.6844, zoom: 14 };

    map = new Map({
      container: mapContainer,
      style: MapStyle.STREETS,
      center: [initialState.lng, initialState.lat],
      zoom: initialState.zoom
    });

    geocoderControl = new GeocodingControl();
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
</style>

--></code></pre>

> [!NOTE]
> The library also has types defined to be used in **TypeScript**.

{:#github-link}
[MapTiler Geocoding control on GitHub](https://github.com/maptiler/maptiler-geocoding-control){:target="\_blank" rel="noopener"}

## Learn more

Visit the [MapTiler Geocoding API reference](https://docs.maptiler.com/cloud/api/geocoding/) for all search options. For example specifying the language of the results, etc.
