# Source: https://docs.maptiler.com/gl-style-specification/layers/

# Layers

A style's `layers` property lists all the layers available in that style. The type of layer is specified by the `"type"` property, and must be one of `background, fill, line, symbol, raster, circle, fill-extrusion, heatmap, hillshade`.

Except for layers of the _background_ type, each layer needs to refer to a source. Layers take the data that they get from a source, optionally filter features, and then define how those features are styled.

```json
"layers": [
  {
    "id": "water",
    "source": "streets",
    "source-layer": "water",
    "type": "fill",
    "paint": {
      "fill-color": "#00ffff"
    }
  }
]
```

## filter

Optional [expression](../expressions).

A expression specifying conditions on source features. Only features that match the filter are displayed. Zoom expressions in filters are only evaluated at integer zoom levels. The `feature-state` expression is not supported in filter expressions.

## id

Required [string](../types/#string).

Unique layer name.

## layout

Optional [layout](#layout-property).

Layout properties for the layer.

## maxzoom

Optional [number](../types/#number) between `0` and `24` inclusive.

The maximum zoom level for the layer. At zoom levels equal to or greater than the maxzoom, the layer will be hidden.

## metadata

Optional.

Arbitrary properties useful to track with the layer, but do not influence rendering. Properties should be prefixed to avoid collisions, like 'openmaptiles:'.

## minzoom

Optional [number](../types/#number) between `0` and `24` inclusive.

The minimum zoom level for the layer. At zoom levels less than the minzoom, the layer will be hidden.

## paint

Optional [paint](#paint-property).

Default paint properties for this layer.

## source

Optional [string](../types/#string).

Name of a source description to be used for this layer. Required for all layer types except `background`.

## source-layer

Optional [string](../types/#string).

Layer to use from a vector tile source. Required for vector tile sources; prohibited for all other source types, including GeoJSON sources.

## type

Required [enum](../types/#enum). One of `"fill"`, `"line"`, `"symbol"`, `"circle"`, `"heatmap"`, `"fill-extrusion"`, `"raster"`, `"hillshade"`, `"background"`.

Rendering type of this layer.

`"fill"`:

A filled polygon with an optional stroked border.

`"line"`:

A stroked line.

`"symbol"`:

An icon or a text label.

`"circle"`:

A filled circle.

`"heatmap"`:

A heatmap.

`"fill-extrusion"`:

An extruded (3D) polygon.

`"raster"`:

Raster map textures such as satellite imagery.

`"hillshade"`:

Client-side hillshading visualization based on DEM data. Currently, the implementation only supports Terrain RGB and Mapzen Terrarium tiles.

`"background"`:

The background color or pattern of the map.

<a id="layout-property" className="anchor" />
<a id="paint-property" className="anchor" />

<hr>

Layers have two sub-properties that determine how data from that layer is rendered: `layout` and `paint` properties.

_Layout properties_ appear in the layer's `"layout"` object. They are applied early in the rendering process and define how data for that layer is passed to the GPU. Changes to a layout property require an asynchronous "layout" step.

_Paint properties_ are applied later in the rendering process. Paint properties appear in the layer's `"paint"` object. Changes to a paint property are cheap and happen synchronously.

## [background](#background)

The `background` style layer covers the entire map. Use a background style layer to configure a color or pattern to show below all other map content. If the background layer is transparent or omitted from the style, any part of the map view that does not show another style layer is transparent.



Use a custom SVG [`background-pattern`](#background-pattern) to achieve a textured vintage look.

### background-color

[Paint](#paint-property) property. Optional [color](../types/#color). Defaults to `"#000000"`. _Disabled by_ background-pattern. Supports [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

The color with which the background will be drawn.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

### background-opacity

[Paint](#paint-property) property. Optional [number](../types/#number) between `0` and `1` inclusive. Defaults to `1`. Supports [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

The opacity at which the background will be drawn.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

### background-pattern

[Paint](#paint-property) property. Optional [resolvedImage](../types/#resolvedimage). Transitionable.

Name of image in sprite to use for drawing an image background. For seamless patterns, image width and height must be a factor of two (2, 4, 8, ..., 512). Note that zoom-dependent expressions will be evaluated only at integer zoom levels.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | Not yet supported | Not yet supported | Not yet supported | Not yet supported |

### visibility

[Layout](#layout-property) property. Optional [enum](../types/#enum). One of `"visible"`, `"none"`. Defaults to `"visible"`.

Whether this layer is displayed.

`"visible"`:

The layer is shown.

`"none"`:

The layer is not shown.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

## [fill](#fill)

A `fill` style layer renders one or more filled (and optionally stroked) polygons on a map. You can use a fill layer to configure the visual appearance of polygon or multipolygon features.



This [map of Rio de Janeiro](/sdk-js/examples/geojson-polygon/) uses the [`fill-opacity`](#fill-opacity) paint property to render a semi-transparent polygon.

### fill-antialias

[Paint](#paint-property) property. Optional [boolean](../types/#boolean). Defaults to `true`.

Whether or not the fill should be antialiased.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

### fill-color

[Paint](#paint-property) property. Optional [color](../types/#color). Defaults to `"#000000"`. _Disabled by_ fill-pattern. Supports _[`feature-state`](../expressions/#feature-state)_ and [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

The color of the filled part of this layer. This color can be specified as `rgba` with an alpha component and the color's opacity will not affect the opacity of the 1px stroke, if it is used.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | >= 0.19.0 | >= 5.0.0 | >= 3.5.0 | >= 0.4.0 |

### fill-opacity

[Paint](#paint-property) property. Optional [number](../types/#number) between `0` and `1` inclusive. Defaults to `1`. Supports _[`feature-state`](../expressions/#feature-state)_ and [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

The opacity of the entire fill layer. In contrast to the `fill-color`, this value will also affect the 1px stroke around the fill, if the stroke is used.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | >= 0.21.0 | >= 5.0.0 | >= 3.5.0 | >= 0.4.0 |

### fill-outline-color

[Paint](#paint-property) property. Optional [color](../types/#color). _Disabled by_ fill-pattern. _Requires_ fill-antialias to be `true`. Supports _[`feature-state`](../expressions/#feature-state)_ and [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

The outline color of the fill. Matches the value of `fill-color` if unspecified.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | >= 0.19.0 | >= 5.0.0 | >= 3.5.0 | >= 0.4.0 |

### fill-pattern

[Paint](#paint-property) property. Optional [resolvedImage](../types/#resolvedimage). Transitionable.

Name of image in sprite to use for drawing image fills. For seamless patterns, image width and height must be a factor of two (2, 4, 8, ..., 512). Note that zoom-dependent expressions will be evaluated only at integer zoom levels.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | >= 0.49.0 | >= 6.5.0 | >= 4.4.0 | >= 0.11.0 |

### fill-sort-key

[Layout](#layout-property) property. Optional [number](../types/#number).

Sorts features in ascending order based on this value. Features with a higher sort key will appear above features with a lower sort key.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 1.2.0 | >= 9.1.0 | >= 5.8.0 | >= 0.15.0 |
| data-driven styling | >= 1.2.0 | >= 9.1.0 | >= 5.8.0 | >= 0.15.0 |

### fill-translate

[Paint](#paint-property) property. Optional [array](../types/#array) of [numbers](../types/#number). Units in pixels. Defaults to `[0,0]`. Supports [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

The geometry's offset. Values are \[x, y\] where negatives indicate left and up, respectively.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

### fill-translate-anchor

[Paint](#paint-property) property. Optional [enum](../types/#enum). One of `"map"`, `"viewport"`. Defaults to `"map"`. _Requires_ fill-translate.

Controls the frame of reference for `fill-translate`.

`"map"`:

The fill is translated relative to the map.

`"viewport"`:

The fill is translated relative to the viewport.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

### visibility

[Layout](#layout-property) property. Optional [enum](../types/#enum). One of `"visible"`, `"none"`. Defaults to `"visible"`.

Whether this layer is displayed.

`"visible"`:

The layer is shown.

`"none"`:

The layer is not shown.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

## [line](#line)

A `line` style layer renders one or more stroked polylines on the map. You can use a line layer to configure the visual appearance of polyline or multipolyline features.



This [hiking map through Grand Teton National Park](/sdk-js/examples/geojson-line/) uses the [`line-color`](#line-color) and [`line-width`](#line-width) paint properties to style the strong red line of the user's route.

### line-blur

[Paint](#paint-property) property. Optional [number](../types/#number) greater than or equal to `0`. Units in pixels. Defaults to `0`. Supports _[`feature-state`](../expressions/#feature-state)_ and [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

Blur applied to the line, in pixels.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | >= 0.29.0 | >= 5.0.0 | >= 3.5.0 | >= 0.4.0 |

### line-cap

[Layout](#layout-property) property. Optional [enum](../types/#enum). One of `"butt"`, `"round"`, `"square"`. Defaults to `"butt"`.

The display of line endings.

`"butt"`:

A cap with a squared-off end which is drawn to the exact endpoint of the line.

`"round"`:

A cap with a rounded end which is drawn beyond the endpoint of the line at a radius of one-half of the line's width and centered on the endpoint of the line.

`"square"`:

A cap with a squared-off end which is drawn beyond the endpoint of the line at a distance of one-half of the line's width.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

### line-color

[Paint](#paint-property) property. Optional [color](../types/#color). Defaults to `"#000000"`. _Disabled by_ line-pattern. Supports _[`feature-state`](../expressions/#feature-state)_ and [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

The color with which the line will be drawn.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | >= 0.23.0 | >= 5.0.0 | >= 3.5.0 | >= 0.4.0 |

### line-dasharray

[Paint](#paint-property) property. Optional [array](../types/#array) of [numbers](../types/#number) greater than or equal to `0`. Units in line widths. _Disabled by_ line-pattern. Transitionable.

Specifies the lengths of the alternating dashes and gaps that form the dash pattern. The lengths are later scaled by the line width. To convert a dash length to pixels, multiply the length by the current line width. Note that GeoJSON sources with `lineMetrics: true` specified won't render dashed lines to the expected scale. Also note that zoom-dependent expressions will be evaluated only at integer zoom levels.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | Not yet supported | Not yet supported | Not yet supported | Not yet supported |

### line-gap-width

[Paint](#paint-property) property. Optional [number](../types/#number) greater than or equal to `0`. Units in pixels. Defaults to `0`. Supports _[`feature-state`](../expressions/#feature-state)_ and [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

Draws a line casing outside of a line's actual path. Value indicates the width of the inner gap.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | >= 0.29.0 | >= 5.0.0 | >= 3.5.0 | >= 0.4.0 |

### line-gradient

[Paint](#paint-property) property. Optional [color](../types/#color). _Disabled by_ line-dasharray. _Disabled by_ line-pattern. _Requires_ source to be `"geojson"`. Supports [`interpolate`](../expressions/#interpolate)expressions.

Defines a gradient with which to color a line feature. Can only be used with GeoJSON sources that specify `"lineMetrics": true`.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.45.0 | >= 6.5.0 | >= 4.4.0 | >= 0.11.0 |
| data-driven styling | Not yet supported | Not yet supported | Not yet supported | Not yet supported |

### line-join

[Layout](#layout-property) property. Optional [enum](../types/#enum). One of `"bevel"`, `"round"`, `"miter"`. Defaults to `"miter"`.

The display of lines when joining.

`"bevel"`:

A join with a squared-off end which is drawn beyond the endpoint of the line at a distance of one-half of the line's width.

`"round"`:

A join with a rounded end which is drawn beyond the endpoint of the line at a radius of one-half of the line's width and centered on the endpoint of the line.

`"miter"`:

A join with a sharp, angled corner which is drawn with the outer sides beyond the endpoint of the path until they meet.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | >= 0.40.0 | >= 5.2.0 | >= 3.7.0 | >= 0.6.0 |

### line-miter-limit

[Layout](#layout-property) property. Optional [number](../types/#number). Defaults to `2`. _Requires_ line-join to be `"miter"`. Supports [`interpolate`](../expressions/#interpolate)expressions.

Used to automatically convert miter joins to bevel joins for sharp angles.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

### line-offset

[Paint](#paint-property) property. Optional [number](../types/#number). Units in pixels. Defaults to `0`. Supports _[`feature-state`](../expressions/#feature-state)_ and [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

The line's offset. For linear features, a positive value offsets the line to the right, relative to the direction of the line, and a negative value to the left. For polygon features, a positive value results in an inset, and a negative value results in an outset.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.12.0 | >= 3.0.0 | >= 3.1.0 | >= 0.1.0 |
| data-driven styling | >= 0.29.0 | >= 5.0.0 | >= 3.5.0 | >= 0.4.0 |

### line-opacity

[Paint](#paint-property) property. Optional [number](../types/#number) between `0` and `1` inclusive. Defaults to `1`. Supports _[`feature-state`](../expressions/#feature-state)_ and [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

The opacity at which the line will be drawn.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | >= 0.29.0 | >= 5.0.0 | >= 3.5.0 | >= 0.4.0 |

### line-pattern

[Paint](#paint-property) property. Optional [resolvedImage](../types/#resolvedimage). Transitionable.

Name of image in sprite to use for drawing image lines. For seamless patterns, image width must be a factor of two (2, 4, 8, ..., 512). Note that zoom-dependent expressions will be evaluated only at integer zoom levels.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | >= 0.49.0 | >= 6.5.0 | >= 4.4.0 | >= 0.11.0 |

### line-round-limit

[Layout](#layout-property) property. Optional [number](../types/#number). Defaults to `1.05`. _Requires_ line-join to be `"round"`. Supports [`interpolate`](../expressions/#interpolate)expressions.

Used to automatically convert round joins to miter joins for shallow angles.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

### line-sort-key

[Layout](#layout-property) property. Optional [number](../types/#number).

Sorts features in ascending order based on this value. Features with a higher sort key will appear above features with a lower sort key.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 1.2.0 | >= 9.1.0 | >= 5.8.0 | >= 0.15.0 |
| data-driven styling | >= 1.2.0 | >= 9.1.0 | >= 5.8.0 | >= 0.15.0 |

### line-translate

[Paint](#paint-property) property. Optional [array](../types/#array) of [numbers](../types/#number). Units in pixels. Defaults to `[0,0]`. Supports [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

The geometry's offset. Values are \[x, y\] where negatives indicate left and up, respectively.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

### line-translate-anchor

[Paint](#paint-property) property. Optional [enum](../types/#enum). One of `"map"`, `"viewport"`. Defaults to `"map"`. _Requires_ line-translate.

Controls the frame of reference for `line-translate`.

`"map"`:

The line is translated relative to the map.

`"viewport"`:

The line is translated relative to the viewport.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

### line-width

[Paint](#paint-property) property. Optional [number](../types/#number) greater than or equal to `0`. Units in pixels. Defaults to `1`. Supports _[`feature-state`](../expressions/#feature-state)_ and [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

Stroke thickness.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | >= 0.39.0 | >= 5.2.0 | >= 3.7.0 | >= 0.6.0 |

### visibility

[Layout](#layout-property) property. Optional [enum](../types/#enum). One of `"visible"`, `"none"`. Defaults to `"visible"`.

Whether this layer is displayed.

`"visible"`:

The layer is shown.

`"none"`:

The layer is not shown.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

## [symbol](#symbol)

A `symbol` style layer renders icon and text labels at points or along lines on a map. You can use a symbol layer to configure the visual appearance of labels for features in vector tiles.



This [map of Airports](/sdk-js/examples/geojson-point/) uses the [`icon-image`](#icon-image) layout property to use a custom image as an icon in a symbol layer.

### icon-allow-overlap

[Layout](#layout-property) property. Optional [boolean](../types/#boolean). Defaults to `false`. _Requires_ icon-image.

If true, the icon will be visible even if it collides with other previously drawn symbols.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

### icon-anchor

[Layout](#layout-property) property. Optional [enum](../types/#enum). One of `"center"`, `"left"`, `"right"`, `"top"`, `"bottom"`, `"top-left"`, `"top-right"`, `"bottom-left"`, `"bottom-right"`. Defaults to `"center"`. _Requires_ icon-image.

Part of the icon placed closest to the anchor.

`"center"`:

The center of the icon is placed closest to the anchor.

`"left"`:

The left side of the icon is placed closest to the anchor.

`"right"`:

The right side of the icon is placed closest to the anchor.

`"top"`:

The top of the icon is placed closest to the anchor.

`"bottom"`:

The bottom of the icon is placed closest to the anchor.

`"top-left"`:

The top left corner of the icon is placed closest to the anchor.

`"top-right"`:

The top right corner of the icon is placed closest to the anchor.

`"bottom-left"`:

The bottom left corner of the icon is placed closest to the anchor.

`"bottom-right"`:

The bottom right corner of the icon is placed closest to the anchor.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.40.0 | >= 5.2.0 | >= 3.7.0 | >= 0.6.0 |
| data-driven styling | >= 0.40.0 | >= 5.2.0 | >= 3.7.0 | >= 0.6.0 |

### icon-color

[Paint](#paint-property) property. Optional [color](../types/#color). Defaults to `"#000000"`. _Requires_ icon-image. Supports _[`feature-state`](../expressions/#feature-state)_ and [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

The color of the icon. This can only be used with sdf icons.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | >= 0.33.0 | >= 5.0.0 | >= 3.5.0 | >= 0.4.0 |

### icon-halo-blur

[Paint](#paint-property) property. Optional [number](../types/#number) greater than or equal to `0`. Units in pixels. Defaults to `0`. _Requires_ icon-image. Supports _[`feature-state`](../expressions/#feature-state)_ and [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

Fade out the halo towards the outside.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | >= 0.33.0 | >= 5.0.0 | >= 3.5.0 | >= 0.4.0 |

### icon-halo-color

[Paint](#paint-property) property. Optional [color](../types/#color). Defaults to `"rgba(0, 0, 0, 0)"`. _Requires_ icon-image. Supports _[`feature-state`](../expressions/#feature-state)_ and [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

The color of the icon's halo. Icon halos can only be used with SDF icons.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | >= 0.33.0 | >= 5.0.0 | >= 3.5.0 | >= 0.4.0 |

### icon-halo-width

[Paint](#paint-property) property. Optional [number](../types/#number) greater than or equal to `0`. Units in pixels. Defaults to `0`. _Requires_ icon-image. Supports _[`feature-state`](../expressions/#feature-state)_ and [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

Distance of halo to the icon outline.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | >= 0.33.0 | >= 5.0.0 | >= 3.5.0 | >= 0.4.0 |

### icon-ignore-placement

[Layout](#layout-property) property. Optional [boolean](../types/#boolean). Defaults to `false`. _Requires_ icon-image.

If true, other symbols can be visible even if they collide with the icon.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

### icon-image

[Layout](#layout-property) property. Optional [resolvedImage](../types/#resolvedimage).

Name of image in sprite to use for drawing an image background.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | >= 0.35.0 | >= 5.1.0 | >= 3.6.0 | >= 0.5.0 |

### icon-keep-upright

[Layout](#layout-property) property. Optional [boolean](../types/#boolean). Defaults to `false`. _Requires_ icon-image. _Requires_ icon-rotation-alignment to be `"map"`. _Requires_ symbol-placement to be `"line"`, or `"line-center"`.

If true, the icon may be flipped to prevent it from being rendered upside-down.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

### icon-offset

[Layout](#layout-property) property. Optional [array](../types/#array) of [numbers](../types/#number). Defaults to `[0,0]`. _Requires_ icon-image. Supports [`interpolate`](../expressions/#interpolate)expressions.

Offset distance of icon from its anchor. Positive values indicate right and down, while negative values indicate left and up. Each component is multiplied by the value of `icon-size` to obtain the final offset in pixels. When combined with `icon-rotate` the offset will be as if the rotated direction was up.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | >= 0.29.0 | >= 5.0.0 | >= 3.5.0 | >= 0.4.0 |

### icon-opacity

[Paint](#paint-property) property. Optional [number](../types/#number) between `0` and `1` inclusive. Defaults to `1`. _Requires_ icon-image. Supports _[`feature-state`](../expressions/#feature-state)_ and [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

The opacity at which the icon will be drawn.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | >= 0.33.0 | >= 5.0.0 | >= 3.5.0 | >= 0.4.0 |

### icon-optional

[Layout](#layout-property) property. Optional [boolean](../types/#boolean). Defaults to `false`. _Requires_ icon-image. _Requires_ text-field.

If true, text will display without their corresponding icons when the icon collides with other symbols and the text does not.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

### icon-padding

[Layout](#layout-property) property. Optional [number](../types/#number) greater than or equal to `0`. Units in pixels. Defaults to `2`. _Requires_ icon-image. Supports [`interpolate`](../expressions/#interpolate)expressions.

Size of the additional area around the icon bounding box used for detecting symbol collisions.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

### icon-pitch-alignment

[Layout](#layout-property) property. Optional [enum](../types/#enum). One of `"map"`, `"viewport"`, `"auto"`. Defaults to `"auto"`. _Requires_ icon-image.

Orientation of icon when map is pitched.

`"map"`:

The icon is aligned to the plane of the map.

`"viewport"`:

The icon is aligned to the plane of the viewport.

`"auto"`:

Automatically matches the value of `icon-rotation-alignment`.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.39.0 | >= 5.2.1 | >= 3.7.0 | >= 0.6.0 |

### icon-rotate

[Layout](#layout-property) property. Optional [number](../types/#number). Units in degrees. Defaults to `0`. _Requires_ icon-image. Supports [`interpolate`](../expressions/#interpolate)expressions.

Rotates the icon clockwise.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | >= 0.21.0 | >= 5.0.0 | >= 3.5.0 | >= 0.4.0 |

### icon-rotation-alignment

[Layout](#layout-property) property. Optional [enum](../types/#enum). One of `"map"`, `"viewport"`, `"auto"`. Defaults to `"auto"`. _Requires_ icon-image.

In combination with `symbol-placement`, determines the rotation behavior of icons.

`"map"`:

When `symbol-placement` is set to `point`, aligns icons east-west. When `symbol-placement` is set to `line` or `line-center`, aligns icon x-axes with the line.

`"viewport"`:

Produces icons whose x-axes are aligned with the x-axis of the viewport, regardless of the value of `symbol-placement`.

`"auto"`:

When `symbol-placement` is set to `point`, this is equivalent to `viewport`. When `symbol-placement` is set to `line` or `line-center`, this is equivalent to `map`.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| <code class="language-plaintext">auto</code> value | >= 0.25.0 | >= 4.2.0 | >= 3.4.0 | >= 0.3.0 |

### icon-size

[Layout](#layout-property) property. Optional [number](../types/#number) greater than or equal to `0`. Units in factor of the original icon size. Defaults to `1`. _Requires_ icon-image. Supports [`interpolate`](../expressions/#interpolate)expressions.

Scales the original size of the icon by the provided factor. The new pixel size of the image will be the original pixel size multiplied by `icon-size`. 1 is the original size; 3 triples the size of the image.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | >= 0.35.0 | >= 5.1.0 | >= 3.6.0 | >= 0.5.0 |

### icon-text-fit

[Layout](#layout-property) property. Optional [enum](../types/#enum). One of `"none"`, `"width"`, `"height"`, `"both"`. Defaults to `"none"`. _Requires_ icon-image. _Requires_ text-field.

Scales the icon to fit around the associated text.

`"none"`:

The icon is displayed at its intrinsic aspect ratio.

`"width"`:

The icon is scaled in the x-dimension to fit the width of the text.

`"height"`:

The icon is scaled in the y-dimension to fit the height of the text.

`"both"`:

The icon is scaled in both x- and y-dimensions.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.21.0 | >= 4.2.0 | >= 3.4.0 | >= 0.2.1 |
| stretchable icons | >= 1.6.0 | >= 9.2.0 | >= 5.8.0 | >= 0.15.0 |

### icon-text-fit-padding

[Layout](#layout-property) property. Optional [array](../types/#array) of [numbers](../types/#number). Units in pixels. Defaults to `[0,0,0,0]`. _Requires_ icon-image. _Requires_ text-field. _Requires_ icon-text-fit to be `"both"`, or `"width"`, or `"height"`. Supports [`interpolate`](../expressions/#interpolate)expressions.

Size of the additional area added to dimensions determined by `icon-text-fit`, in clockwise order: top, right, bottom, left.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.21.0 | >= 4.2.0 | >= 3.4.0 | >= 0.2.1 |

### icon-translate

[Paint](#paint-property) property. Optional [array](../types/#array) of [numbers](../types/#number). Units in pixels. Defaults to `[0,0]`. _Requires_ icon-image. Supports [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

Distance that the icon's anchor is moved from its original placement. Positive values indicate right and down, while negative values indicate left and up.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

### icon-translate-anchor

[Paint](#paint-property) property. Optional [enum](../types/#enum). One of `"map"`, `"viewport"`. Defaults to `"map"`. _Requires_ icon-image. _Requires_ icon-translate.

Controls the frame of reference for `icon-translate`.

`"map"`:

Icons are translated relative to the map.

`"viewport"`:

Icons are translated relative to the viewport.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

### symbol-avoid-edges

[Layout](#layout-property) property. Optional [boolean](../types/#boolean). Defaults to `false`.

If true, the symbols will not cross tile edges to avoid mutual collisions. Recommended in layers that don't have enough padding in the vector tile to prevent collisions, or if it is a point symbol layer placed after a line symbol layer. When using a client that supports global collision detection, like MapLibre GL JS version 0.42.0 or greater, enabling this property is not needed to prevent clipped labels at tile boundaries.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

### symbol-placement

[Layout](#layout-property) property. Optional [enum](../types/#enum). One of `"point"`, `"line"`, `"line-center"`. Defaults to `"point"`.

Label placement relative to its geometry.

`"point"`:

The label is placed at the point where the geometry is located.

`"line"`:

The label is placed along the line of the geometry. Can only be used on `LineString` and `Polygon` geometries.

`"line-center"`:

The label is placed at the center of the line of the geometry. Can only be used on `LineString` and `Polygon` geometries. Note that a single feature in a vector tile may contain multiple line geometries.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| <code class="language-plaintext">line-center</code> value | >= 0.47.0 | >= 6.4.0 | >= 4.3.0 | >= 0.10.0 |

### symbol-sort-key

[Layout](#layout-property) property. Optional [number](../types/#number).

Sorts features in ascending order based on this value. Features with lower sort keys are drawn and placed first. When `icon-allow-overlap` or `text-allow-overlap` is `false`, features with a lower sort key will have priority during placement. When `icon-allow-overlap` or `text-allow-overlap` is set to `true`, features with a higher sort key will overlap over features with a lower sort key.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.53.0 | >= 7.4.0 | >= 4.11.0 | >= 0.14.0 |
| data-driven styling | >= 0.53.0 | >= 7.4.0 | >= 4.11.0 | >= 0.14.0 |

### symbol-spacing

[Layout](#layout-property) property. Optional [number](../types/#number) greater than or equal to `1`. Units in pixels. Defaults to `250`. _Requires_ symbol-placement to be `"line"`. Supports [`interpolate`](../expressions/#interpolate)expressions.

Distance between two symbol anchors.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

### symbol-z-order

[Layout](#layout-property) property. Optional [enum](../types/#enum). One of `"auto"`, `"viewport-y"`, `"source"`. Defaults to `"auto"`.

Determines whether overlapping symbols in the same layer are rendered in the order that they appear in the data source or by their y-position relative to the viewport. To control the order and prioritization of symbols otherwise, use `symbol-sort-key`.

`"auto"`:

Sorts symbols by `symbol-sort-key` if set. Otherwise, sorts symbols by their y-position relative to the viewport if `icon-allow-overlap` or `text-allow-overlap` is set to `true` or `icon-ignore-placement` or `text-ignore-placement` is `false`.

`"viewport-y"`:

Sorts symbols by their y-position relative to the viewport if `icon-allow-overlap` or `text-allow-overlap` is set to `true` or `icon-ignore-placement` or `text-ignore-placement` is `false`.

`"source"`:

Sorts symbols by `symbol-sort-key` if set. Otherwise, no sorting is applied; symbols are rendered in the same order as the source data.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.49.0 | >= 6.6.0 | >= 4.5.0 | >= 0.12.0 |

### text-allow-overlap

[Layout](#layout-property) property. Optional [boolean](../types/#boolean). Defaults to `false`. _Requires_ text-field.

If true, the text will be visible even if it collides with other previously drawn symbols.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

### text-anchor

[Layout](#layout-property) property. Optional [enum](../types/#enum). One of `"center"`, `"left"`, `"right"`, `"top"`, `"bottom"`, `"top-left"`, `"top-right"`, `"bottom-left"`, `"bottom-right"`. Defaults to `"center"`. _Requires_ text-field. _Disabled by_ text-variable-anchor.

Part of the text placed closest to the anchor.

`"center"`:

The center of the text is placed closest to the anchor.

`"left"`:

The left side of the text is placed closest to the anchor.

`"right"`:

The right side of the text is placed closest to the anchor.

`"top"`:

The top of the text is placed closest to the anchor.

`"bottom"`:

The bottom of the text is placed closest to the anchor.

`"top-left"`:

The top left corner of the text is placed closest to the anchor.

`"top-right"`:

The top right corner of the text is placed closest to the anchor.

`"bottom-left"`:

The bottom left corner of the text is placed closest to the anchor.

`"bottom-right"`:

The bottom right corner of the text is placed closest to the anchor.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | >= 0.39.0 | >= 5.2.0 | >= 3.7.0 | >= 0.6.0 |

### text-color

[Paint](#paint-property) property. Optional [color](../types/#color). Defaults to `"#000000"`. _Requires_ text-field. Supports _[`feature-state`](../expressions/#feature-state)_ and [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

The color with which the text will be drawn.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | >= 0.33.0 | >= 5.0.0 | >= 3.5.0 | >= 0.4.0 |

### text-field

[Layout](#layout-property) property. Optional [formatted](../types/#formatted). Defaults to `""`.

Value to use for a text label. If a plain `string` is provided, it will be treated as a `formatted` with default/inherited formatting options.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | >= 0.33.0 | >= 5.0.0 | >= 3.5.0 | >= 0.4.0 |

### text-font

[Layout](#layout-property) property. Optional [array](../types/#array) of [strings](../types/#string). Defaults to `["Open Sans Regular","Arial Unicode MS Regular"]`. _Requires_ text-field.

Font stack to use for displaying text.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | >= 0.43.0 | >= 6.0.0 | >= 4.0.0 | >= 0.7.0 |

### text-halo-blur

[Paint](#paint-property) property. Optional [number](../types/#number) greater than or equal to `0`. Units in pixels. Defaults to `0`. _Requires_ text-field. Supports _[`feature-state`](../expressions/#feature-state)_ and [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

The halo's fadeout distance towards the outside.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | >= 0.33.0 | >= 5.0.0 | >= 3.5.0 | >= 0.4.0 |

### text-halo-color

[Paint](#paint-property) property. Optional [color](../types/#color). Defaults to `"rgba(0, 0, 0, 0)"`. _Requires_ text-field. Supports _[`feature-state`](../expressions/#feature-state)_ and [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

The color of the text's halo, which helps it stand out from backgrounds.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | >= 0.33.0 | >= 5.0.0 | >= 3.5.0 | >= 0.4.0 |

### text-halo-width

[Paint](#paint-property) property. Optional [number](../types/#number) greater than or equal to `0`. Units in pixels. Defaults to `0`. _Requires_ text-field. Supports _[`feature-state`](../expressions/#feature-state)_ and [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

Distance of halo to the font outline. Max text halo width is 1/4 of the font-size.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | >= 0.33.0 | >= 5.0.0 | >= 3.5.0 | >= 0.4.0 |

### text-ignore-placement

[Layout](#layout-property) property. Optional [boolean](../types/#boolean). Defaults to `false`. _Requires_ text-field.

If true, other symbols can be visible even if they collide with the text.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

### text-justify

[Layout](#layout-property) property. Optional [enum](../types/#enum). One of `"auto"`, `"left"`, `"center"`, `"right"`. Defaults to `"center"`. _Requires_ text-field.

Text justification options.

`"auto"`:

The text is aligned towards the anchor position.

`"left"`:

The text is aligned to the left.

`"center"`:

The text is centered.

`"right"`:

The text is aligned to the right.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.39.0 | >= 5.2.0 | >= 3.7.0 | >= 0.6.0 |
| <code class="language-plaintext">auto</code> value | >= 0.54.0 | >= 7.4.0 | >= 4.10.0 | >= 0.14.0 |

### text-keep-upright

[Layout](#layout-property) property. Optional [boolean](../types/#boolean). Defaults to `true`. _Requires_ text-field. _Requires_ text-rotation-alignment to be `"map"`. _Requires_ symbol-placement to be `"line"`, or `"line-center"`.

If true, the text may be flipped vertically to prevent it from being rendered upside-down.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

### text-letter-spacing

[Layout](#layout-property) property. Optional [number](../types/#number). Units in ems. Defaults to `0`. _Requires_ text-field. Supports [`interpolate`](../expressions/#interpolate)expressions.

Text tracking amount.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | >= 0.40.0 | >= 5.2.0 | >= 3.7.0 | >= 0.6.0 |

### text-line-height

[Layout](#layout-property) property. Optional [number](../types/#number). Units in ems. Defaults to `1.2`. _Requires_ text-field. Supports [`interpolate`](../expressions/#interpolate)expressions.

Text leading value for multi-line text.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

### text-max-angle

[Layout](#layout-property) property. Optional [number](../types/#number). Units in degrees. Defaults to `45`. _Requires_ text-field. _Requires_ symbol-placement to be `"line"`, or `"line-center"`. Supports [`interpolate`](../expressions/#interpolate)expressions.

Maximum angle change between adjacent characters.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

### text-max-width

[Layout](#layout-property) property. Optional [number](../types/#number) greater than or equal to `0`. Units in ems. Defaults to `10`. _Requires_ text-field. Supports [`interpolate`](../expressions/#interpolate)expressions.

The maximum line width for text wrapping.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | >= 0.40.0 | >= 5.2.0 | >= 3.7.0 | >= 0.6.0 |

### text-offset

[Layout](#layout-property) property. Optional [array](../types/#array) of [numbers](../types/#number). Units in ems. Defaults to `[0,0]`. _Requires_ text-field. _Disabled by_ text-radial-offset. Supports [`interpolate`](../expressions/#interpolate)expressions.

Offset distance of text from its anchor. Positive values indicate right and down, while negative values indicate left and up. If used with text-variable-anchor, input values will be taken as absolute values. Offsets along the x- and y-axis will be applied automatically based on the anchor position.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | >= 0.35.0 | >= 5.1.0 | >= 3.6.0 | >= 0.5.0 |

### text-opacity

[Paint](#paint-property) property. Optional [number](../types/#number) between `0` and `1` inclusive. Defaults to `1`. _Requires_ text-field. Supports _[`feature-state`](../expressions/#feature-state)_ and [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

The opacity at which the text will be drawn.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | >= 0.33.0 | >= 5.0.0 | >= 3.5.0 | >= 0.4.0 |

### text-optional

[Layout](#layout-property) property. Optional [boolean](../types/#boolean). Defaults to `false`. _Requires_ text-field. _Requires_ icon-image.

If true, icons will display without their corresponding text when the text collides with other symbols and the icon does not.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

### text-padding

[Layout](#layout-property) property. Optional [number](../types/#number) greater than or equal to `0`. Units in pixels. Defaults to `2`. _Requires_ text-field. Supports [`interpolate`](../expressions/#interpolate)expressions.

Size of the additional area around the text bounding box used for detecting symbol collisions.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

### text-pitch-alignment

[Layout](#layout-property) property. Optional [enum](../types/#enum). One of `"map"`, `"viewport"`, `"auto"`. Defaults to `"auto"`. _Requires_ text-field.

Orientation of text when map is pitched.

`"map"`:

The text is aligned to the plane of the map.

`"viewport"`:

The text is aligned to the plane of the viewport.

`"auto"`:

Automatically matches the value of `text-rotation-alignment`.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.21.0 | >= 4.2.0 | >= 3.4.0 | >= 0.2.1 |
| <code class="language-plaintext">auto</code> value | >= 0.25.0 | >= 4.2.0 | >= 3.4.0 | >= 0.3.0 |

### text-radial-offset

[Layout](#layout-property) property. Optional [number](../types/#number). Units in ems. Defaults to `0`. _Requires_ text-field. Supports [`interpolate`](../expressions/#interpolate)expressions.

Radial offset of text, in the direction of the symbol's anchor. Useful in combination with `text-variable-anchor`, which defaults to using the two-dimensional `text-offset` if present.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.54.0 | >= 7.4.0 | >= 4.10.0 | >= 0.14.0 |
| data-driven styling | >= 0.54.0 | >= 7.4.0 | >= 4.10.0 | >= 0.14.0 |

### text-rotate

[Layout](#layout-property) property. Optional [number](../types/#number). Units in degrees. Defaults to `0`. _Requires_ text-field. Supports [`interpolate`](../expressions/#interpolate)expressions.

Rotates the text clockwise.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | >= 0.35.0 | >= 5.1.0 | >= 3.6.0 | >= 0.5.0 |

### text-rotation-alignment

[Layout](#layout-property) property. Optional [enum](../types/#enum). One of `"map"`, `"viewport"`, `"auto"`. Defaults to `"auto"`. _Requires_ text-field.

In combination with `symbol-placement`, determines the rotation behavior of the individual glyphs forming the text.

`"map"`:

When `symbol-placement` is set to `point`, aligns text east-west. When `symbol-placement` is set to `line` or `line-center`, aligns text x-axes with the line.

`"viewport"`:

Produces glyphs whose x-axes are aligned with the x-axis of the viewport, regardless of the value of `symbol-placement`.

`"auto"`:

When `symbol-placement` is set to `point`, this is equivalent to `viewport`. When `symbol-placement` is set to `line` or `line-center`, this is equivalent to `map`.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| <code class="language-plaintext">auto</code> value | >= 0.25.0 | >= 4.2.1 | >= 3.4.0 | >= 0.3.0 |

### text-size

[Layout](#layout-property) property. Optional [number](../types/#number) greater than or equal to `0`. Units in pixels. Defaults to `16`. _Requires_ text-field. Supports [`interpolate`](../expressions/#interpolate)expressions.

Font size.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | >= 0.35.0 | >= 5.1.0 | >= 3.6.0 | >= 0.5.0 |

### text-transform

[Layout](#layout-property) property. Optional [enum](../types/#enum). One of `"none"`, `"uppercase"`, `"lowercase"`. Defaults to `"none"`. _Requires_ text-field.

Specifies how to capitalize text, similar to the CSS `text-transform` property.

`"none"`:

The text is not altered.

`"uppercase"`:

Forces all letters to be displayed in uppercase.

`"lowercase"`:

Forces all letters to be displayed in lowercase.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | >= 0.33.0 | >= 5.0.0 | >= 3.5.0 | >= 0.4.0 |

### text-translate

[Paint](#paint-property) property. Optional [array](../types/#array) of [numbers](../types/#number). Units in pixels. Defaults to `[0,0]`. _Requires_ text-field. Supports [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

Distance that the text's anchor is moved from its original placement. Positive values indicate right and down, while negative values indicate left and up.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

### text-translate-anchor

[Paint](#paint-property) property. Optional [enum](../types/#enum). One of `"map"`, `"viewport"`. Defaults to `"map"`. _Requires_ text-field. _Requires_ text-translate.

Controls the frame of reference for `text-translate`.

`"map"`:

The text is translated relative to the map.

`"viewport"`:

The text is translated relative to the viewport.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

### text-variable-anchor

[Layout](#layout-property) property. Optional [array](../types/#array) of [enums](../types/#enum). One of `"center"`, `"left"`, `"right"`, `"top"`, `"bottom"`, `"top-left"`, `"top-right"`, `"bottom-left"`, `"bottom-right"`. _Requires_ text-field. _Requires_ symbol-placement to be `"point"`.

To increase the chance of placing high-priority labels on the map, you can provide an array of `text-anchor` locations: the renderer will attempt to place the label at each location, in order, before moving onto the next label. Use `text-justify: auto` to choose justification based on anchor position. To apply an offset, use the `text-radial-offset` or the two-dimensional `text-offset`.

`"center"`:

The center of the text is placed closest to the anchor.

`"left"`:

The left side of the text is placed closest to the anchor.

`"right"`:

The right side of the text is placed closest to the anchor.

`"top"`:

The top of the text is placed closest to the anchor.

`"bottom"`:

The bottom of the text is placed closest to the anchor.

`"top-left"`:

The top left corner of the text is placed closest to the anchor.

`"top-right"`:

The top right corner of the text is placed closest to the anchor.

`"bottom-left"`:

The bottom left corner of the text is placed closest to the anchor.

`"bottom-right"`:

The bottom right corner of the text is placed closest to the anchor.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.54.0 | >= 7.4.0 | >= 4.10.0 | >= 0.14.0 |

### text-writing-mode

[Layout](#layout-property) property. Optional [array](../types/#array) of [enums](../types/#enum). One of `"horizontal"`, `"vertical"`. _Requires_ text-field. _Requires_ symbol-placement to be `"point"`.

The property allows control over a symbol's orientation. Note that the property values act as a hint, so that a symbol whose language doesn’t support the provided orientation will be laid out in its natural orientation. Example: English point symbol will be rendered horizontally even if array value contains single 'vertical' enum value. The order of elements in an array define priority order for the placement of an orientation variant.

`"horizontal"`:

If a text's language supports horizontal writing mode, symbols with point placement would be laid out horizontally.

`"vertical"`:

If a text's language supports vertical writing mode, symbols with point placement would be laid out vertically.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 1.3.0 | >= 8.3.0 | >= 5.3.0 | >= 0.15.0 |

### visibility

[Layout](#layout-property) property. Optional [enum](../types/#enum). One of `"visible"`, `"none"`. Defaults to `"visible"`.

Whether this layer is displayed.

`"visible"`:

The layer is shown.

`"none"`:

The layer is not shown.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

## [raster](#raster)

A `raster` style layer renders raster tiles on a map. You can use a raster layer to configure the color parameters of raster tiles.



This [cementery map](/sdk-js/examples/raster-layer/) use the `raster-opacity` paint property to show a raster image overlay to the map.

### raster-brightness-max

[Paint](#paint-property) property. Optional [number](../types/#number) between `0` and `1` inclusive. Defaults to `1`. Supports [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

Increase or reduce the brightness of the image. The value is the maximum brightness.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

### raster-brightness-min

[Paint](#paint-property) property. Optional [number](../types/#number) between `0` and `1` inclusive. Defaults to `0`. Supports [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

Increase or reduce the brightness of the image. The value is the minimum brightness.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

### raster-contrast

[Paint](#paint-property) property. Optional [number](../types/#number) between `-1` and `1` inclusive. Defaults to `0`. Supports [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

Increase or reduce the contrast of the image.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

### raster-fade-duration

[Paint](#paint-property) property. Optional [number](../types/#number) greater than or equal to `0`. Units in milliseconds. Defaults to `300`. Supports [`interpolate`](../expressions/#interpolate)expressions.

Fade duration when a new tile is added.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

### raster-hue-rotate

[Paint](#paint-property) property. Optional [number](../types/#number). Units in degrees. Defaults to `0`. Supports [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

Rotates hues around the color wheel.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

### raster-opacity

[Paint](#paint-property) property. Optional [number](../types/#number) between `0` and `1` inclusive. Defaults to `1`. Supports [`interpolate`](../expressions/#interpolate) expressions. Transitionable.

The opacity at which the image will be drawn.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

### raster-resampling

[Paint](#paint-property) property. Optional [enum](../types/#enum). One of `"linear"`, `"nearest"`. Defaults to `"linear"`.

The resampling/interpolation method to use for overscaling, also known as texture magnification filter

`"linear"`:

(Bi)linear filtering interpolates pixel values using the weighted average of the four closest original source pixels creating a smooth but blurry look when overscaled

`"nearest"`:

Nearest neighbor filtering interpolates pixel values using the nearest original source pixel creating a sharp but pixelated look when overscaled

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.47.0 | >= 6.3.0 | >= 4.2.0 | >= 0.9.0 |

### raster-saturation

[Paint](#paint-property) property. Optional [number](../types/#number) between `-1` and `1` inclusive. Defaults to `0`. Supports [`interpolate`](../expressions/#interpolate) expressions. Transitionable.

Increase or reduce the saturation of the image.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

### visibility

[Layout](#layout-property) property. Optional [enum](../types/#enum). One of `"visible"`, `"none"`. Defaults to `"visible"`.

Whether this layer is displayed.

`"visible"`:

The layer is shown.

`"none"`:

The layer is not shown.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

## [circle](#circle)

A `circle` style layer renders one or more filled circles on a map. You can use a circle layer to configure the visual appearance of point or point collection features in vector tiles. A circle layer renders circles whose radii are measured in screen units.



This [cluster map](/sdk-js/examples/cluster/) uses a circle layer with a GeoJSON data source and sets the source's [`cluster`](../sources/#geojson-cluster) property to `true` to visualize points as clusters.

### circle-blur

[Paint](#paint-property) property. Optional [number](../types/#number). Defaults to `0`. Supports _[`feature-state`](../expressions/#feature-state)_ and [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

Amount to blur the circle. 1 blurs the circle such that only the centerpoint is full opacity.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | >= 0.20.0 | >= 5.0.0 | >= 3.5.0 | >= 0.4.0 |

### circle-color

[Paint](#paint-property) property. Optional [color](../types/#color). Defaults to `"#000000"`. Supports _[`feature-state`](../expressions/#feature-state)_ and [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

The fill color of the circle.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | >= 0.18.0 | >= 5.0.0 | >= 3.5.0 | >= 0.4.0 |

### circle-opacity

[Paint](#paint-property) property. Optional [number](../types/#number) between `0` and `1` inclusive. Defaults to `1`. Supports _[`feature-state`](../expressions/#feature-state)_ and [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

The opacity at which the circle will be drawn.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | >= 0.20.0 | >= 5.0.0 | >= 3.5.0 | >= 0.4.0 |

### circle-pitch-alignment

[Paint](#paint-property) property. Optional [enum](../types/#enum). One of `"map"`, `"viewport"`. Defaults to `"viewport"`.

Orientation of circle when map is pitched.

`"map"`:

The circle is aligned to the plane of the map.

`"viewport"`:

The circle is aligned to the plane of the viewport.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.39.0 | >= 5.2.0 | >= 3.7.0 | >= 0.6.0 |

### circle-pitch-scale

[Paint](#paint-property) property. Optional [enum](../types/#enum). One of `"map"`, `"viewport"`. Defaults to `"map"`.

Controls the scaling behavior of the circle when the map is pitched.

`"map"`:

Circles are scaled according to their apparent distance to the camera.

`"viewport"`:

Circles are not scaled.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.21.0 | >= 4.2.0 | >= 3.4.0 | >= 0.2.1 |

### circle-radius

[Paint](#paint-property) property. Optional [number](../types/#number) greater than or equal to `0`. Units in pixels. Defaults to `5`. Supports _[`feature-state`](../expressions/#feature-state)_ and [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

Circle radius.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |
| data-driven styling | >= 0.18.0 | >= 5.0.0 | >= 3.5.0 | >= 0.4.0 |

### circle-sort-key

[Layout](#layout-property) property. Optional [number](../types/#number).

Sorts features in ascending order based on this value. Features with a higher sort key will appear above features with a lower sort key.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 1.2.0 | >= 9.2.0 | >= 5.9.0 | >= 0.16.0 |
| data-driven styling | >= 1.2.0 | >= 9.2.0 | >= 5.9.0 | >= 0.16.0 |

### circle-stroke-color

[Paint](#paint-property) property. Optional [color](../types/#color). Defaults to `"#000000"`. Supports _[`feature-state`](../expressions/#feature-state)_ and [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

The stroke color of the circle.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.29.0 | >= 5.0.0 | >= 3.5.0 | >= 0.4.0 |
| data-driven styling | >= 0.29.0 | >= 5.0.0 | >= 3.5.0 | >= 0.4.0 |

### circle-stroke-opacity

[Paint](#paint-property) property. Optional [number](../types/#number) between `0` and `1` inclusive. Defaults to `1`. Supports _[`feature-state`](../expressions/#feature-state)_ and [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

The opacity of the circle's stroke.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.29.0 | >= 5.0.0 | >= 3.5.0 | >= 0.4.0 |
| data-driven styling | >= 0.29.0 | >= 5.0.0 | >= 3.5.0 | >= 0.4.0 |

### circle-stroke-width

[Paint](#paint-property) property. Optional [number](../types/#number) greater than or equal to `0`. Units in pixels. Defaults to `0`. Supports _[`feature-state`](../expressions/#feature-state)_ and [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

The width of the circle's stroke. Strokes are placed outside of the `circle-radius`.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.29.0 | >= 5.0.0 | >= 3.5.0 | >= 0.4.0 |
| data-driven styling | >= 0.29.0 | >= 5.0.0 | >= 3.5.0 | >= 0.4.0 |

### circle-translate

[Paint](#paint-property) property. Optional [array](../types/#array) of [numbers](../types/#number). Units in pixels. Defaults to `[0,0]`. Supports [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

The geometry's offset. Values are \[x, y\] where negatives indicate left and up, respectively.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

### circle-translate-anchor

[Paint](#paint-property) property. Optional [enum](../types/#enum). One of `"map"`, `"viewport"`. Defaults to `"map"`. _Requires_ circle-translate.

Controls the frame of reference for `circle-translate`.

`"map"`:

The circle is translated relative to the map.

`"viewport"`:

The circle is translated relative to the viewport.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

### visibility

[Layout](#layout-property) property. Optional [enum](../types/#enum). One of `"visible"`, `"none"`. Defaults to `"visible"`.

Whether this layer is displayed.

`"visible"`:

The layer is shown.

`"none"`:

The layer is not shown.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.10.0 | >= 2.0.1 | >= 2.0.0 | >= 0.1.0 |

## [fill-extrusion](#fill-extrusion)

A `fill-extrusion` style layer renders one or more filled (and optionally stroked) extruded (3D) polygons on a map. You can use a fill-extrusion layer to configure the extrusion and visual appearance of polygon or multipolygon features.



This [map of Europe with countries extruded](/sdk-js/examples/fill-extrusion/) uses an external dataset to provide data-driven values for the [`fill-extrusion-height`](#fill-extrusion-height) paint property of various country polygons in a fill-extrusion layer.

### fill-extrusion-base

[Paint](#paint-property) property. Optional [number](../types/#number) greater than or equal to `0`. Units in meters. Defaults to `0`. _Requires_ fill-extrusion-height. Supports _[`feature-state`](../expressions/#feature-state)_ and [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

The height with which to extrude the base of this layer. Must be less than or equal to `fill-extrusion-height`.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.27.0 | >= 5.1.0 | >= 3.6.0 | >= 0.5.0 |
| data-driven styling | >= 0.27.0 | >= 5.1.0 | >= 3.6.0 | >= 0.5.0 |

### fill-extrusion-color

[Paint](#paint-property) property. Optional [color](../types/#color). Defaults to `"#000000"`. _Disabled by_ fill-extrusion-pattern. Supports _[`feature-state`](../expressions/#feature-state)_ and [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

The base color of the extruded fill. The extrusion's surfaces will be shaded differently based on this color in combination with the root `light` settings. If this color is specified as `rgba` with an alpha component, the alpha component will be ignored; use `fill-extrusion-opacity` to set layer opacity.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.27.0 | >= 5.1.0 | >= 3.6.0 | >= 0.5.0 |
| data-driven styling | >= 0.27.0 | >= 5.1.0 | >= 3.6.0 | >= 0.5.0 |

### fill-extrusion-height

[Paint](#paint-property) property. Optional [number](../types/#number) greater than or equal to `0`. Units in meters. Defaults to `0`. Supports _[`feature-state`](../expressions/#feature-state)_ and [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

The height with which to extrude this layer.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.27.0 | >= 5.1.0 | >= 3.6.0 | >= 0.5.0 |
| data-driven styling | >= 0.27.0 | >= 5.1.0 | >= 3.6.0 | >= 0.5.0 |

### fill-extrusion-opacity

[Paint](#paint-property) property. Optional [number](../types/#number) between `0` and `1` inclusive. Defaults to `1`. Supports [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

The opacity of the entire fill extrusion layer. This is rendered on a per-layer, not per-feature, basis, and data-driven styling is not available.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.27.0 | >= 5.1.0 | >= 3.6.0 | >= 0.5.0 |

### fill-extrusion-pattern

[Paint](#paint-property) property. Optional [resolvedImage](../types/#resolvedimage). Transitionable.

Name of image in sprite to use for drawing images on extruded fills. For seamless patterns, image width and height must be a factor of two (2, 4, 8, ..., 512). Note that zoom-dependent expressions will be evaluated only at integer zoom levels.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.27.0 | >= 5.1.0 | >= 3.6.0 | >= 0.5.0 |
| data-driven styling | >= 0.49.0 | >= 6.5.0 | >= 4.4.0 | >= 0.11.0 |

### fill-extrusion-translate

[Paint](#paint-property) property. Optional [array](../types/#array) of [numbers](../types/#number). Units in pixels. Defaults to `[0,0]`. Supports [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

The geometry's offset. Values are \[x, y\] where negatives indicate left and up (on the flat plane), respectively.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.27.0 | >= 5.1.0 | >= 3.6.0 | >= 0.5.0 |

### fill-extrusion-translate-anchor

[Paint](#paint-property) property. Optional [enum](../types/#enum). One of `"map"`, `"viewport"`. Defaults to `"map"`. _Requires_ fill-extrusion-translate.

Controls the frame of reference for `fill-extrusion-translate`.

`"map"`:

The fill extrusion is translated relative to the map.

`"viewport"`:

The fill extrusion is translated relative to the viewport.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.27.0 | >= 5.1.0 | >= 3.6.0 | >= 0.5.0 |

### fill-extrusion-vertical-gradient

[Paint](#paint-property) property. Optional [boolean](../types/#boolean). Defaults to `true`.

Whether to apply a vertical gradient to the sides of a fill-extrusion layer. If true, sides will be shaded slightly darker farther down.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.50.0 | Not yet supported | >= 4.7.0 | >= 0.13.0 |
| data-driven styling | >= 0.49.0 | >= 6.5.0 | >= 4.4.0 | >= 0.11.0 |

### visibility

[Layout](#layout-property) property. Optional [enum](../types/#enum). One of `"visible"`, `"none"`. Defaults to `"visible"`.

Whether this layer is displayed.

`"visible"`:

The layer is shown.

`"none"`:

The layer is not shown.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.27.0 | >= 5.1.0 | >= 3.6.0 | >= 0.5.0 |

## [heatmap](#heatmap)

A `heatmap` style layer renders a range of colors to represent the density of points in an area.



This [visualization of earthquake data](/sdk-js/examples/heatmap-layer/) uses a heatmap layer with carefully defined [paint](#paint-property) properties to highlight areas where earthquake frequency is high and many points are clustered closely together.

### heatmap-color

[Paint](#paint-property) property. Optional [color](../types/#color). Defaults to `["interpolate",["linear"],["heatmap-density"],0,"rgba(0, 0, 255, 0)",0.1,"royalblue",0.3,"cyan",0.5,"lime",0.7,"yellow",1,"red"]`. Supports [`interpolate`](../expressions/#interpolate)expressions.

Defines the color of each pixel based on its density value in a heatmap. Should be an expression that uses `["heatmap-density"]` as input.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.41.0 | >= 6.0.0 | >= 4.0.0 | >= 0.7.0 |
| data-driven styling | Not yet supported | Not yet supported | Not yet supported | Not yet supported |

### heatmap-intensity

[Paint](#paint-property) property. Optional [number](../types/#number) greater than or equal to `0`. Defaults to `1`. Supports [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

Similar to `heatmap-weight` but controls the intensity of the heatmap globally. Primarily used for adjusting the heatmap based on zoom level.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.41.0 | >= 6.0.0 | >= 4.0.0 | >= 0.7.0 |

### heatmap-opacity

[Paint](#paint-property) property. Optional [number](../types/#number) between `0` and `1` inclusive. Defaults to `1`. Supports [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

The global opacity at which the heatmap layer will be drawn.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.41.0 | >= 6.0.0 | >= 4.0.0 | >= 0.7.0 |

### heatmap-radius

[Paint](#paint-property) property. Optional [number](../types/#number) greater than or equal to `1`. Units in pixels. Defaults to `30`. Supports _[`feature-state`](../expressions/#feature-state)_ and [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

Radius of influence of one heatmap point in pixels. Increasing the value makes the heatmap smoother, but less detailed.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.41.0 | >= 6.0.0 | >= 4.0.0 | >= 0.7.0 |
| data-driven styling | >= 0.43.0 | >= 6.0.0 | >= 4.0.0 | >= 0.7.0 |

### heatmap-weight

[Paint](#paint-property) property. Optional [number](../types/#number) greater than or equal to `0`. Defaults to `1`. Supports _[`feature-state`](../expressions/#feature-state)_ and [`interpolate`](../expressions/#interpolate)expressions.

A measure of how much an individual point contributes to the heatmap. A value of 10 would be equivalent to having 10 points of weight 1 in the same spot. Especially useful when combined with clustering.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.41.0 | >= 6.0.0 | >= 4.0.0 | >= 0.7.0 |
| data-driven styling | >= 0.41.0 | >= 6.0.0 | >= 4.0.0 | >= 0.7.0 |

### visibility

[Layout](#layout-property) property. Optional [enum](../types/#enum). One of `"visible"`, `"none"`. Defaults to `"visible"`.

Whether this layer is displayed.

`"visible"`:

The layer is shown.

`"none"`:

The layer is not shown.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.41.0 | >= 6.0.0 | >= 4.0.0 | >= 0.7.0 |

## [hillshade](#hillshade)

A `hillshade` style layer renders digital elevation model (DEM) data on the client-side. The implementation only supports Terrain RGB and Mapzen Terrarium tiles.



This [map of Mount Shasta](/sdk-js/examples/hillshade/) uses a high value for the [`hillshade-exaggeration`](#hillshade-exaggeration) paint property to apply an intense shading effect. Values of hillshading can be [adjusted dynamically](/sdk-js/examples/dynamic-hillshade/) and simulate movement of the sun.

### hillshade-accent-color

[Paint](#paint-property) property. Optional [color](../types/#color). Defaults to `"#000000"`. Supports [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

The shading color used to accentuate rugged terrain like sharp cliffs and gorges.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.43.0 | >= 6.0.0 | >= 4.0.0 | >= 0.7.0 |

### hillshade-exaggeration

[Paint](#paint-property) property. Optional [number](../types/#number) between `0` and `1` inclusive. Defaults to `0.5`. Supports [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

Intensity of the hillshade

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.43.0 | >= 6.0.0 | >= 4.0.0 | >= 0.7.0 |

### hillshade-highlight-color

[Paint](#paint-property) property. Optional [color](../types/#color). Defaults to `"#FFFFFF"`. Supports [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

The shading color of areas that faces towards the light source.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.43.0 | >= 6.0.0 | >= 4.0.0 | >= 0.7.0 |

### hillshade-illumination-anchor

[Paint](#paint-property) property. Optional [enum](../types/#enum). One of `"map"`, `"viewport"`. Defaults to `"viewport"`.

Direction of light source when map is rotated.

`"map"`:

The hillshade illumination is relative to the north direction.

`"viewport"`:

The hillshade illumination is relative to the top of the viewport.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.43.0 | >= 6.0.0 | >= 4.0.0 | >= 0.7.0 |

### hillshade-illumination-direction

[Paint](#paint-property) property. Optional [number](../types/#number) between `0` and `359` inclusive. Defaults to `335`. Supports [`interpolate`](../expressions/#interpolate)expressions.

The direction of the light source used to generate the hillshading with 0 as the top of the viewport if `hillshade-illumination-anchor` is set to `viewport` and due north if `hillshade-illumination-anchor` is set to `map`.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.43.0 | >= 6.0.0 | >= 4.0.0 | >= 0.7.0 |

### hillshade-shadow-color

[Paint](#paint-property) property. Optional [color](../types/#color). Defaults to `"#000000"`. Supports [`interpolate`](../expressions/#interpolate)expressions. Transitionable.

The shading color of areas that face away from the light source.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.43.0 | >= 6.0.0 | >= 4.0.0 | >= 0.7.0 |

### visibility

[Layout](#layout-property) property. Optional [enum](../types/#enum). One of `"visible"`, `"none"`. Defaults to `"visible"`.

Whether this layer is displayed.

`"visible"`:

The layer is shown.

`"none"`:

The layer is not shown.

| SDK Support | MapLibre GL JS | Android SDK | iOS SDK | macOS SDK |
| --- | --- | --- | --- | --- |
| basic functionality | >= 0.43.0 | >= 6.0.0 | >= 4.0.0 | >= 0.7.0 |
