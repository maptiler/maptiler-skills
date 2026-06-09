# Source: https://docs.maptiler.com/sdk-js/index/

# 

<p id="github-link">
  <span>
  
  <a class="text-secondary mb-2" href="https://www.npmjs.com/package/@maptiler/sdk" target="_blank"
  rel="noopener noreferrer">Get it from npm registry</a><br>
  
  <a class="text-secondary mb-2" href="https://github.com/maptiler/maptiler-sdk-js" target="_blank"
  rel="noopener noreferrer">View source code on GitHub</a>
  </span> 
</p>

MapTiler SDK JS is your complete toolkit for building web maps. At its core, it bundles everything needed to render interactive maps in the browser. On top of that, it provides features to make integration of MapTiler [maps](https://www.maptiler.com/maps/) and [API services](/cloud/api/) as easy as possible. It's also open-source so you can check how it handles your data under the hood.

#### Designed for frontend devs

This SDK was built for JavaScript developers who work on map-based web applications. Focus on your app while the SDK handles all the heavy lifting! *If you only need a specific [location service](/guides/location-services/) without a map, using our [APIs](/cloud/api/) directly or via [JS client](/api-clients/) might be a lighter fit.*

#### In-built maps

MapTiler SDK JS comes with built-in [map styles](https://www.maptiler.com/maps/) to pick from, showing detailed street-level information, 3D terrain, and satellite imagery for the entire world. Each map can be displayed in either [flat (Mercator) or globe projection](#projection).

#### Rich data visualization

Your data can be displayed in many ways, from simple maps with markers to dynamic heatmaps and filtered visualizations of millions of features, all using WebGL technology in a browser. There's [hundreds of code examples](/sdk-js/examples) for inspiration.

#### Modules for added functions

The SDK has many modules with pre-built functions, so it's possible to quickly implement search and other geocoding features, show 3D models in the maps, build weather applications, and much more. Check out [all modules](/sdk-js/modules/).

#### Favorable usage tracking

MapTiler SDK JS by default uses the <strong>session-based</strong> model of tracking map usage. To learn more about what this means, how it affects your map traffic billing, and how to change the model if desired, go to <a href="/guides/maps-apis/maps-platform/tile-requests-and-map-sessions-compared/">Map usage: Sessions vs requests.</a> 

#### Open source at heart

The core of MapTiler SDK JS is MapLibre GL JS, an open-source web map library based on WebGL. Our SDK extends MapLibre GL JS with functions related to the MapTiler mapping platform. MapTiler SDK JS itself has [public source code](https://github.com/maptiler/maptiler-sdk-js){:target="_blank" rel="noopener"} and is BSD-licensed.

<div class="row my-4 align-items-center justify-content-center text-center text-md-start">
  <div class="col-sm-12 col-md-4 mt-1">
    <div class="bg-lighter text-center rounded overflow-hidden position-relative">
      <div class="px-2 pt-1">
        <h3 class="mb-1">Examples</h3>
        <p class="mt-1">Browse code examples</p>
        <a class="btn btn-primary my-2 stretched-link text-wrap" href="./examples" role="button">Go to examples
        </a>
      </div>
    </div>
  </div>
  <div class="col-sm-12 col-md-4 mt-1">
    <div class="bg-lighter text-center rounded overflow-hidden position-relative">
      <div class="px-2 pt-1">
        <h3 class="mb-1">Modules</h3>
        <p class="mt-1">Get ready-to-use functions</p>
        <a class="btn btn-primary my-2 stretched-link text-wrap" href="./modules" role="button">Go to modules
        </a>
      </div>
    </div>
  </div>
  <div class="col-sm-12 col-md-4 mt-1">
    <div class="bg-lighter text-center rounded overflow-hidden position-relative">
      <div class="px-2 pt-1">
        <h3 class="mb-1">Reference</h3>
        <p class="mt-1">Read full SDK JS reference</p>
        <a class="btn btn-primary my-2 stretched-link text-wrap" href="./api" role="button">Go to reference
        </a>
      </div>
    </div>
  </div>
</div>

## Get started

To integrate a map using MapTiler SDK JS, simply use the code below the map. 

For a more detailed tutorial on how to initialize a map and load the style, see [Learn the basics – How to use the MapTiler SDK JS](./examples/how-to-use/).

<iframe style="height: 400px; width: 100%" src="?key="></iframe>



<a name="projection"></a>

## Map projection

The **Web Mercator projection** has been the go-to standard in cartography since the early days of web mapping. It is great for navigation and shows the entire world in one screen, with no hidden face. However, Mercator's heavy distortion at high latitudes and discontinuity at the poles can be a limitation for data visualization. There's been also criticism of providing a biased view of the world. Learn more about Mercator projection on [*Wikipedia*](https://en.wikipedia.org/wiki/Web_Mercator_projection).

The **globe projection**, available from MapTiler SDK v3, does not suffer from these biases and can feel overall more playfull than Mercator. It's a great choice for semi-global data visualization, especially for data close to the poles, thanks to its geographic continuity.

To learn how to set the projection in your map using SDK JS, see the related [projection examples](/sdk-js/examples/?q=projection).

| Mercator projection    | Globe projection |
| :--------: | :-------: |
|  |  |
