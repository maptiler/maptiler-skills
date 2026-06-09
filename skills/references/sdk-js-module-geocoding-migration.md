# Source: https://docs.maptiler.com/sdk-js/modules/geocoding/api/migration/

# Geocoding control migration guide

**Version 3** of the Geocoding control **removes** the dependency on **Svelte**, so it's no longer required to have Svelte installed to use it. It also introduces a new integration approach: the control no longer uses the previous map controller. Instead, each map library **provides its own standalone, self-contained control**, which you use in the same way as any other control from that library.

Version 3 also **includes a standalone geocoder component** implemented as a **standard Web Component**, which you can integrate with any frontend framework or library using its usual integration method.

This page explains how to migrate from version 2 to version 3 of the Geocoding control.

## Imports and entrypoints

### Root entrypoint

The package now **includes a root entry point**: `@maptiler/geocoding-control`.

Importing this entry point without specifying any symbol registers a Web Component named `maptiler-geocoder`.

```js
import "@maptiler/geocoding-control";
```

```html
<maptiler-geocoder class="first" apiKey="YOUR_MAPTILER_API_KEY_HERE"></maptiler-geocoder>
```

Use this component as a standalone geocoder in any environment as a custom solution.

If you use a map library, import the entry point for that specific library instead. See [MapTiler SDK entrypoint](#maptiler-sdk-entrypoint),

```js
import "@maptiler/geocoding-control";
import { type MaptilerGeocoderOptions, type MaptilerGeocoderEvent } from "@maptiler/geocoding-control";
```

#### Importing from CDN

The name of the UMD file has changed from `vanilla.umd.js` to `index.umd.js`

```html

```

### MapTiler SDK entrypoint

The entry point remains `@maptiler/geocoding-control/maptilersdk`.

This entry point no longer exports a function for creating a map controller. Instead, import `GeocodingControl` and add it to the map instance like any other map control.

```js
import { GeocodingControl, type GeocodingControlOptions, type GeocodingControlEvent } from "@maptiler/geocoding-control/maptilersdk";

map.addControl(new GeocodingControl());
```

#### Importing from CDN

The name of the global UMD variable has changed from `maptilersdkMaptilerGeocoder` to `maptilerGeocoder`

<pre><code class="language-diff diff-highlight"><!--
- const gc = new maptilersdkMaptilerGeocoder.GeocodingControl();
+ const gc = new maptilerGeocoder.GeocodingControl();
--></code></pre>

### MapLibre GL entrypoint

The entry point remains `@maptiler/geocoding-control/maplibregl`.

This entry point no longer exports a function for creating a map controller. Instead, import `GeocodingControl` and add it to the map instance like any other map control.

```js
import { GeocodingControl, type GeocodingControlOptions, type GeocodingControlEvent } from "@maptiler/geocoding-control/maplibregl";

map.addControl(new GeocodingControl());
```

#### Importing from CDN

The name of the global UMD variable has changed from `maplibreglMaptilerGeocoder` to `maptilerGeocoder`

<pre><code class="language-diff diff-highlight"><!--
- const gc = new maplibreglMaptilerGeocoder.GeocodingControl();
+ const gc = new maptilerGeocoder.GeocodingControl();
--></code></pre>

### Leaflet entrypoint

The entry point remains `@maptiler/geocoding-control/leaflet`.

This entry point no longer exports a function for creating a map controller. Instead, import `GeocodingControl` and add it to the map instance like any other map control.

```js
import { GeocodingControl, type GeocodingControlOptions, type GeocodingControlEvent } from "@maptiler/geocoding-control/leaflet";

map.addControl(new GeocodingControl());
```

#### Importing from CDN

The name of the global UMD variable has changed from `leafletMaptilerGeocoder` to `maptilerGeocoder`

<pre><code class="language-diff diff-highlight"><!--
- L.control.maptilerGeocoding({ apiKey: key }).addTo(map);
+ const gc = new maptilerGeocoder.GeocodingControl({ apiKey: key });
+ map.addControl(gc);
--></code></pre>

### OpenLayers entrypoint

The entry point remains `@maptiler/geocoding-control/openlayers`.

This entry point no longer exports a function for creating a map controller. Instead, import `GeocodingControl` and add it to the map instance like any other map control.

```js
import { GeocodingControl, type GeocodingControlOptions, type GeocodingControlEvent } from "@maptiler/geocoding-control/openlayers";

map.addControl(new GeocodingControl());
```

#### Importing from CDN

The name of the global UMD variable has changed from `openlayersMaptilerGeocoder` to `maptilerGeocoder`

<pre><code class="language-diff diff-highlight"><!--
- const gc = new openlayersMaptilerGeocoder.GeocodingControl({ apiKey: key });
+ const gc = new maptilerGeocoder.GeocodingControl({ apiKey: key });
--></code></pre>

### Common types entrypoint

The entry point `@maptiler/geocoding-control/types` **no longer exists**.

Import common types shared across modules from the root entry point `@maptiler/geocoding-control` or from any library entry point, such as `@maptiler/geocoding-control/maptilersdk`.

Types that belong to a specific map control, such as `GeocodingControlOptions`, are available only from the entry point of that library. Each library can define slightly different types depending on its features and requirements.

```js
import type { Feature, Position } from "@maptiler/geocoding-control";
import type { Feature, Position } from "@maptiler/geocoding-control/maptilersdk";
```

### Svelte entrypoints

Svelte entrypoints **no longer exist**.

The Geocoding control doesn't use Svelte anymore. To use the control in Svelte with a map library, treat it the same way you treat any other map control.

```js
import { GeocodingControl } from "@maptiler/geocoding-control/maptilersdk";

...
...

let geocoderControl;

...
...

geocoderControl = new GeocodingControl();
geocoderControl.on("select", (data) => {
  console.log("select", data);
});
map.addControl(geocoderControl);

```

To use a standalone geocoder, treat it the same way you treat any other webcomponent.

#### Geocoding control version 2 ⚠️ deprecated

```js
import GeocodingControl from "@maptiler/geocoding-control/svelte/GeocodingControl.svelte";
import { createMapLibreGlMapController } from "@maptiler/geocoding-control/maplibregl";

...
...

let mapController;

...
...

mapController = createMapLibreGlMapController(map, maptilersdk);
```

```html
<div class="geocoding">
  <GeocodingControl {mapController} {apiKey} {maptilersdk} />
</div>
```

### React entrypoint

React entrypoint **no longer exists**.

To use the control in React with a map library, use it the same way as any other map control.

```js
import { GeocodingControl } from "@maptiler/geocoding-control/maptilersdk";

...
...

const control = useRef<GeocodingControl>(null);

...
...

control.current = new GeocodingControl();
control.current.on("select", (data) => {
  log("select", data);
});
map.current.addControl(control.current);
```

To use a standalone geocoder, treat it the same way you treat any other webcomponent. A common approach uses `useRef`.

#### Geocoding control version 2 ⚠️ deprecated

```js
import { GeocodingControl } from "@maptiler/geocoding-control/react";
import { createMapLibreGlMapController } from "@maptiler/geocoding-control/maplibregl-controller";

...
...

const [mapController, setMapController] = useState();

...
...

setMapController(createMapLibreGlMapController(map.current, maptilersdk));
```

```html
<div className="geocoding">
  {mapController && <GeocodingControl apiKey={maptilersdk.config.apiKey} mapController={mapController} />}
</div>
```

### Vanilla entrypoint

Vanilla entrypoint **no longer exists**.

See the [root entrypoint](#root-entrypoint) for using standalone geocoder in Vanilla JavaScript and without any map library. See the library entrypoints for using the geocoding control in Vanilla JavaScript together with a map library.

### Style entrypoint

Style entrypoint **no longer exists**.

The package bundles all required styles inside the Web Component, so you don't need to import any CSS.

Future releases may introduce additional customization and styling options.

#### Importing from CDN

The geocoder component **no longer provides a CSS** and doesn't require loading it.

<pre><code class="language-diff-html diff-highlight"><!--
- <link href="https://cdn.maptiler.com/maptiler-geocoding-control//style.css" rel="stylesheet">
--></code></pre>

## Events

Version 3 renames several events and modifies some behaviors.

### New events

- `featuresclear` The control fires this event when it clears features. For map controls, it fires after the control removes features from the map.
- `featuresshow` The control fires this event when it shows the dropdown with search results.
- `featureshide` The control fires this event when it hides the dropdown with search results.
- `request` The control fires this event before sending a request. It complements the existing `response` event.
- `queryclear` The control fires this event when the user clears the input field.
- `focusin` The control fires this event when the input gains focus.
- `focusout` The control fires this event when the input loses focus.
- `markerclick` The control fires this event when the user clicks a marker on the map.
- `markermouseenter` The control fires this event when the user moves the cursor over a marker on the map.
- `markermouseleave` The control fires this event when the user moves the cursor away from a marker on the map.

> Note: Marker events are available only for map controls.

### Modified events

- `featureslisted` The control fires this event when it loads search results. For map controls, it fires after the control renders features on the map. It no longer fires when the control removes features; use `featuresclear` instead.
- `pick` The control can fire this event twice when rendering full geometry. The first event contains simplified geometry, and the second contains full geometry.
- `querychange` The control fires this event when the user changes the input. It no longer fires when the user clears the input; use `queryclear` instead.

### Deleted events

- `featuresmarked` no longer exists. Use `featureslisted` instead.
- `optionsvisibilitychange` no longer exists. Use `featuresshow` and `featureshide` instead.

The following events remain unchanged: `response`, `select`, and `reversetoggle`.

Event types now use `CustomEvent` for the Web Component and the corresponding event type from each map library for map controls. As a result, the event type differs slightly depending on the control variant.

You can import events individually. Example: `ResponseEvent`.

You can also import all events through the `GeocodingControlEvent` namespace. Example: `GeocodingControlEvent.ResponseEvent`.

`GeocodingControlEvent` also represents the union type of all event types.

## Options

- `adjustUrlQuery(sp: URLSearchParams)` has replaced with `adjustUrl(url: URL)`. The control exposes the full `URL` object for modification after it prepares the request and before it sends it.
- `session` is now available in the MapTiler SDK control. It behaves the same as the `session` configuration option in the MapTiler SDK.


