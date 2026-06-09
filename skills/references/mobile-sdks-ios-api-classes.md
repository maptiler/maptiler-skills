# MapTiler iOS SDK API Reference - Classes

This document is a part of the iOS SDK API reference documentation, covering the `Classes` category.

---

## File: Classes/MTBackgroundLayer.html

---
layout: mobile_sdk
title: "MTBackgroundLayer"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "The background style layer covers the entire map.
Use a background style layer to configure a color or pattern to show below all other map content.
If the background layer is transparent or omitted from the style, any part of the map view that
does not show another style layer is transparent."
id: mtbackgroundlayer
breadcrumb: "Mobile SDK/iOS/Reference/Classes"
---

# MTBackgroundLayer

`public class MTBackgroundLayer : MTLayer, @unchecked Sendable, Codable`

The background style layer covers the entire map.
Use a background style layer to configure a color or pattern to show below all other map content.
If the background layer is transparent or omitted from the style, any part of the map view that
does not show another style layer is transparent.

Core properties

- 

identifier

Unique layer identifier.

#### Declaration

Swift
`public var identifier: String`

- 

type

Type of the layer.

#### Declaration

Swift
`public private(set) var type: MTLayerType { get }`

- 

sourceIdentifier

Background layers have no source. This placeholder satisfies the `MTLayer` protocol.
It is ignored during encoding/decoding and by the style bridge.

#### Declaration

Swift
`public var sourceIdentifier: String`

- 

maxZoom

The maximum zoom level for the layer.
Optional number between 0 and 24. At zoom levels equal to or greater than the maxzoom,
the layer will be hidden.

#### Declaration

Swift
`public var maxZoom: Double?`

- 

minZoom

The minimum zoom level for the layer.
Optional number between 0 and 24. At zoom levels less than the minzoom,
the layer will be hidden.

#### Declaration

Swift
`public var minZoom: Double?`

- 

sourceLayer

Background layers have no source layer; present only to satisfy `MTLayer` protocol.

#### Declaration

Swift
`public var sourceLayer: String?`

Paint properties

- 

color

The color with which the background will be drawn.
Can be a constant color or an expression.
Defaults to black.

#### Declaration

Swift
`public var color: MTStyleValue?`

- 

opacity

The opacity at which the background will be drawn.
Optional number between 0 and 1 inclusive. Defaults to 1.

#### Declaration

Swift
`public var opacity: Double?`

- 

pattern

Name of image in sprite to use for drawing an image background.
For seamless patterns, image width and height must be a factor of two.

#### Declaration

Swift
`public var pattern: String?`

Layout properties

- 

visibility

Whether this layer is displayed. Defaults to “visible”.

#### Declaration

Swift
`public var visibility: MTLayerVisibility?`

Initializers

- 

init(identifier:)

Initializes the background layer with an identifier.

#### Declaration

Swift
`public init(identifier: String)`

- 

init(identifier:maxZoom:minZoom:color:opacity:pattern:visibility:)

Initializes the background layer with all options.

#### Declaration

Swift
public init(
identifier: String,
maxZoom: Double? = nil,
minZoom: Double? = nil,
color: MTStyleValue? = .color(.black),
opacity: Double? = 1.0,
pattern: String? = nil,
visibility: MTLayerVisibility? = .visible
)

Codable

- 

init(from:)

Initializes layer from the decoder.

#### Declaration

Swift
`public required init(from decoder: any Decoder) throws`

- 

encode(to:)

#### Declaration

Swift
`public func encode(to encoder: Encoder) throws`

- 

addToMap(_:)

Adds layer to map DSL style.

Prefer `MTStyle.addLayer(_:)` on MTMapView instead.

#### Declaration

Swift
`public func addToMap(_ mapView: MTMapView)`

Modifiers (for DSL chaining). Not for external use.

- 

