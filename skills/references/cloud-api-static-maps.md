# Static Maps API

The **Static Maps API** makes it possible to use our maps as non-interactive, non-zoomable images. Adding markers or lines to static maps is also supported.

---

## API Reference
URL: https://docs.maptiler.com/cloud/api/static-maps/

### Center-based image
`GET https://api.maptiler.com/maps/{mapId}/static/{lon},{lat},{zoom}/{width}x{height}{scale}.{format}`
- **Parameters:** `lon`, `lat`, `zoom`, `width`, `height` (max 2048), `scale` (`@2x`), `format`.

### Bounds-based image
`GET https://api.maptiler.com/maps/{mapId}/static/{minx},{miny},{maxx},{maxy}/{width}x{height}{scale}.{format}`
- **Parameters:** `minx`, `miny`, `maxx`, `maxy` (WGS84 degrees).

### Auto-fitted image
`GET https://api.maptiler.com/maps/{mapId}/static/auto/{width}x{height}{scale}.{format}`
- **Description:** Calculates area based on features (paths/markers) provided in query parameters.

### Common Query Parameters
- `path`: Define lines/polygons (e.g., `stroke:red|width:3|5.9,45.8|...`).
- `markers`: Define markers (e.g., `icon:default|anchor:center|8.5,47.3`).
- `padding`: Margin for auto-fitted images (default `0.1`).
- `attribution`: Position of attribution (default `bottomright`).

---

## Usage Guide

This section explains how to insert a map into a webpage as a static non-zoomable map image.

A map image shows any area you specify on a map of your choice. A static map renders a fresh, up-to-date map image whenever it loads.

### Quick start

The URL of a static map image is actually an API request to the **Static maps API**, containing all the necessary parameters to render the map image. The easiest way to generate the image's API URL is to use our visual generator:

