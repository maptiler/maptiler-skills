# Source: https://docs.maptiler.com/react/sdk-js/3d-map/

# 

#### Maps in React series

In this series, we will learn how to create a map app in React with popups, a visualization switcher, geocoding control, 3D terrain, and a sidebar.

* Episode 0: [Map in React JS with Material UI](/react/sdk-js/get-started-material-ui/)
* Episode 1: [Map in React JS point data from geojson data](/react/sdk-js/geojson-points/)
* Episode 2: [Map in React JS create a heatmap](/react/sdk-js/heatmap/)
* Episode 3: [Map in React js with popup and sidebar](/react/sdk-js/popup-sidebar/)
* Episode 4: [Map in React js with geocoding control](/react/sdk-js/geocoding-control/)
* **Episode 5: 3D Map in React js with geocoding control**

This example is the **Episode 5** of the Maps in React series. In this step-by-step tutorial, you’ll learn how to a 3D terrain map in your React JS map using the MapTiler SDK JS. 

In this example, I’ll focus on adding the 3D terrain to our React + MUI map. You will also learn to add custom map and show the map labels before your data visualization layer.

By the end of this tutorial, you will be able to create a 3D terrain custom map with a geocoding control. With your newfound knowledge, you will be able to create visually stunning 3D maps with React + MapTiler SDK. Take a look at the final output of this tutorial below:

<iframe style="height: 400px; width: 100%" src=""></iframe>

1. This tutorial builds on [Map in React js with geocoding control](/react/sdk-js/geocoding-control/) code. (That tutorial shows how to create a map with a geocoding control to search places).

1. Change the map style. To see the 3D terrain relief better, we need a map style with some visualization of the terrain. The best choices from the standard maps offered by MapTiler are Backdrop or Outdoor.

    <pre class="line-numbers" data-start="51" data-line-offset="50" data-line="53"><code class="language-jsx"><!--
    map.current = new maptilersdk.Map({
      container: mapContainer.current,
      style: maptilersdk.MapStyle.BACKDROP,
      center: [center.lng, center.lat],
      zoom: zoom, 
      hash: true,
    });
    --></code></pre>

1. As you can see, Backdrop has a strong coast line and small labels. To make our map more visually attractive we can customize it. If you would like to know how to customize MapTiler maps, read about [Maps & styles basics](/guides/map-design/maps-and-styles-basics).

    

1. Change the map style to your custom map. In this example we are going to use a custom map that better suits the visualization of our data. To add a custom map, you need to know its id. Go to your MapTiler account and select a map you want to use. Scroll to vector style and copy its ID.

    <pre class="line-numbers" data-start="51" data-line-offset="50" data-line="53"><code class="language-jsx"><!--
    map.current = new maptilersdk.Map({
      container: mapContainer.current,
      style: 'YOUR_CUSTOM_MAP_ID',
      center: [center.lng, center.lat],
      zoom: zoom, 
      hash: true,
    });
    --></code></pre>

    Replace `YOUR_CUSTOM_MAP_ID` with your actual MapTiler map ID.

1. Let's show the labels before our data layers. That is great for orientation in the map. All MapTiler SDK helper layers have a `beforeId` option where you can specify the ID of an existing layer before which the new layer will be inserted. To find the ID of this layer, you need to go to MapTiler and **select the map** you are using in your application. Then press the **Customize button**. In the  application go to the **Layers tab** then change to the **Verticality tab** and **find the layer** you are interested in. Click on the layer and **open the JSON editor** and **copy the layer ID**, in our case, "Ocean labels".

    

1. Add the `beforeId` option to the points and heatmap layers.

    <pre class="line-numbers" data-start="67" data-line-offset="66" data-line="75,89"><code class="language-jsx"><!--
    const { pointLayerId, labelLayerId } = maptilersdk.helpers.addPoint(map.current, {
      data: geodata,
      pointColor: maptilersdk.ColorRampCollection.COOL.scale(0, 30).reverse(),
      property: "minimum_nights",
      pointOpacity: 0.5,
      showLabel: true,
      labelColor: "black",
      pointRadius: 12,
      beforeId: "Ocean labels",
    });

    const { heatmapLayerId } = maptilersdk.helpers.addHeatmap(map.current, {
      data: geodata,
      property: "minimum_nights",
      weight: [
        { propertyValue: 1, value: 1 },
        { propertyValue: 30, value: 0 },
      ],
      radius: [
        { propertyValue: 1, value: 60 },
        { propertyValue: 30, value: 0 },
      ],
      beforeId: "Ocean labels",
    });
    --></code></pre>

1. Add the terrain to the map. Just add the `terrain: true` to the map constructor options.

    <pre class="line-numbers" data-start="51" data-line-offset="50" data-line="57"><code class="language-jsx"><!--
    map.current = new maptilersdk.Map({
      container: mapContainer.current,
      style: 'YOUR_CUSTOM_MAP_ID',
      center: [center.lng, center.lat],
      zoom: zoom, 
      hash: true,
      terrain: true,
    });
    --></code></pre>

1. Rotate and tilt the map to check that 3D terrain is present.

    

1. Add the Terrain control to enable/disable the 3D terrain. Again, this can be done by just adding the `terrainControl` option in the map.

    <pre class="line-numbers" data-start="51" data-line-offset="50" data-line="58"><code class="language-jsx"><!--
    map.current = new maptilersdk.Map({
      container: mapContainer.current,
      style: 'YOUR_CUSTOM_MAP_ID',
      center: [center.lng, center.lat],
      zoom: zoom, 
      hash: true,
      terrain: true,
      terrainControl: true,
    });
    --></code></pre>

1. Tilt/Untilt the map when the users click on the terrain control. The 3D terrain is truly visible only when the map is tilted. 

    <pre class="line-numbers" data-start="60" data-line-offset="59" data-line="60-67"><code class="language-jsx"><!--
    //change map pitch when terrain is loaded
    map.current.on("terrain", function () {
      if (map.current.hasTerrain()) {
        map.current.easeTo({ pitch: 60 });
      } else {
        map.current.easeTo({ pitch: 0 });
      }
    });
    --></code></pre>

1. Reload the map on your page and use the terrain control to toggle the terrain on and off. We can now see the effect of the transition between the map with 3D terrain and the map without terrain.

1. Let's adjust the animation speed so that the transition is slower.

    <pre class="line-numbers" data-start="60" data-line-offset="59" data-line="63,65"><code class="language-jsx"><!--
    //change map pitch when terrain is loaded
    map.current.on("terrain", function () {
      if (map.current.hasTerrain()) {
        map.current.easeTo({ pitch: 60, duration: 2000 });
      } else {
        map.current.easeTo({ pitch: 0, duration: 2000 });
      }
    });
    --></code></pre>

1. Congratulations! You have created a 3D map in React JS.

    

### Full code to download

We have created a repository with the result of this tutorial that will serve as a basis to build future applications. You can access the repository at [Maps in React](https://github.com/maptiler/maps-in-react/tree/E5-3D-terrain){:target="_blank" rel="noopener"}.