maxZoom(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func maxZoom(_ value: Double) -> Self

- 

minZoom(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func minZoom(_ value: Double) -> Self

- 

color(_:)

Sets a constant background color value.

#### Declaration

Swift
@discardableResult
public func color(_ value: UIColor) -> Self

- 

paintColorExpression(_:)

Sets a background color expression (e.g., interpolate by zoom).

#### Declaration

Swift
@discardableResult
public func paintColorExpression(_ expr: MTPropertyValue) -> Self

- 

opacity(_:)

Sets the background opacity (0–1).

#### Declaration

Swift
@discardableResult
public func opacity(_ value: Double) -> Self

- 

pattern(_:)

Sets the background sprite pattern name.

#### Declaration

Swift
@discardableResult
public func pattern(_ value: String) -> Self

- 

visibility(_:)

Sets the background visibility.

#### Declaration

Swift
@discardableResult
public func visibility(_ value: MTLayerVisibility) -> Self

---

## File: Classes/MTBenchmark.html

---
layout: mobile_sdk
title: "MTBenchmark"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Basic benchmarking class."
id: mtbenchmark
breadcrumb: "Mobile SDK/iOS/Reference/Classes"
---

# MTBenchmark

@MainActor
public final class MTBenchmark : MTMapViewDelegate

Basic benchmarking class.

- 

mapView

Undocumented

#### Declaration

Swift
@MainActor
public var mapView: MTMapView!

- 

didUpdateStressTest

Undocumented

#### Declaration

Swift
@MainActor
public var didUpdateStressTest: ((String) -> Void)?

- 

init(frame:)

Asynchronous

Undocumented

#### Declaration

Swift
@MainActor
public init(frame: CGRect) async

- 

setAPIKey(apiKey:)

Undocumented

#### Declaration

Swift
@MainActor
public func setAPIKey(apiKey: String)

- 

start()

Asynchronous

Undocumented

#### Declaration

Swift
@MainActor
public func start() async

- 

startStressTest(iterations:markersAreOn:)

Asynchronous

Undocumented

#### Declaration

Swift
@MainActor
public func startStressTest(iterations: Int, markersAreOn: Bool) async

- 

mapView(_:didTriggerEvent:with:)

#### Declaration

Swift
@MainActor
public func mapView(_ mapView: MTMapView, didTriggerEvent event: MTEvent, with data: MTData?)

- 

mapViewDidInitialize(_:)

#### Declaration

Swift
@MainActor
public func mapViewDidInitialize(_ mapView: MTMapView)

---

## File: Classes/MTCircleLayer.html

---
layout: mobile_sdk
title: "MTCircleLayer"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "The circle style layer renders one or more filled circles on the map."
id: mtcirclelayer
breadcrumb: "Mobile SDK/iOS/Reference/Classes"
---

# MTCircleLayer

`public class MTCircleLayer : MTLayer, @unchecked Sendable, Codable`
`extension MTCircleLayer: Equatable`

The circle style layer renders one or more filled circles on the map.

Core properties

- 

identifier

Unique layer identifier.

#### Declaration

Swift
`public var identifier: String`

- 

type

Type of the layer.

#### Declaration

Swift
`public private(set) var type: MTLayerType { get }`

- 

sourceIdentifier

Identifier of the source to be used for this layer.

#### Declaration

Swift
`public var sourceIdentifier: String`

- 

maxZoom

The maximum zoom level for the layer.
Optional number between 0 and 24. At zoom levels equal to or greater than the maxzoom,
the layer will be hidden.

#### Declaration

Swift
`public var maxZoom: Double?`

- 

minZoom

The minimum zoom level for the layer.
Optional number between 0 and 24. At zoom levels less than the minzoom,
the layer will be hidden.

#### Declaration

Swift
`public var minZoom: Double?`

- 

sourceLayer

Layer to use from a vector tile source.
Required for vector tile sources; prohibited for all other source types,
including GeoJSON sources.

#### Declaration

Swift
`public var sourceLayer: String?`

Paint properties

- 

blur

Amount to blur the circle. Default 0.

#### Declaration

Swift
`public var blur: Double?`

- 

color

The fill color of the circle (constant or expression).

#### Declaration

Swift
`public var color: MTStyleValue?`

- 

opacity

The opacity at which the circle will be drawn. Default 1.

#### Declaration

Swift
`public var opacity: Double?`

- 

radius

Circle radius in pixels (constant or expression).

#### Declaration

Swift
`public var radius: MTStyleValue?`

- 

strokeColor

The stroke color of the circle’s outline.

#### Declaration

Swift
`public var strokeColor: UIColor?`

- 

strokeOpacity

The opacity of the circle’s outline.

#### Declaration

Swift
`public var strokeOpacity: Double?`

- 

strokeWidth

The width of the circle’s outline in pixels.

#### Declaration

Swift
`public var strokeWidth: Double?`

- 

translate

The geometry’s offset. Values are [x, y] where negatives indicate left and up.

#### Declaration

Swift
`public var translate: [Double]?`

- 

translateAnchor

Controls the frame of reference for translate.

#### Declaration

Swift
`public var translateAnchor: MTCircleTranslateAnchor?`

- 

pitchAlignment

Orientation of circle when map is pitched.
Defaults to “viewport”.

#### Declaration

Swift
`public var pitchAlignment: MTCirclePitchAlignment?`

- 

pitchScale

Controls scaling behavior of the circle when the map is pitched.
Defaults to “map”.

#### Declaration

Swift
`public var pitchScale: MTCirclePitchScale?`

Layout properties

- 

sortKey

Feature ordering value. Features with a higher sort key will appear above features with a lower sort key.

#### Declaration

Swift
`public var sortKey: Double?`

- 

visibility

Enum controlling whether this layer is displayed.

#### Declaration

Swift
`public var visibility: MTLayerVisibility?`

- 

initialFilter

Optional initial filter to apply after the layer is added to the map.

#### Declaration

Swift
`public var initialFilter: MTPropertyValue?`

Initial paint expressions (applied after add)

- 

circleColor

Circle color can be a constant or an expression.

#### Declaration

Swift
`public var circleColor: MTStyleValue?`

- 

circleRadius

Circle radius can be a constant or an expression.

#### Declaration

Swift
`public var circleRadius: MTStyleValue?`

- 

filterExpression

Filter expression to be embedded inline in layer JSON.

#### Declaration

Swift
`public var filterExpression: MTPropertyValue?`

- 

filter

Optional filter to apply to this layer.

#### Declaration

Swift
`public var filter: MTPropertyValue?`

Initializers

- 

init(identifier:sourceIdentifier:)

Initializes the layer with unique identifier and source identifier.

#### Declaration

Swift
public init(
identifier: String,
sourceIdentifier: String
)

- 

init(identifier:sourceIdentifier:maxZoom:minZoom:sourceLayer:blur:color:opacity:radius:strokeColor:strokeOpacity:strokeWidth:translate:translateAnchor:sortKey:visibility:)

Initializes the layer with all options.

#### Declaration

Swift
public init(
identifier: String,
sourceIdentifier: String,
maxZoom: Double? = nil,
minZoom: Double? = nil,
sourceLayer: String? = nil,
blur: Double? = 0.0,
color: MTStyleValue? = nil,
opacity: Double? = 1.0,
radius: MTStyleValue? = nil,
strokeColor: UIColor? = .black,
strokeOpacity: Double? = 1.0,
strokeWidth: Double? = 0.0,
translate: [Double]? = [0.0, 0.0],
translateAnchor: MTCircleTranslateAnchor? = .map,
sortKey: Double? = nil,
visibility: MTLayerVisibility? = .visible
)

Codable

- 

init(from:)

Initializes the layer from the decoder.

#### Declaration

Swift
`public required init(from decoder: any Decoder) throws`

- 

encode(to:)

#### Declaration

Swift
`public func encode(to encoder: Encoder) throws`

- 

addToMap(_:)

Adds layer to map DSL style.

Prefer `addLayer(_:)` on MTMapView instead.

#### Declaration

Swift
`public func addToMap(_ mapView: MTMapView)`

Modifiers (for DSL chaining). Not for external use.

- 

maxZoom(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func maxZoom(_ value: Double) -> Self

- 

minZoom(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func minZoom(_ value: Double) -> Self

- 

sourceLayer(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func sourceLayer(_ value: String) -> Self

- 

blur(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func blur(_ value: Double) -> Self

- 

color(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func color(_ value: UIColor) -> Self

- 

opacity(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func opacity(_ value: Double) -> Self

- 

radius(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func radius(_ value: Double) -> Self

- 

strokeColor(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func strokeColor(_ value: UIColor) -> Self

- 

strokeOpacity(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func strokeOpacity(_ value: Double) -> Self

- 

strokeWidth(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func strokeWidth(_ value: Double) -> Self

- 

translate(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func translate(_ value: [Double]) -> Self

- 

translateAnchor(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func translateAnchor(_ value: MTCircleTranslateAnchor) -> Self

- 

sortKey(_:)

Sets the sort key for feature ordering.

#### Declaration

Swift
@discardableResult
public func sortKey(_ value: Double) -> Self

#### Parameters

| value | Sort key; higher draws above lower. |

- 

visibility(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func visibility(_ value: MTLayerVisibility) -> Self

- 

pitchAlignment(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func pitchAlignment(_ value: MTCirclePitchAlignment) -> Self

- 

pitchScale(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func pitchScale(_ value: MTCirclePitchScale) -> Self

- 

withFilter(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func withFilter(_ value: MTPropertyValue) -> Self

- 

paintColorExpression(_:)

Sets a circle color expression (e.g., step).

#### Declaration

Swift
@discardableResult
public func paintColorExpression(_ expr: MTPropertyValue) -> Self

#### Parameters

| expr | Expression to drive circle color. |

- 

paintRadiusExpression(_:)

Sets a circle radius expression (e.g., step).

#### Declaration

Swift
@discardableResult
public func paintRadiusExpression(_ expr: MTPropertyValue) -> Self

#### Parameters

| expr | Expression to drive circle radius. |

- 

paintColor(_:)

Sets a constant circle color value.

#### Declaration

Swift
@discardableResult
public func paintColor(_ color: UIColor) -> Self

#### Parameters

| color | UIColor value. |

- 

paintRadius(_:)

Sets a constant circle radius value in pixels.

#### Declaration

Swift
@discardableResult
public func paintRadius(_ value: Double) -> Self

#### Parameters

| value | Radius in pixels. |

- 

==(_:_:)

#### Declaration

Swift
`public static func == (lhs: MTCircleLayer, rhs: MTCircleLayer) -> Bool`

---

## File: Classes/MTColorRamp.html

---
layout: mobile_sdk
title: "MTColorRamp"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Swift wrapper over the MapTiler SDK ColorRamp class."
id: mtcolorramp
breadcrumb: "Mobile SDK/iOS/Reference/Classes"
---

# MTColorRamp

@MainActor
public final class MTColorRamp : @unchecked Sendable

Swift wrapper over the MapTiler SDK ColorRamp class.

- 

identifier

Undocumented

#### Declaration

Swift
@MainActor
public let identifier: String

- 

init(options:)

Creates a custom color ramp using the provided options.

#### Declaration

Swift
@MainActor
public convenience init(options: MTColorRampOptions)

- 

init(min:max:stops:)

Creates a custom color ramp using explicit values and stops.

#### Declaration

Swift
@MainActor
public convenience init(min: Double? = nil, max: Double? = nil, stops: [MTColorRampStop])

- 

preset(_:)

Creates a color ramp from a built-in preset. The preset is cloned to keep the global preset untouched.

#### Declaration

Swift
@MainActor
public static func preset(_ preset: MTColorRampPreset) -> MTColorRamp

- 

fromArrayDefinition(_:)

Creates a color ramp from the array definition.

#### Declaration

Swift
@MainActor
public static func fromArrayDefinition(_ definition: [MTColorRampArrayStop]) -> MTColorRamp

- 

getBounds(in:)

Asynchronous

Returns bounds of the color ramp.

#### Declaration

Swift
@MainActor
public func getBounds(in mapView: MTMapView) async throws -> MTColorRampBounds

- 

getColor(at:smooth:in:)

Asynchronous

Returns the color at the provided value.

#### Declaration

Swift
@MainActor
public func getColor(
at value: Double,
smooth: Bool = true,
in mapView: MTMapView
) async throws -> MTRGBAColor

- 

getColorHex(at:smooth:includeAlpha:in:)

Asynchronous

Returns the color hex string at the provided value.

#### Declaration

Swift
@MainActor
public func getColorHex(
at value: Double,
smooth: Bool = true,
includeAlpha: Bool = false,
in mapView: MTMapView
) async throws -> String

- 

getColorRelative(at:smooth:in:)

Asynchronous

Returns the color for a relative value in [0, 1].

#### Declaration

Swift
@MainActor
public func getColorRelative(
at value: Double,
smooth: Bool = true,
in mapView: MTMapView
) async throws -> MTRGBAColor

- 

getRawColorStops(in:)

Asynchronous

Returns raw stops backing the ramp.

#### Declaration

Swift
@MainActor
public func getRawColorStops(in mapView: MTMapView) async throws -> [MTColorRampStop]

- 

clone(in:)

Asynchronous

Clones the color ramp.

#### Declaration

Swift
@MainActor
public func clone(in mapView: MTMapView) async throws -> MTColorRamp

- 

reverse(clone:in:)

Asynchronous

Returns a ramp reversed in-place or cloned depending on the `clone` flag.

#### Declaration

Swift
@MainActor
public func reverse(clone: Bool = true, in mapView: MTMapView) async throws -> MTColorRamp

- 

scale(min:max:clone:in:)

Asynchronous

Scales the ramp to the given bounds.

#### Declaration

Swift
@MainActor
public func scale(
min: Double,
max: Double,
clone: Bool = true,
in mapView: MTMapView
) async throws -> MTColorRamp

- 

setStops(_:clone:in:)

Asynchronous

Replaces the stops on the ramp.

#### Declaration

Swift
@MainActor
public func setStops(
_ stops: [MTColorRampStop],
clone: Bool = true,
in mapView: MTMapView
) async throws -> MTColorRamp

- 

resample(_:samples:in:)

Asynchronous

Resamples the ramp using the provided method and sample count.

#### Declaration

Swift
@MainActor
public func resample(
_ method: MTColorRampResampleMethod,
samples: Int = 15,
in mapView: MTMapView
) async throws -> MTColorRamp

- 

transparentStart(in:)

Asynchronous

Prepends a transparent stop at the beginning of the ramp.

#### Declaration

Swift
@MainActor
public func transparentStart(in mapView: MTMapView) async throws -> MTColorRamp

- 

hasTransparentStart(in:)

Asynchronous

Returns true if the first stop is transparent.

#### Declaration

Swift
@MainActor
public func hasTransparentStart(in mapView: MTMapView) async throws -> Bool

- 

getCanvasStrip(options:in:)

Asynchronous

Renders the ramp to a canvas strip and returns it as `UIImage`.

#### Declaration

Swift
@MainActor
public func getCanvasStrip(
options: MTColorRampCanvasStripOptions = MTColorRampCanvasStripOptions(),
in mapView: MTMapView
) async throws -> UIImage

- 

getColor(at:smooth:in:completionHandler:)

Deprecated completion-based variant of `getColor(at:smooth:in:)`.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
func getColor(
at value: Double,
smooth: Bool = true,
in mapView: MTMapView,
completionHandler: ((Result<MTRGBAColor, MTError>) -> Void)? = nil
)

- 

getColorHex(at:smooth:includeAlpha:in:completionHandler:)

Deprecated completion-based variant of `getColorHex(at:smooth:includeAlpha:in:)`.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
func getColorHex(
at value: Double,
smooth: Bool = true,
includeAlpha: Bool = false,
in mapView: MTMapView,
completionHandler: ((Result<String, MTError>) -> Void)? = nil
)

- 

getBounds(in:completionHandler:)

Deprecated completion-based variant of `getBounds(in:)`.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
func getBounds(
in mapView: MTMapView,
completionHandler: ((Result<MTColorRampBounds, MTError>) -> Void)? = nil
)

- 

getRawColorStops(in:completionHandler:)

Deprecated completion-based variant of `getRawColorStops(in:)`.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
func getRawColorStops(
in mapView: MTMapView,
completionHandler: ((Result<[MTColorRampStop], MTError>) -> Void)? = nil
)

- 

clone(in:completionHandler:)

Deprecated completion-based variant of `clone(in:)`.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
func clone(
in mapView: MTMapView,
completionHandler: ((Result<MTColorRamp, MTError>) -> Void)? = nil
)

---

## File: Classes/MTCustomAnnotationView.html

---
layout: mobile_sdk
title: "MTCustomAnnotationView"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Subclassable view for adding custom annotations to the map."
id: mtcustomannotationview
breadcrumb: "Mobile SDK/iOS/Reference/Classes"
---

# MTCustomAnnotationView

@MainActor
open class MTCustomAnnotationView : UIView, @preconcurrency MTAnnotation
`extension MTCustomAnnotationView: @preconcurrency MTMapViewContent`

Subclassable view for adding custom annotations to the map.

- 

identifier

Unique id of the view.

#### Declaration

Swift
@MainActor
public private(set) var identifier: String { get }

- 

coordinates

Position of the view on the map.

#### Declaration

Swift
@MainActor
public private(set) var coordinates: CLLocationCoordinate2D { get }

- 

offset

Offset from the center.

#### Declaration

Swift
@MainActor
public private(set) var offset: MTPoint { get }

- 

init(size:coordinates:)

#### Declaration

Swift
@MainActor
public init(
size: CGSize,
coordinates: CLLocationCoordinate2D
)

#### Parameters

| size | Size of the annotation view. |
| coordinates | Position of the annotation. |

- 

init(size:coordinates:offset:)

#### Declaration

Swift
@MainActor
public init(
size: CGSize,
coordinates: CLLocationCoordinate2D,
offset: MTPoint
)

#### Parameters

| size | Size of the annotation view. |
| coordinates | Position of the annotation. |
| offset | Offset from the center. |

- 

init(coder:)

Not implemented code init.

#### Declaration

Swift
@MainActor
required public init?(coder: NSCoder)

- 

setOffset(_:)

Sets the offset of the annotation view in pixels.

#### Declaration

Swift
@MainActor
public func setOffset(_ offset: MTPoint)

#### Parameters

| offset | Desired offset. |

- 

setCoordinates(_:in:completionHandler:)

Sets coordinates for the view.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setCoordinates(
_ coordinates: CLLocationCoordinate2D,
in mapView: MTMapView,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| coordinates | Position of the view |
| completionHandler | A handler block to execute when function finishes. |
| mapView | Map view to apply to. |

- 

addTo(_:completionHandler:)

Adds custom annotation view to the map.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func addTo(_ mapView: MTMapView, completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| mapView | Map view to add annotation to. |
| completionHandler | A handler block to execute when function finishes. |

- 

remove()

Removes custom annotation view from the map.

#### Declaration

Swift
@MainActor
public func remove()

- 

setCoordinates(_:in:)

Asynchronous

Sets coordinates for the view.

#### Declaration

Swift
@MainActor
public func setCoordinates(_ coordinates: CLLocationCoordinate2D, in mapView: MTMapView) async

#### Parameters

| coordinates | Position of the view. |

- 

addTo(_:)

Asynchronous

Adds custom annotation view to the map.

#### Declaration

Swift
@MainActor
public func addTo(_ mapView: MTMapView) async

#### Parameters

| mapView | Map view to add annotation to. |

- 

addToMap(_:)

Adds annotation view to map DSL style.

Prefer `addTo(_:)` instead.

#### Declaration

Swift
@MainActor
public func addToMap(_ mapView: MTMapView)

---

## File: Classes/MTFillExtrusionLayer.html

---
layout: mobile_sdk
title: "MTFillExtrusionLayer"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "A fill-extrusion style layer renders one or more filled (and optionally stroked) extruded (3D) polygons on a map."
id: mtfillextrusionlayer
breadcrumb: "Mobile SDK/iOS/Reference/Classes"
---

# MTFillExtrusionLayer

`public class MTFillExtrusionLayer : MTLayer, @unchecked Sendable, Codable`
`extension MTFillExtrusionLayer: Equatable`

A fill-extrusion style layer renders one or more filled (and optionally stroked) extruded (3D) polygons on a map.

Core properties

- 

identifier

Unique layer identifier.

#### Declaration

Swift
`public var identifier: String`

- 

type

Type of the layer.

#### Declaration

Swift
`public private(set) var type: MTLayerType { get }`

- 

sourceIdentifier

Identifier of the source to be used for this layer.

#### Declaration

Swift
`public var sourceIdentifier: String`

- 

maxZoom

The maximum zoom level for the layer. Optional number between 0 and 24.

#### Declaration

Swift
`public var maxZoom: Double?`

- 

minZoom

The minimum zoom level for the layer. Optional number between 0 and 24.

#### Declaration

Swift
`public var minZoom: Double?`

- 

sourceLayer

Layer to use from a vector tile source. Required for vector tile sources; prohibited for others.

#### Declaration

Swift
`public var sourceLayer: String?`

Paint properties

- 

base

The height with which to extrude the base of this layer.
Must be less than or equal to fill-extrusion-height. Units in meters.
Supports expressions.

#### Declaration

Swift
`public var base: MTStyleValue?`

- 

color

The base color of the extruded fill. Supports expressions.

#### Declaration

Swift
`public var color: MTStyleValue?`

- 

height

The height with which to extrude this layer. Units in meters. Supports expressions.

#### Declaration

Swift
`public var height: MTStyleValue?`

- 

opacity

The opacity of the entire fill extrusion layer. Supports expressions. Default 1.

#### Declaration

Swift
`public var opacity: MTStyleValue?`

- 

pattern

Name of image in sprite to use for drawing images on extruded fills.

#### Declaration

Swift
`public var pattern: String?`

- 

translate

The geometry’s offset. Values are [x, y] in pixels.

#### Declaration

Swift
`public var translate: [Double]?`

- 

translateAnchor

Controls the frame of reference for translate.

#### Declaration

Swift
`public var translateAnchor: MTFillExtrusionTranslateAnchor?`

- 

verticalGradient

Whether to apply a vertical gradient to the sides of a fill-extrusion layer. Defaults to true.

#### Declaration

Swift
`public var verticalGradient: Bool?`

Layout properties

- 

visibility

Whether this layer is displayed. Defaults to “visible”.

#### Declaration

Swift
`public var visibility: MTLayerVisibility?`

Filters

- 

filterExpression

Inline filter expression to be embedded in the layer JSON.

#### Declaration

Swift
`public var filterExpression: MTPropertyValue?`

- 

initialFilter

Optional filter to apply to this layer after it is added to the map.

#### Declaration

Swift
`public var initialFilter: MTPropertyValue?`

Initializers

- 

init(identifier:sourceIdentifier:)

Initializes the layer with a unique identifier and source identifier.

#### Declaration

Swift
`public init(identifier: String, sourceIdentifier: String)`

- 

init(identifier:sourceIdentifier:maxZoom:minZoom:sourceLayer:base:color:height:opacity:pattern:translate:translateAnchor:verticalGradient:visibility:)

Initializes the layer with all options.

#### Declaration

Swift
public init(
identifier: String,
sourceIdentifier: String,
maxZoom: Double? = nil,
minZoom: Double? = nil,
sourceLayer: String? = nil,
base: MTStyleValue? = nil,
color: MTStyleValue? = .color(.black),
height: MTStyleValue? = nil,
opacity: MTStyleValue? = .number(1.0),
pattern: String? = nil,
translate: [Double]? = [0.0, 0.0],
translateAnchor: MTFillExtrusionTranslateAnchor? = .map,
verticalGradient: Bool? = true,
visibility: MTLayerVisibility? = .visible
)

Codable

- 

init(from:)

#### Declaration

Swift
`public required init(from decoder: any Decoder) throws`

- 

encode(to:)

#### Declaration

Swift
`public func encode(to encoder: Encoder) throws`

- 

addToMap(_:)

Adds layer to map DSL style.
Prefer MTStyle.addLayer(_:) on MTMapView instead.

#### Declaration

Swift
`public func addToMap(_ mapView: MTMapView)`

Modifiers (not to be used outside DSL)

- 

maxZoom(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func maxZoom(_ value: Double) -> Self

- 

minZoom(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func minZoom(_ value: Double) -> Self

- 

sourceLayer(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func sourceLayer(_ value: String) -> Self

- 

base(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func base(_ value: MTStyleValue) -> Self

- 

color(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func color(_ value: MTStyleValue) -> Self

- 

height(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func height(_ value: MTStyleValue) -> Self

- 

opacity(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func opacity(_ value: MTStyleValue) -> Self

- 

pattern(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func pattern(_ value: String) -> Self

- 

translate(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func translate(_ value: [Double]) -> Self

- 

translateAnchor(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func translateAnchor(_ value: MTFillExtrusionTranslateAnchor) -> Self

- 

verticalGradient(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func verticalGradient(_ value: Bool) -> Self

- 

visibility(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func visibility(_ value: MTLayerVisibility) -> Self

- 

withFilter(_:)

Modifier. Sets the initial filter to apply upon add.

#### Declaration

Swift
@discardableResult
public func withFilter(_ value: MTPropertyValue) -> Self

- 

==(_:_:)

#### Declaration

Swift
`public static func == (lhs: MTFillExtrusionLayer, rhs: MTFillExtrusionLayer) -> Bool`

---

## File: Classes/MTFillLayer.html

---
layout: mobile_sdk
title: "MTFillLayer"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "The fill style layer that renders one or more filled (and optionally stroked) polygons on a map."
id: mtfilllayer
breadcrumb: "Mobile SDK/iOS/Reference/Classes"
---

# MTFillLayer

`public class MTFillLayer : MTLayer, @unchecked Sendable, Codable`
`extension MTFillLayer: Equatable`

The fill style layer that renders one or more filled (and optionally stroked) polygons on a map.

- 

identifier

Unique layer identifier.

#### Declaration

Swift
`public var identifier: String`

- 

type

Type of the layer.

#### Declaration

Swift
`public private(set) var type: MTLayerType { get }`

- 

sourceIdentifier

Identifier of the source to be used for this layer.

#### Declaration

Swift
`public var sourceIdentifier: String`

- 

maxZoom

The maximum zoom level for the layer.

Optional number between 0 and 24. At zoom levels equal to or greater than the maxzoom,
the layer will be hidden.

#### Declaration

Swift
`public var maxZoom: Double?`

- 

minZoom

The minimum zoom level for the layer.

Optional number between 0 and 24. At zoom levels less than the minzoom,
the layer will be hidden.

#### Declaration

Swift
`public var minZoom: Double?`

- 

sourceLayer

Layer to use from a vector tile source.

Required for vector tile sources; prohibited for all other source types,
including GeoJSON sources.

#### Declaration

Swift
`public var sourceLayer: String?`

- 

shouldBeAntialised

Boolean indicating whether or not the fill should be antialiased.

Note
Defaults to true.

#### Declaration

Swift
`public var shouldBeAntialised: Bool?`

- 

color

The color of the filled part of this layer.

Note
Defaults to black.

#### Declaration

Swift
`public var color: UIColor?`

- 

opacity

The opacity of the entire fill layer.

Optional number between 0 and 1 inclusive.

Note
Defaults to 1.

#### Declaration

Swift
`public var opacity: Double?`

- 

outlineColor

The outline color of the fill.

Matches the value of fill-color if unspecified.

#### Declaration

Swift
`public var outlineColor: UIColor?`

- 

translate

The geometry’s offset.

Units in pixels. Values are [x, y] where negatives indicate left and up, respectively.

Note
Defaults to [0,0].

#### Declaration

Swift
`public var translate: [Double]?`

- 

translateAnchor

Enum controlling the frame of reference for translate.

#### Declaration

Swift
`public var translateAnchor: MTFillTranslateAnchor?`

- 

sortKey

Key for sorting features.

Features with a higher sort key will appear above features with a lower sort key.

#### Declaration

Swift
`public var sortKey: Double?`

- 

visibility

Enum controlling whether this layer is displayed.

#### Declaration

Swift
`public var visibility: MTLayerVisibility?`

- 

initialFilter

Optional initial filter to apply after the layer is added to the map.

#### Declaration

Swift
`public var initialFilter: MTPropertyValue?`

- 

init(identifier:sourceIdentifier:maxZoom:minZoom:sourceLayer:)

Initializes the layer with unique identifier, source identifier, max and min zoom levels and source layer,
which is required for vector tile sources.

#### Declaration

Swift
public init(
identifier: String,
sourceIdentifier: String,
maxZoom: Double,
minZoom: Double,
sourceLayer: String? = nil
)

- 

init(identifier:sourceIdentifier:)

Initializes the layer with the unique identifier and a source identifier.

#### Declaration

Swift
public init(
identifier: String,
sourceIdentifier: String
)

- 

init(identifier:sourceIdentifier:maxZoom:minZoom:sourceLayer:shouldBeAntialised:color:opacity:outlineColor:translate:translateAnchor:sortKey:visibility:)

Initializes the layer with all options.

#### Declaration

Swift
public init(
identifier: String,
sourceIdentifier: String,
maxZoom: Double? = nil,
minZoom: Double? = nil,
sourceLayer: String? = nil,
shouldBeAntialised: Bool? = true,
color: UIColor? = .black,
opacity: Double? = 1.0,
outlineColor: UIColor? = nil,
translate: [Double]? = nil,
translateAnchor: MTFillTranslateAnchor? = .map,
sortKey: Double? = nil,
visibility: MTLayerVisibility? = .visible
)

- 

init(from:)

Initializes the layer from the decoder.

#### Declaration

Swift
`public required init(from decoder: any Decoder) throws`

- 

encode(to:)

#### Declaration

Swift
`public func encode(to encoder: Encoder) throws`

- 

addToMap(_:)

Adds layer to map DSL style.

Prefer `addLayer(_:)` on MTMapView instead.

#### Declaration

Swift
`public func addToMap(_ mapView: MTMapView)`

- 

maxZoom(_:)

Modifier. Sets the `maxZoom`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func maxZoom(_ value: Double) -> Self

- 

minZoom(_:)

Modifier. Sets the `minZoom`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func minZoom(_ value: Double) -> Self

- 

sourceLayer(_:)

Modifier. Sets the `sourceLayer`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func sourceLayer(_ value: String) -> Self

- 

shouldBeAntialised(_:)

Modifier. Sets the `shouldBeAntialised`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func shouldBeAntialised(_ value: Bool) -> Self

- 

color(_:)

Modifier. Sets the `color`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func color(_ value: UIColor) -> Self

- 

opacity(_:)

Modifier. Sets the `opacity`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func opacity(_ value: Double) -> Self

- 

outlineColor(_:)

Modifier. Sets the `outlineColor`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func outlineColor(_ value: UIColor) -> Self

- 

translate(_:)

Modifier. Sets the `translate`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func translate(_ value: [Double]) -> Self

- 

translateAnchor(_:)

Modifier. Sets the `translateAnchor`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func translateAnchor(_ value: MTFillTranslateAnchor) -> Self

- 

sortKey(_:)

Modifier. Sets the `sortKey`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func sortKey(_ value: Double) -> Self

- 

visibility(_:)

Modifier. Sets the `visibility`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func visibility(_ value: MTLayerVisibility) -> Self

- 

withFilter(_:)

Modifier. Sets the initial filter to apply upon add.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func withFilter(_ value: MTPropertyValue) -> Self

- 

==(_:_:)

#### Declaration

Swift
`public static func == (lhs: MTFillLayer, rhs: MTFillLayer) -> Bool`

---

## File: Classes/MTGeoJSONSource.html

---
layout: mobile_sdk
title: "MTGeoJSONSource"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "A geojson source."
id: mtgeojsonsource
breadcrumb: "Mobile SDK/iOS/Reference/Classes"
---

# MTGeoJSONSource

`public class MTGeoJSONSource : MTSource, @unchecked Sendable, Codable`

A geojson source.

- 

identifier

Unique id of the source.

#### Declaration

Swift
`public var identifier: String`

- 

url

URL pointing to the geojson resource.

#### Declaration

Swift
`public var url: URL?`

- 

jsonString

GeoJSON String.

GeoJSON string parses coordinates as Longitude, Latitude pairs, in that order.

#### Declaration

Swift
`public var jsonString: String?`

- 

type

Type of the source.

#### Declaration

Swift
`public private(set) var type: MTSourceType { get }`

- 

attribution

Attribution to be displayed when the map is shown to a user.

#### Declaration

Swift
`public var attribution: String?`

- 

buffer

Size of the tile buffer on each side.

Optional number between 0 and 512 inclusive. A value of 0 produces no buffer.
A value of 512 produces a buffer as wide as the tile itself.
Larger values produce fewer rendering artifacts near tile edges and slower performance.

Note
Defaults to 128.

#### Declaration

Swift
`public var buffer: Int?`

- 

isCluster

If the data is a collection of point features, sets the points by radius into groups.

Note
Defaults to false.

#### Declaration

Swift
`public var isCluster: Bool`

- 

clusterMaxZoom

Max zoom on which to cluster points if clustering is enabled.

Defaults to one zoom less than maxzoom (so that last zoom features are not clustered).

#### Declaration

Swift
`public var clusterMaxZoom: Double?`

- 

clusterRadius

Radius of each cluster if clustering is enabled.

A value of 512 indicates a radius equal to the width of a tile.

Note
Defaults to 50.

#### Declaration

Swift
`public var clusterRadius: Double?`

- 

maxZoom

Maximum zoom level at which to create vector tiles.

Higher value means greater detail at high zoom levels.

Note
Defaults to 18.

#### Declaration

Swift
`public var maxZoom: Double?`

- 

tolerance

Douglas-Peucker simplification tolerance.

Higher value means simpler geometries and faster performance.

Note
Defaults to 0.375

#### Declaration

Swift
`public var tolerance: Double?`

- 

lineMetrics

Specifices whether to calculate line distance metrics

#### Declaration

Swift
`public var lineMetrics: Bool?`

- 

init(identifier:url:)

Initializes the source with unique id and url to TileJSON resource.

#### Declaration

Swift
`public init(identifier: String, url: URL)`

- 

init(identifier:jsonString:)

Initializes the source with unique id and GeoJSON string.

GeoJSON string parses coordinates as Longitude, Latitude pairs, in that order.

#### Declaration

Swift
`public init(identifier: String, jsonString: String)`

- 

init(identifier:url:attribution:buffer:isCluster:clusterMaxZoom:clusterRadius:maxZoom:tolerance:lineMetrics:)

Initializes the source with all the options.

#### Declaration

Swift
public init(
identifier: String,
url: URL? = nil,
attribution: String? = nil,
buffer: Int? = 128,
isCluster: Bool = false,
clusterMaxZoom: Double? = nil,
clusterRadius: Double? = 50,
maxZoom: Double? = 18,
tolerance: Double? = 0.375,
lineMetrics: Bool? = false
)

- 

init(from:)

Initializes the source from the decoder.

#### Declaration

Swift
`public required init(from decoder: any Decoder) throws`

- 

encode(to:)

#### Declaration

Swift
`public func encode(to encoder: Encoder) throws`

- 

setData(data:in:completionHandler:)

Sets the data of the source.

Used for updating the source data.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setData(data: URL, in mapView: MTMapView, completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| data | url to GeoJSON resource. |
| mapView | MTMapView which holds the source. |
| completionHandler | A handler block to execute when function finishes. |

- 

setData(data:in:)

Asynchronous

Sets the data of the source.

Used for updating the source data.

#### Declaration

Swift
@MainActor
public func setData(data: URL, in mapView: MTMapView) async

#### Parameters

| data | url to GeoJSON resource. |
| mapView | MTMapView which holds the source. |

- 

addToMap(_:)

Adds source to map DSL style.

Prefer `addSource(_:)` on MTMapView instead.

#### Declaration

Swift
`public func addToMap(_ mapView: MTMapView)`

---

## File: Classes/MTGestureService.html

---
layout: mobile_sdk
title: "MTGestureService"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Service responsible for gesture handling and state."
id: mtgestureservice
breadcrumb: "Mobile SDK/iOS/Reference/Classes"
---

# MTGestureService

@MainActor
public class MTGestureService

Service responsible for gesture handling and state.

- 

enabledGestures

List of the enabled gestures on the map.

#### Declaration

Swift
@MainActor
public private(set) var enabledGestures: [MTGestureType : MTGesture] { get }

- 

disableGesture(with:completionHandler:)

Removes the gesture with the provided type from the map.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func disableGesture(with type: MTGestureType, completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| type | type of gesture to disable. |
| completionHandler | A handler block to execute when function finishes. |

- 

enableDragPanGesture(options:completionHandler:)

Enables drag to pan gesture.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func enableDragPanGesture(
options: MTDragPanOptions? = nil,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| options | Drag to pan options (optional). |
| completionHandler | A handler block to execute when function finishes. |

- 

enablePinchRotateAndZoomGesture(completionHandler:)

Enables pinch to rotate and zoom gesture.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func enablePinchRotateAndZoomGesture(completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| completionHandler | A handler block to execute when function finishes. |

- 

enableTwoFingerDragPitchGesture(completionHandler:)

Enables two fingers drag pitch gesture.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func enableTwoFingerDragPitchGesture(completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

- 

enableDoubleTapZoomInGesture(completionHandler:)

Enables double tap zoom in gesture.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func enableDoubleTapZoomInGesture(completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| completionHandler | A handler block to execute when function finishes. |

- 

setDoubleTapSensitivity(_:)

Sets the double tap sensitivity level (i.e. required time between taps).

Note
Default: 0.4

#### Declaration

Swift
@MainActor
public func setDoubleTapSensitivity(_ sensitivity: Double)

#### Parameters

| completionHandler | A handler block to execute when function finishes. |

- 

disableGesture(with:)

Asynchronous

Removes the gesture with the provided type from the map.

#### Declaration

Swift
@MainActor
public func disableGesture(with type: MTGestureType) async

#### Parameters

| type | type of gesture to disable. |

- 

enableDragPanGesture(options:)

Asynchronous

Enables drag to pan gesture.

#### Declaration

Swift
@MainActor
public func enableDragPanGesture(options: MTDragPanOptions? = nil) async

#### Parameters

| options | Drag to pan options (optional). |

- 

enablePinchRotateAndZoomGesture()

Asynchronous

Enables pinch to rotate and zoom gesture.

#### Declaration

Swift
@MainActor
public func enablePinchRotateAndZoomGesture() async

- 

enableTwoFingerDragPitchGesture()

Asynchronous

Enables two fingers drag pitch gesture.

#### Declaration

Swift
@MainActor
public func enableTwoFingerDragPitchGesture() async

- 

enableDoubleTapZoomInGesture()

Asynchronous

Enables double tap zoom in gesture.

#### Declaration

Swift
@MainActor
public func enableDoubleTapZoomInGesture() async

---

## File: Classes/MTHeatmapLayer.html

---
layout: mobile_sdk
title: "MTHeatmapLayer"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "A heatmap style layer renders a range of colors to represent the density of points in an area."
id: mtheatmaplayer
breadcrumb: "Mobile SDK/iOS/Reference/Classes"
---

# MTHeatmapLayer

`public class MTHeatmapLayer : MTLayer, @unchecked Sendable, Codable`
`extension MTHeatmapLayer: Equatable`

A heatmap style layer renders a range of colors to represent the density of points in an area.

Core properties

- 

identifier

Unique layer identifier.

#### Declaration

Swift
`public var identifier: String`

- 

type

Type of the layer.

#### Declaration

Swift
`public private(set) var type: MTLayerType { get }`

- 

sourceIdentifier

Identifier of the source to be used for this layer.

#### Declaration

Swift
`public var sourceIdentifier: String`

- 

maxZoom

The maximum zoom level for the layer. Optional number between 0 and 24.

#### Declaration

Swift
`public var maxZoom: Double?`

- 

minZoom

The minimum zoom level for the layer. Optional number between 0 and 24.

#### Declaration

Swift
`public var minZoom: Double?`

- 

sourceLayer

Layer to use from a vector tile source. Required for vector tile sources; prohibited for others.

#### Declaration

Swift
`public var sourceLayer: String?`

Paint properties

- 

color

Defines the color of each pixel based on its density value in a heatmap.
Should generally be an expression using [“heatmap-density”].

#### Declaration

Swift
`public var color: MTStyleValue?`

- 

intensity

Similar to heatmap-weight but controls the intensity of the heatmap globally.

#### Declaration

Swift
`public var intensity: MTStyleValue?`

- 

opacity

The global opacity at which the heatmap layer will be drawn.

#### Declaration

Swift
`public var opacity: MTStyleValue?`

- 

radius

Radius of influence of one heatmap point in pixels.

#### Declaration

Swift
`public var radius: MTStyleValue?`

- 

weight

A measure of how much an individual point contributes to the heatmap.

#### Declaration

Swift
`public var weight: MTStyleValue?`

Layout properties

- 

visibility

Whether this layer is displayed. Defaults to “visible”.

#### Declaration

Swift
`public var visibility: MTLayerVisibility?`

Optional filter hooks

- 

filterExpression

Inline filter expression to be embedded in the layer JSON.

#### Declaration

Swift
`public var filterExpression: MTPropertyValue?`

- 

initialFilter

Optional filter to apply after the layer is added to the map.

#### Declaration

Swift
`public var initialFilter: MTPropertyValue?`

Initializers

- 

init(identifier:sourceIdentifier:)

Initializes the layer with a unique identifier and source identifier.

#### Declaration

Swift
`public init(identifier: String, sourceIdentifier: String)`

- 

init(identifier:sourceIdentifier:maxZoom:minZoom:sourceLayer:color:intensity:opacity:radius:weight:visibility:)

Initializes the layer with all options.

#### Declaration

Swift
public init(
identifier: String,
sourceIdentifier: String,
maxZoom: Double? = nil,
minZoom: Double? = nil,
sourceLayer: String? = nil,
color: MTStyleValue? = nil,
intensity: MTStyleValue? = .number(1.0),
opacity: MTStyleValue? = .number(1.0),
radius: MTStyleValue? = .number(30.0),
weight: MTStyleValue? = .number(1.0),
visibility: MTLayerVisibility? = .visible
)

Codable

- 

init(from:)

#### Declaration

Swift
`public required init(from decoder: any Decoder) throws`

- 

encode(to:)

#### Declaration

Swift
`public func encode(to encoder: Encoder) throws`

- 

addToMap(_:)

Adds layer to map DSL style.

Prefer `addLayer(_:)` on MTMapView instead.

#### Declaration

Swift
`public func addToMap(_ mapView: MTMapView)`

- 

==(_:_:)

#### Declaration

Swift
`public static func == (lhs: MTHeatmapLayer, rhs: MTHeatmapLayer) -> Bool`

---

## File: Classes/MTHeatmapLayerHelper.html

---
layout: mobile_sdk
title: "MTHeatmapLayerHelper"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Helper for creating a heatmap visualization layer from data and styling options."
id: mtheatmaplayerhelper
breadcrumb: "Mobile SDK/iOS/Reference/Classes"
---

# MTHeatmapLayerHelper

`public final class MTHeatmapLayerHelper : MTVectorLayerHelper, @unchecked Sendable`

Helper for creating a heatmap visualization layer from data and styling options.

- 

style

Undocumented

#### Declaration

Swift
`public var style: MTStyle { get }`

- 

init(_:)

Undocumented

#### Declaration

Swift
`public init(_ style: MTStyle)`

- 

addHeatmap(_:in:completionHandler:)

Adds a heatmap layer based on the provided options.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func addHeatmap(
_ options: MTHeatmapLayerOptions,
in mapView: MTMapView,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

- 

addHeatmap(_:colorRamp:in:)

Asynchronous

Adds a heatmap layer using a color ramp.

#### Declaration

Swift
public func addHeatmap(
_ options: MTHeatmapLayerOptions,
colorRamp: MTColorRamp?,
in mapView: MTMapView
) async

---

## File: Classes/MTHillshadeLayer.html

---
layout: mobile_sdk
title: "MTHillshadeLayer"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "A hillshade style layer renders digital elevation model (DEM) data on the client-side.
Supports Terrain RGB and Mapzen Terrarium tiles via a raster-dem source."
id: mthillshadelayer
breadcrumb: "Mobile SDK/iOS/Reference/Classes"
---

# MTHillshadeLayer

`public class MTHillshadeLayer : MTLayer, @unchecked Sendable, Codable`

A hillshade style layer renders digital elevation model (DEM) data on the client-side.
Supports Terrain RGB and Mapzen Terrarium tiles via a `raster-dem` source.

Core properties

- 

identifier

Unique layer identifier.

#### Declaration

Swift
`public var identifier: String`

- 

type

Type of the layer.

#### Declaration

Swift
`public private(set) var type: MTLayerType { get }`

- 

sourceIdentifier

Identifier of the source to be used for this layer.

#### Declaration

Swift
`public var sourceIdentifier: String`

- 

maxZoom

The maximum zoom level for the layer.
Optional number between 0 and 24. At zoom levels equal to or greater than the maxzoom,
the layer will be hidden.

#### Declaration

Swift
`public var maxZoom: Double?`

- 

minZoom

The minimum zoom level for the layer.
Optional number between 0 and 24. At zoom levels less than the minzoom,
the layer will be hidden.

#### Declaration

Swift
`public var minZoom: Double?`

- 

sourceLayer

Layer to use from a vector tile source.
Required for vector tile sources; prohibited for all other source types.

#### Declaration

Swift
`public var sourceLayer: String?`

Paint properties

- 

accentColor

The shading color used to accentuate rugged terrain like sharp cliffs and gorges.
Optional color. Defaults to black (“#000000”).

#### Declaration

Swift
`public var accentColor: UIColor?`

- 

exaggeration

Intensity of the hillshade. Optional number between 0 and 1 inclusive. Defaults to 0.5.

#### Declaration

Swift
`public var exaggeration: Double?`

- 

highlightColor

The shading color of areas that face towards the light source. Defaults to white (“#FFFFFF”).

#### Declaration

Swift
`public var highlightColor: UIColor?`

- 

illuminationAnchor

Direction of light source when map is rotated. Defaults to “viewport”.

#### Declaration

Swift
`public var illuminationAnchor: MTHillshadeIlluminationAnchor?`

- 

illuminationDirection

The direction of the light source used to generate the hillshading with 0 as the top of the viewport
if hillshade-illumination-anchor is set to viewport and due north if set to map. Defaults to 335.

#### Declaration

Swift
`public var illuminationDirection: Double?`

- 

shadowColor

The shading color of areas that face away from the light source. Defaults to black (“#000000”).

#### Declaration

Swift
`public var shadowColor: UIColor?`

Layout properties

- 

visibility

Whether this layer is displayed. Defaults to “visible”.

#### Declaration

Swift
`public var visibility: MTLayerVisibility?`

Initializers

- 

init(identifier:sourceIdentifier:)

Initializes the layer with required identifiers.

#### Declaration

Swift
public init(
identifier: String,
sourceIdentifier: String
)

- 

init(identifier:sourceIdentifier:maxZoom:minZoom:sourceLayer:accentColor:exaggeration:highlightColor:illuminationAnchor:illuminationDirection:shadowColor:visibility:)

Initializes the layer with all options.

#### Declaration

Swift
public init(
identifier: String,
sourceIdentifier: String,
maxZoom: Double? = nil,
minZoom: Double? = nil,
sourceLayer: String? = nil,
accentColor: UIColor? = .black,
exaggeration: Double? = 0.5,
highlightColor: UIColor? = .white,
illuminationAnchor: MTHillshadeIlluminationAnchor? = .viewport,
illuminationDirection: Double? = 335.0,
shadowColor: UIColor? = .black,
visibility: MTLayerVisibility? = .visible
)

Codable

- 

init(from:)

Initializes the layer from the decoder.

#### Declaration

Swift
`public required init(from decoder: any Decoder) throws`

- 

encode(to:)

#### Declaration

Swift
`public func encode(to encoder: Encoder) throws`

- 

addToMap(_:)

Adds layer to map DSL style.

Prefer `addLayer(_:)` on MTMapView instead.

#### Declaration

Swift
`public func addToMap(_ mapView: MTMapView)`

Modifiers (not to be used outside DSL)

- 

maxZoom(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func maxZoom(_ value: Double) -> Self

- 

minZoom(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func minZoom(_ value: Double) -> Self

- 

sourceLayer(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func sourceLayer(_ value: String) -> Self

- 

accentColor(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func accentColor(_ value: UIColor) -> Self

- 

exaggeration(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func exaggeration(_ value: Double) -> Self

- 

highlightColor(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func highlightColor(_ value: UIColor) -> Self

- 

illuminationAnchor(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func illuminationAnchor(_ value: MTHillshadeIlluminationAnchor) -> Self

- 

illuminationDirection(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func illuminationDirection(_ value: Double) -> Self

- 

shadowColor(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func shadowColor(_ value: UIColor) -> Self

- 

visibility(_:)

Undocumented

#### Declaration

Swift
@discardableResult
public func visibility(_ value: MTLayerVisibility) -> Self

---

## File: Classes/MTImageSource.html

---
layout: mobile_sdk
title: "MTImageSource"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "An image source."
id: mtimagesource
breadcrumb: "Mobile SDK/iOS/Reference/Classes"
---

# MTImageSource

`public class MTImageSource : MTSource, @unchecked Sendable`

An image source.

The `url` value contains the image location.
The `coordinates` array contains [longitude, latitude] pairs for the image corners
listed in clockwise order: top left, top right, bottom right, bottom left.

- 

identifier

Unique id of the source.

#### Declaration

Swift
`public var identifier: String`

- 

url

URL that points to an image.

#### Declaration

Swift
`public var url: URL?`

- 

coordinates

Corners of image specified as `CLLocationCoordinate2D`.
Clockwise order: top-left, top-right, bottom-right, bottom-left.

#### Declaration

Swift
`public var coordinates: [CLLocationCoordinate2D]`

- 

type

Type of the source.

#### Declaration

Swift
`public private(set) var type: MTSourceType { get }`

- 

init(identifier:url:coordinates:)

Initializes the image source with required values.

#### Declaration

Swift
`public init(identifier: String, url: URL, coordinates: [CLLocationCoordinate2D])`

#### Parameters

| identifier | Unique id of the source. |
| url | URL to the image resource. |
| coordinates | Corners of image in clockwise order using `CLLocationCoordinate2D`. |

Operations

- 

setCoordinates(_:in:completionHandler:)

Updates the coordinates of the image source.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setCoordinates(
_ coordinates: [CLLocationCoordinate2D],
in mapView: MTMapView,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| coordinates | New corners of the image using `CLLocationCoordinate2D`. |
| mapView | MTMapView which holds the source. |
| completionHandler | A handler block to execute when function finishes. |

- 

updateImage(url:coordinates:in:completionHandler:)

Updates the image URL and coordinates simultaneously.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func updateImage(
url: URL,
coordinates: [CLLocationCoordinate2D],
in mapView: MTMapView,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| url | New image URL. |
| coordinates | New corners of the image using `CLLocationCoordinate2D`. |
| mapView | MTMapView which holds the source. |
| completionHandler | A handler block to execute when function finishes. |

Concurrency

- 

setCoordinates(_:in:)

Asynchronous

Updates the coordinates of the image source.

#### Declaration

Swift
@MainActor
public func setCoordinates(_ coordinates: [CLLocationCoordinate2D], in mapView: MTMapView) async

#### Parameters

| coordinates | New corners of the image using `CLLocationCoordinate2D`. |
| mapView | MTMapView which holds the source. |

- 

updateImage(url:coordinates:in:)

Asynchronous

Updates the image URL and coordinates simultaneously.

#### Declaration

Swift
@MainActor
public func updateImage(url: URL, coordinates: [CLLocationCoordinate2D], in mapView: MTMapView) async

#### Parameters

| url | New image URL. |
| coordinates | New corners of the image using `CLLocationCoordinate2D`. |
| mapView | MTMapView which holds the source. |

DSL

- 

addToMap(_:)

Adds source to map DSL style.

Prefer `addSource(_:)` on MTMapView instead.

#### Declaration

Swift
`public func addToMap(_ mapView: MTMapView)`

---

## File: Classes/MTLineLayer.html

---
layout: mobile_sdk
title: "MTLineLayer"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "The line style layer that renders one or more stroked polylines on the map."
id: mtlinelayer
breadcrumb: "Mobile SDK/iOS/Reference/Classes"
---

# MTLineLayer

`public class MTLineLayer : MTLayer, @unchecked Sendable, Codable`

The line style layer that renders one or more stroked polylines on the map.

- 

identifier

Unique layer identifier.

#### Declaration

Swift
`public var identifier: String`

- 

type

Type of the layer.

#### Declaration

Swift
`public private(set) var type: MTLayerType { get }`

- 

sourceIdentifier

Identifier of the source to be used for this layer.

#### Declaration

Swift
`public var sourceIdentifier: String`

- 

maxZoom

The maximum zoom level for the layer.

Optional number between 0 and 24. At zoom levels equal to or greater than the maxzoom,
the layer will be hidden.

#### Declaration

Swift
`public var maxZoom: Double?`

- 

minZoom

The minimum zoom level for the layer.

Optional number between 0 and 24. At zoom levels less than the minzoom,
the layer will be hidden.

#### Declaration

Swift
`public var minZoom: Double?`

- 

sourceLayer

Layer to use from a vector tile source.

Required for vector tile sources; prohibited for all other source types,
including GeoJSON sources.

#### Declaration

Swift
`public var sourceLayer: String?`

- 

blur

Blur of the line.

#### Declaration

Swift
`public var blur: Double?`

- 

cap

The display of line endings.

#### Declaration

Swift
`public var cap: MTLineCap?`

- 

color

The color with which the line will be drawn.

#### Declaration

Swift
`public var color: UIColor?`

- 

dashArray

The lengths of the alternating dashes and gaps that form the dash pattern.

#### Declaration

Swift
`public var dashArray: [Double]?`

- 

gapWidth

Line casing outside of a line’s actual path.

#### Declaration

Swift
`public var gapWidth: Double?`

- 

gradient

The gradient with which to color a line feature.

Can only be used with GeoJSON sources that specify “lineMetrics”: true.

#### Declaration

Swift
`public var gradient: UIColor?`

- 

join

The display of lines when joining.

#### Declaration

Swift
`public var join: MTLineJoin?`

- 

miterLimit

Used to automatically convert miter joins to bevel joins for sharp angles.

Requires join to be “miter”.

#### Declaration

Swift
`public var miterLimit: Double?`

- 

offset

The line’s offset.

For linear features, a positive value offsets the line to the right, relative to the
direction of the line, and a negative value to the left. For polygon features, a
positive value results in an inset, and a negative value results in an outset.

#### Declaration

Swift
`public var offset: Double?`

- 

opacity

Optional number between 0 and 1 inclusive.

#### Declaration

Swift
`public var opacity: Double?`

- 

roundLimit

Used to automatically convert round joins to miter joins for shallow angles.

#### Declaration

Swift
`public var roundLimit: Double?`

- 

sortKey

Feature ordering value.

Features with a higher sort key will appear above features with a lower sort key.

#### Declaration

Swift
`public var sortKey: Double?`

- 

translate

The geometry’s offset.

Values are [x, y] where negatives indicate left and up, respectively.

#### Declaration

Swift
`public var translate: [Double]?`

- 

translateAnchor

Controls the frame of reference for translate.

#### Declaration

Swift
`public var translateAnchor: MTLineTranslateAnchor?`

- 

width

Width of the line.

#### Declaration

Swift
`public var width: Double?`

- 

visibility

Enum controlling whether this layer is displayed.

#### Declaration

Swift
`public var visibility: MTLayerVisibility?`

- 

initialFilter

Optional initial filter to apply after the layer is added to the map.

#### Declaration

Swift
`public var initialFilter: MTPropertyValue?`

- 

init(identifier:sourceIdentifier:maxZoom:minZoom:sourceLayer:)

Initializes the layer with unique identifier, source identifier, max and min zoom levels and source layer,
which is required for vector tile sources.

#### Declaration

Swift
public init(
identifier: String,
sourceIdentifier: String,
maxZoom: Double,
minZoom: Double,
sourceLayer: String? = nil
)

- 

init(identifier:sourceIdentifier:maxZoom:minZoom:sourceLayer:blur:cap:color:dashArray:gapWidth:gradient:join:miterLimit:offset:opacity:roundLimit:sortKey:translate:translateAnchor:width:visibility:)

Initializes the layer with all options.

#### Declaration

Swift
public init(
identifier: String,
sourceIdentifier: String,
maxZoom: Double? = nil,
minZoom: Double? = nil,
sourceLayer: String? = nil,
blur: Double? = 0.0,
cap: MTLineCap? = .butt,
color: UIColor? = .black,
dashArray: [Double]? = nil,
gapWidth: Double? = 0.0,
gradient: UIColor? = nil,
join: MTLineJoin? = .miter,
miterLimit: Double? = 2.0,
offset: Double? = 0.0,
opacity: Double? = 1.0,
roundLimit: Double? = 1.05,
sortKey: Double? = nil,
translate: [Double]? = [0.0, 0.0],
translateAnchor: MTLineTranslateAnchor? = .map,
width: Double? = 1.0,
visibility: MTLayerVisibility? = .visible
)

- 

init(from:)

Initializes layer from the decoder.

#### Declaration

Swift
`public required init(from decoder: any Decoder) throws`

- 

encode(to:)

#### Declaration

Swift
`public func encode(to encoder: Encoder) throws`

- 

addToMap(_:)

Adds layer to map DSL style.

Prefer `addLayer(_:)` on MTMapView instead.

#### Declaration

Swift
`public func addToMap(_ mapView: MTMapView)`

- 

maxZoom(_:)

Modifier. Sets the `maxZoom`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func maxZoom(_ value: Double) -> Self

- 

minZoom(_:)

Modifier. Sets the `minZoom`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func minZoom(_ value: Double) -> Self

- 

sourceLayer(_:)

Modifier. Sets the `sourceLayer`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func sourceLayer(_ value: String) -> Self

- 

blur(_:)

Modifier. Sets the `blur`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func blur(_ value: Double) -> Self

- 

cap(_:)

Modifier. Sets the `cap`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func cap(_ value: MTLineCap) -> Self

- 

color(_:)

Modifier. Sets the `color`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func color(_ value: UIColor) -> Self

- 

dashArray(_:)

Modifier. Sets the `dashArray`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func dashArray(_ value: [Double]) -> Self

- 

gapWidth(_:)

Modifier. Sets the `gapWidth`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func gapWidth(_ value: Double) -> Self

- 

gradient(_:)

Modifier. Sets the `gradient`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func gradient(_ value: UIColor) -> Self

- 

join(_:)

Modifier. Sets the `join`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func join(_ value: MTLineJoin) -> Self

- 

miterLimit(_:)

Modifier. Sets the `miterLimit`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func miterLimit(_ value: Double) -> Self

- 

offset(_:)

Modifier. Sets the `offset`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func offset(_ value: Double) -> Self

- 

opacity(_:)

Modifier. Sets the `opacity`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func opacity(_ value: Double) -> Self

- 

roundLimit(_:)

Modifier. Sets the `roundLimit`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func roundLimit(_ value: Double) -> Self

- 

sortKey(_:)

Modifier. Sets the `sortKey`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func sortKey(_ value: Double) -> Self

- 

translate(_:)

Modifier. Sets the `translate`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func translate(_ value: [Double]) -> Self

- 

translateAnchor(_:)

Modifier. Sets the `translateAnchor`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func translateAnchor(_ value: MTLineTranslateAnchor) -> Self

- 

width(_:)

Modifier. Sets the `width`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func width(_ value: Double) -> Self

- 

visibility(_:)

Modifier. Sets the `visibility`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func visibility(_ value: MTLayerVisibility) -> Self

---

## File: Classes/MTLocationManager.html

---
layout: mobile_sdk
title: "MTLocationManager"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Class responsible for location updates."
id: mtlocationmanager
breadcrumb: "Mobile SDK/iOS/Reference/Classes"
---

# MTLocationManager

`public class MTLocationManager : NSObject, @preconcurrency CLLocationManagerDelegate`

Class responsible for location updates.

- 

init(using:accuracy:)

Initializes the location manager.

#### Declaration

Swift
`public init(using manager: CLLocationManager? = nil, accuracy: CLLocationAccuracy? = nil)`

- 

startLocationUpdates()

Starts the location updates.

Updates are available in didUpdateLocations method.

#### Declaration

Swift
`public func startLocationUpdates()`

- 

requestLocationOnce()

Requests location only once and calls didUpdateLocations delegate method.

#### Declaration

Swift
`public func requestLocationOnce()`

- 

stopLocationUpdates()

Stops the location updates.

#### Declaration

Swift
`public func stopLocationUpdates()`

- 

requestLocationPermission()

Requests whenInUse location permission.

#### Declaration

Swift
@MainActor
public func requestLocationPermission()

- 

requestAlwaysLocationPermission()

Requests always location permission.

Make sure whenInUse location permission is active first.

#### Declaration

Swift
@MainActor
public func requestAlwaysLocationPermission()

- 

locationManager(_:didUpdateLocations:)

Undocumented

#### Declaration

Swift
@MainActor
public func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation])

- 

locationManager(_:didFailWithError:)

Undocumented

#### Declaration

Swift
@MainActor
public func locationManager(_ manager: CLLocationManager, didFailWithError error: Error)

---

## File: Classes/MTLogger.html

---
layout: mobile_sdk
title: "MTLogger"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Logger class used for SDK logs."
id: mtlogger
breadcrumb: "Mobile SDK/iOS/Reference/Classes"
---

# MTLogger

`public class MTLogger`

Logger class used for SDK logs.

- 

infoMarker

Log marker for information messages.

#### Declaration

Swift
`public static let infoMarker: String`

- 

log(_:type:)

Add a log.

#### Declaration

Swift
`public static func log(_ message: String, type: MTLogType)`

- 

printLogs()

Print all current logs to the console.

#### Declaration

Swift
`public static func printLogs()`

- 

setCustomLogger(_:)

Inject a custom logger conforming to the MTLoggable protocol.

#### Declaration

Swift
`public static func setCustomLogger(_ logger: MTLoggable)`

---

## File: Classes/MTMapCameraHelper.html

---
layout: mobile_sdk
title: "MTMapCameraHelper"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Sets combination of center, bearing and pitch, as well as roll and elevation."
id: mtmapcamerahelper
breadcrumb: "Mobile SDK/iOS/Reference/Classes"
---

# MTMapCameraHelper

`public class MTMapCameraHelper`

Sets combination of center, bearing and pitch, as well as roll and elevation.

- 

centerCoordinate

The geographical centerpoint of the map.

If center is not specified, SDK will look for it in the map style object.
If it is not specified in the style, it will default to (latitude: 0.0, longitude: 0.0).

#### Declaration

Swift
`public var centerCoordinate: CLLocationCoordinate2D?`

- 

bearing

The bearing of the map, measured in degrees counter-clockwise from north.

If bearing is not specified, SDK will look for it in the map style object.
If it is not specified in the style, it will default to 0.0.

#### Declaration

Swift
`public var bearing: Double?`

- 

pitch

The pitch (tilt) of the map, measured in degrees away from the plane of the screen (0-85).

If pitch is not specified, SDK will look for it in the map style object.
If it is not specified in the style, it will default to 0.0.

#### Declaration

Swift
`public var pitch: Double?`

- 

roll

The roll angle of the map, measured in degrees counter-clockwise about the camera boresight.

If roll is not specified, SDK will look for it in the map style object.
If it is not specified in the style, it will default to 0.0.

#### Declaration

Swift
`public var roll: Double?`

- 

elevation

The elevation of the geographical centerpoint of the map, in meters above sea level.

If elevation is not specified, SDK will look for it in the map style object.
If it is not specified in the style, it will default to 0.0.

#### Declaration

Swift
`public var elevation: Double?`

- 

getCamera()

Returns camera object with all properties set to 0.

#### Declaration

Swift
`public static func getCamera() -> MTMapCameraHelper`

- 

getCameraFromMapStyle()

Returns camera object initialized from map style options.

If any of the properties is not set within the style, it will default to 0.

#### Declaration

Swift
`public static func getCameraFromMapStyle() -> MTMapCameraHelper`

- 

getCameraWith(_:)

Returns camera object constructed from given options object.

#### Declaration

Swift
`public static func getCameraWith(_ options: MTMapOptions) -> MTMapCameraHelper`

#### Parameters

| options | MTMapOptions object with initial camera options. |

- 

cameraLookingAtCenterCoordinate(_:bearing:pitch:roll:elevation:)

Returns camera object with the given center coordinate, bearing, pitch, roll and elevation.

#### Declaration

Swift
public static func cameraLookingAtCenterCoordinate(
_ centerCoordinate: CLLocationCoordinate2D,
bearing: Double,
pitch: Double,
roll: Double,
elevation: Double
) -> MTMapCameraHelper

#### Parameters

| centerCoordinate | Latitude and longitude pair. |
| bearing | Bearing of the map, measured in degrees counter-clockwise from north. |
| pitch | Pitch of the map, measured in degrees away from the plane of the screen (0-85). |
| roll | Roll angle of the map, measured in degrees counter-clockwise about the camera boresight. |
| elevation | Elevation of the initial geographical centerpoint of the map, in meters above sea level. |

- 

cameraLookingAtCenterCoordinate(_:bearing:pitch:)

Returns camera object with the given center coordinate, bearing and pitch.

Looks for roll and elevation in the map’s style object.
If they are not specified in the style, they will default to 0.

#### Declaration

Swift
public static func cameraLookingAtCenterCoordinate(
_ centerCoordinate: CLLocationCoordinate2D,
bearing: Double,
pitch: Double
) -> MTMapCameraHelper

#### Parameters

| centerCoordinate | Latitude and longitude pair. |
| bearing | Bearing of the map, measured in degrees counter-clockwise from north. |
| pitch | Pitch of the map, measured in degrees away from the plane of the screen (0-85). |

- 

isEqualToMapCameraHelper(_:)

Returns a Boolean indicating whether the camera object is equal to the receiver.

#### Declaration

Swift
`public func isEqualToMapCameraHelper(_ camera: MTMapCameraHelper) -> Bool`

#### Parameters

| camera | MTMapCamera object to compare with. |

---

## File: Classes/MTMapView.html

---
layout: mobile_sdk
title: "MTMapView"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Object representing the map on the screen."
id: mtmapview
breadcrumb: "Mobile SDK/iOS/Reference/Classes"
---

# MTMapView

@MainActor
open class MTMapView : UIView, Sendable
`extension MTMapView: MTControllable`
`extension MTMapView: MTNavigable`
`extension MTMapView: MTRendering`
`extension MTMapView: MTStylable`
`extension MTMapView: MTZoomable`
`extension MTMapView: MTLocationManagerDelegate`

Object representing the map on the screen.

Exposes methods and properties that enable changes to the map,
and fires events that can be interacted with.

- 

style

Proxy style object of the map.

#### Declaration

Swift
@MainActor
public private(set) var style: MTStyle? { get }

- 

locationManager

Undocumented

#### Declaration

Swift
@MainActor
public private(set) var locationManager: MTLocationManager? { get set }

- 

options

Current options of the map object.

#### Declaration

Swift
@MainActor
public var options: MTMapOptions?

- 

gestureService

Service responsible for gestures handling

#### Declaration

Swift
@MainActor
public var gestureService: MTGestureService!

- 

delegate

Delegate object responsible for event propagation

#### Declaration

Swift
@MainActor
public weak var delegate: MTMapViewDelegate?

- 

isInitialized

Boolean indicating whether map is initialized,

#### Declaration

Swift
@MainActor
public private(set) var isInitialized: Bool { get }

- 

didInitialize

Triggers when map initializes for the first time.

#### Declaration

Swift
@MainActor
public var didInitialize: (() -> Void)?

- 

init(frame:)

Initializes the map with the frame.

#### Declaration

Swift
@MainActor
override public init(frame: CGRect)

- 

init(coder:)

Initializes the map with the coder.

#### Declaration

Swift
@MainActor
required public init?(coder: NSCoder)

- 

init(frame:options:referenceStyle:styleVariant:)

Initializes the map with the frame, options and style.

#### Declaration

Swift
@MainActor
convenience public init(
frame: CGRect,
options: MTMapOptions,
referenceStyle: MTMapReferenceStyle,
styleVariant: MTMapStyleVariant? = nil
)

- 

init(options:)

Initializes the map with the options.

#### Declaration

Swift
@MainActor
convenience public init(options: MTMapOptions?)

- 

initLocationTracking(using:accuracy:)

Initializes location tracking manager.

In order to track user location you have to initialize the MLLocationManager,
add necessary Privacy Location messages to Info.plist, subscribe to MTLocationManagerDelegate
and start location updates and/or request location once via the locationManager property on MTMapView.

#### Declaration

Swift
@MainActor
public func initLocationTracking(using manager: CLLocationManager? = nil, accuracy: CLLocationAccuracy? = nil)

#### Parameters

| manager | Optional external CLLocationManager to use. |
| accuracy | Optional desired accuracy to use. |

- 

layoutSubviews()

Undocumented

#### Declaration

Swift
@MainActor
open override func layoutSubviews()

- 

reload()

Reloads the map view.

#### Declaration

Swift
@MainActor
public func reload()

- 

convertGPXToGeoJSON(_:)

Asynchronous

Converts a GPX document string to a GeoJSON FeatureCollection JSON string.

#### Declaration

Swift
@MainActor
func convertGPXToGeoJSON(_ gpxString: String) async throws -> String

#### Parameters

| gpxString | Raw GPX XML content. |

#### Return Value

A GeoJSON FeatureCollection encoded as a JSON string.

- 

convertKMLToGeoJSON(_:)

Asynchronous

Converts a KML document string to a GeoJSON FeatureCollection JSON string.

#### Declaration

Swift
@MainActor
func convertKMLToGeoJSON(_ kmlString: String) async throws -> String

#### Parameters

| kmlString | Raw KML XML content. |

#### Return Value

A GeoJSON FeatureCollection encoded as a JSON string.

- 

addMapTilerLogoControl(position:completionHandler:)

Adds Maptiler logo to the map.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func addMapTilerLogoControl(
position: MTMapCorner,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| position | The corner position of the logo. |
| completionHandler | A handler block to execute when function finishes. |

- 

addLogoControl(name:logoURL:linkURL:position:completionHandler:)

Adds logo control to the map.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func addLogoControl(
name: String,
logoURL: URL,
linkURL: URL,
position: MTMapCorner,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| name | Unique name of the logo. |
| logoURL | URL of logo image. |
| linkURL | URL of logo link. |
| position | The corner position of the logo. |
| completionHandler | A handler block to execute when function finishes. |

- 

addMapTilerLogoControl(position:)

Asynchronous

Adds Maptiler logo to the map.

#### Declaration

Swift
@MainActor
public func addMapTilerLogoControl(position: MTMapCorner) async

#### Parameters

| name | Unique name of the logo. |
| position | The corner position of the logo. |

- 

addLogoControl(name:logoURL:linkURL:position:)

Asynchronous

Adds logo control to the map.

#### Declaration

Swift
@MainActor
public func addLogoControl(name: String, logoURL: URL, linkURL: URL, position: MTMapCorner) async

#### Parameters

| name | Unique name of the logo. |
| logoURL | URL of logo image. |
| linkURL | URL of logo link. |
| position | The corner position of the logo. |

- 

setBearing(_:completionHandler:)

Sets the bearing of the map.

The bearing is the compass direction that is “up”;
for example, a bearing of 90° orients the map so that east is up.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setBearing(_ bearing: Double, completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| bearing | The desired bearing. |
| completionHandler | A handler block to execute when function finishes. |

- 

setCenter(_:completionHandler:)

Sets the map’s geographical centerpoint.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setCenter(
_ center: CLLocationCoordinate2D,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| center | The desired center coordinate. |
| completionHandler | A handler block to execute when function finishes. |

- 

flyTo(_:options:animationOptions:completionHandler:)

Changes any combination of center, zoom, bearing, and pitch.

The animation seamlessly incorporates zooming and panning to help the user maintain her bearings
even after traversing a great distance.

Note
The animation will be skipped, and this will behave equivalently to jumpTo
if the user has the reduced motion accessibility feature enabled,
unless options includes essential: true.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func flyTo(
_ center: CLLocationCoordinate2D,
options: MTFlyToOptions?,
animationOptions: MTAnimationOptions?,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| center | The desired center coordinate. |
| options | Custom options to use. |
| animationOptions | Optional animation options to use. |
| completionHandler | A handler block to execute when function finishes. |

- 

easeTo(_:options:animationOptions:completionHandler:)

Changes any combination of center, zoom, bearing, pitch, and padding.

The map will retain its current values for any details not specified in options.

Note
The transition will happen instantly if the user has enabled the reduced motion accessibility feature,
unless options includes essential: true.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func easeTo(
_ center: CLLocationCoordinate2D,
options: MTCameraOptions?,
animationOptions: MTAnimationOptions?,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| center | The desired center coordinate. |
| options | Custom options to use. |
| animationOptions | Optional animation options to use. |
| completionHandler | A handler block to execute when function finishes. |

- 

jumpTo(_:options:completionHandler:)

Changes any combination of center, zoom, bearing, and pitch, without an animated transition.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func jumpTo(
_ center: CLLocationCoordinate2D,
options: MTCameraOptions?,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| center | The desired center coordinate. |
| options | Custom options to use. |
| completionHandler | A handler block to execute when function finishes. |

- 

fitBounds(_:options:completionHandler:)

Fits the map so the provided bounds are fully visible within the viewport.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func fitBounds(
_ bounds: MTBounds,
options fitOptions: MTFitBoundsOptions? = nil,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| bounds | Geographic bounds to display. |
| fitOptions | Additional configuration that controls the fitting animation. |
| completionHandler | A handler block to execute when function finishes. |

- 

setPadding(_:completionHandler:)

Sets the padding in pixels around the viewport.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setPadding(_ options: MTPaddingOptions, completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| options | Custom options to use. |
| completionHandler | A handler block to execute when function finishes. |

- 

fitToIpBounds(completionHandler:)

Fits the map to the bounds inferred from the current IP address.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func fitToIpBounds(completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| completionHandler | A handler block to execute when function finishes. |

- 

centerOnIpPoint(completionHandler:)

Centers the map on the location inferred from the current IP address.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func centerOnIpPoint(completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| completionHandler | A handler block to execute when function finishes. |

- 

setIsCenterClampedToGround(_:completionHandler:)

Sets the value of centerClampedToGround.

If true, the elevation of the center point will automatically be set to the terrain elevation
(or zero if terrain is not enabled).
If false, the elevation of the center point will default to sea level and will not automatically update.
Needs to be set to false to keep the camera above ground when pitch > 90 degrees.

Note
Defaults to true.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setIsCenterClampedToGround(
_ isCenterClampedToGround: Bool,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| isCenterClampedToGround | The boolean value indicating if center will be clamped to ground. |
| completionHandler | A handler block to execute when function finishes. |

- 

setCenterElevation(_:completionHandler:)

Sets the elevation of the map’s center point, in meters above sea level.

Note
Triggers the following events: moveStart and moveEnd.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setCenterElevation(_ elevation: Double, completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| elevation | The desired elevation. |
| completionHandler | A handler block to execute when function finishes. |

- 

setMaxPitch(_:completionHandler:)

Sets or clears the map’s maximum pitch.

If the map’s current pitch is higher than the new maximum, the map will pitch to the new maximum.
If null is provided, the function removes the current maximum pitch (sets it to 60).

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setMaxPitch(_ maxPitch: Double?, completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| maxPitch | The maximum pitch to set (0-85). |
| completionHandler | A handler block to execute when function finishes. |

- 

setMaxZoom(_:completionHandler:)

Sets or clears the map’s maximum zoom.

If the map’s current zoom level is higher than the new maximum, the map will zoom to the new maximum.
If null or undefined is provided, the function removes the current maximum zoom (sets it to 22).

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setMaxZoom(_ maxZoom: Double?, completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| maxZoom | The maximum zoom level to set. |
| completionHandler | A handler block to execute when function finishes. |

- 

setMinPitch(_:completionHandler:)

Sets or clears the map’s minimum pitch.

If the map’s current pitch is lower than the new minimum, the map will pitch to the new minimum.
If null is provided, the function removes the current minimum pitch (i.e. sets it to 0).

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setMinPitch(_ minPitch: Double?, completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| minPitch | The minimum pitch to set (0-85) |
| completionHandler | A handler block to execute when function finishes. |

- 

setMinZoom(_:completionHandler:)

Sets or clears the map’s minimum zoom.

If the map’s current zoom level is lower than the new minimum, the map will zoom to the new minimum.
If null  is provided, the function removes the current minimum zoom (i.e. sets it to -2).

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setMinZoom(_ minZoom: Double?, completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| minZoom | The minimum zoom level to set (-2 - 24). |
| completionHandler | A handler block to execute when function finishes. |

- 

setMaxBounds(_:completionHandler:)

Sets or clears the map’s maximum bounds constraint.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setMaxBounds(
_ bounds: MTBounds?,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| bounds | The bounds to constrain panning to, or `nil` to remove the constraint. |
| completionHandler | A handler block to execute when function finishes. |

- 

setPitch(_:completionHandler:)

Sets the map’s pitch (tilt).

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setPitch(_ pitch: Double, completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| pitch | The pitch to set, measured in degrees away from the plane of the screen (0-60). |
| completionHandler | A handler block to execute when function finishes. |

- 

setRoll(_:completionHandler:)

Sets the map’s roll angle.

Note
Triggers the following events: moveStart, moveEnd, rollStart, and rollEnd.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setRoll(_ roll: Double, completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| roll | The roll to set, measured in degrees about the camera boresight. |
| completionHandler | A handler block to execute when function finishes. |

- 

setViewport(with:zoomLevel:)

Set combination of center, bearing, pitch, roll and elevation.

#### Declaration

Swift
@MainActor
public func setViewport(with cameraHelper: MTMapCameraHelper, zoomLevel: Double? = nil)

#### Parameters

| cameraHelper | Helper to use for setting the viewport. |
| zoomLevel | Desired zoom level to set. |

- 

getPitch(completionHandler:)

Returns the map’s current pitch (tilt).

The map’s current pitch, measured in degrees away from the plane of the screen.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func getPitch(completionHandler: @escaping (Result<Double, MTError>) -> Void)

#### Parameters

| completionHandler | A handler block to execute when function finishes. |

- 

getMaxPitch(completionHandler:)

Returns the map’s maximum pitch (tilt).

The map’s maximum pitch, measured in degrees away from the plane of the screen.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func getMaxPitch(completionHandler: @escaping (Result<Double, MTError>) -> Void)

#### Parameters

| completionHandler | A handler block to execute when function finishes. |

- 

getMaxZoom(completionHandler:)

Returns the map’s maximum zoom.

The map’s maximum zoom level.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func getMaxZoom(completionHandler: @escaping (Result<Double, MTError>) -> Void)

#### Parameters

| completionHandler | A handler block to execute when function finishes. |

- 

getMinPitch(completionHandler:)

Returns the map’s minimum pitch (tilt).

The map’s minimum pitch, measured in degrees away from the plane of the screen.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func getMinPitch(completionHandler: @escaping (Result<Double, MTError>) -> Void)

#### Parameters

| completionHandler | A handler block to execute when function finishes. |

- 

getMinZoom(completionHandler:)

Returns the map’s minimum zoom.

The map’s minimum zoom level.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func getMinZoom(completionHandler: @escaping (Result<Double, MTError>) -> Void)

#### Parameters

| completionHandler | A handler block to execute when function finishes. |

- 

panBy(_:completionHandler:)

Pans the map by the specified offset.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func panBy(_ offset: MTPoint, completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| offset | The x and y coordinates by which to pan the map. |
| completionHandler | A handler block to execute when function finishes. |

- 

panTo(_:completionHandler:)

Pans the map to the specified location with an animated transition.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func panTo(
_ coordinates: CLLocationCoordinate2D,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| coordinates | The location to pan the map to. |
| completionHandler | A handler block to execute when function finishes. |

- 

stop(completionHandler:)

Stops any ongoing animated transition.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func stop(completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| completionHandler | A handler block to execute when function finishes. |

- 

snapToNorth(animationOptions:completionHandler:)

Snaps the map so that north is up.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func snapToNorth(
animationOptions: MTAnimationOptions? = nil,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| animationOptions | Animation options. |
| completionHandler | A handler block to execute when function finishes. |

- 

getCenter(completionHandler:)

Returns the map’s current center.

The map’s current geographical center.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func getCenter(completionHandler: @escaping (Result<CLLocationCoordinate2D, MTError>) -> Void)

- 

getBounds(completionHandler:)

Returns the map’s current geographic bounds.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func getBounds(completionHandler: @escaping (Result<MTBounds, MTError>) -> Void)

#### Parameters

| completionHandler | A handler block to execute when function finishes. |

- 

getMaxBounds(completionHandler:)

Returns the maximum bounds constraint applied to the map, if any.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func getMaxBounds(completionHandler: @escaping (Result<MTBounds?, MTError>) -> Void)

#### Parameters

| completionHandler | A handler block to execute when function finishes. |

- 

getCenterClampedToGround(completionHandler:)

Returns whether the map’s center is clamped to the ground.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func getCenterClampedToGround(completionHandler: @escaping (Result<Bool, MTError>) -> Void)

#### Parameters

| completionHandler | A handler block to execute when function finishes. |

- 

getCenterElevation(completionHandler:)

Returns the elevation of the map’s center point, in meters above sea level.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func getCenterElevation(completionHandler: @escaping (Result<Double, MTError>) -> Void)

#### Parameters

| completionHandler | A handler block to execute when function finishes. |

- 

getCameraTargetElevation(completionHandler:)

Returns the elevation for the point where the camera is looking,
in meters above sea level multiplied by exaggeration.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func getCameraTargetElevation(completionHandler: @escaping (Result<Double, MTError>) -> Void)

#### Parameters

| completionHandler | A handler block to execute when function finishes. |

- 

project(coordinates:completionHandler:)

Project coordinates to point on the container.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func project(
coordinates: CLLocationCoordinate2D,
completionHandler: @escaping (Result<CLLocationCoordinate2D, MTError>) -> Void
)

#### Parameters

| coordinates | The location to project. |
| completionHandler | A handler block to execute when function finishes. |

- 

unproject(point:completionHandler:)

Unproject screen coordinates to geographical coordinates.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func unproject(
point: MTPoint,
completionHandler: @escaping (Result<CLLocationCoordinate2D, MTError>) -> Void
)

#### Parameters

| point | The screen coordinates to unproject. |
| completionHandler | A handler block to execute when function finishes. |

- 

getBearing(completionHandler:)

Returns the map’s current bearing.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func getBearing(completionHandler: @escaping (Result<Double, MTError>) -> Void)

#### Parameters

| completionHandler | A handler block to execute when function finishes. |

- 

getRoll(completionHandler:)

Returns the map’s current roll.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func getRoll(completionHandler: @escaping (Result<Double, MTError>) -> Void)

#### Parameters

| completionHandler | A handler block to execute when function finishes. |

- 

setBearing(_:)

Asynchronous

Sets the bearing of the map.

The bearing is the compass direction that is “up”;
for example, a bearing of 90° orients the map so that east is up.

#### Declaration

Swift
@MainActor
public func setBearing(_ bearing: Double) async

#### Parameters

| bearing | The desired bearing. |

- 

setCenter(_:)

Asynchronous

Sets the map’s geographical centerpoint.

#### Declaration

Swift
@MainActor
public func setCenter(_ center: CLLocationCoordinate2D) async

#### Parameters

| center | The desired center coordinate. |

- 

flyTo(_:options:animationOptions:)

Asynchronous

Changes any combination of center, zoom, bearing, and pitch.

The animation seamlessly incorporates zooming and panning to help the user maintain her bearings
even after traversing a great distance.

Note
The animation will be skipped, and this will behave equivalently to jumpTo
if the user has the reduced motion accessibility feature enabled,
unless options includes essential: true.

#### Declaration

Swift
@MainActor
public func flyTo(
_ center: CLLocationCoordinate2D,
options: MTFlyToOptions?,
animationOptions: MTAnimationOptions?
) async

#### Parameters

| center | The desired center coordinate. |
| options | Custom options to use. |
| animationOptions | Optional animation options to use. |
| completionHandler | A handler block to execute when function finishes. |

- 

easeTo(_:options:animationOptions:)

Asynchronous

Changes any combination of center, zoom, bearing, pitch, and padding.

The map will retain its current values for any details not specified in options.

Note
The transition will happen instantly if the user has enabled the reduced motion accessibility feature,
unless options includes essential: true.

#### Declaration

Swift
@MainActor
public func easeTo(
_ center: CLLocationCoordinate2D,
options: MTCameraOptions?,
animationOptions: MTAnimationOptions?
) async

#### Parameters

| center | The desired center coordinate. |
| options | Custom options to use. |
| animationOptions | Optional animation options to use. |
| completionHandler | A handler block to execute when function finishes. |

- 

jumpTo(_:options:)

Asynchronous

Changes any combination of center, zoom, bearing, and pitch, without an animated transition.

#### Declaration

Swift
@MainActor
public func jumpTo(_ center: CLLocationCoordinate2D, options: MTCameraOptions?) async

- 

fitBounds(_:options:)

Asynchronous

Fits the map so the provided bounds are fully visible within the viewport.

#### Declaration

Swift
@MainActor
public func fitBounds(_ bounds: MTBounds, options fitOptions: MTFitBoundsOptions? = nil) async

#### Parameters

| bounds | Geographic bounds to display. |
| fitOptions | Additional configuration that controls the fitting animation. |

- 

setPadding(_:)

Asynchronous

Sets the padding in pixels around the viewport.

#### Declaration

Swift
@MainActor
public func setPadding(_ options: MTPaddingOptions) async

- 

fitToIpBounds()

Asynchronous

Fits the map to the bounds inferred from the current IP address.

#### Declaration

Swift
@MainActor
public func fitToIpBounds() async

- 

centerOnIpPoint()

Asynchronous

Centers the map on the location inferred from the current IP address.

#### Declaration

Swift
@MainActor
public func centerOnIpPoint() async

- 

setIsCenterClampedToGround(_:)

Asynchronous

Sets the value of centerClampedToGround.

If true, the elevation of the center point will automatically be set to the terrain elevation
(or zero if terrain is not enabled).
If false, the elevation of the center point will default to sea level and will not automatically update.
Needs to be set to false to keep the camera above ground when pitch > 90 degrees.

Note
Defaults to true.

#### Declaration

Swift
@MainActor
public func setIsCenterClampedToGround(_ isCenterClampedToGround: Bool) async

#### Parameters

| isCenterClampedToGround | The boolean value indicating if center will be clamped to ground. |

- 

setCenterElevation(_:)

Asynchronous

Sets the elevation of the map’s center point, in meters above sea level.

Note
Triggers the following events: moveStart and moveEnd.

#### Declaration

Swift
@MainActor
public func setCenterElevation(_ elevation: Double) async

#### Parameters

| elevation | The desired elevation. |

- 

setMaxPitch(_:)

Asynchronous

Sets or clears the map’s maximum pitch.

If the map’s current pitch is higher than the new maximum, the map will pitch to the new maximum.
If null is provided, the function removes the current maximum pitch (sets it to 60).

Throws
A `MTError` if maxPitch is out of bounds.

#### Declaration

Swift
@MainActor
public func setMaxPitch(_ maxPitch: Double?) async throws

#### Parameters

| maxPitch | The maximum pitch to set (0-85). |

- 

setMaxZoom(_:)

Asynchronous

Sets or clears the map’s maximum zoom.

If the map’s current zoom level is higher than the new maximum, the map will zoom to the new maximum.
If null or undefined is provided, the function removes the current maximum zoom (sets it to 22).

Throws
A `MTError` if maxZoom is out of bounds.

#### Declaration

Swift
@MainActor
public func setMaxZoom(_ maxZoom: Double?) async throws

#### Parameters

| maxZoom | The maximum zoom level to set. |

- 

setMinPitch(_:)

Asynchronous

Sets or clears the map’s minimum pitch.

If the map’s current pitch is lower than the new minimum, the map will pitch to the new minimum.
If null is provided, the function removes the current minimum pitch (i.e. sets it to 0).

Throws
A `MTError` if minPitch is out of bounds.

#### Declaration

Swift
@MainActor
public func setMinPitch(_ minPitch: Double?) async throws

#### Parameters

| minPitch | The minimum pitch to set (0-85) |

- 

setMinZoom(_:)

Asynchronous

Sets or clears the map’s minimum zoom.

If the map’s current zoom level is lower than the new minimum, the map will zoom to the new minimum.
If null  is provided, the function removes the current minimum zoom (i.e. sets it to -2).

Throws
A `MTError` if minZoom is out of bounds.

#### Declaration

Swift
@MainActor
public func setMinZoom(_ minZoom: Double?) async throws

#### Parameters

| minZoom | The minimum zoom level to set (-2 - 24). |

- 

setMaxBounds(_:)

Asynchronous

Sets or clears the map’s maximum bounds constraint.

#### Declaration

Swift
@MainActor
public func setMaxBounds(_ bounds: MTBounds?) async throws

#### Parameters

| bounds | The bounds to constrain panning to, or `nil` to remove the constraint. |

- 

setPitch(_:)

Asynchronous

Sets the map’s pitch (tilt).

#### Declaration

Swift
@MainActor
public func setPitch(_ pitch: Double) async

#### Parameters

| pitch | The pitch to set, measured in degrees away from the plane of the screen (0-60). |

- 

setRoll(_:)

Asynchronous

Sets the map’s roll angle.

Note
Triggers the following events: moveStart, moveEnd, rollStart, and rollEnd.

#### Declaration

Swift
@MainActor
public func setRoll(_ roll: Double) async

#### Parameters

| roll | The roll to set, measured in degrees about the camera boresight. |

- 

getPitch()

Asynchronous

Returns the map’s current pitch (tilt).

The map’s current pitch, measured in degrees away from the plane of the screen.

#### Declaration

Swift
@MainActor
public func getPitch() async -> Double

- 

getMaxPitch()

Asynchronous

Returns the map’s maximum pitch (tilt).

The map’s maximum pitch, measured in degrees away from the plane of the screen.

#### Declaration

Swift
@MainActor
public func getMaxPitch() async -> Double

- 

getMaxZoom()

Asynchronous

Returns the map’s maximum zoom.

The map’s maximum zoom level.

#### Declaration

Swift
@MainActor
public func getMaxZoom() async -> Double

- 

getMinPitch()

Asynchronous

Returns the map’s minimum pitch (tilt).

The map’s minimum pitch, measured in degrees away from the plane of the screen.

#### Declaration

Swift
@MainActor
public func getMinPitch() async -> Double

- 

getMinZoom()

Asynchronous

Returns the map’s minimum zoom.

The map’s minimum zoom level.

#### Declaration

Swift
@MainActor
public func getMinZoom() async -> Double

- 

panBy(_:)

Asynchronous

Pans the map by the specified offset.

#### Declaration

Swift
@MainActor
public func panBy(_ offset: MTPoint) async

#### Parameters

| offset | The x and y coordinates by which to pan the map. |

- 

panTo(_:)

Asynchronous

Pans the map to the specified location with an animated transition.

#### Declaration

Swift
@MainActor
public func panTo(_ coordinates: CLLocationCoordinate2D) async

#### Parameters

| coordinates | The location to pan the map to. |

- 

stop()

Asynchronous

Stops any ongoing animated transition.

#### Declaration

Swift
@MainActor
public func stop() async

- 

snapToNorth(animationOptions:)

Asynchronous

Snaps the map so that north is up.

#### Declaration

Swift
@MainActor
public func snapToNorth(animationOptions: MTAnimationOptions? = nil) async

#### Parameters

| animationOptions | Animation options. |

- 

getCenter()

Asynchronous

Returns the map’s current center.

The map’s current geographical center.

#### Declaration

Swift
@MainActor
public func getCenter() async -> CLLocationCoordinate2D

- 

getBounds()

Asynchronous

Returns the map’s current geographic bounds.

#### Declaration

Swift
@MainActor
public func getBounds() async -> MTBounds

- 

getMaxBounds()

Asynchronous

Returns the maximum bounds constraint applied to the map, if any.

#### Declaration

Swift
@MainActor
public func getMaxBounds() async -> MTBounds?

- 

getCenterClampedToGround()

Asynchronous

Returns whether the map’s center point is clamped to the ground.

#### Declaration

Swift
@MainActor
public func getCenterClampedToGround() async -> Bool

- 

getCenterElevation()

Asynchronous

Returns the elevation of the map’s center point, in meters above sea level.

#### Declaration

Swift
@MainActor
public func getCenterElevation() async -> Double

- 

getCameraTargetElevation()

Asynchronous

Returns the elevation for the point where the camera is looking,
in meters above sea level multiplied by exaggeration.

#### Declaration

Swift
@MainActor
public func getCameraTargetElevation() async -> Double

- 

project(coordinates:)

Asynchronous

Project coordinates to point on the container.

#### Declaration

Swift
@MainActor
public func project(coordinates: CLLocationCoordinate2D) async -> MTPoint

#### Parameters

| coordinates | The location to project. |

- 

unproject(point:)

Asynchronous

Unproject screen coordinates to geographical coordinates.

#### Declaration

Swift
@MainActor
public func unproject(point: MTPoint) async -> CLLocationCoordinate2D

#### Parameters

| point | The screen coordinates to unproject. |

- 

getBearing()

Asynchronous

Returns the map’s current bearing.

#### Declaration

Swift
@MainActor
public func getBearing() async -> Double

- 

getRoll()

Asynchronous

Returns the map’s current roll.

#### Declaration

Swift
@MainActor
public func getRoll() async -> Double

- 

getPixelRatio(completionHandler:)

Returns the pixel ratio currently used by the map.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func getPixelRatio(completionHandler: @escaping (Result<Double, MTError>) -> Void)

#### Parameters

| completionHandler | A handler block to execute when function finishes. |

- 

setPixelRatio(_:completionHandler:)

Sets the pixel ratio used by the map.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setPixelRatio(
_ pixelRatio: Double,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| pixelRatio | Pixel ratio value to apply. |
| completionHandler | A handler block to execute when function finishes. |

- 

triggerRepaint(completionHandler:)

Trigger the rendering of a single frame. Use this method with custom layers to repaint the map
when the layer changes. Calling this multiple times before the next frame is rendered will still
result in only a single frame being rendered.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func triggerRepaint(
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| completionHandler | A handler block to execute when function finishes. |

- 

setShowTileBoundaries(_:completionHandler:)

Displays tile boundaries on the map.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setShowTileBoundaries(
_ show: Bool,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| show | A boolean value indicating whether to show tile boundaries. |
| completionHandler | A handler block to execute when function finishes. |

- 

setShowPadding(_:completionHandler:)

Displays padding on the map.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setShowPadding(
_ show: Bool,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| show | A boolean value indicating whether to show padding. |
| completionHandler | A handler block to execute when function finishes. |

- 

setShowOverdrawInspector(_:completionHandler:)

Displays the overdraw inspector on the map.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setShowOverdrawInspector(
_ show: Bool,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| show | A boolean value indicating whether to show the overdraw inspector. |
| completionHandler | A handler block to execute when function finishes. |

- 

setShowCollisionBoxes(_:completionHandler:)

Displays collision boxes on the map.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setShowCollisionBoxes(
_ show: Bool,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| show | A boolean value indicating whether to show collision boxes. |
| completionHandler | A handler block to execute when function finishes. |

- 

setMaxParallelImageRequests(_:completionHandler:)

Sets the maximum number of images loaded in parallel.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setMaxParallelImageRequests(
_ maxParallelImageRequests: Int,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| maxParallelImageRequests | The maximum number of images. |
| completionHandler | A handler block to execute when function finishes. |

- 

setRTLTextPlugin(pluginURL:deferred:completionHandler:)

Sets the map’s RTL text plugin.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setRTLTextPlugin(
pluginURL: String,
deferred: Bool = false,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| pluginURL | URL pointing to the Mapbox RTL text plugin source. |
| deferred | A boolean indicating if the plugin evaluation should be deferred. |
| completionHandler | A handler block to execute when function finishes. |

- 

getPixelRatio()

Asynchronous

Returns the pixel ratio currently used by the map.

#### Declaration

Swift
@MainActor
public func getPixelRatio() async -> Double

- 

setPixelRatio(_:)

Asynchronous

Sets the pixel ratio used by the map.

#### Declaration

Swift
@MainActor
public func setPixelRatio(_ pixelRatio: Double) async

#### Parameters

| pixelRatio | Pixel ratio value to apply. |

- 

triggerRepaint()

Asynchronous

Trigger the rendering of a single frame. Use this method with custom layers to repaint the map
when the layer changes. Calling this multiple times before the next frame is rendered will still
result in only a single frame being rendered.

#### Declaration

Swift
@MainActor
public func triggerRepaint() async

- 

setShowTileBoundaries(_:)

Asynchronous

Displays tile boundaries on the map.

#### Declaration

Swift
@MainActor
public func setShowTileBoundaries(_ show: Bool) async

#### Parameters

| show | A boolean value indicating whether to show tile boundaries. |

- 

setShowPadding(_:)

Asynchronous

Displays padding on the map.

#### Declaration

Swift
@MainActor
public func setShowPadding(_ show: Bool) async

#### Parameters

| show | A boolean value indicating whether to show padding. |

- 

setShowOverdrawInspector(_:)

Asynchronous

Displays the overdraw inspector on the map.

#### Declaration

Swift
@MainActor
public func setShowOverdrawInspector(_ show: Bool) async

#### Parameters

| show | A boolean value indicating whether to show the overdraw inspector. |

- 

setShowCollisionBoxes(_:)

Asynchronous

Displays collision boxes on the map.

#### Declaration

Swift
@MainActor
public func setShowCollisionBoxes(_ show: Bool) async

#### Parameters

| show | A boolean value indicating whether to show collision boxes. |

- 

setMaxParallelImageRequests(_:)

Asynchronous

Sets the maximum number of images loaded in parallel.

#### Declaration

Swift
@MainActor
public func setMaxParallelImageRequests(_ maxParallelImageRequests: Int) async

#### Parameters

| maxParallelImageRequests | The maximum number of images. |

- 

setRTLTextPlugin(pluginURL:deferred:)

Asynchronous

Sets the map’s RTL text plugin.

#### Declaration

Swift
@MainActor
public func setRTLTextPlugin(pluginURL: String, deferred: Bool = false) async

#### Parameters

| pluginURL | URL pointing to the Mapbox RTL text plugin source. |
| deferred | A boolean indicating if the plugin evaluation should be deferred. |

- 

setGlyphs(url:options:completionHandler:)

Sets the value of the style’s glyphs property.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setGlyphs(
url: URL,
options: MTStyleSetterOptions?,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| url | URL of the Glyph |
| options | Supporting type to add validation to another style related type. |
| completionHandler | A handler block to execute when function finishes. |

- 

setLanguage(_:completionHandler:)

Sets the map labels language.

The language generally depends on the style. Whenever a label is not supported in the defined language,
it falls back to MTLanguage.latin.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setLanguage(_ language: MTLanguage, completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| language | The language to be applied. |
| completionHandler | A handler block to execute when function finishes. |

- 

setSecondaryLanguage(_:completionHandler:)

Undocumented

#### Declaration

Swift
@MainActor
public func setSecondaryLanguage(
_ language: MTLanguage,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

- 

setSprite(_:completionHandler:)

Undocumented

#### Declaration

Swift
@MainActor
public func setSprite(_ url: URL, completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

- 

setLight(_:options:completionHandler:)

Sets the any combination of light values.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setLight(
_ light: MTLight,
options: MTStyleSetterOptions?,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| light | Light properties to set. |
| options | Supporting type to add validation to another style related type. |
| completionHandler | A handler block to execute when function finishes. |

- 

setSky(_:options:completionHandler:)

Sets the sky configuration for the map.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setSky(
_ sky: MTSky,
options: MTStyleSetterOptions?,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| sky | Sky definition. |
| options | Supporting type to add validation to another style related type. |
| completionHandler | A handler block to execute when function finishes. |

- 

setSpace(_:completionHandler:)

Sets the space background for globe projection (cubemap/spacebox).

Note
Make sure space is enabled and projection is set to Globe before initializing the map via MTMapOptions.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setSpace(
_ space: MTSpaceOption,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| space | Space configuration or a boolean to enable default. |
| completionHandler | A handler block to execute when function finishes. |

- 

setHalo(_:completionHandler:)

Sets the atmospheric halo (glow) around the globe.

Note
Make sure halo is enabled and projection is set to Globe before initializing the map via MTMapOptions.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setHalo(
_ halo: MTHaloOption,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| halo | Halo configuration or a boolean to enable default. |
| completionHandler | A handler block to execute when function finishes. |

- 

disableHaloAnimations(completionHandler:)

Disables state transitions/animations for halo updates.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func disableHaloAnimations(
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| completionHandler | A handler block to execute when function finishes. |

- 

disableSpaceAnimations(completionHandler:)

Disables state transitions/animations for space updates.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func disableSpaceAnimations(
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| completionHandler | A handler block to execute when function finishes. |

- 

setShouldRenderWorldCopies(_:completionHandler:)

Sets the state of shouldRenderWorldCopies.

If true , multiple copies of the world will be rendered side by side beyond -180 and 180 degrees longitude.
If set to false:
When the map is zoomed out far enough that a single representation of the world does not
fill the map’s entire container, there will be blank space beyond 180 and -180 degrees longitude.
When the map is zoomed out far enough that a single representation of the world does not fill the
map’s entire container, there will be blank space beyond 180 and -180 degrees longitude.
Features that cross 180 and -180 degrees longitude will be cut in two (with one portion on
the right edge of the map and the other on the left edge of the map) at every zoom level.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setShouldRenderWorldCopies(
_ shouldRenderWorldCopies: Bool,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| shouldRenderWorldCopies | Boolean indicating whether world copies should be rendered. |
| completionHandler | A handler block to execute when function finishes. |

- 

addImage(name:image:options:completionHandler:)

Registers an image with the current style so it can be referenced by layers and annotations.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func addImage(
name: String,
image: UIImage,
options: MTStyleImageOptions? = nil,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| name | Unique identifier for the image. |
| image | Image to register. |
| options | Additional configuration that controls how the image is rendered. |
| completionHandler | A handler block to execute when function finishes. |

- 

updateImage(name:image:completionHandler:)

Updates an image in a style.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func updateImage(
name: String,
image: UIImage,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| name | Unique identifier for the image to update. |
| image | New image to set. |
| completionHandler | A handler block to execute when function finishes. |

- 

addSprite(id:url:completionHandler:)

Registers a sprite with the current style so it can be referenced by layers and annotations.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func addSprite(
id: String,
url: URL,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| id | Unique identifier for the sprite. |
| url | URL pointing to the sprite resource. |
| completionHandler | A handler block to execute when function finishes. |

- 

addMarker(_:completionHandler:)

Adds a marker to the map.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func addMarker(_ marker: MTMarker, completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| marker | Marker to be added to the map. |
| completionHandler | A handler block to execute when function finishes. |

- 

addMarkers(_:withSingleIcon:completionHandler:)

Adds multiple markers to the map.

Batch adding is preferred way of adding multiple markers to the map.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func addMarkers(
_ markers: [MTMarker],
withSingleIcon: UIImage?,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| markers | Markers to be added to the map. |
| withSingleIcon | Optional single image to use for all markers. |
| completionHandler | A handler block to execute when function finishes. |

- 

removeMarker(_:completionHandler:)

Removes a marker from the map.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func removeMarker(_ marker: MTMarker, completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| marker | Marker to be removed from the map. |
| completionHandler | A handler block to execute when function finishes. |

- 

removeMarkers(_:completionHandler:)

Removes multiple markers from the map.

Batch removing is preferred way of removing multiple markers from the map.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func removeMarkers(_ markers: [MTMarker], completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| markers | Markers to be removed from the map. |
| completionHandler | A handler block to execute when function finishes. |

- 

addTextPopup(_:completionHandler:)

Adds a text popup to the map.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func addTextPopup(_ popup: MTTextPopup, completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| popup | Popup to be added to the map. |
| completionHandler | A handler block to execute when function finishes. |

- 

removeTextPopup(_:completionHandler:)

Removes a text popup from the map.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func removeTextPopup(_ popup: MTTextPopup, completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| popup | Popup to be removed from the map. |
| completionHandler | A handler block to execute when function finishes. |

- 

getProjection(completionHandler:)

Returns the projection currently active on the map.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func getProjection(completionHandler: ((Result<MTProjectionType, MTError>) -> Void)? = nil)

#### Parameters

| completionHandler | A handler block to execute when function finishes. |

- 

enableGlobeProjection(completionHandler:)

Enables the globe projection visualization.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func enableGlobeProjection(completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| completionHandler | A handler block to execute when function finishes. |

- 

enableMercatorProjection(completionHandler:)

Enables the mercator projection visualization.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func enableMercatorProjection(completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| completionHandler | A handler block to execute when function finishes. |

- 

enableTerrain(exaggerationFactor:completionHandler:)

Enables the 3D terrain visualization.

Note
Default is 1.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func enableTerrain(
exaggerationFactor: Double = 1.0,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| exaggerationFactor | Factor for volume boosting. |
| completionHandler | A handler block to execute when function finishes. |

- 

disableTerrain(completionHandler:)

Disables  the 3D terrain visualization.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func disableTerrain(completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| completionHandler | A handler block to execute when function finishes. |

- 

setTerrainExaggeration(_:animate:completionHandler:)

Sets the terrain exaggeration.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setTerrainExaggeration(
_ exaggeration: Double,
animate: Bool = true,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| exaggeration | The new exaggeration factor. |
| animate | Whether to animate the transition. Defaults to `true`. |
| completionHandler | A handler block to execute when function finishes. |

- 

setTerrainAnimationDuration(_:completionHandler:)

Sets the animation duration of the terrain transitions.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setTerrainAnimationDuration(
_ duration: Double,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| duration | The duration in milliseconds. |
| completionHandler | A handler block to execute when function finishes. |

- 

setTerrain(sourceId:exaggeration:completionHandler:)

Sets the 3D terrain on the map.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setTerrain(
sourceId: String,
exaggeration: Double? = nil,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| sourceId | The ID of the terrain source. |
| exaggeration | Factor for volume boosting. |
| completionHandler | A handler block to execute when function finishes. |

- 

setTerrain(completionHandler:)

Removes the 3D terrain from the map.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setTerrain(completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| completionHandler | A handler block to execute when function finishes. |

- 

setVerticalFieldOfView(degrees:completionHandler:)

Sets the map’s vertical field of view, in degrees.

The internal camera has a default vertical field of view of a wide ~36.86 degrees. In globe mode,
such a large FOV reduces the amount of the Earth that can be seen at once and exaggerates
the central part, comparably to a fisheye lens. In many cases, a narrower FOV is preferable.

Note
Default is 36.87.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setVerticalFieldOfView(
degrees: Double = 36.87,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| degrees | The vertical field of view to set, in degrees (0-180). |
| completionHandler | A handler block to execute when function finishes. |

- 

isSourceLoaded(id:completionHandler:)

Returns boolean value indicating whether the source with provided id is loaded.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func isSourceLoaded(
id: String,
completionHandler: ((Result<Bool, MTError>) -> Void)? = nil
)

#### Parameters

| id | The id of the source. |
| completionHandler | A handler block to execute when function finishes. |

- 

areTilesLoaded(completionHandler:)

Returns boolean value indicating whether all tiles required for the current viewport are loaded.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func areTilesLoaded(
completionHandler: ((Result<Bool, MTError>) -> Void)? = nil
)

#### Parameters

| completionHandler | A handler block to execute when function finishes. |

- 

isMapLoaded(completionHandler:)

Returns boolean value indicating whether the map is fully loaded.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func isMapLoaded(
completionHandler: ((Result<Bool, MTError>) -> Void)? = nil
)

#### Parameters

| completionHandler | A handler block to execute when function finishes. |

- 

getRenderWorldCopies(completionHandler:)

Returns boolean value indicating whether the map renders world copies.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func getRenderWorldCopies(
completionHandler: ((Result<Bool, MTError>) -> Void)? = nil
)

#### Parameters

| completionHandler | A handler block to execute when function finishes. |

- 

setFilter(forLayerId:filter:)

Asynchronous

Undocumented

#### Declaration

Swift
@MainActor
public func setFilter(forLayerId layerId: String, filter: MTPropertyValue) async

- 

setLayoutProperty(forLayerId:name:value:)

Asynchronous

Undocumented

#### Declaration

Swift
@MainActor
public func setLayoutProperty(forLayerId layerId: String, name: String, value: MTPropertyValue) async

- 

setPaintProperty(forLayerId:name:value:)

Asynchronous

Undocumented

#### Declaration

Swift
@MainActor
public func setPaintProperty(forLayerId layerId: String, name: String, value: MTPropertyValue) async

Typed property setters (async)

- 

setLayoutProperty(forLayerId:property:value:)

Asynchronous

Sets a symbol layout property using a typed key (async).

#### Declaration

Swift
@MainActor
public func setLayoutProperty(
forLayerId layerId: String,
property: MTSymbolLayoutProperty,
value: MTPropertyValue
) async

#### Parameters

| layerId | Identifier of the target layer. |
| property | Typed symbol layout property key. |
| value | Property value or expression. |

- 

setPaintProperty(forLayerId:property:value:)

Asynchronous

Sets a circle paint property using a typed key (async).

#### Declaration

Swift
@MainActor
public func setPaintProperty(
forLayerId layerId: String,
property: MTCirclePaintProperty,
value: MTPropertyValue
) async

#### Parameters

| layerId | Identifier of the target layer. |
| property | Typed circle paint property key. |
| value | Property value or expression. |

- 

setPaintProperty(forLayerId:property:value:)

Asynchronous

Sets a symbol paint property using a typed key (async).

#### Declaration

Swift
@MainActor
public func setPaintProperty(
forLayerId layerId: String,
property: MTSymbolPaintProperty,
value: MTPropertyValue
) async

#### Parameters

| layerId | Identifier of the target layer. |
| property | Typed symbol paint property key. |
| value | Property value or expression. |

- 

setGlyphs(url:options:)

Asynchronous

Sets the value of the style’s glyphs property.

#### Declaration

Swift
@MainActor
public func setGlyphs(url: URL, options: MTStyleSetterOptions?) async

#### Parameters

| url | URL of the Glyph |
| options | Supporting type to add validation to another style related type. |

- 

setLanguage(_:)

Asynchronous

Sets the map labels language.

The language generally depends on the style. Whenever a label is not supported in the defined language,
it falls back to MTLanguage.latin.

#### Declaration

Swift
@MainActor
public func setLanguage(_ language: MTLanguage) async

#### Parameters

| language | The language to be applied. |

- 

setSecondaryLanguage(_:)

Asynchronous

#### Declaration

Swift
@MainActor
public func setSecondaryLanguage(_ language: MTLanguage) async

- 

setSprite(_:)

Asynchronous

#### Declaration

Swift
@MainActor
public func setSprite(_ url: URL) async

- 

setLight(_:options:)

Asynchronous

Sets the any combination of light values.

#### Declaration

Swift
@MainActor
public func setLight(_ light: MTLight, options: MTStyleSetterOptions?) async

#### Parameters

| light | Light properties to set. |
| options | Supporting type to add validation to another style related type. |

- 

setSky(_:options:)

Asynchronous

Sets the sky configuration for the map.

#### Declaration

Swift
@MainActor
public func setSky(_ sky: MTSky, options: MTStyleSetterOptions?) async

#### Parameters

| sky | Sky definition. |
| options | Supporting type to add validation to another style related type. |

- 

setSpace(_:)

Asynchronous

Sets the space background for globe projection (cubemap/spacebox).

Note
Make sure space is enabled and projection is set to Globe before initializing the map via MTMapOptions.

#### Declaration

Swift
@MainActor
public func setSpace(_ space: MTSpaceOption) async

#### Parameters

| space | Space configuration or a boolean to enable default. |

- 

setShouldRenderWorldCopies(_:)

Asynchronous

Sets the state of shouldRenderWorldCopies.

If true , multiple copies of the world will be rendered side by side beyond -180 and 180 degrees longitude.
If set to false:
When the map is zoomed out far enough that a single representation of the world does not
fill the map’s entire container, there will be blank space beyond 180 and -180 degrees longitude.
When the map is zoomed out far enough that a single representation of the world does not fill the
map’s entire container, there will be blank space beyond 180 and -180 degrees longitude.
Features that cross 180 and -180 degrees longitude will be cut in two (with one portion on
the right edge of the map and the other on the left edge of the map) at every zoom level.

#### Declaration

Swift
@MainActor
public func setShouldRenderWorldCopies(_ shouldRenderWorldCopies: Bool) async

#### Parameters

| shouldRenderWorldCopies | Boolean indicating whether world copies should be rendered. |

- 

addImage(name:image:options:)

Asynchronous

Registers an image with the current style so it can be referenced by layers and annotations.

#### Declaration

Swift
@MainActor
public func addImage(name: String, image: UIImage, options: MTStyleImageOptions? = nil) async

#### Parameters

| name | Unique identifier for the image. |
| image | Image to register. |
| options | Additional configuration that controls how the image is rendered. |

- 

updateImage(name:image:)

Asynchronous

Updates an image in a style.

#### Declaration

Swift
@MainActor
public func updateImage(name: String, image: UIImage) async

#### Parameters

| name | Unique identifier for the image to update. |
| image | New image to set. |

- 

addSprite(id:url:)

Asynchronous

Registers a sprite with the current style so it can be referenced by layers and annotations.

#### Declaration

Swift
@MainActor
public func addSprite(id: String, url: URL) async

#### Parameters

| id | Unique identifier for the sprite. |
| url | URL pointing to the sprite resource. |

- 

addMarker(_:)

Asynchronous

Adds a marker to the map.

#### Declaration

Swift
@MainActor
public func addMarker(_ marker: MTMarker) async

#### Parameters

| marker | Marker to be added to the map. |

- 

addMarkers(_:withSingleIcon:)

Asynchronous

Adds multiple markers to the map.

Batch adding is preferred way of adding multiple markers to the map.

#### Declaration

Swift
@MainActor
public func addMarkers(_ markers: [MTMarker], withSingleIcon: UIImage?) async

#### Parameters

| markers | Markers to be added to the map. |
| withSingleIcon | Optional single image to use for all markers. |

- 

removeMarker(_:)

Asynchronous

Removes a marker from the map.

#### Declaration

Swift
@MainActor
public func removeMarker(_ marker: MTMarker) async

#### Parameters

| marker | Marker to be removed from the map. |

- 

removeMarkers(_:)

Asynchronous

Removes multiple markers from the map.

Batch removing is preferred way of removing multiple markers from the map.

#### Declaration

Swift
@MainActor
public func removeMarkers(_ markers: [MTMarker]) async

#### Parameters

| markers | Markers to be removed from the map. |

- 

addTextPopup(_:)

Asynchronous

Adds a text popup to the map.

#### Declaration

Swift
@MainActor
public func addTextPopup(_ popup: MTTextPopup) async

#### Parameters

| popup | Popup to be added to the map. |

- 

removeTextPopup(_:)

Asynchronous

Removes a text popup from the map.

#### Declaration

Swift
@MainActor
public func removeTextPopup(_ popup: MTTextPopup) async

#### Parameters

| marker | Popup to be removed from the map. |

- 

getProjection()

Asynchronous

Returns the projection currently active on the map.

#### Declaration

Swift
@MainActor
public func getProjection() async -> MTProjectionType

- 

enableGlobeProjection()

Asynchronous

Enables the globe projection visualization.

#### Declaration

Swift
@MainActor
public func enableGlobeProjection() async

- 

enableMercatorProjection()

Asynchronous

Enables the mercator projection visualization.

#### Declaration

Swift
@MainActor
public func enableMercatorProjection() async

- 

enableTerrain(exaggerationFactor:)

Asynchronous

Enables the 3D terrain visualization.

Note
Default is 1.

#### Declaration

Swift
@MainActor
public func enableTerrain(exaggerationFactor: Double = 1.0) async

#### Parameters

| exaggerationFactor | Factor for volume boosting. |

- 

disableTerrain()

Asynchronous

Disables  the 3D terrain visualization.

#### Declaration

Swift
@MainActor
public func disableTerrain() async

- 

setTerrainExaggeration(_:animate:)

Asynchronous

Sets the terrain exaggeration.

#### Declaration

Swift
@MainActor
public func setTerrainExaggeration(_ exaggeration: Double, animate: Bool = true) async

#### Parameters

| exaggeration | The new exaggeration factor. |
| animate | Whether to animate the transition. Defaults to `true`. |

- 

setTerrainAnimationDuration(_:)

Asynchronous

Sets the animation duration of the terrain transitions.

#### Declaration

Swift
@MainActor
public func setTerrainAnimationDuration(_ duration: Double) async

#### Parameters

| duration | The duration in milliseconds. |

- 

setTerrain(sourceId:exaggeration:)

Asynchronous

Sets the 3D terrain on the map.

#### Declaration

Swift
@MainActor
public func setTerrain(sourceId: String, exaggeration: Double? = nil) async

#### Parameters

| sourceId | The ID of the terrain source. |
| exaggeration | Factor for volume boosting. |

- 

setTerrain()

Asynchronous

Removes the 3D terrain from the map.

#### Declaration

Swift
@MainActor
public func setTerrain() async

- 

setVerticalFieldOfView(degrees:)

Asynchronous

Sets the map’s vertical field of view, in degrees.

The internal camera has a default vertical field of view of a wide ~36.86 degrees. In globe mode,
such a large FOV reduces the amount of the Earth that can be seen at once and exaggerates
the central part, comparably to a fisheye lens. In many cases, a narrower FOV is preferable.

Note
Default is 36.87.

#### Declaration

Swift
@MainActor
public func setVerticalFieldOfView(degrees: Double = 36.87) async

#### Parameters

| degrees | The vertical field of view to set, in degrees (0-180). |

- 

setHalo(_:)

Asynchronous

Sets the atmospheric halo (glow) around the globe.

Note
Make sure halo is enabled and projection is set to Globe before initializing the map via MTMapOptions.

#### Declaration

Swift
@MainActor
public func setHalo(_ halo: MTHaloOption) async

#### Parameters

| halo | Halo configuration or a boolean to enable default. |

- 

disableHaloAnimations()

Asynchronous

Disables state transitions/animations for halo updates.

#### Declaration

Swift
@MainActor
public func disableHaloAnimations() async

- 

disableSpaceAnimations()

Asynchronous

Disables state transitions/animations for space updates.

#### Declaration

Swift
@MainActor
public func disableSpaceAnimations() async

- 

isSourceLoaded(id:)

Asynchronous

Returns boolean value indicating whether the source with provided id is loaded.

#### Declaration

Swift
@MainActor
public func isSourceLoaded(id: String) async -> Bool

#### Parameters

| id | The id of the source. |

- 

areTilesLoaded()

Asynchronous

Returns boolean value indicating whether all tiles required for the current viewport are loaded.

#### Declaration

Swift
@MainActor
public func areTilesLoaded() async -> Bool

- 

isMapLoaded()

Asynchronous

Returns boolean value indicating whether the map is fully loaded.

#### Declaration

Swift
@MainActor
public func isMapLoaded() async -> Bool

- 

getRenderWorldCopies()

Asynchronous

Returns boolean value indicating whether the map renders world copies.

#### Declaration

Swift
@MainActor
public func getRenderWorldCopies() async -> Bool

- 

zoomIn(completionHandler:)

Increases the map’s zoom level by 1.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func zoomIn(completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

- 

zoomOut(completionHandler:)

Decreases the map’s zoom level by 1.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func zoomOut(completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| completionHandler | A handler block to execute when function finishes. |

- 

getZoom(completionHandler:)

Returns the map’s current zoom level.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func getZoom(completionHandler: @escaping (Result<Double, MTError>) -> Void)

#### Parameters

| completionHandler | A handler block to execute when function finishes. |

- 

setZoom(_:completionHandler:)

Sets the map’s zoom level.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setZoom(_ zoom: Double, completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| zoom | The zoom level to set (0-20). |
| completionHandler | A handler block to execute when function finishes. |

- 

zoomTo(_:options:completionHandler:)

Zooms to the specified zoom level with an animated transition.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func zoomTo(
_ zoom: Double,
options: MTAnimationOptions? = nil,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| zoom | The zoom level to transition to. |
| options | Animation options to use. |
| completionHandler | A handler block to execute when function finishes. |

- 

zoomIn()

Asynchronous

Increases the map’s zoom level by 1.

#### Declaration

Swift
@MainActor
public func zoomIn() async

- 

zoomOut()

Asynchronous

Decreases the map’s zoom level by 1.

#### Declaration

Swift
@MainActor
public func zoomOut() async

- 

getZoom()

Asynchronous

Returns the map’s current zoom level.

#### Declaration

Swift
@MainActor
public func getZoom() async -> Double

- 

setZoom(_:)

Asynchronous

Sets the map’s zoom level.

#### Declaration

Swift
@MainActor
public func setZoom(_ zoom: Double) async

- 

zoomTo(_:options:)

Asynchronous

Zooms to the specified zoom level with an animated transition.

#### Declaration

Swift
@MainActor
public func zoomTo(_ zoom: Double, options: MTAnimationOptions? = nil) async

#### Parameters

| zoom | The zoom level to transition to. |
| options | Animation options to use. |

- 

didUpdateLocation(_:)

#### Declaration

Swift
@MainActor
public func didUpdateLocation(_ location: CLLocation)

- 

didFailWithError(_:)

#### Declaration

Swift
@MainActor
public func didFailWithError(_ error: Error)

- 

pinToSuperviewEdges()

Pins the map view to its superview edges using auto layout.

Note
Map view must be added to the superview before calling the function.

#### Declaration

Swift
@MainActor
func pinToSuperviewEdges()

---

## File: Classes/MTMarker.html

---
layout: mobile_sdk
title: "MTMarker"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Annotation element that can be added to the map."
id: mtmarker
breadcrumb: "Mobile SDK/iOS/Reference/Classes"
---

# MTMarker

`public class MTMarker : MTAnnotation, MTMapViewContent, @unchecked Sendable`

Annotation element that can be added to the map.

- 

identifier

Unique id of the marker.

#### Declaration

Swift
`public private(set) var identifier: String { get }`

- 

coordinates

Position of the marker on the map.

#### Declaration

Swift
`public private(set) var coordinates: CLLocationCoordinate2D { get }`

- 

color

Color of the marker.

#### Declaration

Swift
`public var color: UIColor?`

- 

opacity

Opacity of the marker.

#### Declaration

Swift
`public var opacity: Double`

- 

opacityWhenCovered

Opacity applied when the marker is covered by another object.

#### Declaration

Swift
`public var opacityWhenCovered: Double`

- 

draggable

Boolean indicating whether marker is draggable.

#### Declaration

Swift
`public var draggable: Bool?`

- 

icon

Custom icon to use for marker.

#### Declaration

Swift
`public var icon: UIImage?`

- 

anchor

Anchor position of the marker.

#### Declaration

Swift
`public var anchor: MTAnchor`

- 

offset

Offset distance from the marker’s anchor, applied on both axes in pixels.

#### Declaration

Swift
`public var offset: Double`

- 

scale

Scale factor applied to the marker.

#### Declaration

Swift
`public var scale: Double`

- 

subpixelPositioning

Enables subpixel positioning when rendering the marker.

#### Declaration

Swift
`public var subpixelPositioning: Bool`

- 

rotation

Rotation of the marker in degrees.

#### Declaration

Swift
`public var rotation: Double`

- 

rotationAlignment

Alignment of the marker rotation relative to the map or viewport.

#### Declaration

Swift
`public var rotationAlignment: MTMarkerRotationAlignment`

- 

pitchAlignment

Alignment of the marker pitch relative to the map or viewport.

#### Declaration

Swift
`public var pitchAlignment: MTMarkerPitchAlignment`

- 

popup

Optional attached popup.

#### Declaration

Swift
`public private(set) var popup: MTTextPopup? { get }`

- 

annotationView

Optional attached custom annotation.

#### Declaration

Swift
`weak public private(set) var annotationView: MTCustomAnnotationView? { get }`

- 

init(coordinates:anchor:offset:opacity:opacityWhenCovered:rotation:rotationAlignment:pitchAlignment:scale:subpixelPositioning:)

Initializes the marker with the specified position.

#### Declaration

Swift
public init(
coordinates: CLLocationCoordinate2D,
anchor: MTAnchor = .center,
offset: Double = 0.0,
opacity: Double = 1.0,
opacityWhenCovered: Double = 0.2,
rotation: Double = 0.0,
rotationAlignment: MTMarkerRotationAlignment = .auto,
pitchAlignment: MTMarkerPitchAlignment = .auto,
scale: Double = 1.0,
subpixelPositioning: Bool = true
)

#### Parameters

| coordinates | Position of the marker. |
| anchor | Anchor position for the marker. |
| offset | Pixel offset from the anchor applied on both axes. |

- 

init(coordinates:popup:anchor:offset:opacity:opacityWhenCovered:rotation:rotationAlignment:pitchAlignment:scale:subpixelPositioning:)

Initializes the marker with the specified position and text popup.

#### Declaration

Swift
public init(
coordinates: CLLocationCoordinate2D,
popup: MTTextPopup?,
anchor: MTAnchor = .center,
offset: Double = 0.0,
opacity: Double = 1.0,
opacityWhenCovered: Double = 0.2,
rotation: Double = 0.0,
rotationAlignment: MTMarkerRotationAlignment = .auto,
pitchAlignment: MTMarkerPitchAlignment = .auto,
scale: Double = 1.0,
subpixelPositioning: Bool = true
)

#### Parameters

| coordinates | Position of the marker. |
| popup | Popup to attach to the marker. |
| anchor | Anchor position for the marker. |
| offset | Pixel offset from the anchor applied on both axes. |

- 

init(coordinates:color:icon:draggable:anchor:offset:opacity:opacityWhenCovered:rotation:rotationAlignment:pitchAlignment:scale:subpixelPositioning:)

Initializes the marker with the specified position, color/icon and behaviour.

#### Declaration

Swift
public init(
coordinates: CLLocationCoordinate2D,
color: UIColor? = .blue,
icon: UIImage? = nil,
draggable: Bool? = false,
anchor: MTAnchor = .center,
offset: Double = 0.0,
opacity: Double = 1.0,
opacityWhenCovered: Double = 0.2,
rotation: Double = 0.0,
rotationAlignment: MTMarkerRotationAlignment = .auto,
pitchAlignment: MTMarkerPitchAlignment = .auto,
scale: Double = 1.0,
subpixelPositioning: Bool = true
)

#### Parameters

| coordinates | Position of the marker. |
| color | Color of the marker. |
| icon | Icon for the marker. |
| draggable | Boolean indicating whether the  marker is draggable. |
| anchor | Anchor position for the marker. |
| offset | Pixel offset from the anchor applied on both axes. |

- 

init(coordinates:color:icon:draggable:popup:anchor:offset:opacity:opacityWhenCovered:rotation:rotationAlignment:pitchAlignment:scale:subpixelPositioning:)

Initializes the marker with the specified position, color/icon and popup.

#### Declaration

Swift
public init(
coordinates: CLLocationCoordinate2D,
color: UIColor? = .blue,
icon: UIImage? = nil,
draggable: Bool? = false,
popup: MTTextPopup?,
anchor: MTAnchor = .center,
offset: Double = 0.0,
opacity: Double = 1.0,
opacityWhenCovered: Double = 0.2,
rotation: Double = 0.0,
rotationAlignment: MTMarkerRotationAlignment = .auto,
pitchAlignment: MTMarkerPitchAlignment = .auto,
scale: Double = 1.0,
subpixelPositioning: Bool = true
)

#### Parameters

| coordinates | Position of the marker. |
| color | Color of the marker. |
| icon | Icon for the marker. |
| draggable | Boolean indicating whether the  marker is draggable. |
| popup | Popup to attach to the marker. |
| anchor | Anchor position for the marker. |
| offset | Pixel offset from the anchor applied on both axes. |

- 

setCoordinates(_:in:completionHandler:)

Sets coordinates for the marker.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setCoordinates(
_ coordinates: CLLocationCoordinate2D,
in mapView: MTMapView,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| coordinates | Position of the marker. |
| completionHandler | A handler block to execute when function finishes. |

- 

setDelegate(to:)

Sets marker as map’s delegate.

#### Declaration

Swift
@MainActor
public func setDelegate(to mapView: MTMapView)

#### Parameters

| mapView | Map view for which to subscribe to. |

- 

attachAnnotationView(_:)

Attaches custom annotation view to the marker.

Note
Does not add the custom view to the map. Use customAnnotationView.addTo.

#### Declaration

Swift
`public func attachAnnotationView(_ view: MTCustomAnnotationView)`

- 

detachAnnotationView()

Detaches custom annotation view from the marker.

#### Declaration

Swift
`public func detachAnnotationView()`

- 

setDraggable(_:in:completionHandler:)

Sets whether the marker is draggable.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setDraggable(
_ draggable: Bool,
in mapView: MTMapView,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| draggable | Boolean indicating whether the marker should be draggable. |
| mapView | Map view to apply to. |
| completionHandler | A handler block to execute when function finishes. |

- 

setOffset(_:in:completionHandler:)

Sets the offset distance from the marker’s anchor.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setOffset(
_ offset: Double,
in mapView: MTMapView,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| offset | Pixel offset applied on both axes. |
| mapView | Map view to apply to. |
| completionHandler | A handler block to execute when function finishes. |

- 

setRotation(_:in:completionHandler:)

Sets the rotation of the marker in degrees.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setRotation(
_ rotation: Double,
in mapView: MTMapView,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| rotation | Rotation in degrees. |
| mapView | Map view to apply to. |
| completionHandler | A handler block to execute when function finishes. |

- 

setRotationAlignment(_:in:completionHandler:)

Sets the rotation alignment of the marker.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setRotationAlignment(
_ alignment: MTMarkerRotationAlignment,
in mapView: MTMapView,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| alignment | Rotation alignment relative to map or viewport. |
| mapView | Map view to apply to. |
| completionHandler | A handler block to execute when function finishes. |

- 

togglePopup(in:completionHandler:)

Toggles the popup bound to the marker.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func togglePopup(
in mapView: MTMapView,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| mapView | Map view to apply to. |
| completionHandler | A handler block to execute when function finishes. |

- 

getCoordinates(in:completionHandler:)

Returns current coordinates of the marker.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func getCoordinates(
in mapView: MTMapView,
completionHandler: ((Result<CLLocationCoordinate2D, MTError>) -> Void)? = nil
)

#### Parameters

| mapView | Map view to query. |
| completionHandler | A handler block to execute when function finishes. |

- 

getPitchAlignment(in:completionHandler:)

Returns the marker’s pitch alignment.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func getPitchAlignment(
in mapView: MTMapView,
completionHandler: ((Result<MTMarkerPitchAlignment, MTError>) -> Void)? = nil
)

#### Parameters

| mapView | Map view to query. |
| completionHandler | A handler block to execute when function finishes. |

- 

getRotation(in:completionHandler:)

Returns the marker’s rotation value.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func getRotation(
in mapView: MTMapView,
completionHandler: ((Result<Double, MTError>) -> Void)? = nil
)

#### Parameters

| mapView | Map view to query. |
| completionHandler | A handler block to execute when function finishes. |

- 

getRotationAlignment(in:completionHandler:)

Returns the marker’s rotation alignment.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func getRotationAlignment(
in mapView: MTMapView,
completionHandler: ((Result<MTMarkerRotationAlignment, MTError>) -> Void)? = nil
)

#### Parameters

| mapView | Map view to query. |
| completionHandler | A handler block to execute when function finishes. |

- 

getOffset(in:completionHandler:)

Returns the marker’s offset value in pixels.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func getOffset(
in mapView: MTMapView,
completionHandler: ((Result<Double, MTError>) -> Void)? = nil
)

#### Parameters

| mapView | Map view to query. |
| completionHandler | A handler block to execute when function finishes. |

- 

isDraggable(in:completionHandler:)

Returns whether the marker is draggable.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func isDraggable(
in mapView: MTMapView,
completionHandler: ((Result<Bool, MTError>) -> Void)? = nil
)

#### Parameters

| mapView | Map view to query. |
| completionHandler | A handler block to execute when function finishes. |

- 

setCoordinates(_:in:)

Asynchronous

Sets coordinates for the marker.

#### Declaration

Swift
@MainActor
public func setCoordinates(_ coordinates: CLLocationCoordinate2D, in mapView: MTMapView) async

#### Parameters

| coordinates | Position of the marker. |
| mapView | Map view to apply to. |

- 

setDraggable(_:in:)

Asynchronous

Sets whether the marker is draggable.

#### Declaration

Swift
@MainActor
public func setDraggable(_ draggable: Bool, in mapView: MTMapView) async

#### Parameters

| draggable | Boolean indicating whether the marker should be draggable. |
| mapView | Map view to apply to. |

- 

setOffset(_:in:)

Asynchronous

Sets the offset distance from the marker’s anchor.

#### Declaration

Swift
@MainActor
public func setOffset(_ offset: Double, in mapView: MTMapView) async

#### Parameters

| offset | Pixel offset applied on both axes. |
| mapView | Map view to apply to. |

- 

setRotation(_:in:)

Asynchronous

Sets the rotation of the marker in degrees.

#### Declaration

Swift
@MainActor
public func setRotation(_ rotation: Double, in mapView: MTMapView) async

#### Parameters

| rotation | Rotation in degrees. |
| mapView | Map view to apply to. |

- 

setRotationAlignment(_:in:)

Asynchronous

Sets the rotation alignment of the marker.

#### Declaration

Swift
@MainActor
public func setRotationAlignment(_ alignment: MTMarkerRotationAlignment, in mapView: MTMapView) async

#### Parameters

| alignment | Rotation alignment relative to map or viewport. |
| mapView | Map view to apply to. |

- 

togglePopup(in:)

Asynchronous

Toggles the popup bound to the marker.

#### Declaration

Swift
@MainActor
public func togglePopup(in mapView: MTMapView) async

#### Parameters

| mapView | Map view to apply to. |

- 

getCoordinates(in:)

Asynchronous

Returns current coordinates of the marker.

#### Declaration

Swift
@MainActor
public func getCoordinates(in mapView: MTMapView) async -> CLLocationCoordinate2D

#### Parameters

| mapView | Map view to query. |

- 

getPitchAlignment(in:)

Asynchronous

Returns the marker’s pitch alignment.

#### Declaration

Swift
@MainActor
public func getPitchAlignment(in mapView: MTMapView) async -> MTMarkerPitchAlignment

#### Parameters

| mapView | Map view to query. |

- 

getRotation(in:)

Asynchronous

Returns the marker’s rotation value.

#### Declaration

Swift
@MainActor
public func getRotation(in mapView: MTMapView) async -> Double

#### Parameters

| mapView | Map view to query. |

- 

getRotationAlignment(in:)

Asynchronous

Returns the marker’s rotation alignment.

#### Declaration

Swift
@MainActor
public func getRotationAlignment(in mapView: MTMapView) async -> MTMarkerRotationAlignment

#### Parameters

| mapView | Map view to query. |

- 

getOffset(in:)

Asynchronous

Returns the marker’s offset value in pixels.

#### Declaration

Swift
@MainActor
public func getOffset(in mapView: MTMapView) async -> Double

#### Parameters

| mapView | Map view to query. |

- 

isDraggable(in:)

Asynchronous

Returns whether the marker is draggable.

#### Declaration

Swift
@MainActor
public func isDraggable(in mapView: MTMapView) async -> Bool

#### Parameters

| mapView | Map view to query. |

- 

addToMap(_:)

Adds marker to map DSL style.

Prefer `addMarker(_:)` instead.

#### Declaration

Swift
`public func addToMap(_ mapView: MTMapView)`

- 

popup(_:)

Modifier. Sets the `popup`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func popup(_ value: MTTextPopup) -> Self

---

## File: Classes/MTPointLayerHelper.html

---
layout: mobile_sdk
title: "MTPointLayerHelper"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Helper for creating a point visualization layer from data and styling options."
id: mtpointlayerhelper
breadcrumb: "Mobile SDK/iOS/Reference/Classes"
---

# MTPointLayerHelper

`public final class MTPointLayerHelper : MTVectorLayerHelper, @unchecked Sendable`

Helper for creating a point visualization layer from data and styling options.

Uses the current style to create the underlying source and layers.

- 

style

Undocumented

#### Declaration

Swift
`public var style: MTStyle { get }`

- 

init(_:)

Undocumented

#### Declaration

Swift
`public init(_ style: MTStyle)`

- 

addPoint(_:completionHandler:)

Adds a point layer based on the provided options.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func addPoint(_ options: MTPointLayerOptions, completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

- 

addPoint(_:)

Asynchronous

Adds a point layer based on the provided options.

#### Declaration

Swift
`public func addPoint(_ options: MTPointLayerOptions) async`

- 

addPoint(_:colorRamp:in:)

Asynchronous

Adds a point layer using a ColorRamp for pointColor.

#### Declaration

Swift
`public func addPoint(_ options: MTPointLayerOptions, colorRamp: MTColorRamp, in mapView: MTMapView) async`

- 

addPoint(_:colorRamp:in:completionHandler:)

Adds a point layer using a ColorRamp for pointColor (completion-based variant).

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func addPoint(
_ options: MTPointLayerOptions,
colorRamp: MTColorRamp,
in mapView: MTMapView,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

---

## File: Classes/MTPolygonLayerHelper.html

---
layout: mobile_sdk
title: "MTPolygonLayerHelper"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Helper for creating a polygon (fill) visualization layer from data and styling options."
id: mtpolygonlayerhelper
breadcrumb: "Mobile SDK/iOS/Reference/Classes"
---

# MTPolygonLayerHelper

`public final class MTPolygonLayerHelper : MTVectorLayerHelper, @unchecked Sendable`

Helper for creating a polygon (fill) visualization layer from data and styling options.

- 

style

Undocumented

#### Declaration

Swift
`public var style: MTStyle { get }`

- 

init(_:)

Undocumented

#### Declaration

Swift
`public init(_ style: MTStyle)`

- 

addPolygon(_:completionHandler:)

Adds a polygon layer based on the provided options.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func addPolygon(
_ options: MTPolygonLayerOptions,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

- 

addPolygon(_:)

Asynchronous

Adds a polygon layer based on the provided options (async).

#### Declaration

Swift
`public func addPolygon(_ options: MTPolygonLayerOptions) async`

---

## File: Classes/MTPolylineLayerHelper.html

---
layout: mobile_sdk
title: "MTPolylineLayerHelper"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Helper for creating a polyline (line) visualization layer from data and styling options."
id: mtpolylinelayerhelper
breadcrumb: "Mobile SDK/iOS/Reference/Classes"
---

# MTPolylineLayerHelper

`public final class MTPolylineLayerHelper : MTVectorLayerHelper, @unchecked Sendable`

Helper for creating a polyline (line) visualization layer from data and styling options.

- 

style

Undocumented

#### Declaration

Swift
`public var style: MTStyle { get }`

- 

init(_:)

Undocumented

#### Declaration

Swift
`public init(_ style: MTStyle)`

- 

addPolyline(_:completionHandler:)

Adds a polyline layer based on the provided options.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func addPolyline(
_ options: MTPolylineLayerOptions,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

- 

addPolyline(_:)

Asynchronous

Adds a polyline layer based on the provided options (async).

#### Declaration

Swift
`public func addPolyline(_ options: MTPolylineLayerOptions) async`

---

## File: Classes/MTRasterDEMSource.html

---
layout: mobile_sdk
title: "MTRasterDEMSource"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "A raster DEM source. Only supports Terrain RGB."
id: mtrasterdemsource
breadcrumb: "Mobile SDK/iOS/Reference/Classes"
---

# MTRasterDEMSource

`public class MTRasterDEMSource : MTTileSource, @unchecked Sendable`

A raster DEM source. Only supports Terrain RGB.

- 

identifier

Unique identifier of a source.

#### Declaration

Swift
`public var identifier: String`

- 

bounds

An array containing the longitude and latitude of the southwest and northeast corners
of the source’s bounding box in the following order: [sw.lng, sw.lat, ne.lng, ne.lat].

Note
Defaults to [-180, -85.051129, 180, 85.051129].

#### Declaration

Swift
`public var bounds: [Double]`

- 

maxZoom

Maximum zoom level for which tiles are available.

Note
Defaults to 22.

#### Declaration

Swift
`public var maxZoom: Double`

- 

minZoom

Minimum zoom level for which tiles are available.

Note
Defaults to 0.

#### Declaration

Swift
`public var minZoom: Double`

- 

tileSize

The minimum visual size to display tiles for this layer. Units in pixels.

Note
Defaults to 512.

#### Declaration

Swift
`public var tileSize: Int`

- 

encoding

DEM encoding format. Defaults to Terrain RGB (mapbox).

#### Declaration

Swift
`public var encoding: MTRasterDEMEncoding`

- 

tiles

An array of one or more tile source URLs.

#### Declaration

Swift
`public var tiles: [URL]?`

- 

url

A URL to a TileJSON resource. Supported protocols are http, https.

#### Declaration

Swift
`public var url: URL?`

- 

attribution

Attribution to be displayed when the map is shown to a user.

#### Declaration

Swift
`public var attribution: String?`

- 

type

Type of the source.

#### Declaration

Swift
`public private(set) var type: MTSourceType { get }`

- 

init(identifier:url:)

Initializes the source with unique id and url to TileJSON resource.

#### Declaration

Swift
`public init(identifier: String, url: URL)`

- 

init(identifier:tiles:)

Initializes the source with unique id and one or more tile source urls.

#### Declaration

Swift
`public init(identifier: String, tiles: [URL])`

- 

init(identifier:bounds:maxZoom:minZoom:tileSize:encoding:tiles:url:attribution:)

Initializes the source with all options.

#### Declaration

Swift
public init(
identifier: String,
bounds: [Double],
maxZoom: Double,
minZoom: Double,
tileSize: Int = 512,
encoding: MTRasterDEMEncoding = .mapbox,
tiles: [URL]? = nil,
url: URL? = nil,
attribution: String? = nil
)

- 

setURL(url:in:completionHandler:)

Sets the url of the source.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setURL(url: URL, in mapView: MTMapView, completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

- 

setTiles(tiles:in:completionHandler:)

Sets the tiles of the source.

#### Declaration

Swift
@MainActor
public func setTiles(
tiles: [URL],
in mapView: MTMapView,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

- 

setURL(url:in:)

Asynchronous

Sets the url of the source.

#### Declaration

Swift
@MainActor
public func setURL(url: URL, in mapView: MTMapView) async

- 

setTiles(tiles:in:)

Asynchronous

Sets the tiles of the source.

#### Declaration

Swift
@MainActor
public func setTiles(tiles: [URL], in mapView: MTMapView) async

- 

addToMap(_:)

Adds source to map DSL style.

Prefer `addSource(_:)` on MTMapView instead.

#### Declaration

Swift
`public func addToMap(_ mapView: MTMapView)`

---

## File: Classes/MTRasterLayer.html

---
layout: mobile_sdk
title: "MTRasterLayer"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "The raster style layer renders raster map textures such as imagery."
id: mtrasterlayer
breadcrumb: "Mobile SDK/iOS/Reference/Classes"
---

# MTRasterLayer

`public class MTRasterLayer : MTLayer, @unchecked Sendable, Codable`

The raster style layer renders raster map textures such as imagery.

- 

identifier

Unique layer identifier.

#### Declaration

Swift
`public var identifier: String`

- 

type

Type of the layer.

#### Declaration

Swift
`public private(set) var type: MTLayerType { get }`

- 

sourceIdentifier

Identifier of the source to be used for this layer.

#### Declaration

Swift
`public var sourceIdentifier: String`

- 

maxZoom

The maximum zoom level for the layer.
Optional number between 0 and 24. At zoom levels equal to or greater than the maxzoom,
the layer will be hidden.

#### Declaration

Swift
`public var maxZoom: Double?`

- 

minZoom

The minimum zoom level for the layer.
Optional number between 0 and 24. At zoom levels less than the minzoom,
the layer will be hidden.

#### Declaration

Swift
`public var minZoom: Double?`

- 

sourceLayer

Layer to use from a vector tile source.
Required for vector tile sources; prohibited for all other source types.

#### Declaration

Swift
`public var sourceLayer: String?`

Paint properties

- 

brightnessMax

Increase or reduce the brightness of the image. The value is the maximum brightness.
Optional number between 0 and 1 inclusive. Defaults to 1.

#### Declaration

Swift
`public var brightnessMax: Double?`

- 

brightnessMin

Increase or reduce the brightness of the image. The value is the minimum brightness.
Optional number between 0 and 1 inclusive. Defaults to 0.

#### Declaration

Swift
`public var brightnessMin: Double?`

- 

contrast

Increase or reduce the contrast of the image.
Optional number between -1 and 1 inclusive. Defaults to 0.

#### Declaration

Swift
`public var contrast: Double?`

- 

fadeDuration

Fade duration when a new tile is added. Units in milliseconds. Defaults to 300.

#### Declaration

Swift
`public var fadeDuration: Double?`

- 

hueRotate

Rotates hues around the color wheel. Units in degrees. Defaults to 0.

#### Declaration

Swift
`public var hueRotate: Double?`

- 

opacity

The opacity at which the image will be drawn.
Optional number between 0 and 1 inclusive. Defaults to 1.

#### Declaration

Swift
`public var opacity: Double?`

- 

resampling

The resampling/interpolation method to use for overscaling.
Defaults to “linear”.

#### Declaration

Swift
`public var resampling: MTRasterResampling?`

- 

saturation

Increase or reduce the saturation of the image.
Optional number between -1 and 1 inclusive. Defaults to 0.

#### Declaration

Swift
`public var saturation: Double?`

Layout properties

- 

visibility

Whether this layer is displayed. Defaults to “visible”.

#### Declaration

Swift
`public var visibility: MTLayerVisibility?`

Initializers

- 

init(identifier:sourceIdentifier:)

Initializes the layer with required identifiers.

#### Declaration

Swift
public init(
identifier: String,
sourceIdentifier: String
)

- 

init(identifier:sourceIdentifier:maxZoom:minZoom:sourceLayer:brightnessMax:brightnessMin:contrast:fadeDuration:hueRotate:opacity:resampling:saturation:visibility:)

Initializes the layer with all options.

#### Declaration

Swift
public init(
identifier: String,
sourceIdentifier: String,
maxZoom: Double? = nil,
minZoom: Double? = nil,
sourceLayer: String? = nil,
brightnessMax: Double? = 1.0,
brightnessMin: Double? = 0.0,
contrast: Double? = 0.0,
fadeDuration: Double? = 300.0,
hueRotate: Double? = 0.0,
opacity: Double? = 1.0,
resampling: MTRasterResampling? = .linear,
saturation: Double? = 0.0,
visibility: MTLayerVisibility? = .visible
)

Codable

- 

init(from:)

Initializes the layer from the decoder.

#### Declaration

Swift
`public required init(from decoder: any Decoder) throws`

- 

encode(to:)

#### Declaration

Swift
`public func encode(to encoder: Encoder) throws`

- 

addToMap(_:)

Adds layer to map DSL style.

Prefer `addLayer(_:)` on MTMapView instead.

#### Declaration

Swift
`public func addToMap(_ mapView: MTMapView)`

- 

maxZoom(_:)

Modifier. Sets the `maxZoom`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func maxZoom(_ value: Double) -> Self

- 

minZoom(_:)

Modifier. Sets the `minZoom`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func minZoom(_ value: Double) -> Self

- 

sourceLayer(_:)

Modifier. Sets the `sourceLayer`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func sourceLayer(_ value: String) -> Self

- 

brightnessMax(_:)

Modifier. Sets the `brightnessMax`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func brightnessMax(_ value: Double) -> Self

- 

brightnessMin(_:)

Modifier. Sets the `brightnessMin`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func brightnessMin(_ value: Double) -> Self

- 

contrast(_:)

Modifier. Sets the `contrast`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func contrast(_ value: Double) -> Self

- 

fadeDuration(_:)

Modifier. Sets the `fadeDuration`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func fadeDuration(_ value: Double) -> Self

- 

hueRotate(_:)

Modifier. Sets the `hueRotate`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func hueRotate(_ value: Double) -> Self

- 

opacity(_:)

Modifier. Sets the `opacity`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func opacity(_ value: Double) -> Self

- 

resampling(_:)

Modifier. Sets the `resampling`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func resampling(_ value: MTRasterResampling) -> Self

- 

saturation(_:)

Modifier. Sets the `saturation`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func saturation(_ value: Double) -> Self

- 

visibility(_:)

Modifier. Sets the `visibility`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func visibility(_ value: MTLayerVisibility) -> Self

---

## File: Classes/MTRasterTileSource.html

---
layout: mobile_sdk
title: "MTRasterTileSource"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "A raster tile source."
id: mtrastertilesource
breadcrumb: "Mobile SDK/iOS/Reference/Classes"
---

# MTRasterTileSource

`public class MTRasterTileSource : MTTileSource, @unchecked Sendable`

A raster tile source.

For raster tiles hosted by MapTiler, the “url” value should be of the form
https://api.maptiler.com/tiles/[tilesetid]/tiles.json?key=

- 

identifier

Unique identifier of a source.

#### Declaration

Swift
`public var identifier: String`

- 

bounds

An array containing the longitude and latitude of the southwest and northeast corners
of the source’s bounding box in the following order: [sw.lng, sw.lat, ne.lng, ne.lat].

Note
Defaults to [-180, -85.051129, 180, 85.051129].

#### Declaration

Swift
`public var bounds: [Double]`

- 

maxZoom

Maximum zoom level for which tiles are available.

Note
Defaults to 22.

#### Declaration

Swift
`public var maxZoom: Double`

- 

minZoom

Minimum zoom level for which tiles are available.

Note
Defaults to 0.

#### Declaration

Swift
`public var minZoom: Double`

- 

scheme

Scheme used for tiles.

Influences the y direction of the tile coordinates. The global-mercator (aka Spherical Mercator)
profile is assumed.

#### Declaration

Swift
`public var scheme: MTTileScheme`

- 

tileSize

The minimum visual size to display tiles for this layer. Units in pixels.

Note
Defaults to 512. Only configurable for raster layers.

#### Declaration

Swift
`public var tileSize: Int`

- 

tiles

An array of one or more tile source URLs.

#### Declaration

Swift
`public var tiles: [URL]?`

- 

url

A URL to a TileJSON resource. Supported protocols are http, https.

#### Declaration

Swift
`public var url: URL?`

- 

attribution

Attribution to be displayed when the map is shown to a user.

#### Declaration

Swift
`public var attribution: String?`

- 

type

Type of the source.

#### Declaration

Swift
`public private(set) var type: MTSourceType { get }`

- 

init(identifier:url:)

Initializes the source with unique id and url to TileJSON resource.

#### Declaration

Swift
`public init(identifier: String, url: URL)`

- 

init(identifier:tiles:)

Initializes the source with unique id and one or more tile source urls.

#### Declaration

Swift
`public init(identifier: String, tiles: [URL])`

- 

init(identifier:bounds:maxZoom:minZoom:scheme:tileSize:tiles:url:attribution:)

Initializes the source with all options.

#### Declaration

Swift
public init(
identifier: String,
bounds: [Double],
maxZoom: Double,
minZoom: Double,
scheme: MTTileScheme,
tileSize: Int = 512,
tiles: [URL]? = nil,
url: URL? = nil,
attribution: String? = nil
)

- 

setURL(url:in:completionHandler:)

Sets the url of the source.

Used for updating the source data.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setURL(url: URL, in mapView: MTMapView, completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| url | url to Raster Tile resource. |
| mapView | MTMapView which holds the source. |
| completionHandler | A handler block to execute when function finishes. |

- 

setTiles(tiles:in:completionHandler:)

Sets the tiles of the source.

Used for updating the source data.

#### Declaration

Swift
@MainActor
public func setTiles(
tiles: [URL],
in mapView: MTMapView,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| tiles | list of urls with tile resources. |
| mapView | MTMapView which holds the source. |
| completionHandler | A handler block to execute when function finishes. |

- 

setURL(url:in:)

Asynchronous

Sets the url of the source.

Used for updating the source data.

#### Declaration

Swift
@MainActor
public func setURL(url: URL, in mapView: MTMapView) async

#### Parameters

| url | url to Raster Tile resource. |
| mapView | MTMapView which holds the source. |

- 

setTiles(tiles:in:)

Asynchronous

Sets the tiles of the source.

Used for updating the source data.

#### Declaration

Swift
@MainActor
public func setTiles(tiles: [URL], in mapView: MTMapView) async

#### Parameters

| tiles | list of urls with tile resources. |
| mapView | MTMapView which holds the source. |

- 

addToMap(_:)

Adds source to map DSL style.

Prefer `addSource(_:)` on MTMapView instead.

#### Declaration

Swift
`public func addToMap(_ mapView: MTMapView)`

---

## File: Classes/MTStyle.html

---
layout: mobile_sdk
title: "MTStyle"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "The proxy object for the current map style."
id: mtstyle
breadcrumb: "Mobile SDK/iOS/Reference/Classes"
---

# MTStyle

@MainActor
public class MTStyle

The proxy object for the current map style.

Set of convenience methods for style, sources and layers manipulation.
MTStyle is nil until map loading is complete.
Since it is loaded asynchronously it should be manipulated only after `MTEvent.didLoad` triggers.

- 

referenceStyle

Current reference style of the map object.

#### Declaration

Swift
@MainActor
public private(set) var referenceStyle: MTMapReferenceStyle { get }

- 

styleVariant

Current style variant of the map object.

#### Declaration

Swift
@MainActor
public private(set) var styleVariant: MTMapStyleVariant? { get }

- 

setStyle(_:styleVariant:completionHandler:)

Updates the map’s style object with a new value.

Setting the style resets custom sources and layers, so make sure to wait for style to load
(`styleDidUpdate`) before adding them.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setStyle(
_ referenceStyle: MTMapReferenceStyle,
styleVariant: MTMapStyleVariant?,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| referenceStyle | Desired reference map style. |
| styleVariant | Optional variant of the reference style. |
| completionHandler | A handler block to execute when function finishes. |

- 

getVariantsForCurrentReferenceStyle()

Returns variants for the current reference style if they exist.

#### Declaration

Swift
@MainActor
public func getVariantsForCurrentReferenceStyle() -> [MTMapStyleVariant]?

- 

getVariants(for:)

Returns variants for the provided reference style if they exist.

#### Declaration

Swift
@MainActor
public func getVariants(for referenceStyle: MTMapReferenceStyle) -> [MTMapStyleVariant]?

#### Parameters

| referenceStyle | Reference style for which to get variants. |

- 

getIdForCurrentReferenceStyle(completionHandler:)

Returns ID of the current reference style.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func getIdForCurrentReferenceStyle(completionHandler: ((Result<String, MTError>) -> Void)? = nil)

#### Parameters

| completionHandler | A handler block to execute when function finishes. |

- 

getId(for:completionHandler:)

Returns ID for the provided reference style.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func getId(
for referenceStyle: MTMapReferenceStyle,
completionHandler: ((Result<String, MTError>) -> Void)? = nil
)

#### Parameters

| referenceStyle | Reference style for which to get id. |
| completionHandler | A handler block to execute when function finishes. |

- 

getIdForCurrentStyleVariant(completionHandler:)

Returns ID of the current style variant, if it exists.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func getIdForCurrentStyleVariant(completionHandler: ((Result<String, MTError>) -> Void)? = nil)

#### Parameters

| completionHandler | A handler block to execute when function finishes. |

- 

getId(for:completionHandler:)

Returns id for the provided style variant.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func getId(
for styleVariant: MTMapStyleVariant,
completionHandler: ((Result<String, MTError>) -> Void)? = nil
)

#### Parameters

| styleVariant | Style variant for which to get id. |
| completionHandler | A handler block to execute when function finishes. |

- 

getNameForCurrentReferenceStyle(completionHandler:)

Returns name of the current reference style.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func getNameForCurrentReferenceStyle(completionHandler: ((Result<String, MTError>) -> Void)? = nil)

#### Parameters

| completionHandler | A handler block to execute when function finishes. |

- 

getName(for:completionHandler:)

Returns name of the provided reference style.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func getName(
for referenceStyle: MTMapReferenceStyle,
completionHandler: ((Result<String, MTError>) -> Void)? = nil
)

#### Parameters

| referenceStyle | Reference style for which to get name. |
| completionHandler | A handler block to execute when function finishes. |

- 

getNameForCurrentStyleVariant(completionHandler:)

Returns name of the current style variant, if it exists.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func getNameForCurrentStyleVariant(completionHandler: ((Result<String, MTError>) -> Void)? = nil)

#### Parameters

| completionHandler | A handler block to execute when function finishes. |

- 

getName(for:completionHandler:)

Returns name for the provided style variant.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func getName(
for styleVariant: MTMapStyleVariant,
completionHandler: ((Result<String, MTError>) -> Void)? = nil
)

#### Parameters

| styleVariant | Style variant for which to get name. |
| completionHandler | A handler block to execute when function finishes. |

Utilities

- 

forceReloadStyle(completionHandler:)

Forces a style reload using the current reference style and variant.
Also reapplies any configured `space` from map options to keep background consistent.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func forceReloadStyle(completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| completionHandler | Optional completion handler (deprecated; prefer async overload). |

- 

forceReloadStyle()

Asynchronous

Forces a style reload using the current reference style and variant.
Also reapplies any configured `space` from map options to keep background consistent.

#### Declaration

Swift
@MainActor
public func forceReloadStyle() async

Circle helpers

- 

setCircleRadiusStep(layerId:key:default:stops:completionHandler:)

Sets circle radius as a step expression on a feature key.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
func setCircleRadiusStep(
layerId: String,
key: MTFeatureKey,
default defaultRadius: Double,
stops: [(Double, Double)],
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

- 

setCircleColorStep(layerId:key:default:stops:completionHandler:)

Sets circle color as a step expression on a feature key.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
func setCircleColorStep(
layerId: String,
key: MTFeatureKey,
default defaultColor: UIColor,
stops: [(Double, UIColor)],
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

Symbol helpers

- 

setTextFieldToken(layerId:token:completionHandler:)

Sets text field using a common token.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
func setTextFieldToken(
layerId: String,
token: MTTextToken,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

- 

setTextSize(layerId:size:completionHandler:)

Sets text size.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
func setTextSize(
layerId: String,
size: Double,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

- 

setTextAllowOverlap(layerId:_:completionHandler:)

Sets text allow overlap.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
func setTextAllowOverlap(
layerId: String,
_ allow: Bool,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

- 

setTextColor(layerId:color:completionHandler:)

Sets text color.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
func setTextColor(
layerId: String,
color: UIColor,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

- 

setTextAnchor(layerId:anchor:completionHandler:)

Sets text anchor.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
func setTextAnchor(
layerId: String,
anchor: MTTextAnchor,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

- 

setTextFont(layerId:fonts:completionHandler:)

Sets text font. Provide an ordered list of font families.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
func setTextFont(
layerId: String,
fonts: [String],
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

Async versions

- 

setCircleRadiusStep(layerId:key:default:stops:)

Asynchronous

Sets circle radius as a step expression on a feature key.

#### Declaration

Swift
@MainActor
func setCircleRadiusStep(
layerId: String,
key: MTFeatureKey,
default defaultRadius: Double,
stops: [(Double, Double)]
) async

- 

setCircleColorStep(layerId:key:default:stops:)

Asynchronous

Sets circle color as a step expression on a feature key.

#### Declaration

Swift
@MainActor
func setCircleColorStep(
layerId: String,
key: MTFeatureKey,
default defaultColor: UIColor,
stops: [(Double, UIColor)]
) async

- 

setTextFieldToken(layerId:token:)

Asynchronous

Undocumented

#### Declaration

Swift
@MainActor
func setTextFieldToken(layerId: String, token: MTTextToken) async

- 

setTextSize(layerId:size:)

Asynchronous

Sets text size.

#### Declaration

Swift
@MainActor
func setTextSize(layerId: String, size: Double) async

- 

setTextAllowOverlap(layerId:_:)

Asynchronous

Sets text allow overlap.

#### Declaration

Swift
@MainActor
func setTextAllowOverlap(layerId: String, _ allow: Bool) async

- 

setTextColor(layerId:color:)

Asynchronous

Sets text color.

#### Declaration

Swift
@MainActor
func setTextColor(layerId: String, color: UIColor) async

- 

setTextAnchor(layerId:anchor:)

Asynchronous

Sets text anchor.

#### Declaration

Swift
@MainActor
func setTextAnchor(layerId: String, anchor: MTTextAnchor) async

- 

setTextFont(layerId:fonts:)

Asynchronous

Sets text font. Provide an ordered list of font families.

#### Declaration

Swift
@MainActor
func setTextFont(layerId: String, fonts: [String]) async

- 

addSource(_:completionHandler:)

Adds a source to the map.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func addSource(_ source: MTSource, completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| source | Source to be added. |

- 

removeSource(_:completionHandler:)

Removes a source from the map.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func removeSource(_ source: MTSource, completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| source | Source to be removed. |

- 

sourceExists(_:)

Returns a boolean indicating whether a source is already added to the map.

#### Declaration

Swift
@MainActor
public func sourceExists(_ source: MTSource) -> Bool

- 

addLayer(_:completionHandler:)

Adds a layer to the map.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func addLayer(_ layer: MTLayer, completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| layer | Layer to be added. |

- 

addLayers(_:completionHandler:)

Adds multiple layers to the map.

Note
All parent sources must be loaded prior to calling this method.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func addLayers(_ layers: [MTLayer], completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| layers | Layers to be added. |

- 

removeLayer(_:completionHandler:)

Removes a layer from the map.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func removeLayer(_ layer: MTLayer, completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| layer | Layer to be removed. |

- 

removeLayers(_:completionHandler:)

Remove multiple layers from the map.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func removeLayers(_ layers: [MTLayer], completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| layers | Layers to be removed. |

- 

layerExists(_:)

Returns a boolean indicating whether a layer is already added to the map.

#### Declaration

Swift
@MainActor
public func layerExists(_ layer: MTLayer) -> Bool

- 

setStyle(_:styleVariant:)

Asynchronous

Updates the map’s style object with a new value.

Setting the style resets custom sources and layers, so make sure to wait for style to load
(`styleDidUpdate`) before adding them.

#### Declaration

Swift
@MainActor
public func setStyle(_ referenceStyle: MTMapReferenceStyle, styleVariant: MTMapStyleVariant?) async

#### Parameters

| referenceStyle | Desired reference map style. |
| styleVariant | Optional variant of the reference style. |

- 

getIdForCurrentReferenceStyle()

Asynchronous

Returns ID of the current reference style.

#### Declaration

Swift
@MainActor
public func getIdForCurrentReferenceStyle() async -> String

- 

getId(for:)

Asynchronous

Returns ID for the provided reference style.

#### Declaration

Swift
@MainActor
public func getId(for referenceStyle: MTMapReferenceStyle) async -> String

#### Parameters

| referenceStyle | Reference style for which to get id. |

- 

getIdForCurrentStyleVariant()

Asynchronous

Returns ID of the current style variant, if it exists.

#### Declaration

Swift
@MainActor
public func getIdForCurrentStyleVariant() async -> String?

- 

getId(for:)

Asynchronous

Returns id for the provided style variant.

#### Declaration

Swift
@MainActor
public func getId(for styleVariant: MTMapStyleVariant) async -> String

#### Parameters

| styleVariant | Style variant for which to get id. |

- 

getNameForCurrentReferenceStyle()

Asynchronous

Returns name of the current reference style.

#### Declaration

Swift
@MainActor
public func getNameForCurrentReferenceStyle() async -> String

- 

getName(for:)

Asynchronous

Returns name of the provided reference style.

#### Declaration

Swift
@MainActor
public func getName(for referenceStyle: MTMapReferenceStyle) async -> String

#### Parameters

| referenceStyle | Reference style for which to get name. |

- 

getNameForCurrentStyleVariant()

Asynchronous

Returns name of the current style variant, if it exists.

#### Declaration

Swift
@MainActor
public func getNameForCurrentStyleVariant() async -> String?

- 

getName(for:)

Asynchronous

Returns name for the provided style variant.

#### Declaration

Swift
@MainActor
public func getName(for styleVariant: MTMapStyleVariant) async -> String

#### Parameters

| styleVariant | Style variant for which to get name. |

- 

addSource(_:)

Asynchronous

Adds a source to the map.

Throws
A `MTStyleError.sourceAlreadyExists` if source with the same
id is already added to the map.

#### Declaration

Swift
@MainActor
public func addSource(_ source: MTSource) async throws

#### Parameters

| source | Source to be added. |

- 

removeSource(_:)

Asynchronous

Removes a source from the map.

Throws
A `MTStyleError.sourceNotFound` if source does not exist on the map.

#### Declaration

Swift
@MainActor
public func removeSource(_ source: MTSource) async throws

#### Parameters

| source | Source to be removed. |

- 

addLayer(_:)

Asynchronous

Adds a layer to the map.

Throws
A `MTStyleError.layerAlreadyExists` if layer with the same
id is already added to the map.

#### Declaration

Swift
@MainActor
public func addLayer(_ layer: MTLayer) async throws

#### Parameters

| layer | Layer to be added. |

- 

addLayers(_:)

Asynchronous

Adds multiple layers to the map.

Note
All parent sources must be loaded prior to calling this method.

#### Declaration

Swift
@MainActor
public func addLayers(_ layers: [MTLayer]) async throws

#### Parameters

| layers | Layers to be added. |

- 

removeLayer(_:)

Asynchronous

Removes a layer from the map.

Throws
A `MTStyleError.layerNotFound` if layer does not exist on the map.

#### Declaration

Swift
@MainActor
public func removeLayer(_ layer: MTLayer) async throws

#### Parameters

| layer | Layer to be removed. |

- 

removeLayers(_:)

Asynchronous

Removes multiple layers from the map.

#### Declaration

Swift
@MainActor
public func removeLayers(_ layers: [MTLayer]) async throws

#### Parameters

| layers | Layers to be removed. |

Style property setters

- 

setFilter(layerId:filter:completionHandler:)

Sets a filter expression on a layer.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setFilter(
layerId: String,
filter: MTPropertyValue,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| layerId | Target layer identifier. |
| filter | Expression value |

- 

setLayoutProperty(layerId:name:value:completionHandler:)

Sets a layout property on a layer.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setLayoutProperty(
layerId: String,
name: String,
value: MTPropertyValue,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| layerId | Target layer identifier. |
| name | Layout property name |
| value | Property value or expression. |

- 

setPaintProperty(layerId:name:value:completionHandler:)

Sets a paint property on a layer.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setPaintProperty(
layerId: String,
name: String,
value: MTPropertyValue,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| layerId | Target layer identifier. |
| name | Paint property name |
| value | Property value or expression. |

Typed property setters (overloads)

- 

setLayoutProperty(layerId:property:value:completionHandler:)

Sets a symbol layout property using a typed key.

#### Declaration

Swift
@MainActor
public func setLayoutProperty(
layerId: String,
property: MTSymbolLayoutProperty,
value: MTPropertyValue,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| layerId | Target layer identifier. |
| property | Typed layout property key for symbol layers. |
| value | Property value or expression. |
| completionHandler | A handler block to execute when function finishes. |

- 

setPaintProperty(layerId:property:value:completionHandler:)

Sets a circle paint property using a typed key.

#### Declaration

Swift
@MainActor
public func setPaintProperty(
layerId: String,
property: MTCirclePaintProperty,
value: MTPropertyValue,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| layerId | Target layer identifier. |
| property | Typed paint property key for circle layers. |
| value | Property value or expression. |
| completionHandler | A handler block to execute when function finishes. |

- 

setPaintProperty(layerId:property:value:completionHandler:)

Sets a symbol paint property using a typed key.

#### Declaration

Swift
@MainActor
public func setPaintProperty(
layerId: String,
property: MTSymbolPaintProperty,
value: MTPropertyValue,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| layerId | Target layer identifier. |
| property | Typed paint property key for symbol layers. |
| value | Property value or expression. |
| completionHandler | A handler block to execute when function finishes. |

Style property setters

- 

setFilter(layerId:filter:)

Asynchronous

Undocumented

#### Declaration

Swift
@MainActor
public func setFilter(layerId: String, filter: MTPropertyValue) async

- 

setLayoutProperty(layerId:name:value:)

Asynchronous

Undocumented

#### Declaration

Swift
@MainActor
public func setLayoutProperty(layerId: String, name: String, value: MTPropertyValue) async

- 

setPaintProperty(layerId:name:value:)

Asynchronous

Undocumented

#### Declaration

Swift
@MainActor
public func setPaintProperty(layerId: String, name: String, value: MTPropertyValue) async

Typed property setters (async)

- 

setLayoutProperty(layerId:property:value:)

Asynchronous

Sets a symbol layout property using a typed key (async).

#### Declaration

Swift
@MainActor
public func setLayoutProperty(layerId: String, property: MTSymbolLayoutProperty, value: MTPropertyValue) async

#### Parameters

| layerId | Target layer identifier. |
| property | Typed layout property key for symbol layers. |
| value | Property value or expression. |

- 

setPaintProperty(layerId:property:value:)

Asynchronous

Sets a circle paint property using a typed key (async).

#### Declaration

Swift
@MainActor
public func setPaintProperty(layerId: String, property: MTCirclePaintProperty, value: MTPropertyValue) async

#### Parameters

| layerId | Target layer identifier. |
| property | Typed paint property key for circle layers. |
| value | Property value or expression. |

- 

setPaintProperty(layerId:property:value:)

Asynchronous

Sets a symbol paint property using a typed key (async).

#### Declaration

Swift
@MainActor
public func setPaintProperty(layerId: String, property: MTSymbolPaintProperty, value: MTPropertyValue) async

#### Parameters

| layerId | Target layer identifier. |
| property | Typed paint property key for symbol layers. |
| value | Property value or expression. |

---

## File: Classes/MTSymbolLayer.html

---
layout: mobile_sdk
title: "MTSymbolLayer"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "The symbol style that layer renders icon and text labels at points or along lines on a map."
id: mtsymbollayer
breadcrumb: "Mobile SDK/iOS/Reference/Classes"
---

# MTSymbolLayer

`public class MTSymbolLayer : MTLayer, @unchecked Sendable, Codable`
`extension MTSymbolLayer: Equatable`

The symbol style that layer renders icon and text labels at points or along lines on a map.

- 

identifier

Unique layer identifier.

#### Declaration

Swift
`public var identifier: String`

- 

type

Type of the layer.

#### Declaration

Swift
`public private(set) var type: MTLayerType { get }`

- 

sourceIdentifier

Identifier of the source to be used for this layer.

#### Declaration

Swift
`public var sourceIdentifier: String`

- 

maxZoom

The maximum zoom level for the layer.

Optional number between 0 and 24. At zoom levels equal to or greater than the maxzoom,
the layer will be hidden.

#### Declaration

Swift
`public var maxZoom: Double?`

- 

minZoom

The minimum zoom level for the layer.

Optional number between 0 and 24. At zoom levels less than the minzoom,
the layer will be hidden.

#### Declaration

Swift
`public var minZoom: Double?`

- 

sourceLayer

Layer to use from a vector tile source.

Required for vector tile sources; prohibited for all other source types,
including GeoJSON sources.

#### Declaration

Swift
`public var sourceLayer: String?`

- 

icon

Icon to use for the layer.

#### Declaration

Swift
`public var icon: UIImage?`

- 

visibility

Enum controlling whether this layer is displayed.

#### Declaration

Swift
`public var visibility: MTLayerVisibility?`

- 

initialFilter

Optional initial filter to apply after the layer is added to the map.

#### Declaration

Swift
`public var initialFilter: MTPropertyValue?`

Layout: text properties

- 

textField

Text field (tokens allowed), e.g. “{point_count_abbreviated}”

#### Declaration

Swift
`public var textField: String?`

- 

textSize

Text size in px

#### Declaration

Swift
`public var textSize: Double?`

- 

textAllowOverlap

Text allow overlap

#### Declaration

Swift
`public var textAllowOverlap: Bool?`

- 

textAnchor

Text anchor

#### Declaration

Swift
`public var textAnchor: MTTextAnchor?`

- 

textFont

Text font stack

#### Declaration

Swift
`public var textFont: [String]?`

- 

filterExpression

Inline filter expression for this layer

#### Declaration

Swift
`public var filterExpression: MTPropertyValue?`

Paint: text properties

- 

textColor

Text color

#### Declaration

Swift
`public var textColor: UIColor?`

- 

init(identifier:sourceIdentifier:maxZoom:minZoom:sourceLayer:)

Initializes the layer with unique identifier, source identifier, max and min zoom levels and source layer,
which is required for vector tile sources.

#### Declaration

Swift
public init(
identifier: String,
sourceIdentifier: String,
maxZoom: Double,
minZoom: Double,
sourceLayer: String? = nil
)

- 

init(identifier:sourceIdentifier:)

Initializes the layer with the unique identifier and a source identifier.

#### Declaration

Swift
public init(
identifier: String,
sourceIdentifier: String
)

- 

init(identifier:sourceIdentifier:maxZoom:minZoom:sourceLayer:icon:visibility:)

Undocumented

#### Declaration

Swift
public init(
identifier: String,
sourceIdentifier: String,
maxZoom: Double? = nil,
minZoom: Double? = nil,
sourceLayer: String? = nil,
icon: UIImage? = nil,
visibility: MTLayerVisibility? = .visible
)

- 

init(from:)

#### Declaration

Swift
`public required init(from decoder: any Decoder) throws`

- 

encode(to:)

#### Declaration

Swift
`public func encode(to encoder: Encoder) throws`

- 

addToMap(_:)

Adds layer to map DSL style.

Prefer `addLayer(_:)` on MTMapView instead.

#### Declaration

Swift
`public func addToMap(_ mapView: MTMapView)`

- 

maxZoom(_:)

Modifier. Sets the `maxZoom`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func maxZoom(_ value: Double) -> Self

- 

minZoom(_:)

Modifier. Sets the `minZoom`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func minZoom(_ value: Double) -> Self

- 

sourceLayer(_:)

Modifier. Sets the `sourceLayer`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func sourceLayer(_ value: String) -> Self

- 

icon(_:)

Modifier. Sets the `icon`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
`public func icon(_ value: UIImage) -> Self`

- 

textField(_:)

Sets the symbol text field (tokens allowed).

#### Declaration

Swift
@discardableResult
public func textField(_ value: String) -> Self

#### Parameters

| value | Text field string, e.g. “{point_count_abbreviated}”. |

- 

textSize(_:)

Sets the symbol text size.

#### Declaration

Swift
@discardableResult
public func textSize(_ value: Double) -> Self

#### Parameters

| value | Text size in points. |

- 

textAllowOverlap(_:)

Sets whether text labels can overlap.

#### Declaration

Swift
@discardableResult
public func textAllowOverlap(_ value: Bool) -> Self

#### Parameters

| value | True to allow overlap. |

- 

textAnchor(_:)

Sets the text anchor position.

#### Declaration

Swift
@discardableResult
public func textAnchor(_ value: MTTextAnchor) -> Self

#### Parameters

| value | Anchor for text placement. |

- 

textFont(_:)

Sets the preferred text fonts.

#### Declaration

Swift
@discardableResult
public func textFont(_ value: [String]) -> Self

#### Parameters

| value | Ordered list of font family names. |

- 

paintTextColor(_:)

Sets a constant text color for the symbol.

#### Declaration

Swift
@discardableResult
public func paintTextColor(_ value: UIColor) -> Self

#### Parameters

| value | UIColor value. |

- 

visibility(_:)

Modifier. Sets the `visibility`.

Note
Not to be used outside of DSL.

#### Declaration

Swift
@discardableResult
public func visibility(_ value: MTLayerVisibility) -> Self

- 

withFilter(_:)

Sets an inline filter expression for this layer.

#### Declaration

Swift
@discardableResult
public func withFilter(_ value: MTPropertyValue) -> Self

#### Parameters

| value | Filter expression. |

- 

==(_:_:)

#### Declaration

Swift
`public static func == (lhs: MTSymbolLayer, rhs: MTSymbolLayer) -> Bool`

---

## File: Classes/MTTextPopup.html

---
layout: mobile_sdk
title: "MTTextPopup"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Basic text popup."
id: mttextpopup
breadcrumb: "Mobile SDK/iOS/Reference/Classes"
---

# MTTextPopup

`public class MTTextPopup : MTAnnotation, MTMapViewContent, @unchecked Sendable`

Basic text popup.

Can be attached to MTMarker or standalone.

- 

identifier

Unique id of the popup.

#### Declaration

Swift
`public private(set) var identifier: String { get }`

- 

coordinates

Position of the popup on the map.

#### Declaration

Swift
`public private(set) var coordinates: CLLocationCoordinate2D { get }`

- 

text

Text content of the popup.

#### Declaration

Swift
`public private(set) var text: String { get }`

- 

offset

The pixel distance from the popup’s coordinates.

#### Declaration

Swift
`public private(set) var offset: Double? { get }`

- 

maxWidth

The maximum width of the popup in pixels.

#### Declaration

Swift
`public private(set) var maxWidth: Double? { get }`

- 

isSubpixelPositioningEnabled

Boolean value indicating whether the popup uses subpixel positioning.

#### Declaration

Swift
`public private(set) var isSubpixelPositioningEnabled: Bool { get }`

- 

isTrackingPointer

Boolean value indicating whether the popup is tracking the pointer.

#### Declaration

Swift
`public private(set) var isTrackingPointer: Bool { get }`

- 

isOpen

Boolean value indicating whether the popup is currently open on the map.

#### Declaration

Swift
`public private(set) var isOpen: Bool { get }`

- 

onOpen

Called when the popup opens on the map.

#### Declaration

Swift
`public var onOpen: (() -> Void)?`

- 

onClose

Called when the popup closes from the map.

#### Declaration

Swift
`public var onClose: (() -> Void)?`

- 

init(coordinates:text:offset:maxWidth:)

Initializes the popup with the specified position and text.

#### Declaration

Swift
public init(
coordinates: CLLocationCoordinate2D,
text: String,
offset: Double = 0.0,
maxWidth: Double? = nil
)

#### Parameters

| coordinates | Position of the popup. |
| text | Text content of the popup. |

- 

setCoordinates(_:in:completionHandler:)

Sets coordinates for the popup.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setCoordinates(
_ coordinates: CLLocationCoordinate2D,
in mapView: MTMapView,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| coordinates | Position of the popup |
| mapView | Map view to apply to. |
| completionHandler | A handler block to execute when function finishes. |

- 

setLngLat(_:in:completionHandler:)

Sets coordinates for the popup.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setLngLat(
_ coordinates: CLLocationCoordinate2D,
in mapView: MTMapView,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| coordinates | Position of the popup. |
| mapView | Map view to apply to. |
| completionHandler | A handler block to execute when function finishes. |

- 

setMaxWidth(_:in:completionHandler:)

Sets the maximum width of the popup in pixels.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setMaxWidth(
_ maxWidth: Double,
in mapView: MTMapView,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| maxWidth | Maximum width in pixels. |
| mapView | Map view to apply to. |
| completionHandler | A handler block to execute when function finishes. |

- 

setOffset(_:in:completionHandler:)

Sets the pixel offset distance from the popup’s anchor coordinate.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setOffset(
_ offset: Double,
in mapView: MTMapView,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| offset | Pixel offset applied on both axes. |
| mapView | Map view to apply to. |
| completionHandler | A handler block to execute when function finishes. |

- 

setSubpixelPositioning(_:in:completionHandler:)

Enables or disables subpixel positioning for the popup.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setSubpixelPositioning(
_ isEnabled: Bool,
in mapView: MTMapView,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| isEnabled | Boolean indicating whether subpixel positioning is enabled. |
| mapView | Map view to apply to. |
| completionHandler | A handler block to execute when function finishes. |

- 

setText(_:in:completionHandler:)

Updates the popup text content.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setText(
_ text: String,
in mapView: MTMapView,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| text | Text content of the popup. |
| mapView | Map view to apply to. |
| completionHandler | A handler block to execute when function finishes. |

- 

trackPointer(in:completionHandler:)

Enables tracking the pointer position for the popup.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func trackPointer(
in mapView: MTMapView,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| mapView | Map view to apply to. |
| completionHandler | A handler block to execute when function finishes. |

- 

open(in:completionHandler:)

Opens the popup on the provided map view.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func open(
in mapView: MTMapView,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| mapView | Map view to add the popup to. |
| completionHandler | A handler block to execute when function finishes. |

- 

close(in:completionHandler:)

Closes the popup on the provided map view.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func close(
in mapView: MTMapView,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| mapView | Map view to remove the popup from. |
| completionHandler | A handler block to execute when function finishes. |

- 

getCoordinates(in:completionHandler:)

Returns current coordinates of the popup.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func getCoordinates(
in mapView: MTMapView,
completionHandler: ((Result<CLLocationCoordinate2D, MTError>) -> Void)? = nil
)

#### Parameters

| mapView | Map view to query. |
| completionHandler | A handler block to execute when function finishes. |

- 

isOpen(in:completionHandler:)

Returns a Boolean value indicating whether the popup is currently open.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func isOpen(
in mapView: MTMapView,
completionHandler: ((Result<Bool, MTError>) -> Void)? = nil
)

#### Parameters

| mapView | Map view to query. |
| completionHandler | A handler block to execute when function finishes. |

- 

setCoordinates(_:in:)

Asynchronous

Sets coordinates for the popup.

#### Declaration

Swift
@MainActor
public func setCoordinates(_ coordinates: CLLocationCoordinate2D, in mapView: MTMapView) async

#### Parameters

| coordinates | Position of the popup. |
| mapView | Map view to apply to. |

- 

setLngLat(_:in:)

Asynchronous

Sets coordinates for the popup.

#### Declaration

Swift
@MainActor
public func setLngLat(_ coordinates: CLLocationCoordinate2D, in mapView: MTMapView) async

#### Parameters

| mapView | Map view to apply to. |

- 

setMaxWidth(_:in:)

Asynchronous

Sets the maximum width of the popup in pixels.

#### Declaration

Swift
@MainActor
public func setMaxWidth(_ maxWidth: Double, in mapView: MTMapView) async

#### Parameters

| mapView | Map view to apply to. |

- 

setOffset(_:in:)

Asynchronous

Sets the pixel offset distance from the popup’s anchor coordinate.

#### Declaration

Swift
@MainActor
public func setOffset(_ offset: Double, in mapView: MTMapView) async

#### Parameters

| mapView | Map view to apply to. |

- 

setSubpixelPositioning(_:in:)

Asynchronous

Enables or disables subpixel positioning for the popup.

#### Declaration

Swift
@MainActor
public func setSubpixelPositioning(_ isEnabled: Bool, in mapView: MTMapView) async

#### Parameters

| mapView | Map view to apply to. |

- 

setText(_:in:)

Asynchronous

Updates the popup text content.

#### Declaration

Swift
@MainActor
public func setText(_ text: String, in mapView: MTMapView) async

#### Parameters

| mapView | Map view to apply to. |

- 

trackPointer(in:)

Asynchronous

Enables tracking the pointer position for the popup.

#### Declaration

Swift
@MainActor
public func trackPointer(in mapView: MTMapView) async

#### Parameters

| mapView | Map view to apply to. |

- 

open(in:)

Asynchronous

Opens the popup on the provided map view.

#### Declaration

Swift
@MainActor
public func open(in mapView: MTMapView) async

#### Parameters

| mapView | Map view to add the popup to. |

- 

close(in:)

Asynchronous

Closes the popup on the provided map view.

#### Declaration

Swift
@MainActor
public func close(in mapView: MTMapView) async

#### Parameters

| mapView | Map view to remove the popup from. |

- 

getCoordinates(in:)

Asynchronous

Returns current coordinates of the popup.

#### Declaration

Swift
@MainActor
public func getCoordinates(in mapView: MTMapView) async -> CLLocationCoordinate2D

#### Parameters

| mapView | Map view to query. |

- 

isOpen(in:)

Asynchronous

Returns a Boolean value indicating whether the popup is currently open.

#### Declaration

Swift
@MainActor
public func isOpen(in mapView: MTMapView) async -> Bool

#### Parameters

| mapView | Map view to query. |

- 

addToMap(_:)

Adds popup to map DSL style.

Prefer `addTextPopup(_:)` instead.

#### Declaration

Swift
`public func addToMap(_ mapView: MTMapView)`

---

## File: Classes/MTVectorTileSource.html

---
layout: mobile_sdk
title: "MTVectorTileSource"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Undocumented"
id: mtvectortilesource
breadcrumb: "Mobile SDK/iOS/Reference/Classes"
---

# MTVectorTileSource

`public class MTVectorTileSource : MTTileSource, @unchecked Sendable`

Undocumented

- 

identifier

Unique identifier of a source.

#### Declaration

Swift
`public var identifier: String`

- 

bounds

An array containing the longitude and latitude of the southwest and northeast corners
of the source’s bounding box in the following order: [sw.lng, sw.lat, ne.lng, ne.lat].

Note
Defaults to [-180, -85.051129, 180, 85.051129].

#### Declaration

Swift
`public var bounds: [Double]`

- 

maxZoom

Maximum zoom level for which tiles are available.

Note
Defaults to 22.

#### Declaration

Swift
`public var maxZoom: Double`

- 

minZoom

Minimum zoom level for which tiles are available.

Note
Defaults to 0.

#### Declaration

Swift
`public var minZoom: Double`

- 

scheme

Scheme used for tiles.

Influences the y direction of the tile coordinates. The global-mercator (aka Spherical Mercator)
profile is assumed.

#### Declaration

Swift
`public var scheme: MTTileScheme`

- 

tiles

An array of one or more tile source URLs.

#### Declaration

Swift
`public var tiles: [URL]?`

- 

url

A URL to a TileJSON resource. Supported protocols are http, https.

#### Declaration

Swift
`public var url: URL?`

- 

attribution

Attribution to be displayed when the map is shown to a user.

#### Declaration

Swift
`public var attribution: String?`

- 

type

Type of the layer.

#### Declaration

Swift
`public private(set) var type: MTSourceType { get }`

- 

init(identifier:url:)

Initializes the source with unique id and url to TileJSON resource.

#### Declaration

Swift
`public init(identifier: String, url: URL)`

- 

init(identifier:tiles:)

Initializes the source with unique id and one or more tile source urls.

#### Declaration

Swift
`public init(identifier: String, tiles: [URL])`

- 

init(identifier:bounds:maxZoom:minZoom:scheme:tiles:url:attribution:)

Initializes the source with all options.

#### Declaration

Swift
public init(
identifier: String,
bounds: [Double],
maxZoom: Double,
minZoom: Double,
scheme: MTTileScheme,
tiles: [URL]? = nil,
url: URL? = nil,
attribution: String? = nil
)

- 

setURL(url:in:completionHandler:)

Sets the url of the source.

Used for updating the source data.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setURL(url: URL, in mapView: MTMapView, completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| url | url to Vector Tile resource. |
| mapView | MTMapView which holds the source. |
| completionHandler | A handler block to execute when function finishes. |

- 

setTiles(tiles:in:completionHandler:)

Sets the tiles of the source.

Used for updating the source data.

#### Declaration

Swift
@MainActor
public func setTiles(
tiles: [URL],
in mapView: MTMapView,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| tiles | list of urls with tile resources. |
| mapView | MTMapView which holds the source. |
| completionHandler | A handler block to execute when function finishes. |

- 

setURL(url:in:)

Asynchronous

Sets the url of the source.

Used for updating the source data.

#### Declaration

Swift
@MainActor
public func setURL(url: URL, in mapView: MTMapView) async

#### Parameters

| url | url to Vector Tile resource. |
| mapView | MTMapView which holds the source. |

- 

setTiles(tiles:in:)

Asynchronous

Sets the tiles of the source.

Used for updating the source data.

#### Declaration

Swift
@MainActor
public func setTiles(tiles: [URL], in mapView: MTMapView) async

#### Parameters

| tiles | list of urls with tile resources. |
| mapView | MTMapView which holds the source. |

- 

addToMap(_:)

Adds source to map DSL style.

Prefer `addSource(_:)` on MTMapView instead.

#### Declaration

Swift
`public func addToMap(_ mapView: MTMapView)`

---

## File: Classes/MTVideoSource.html

---
layout: mobile_sdk
title: "MTVideoSource"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "A video source."
id: mtvideosource
breadcrumb: "Mobile SDK/iOS/Reference/Classes"
---

# MTVideoSource

`public class MTVideoSource : MTSource, @unchecked Sendable`

A video source.

The `urls` value is an array. For each URL in the array, a video element source will be created.
The `coordinates` array contains [longitude, latitude] pairs for the video corners listed in
clockwise order: top left, top right, bottom right, bottom left.

- 

identifier

Unique id of the source.

#### Declaration

Swift
`public var identifier: String`

- 

url

Unused for video sources but required by `MTSource` protocol.
First URL from `urls` may be mirrored here if needed by callers.

#### Declaration

Swift
`public var url: URL?`

- 

urls

URLs to video content in order of preferred format.

#### Declaration

Swift
`public var urls: [URL]`

- 

coordinates

Corners of video specified as `CLLocationCoordinate2D`.
Clockwise order: top-left, top-right, bottom-right, bottom-left.

#### Declaration

Swift
`public var coordinates: [CLLocationCoordinate2D]`

- 

type

Type of the source.

#### Declaration

Swift
`public private(set) var type: MTSourceType { get }`

- 

init(identifier:urls:coordinates:)

Initializes the video source with required values.

#### Declaration

Swift
`public init(identifier: String, urls: [URL], coordinates: [CLLocationCoordinate2D])`

#### Parameters

| identifier | Unique id of the source. |
| urls | URLs to video content in order of preferred format. |
| coordinates | Corners of the video in clockwise order using `CLLocationCoordinate2D`. |

Operations

- 

setCoordinates(_:in:completionHandler:)

Updates the coordinates of the video source.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func setCoordinates(
_ coordinates: [CLLocationCoordinate2D],
in mapView: MTMapView,
completionHandler: ((Result<Void, MTError>) -> Void)? = nil
)

#### Parameters

| coordinates | New corners of the video using `CLLocationCoordinate2D`. |
| mapView | MTMapView which holds the source. |
| completionHandler | A handler block to execute when function finishes. |

Concurrency

- 

setCoordinates(_:in:)

Asynchronous

Updates the coordinates of the video source.

#### Declaration

Swift
@MainActor
public func setCoordinates(_ coordinates: [CLLocationCoordinate2D], in mapView: MTMapView) async

#### Parameters

| coordinates | New corners of the video using `CLLocationCoordinate2D`. |
| mapView | MTMapView which holds the source. |

Playback controls

- 

play(in:completionHandler:)

Starts playback of the video source.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func play(in mapView: MTMapView, completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| mapView | MTMapView which holds the source. |
| completionHandler | A handler block to execute when function finishes. |

- 

pause(in:completionHandler:)

Pauses playback of the video source.

#### Declaration

Swift
@available(iOS, deprecated: 16.0, message: "Prefer the async version for modern concurrency handling")
@MainActor
public func pause(in mapView: MTMapView, completionHandler: ((Result<Void, MTError>) -> Void)? = nil)

#### Parameters

| mapView | MTMapView which holds the source. |
| completionHandler | A handler block to execute when function finishes. |

Playback controls (async)

- 

play(in:)

Asynchronous

Starts playback of the video source (async).

#### Declaration

Swift
@MainActor
public func play(in mapView: MTMapView) async

- 

pause(in:)

Asynchronous

Pauses playback of the video source (async).

#### Declaration

Swift
@MainActor
public func pause(in mapView: MTMapView) async

DSL

- 

addToMap(_:)

Adds source to map DSL style.

Prefer `addSource(_:)` on MTMapView instead.

#### Declaration

Swift
`public func addToMap(_ mapView: MTMapView)`

---

