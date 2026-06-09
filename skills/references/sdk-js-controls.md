# Source: https://docs.maptiler.com/sdk-js/api/controls/


# Controls

The term "control" is commonly used for all sorts of buttons and information display that take place in one of the corner of the map area. The most well know are probably the `[+]` and `[-]` zoom buttons as well as the attribution information.

User interface elements that can be added to the map. The items in this section exist outside of the map's `canvas` element.

<!-- Easy to add controls -->
## Easy to add controls 

The easiest way to add the most used controls is through the [Map constructor options](/sdk-js/api/map/#map-options).

To add a control in the map constructor, you must indicate the name of the control and one of these values: `true` to add the control or `false` to hide the control. You can also indicate in which position we are going to add the control: `top-left`, `top-right`, `bottom-left`, `bottom-right`.

### Example

```js
const map = new maptilersdk.Map({
  container: document.getElementById("my-container-div"),
  terrainControl: true,
  scaleControl: true,
  fullscreenControl: "top-left",
  geolocateControl: false
})
```

These are the controls that are directly accessible in the map constructor:

- `navigationControl`: Shows the `[+]`, `[-]` zoom buttons and tilt/bearing/compass buttons. Showing on the `top-right` by default.
- `geolocateControl`: Shows a arrow-shaped locate button. When clicked, it adds a marker and center the map. If clicked again, the marker disapears (unless the map was moved since first clicked). Showing on the `top-right` by default.
- `terrainControl`: Shows a button to enable/disable the 3D terrain (does not tilt the map). Hidden by default, showing on the `top-right` if true.
- `scaleControl`: Shows a distance scale. The unit ("metric", "imperial" or "nautical") can be set in the [config object](/sdk-js/api/config/) config.unit (default: "metric"). Hidden by default, showing on the `bottom-right` if true.
- `fullscreenControl`: Shows a button that toggles the map into fullscreen. Hidden by default, showing on the `top-right` if true.


<!-- Custom controls -->
## Custom controls 

MapTiler SDK JS supports two flexible ways to add custom controls to your map interface, depending on the level of control and flexibility you need.

### Related examples

- [How to add a custom control programmatically](/sdk-js/examples/custom-controls-programmatic/)
- [Add a custom control declarative way](/sdk-js/examples/custom-controls-declarative/)

### Programmatic Controls

Programmatic controls allow developers to have more control and register custom control elements manually by calling `map.addControl()` and providing a control implementation. This method is ideal for applications that require dynamic logic, event-based behaviour, or a deeper integration with a framework like React.

Custom controls are instantiated using the [`MaptilerCustomControl`](#maptilercustomcontrol) class. The element that should be used can be provided either as the **element itself**, or as its **CSS selector**. Optionally, two callback functions can be provided:

- `onClick` function that is called when the element is clicked, and
- `onRender` function that is called every time the map renders a new state.

Both callbacks receive the active `Map` instance, the associated control element itself, and an event object associated with the original event (`PointerEvent` and `MapLibreEvent` respectively).

#### Example

```js
const panControl = new maptilersdk.MaptilerCustomControl(
  ".pan-control",
  (map) => map.panBy([10, 10]), // Move southeast when clicked
  (map, el) => el.classList.toggle( // Change class based on current hemisphere
    "northern-hemisphere", map.getCenter().lat > 0
  )
);
map.addControl(panControl);

const element = document.createElement("button");
element.className = "btn btn-primary pan-nw"
element.textContent = "Pan NW";

map.addControl(
  new maptilersdk.MaptilerCustomControl(
    element,
    (map) => map.panBy([-10, -10]) // Move northwest when clicked
  ),
  "top-left"
);
```

Example: [How to add a custom control programmatically](/sdk-js/examples/custom-controls-programmatic/)

#### Behaviour Overview

- Upon adding, the control element is removed from its original DOM position and inserted into the map UI.
- The `onClick` callback binds an action to user interaction.
- The `onRender` callback can be used for state-based updates, styling, or other custom logic.
- The control is treated as a native part of the map UI but maintains its own DOM context.
- Upon removing, the control element is moved back into its original DOM position (if any) to not interfere with DOM handling of frameworks like React.

### Declarative Controls

Declarative controls offer a simple way to add interactive UI elements to the map by using HTML attributes alone. Instead of instantiating controls through JavaScript, developers annotate DOM elements and allow the SDK to discover and wire them automatically.

Declarative controls are instantiated under the hood using the [`MaptilerExternalControl`](#maptilerexternalcontrol) class.

#### Example

[Add a custom control declarative way](/sdk-js/examples/custom-controls-declarative/)

#### Enabling Detection

To activate declarative control detection:

- Set the `customControls` option to `true` in the map initialization configuration, to enable detection globally.
- Alternatively, `customControls` may be set to a **CSS selector string**, to scope the autodetection to:
  - Elements matching the selector directly
  - Or elements whose **ancestor** matches the selector

```js
const map = new maptilersdk.Map({
  container: "map",
  customControls: true, // or ".custom-ui"
});  
```

#### Declaring a Control

To declare a control element, use the `data-maptiler-control` attribute:

```html
<button data-maptiler-control="zoom-in">+</button> 
```

The attribute’s value must be one of the predefined keywords, or an empty value. The element is automatically registered as a control and moved into the map UI. Supported values:

| Value | Description |
|---|---|
| `zoom-in` | zooms the map in |
| `zoom-out` | zooms the map out |
| `toggle-projection` | toggles between Mercator and Globe projections |
| `toggle-terrain` | turns Terrain layer on and off |
| `reset-view` | resets bearing, pitch, and roll to 0 (heading north, no pitch, no roll) |
| `reset-bearing` | resets bearing to 0 (heading north) |
| `reset-pitch` | resets pitch to 0 (no pitch) |
| `reset-roll` | resets roll to 0 (no roll) |
| *empty value* | registers the element as control but does not add any functionality automatically |

> [!WARNING]
> An Error is thrown when an unrecognized value is used.

#### Grouping Controls

For grouping related controls together, use the `data-maptiler-control-group` attribute. This approach is ideal for styling multiple buttons as a single floating UI block.

```html
<div data-maptiler-control-group>
  <button data-maptiler-control="zoom-in">+</button>
  <button data-maptiler-control="zoom-out">−</button>
</div> 
```

- The **group container** (`data-maptiler-control-group`) is registered as a control and moved into the map UI.
- It does **not** receive any automatic functionality.
- Functional behaviour is attached to valid descendant elements with `data-maptiler-control`.

#### Positioning Controls

To set a specific position for a control or group, use the `data-maptiler-position`. The allowed values are the same as in [addControl](/sdk-js/api/map/#map#addcontrol) method.

```html
<button data-maptiler-control="reset-view" data-maptiler-position="top-left">↻</button>
<div data-maptiler-control-group data-maptiler-position="bottom-right">
  <button data-maptiler-control="zoom-in">+</button>
  <button data-maptiler-control="zoom-out">−</button>
</div> 
```

#### State Styling via CSS

To support dynamic styling based on map state (without relying on JavaScript), custom CSS variables are set directly on the map container when declarative controls are enabled. Available CSS properties:

| Property | Description | Data type |
|---|---|---|
| `--maptiler-center-lng` | Longitude of map center | unitless number |
| `--maptiler-center-lat` | Latitude of map center | unitless number |
| `--maptiler-zoom` | Current zoom level | unitless number |
| `--maptiler-bearing` | Current map bearing (rotation) | unitless number |
| `--maptiler-pitch` | Pitch angle | unitless number |
| `--maptiler-roll` | Roll angle | unitless number |
| `--maptiler-is-globe-projection` | `true` if globe view is enabled, `false` otherwise | string |
| `--maptiler-has-terrain` | `true` if terrain is active, `false` otherwise | string |

This enables responsive UI tweaks via pure CSS, for example:

```css
/* transform compass icon based on bearing and pitch */
.compass-icon {
  transform: rotateX(calc(var(--maptiler-pitch) * 1deg))
            rotateZ(calc(var(--maptiler-bearing) * -1deg));
}

/* change projection button icon when Globe projection is on */
@container style(--maptiler-is-globe-projection: true) {
  .projection-icon {
    content: "globe";
  }
}
```


<!-- MaptilerNavigationControl -->
## MaptilerNavigationControl 

<p class="github-link"><a class="text-secondary mb-2 ms-1"
      href="https://github.com/maplibre/maplibre-gl-js/tree/4.7.1/src/ui/control/globe_control.ts"
      target="_blank" rel="noopener noreferrer">src/ui/control/globe_control.ts</a></p>

A `MaptilerNavigationControl` control contains zoom buttons and a compass.

Behavior changes:
- When enabled, the pitch button is always present.
- The pitch button now pitches the map if it was not (and as before, unpitches the map if pitched).
- The compass icon on the pitch button has a capped “squeeziness” factor to prevent it from looking extra flat and wide when pitch is set higher than 60.

### Example

```js
const nav = new maptilersdk.MaptilerNavigationControl();
map.addControl(nav, 'top-left');
```

### Parameters

**options** (`Object?`)


| options.showCompassBoolean                  default: true | If true the compass button is included. |
| --- | --- |
| options.showZoomBoolean                  default: true | If true the zoom-in and zoom-out buttons are included. |
| options.visualizePitchBoolean                  default: false | If true the pitch is visualized by rotating X-axis of compass. |



### Related examples

- [Display map navigation controls](/sdk-js/examples/navigation/)
- [Add a third party vector tile source](/sdk-js/examples/third-party/)


<!-- MaptilerGeolocateControl -->
## MaptilerGeolocateControl 

<p class="github-link"><a class="text-secondary mb-2 ms-1"
      href="https://github.com/maptiler/maptiler-sdk-js/blob/main/src/controls/MaptilerGeolocateControl.ts"
      target="_blank" rel="noopener noreferrer">src/MaptilerGeolocateControl.ts</a></p>

A `MaptilerGeolocateControl` control provides a button that uses the browser's geolocation API to locate the user on the map.

Not all browsers support geolocation, and some users may disable the feature. Geolocation support for modern browsers including Chrome requires sites to be served over HTTPS. If geolocation support is not available, the `MaptilerGeolocateControl` will show as disabled.

The zoom level applied will depend on the accuracy of the geolocation provided by the device.

The `MaptilerGeolocateControl` has two modes. If `trackUserLocation` is `false` (default) the control acts as a button, which when pressed will set the map's camera to target the user location. If the user moves, the map won't update. This is most suited for the desktop. If `trackUserLocation` is `true` the control acts as a toggle button that when active the user's location is actively monitored for changes. In this mode the `MaptilerGeolocateControl` has three interaction states:

- **active** - the map's camera automatically updates as the user's location changes, keeping the location dot in the center. Initial state and upon clicking the `MaptilerGeolocateControl` button.
- **passive** - the user's location dot automatically updates, but the map's camera does not. Occurs upon the user initiating a map movement.
- **disabled** - occurs if Geolocation is not available, disabled or denied.

These interaction states can't be controlled programmatically, rather they are set based on user interactions.

Behavior changes:
- Now with these defaults:
  - `enableHighAccuracy`: true (uses browser location, probably GPS)
  - `maximumAge`: 0 (not using any cached location)
  - `Timeout`: 6000 (6 seconds)
  - `trackUserLocation`: true
- When geolocate is “active”, zooming/rotating/pitching the map no longer changes the status to “background” because it does not change the center of the map. The center of the map must move of at least 1 m (world) from the active locked position in order for the status to change to “background” (note: the “background” status means the location is still refreshed but if the user moves, the map will no longer continue to be centered on them).
- The method to update the blue disc (location precision radius) has been improved as we zoom in. It is now less shaky and behave according to perspective when the camera is tilted.

Extends [Evented](/sdk-js/api/events/#evented).

### Example

```js
map.addControl(new maptilersdk.MaptilerGeolocateControl({
  positionOptions: {
      enableHighAccuracy: true
  },
  trackUserLocation: true
}), 'top-left');
```

### Parameters

**options** (`Object?`)


| options.positionOptionsObject                  default: {enableHighAccuracy:false,timeout:6000} | A Geolocation API PositionOptions object. |
| --- | --- |
| options.fitBoundsOptionsObject                  default: {maxZoom:15} | A Map#fitBounds options object to use when the map is panned and zoomed to the user's location. The default is to use a maxZoom of 15 to limit how far the map will zoom in for very accurate locations. |
| options.trackUserLocationObject                  default: false | If true the Geolocate Control becomes a toggle button and when active the map will receive updates to the user's location as it changes. |
| options.showAccuracyCircleObject                  default: true | By default, if showUserLocation is true, a transparent circle will be drawn around the user location indicating the accuracy (95% confidence level) of the user's location. Set to false to disable. Always disabled when showUserLocation is false. |
| options.showUserLocationObject                  default: true | By default a dot will be shown on the map at the user's location. Set to false to disable. |



### Methods

<div class="border rounded-3 my-1 accordion-item" id="geolocatecontrol#trigger" aria-expanded="false">
  <div class="bg-lighter rounded-3"><a role="button" data-bs-toggle="collapse" data-bs-target="#trigger" aria-expanded="false" aria-controls="addcontrol" class="collapsed"><span class="px-2 py-1 h6 text-secondary d-block m-0">trigger<span class="text-dark">()</span><span class="float-end collapse-arrow"> <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><use href="/styles/style/icon/icon.svg#keyboard_arrow_down"></use></svg></span></span></a></div>
  <div id="trigger" class="collapse" aria-labelledby="addcontrol" data-parent="#accordion">
    <div class="card-body px-2"><span>
        <p>Programmatically request and move the map to the user's location.</p>
      </span>
      <h5 id="trigger-returns" class="fs-6"><a class="text-dark mb-1 fw-bold" href="#trigger-returns">Returns</a></h5>
      <code class="language-plaintext"><span><a href="https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean">boolean</a></span></code><span>: Returns <code>false</code> if called before control was added to a map, otherwise returns <code>true</code>.</span>
      <h5 id="trigger-example" class="fs-6"><a class="text-dark mb-1 fw-bold" href="#trigger-example">Example</a></h5>
      <div class="mb-1 api-example">
        <pre><code class="language-js">
// Initialize the geolocate control.
const geolocate = new maptilersdk.GeolocateControl({
  positionOptions: {
    enableHighAccuracy: true
  },
  trackUserLocation: true
});
// Add the control to the map.
map.addControl(geolocate);
map.on('load', function() {
  geolocate.trigger();
});
        </code></pre>
      </div>
    </div>
  </div>
</div>

### Events

<div class="border rounded-3 my-1 accordion-item" id="geolocatecontrol.event:error" aria-expanded="false">
  <div class="bg-lighter rounded-3"><a role="button" data-bs-toggle="collapse" data-bs-target="#error" aria-expanded="false" aria-controls="addcontrol" class="collapsed"><span class="px-2 py-1 h6 text-secondary d-block m-0">error<span class="float-end collapse-arrow"> <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><use href="/styles/style/icon/icon.svg#keyboard_arrow_down"></use></svg></span></span></a></div>
  <div id="error" class="collapse" aria-labelledby="addcontrol" data-parent="#accordion">
    <div class="card-body px-2"><span>
        <p>Fired on each Geolocation API position update which returned as an error.</p>
      </span>
      <h5 id="error-properties" class="fs-6"><a class="text-dark mb-1 fw-bold" href="#error-properties">Properties</a></h5>
      <div class="mb-1"><span class="fw-bolder me-1">data</span><code class="language-plaintext">(<span><a href="https://developer.mozilla.org/docs/Web/API/PositionError">PositionError</a></span>)</code><span>: The returned <a href="https://developer.mozilla.org/en-US/docs/Web/API/PositionError">PositionError</a> object from the callback in <a href="https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition">Geolocation.getCurrentPosition()</a> or <a href="https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition">Geolocation.watchPosition()</a>.</span></div>
      <h5 id="error-example" class="fs-6"><a class="text-dark mb-1 fw-bold" href="#error-example">Example</a></h5>
      <div class="mb-1 api-example">
        <pre><code class="language-js">
// Initialize the geolocate control.
const geolocate = new maptilersdk.GeolocateControl({
  positionOptions: {
      enableHighAccuracy: true
  },
  trackUserLocation: true
});
// Add the control to the map.
map.addControl(geolocate);
// Set an event listener that fires
// when an error event occurs.
geolocate.on('error', function() {
  console.log('An error event has occurred.')
});
        </code></pre>
      </div>
    </div>
  </div>
</div>

<div class="border rounded-3 my-1 accordion-item" id="geolocatecontrol.event:geolocate" aria-expanded="false">
  <div class="bg-lighter rounded-3"><a role="button" data-bs-toggle="collapse" data-bs-target="#geolocate" aria-expanded="false" aria-controls="addcontrol" class="collapsed"><span class="px-2 py-1 h6 text-secondary d-block m-0">geolocate<span class="float-end collapse-arrow"> <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><use href="/styles/style/icon/icon.svg#keyboard_arrow_down"></use></svg></span></span></a></div>
  <div id="geolocate" class="collapse" aria-labelledby="addcontrol" data-parent="#accordion">
    <div class="card-body px-2"><span>
        <p>Fired on each Geolocation API position update which returned as success.</p>
      </span>
      <h5 id="geolocate-properties" class="fs-6"><a class="text-dark mb-1 fw-bold" href="#geolocate-properties">Properties</a></h5>
      <div class="mb-1"><span class="fw-bolder me-1">data</span><code class="language-plaintext">(<span><a href="https://developer.mozilla.org/docs/Web/API/Position">Position</a></span>)</code><span>: The returned <a href="https://developer.mozilla.org/en-US/docs/Web/API/Position">Position</a> object from the callback in <a href="https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition">Geolocation.getCurrentPosition()</a> or <a href="https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition">Geolocation.watchPosition()</a>.</span></div>
      <h5 id="geolocate-example" class="fs-6"><a class="text-dark mb-1 fw-bold" href="#geolocate-example">Example</a></h5>
      <div class="mb-1 api-example">
        <pre><code class="language-js">
// Initialize the geolocate control.
const geolocate = new maptilersdk.GeolocateControl({
  positionOptions: {
      enableHighAccuracy: true
  },
  trackUserLocation: true
});
// Add the control to the map.
map.addControl(geolocate);
// Set an event listener that fires
// when a geolocate event occurs.
geolocate.on('geolocate', function() {
  console.log('A geolocate event has occurred.')
});
        </code></pre>
      </div>
    </div>
  </div>
</div>

<div class="border rounded-3 my-1 accordion-item" id="geolocatecontrol.event:outofmaxbounds" aria-expanded="false">
  <div class="bg-lighter rounded-3"><a role="button" data-bs-toggle="collapse" data-bs-target="#outofmaxbounds" aria-expanded="false" aria-controls="addcontrol" class="collapsed"><span class="px-2 py-1 h6 text-secondary d-block m-0">outofmaxbounds<span class="float-end collapse-arrow"> <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><use href="/styles/style/icon/icon.svg#keyboard_arrow_down"></use></svg></span></span></a></div>
  <div id="outofmaxbounds" class="collapse" aria-labelledby="addcontrol" data-parent="#accordion">
    <div class="card-body px-2"><span>
        <p>Fired on each Geolocation API position update which returned as success but user position is out of map maxBounds.</p>
      </span>
      <h5 id="outofmaxbounds-properties" class="fs-6"><a class="text-dark mb-1 fw-bold" href="#outofmaxbounds-properties">Properties</a></h5>
      <div class="mb-1"><span class="fw-bolder me-1">data</span><code class="language-plaintext">(<span><a href="https://developer.mozilla.org/docs/Web/API/Position">Position</a></span>)</code><span>: The returned <a href="https://developer.mozilla.org/en-US/docs/Web/API/Position">Position</a> object from the callback in <a href="https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition">Geolocation.getCurrentPosition()</a> or <a href="https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition">Geolocation.watchPosition()</a>.</span></div>
      <h5 id="outofmaxbounds-example" class="fs-6"><a class="text-dark mb-1 fw-bold" href="#outofmaxbounds-example">Example</a></h5>
      <div class="mb-1 api-example">
        <pre><code class="language-js">
// Initialize the geolocate control.
const geolocate = new maptilersdk.GeolocateControl({
  positionOptions: {
      enableHighAccuracy: true
  },
  trackUserLocation: true
});
// Add the control to the map.
map.addControl(geolocate);
// Set an event listener that fires
// when an outofmaxbounds event occurs.
geolocate.on('outofmaxbounds', function() {
  console.log('An outofmaxbounds event has occurred.')
});
        </code></pre>
      </div>
    </div>
  </div>
</div>

<div class="border rounded-3 my-1 accordion-item" id="geolocatecontrol.event:trackuserlocationend" aria-expanded="false">
  <div class="bg-lighter rounded-3"><a role="button" data-bs-toggle="collapse" data-bs-target="#trackuserlocationend" aria-expanded="false" aria-controls="addcontrol" class="collapsed"><span class="px-2 py-1 h6 text-secondary d-block m-0">trackuserlocationend<span class="float-end collapse-arrow"> <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><use href="/styles/style/icon/icon.svg#keyboard_arrow_down"></use></svg></span></span></a></div>
  <div id="trackuserlocationend" class="collapse" aria-labelledby="addcontrol" data-parent="#accordion">
    <div class="card-body px-2"><span>
        <p>Fired when the Geolocate Control changes to the background state, which happens when a user changes the camera during an active position lock. This only applies when trackUserLocation is true. In the background state, the dot on the map will update with location updates but the camera will not.</p>
      </span>
      <h5 id="trackuserlocationend-example" class="fs-6"><a class="text-dark mb-1 fw-bold" href="#trackuserlocationend-example">Example</a></h5>
      <div class="mb-1 api-example">
        <pre><code class="language-js">
// Initialize the geolocate control.
const geolocate = new maptilersdk.GeolocateControl({
  positionOptions: {
      enableHighAccuracy: true
  },
  trackUserLocation: true
});
// Add the control to the map.
map.addControl(geolocate);
// Set an event listener that fires
// when a trackuserlocationend event occurs.
geolocate.on('trackuserlocationend', function() {
  console.log('A trackuserlocationend event has occurred.')
});
        </code></pre>
      </div>
    </div>
  </div>
</div>

<div class="border rounded-3 my-1 accordion-item" id="geolocatecontrol.event:trackuserlocationstart" aria-expanded="false">
  <div class="bg-lighter rounded-3"><a role="button" data-bs-toggle="collapse" data-bs-target="#trackuserlocationstart" aria-expanded="false" aria-controls="addcontrol" class="collapsed"><span class="px-2 py-1 h6 text-secondary d-block m-0">trackuserlocationstart<span class="float-end collapse-arrow"> <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><use href="/styles/style/icon/icon.svg#keyboard_arrow_down"></use></svg></span></span></a></div>
  <div id="trackuserlocationstart" class="collapse" aria-labelledby="addcontrol" data-parent="#accordion">
    <div class="card-body px-2"><span>
        <p>Fired when the Geolocate Control changes to the active lock state, which happens either upon first obtaining a successful Geolocation API position for the user (a geolocate event will follow), or the user clicks the geolocate button when in the background state which uses the last known position to recenter the map and enter active lock state (no geolocate event will follow unless the users's location changes).</p>
      </span>
      <h5 id="trackuserlocationstart-example" class="fs-6"><a class="text-dark mb-1 fw-bold" href="#trackuserlocationstart-example">Example</a></h5>
      <div class="mb-1 api-example">
        <pre><code class="language-js">
// Initialize the geolocate control.
const geolocate = new maptilersdk.GeolocateControl({
  positionOptions: {
      enableHighAccuracy: true
  },
  trackUserLocation: true
});
// Add the control to the map.
map.addControl(geolocate);
// Set an event listener that fires
// when a trackuserlocationstart event occurs.
geolocate.on('trackuserlocationstart', function() {
  console.log('A trackuserlocationstart event has occurred.')
});
        </code></pre>
      </div>
    </div>
  </div>
</div>

### Related examples

- [Locate the user](/sdk-js/examples/geolocate-control/)


<!-- MaptilerTerrainControl -->
## MaptilerTerrainControl 

<p class="github-link"><a class="text-secondary mb-2 ms-1"
      href="https://github.com/maptiler/maptiler-sdk-js/blob/main/src/controls/MaptilerTerrainControl.ts"
      target="_blank" rel="noopener noreferrer">src/MaptilerTerrainControl.ts</a></p>

The `MaptilerTerrainControl` shows a button to enable/disable the 3D terrain (does not tilt the map).

### Example

```js
const terrain3d = new maptilersdk.MaptilerTerrainControl();
map.addControl(terrain3d, 'top-left');
```

### Related examples

- [Display a 3D terrain map](/sdk-js/examples/3d-map/)
 

<!-- AttributionControl -->
## AttributionControl

<p class="github-link"><a class="text-secondary mb-2 ms-1"
      href="https://github.com/maplibre/maplibre-gl-js/tree/4.7.1/src/ui/control/attribution_control.ts"
      target="_blank" rel="noopener noreferrer">src/ui/control/attribution_control.ts</a></p>

An `AttributionControl` control presents the map's attribution information. By default, the attribution control is expanded (regardless of map width).

### Example

```js
const map = new maptilersdk.Map({attributionControl: false})
.addControl(new maptilersdk.AttributionControl({
    compact: true
}));
```

### Parameters

**options** (`Object?`) (default `{}`)


| options.compactboolean? | If true, the attribution control will always collapse when moving the map.         If false (default), use expanded attribution control that is always visible.         If "auto" or undefined, use responsive attribution that collapses when the user moves the map on maps less than 640 pixels wide.                    Attribution should not be collapsed if it can comfortably fit on the map. compact should only be used to modify default attribution when map size makes it impossible to fit default attribution and when the automatic compact resizing for default settings are not sufficient. Always prefer "auto" to true to show the attribution uncollapsed on large maps. |
| --- | --- |
| options.customAttribution(string             | Array&lt;string&gt;)? | String or strings to show in addition to any other attributions. |


 

<!-- ScaleControl -->
## ScaleControl

<p class="github-link"><a class="text-secondary mb-2 ms-1"
      href="https://github.com/maplibre/maplibre-gl-js/tree/4.7.1/src/ui/control/scale_control.ts"
      target="_blank" rel="noopener noreferrer">src/ui/control/scale_control.ts</a></p>

A `ScaleControl` control displays the ratio of a distance on the map to the corresponding distance on the ground.

### Example

```js
const scale = new maptilersdk.ScaleControl({
  maxWidth: 80,
  unit: 'imperial'
});
map.addControl(scale);

scale.setUnit('metric');
```

### Parameters

**options** (`Object?`)


| options.maxWidthnumber                  default: '100' | The maximum length of the scale control in pixels. |
| --- | --- |
| options.unitstring                  default: 'metric' | Unit of the distance ('imperial', 'metric' or 'nautical'). |



### Methods

<div class="border rounded-3 my-1 accordion-item" id="scalecontrol#setunit" aria-expanded="false">
  <div class="bg-lighter rounded-3"><a role="button" data-bs-toggle="collapse" data-bs-target="#setUnit" aria-expanded="false" aria-controls="addcontrol" class="collapsed"><span class="px-2 py-1 h6 text-secondary d-block m-0">setUnit<span class="text-dark">(unit)</span><span class="float-end collapse-arrow"> <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><use href="/styles/style/icon/icon.svg#keyboard_arrow_down"></use></svg></span></span></a></div>
  <div id="setUnit" class="collapse" aria-labelledby="addcontrol" data-parent="#accordion">
    <div class="card-body px-2"><span>
        <p>Set the scale's unit of the distance</p>
      </span>
      <h5 id="setunit-parameters" class="fs-6"><a class="text-dark mb-1 fw-bold" href="#setunit-parameters">Parameters</a></h5>
      <div class="mb-1"><span class="fw-bolder me-1">unit</span><code class="language-plaintext">(<span>Unit</span>)</code><span>Unit of the distance (<code>'imperial'</code>, <code>'metric'</code> or <code>'nautical'</code>).</span></div>
    </div>
  </div>
</div>
 

<!-- FullscreenControl -->
## FullscreenControl

<p class="github-link"><a class="text-secondary mb-2 ms-1"
      href="https://github.com/maplibre/maplibre-gl-js/tree/4.7.1/src/ui/control/fullscreen_control.ts"
      target="_blank" rel="noopener noreferrer">src/ui/control/fullscreen_control.ts</a></p>

A `FullscreenControl` control contains a button for toggling the map in and out of fullscreen mode.

### Example

```js
map.addControl(new maptilersdk.FullscreenControl({container: document.querySelector('body')}));
```

### Parameters

**options** (`Object?`)


| options.containerHTMLElement? | container is the compatible DOM element which should be made full screen. By default, the map container element will be made full screen. |
| --- | --- |



### Related examples

- [View a fullscreen map](/sdk-js/examples/fullscreen/)
 

<!-- MaptilerLogoControl -->
## MaptilerLogoControl 

<p class="github-link"><a class="text-secondary mb-2 ms-1"
      href="https://github.com/maptiler/maptiler-sdk-js/blob/main/src/controls/MaptilerLogoControl.ts"
      target="_blank" rel="noopener noreferrer">src/MaptilerLogoControl.ts</a></p>

A `MaptilerLogoControl` replaces MaplibreLogoControl.

Can be used only with paid account.

### Example

```js
const logo = new maptilersdk.MaptilerLogoControl({
  logoURL: "https://api.maptiler.com/resources/logo.svg",
  linkURL: "https://www.maptiler.com"
});
map.addControl(logo, 'bottom-left');
```

### Parameters

**options** (`Object?`)


| options.logoURLstring                  default: "" | Image logo URL. |
| --- | --- |
| options.linkURLstring                  default: "" | Logo link URL |


 

<!-- MaptilerMinimapControl -->
## MaptilerMinimapControl 

<p class="github-link"><a class="text-secondary mb-2 ms-1"
      href="https://github.com/maptiler/maptiler-sdk-js/blob/main/src/controls/Minimap.ts" target="_blank"
      rel="noopener noreferrer">src/Minimap.ts</a></p>
      
A `MaptilerMinimapControl` control. Display a overview (minimap) in a user defined corner of the map.

### Parameters

**options** (`Object?`)


| options.style                             (ReferenceMapStyle | MapStyleVariant | string | StyleSpecification)? | The map's style. This must be:                        ReferenceMapStyle (e.g. MapStyle.STREETS)             MapStyleVariant (e.g. MapStyle.STREETS.DARK)             MapTIler Style ID (e.g. “streets-v4”)             uuid of custom style             an a JSON object conforming to the schema described in the GL Style Specification             a URL to such JSON. |
| --- | --- |
| options.zoomAdjustnumber?                  default: -4 | Set the zoom difference between the parent and the minimap. If the parent is zoomed to 10 and the minimap is zoomed to 8, the zoomAdjust should be 2. |
| options.lockZoomnumber? | Set a zoom of the minimap and don't allow any future changes. |
| options.pitchAdjustboolean?                  default: false | Adjust the pitch only if the user requests. |
| options.containerStyleRecord&lt;string, string&gt;? | Set CSS properties of the container using object key-values. |
| options.positionstring?                  default: 'bottom-left' | Set the position of the minimap. Valid values are 'top-left', 'top-right', 'bottom-left', and 'bottom-right'. |
| options.parentRectParentRect? | Set the parentRect fill and/or line options. |


 

<!-- MaptilerProjectionControl -->
## MaptilerProjectionControl 

<p class="github-link"><a class="text-secondary mb-2 ms-1"
      href="https://github.com/maplibre/maplibre-gl-js/tree/4.7.1/src/ui/control/globe_control.ts"
      target="_blank" rel="noopener noreferrer">src/ui/control/globe_control.ts</a></p>

A `MaptilerProjectionControl` control contains a button for toggling the map projection between "mercator" and "globe".

### Example

```js
map.addControl(new maptilersdk.MaptilerProjectionControl());
```

### Related examples

- [Projection control how to toggle the map between mercator and globe projection](/sdk-js/examples/globe-control/)


<!-- MaptilerExternalControl -->
## MaptilerExternalControl 

<p class="github-link"><a class="text-secondary mb-2 ms-1"
      href="https://github.com/maptiler/maptiler-sdk-js/blob/main/src/controls/MaptilerExternalControl.ts" target="_blank"
      rel="noopener noreferrer">src/controls/MaptilerExternalControl.ts</a></p>

The `MaptilerExternalControl` allows any existing element to automatically become a map control. Used for detected controls if `customControls` config is turned on.

### Example

```js
const zoomInControl = new maptilersdk.MaptilerExternalControl(
  ".zoom-in-control",
  "zoom-in"
);
```

### Parameters

- **controlElement** (`HTMLElement`): Element to be used as control, specified as either reference to element itself or a CSS selector to find the element in DOM
- **controlType** (`MaptilerExternalControlType`): One of the predefined types of functionality. Allowed values: `zoom-in` | `zoom-out` | `toggle-projection` | `toggle-terrain` | `reset-view` | `reset-bearing` | `reset-pitch` | `reset-roll`


<!-- MaptilerCustomControl -->
## MaptilerCustomControl 

<p class="github-link"><a class="text-secondary mb-2 ms-1"
      href="https://github.com/maptiler/maptiler-sdk-js/blob/main/src/controls/MaptilerCustomControl.ts" target="_blank"
      rel="noopener noreferrer">src/controls/MaptilerCustomControl.ts</a></p>

The `MaptilerCustomControl` allows any existing element to become a map control.

### Example

```js
const panControl = new maptilersdk.MaptilerCustomControl(
  ".pan-control",
  (map) => map.panBy([10, 10]), // Move southeast when clicked
  (map, el) => el.classList.toggle( // Change class based on current hemisphere
    "northern-hemisphere", map.getCenter().lat > 0
  )
);
```

### Parameters

- **selectorOrElement** (`string` | `HTMLElement`): Element to be used as control, specified as either reference to element itself or a CSS selector to find the element in DOM
- **onClick** (`MaptilerCustomControlCallback<PointerEvent>?`): Function called when the element is clicked
- **onRender** (`MaptilerCustomControlCallback<MapLibreEvent>?`): Function called every time the underlying map renders a new state

> [!INFO]
> Both callbacks receive the active `Map` instance, the associated control element itself, and an event object associated with the original event (`PointerEvent` and `MapLibreEvent` respectively).

### Related examples

- [How to add a custom control programmatically](/sdk-js/examples/custom-controls-programmatic/)


<!-- IControl -->
## IControl

<p class="github-link"><a class="text-secondary mb-2 ms-1"
      href="https://github.com/maplibre/maplibre-gl-js/tree/4.7.1/src/ui/control/control.ts" target="_blank"
      rel="noopener noreferrer">src/ui/control/control.ts</a></p>

Interface for interactive controls added to the map. This is a specification for implementers to model: it is not an exported method or class. This interface is the one to use to create custom controls.

Controls must implement `onAdd` and `onRemove`, and must own an element, which is often a `div` element. To use MapLibre GL JS's default control styling, add the `maplibregl-ctrl` class to your control's node.

### Example

```js
// Control implemented as ES6 class
class HelloWorldControl {
  onAdd(map) {
      this._map = map;
      this._container = document.createElement('div');
      this._container.className = 'maplibregl-ctrl';
      this._container.textContent = 'Hello, world';
      return this._container;
  }

  onRemove() {
      this._container.parentNode.removeChild(this._container);
      this._map = undefined;
  }
}

// Control implemented as ES5 prototypical class
function HelloWorldControl() { }

HelloWorldControl.prototype.onAdd = function(map) {
  this._map = map;
  this._container = document.createElement('div');
  this._container.className = 'maplibregl-ctrl';
  this._container.textContent = 'Hello, world';
  return this._container;
};

HelloWorldControl.prototype.onRemove = function () {
    this._container.parentNode.removeChild(this._container);
    this._map = undefined;
};
```

### Methods

<div class="border rounded-3 my-1 accordion-item" id="icontrol#getdefaultposition" aria-expanded="false">
  <div class="bg-lighter rounded-3"><a role="button" data-bs-toggle="collapse" data-bs-target="#getDefaultPosition" aria-expanded="false" aria-controls="addcontrol" class="collapsed"><span class="px-2 py-1 h6 text-secondary d-block m-0">getDefaultPosition<span class="text-dark">()</span><span class="float-end collapse-arrow"> <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><use href="/styles/style/icon/icon.svg#keyboard_arrow_down"></use></svg></span></span></a></div>
  <div id="getDefaultPosition" class="collapse" aria-labelledby="addcontrol" data-parent="#accordion">
    <div class="card-body px-2"><span>
        <p>Optionally provide a default position for this control. If this method is implemented and <a href="/sdk-js/api/map/#map#addcontrol">Map#addControl</a> is called without the <code>position</code> parameter, the value returned by getDefaultPosition will be used as the control's position.</p>
      </span>
      <h5 id="getdefaultposition-returns" class="fs-6"><a class="text-dark mb-1 fw-bold" href="#getdefaultposition-returns">Returns</a></h5><code class="language-plaintext"><span>ControlPosition</span></code><span>: a control position, one of the values valid in addControl.</span>
    </div>
  </div>
</div>

<div class="border rounded-3 my-1 accordion-item" id="icontrol#onadd" aria-expanded="false">
  <div class="bg-lighter rounded-3"><a role="button" data-bs-toggle="collapse" data-bs-target="#onAdd" aria-expanded="false" aria-controls="addcontrol" class="collapsed"><span class="px-2 py-1 h6 text-secondary d-block m-0">onAdd<span class="text-dark">(map)</span><span class="float-end collapse-arrow"> <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><use href="/styles/style/icon/icon.svg#keyboard_arrow_down"></use></svg></span></span></a></div>
  <div id="onAdd" class="collapse" aria-labelledby="addcontrol" data-parent="#accordion">
    <div class="card-body px-2"><span>
        <p>Register a control on the map and give it a chance to register event listeners and resources. This method is called by <a href="/sdk-js/api/map/#map#addcontrol">Map#addControl</a> internally.</p>
      </span>
      <h5 id="onadd-parameters" class="fs-6"><a class="text-dark mb-1 fw-bold" href="#onadd-parameters">Parameters</a></h5>
      <div class="mb-1"><span class="fw-bolder me-1">map</span><code class="language-plaintext">(<span><a href="/sdk-js/api/map/#map">Map</a></span>)</code><span>the Map this control will be added to</span></div>
      <h5 id="onadd-returns" class="fs-6"><a class="text-dark mb-1 fw-bold" href="#onadd-returns">Returns</a></h5>
      <code class="language-plaintext"><span><a href="https://developer.mozilla.org/docs/Web/HTML/Element">HTMLElement</a></span></code><span>: The control's container element. This should be created by the control and returned by onAdd without being attached to the DOM: the map will insert the control's element into the DOM as necessary.</span>
    </div>
  </div>
</div>

<div class="border rounded-3 my-1 accordion-item" id="icontrol#onremove" aria-expanded="false">
  <div class="bg-lighter rounded-3"><a role="button" data-bs-toggle="collapse" data-bs-target="#onRemove" aria-expanded="false" aria-controls="addcontrol" class="collapsed"><span class="px-2 py-1 h6 text-secondary d-block m-0">onRemove<span class="text-dark">(map)</span><span class="float-end collapse-arrow"> <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><use href="/styles/style/icon/icon.svg#keyboard_arrow_down"></use></svg></span></span></a></div>
  <div id="onRemove" class="collapse" aria-labelledby="addcontrol" data-parent="#accordion">
    <div class="card-body px-2"><span>
        <p>Unregister a control on the map and give it a chance to detach event listeners and resources. This method is called by <a href="/sdk-js/api/map/#map#removecontrol">Map#removeControl</a> internally.</p>
      </span>
      <h5 id="onremove-parameters" class="fs-6"><a class="text-dark mb-1 fw-bold" href="#onremove-parameters">Parameters</a></h5>
      <div class="mb-1"><span class="fw-bolder me-1">map</span><code class="language-plaintext">(<span><a href="/sdk-js/api/map/#map">Map</a></span>)</code><span>the Map this control will be removed from</span></div>
      <h5 id="onremove-returns" class="fs-6"><a class="text-dark mb-1 fw-bold" href="#onremove-returns">Returns</a></h5>
      <code class="language-plaintext"><span><a href="https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/undefined">undefined</a></span></code><span>: there is no required return value for this method</span>
    </div>
  </div>
</div>