[Open static maps generator](https://www.maptiler.com/cloud/static-maps/generator/)

With the URL generated, insert the map image into your website just like a regular image, for example using HTML tag ``.

The API URL contains a placeholder for an API key. Replace `YOUR_MAPTILER_API_KEY_HERE` with your actual API key.

### Switch map to static

If you have an existing interactive web map, you can switch it to static with a single parameter. This is also handy if you need to add more complex features than markers and lines. See the code example "Create a non-interactive map" for MapTiler SDK JS.

---

## Defining the Area

This section explains in detail how the API URL for a static map is constructed.

### By center

To define your map image by its center, use this URL format:

`https://api.maptiler.com/maps/{mapId}/static/{longitude},{latitude},{zoom}/{width}x{height}.{format}?key=YOUR_MAPTILER_API_KEY_HERE`

#### Parameters

- **mapId** – Identifier of the map (e.g., `streets-v4`).
- **lng, lat** – WGS84 coordinates.
- **zoom** – Zoom level.
- **width, height** – The image dimensions in pixels.
- **format** – The image format, for example `PNG`.
- **key** – Your MapTiler API key.

*Bearing and pitch aren't supported at the moment.*

#### Example

`https://api.maptiler.com/maps/dataviz/static/8.581627,47.137726,16/825x350.png?key=YOUR_MAPTILER_API_KEY_HERE`

### Get HiDPI resolution

For Retina and other high resolution displays, add `@2x` before the file extension to increase scale. This renders the map image in double resolution.

#### Example

`https://api.maptiler.com/maps/dataviz/static/8.581627,47.137726,16/825x350@2x.png?key=YOUR_MAPTILER_API_KEY_HERE`

### By bounds

To define your map area by a bounding box, use this format:

`https://api.maptiler.com/maps/{mapId}/static/{minx},{miny},{maxx},{maxy}/{width}x{height}.{format}?key=YOUR_MAPTILER_API_KEY_HERE`

Parameters are the same as in a center-based URL, except:

- **minx, miny** – Coordinates of the lower left corner of the bounding box.
- **maxx, maxy** – Coordinates of the upper right corner of the bounding box.

#### Example

`https://api.maptiler.com/maps/base/static/-70.3,-46.5,70.3,46.5/825x350.png?key=YOUR_MAPTILER_API_KEY_HERE`

### Auto-fit

If you add at least one marker, line, or polygon to your static map, you can use `auto` instead of center or bounds. This will calculate the image area automatically so that all markers and paths in your query are visible.

---

## Working with Markers

To add markers to your static map, use the `markers` parameter in the URL. Each marker is a `lng,lat` pair of coordinates, with multiple markers separated by pipe symbols `|`.

To get the coordinates of a place, use our [Coordinates finder](https://www.maptiler.com/tools/coordinates) tool.

### Basic markers

`https://api.maptiler.com/maps/base-v4/static/auto/825x350.png?key=YOUR_MAPTILER_API_KEY_HERE&markers=14.4,50.1|8.6,47.4|2.4,48.9`

### Colored markers

To style your markers in various colors, add color as a third parameter. You can define color in several ways:

- Color names: `red`, `blue`
- RGBA: `rgba(255,255,255,0.5)`
- Hexadecimal: `#0000ff` (use `%23` instead of `#` in URLs!)

`https://api.maptiler.com/maps/base-v4/static/auto/825x350.png?key=YOUR_MAPTILER_API_KEY_HERE&markers=14.4,50.1,red|8.6,47.4,rgba(118,31,232,1)|2.4,48.9,%23ffaa00`

### Custom marker icons

To use a custom image as marker, add the necessary parameters in this format:

`&markers=icon:{url}|anchor:{position]}|{scale}|{lng,lat}`

- **icon** – Specify URL to a remote image.
  - Max size of the icon image is 4096 pixels (64 x 64)
  - SVG icons must have explicit width and height attributes
  - URLs generated by shortener services are allowed
  - Any specified colors are ignored
- **anchor** – Specify the position (anchor point) of the icon relative to its coordinates.
  - Accepted values: `top`, `left`, `bottom`, `right`, `center`, `topleft`, `bottomleft`, `topright`, `bottomright`
  - Default is `bottom`
- **scale** – Scale of the image icon. Default is `1`, for HiDPI/Retina displays use `2`.
- **lng, lat** – Add the coordinates of where to place the marker icon. You can specify multiple places separated by pipe symbols `|`.

#### Single custom marker

`https://api.maptiler.com/maps/dataviz/static/8.579446,47.127792,16/825x350.png?key=YOUR_MAPTILER_API_KEY_HERE&markers=icon:https://tinyurl.com/yakrjl3t|anchor:center|8.57916,47.127899`

#### Multiple custom markers

*Note that you can only use one custom icon for multiple markers.*

`https://api.maptiler.com/maps/base-v4/static/auto/825x350.png?key=YOUR_MAPTILER_API_KEY_HERE&markers=icon:https://tinyurl.com/yakrjl3t|anchor:center|14.4,50.1|8.6,47.4|2.4,48.9`

### Use case: Office locations

```html
<a
  href="https://api.maptiler.com/maps/dataviz/?key=YOUR_MAPTILER_API_KEY_HERE#17.87/49.21256/16.626597"
  target="_blank"
  rel="noopener"
>
  <img
    src="https://api.maptiler.com/maps/dataviz/static/16.626597,49.21256,15/200x200.png?key=YOUR_MAPTILER_API_KEY_HERE&markers=icon:https://tinyurl.com/yakrjl3t|anchor:center|16.626597,49.21256"
  />
</a>
```

---

## Working with Lines and Polygons

To add lines or polygons to your static map, specify coordinates of the individual path vertices as comma-separated lng, lat pairs. To get the coordinates, use our [Coordinates finder](https://www.maptiler.com/tools/coordinates) tool.

You can add multiple lines by using the path parameter several times. Separate the vertices by a pipe symbol `|`.

Specify styling before the path coordinates using `key:value` format:

- **fill** – Fill color: `red`, `rgba(255,255,255,0.5)`, `#0000ff` (default: `rgba(255, 255, 255, 0.5)`). To draw lines without fill, set the fill property to `none` or `false`.
- **stroke** – Stroke color (default: `blue`)
- **width** – Stroke width in pixels (default: `1`)
- **shortest** – Draw the shortest paths, crossing the dateline if needed.
- **enc** – Path encoded with [Google Encoded Polyline Format](https://developers.google.com/maps/documentation/utilities/polylinealgorithm) (optional).

### Examples

#### Simple Line
`https://api.maptiler.com/maps/streets/static/auto/825x350.png?key=YOUR_MAPTILER_API_KEY_HERE&path=fill:none|width:3|stroke:red|2.1699929237365723,41.40282721444188|2.1697568893432617,41.40266626487097|2.1708834171295166,41.401801154097434|2.172026038169861,41.40266224112659|2.173168659210205,41.40181724928674|2.1750354766845703,41.403217515495896`

#### Multiple Lines
`https://api.maptiler.com/maps/base/static/auto/825x350.png?key=YOUR_MAPTILER_API_KEY_HERE&path=fill:none|width:3|stroke:red|2.1751588582992554,41.40390556628419|2.1745795011520386,41.404336097282346|2.17429518699646,41.40427171899671|2.174190580844879,41.40433408546189|2.1740511059761047,41.4042314825358&path=fill:none|width:3|stroke:blue|2.1751856803894043,41.403909589951574|2.1755397319793697,41.40361586157709|2.17429518699646,41.402710526042696`

#### Polygon
`https://api.maptiler.com/maps/hybrid/static/-80.40494,26.11650,16/825x350.png?key=YOUR_MAPTILER_API_KEY_HERE&path=width:3|stroke:rgba(255,170,1,1)|-80.40516972541809,26.11666628740777|-80.40514826774597,26.116630162087464|-80.40510803461075,26.116547073808373|-80.40506646037102,26.116436289344406|-80.40499940514565,26.116255662275762|-80.40496319532393,26.116255662275762|-80.40483713150024,26.116313462968083|-80.40466278791428,26.116457964573883|-80.40470570325851,26.11651456098744|-80.40483176708221,26.116654245635566|-80.40503025054932,26.116740946367674|-80.40506646037102,26.116704821070446|-80.40516972541809,26.11666628740777`
