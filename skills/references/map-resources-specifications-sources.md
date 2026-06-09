# Source: https://docs.maptiler.com/gl-style-specification/sources/

# Sources

Sources state which data the map should display. Specify the type of source with the `"type"` property, which must be one of `vector, raster, raster-dem, geojson, image, video.` Adding a source isn't enough to make data appear on the map because sources don't contain styling details like color or width. Layers refer to a source and give it a visual representation. This makes it possible to style the same source in different ways, like differentiating between types of roads in a highways layer.

Tiled sources (vector and raster) must specify their details according to the [TileJSON specification](https://github.com/mapbox/tilejson-spec). There are several ways to do so:

- By supplying TileJSON properties such as `"tiles"`, `"minzoom"`, and `"maxzoom"` directly in the source:

```json
"streets": {
    "type": "vector",
    "tiles": [
        "http://a.example.com/tiles/{z}/{x}/{y}.pbf",
        "http://b.example.com/tiles/{z}/{x}/{y}.pbf"
    ],
    "maxzoom": 14
}
```

- By providing a `"url"` to a TileJSON resource:

```json
"streets": {
    "type": "vector",
    "url": "http://api.example.com/tilejson.json"
}
```

- By providing a URL to a WMS server that supports EPSG:3857 (or EPSG:900913) as a source of tiled data. The server URL should contain a `"{bbox-epsg-3857}"` replacement token to supply the `bbox` parameter.

```json
"wms-imagery": {
    "type": "raster",
    "tiles": [
        "http://a.example.com/wms?bbox={bbox-epsg-3857}&format=image/png&service=WMS&version=1.1.1&request=GetMap&srs=EPSG:3857&width=256&height=256&layers=example"
    ],
    "tileSize": 256
}
```

## vector

A vector tile source. Tiles must be in [Vector Tile format](https://www.maptiler.com/news/2019/02/what-are-vector-tiles-and-why-you-should-care/). All geometric coordinates in vector tiles must be between `-1 * extent` and `(extent * 2) - 1` inclusive. All layers that use a vector source must specify a [`"source-layer"`](../layers/#source-layer) value. For vector tiles hosted by MapTiler, the `"url"` value should be of the form  `https://api.maptiler.com/tiles/{tilesetid}/tiles.json?key=<YOUR_MAPTILER_API_KEY>"`.

```json
"Streets": {
    "type": "vector",
    "url": "https://api.maptiler.com/tiles/v3/tiles.json?key=<YOUR_MAPTILER_API_KEY>"
}
```

### attribution

Optional [string](../types/#string)

Contains an attribution to be displayed when the map is shown to a user.

### bounds

Optional [array](../types/#array) of [numbers](../types/#number). Defaults to `[-180,-85.051129,180,85.051129]`.

An array containing the longitude and latitude of the southwest and northeast corners of the source's bounding box in the following order: `[sw.lng, sw.lat, ne.lng, ne.lat]`. When this property is included in a source, no tiles outside of the given bounds are requested by MapTiler SDK JS.

### maxzoom

Optional [number](../types/#number). Defaults to `22`.

Maximum zoom level for which tiles are available, as in the TileJSON spec. Data from tiles at the maxzoom are used when displaying the map at higher zoom levels.

### minzoom

Optional [number](../types/#number). Defaults to `0`.

Minimum zoom level for which tiles are available, as in the TileJSON spec.

### promoteId

Optional [promoteId](../types/#promoteid).

A property to use as a feature id (for feature state). Either a property name, or an object of the form `{<sourceLayer>: <propertyName>}`. If specified as a string for a vector tile source, the same property is used across all its source layers.

### scheme

Optional [enum](../types/#enum). One of `"xyz"`, `"tms"`. Defaults to `"xyz"`.

Influences the y direction of the tile coordinates. The global-mercator (aka Spherical Mercator) profile is assumed.

`"xyz"`:

Slippy map tilenames scheme.

`"tms"`:

OSGeo spec scheme.

### tiles

Optional [array](../types/#array) of [strings](../types/#string).

An array of one or more tile source URLs, as in the TileJSON spec.

### url

Optional [string](../types/#string).

A URL to a TileJSON resource. Supported protocols are `http:`, `https:`.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

## raster

A raster tile source. For raster tiles hosted by MapTiler, the `"url"` value should be of the form `https://api.maptiler.com/tiles/[tilesetid]/tiles.json?key=<YOUR_MAPTILER_API_KEY>`.

```json
"satellite": {
    "type": "raster",
    "url": "https://api.maptiler.com/tiles/satellite/tiles.json?key=<YOUR_MAPTILER_API_KEY>",
    "tileSize": 256
}
```

### attribution

Optional [string](../types/#string).

Contains an attribution to be displayed when the map is shown to a user.

### bounds

Optional [array](../types/#array) of [numbers](../types/#number). Defaults to `[-180,-85.051129,180,85.051129]`.

An array containing the longitude and latitude of the southwest and northeast corners of the source's bounding box in the following order: `[sw.lng, sw.lat, ne.lng, ne.lat]`. When this property is included in a source, no tiles outside of the given bounds are requested by MapTiler SDK JS.

### maxzoom

Optional [number](../types/#number). Defaults to `22`.

Maximum zoom level for which tiles are available, as in the TileJSON spec. Data from tiles at the maxzoom are used when displaying the map at higher zoom levels.

### minzoom

Optional [number](../types/#number). Defaults to `0`.

Minimum zoom level for which tiles are available, as in the TileJSON spec.

### scheme

Optional [enum](../types/#enum). One of `"xyz"`, `"tms"`. Defaults to `"xyz"`.

Influences the y direction of the tile coordinates. The global-mercator (aka Spherical Mercator) profile is assumed.

`"xyz"`:

Slippy map tilenames scheme.

`"tms"`:

OSGeo spec scheme.

### tileSize

Optional [number](../types/#number). Units in pixels. Defaults to `512`.

The minimum visual size to display tiles for this layer. Only configurable for raster layers.

### tiles

Optional [array](../types/#array) of [strings](../types/#string).

An array of one or more tile source URLs, as in the TileJSON spec.

### url

Optional [string](../types/#string).

A URL to a TileJSON resource. Supported protocols are `http:`, `https:`.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

## raster-dem

A raster DEM source. Only supports [Terrain RGB](/guides/map-tiling-hosting/data-hosting/rgb-terrain-by-maptiler)

```json
"terrain-rgb": {
    "type": "raster-dem",
    "url": "https://api.maptiler.com/tiles/terrain-rgb-v2/tiles.json?key=<YOUR_MAPTILER_API_KEY>"
}
```

### attribution

Optional [string](../types/#string).

Contains an attribution to be displayed when the map is shown to a user.

### bounds

Optional [array](../types/#array) of [numbers](../types/#number). Defaults to `[-180,-85.051129,180,85.051129]`.

An array containing the longitude and latitude of the southwest and northeast corners of the source's bounding box in the following order: `[sw.lng, sw.lat, ne.lng, ne.lat]`. When this property is included in a source, no tiles outside of the given bounds are requested by MapTiler SDK JS.

### encoding

Optional [enum](../types/#enum). One of `"terrarium"`, `"mapbox"`. Defaults to `"mapbox"`.

The encoding used by this source. Terrain RGB is used by default

`"terrarium"`:

Terrarium format PNG tiles. See [https://aws.amazon.com/es/public-datasets/terrain/](https://aws.amazon.com/es/public-datasets/terrain/) for more info.

`"mapbox"`:

Terrain RGB tiles. See [RGB Terrain by MapTiler](/guides/map-tiling-hosting/data-hosting/rgb-terrain-by-maptiler) for more info.

### maxzoom

Optional [number](../types/#number). Defaults to `22`.

Maximum zoom level for which tiles are available, as in the TileJSON spec. Data from tiles at the maxzoom are used when displaying the map at higher zoom levels.

### minzoom

Optional [number](../types/#number). Defaults to `0`.

Minimum zoom level for which tiles are available, as in the TileJSON spec.

### tileSize

Optional [number](../types/#number). Units in pixels. Defaults to `512`.

The minimum visual size to display tiles for this layer. Only configurable for raster layers.

### tiles

Optional [array](../types/#array) of [strings](../types/#string).

An array of one or more tile source URLs, as in the TileJSON spec.

### url

Optional [string](../types/#string).

A URL to a TileJSON resource. Supported protocols are `http:`, `https:`.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.43.0 | Not yet supported | Not yet supported | Not yet supported |

## geojson

A [GeoJSON](https://geojson.org/) source. Data must be provided via a `"data"` property, whose value can be a URL or inline GeoJSON.

```json
"geojson-marker": {
    "type": "geojson",
    "data": {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [16.62662018, 49.2125578]
        },
        "properties": {
            "title": "MapTiler",
            "marker-symbol": "monument"
        }
    }
}
```

This example of a GeoJSON source refers to an external GeoJSON document via its URL. The GeoJSON document must be on the same domain or accessible using [CORS](https://enable-cors.org/).

```json
"geojson-lines": {
    "type": "geojson",
    "data": "./lines.geojson"
}
```

### attribution

Optional [string](../types/#string).

Contains an attribution to be displayed when the map is shown to a user.

### buffer

Optional [number](../types/#number) between `0` and `512` inclusive. Defaults to `128`.

Size of the tile buffer on each side. A value of 0 produces no buffer. A value of 512 produces a buffer as wide as the tile itself. Larger values produce fewer rendering artifacts near tile edges and slower performance.

### cluster

Optional [boolean](../types/#boolean). Defaults to `false`.

If the data is a collection of point features, setting this to true clusters the points by radius into groups. Cluster groups become new `Point` features in the source with additional properties:

- `cluster` Is `true` if the point is a cluster
- `cluster_id` A unqiue id for the cluster to be used in conjunction with the cluster inspection methods
- `point_count` Number of original points grouped into this cluster
- `point_count_abbreviated` An abbreviated point count

### clusterMaxZoom

Optional [number](../types/#number).

Max zoom on which to cluster points if clustering is enabled. Defaults to one zoom less than maxzoom (so that last zoom features are not clustered).

### clusterProperties

Optional.

An object defining custom properties on the generated clusters if clustering is enabled, aggregating values from clustered points. Has the form `{"property_name": [operator, map_expression]}`. `operator` is any expression function that accepts at least 2 operands (e.g. `"+"` or `"max"`) — it accumulates the property value from clusters/points the cluster contains; `map_expression` produces the value of a single point.

Example: `{"sum": ["+", ["get", "scalerank"]]}`.

For more advanced use cases, in place of `operator`, you can use a custom reduce expression that references a special `["accumulated"]` value, e.g.: `{"sum": [["+", ["accumulated"], ["get", "sum"]], ["get", "scalerank"]]}`

### clusterRadius

Optional [number](../types/#number) greater than or equal to `0`. Defaults to `50`.

Radius of each cluster if clustering is enabled. A value of 512 indicates a radius equal to the width of a tile.

### data

Optional.

A URL to a GeoJSON file, or inline GeoJSON.

### generateId

Optional [boolean](../types/#boolean). Defaults to `false`.

Whether to generate ids for the geojson features. When enabled, the `feature.id` property will be auto assigned based on its index in the `features` array, over-writing any previous values.

### lineMetrics

Optional [boolean](../types/#boolean). Defaults to `false`.

Whether to calculate line distance metrics. This is required for line layers that specify `line-gradient` values.

### maxzoom

Optional [number](../types/#number). Defaults to `18`.

Maximum zoom level at which to create vector tiles (higher means greater detail at high zoom levels).

### promoteId

Optional [promoteId](../types/#promoteid).

A property to use as a feature id (for feature state). Either a property name, or an object of the form `{<sourceLayer>: <propertyName>}`.

### tolerance

Optional [number](../types/#number). Defaults to `0.375`.

Douglas-Peucker simplification tolerance (higher means simpler geometries and faster performance).

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| clustering | >= 0.14.0 | >= 4.2.0 | >= 3.4.0 | >= 0.3.0 |
| line distance metrics | >= 0.45.0 | >= 6.5.0 | >= 4.4.0 | >= 0.11.0 |

## image

An image source. The `"url"` value contains the image location.

The `"coordinates"` array contains `[longitude, latitude]` pairs for the image corners listed in clockwise order: top left, top right, bottom right, bottom left.

```json
"image": {
    "type": "image",
    "url": "https://docs.maptiler.com/sdk-js/raster-layer/img/aerial_wgs84.png",
    "coordinates": [
        [4.639663696289062, 50.900867668253724],
        [4.642066955566406, 50.900867668253724],
        [4.642066955566406, 50.89935199434383],
        [4.639663696289062, 50.89935199434383]
    ]
}
```

### coordinates

Required [array](../types/#array) of [array](../types/#array) of [numbers](../types/#number).

Corners of image specified in longitude, latitude pairs.

### url

Required [string](../types/#string).

URL that points to an image.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 5.2.0 | >= 3.7.0 | >= 0.6.0 |

## video

A video source. The `"urls"` value is an array. For each URL in the array, a video element [source](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/source) will be created. To support the video across browsers, supply URLs in multiple formats.

The `"coordinates"` array contains `[longitude, latitude]` pairs for the video corners listed in clockwise order: top left, top right, bottom right, bottom left.

```json
"video": {
    "type": "video",
    "urls": [
        "https://static-assets.mapbox.com/mapbox-gl-js/drone.mp4",
        "https://static-assets.mapbox.com/mapbox-gl-js/drone.webm"
    ],
    "coordinates": [
        [-122.51596391201019, 37.56238816766053],
        [-122.51467645168304, 37.56410183312965],
        [-122.51309394836426, 37.563391708549425],
        [-122.51423120498657, 37.56161849366671]
    ]
}
```

### coordinates

Required [array](../types/#array) of [array](../types/#array) of [numbers](../types/#number).

Corners of video specified in longitude, latitude pairs.

### urls

Required [array](../types/#array) of [strings](../types/#string).

URLs to video content in order of preferred format.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | Not yet supported | Not yet supported | Not yet supported |
