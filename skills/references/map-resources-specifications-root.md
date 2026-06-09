# Source: https://docs.maptiler.com/gl-style-specification/root/

# Root

Root level properties of a GL style specify the map's layers, tile sources and other resources, and default values for the initial camera position when not specified elsewhere.

```json
{
    "version": 8,
    "name": "Streets",
    "sprite": "https://api.maptiler.com/maps/streets-v4/sprite",
    "glyphs": "https://api.maptiler.com/fonts/{fontstack}/{range}.pbf?key=<YOUR_MAPTILER_API_KEY>",
    "sources": {...},
    "layers": [...]
}
```

## bearing

Optional [number](../types/#number). Units in degrees. Defaults to `0`.

Default bearing, in degrees. The bearing is the compass direction that is "up"; for example, a bearing of 90° orients the map so that east is up. This value will be used only if the map has not been positioned by other means (e.g. map options or user interaction).

```json
"bearing": 29
```

## center

Optional [array](../types/#array) of [numbers](../types/#number).

Default map center in longitude and latitude. The style center will be used only if the map has not been positioned by other means (e.g. map options or user interaction).

```json
"center": [
  -73.9749,
  40.7736
]
```

## glyphs

Optional [string](../types/#string).

A URL template for loading signed-distance-field glyph sets in PBF format. The URL must include `{fontstack}` and `{range}` tokens. This property is required if any layer uses the `text-field` layout property. The URL must be absolute, containing the [scheme, authority and path components](https://en.wikipedia.org/wiki/URL#Syntax).

```json
"glyphs": "https://api.maptiler.com/fonts/{fontstack}/{range}.pbf?key=<YOUR_MAPTILER_API_KEY>"
```

## layers

Required [array](../types/#array) of [layers](../layers).

Layers will be drawn in the order of this array.

```json
"layers": [
  {
    "id": "water",
    "source": "openmaptiles",
    "source-layer": "water",
    "type": "fill",
    "paint": {
      "fill-color": "#00ffff"
    }
  }
]
```

## light

Optional [light](../light).

The global light source.

```json
"light": {
  "anchor": "viewport",
  "color": "white",
  "intensity": 0.4
}
```

## sky

Optional [sky](../sky/).

The map's sky configuration.

> [!NOTE]
> This definition is still experimental and is under development in maplibre-gl-js.

```json
"sky": {
    "sky-color": "#199EF3",
    "sky-horizon-blend": 0.5,
    "horizon-color": "#ffffff",
    "horizon-fog-blend": 0.5,
    "fog-color": "#0000ff",
    "fog-ground-blend": 0.5,
    "atmosphere-blend": [
        "interpolate",
        ["linear"],
        ["zoom"],
        0,
        1,
        10,
        1,
        12,
        0
    ]
}
```

## metadata

Optional.

Arbitrary properties useful to track with the stylesheet, but do not influence rendering. Properties should be prefixed to avoid collisions, like 'openmaptiles:'.

## name

Optional [string](../types/#string).

A human-readable name for the style.

```json
"name": "Bright"
```

## pitch

Optional [number](../types/#number). Units in degrees. Defaults to `0`.

Default pitch, in degrees. Zero is perpendicular to the surface, for a look straight down at the map, while a greater value like 60 looks ahead towards the horizon. The style pitch will be used only if the map has not been positioned by other means (e.g. map options or user interaction).

```json
"pitch": 50
```

## sources

Required object with [source](../sources) values.

Data source specifications.

```json
"sources": {
    "openmaptiles": {
        "url": "https://api.maptiler.com/tiles/v3/tiles.json?key=<YOUR_MAPTILER_API_KEY>",
        "type": "vector"
    }
}
```

## sprite

Optional [string](../types/#string).

A base URL for retrieving the sprite image and metadata. The extensions `.png`, `.json` and scale factor `@2x.png` will be automatically appended. This property is required if any layer uses the `background-pattern`, `fill-pattern`, `line-pattern`, `fill-extrusion-pattern`, or `icon-image` properties. The URL must be absolute, containing the [scheme, authority and path components](https://en.wikipedia.org/wiki/URL#Syntax).

```json
"sprite": "https://api.maptiler.com/maps/streets-v4/sprite"
```

## transition

Optional [transition](../transition).

A global transition definition to use as a default across properties, to be used for timing transitions between one value and the next when no property-specific transition is set. Collision-based symbol fading is controlled independently of the style's `transition` property.

```json
"transition": {
  "duration": 300,
  "delay": 0
}
```

## version

Required [enum](../types/#enum).

Style specification version number. Must be 8.

```json
"version": 8
```

## zoom

Optional [number](../types/#number).

Default zoom level. The style zoom will be used only if the map has not been positioned by other means (e.g. map options or user interaction).

```json
"zoom": 12.5
```
