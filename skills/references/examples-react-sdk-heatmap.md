# Source: https://docs.maptiler.com/react/sdk-js/heatmap/

# 

#### Maps in React series

In this series, we will learn how to create a map app in React with popups, a visualization switcher, geocoding control, 3D terrain, and a sidebar.

* Episode 0: [Map in React JS with Material UI](/react/sdk-js/get-started-material-ui/)
* Episode 1: [Map in React JS point data from geojson data](/react/sdk-js/geojson-points/)
* **Episode 2: Map in React JS create a heatmap**
* Episode 3: [Map in React js with popup and sidebar](/react/sdk-js/popup-sidebar/)
* Episode 4: [Map in React js with geocoding control](/react/sdk-js/geocoding-control/)
* Episode 5: [3D Map in React js with geocoding control](/react/sdk-js/3d-map/)

This example is the **Episode 2** of the Maps in React series. In this step-by-step tutorial, you’ll learn how to create a heatmap in your React JS map using the MapTiler SDK JS [heatmap helper](/sdk-js/api/helpers/#heatmap).

In this example, I’ll show you how to create a heatmap visualization of a point dataset and how to switch between this and the points.

By the end of this tutorial, you will be able to create a heatmap. With your newfound knowledge, you will be able to create visually stunning maps with React + Heatmap + MapTiler SDK. Take a look at the final output of this tutorial below:

<iframe style="height: 400px; width: 100%" src=""></iframe>

1. This tutorial builds on [Map in React JS point data from geojson data](/react/sdk-js/geojson-points/) code. (That tutorial shows how to build a simple full-screen map application with hundreds of points.) Heatmap is a visualization method that shows the spatial density of point data based on attribute weight or simply by spatial distribution.

1. Create a new layer with the heatmap helper. Open the `/src/components/Map/map.jsx` file and add the highlighted lines:

    <pre class="line-numbers" data-start="27" data-line-offset="26" data-line="38-40"><code class="language-jsx"><!--
    map.current.on("load", () => {
      maptilersdk.helpers.addPoint(map.current, {
        data: geodata,
        pointColor: maptilersdk.ColorRampCollection.COOL.scale(0, 30).reverse(),
        property: "minimum_nights",
        pointOpacity: 0.5,
        showLabel: true,
        labelColor: "black",
        pointRadius: 12,
      });

      maptilersdk.helpers.addHeatmap(map.current, {
        data: geodata,
      });
    });
    --></code></pre>

1. When use the heatmap visualization on the accommodation dataset for Hawaii, it shows that most of the accommodation is concentrated around the coast. It does this clearly without crowding the map with overlapping points.

    

1. Create a heatmap of accommodation based on the minimum nights' stay attribute. We can do this by setting up property and weight. In this example, we will exclude accommodation that can only be rented for more than 30 days.

    <pre class="line-numbers" data-start="38" data-line-offset="37" data-line="40-44"><code class="language-jsx"><!--
    maptilersdk.helpers.addHeatmap(map.current, {
      data: geodata,
      property: "minimum_nights",
      weight: [
        { propertyValue: 1, value: 1 },
        { propertyValue: 30, value: 0 },
      ],
    });
    --></code></pre>

1. Refresh the page and see that some points are now not being included in the calculations for the heatmap. But all the points have the same radius.

    

1. We will make the radius of the heatmap points also determined by a value of the property defined above.

    <pre class="line-numbers" data-start="38" data-line-offset="37" data-line="45-48"><code class="language-jsx"><!--
    maptilersdk.helpers.addHeatmap(map.current, {
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
    });
    --></code></pre>

1. **Optional**. If you would like to play with heatmap opacity or styling across zoom levels, look at the [heatmap helper documentation](/sdk-js/api/helpers/#heatmap).

1. Let's create the visualization switcher. This will allow users to turn the heatmap back into points, letting them zoom in and identify individual locations.

1. Import the Material UI `Button` component.

    <pre class="line-numbers" data-start="6" data-line-offset="5" data-line="6"><code class="language-jsx"><!--
    import { Button } from "@mui/material";
    import Box from "@mui/material/Box";
    --></code></pre>

1. Create a button. We will use Material UI to style it. 

    
    <pre class="line-numbers" data-start="56" data-line-offset="55" data-line="61-68"><code class="language-jsx"><!--
    return (
      <Box sx=>
        <Navbar />
        <div className="container">
          <div ref={mapContainer} id="map" className="map" />
          <Button 
            variant="contained"
            className="btn"
            sx=
            onClick={handleVisualizationChange}
          >
            Change to {selectedMapLayer === "point" ? "heatmap" : "point"}
          </Button>
        </div>
      </Box>
    );
    --></code></pre>
    

1. In the `handleVisualizationChange` function, we want to change the selected layer.

    <pre class="line-numbers" data-start="56" data-line-offset="57" data-line="56-58"><code class="language-jsx"><!--
    const handleVisualizationChange = () => {
      setSelectedMapLayer((prev) => (prev === "point" ? "heatmap" : "point"));
    };
    --></code></pre>

1. Create `selectedMapLayer` state to show the selected layer.

    <pre class="line-numbers" data-start="16" data-line-offset="15" data-line="17"><code class="language-jsx"><!--
    maptilersdk.config.apiKey = configData.MAPTILER_API_KEY;
    const [selectedMapLayer, setSelectedMapLayer] = useState("point"); // 'point' or 'heatmap'
    --></code></pre>

1. In order to switch between visualizations, we need to be able to make layers created by the MapTilerSDK helpers visible or invisible. This means we'll need to know the ID of each layer. Check out the [MapTiler SDK helpers](/sdk-js/api/helpers/) documentation to learn how to get the IDs of each layers.

1. We will use states to prevent errors caused by setting the visibility of a nonexistent layer.

    <pre class="line-numbers" data-start="16" data-line-offset="15" data-line="17-19,21"><code class="language-jsx"><!--
    maptilersdk.config.apiKey = configData.MAPTILER_API_KEY;
    const [heatmapLayer, setHeatmapLayer] = useState("");
    const [pointLayer, setPointLayer] = useState("");
    const [pointLabels, setPointLabels] = useState("");
    const [selectedMapLayer, setSelectedMapLayer] = useState("point"); // 'point' or 'heatmap'
    const [mapLoaded, setMapLoaded] = useState(false);
    --></code></pre>

1. Now let's set the IDs of individual layers.

    <pre class="line-numbers" data-start="33" data-line-offset="32" data-line="34,44,56-59"><code class="language-jsx"><!--
    map.current.on("load", () => {
      const { pointLayerId, labelLayerId } = maptilersdk.helpers.addPoint(map.current, {
        data: geodata,
        pointColor: maptilersdk.ColorRampCollection.COOL.scale(0, 30).reverse(),
        property: "minimum_nights",
        pointOpacity: 0.5,
        showLabel: true,
        labelColor: "black",
        pointRadius: 12,
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
      });
      setHeatmapLayer(heatmapLayerId);
      setPointLabels(labelLayerId);
      setPointLayer(pointLayerId);
      setMapLoaded(true);
    });
    --></code></pre>

1. Change layers visibility only after the map is loaded. `setLayoutProperties` has 3 arguments `layerId`, `name`, and `value`. If the layer is selected, then the visibility should be set to `visible` otherwise it should be `none`.

    <pre class="line-numbers" data-start="64" data-line-offset="63" data-line="64-87"><code class="language-jsx"><!--
    useEffect(() => {
      if (heatmapLayer && mapLoaded) {
        map.current.setLayoutProperty(
          heatmapLayer,
          "visibility",
          selectedMapLayer === "heatmap" ? "visible" : "none",
        );
      }
    }, [heatmapLayer, selectedMapLayer, mapLoaded]);

    useEffect(() => {
      if (pointLayer && mapLoaded) {
        map.current.setLayoutProperty(
          pointLayer,
          "visibility",
          selectedMapLayer === "point" ? "visible" : "none",
        );
        map.current.setLayoutProperty(
          pointLabels,
          "visibility",
          selectedMapLayer === "point" ? "visible" : "none",
        );
      }
    }, [pointLayer, selectedMapLayer, mapLoaded]);
    --></code></pre>

1. Congratulations! You have created a heatmap, and added a button to your application to switch between displaying the point layer or the heatmap.

    

### Full code to download

We have created a repository with the result of this tutorial that will serve as a basis to build future applications. You can access the repository at [Maps in React](https://github.com/maptiler/maps-in-react/tree/E2-heatmap){:target="_blank" rel="noopener"}.

## Next episode

Continue to [Episode 3: Map in React js with popup and sidebar](/react/sdk-js/popup-sidebar/) to learn how to create a map with a sidebar and popup in your React JS map using the MapTiler SDK JS.
