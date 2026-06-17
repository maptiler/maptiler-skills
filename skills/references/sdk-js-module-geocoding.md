# Source: https://docs.maptiler.com/sdk-js/modules/geocoding/api/index/

# 

<p id="github-link">
  <span>
    
  <a class="text-secondary mb-2" href="https://www.npmjs.com/package/@maptiler/geocoding-control" target="_blank"
  rel="noopener noreferrer">Get it from npm registry</a><br>
  
  <a class="text-secondary mb-2" href="https://github.com/maptiler/maptiler-geocoding-control" target="_blank"
  rel="noopener noreferrer">View source code on GitHub</a>
  </span> 
</p>

The geocoding control implements a complete [**place search**](/guides/location-services/geocoding-search/) in your map or other frontend application. This page explains how to implement it with [MapTiler SDK JS](/sdk-js/).

<iframe style="height: 400px; width: 100%" src="?key="></iframe>

## Get started

For the most basic integration, see the code example [Add place search to map](/sdk-js/examples/geocoder-component/).

If you're using a JS framework like React or Svelte, get tailored instructions in these tutorials:

- [React component](/react/sdk-js/geocoding-control/)
- [Svelte component](/svelte/sdk-js/geocoding-control/)

You can also go to [GitHub]("https://github.com/maptiler/maptiler-geocoding-control) or [npm](https://www.npmjs.com/package/@maptiler/geocoding-control){:target="\_blank" rel="noopener"} for integration details.

## Configure search

To customize the geocoding control behavior for your needs, see these examples:

- [Limit results by country](/sdk-js/examples/geocoding-filter-country/)
- [Limit results by a bounding box](/sdk-js/examples/geocoding-filter-bbox/)
- [Draw a custom search area](/sdk-js/examples/geocoding-filter-draw-bbox/)
- [Prioritize nearby results](/sdk-js/examples/geocoding-filter-proximity/)
- [Search specific place types](/sdk-js/examples/geocoding-filter-types/)
- [Set search language](/sdk-js/examples/geocoding-language/)

The search control has many more powerful config options, including autocomplete and typing predictions or highlighting search results on the map. Check out the [geocoding control API reference](/sdk-js/modules/geocoding/api/api-reference/#geocoding-parameters) to see all options.

## Advanced topics

The geocoding control can be used as an **ES Module** (ESM) or **UMD** (Universal Module Definition).

### UMD global variables

When importing scripts from CDN using `<script>` tags, the library creates global variables according to this table:

| Script filename                | UMD global variable name                | Exports                                                            |
| ------------------------------ | --------------------------------------- | ------------------------------------------------------------------ |
| `maptilersdk.umd.js`           | `maptilerGeocoder`           | `class GeocodingControl` |
| `leaflet.umd.js`               | `maptilerGeocoder`               | `class GeocodingControl` |
| `maplibregl.umd.js`            | `maptilerGeocoder`            | `class GeocodingControl` |
| `openlayers.umd.js`            | `maptilerGeocoder`            | `class GeocodingControl` |
| `index.umd.js`               | `maptilerGeocoder`                      | `class GeocodingControl` |
{: .table-100 }

The variable is an object with properties representing library-exported variables, for example `maptilerGeocoder.GeocodingControl`.

Alternatively you can use different CDN, for example <code class="language-plaintext">https://www.unpkg.com/@maptiler/geocoding-control@${version}/${Script filename}</code>. Replace <code class="language-plaintext">${version}</code> with the desired library version and <code class="language-plaintext">${Script filename}</code> with the script filename from the table above.

### POI icons and bundlers

POI icons are served from CDN by default. If you need to serve them from a different location when using a web application bundler (Webpack, Vite), you'll need additional configuration.

Icons are bundled in the library at `node_modules/@maptiler/geocoding-control/icons`. You can either:

1. Configure your bundler to handle the icons directory
2. Use the `iconsBaseUrl` configuration option to specify the icon location
3. Copy the icons to your `public` directory

---
