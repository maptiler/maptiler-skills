# Source: https://docs.maptiler.com/guides/on-prem/server/getting-started/

# 

The quickest way to explore [MapTiler Server](/guides/self-hosting/map-server/) and the essential first step for any setup is to deploy our **free sample maps package**. This is the primary way to obtain our professional map styles (designs) together with sample data to test them out. Whether you are starting a trial to evaluate the platform or preparing a full production environment, this package provides the styling foundation needed to make any additional map data work.

At the end of this guide, you'll have:

- A fully functional *local Maps API* running on your machine.
- Our professional *map styles*, ready for importing more data to show the world.
- *Sample map data* for Zurich (Switzerland) to preview the map styles immediately.
- An *application example* with instructions to quickly test the local API.

## Prerequisites

MapTiler Server [installed and running](/guides/on-prem/server/installation/).

## Deploy the map package

1. [Open this link](https://data.maptiler.com/my-extracts/?sample){:target="_blank" rel="noopener"} and download the **map package**. Note that the download may take some time due to the package size.

2. Open the MapTiler Server admin interface, by default at [http://localhost:3650/admin](http://localhost:3650/admin){:target="_blank" rel="noopener"}.

3. Use the **New map** button to upload the zipped map package. Alternatively, drag and drop it onto the page.



The upload automatically populates your MapTiler Server:

- The **Datasets** section now contains the raw data for your maps. The data included in the starter package is intended for testing, and only covers the Zurich region in Switzerland.
- The **Maps** section lists the map styles (designs). The package provides you with a selection of [our maps](https://www.maptiler.com/maps/){:target="_blank" rel="noopener"} for various purposes to get you started.

[Learn more about data, map styles, and how they relate.](/guides/how-maps-work/)

<div class='border rounded-3 my-1 accordion-item' id='sample-package#contents' aria-expanded='false'>
  <div class='bg-lighter rounded-3'>
    <a role='button' data-bs-toggle='collapse' data-bs-target='#contents' aria-expanded='false' aria-controls='contents' class='collapsed'>
      <span class='px-2 py-1 h6 text-secondary d-block m-0'>What's inside the current package (v3.15)?
        <span class='float-end collapse-arrow'>
          <svg version='1.1' xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'><use href='/styles/style/icon/icon.svg#keyboard_arrow_down'></use></svg>
        </span>
      </span>
    </a>
  </div>
  <div id='contents' class='collapse' aria-labelledby='contents' data-parent='#accordion'>
    <div class='card-body px-2'>
      <span>
        <p>The sample package contains a complete set of components (map styles, data, and offline fonts) for a map self-hosting demo. In its latest version, you get these maps:</p>
          <ul>
            <li><a href="https://www.maptiler.com/maps/#style=streets" target="_blank">Streets</a></li>
            <li><a href="https://www.maptiler.com/maps/#style=satellite" target="_blank">Satellite</a></li>
            <li><a href="https://www.maptiler.com/maps/#style=basic" target="_blank">Basic</a></li>
            <li><a href="https://www.maptiler.com/maps/#style=outdoor" target="_blank">Outdoor</a></li>
            <li><a href="https://www.maptiler.com/maps/#style=dataviz" target="_blank">Dataviz</a></li>
          </ul>
        <p>Each map (except Satellite) is available either as a <strong>MapTiler Planet</strong> version, which pulls the map data from our professionally maintained <a href="https://maptiler.com/planet/" target="_blank">MapTiler Planet</a> dataset, or as an <strong>OpenStreetMap</strong> version which uses the open-source <a href="https://www.openstreetmap.org/about" target="_blank">OSM data</a>.</p>
        <p><strong>Satellite</strong> is a <a href="/guides/self-hosting/map-server/virtual-tileset-json-for-seamless-blending-of-drone-aerial-and-satellite-imagery">virtual tileset</a> which combines several regular datasets into one.</p>
        <p>For a complete list and description of the maps, datasets, and offline fonts you get with this package, please refer to the <code>README</code> file included in the ZIP file.</p>
      </span>
    </div>
  </div>
</div>

## Preview and test the maps {#testMaps}

With the maps uploaded, let's see how to display them to their audience. Note that the following examples will only work on your computer and *can't be used to test remote access* to the self-hosted maps. The goal here is to give you an idea of presentation options and let you explore the maps. 

<div class="message warning mt-3 mb-5">
  Remember that the sample package only contains map data for Zurich, which means that the maps get clipped when you zoom out of the Zurich area. This won't happen once you use <a href="https://www.maptiler.com/data/" target="_blank">professional map data</a> available with our paid plans.
</div>

### Check public preview

The map upload makes the demo maps available not only in the [administration interface](http://localhost:3650/admin/){:target="_blank" rel="noopener"}, but also on the [public preview](http://localhost:3650/){:target="_blank" rel="noopener"}. Visit it to see the maps presentation to a non-admin user. This is a simple way to quickly explore the self-hosted map styles.

### Test an API endpoint

1. In the **Maps** section, choose one of the listed maps and use the **Detail** button next to it. This takes you to a page with the map preview and a list of prepared API calls for various uses.
2. Use the **View fullscreen** button below the map. This opens a new tab in your web browser and displays the simplest fullscreen view of the map. The URL in the address bar corresponds to the API request that loaded the map view.

### Test a simple web app

Follow the steps below to see how you can combine your self-hosted map with custom data. You can also [watch it on video](https://vimeo.com/1080820909/2178b2e8f1){:target="_blank" rel="noopener"}.

1. Copy the following code and save it as a HTML file on your computer. 

    <div class='border rounded-3 my-1 accordion-item' id='sample-package#example' aria-expanded='false'>
      <div class='bg-lighter rounded-3'>
      <a role='button' data-bs-toggle='collapse' data-bs-target='#example' aria-expanded='false' aria-controls='example' class='collapsed'>
      <span class='px-2 py-1 h6 text-secondary d-block m-0'>Web app example code
      <span class='float-end collapse-arrow'>
      <svg version='1.1' xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'><use href='/styles/style/icon/icon.svg#keyboard_arrow_down'></use></svg>
      </span>
      </span>
      </a>
      </div>
      <div id='example' class='collapse' aria-labelledby='example' data-parent='#accordion'>
      <div class='card-body px-2'>
      <pre data-src="./example/index.html"></pre>
      </div>
      </div>
    </div>

2. Open the file in your web browser. What you see is your self-hosted **Dataviz** map displayed using [MapTiler SDK](/sdk-js/), with additional data on top of it. The additional data is pulled from [this file](/sdk-js/assets/zurich-hotels.geojson){:target="_blank" rel="noopener"} which lists hotels in Zurich. They're shown on the map as blue dots.

     
     
3. Open the file in a code editor and find this line:
   
     `style: "http://localhost:3650/api/maps/dataviz/style.json",`

     It refers to the **Dataviz** map style. Replace `dataviz` with another map style hosted in your MapTiler Server, for example `streets`, and reload the browser view to see the hotels data layer on a different map.

## Next steps {#nextSteps}

With the sample maps running, here's what to do next:

- **Mind the license.** The free version you've just deployed is for trial or non-commercial use only. Before you proceed to live production setup, make sure to check out the [features and pricing](https://www.maptiler.com/data/pricing/){:target="_blank" rel="noopener"} of the commercial version of MapTiler Server and data. 

- **Get more map data.** The maps (styles) in the sample package are fully functional out-of-the-box, but they won't show the whole world because the sample package only contains data for the Zurich region. To make your self-hosted maps work correctly in other areas as well, you'll need <a href="https://www.maptiler.com/data/" target="_blank">additional datasets</a>. We offer detail-rich, professionally maintained datasets as well as free OpenStreetMap data.

- **Build your map app.** Explore our [SDK JS](/sdk-js/), particularly the [code examples](/sdk-js/examples/), to see how you can build a browser-based application with your on-prem maps. Also, check how you can implement [on-prem map search](/guides/geocoding/on-premise-geocoding-in-maptiler-server/) that can work completely offline.


