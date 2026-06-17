# Source: https://docs.maptiler.com/guides/on-prem/server/geocoding/

# 

[Geocoding](https://www.maptiler.com/cloud/geocoding/){:target="_blank" rel="noopener"} makes it possible to search your maps. We provide the functionality from our cloud but it's also possible to self-host it, and this page explains how.

The key component of the search functionality is a **geocoding index** – a data structure that stores all searchable locations. At MapTiler, we have professionally maintained geocoding indexes for the whole world, and you can use them via our [online Geocoding API](https://www.maptiler.com/cloud/geocoding/){:target="_blank" rel="noopener"}. To use them on-prem or completely offline, you need to set them up in your self-hosted environment. By doing that, you'll get a [local Geocoding API](/server/api/geocoding/) which works just like the online one, and you can use it to add a **search box** ([geocoding control](/sdk-js/modules/geocoding/)) to your on-prem maps. 

## Before you start

Before you get to the geocoding setup itself, make sure that [MapTiler Server](/guides/self-hosting/map-server/) is installed and you have some maps ready. If you need help with these tasks, follow the 👉 [Getting started with MapTiler Server](/guides/self-hosting/map-server/getting-started/) guide. 

#### Technical requirements

The geocoding service will run smoothly on a hosting machine with the following parameters:

- 2GHz dual-core CPU
- 4+ GB RAM 
- 200+ GB of free HDD space for global geocoding indexes

For complete specs, see the [MapTiler Server technical specification](/guides/self-hosting/map-server/maptiler-server-technical-specification/).

## Set up the endpoint

First, let's set up the [local Geocoding API](/server/api/geocoding/) endpoint. We'll use a sample geocoding index, which is much smaller than full global indexes and thus more suitable for testing. The sample index only works for Switzerland, so you can test it together with the [sample package](/guides/self-hosting/self-hosted-maps/maptiler-data-sample-package/) which contains map data for the Zurich area in Switzerland. 

When you get the <a href="#full-index">full index</a> for the whole world, you can set it up by following the same steps.

1. [**Open this link**](https://data.maptiler.com/my-extracts/?sample){:target="_blank" rel="noopener"} and download the sample **Geocoding index**. It's a `tar.gz` archive file.

2. Go to your MapTiler Server administration Geocoding page `http://localhost:3650/admin/geocoding`.

3. Use the **Import index file** button to upload the `tar.gz` file. Or just drag & drop it onto the page. 

    

MapTiler Server sets up the geocoding index automatically and your local geocoding API is ready.

#### Test the endpoint

The local geocoding API endpoint is available in the `/api/geocoding/` path. You can test it using `wget` or `curl` commands: 

- Save the JSON file to the folder where MapTiler Server is running: 
     ```bash
     wget -o - http://localhost:3650/api/geocoding/zurich.json
     ```
- Print the file contents to standard output: 
     ```bash
     wget -O - http://localhost:3650/api/geocoding/zurich.json
     ```

To test in the browser, go to `http://localhost:3650/api/geocoding/zurich.json`.

## Add search to your map

The on-prem geocoding functionality is completely independent of the on-prem maps. This means that the setup gives you the API endpoint, but doesn't automatically add the search to your local maps. Instead, you get sample code to help you integrate the search control into a self-hosted map application. Here's how.

1. **Select a basemap style:** Use the dropdown menu to pick any of the maps hosted in MapTiler Server. This will be the basemap to show the search box on. The sample code for your map app will contain a link to this map style, which you can simply replace when you want to use a different map.

    

2. **Configure the search:** The geocoding feature and the control (aka search box) has plenty of config options, which you can adjust in the right panel. To learn more about the options, see the tooltips and [Geocoding Control module documentation](/sdk-js/modules/geocoding/).

    

3. **Copy the sample code:** Use the provided sample code to add a search box to your map app. The code updates itself dynamically when you make changes in the config panel, so once you're happy with the settings, the code is ready too. There are two options, both using the [MapTiler SDK JS](/sdk-js/):

    - **NPM module** code to add the geocoding control to your Node.js project. Start by using the first provided code block to install the SDK and geocoding control, then include the second code block in your JavaScript file. 
    - **Basic JavaScript** with complete code for a simple web map application. To use it, copy the code, paste it into a code editor or plain text editor, and save it as a .html file. Test it by opening in your web browser. 

> [!WARNING]
> Remember that if you're using maps with [sample data](/guides/self-hosting/self-hosted-maps/maptiler-data-sample-package/) instead of the [full data](https://www.maptiler.com/data/) and a sample geocoding index instead of the [full index](#full-index), you'll only get a sample map application too – with a clipped map and limited search. Specifically, you'll be only able to search and display places in Zurich, Switzerland.

If you want to use a specific framework or another map library to implement the search box in your map app, you need to modify the code accordingly. We have a complete set of [code examples for various libraries](/sdk-js/modules/geocoding/examples/) using the online Geocoding API, which you can check out and adapt for on-prem use.

#### Offline use

You may notice that the code refers to online stylesheets and scripts from our SDK, meaning it won't work when fully offline. To update it for offline use, you need to download the dependencies and replace URLs in the file header with local paths to the downloaded files. For example, in the basic JavaScript code, you'd replace `<link href="https://cdn.maptiler.com/maptiler-sdk-js/v3.3.0/maptiler-sdk.css" rel="stylesheet">` with `<link href="path/to/maptiler-sdk.css" rel="stylesheet">`, replacing `path/to/` with the relative path to the file in your project directory.

<div class="message info mt-3 mb-5">
  When downloading any dependencies for local use, note the version listed in the sample code and preferably get this exact version. These versions are tested. Different minor versions should work as well but it's not guaranteed, and different major versions are usually not compatible.
</div>

<a name="full-index"></a>

## What's next: Get full index

Once you've tested on-prem geocoding using the sample index limited to Switzerland, you may want to get a full index for the whole world. If your license doesn't include on-prem geocoding, first [contact our Sales team](https://www.maptiler.com/contacts/#contact){:target="_blank" rel="noopener"} to arrange it. The global indexes will be then available on the [Downloads page](https://data.maptiler.com/my-extracts/) in your MapTiler account.



## Useful links

- [Geocoding live demo](https://www.maptiler.com/showcase/geocoding/){:target="_blank" rel="noopener"}
- [Geocoding product page](https://www.maptiler.com/cloud/geocoding/){:target="_blank" rel="noopener"}
- [On-prem geocoding API reference](/server/api/geocoding/)
- [Geocoding control – SDK module documentation](/sdk-js/modules/geocoding/)
- [Geocoding control – code example](/sdk-js/examples/geocoder-component/)
- [NPM geocoding package](https://www.npmjs.com/package/@maptiler/geocoding-control){:target="_blank" rel="noopener"}
