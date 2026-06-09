# Source: https://docs.maptiler.com/react/sdk-js/geocoding-control/

# 

#### Maps in React series

In this series, we will learn how to create a map app in React with popups, a visualization switcher, geocoding control, 3D terrain, and a sidebar.

- Episode 0: [Map in React JS with Material UI](/react/sdk-js/get-started-material-ui/)
- Episode 1: [Map in React JS point data from geojson data](/react/sdk-js/geojson-points/)
- Episode 2: [Map in React JS create a heatmap](/react/sdk-js/heatmap/)
- Episode 3: [Map in React js with popup and sidebar](/react/sdk-js/popup-sidebar/)
- **Episode 4: Map in React js with geocoding control**
- Episode 5: [3D Map in React js with geocoding control](/react/sdk-js/3d-map/)

This example is the **Episode 4** of the Maps in React series. In this step-by-step tutorial, you’ll learn how to create a map with a geocoding control in your React JS map using the MapTiler SDK JS. The [geocoding control](/sdk-js/modules/geocoding/) facilitates the use of the [MapTiler Geocoding API](https://www.maptiler.com/cloud/geocoding/){:target="\_blank" rel="noopener"} to search places (States, Cities, Streets, Addresses, POIs, ...).

In this example, I’ll focus on adding the geocoding control to our React + MUI map.

{:#github-link}
[MapTiler Geocoding control on GitHub](https://github.com/maptiler/maptiler-geocoding-control){:target="\_blank" rel="noopener"}

By the end of this tutorial, you will be able to create a map with a geocoding control. With your newfound knowledge, you will be able to create visually stunning maps with React + Geocoding Control + MapTiler SDK. Take a look at the final output of this tutorial below:

<iframe style="height: 400px; width: 100%" src=""></iframe>

1. This tutorial builds on [Map in React js with popup and sidebar](/react/sdk-js/popup-sidebar/) code. (That tutorial shows how to create a map with a sidebar and popup).

1. Install MapTiler Geocoding control library, navigate to your project folder and run the command:

    ```bash
    npm i @maptiler/geocoding-control
    ```

1. Import the `geocodingControl` and its styles into the `src/components/Map/map.jsx` component. In this example we will not be using the geocodingControl React component. In the example [MapTiler SDK JS geocoding component how to search places using React JS](/react/sdk-js/geocoding-component/) you can see how to use the component on a map. You can also use the geocodingControl component if you need the geocoding control without a map.

 <pre class="line-numbers" data-start="2" data-line-offset="1" data-line="4"><code class="language-jsx"><!--
 import * as maptilersdk from "@maptiler/sdk";
 import "@maptiler/sdk/dist/maptiler-sdk.css";
 import { GeocodingControl } from "@maptiler/geocoding-control/maptilersdk";
 --></code></pre>

1. Add the `geocodingControl` to the map.

 <pre class="line-numbers" data-start="58" data-line-offset="57" data-line="58-59"><code class="language-jsx"><!--
 const gc = new GeocodingControl();
 map.current.addControl(gc);
 --></code></pre>

1. We already have the geocoding control working on our map.

    

1. Let's add some options to the `geocodingControl` to improve the results. Limit the number of results to 3.

 <pre class="line-numbers" data-start="58" data-line-offset="57" data-line="58-60"><code class="language-jsx"><!--
 const gc = new GeocodingControl({
    limit: 3, // limit result number
 });
 map.current.addControl(gc);
 --></code></pre>

1. Limit the results to a specific country. Since our map is in Honolulu we will limit the results to the United States of America.

 <pre class="line-numbers" data-start="58" data-line-offset="57" data-line="60"><code class="language-jsx"><!--
 const gc = new GeocodingControl({
    limit: 3, // limit result number
    country: "us", // limit resoults to united states
 });
 map.current.addControl(gc);
 --></code></pre>

1. Now the results are only from the USA.

    

1. That removes the other countries from the results, but we still don't get the results for Honolulu first. To fix this we can either set a fixed proximity or specify the center of my map. In the example we're going to use the center of the map.

 <pre class="line-numbers" data-start="58" data-line-offset="57" data-line="61"><code class="language-jsx"><!--
 const gc = new GeocodingControl({
    limit: 3, // limit result number
    country: "us", // limit resoults to united states
    proximity: [{ type: "map-center" }], // resoults closer to map center will be shown first
 });
 map.current.addControl(gc);
 --></code></pre>

1. We now have the results prioritized by proximity to the center of the map, which shows us the results for Honolulu first. Let's refine the search a little further by specifying the type of results we want. In this case, we are only interested in addresses.

    <pre class="line-numbers" data-start="58" data-line-offset="57" data-line="62"><code class="language-jsx"><!--
    const gc = new GeocodingControl({
       limit: 3, // limit result number
       country: "us", // limit resoults to united states
       proximity: [{ type: "map-center" }], // resoults closer to map center will be shown first
       types: ["address"], // limit search types only to adresses
    });
    map.current.addControl(gc);
    --></code></pre>

    

1. Congratulations! You have created a map with a geocoding control to search places. Have a look at the [Geocoding Control API reference](/sdk-js/modules/geocoding/api/api-reference/) to learn more about the control options and events.

    

### Full code to download

We have created a repository with the result of this tutorial that will serve as a basis to build future applications. You can access the repository at [Maps in React](https://github.com/maptiler/maps-in-react/tree/E4-geocoding){:target="\_blank" rel="noopener"}.

## Next episode

Continue to [Episode 5: 3D Map in React js with geocoding control](/react/sdk-js/3d-map/) to learn how to a 3D terrain map in your React JS map using the MapTiler SDK JS.
