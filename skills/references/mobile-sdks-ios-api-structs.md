# MapTiler iOS SDK API Reference - Structs

This document is a part of the iOS SDK API reference documentation, covering the `Structs` category.

---

## File: Structs/MTAnimationOptions.html

---
layout: mobile_sdk
title: "MTAnimationOptions"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Provides animation options for navigation functions."
id: mtanimationoptions
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTAnimationOptions

`public struct MTAnimationOptions : Sendable, Codable`

Provides animation options for navigation functions.

- 

duration

The animation’s duration, measured in milliseconds.

#### Declaration

Swift
`public var duration: Double?`

- 

offset

Point of the target center relative to real map container center at the end of animation.

#### Declaration

Swift
`public var offset: MTPoint?`

- 

shouldAnimate

Boolean indicating whether animation will occur.

#### Declaration

Swift
`public var shouldAnimate: Bool?`

- 

isEssential

Boolean indicating whether animation is essential.

#### Declaration

Swift
`public var isEssential: Bool?`

- 

easing

Rate of the change of the animation.

#### Declaration

Swift
`public var easing: MTEasing?`

- 

init(duration:offset:shouldAnimate:isEssential:easing:)

Initializes the options.

#### Declaration

Swift
public init(
duration: Double? = nil,
offset: MTPoint? = nil,
shouldAnimate: Bool? = nil,
isEssential: Bool? = nil,
easing: MTEasing? = nil
)

---

## File: Structs/MTBounds.html

---
layout: mobile_sdk
title: "MTBounds"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Represents rectangular geographic bounds defined by southwest and northeast corners."
id: mtbounds
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTBounds

`public struct MTBounds : Sendable, Codable, Equatable`

Represents rectangular geographic bounds defined by southwest and northeast corners.

- 

southWest

Southwest corner of the bounds.

#### Declaration

Swift
`public var southWest: CLLocationCoordinate2D`

- 

northEast

Northeast corner of the bounds.

#### Declaration

Swift
`public var northEast: CLLocationCoordinate2D`

- 

init(southWest:northEast:)

Creates a new bounds instance.

#### Declaration

Swift
`public init(southWest: CLLocationCoordinate2D, northEast: CLLocationCoordinate2D)`

#### Parameters

| southWest | The southwest corner coordinate. |
| northEast | The northeast corner coordinate. |

- 

init(from:)

#### Declaration

Swift
`public init(from decoder: Decoder) throws`

- 

encode(to:)

#### Declaration

Swift
`public func encode(to encoder: Encoder) throws`

- 

contains(_:)

Checks if the bounds contain the coordinate.

#### Declaration

Swift
`public func contains(_ coordinate: CLLocationCoordinate2D) -> Bool`

#### Parameters

| coordinate | The coordinate to check. |

#### Return Value

True if the coordinate is inside the bounds.

---

## File: Structs/MTCameraOptions.html

---
layout: mobile_sdk
title: "MTCameraOptions"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Options for controlling the desired location, zoom, bearing, and pitch of the camera."
id: mtcameraoptions
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTCameraOptions

`public struct MTCameraOptions : Sendable`
`extension MTCameraOptions: Codable`

Options for controlling the desired location, zoom, bearing, and pitch of the camera.

- 

center

Geographical center of the map.

#### Declaration

Swift
`public var center: CLLocationCoordinate2D?`

- 

zoom

Zoom level of the map.

#### Declaration

Swift
`public var zoom: Double?`

- 

bearing

The bearing of the map, measured in degrees counter-clockwise from north.

#### Declaration

Swift
`public var bearing: Double?`

- 

pitch

The pitch (tilt) of the map, measured in degrees away from the plane of the screen (0-85).

#### Declaration

Swift
`public var pitch: Double?`

- 

init(center:zoom:bearing:pitch:)

Initializes options.

#### Declaration

Swift
public init(
center: CLLocationCoordinate2D? = nil,
zoom: Double? = nil,
bearing: Double? = nil,
pitch: Double? = nil
)

- 

encode(to:)

#### Declaration

Swift
`public func encode(to encoder: Encoder) throws`

---

## File: Structs/MTColor.html

---
layout: mobile_sdk
title: "MTColor"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Color wrapper."
id: mtcolor
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTColor

`public struct MTColor : Sendable, Codable, Equatable`

Color wrapper.

- 

cgColor

CGColor representation of the MTColor.

#### Declaration

Swift
`public var cgColor: CGColor? { get }`

- 

init(color:)

Initializes the MTColor with CGColor

#### Declaration

Swift
`public init(color: CGColor)`

- 

init(hex:)

Initializes the `MTColor` with a hex string (e.g., “#RRGGBB” or “#RRGGBBAA”).

#### Declaration

Swift
`public init(hex: String)`

---

## File: Structs/MTColorRampArrayStop.html

---
layout: mobile_sdk
title: "MTColorRampArrayStop"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Array-based stop definition for fromArrayDefinition."
id: mtcolorramparraystop
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTColorRampArrayStop

`public struct MTColorRampArrayStop : Sendable, Codable`

Array-based stop definition for `fromArrayDefinition`.

- 

value

Undocumented

#### Declaration

Swift
`public var value: Double`

- 

color

Undocumented

#### Declaration

Swift
`public var color: MTRGBAColor`

- 

init(value:color:)

Undocumented

#### Declaration

Swift
`public init(value: Double, color: MTRGBAColor)`

- 

encode(to:)

#### Declaration

Swift
`public func encode(to encoder: Encoder) throws`

---

## File: Structs/MTColorRampBounds.html

---
layout: mobile_sdk
title: "MTColorRampBounds"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Bounds of a color ramp."
id: mtcolorrampbounds
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTColorRampBounds

`public struct MTColorRampBounds : Sendable, Codable`

Bounds of a color ramp.

- 

min

Undocumented

#### Declaration

Swift
`public let min: Double`

- 

max

Undocumented

#### Declaration

Swift
`public let max: Double`

---

## File: Structs/MTColorRampCanvasStripOptions.html

---
layout: mobile_sdk
title: "MTColorRampCanvasStripOptions"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Options for rendering the ramp to a canvas strip."
id: mtcolorrampcanvasstripoptions
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTColorRampCanvasStripOptions

`public struct MTColorRampCanvasStripOptions : Sendable, Codable`

Options for rendering the ramp to a canvas strip.

- 

horizontal

Undocumented

#### Declaration

Swift
`public var horizontal: Bool?`

- 

size

Undocumented

#### Declaration

Swift
`public var size: Int?`

- 

smooth

Undocumented

#### Declaration

Swift
`public var smooth: Bool?`

- 

init(horizontal:size:smooth:)

Undocumented

#### Declaration

Swift
`public init(horizontal: Bool? = nil, size: Int? = nil, smooth: Bool? = nil)`

---

## File: Structs/MTColorRampOptions.html

---
layout: mobile_sdk
title: "MTColorRampOptions"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Options used when instantiating a color ramp."
id: mtcolorrampoptions
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTColorRampOptions

`public struct MTColorRampOptions : Sendable, Codable`

Options used when instantiating a color ramp.

- 

min

Undocumented

#### Declaration

Swift
`public var min: Double?`

- 

max

Undocumented

#### Declaration

Swift
`public var max: Double?`

- 

stops

Undocumented

#### Declaration

Swift
`public var stops: [MTColorRampStop]`

- 

init(min:max:stops:)

Undocumented

#### Declaration

Swift
`public init(min: Double? = nil, max: Double? = nil, stops: [MTColorRampStop])`

---

## File: Structs/MTColorRampStop.html

---
layout: mobile_sdk
title: "MTColorRampStop"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "A stop describing the value and color to apply."
id: mtcolorrampstop
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTColorRampStop

`public struct MTColorRampStop : Sendable, Codable`

A stop describing the value and color to apply.

- 

value

Undocumented

#### Declaration

Swift
`public var value: Double`

- 

color

Undocumented

#### Declaration

Swift
`public var color: MTRGBAColor`

- 

init(value:color:)

Undocumented

#### Declaration

Swift
`public init(value: Double, color: MTRGBAColor)`

---

## File: Structs/MTColorValue.html

---
layout: mobile_sdk
title: "MTColorValue"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Encodes a color to a hex string when converted to JSON.
Accepts either a hex color string (e.g. “#RRGGBB”) or a UIColor."
id: mtcolorvalue
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTColorValue

`public struct MTColorValue : Codable, Sendable`

Encodes a color to a hex string when converted to JSON.
Accepts either a hex color string (e.g. “#RRGGBB”) or a UIColor.

- 

raw

Undocumented

#### Declaration

Swift
`public let raw: String`

- 

init(_:)

Undocumented

#### Declaration

Swift
`public init(_ hexColor: String)`

- 

init(_:)

Undocumented

#### Declaration

Swift
`public init(_ color: UIColor)`

- 

init(from:)

#### Declaration

Swift
`public init(from decoder: any Decoder) throws`

- 

encode(to:)

#### Declaration

Swift
`public func encode(to encoder: any Encoder) throws`

---

## File: Structs/MTData.html

---
layout: mobile_sdk
title: "MTData"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Object sent together with MTEvent."
id: mtdata
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTData

`public struct MTData : Codable`

Object sent together with MTEvent.

- 

id

Unique id.

#### Declaration

Swift
`public var id: String?`

- 

coordinate

Coordinate of the event tap.

#### Declaration

Swift
`public var coordinate: CLLocationCoordinate2D?`

- 

point

Point of the event tap.

#### Declaration

Swift
`public var point: MTPoint?`

- 

dataType

Type of the event.

#### Declaration

Swift
`public var dataType: String?`

- 

isSourceLoaded

Boolean indicating if source is fully  loaded.

#### Declaration

Swift
`public var isSourceLoaded: Bool?`

- 

source

Source data.

#### Declaration

Swift
`public var source: MTSourceData?`

- 

sourceDataType

Type of the source data.

#### Declaration

Swift
`public var sourceDataType: String?`

- 

init(from:)

Initialiaes the data from decoder.

#### Declaration

Swift
`public init(from decoder: any Decoder) throws`

---

## File: Structs/MTDoubleTapZoomInGesture.html

---
layout: mobile_sdk
title: "MTDoubleTapZoomInGesture"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Handles zooming in the map with double tap."
id: mtdoubletapzoomingesture
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTDoubleTapZoomInGesture

@MainActor
public struct MTDoubleTapZoomInGesture : MTGesture

Handles zooming in the map with double tap.

- 

type

Type of the gesture.

#### Declaration

Swift
@MainActor
public var type: MTGestureType

- 

disable()

Asynchronous

Disables the gesture on the map.

#### Declaration

Swift
@MainActor
public func disable() async

- 

enable()

Asynchronous

#### Declaration

Swift
@MainActor
public func enable() async

---

## File: Structs/MTDragPanGesture.html

---
layout: mobile_sdk
title: "MTDragPanGesture"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Handles panning the map by dragging."
id: mtdragpangesture
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTDragPanGesture

@MainActor
public struct MTDragPanGesture : MTGesture

Handles panning the map by dragging.

- 

type

Type of the gesture.

#### Declaration

Swift
@MainActor
public var type: MTGestureType

- 

disable()

Asynchronous

Disables the gesture on the map.

#### Declaration

Swift
@MainActor
public func disable() async

- 

enable()

Asynchronous

Enables the gesture on the map.

#### Declaration

Swift
@MainActor
public func enable() async

- 

enable(with:)

Asynchronous

Enables the gesture on the map with options.

#### Declaration

Swift
@MainActor
public func enable(with options: MTDragPanOptions) async

#### Parameters

| options | Drag and pan options. |

---

## File: Structs/MTDragPanOptions.html

---
layout: mobile_sdk
title: "MTDragPanOptions"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Options for drag and pan gesstures."
id: mtdragpanoptions
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTDragPanOptions

`public struct MTDragPanOptions : Sendable, Codable`

Options for drag and pan gesstures.

- 

linearity

Factor used to scale the drag velocity.

Note
Default: 0

#### Declaration

Swift
`public var linearity: Double?`

- 

maxSpeed

The maximum value of the drag velocity.

Note
Default: 1400

#### Declaration

Swift
`public var maxSpeed: Double?`

- 

deceleration

The rate at which the speed reduces after the pan ends.

Note
Default: 2500

#### Declaration

Swift
`public var deceleration: Double?`

- 

init(linearity:maxSpeed:deceleration:)

Initializes the options with linearity, maxSpeed and deceleration.

#### Declaration

Swift
`public init(linearity: Double? = nil, maxSpeed: Double? = nil, deceleration: Double? = nil)`

---

## File: Structs/MTException.html

---
layout: mobile_sdk
title: "MTException"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Represents body of the MTError exception."
id: mtexception
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTException

`public struct MTException : Sendable`

Represents body of the MTError exception.

- 

code

Exception code.

#### Declaration

Swift
`public var code: Int`

- 

reason

Explanation of the exception.

#### Declaration

Swift
`public var reason: String`

---

## File: Structs/MTFitBoundsOptions.html

---
layout: mobile_sdk
title: "MTFitBoundsOptions"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Options that configure how the map fits to a set of bounds."
id: mtfitboundsoptions
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTFitBoundsOptions

`public struct MTFitBoundsOptions : Sendable, Codable`

Options that configure how the map fits to a set of bounds.

- 

padding

Padding to apply on each side of the viewport when fitting the bounds.

#### Declaration

Swift
`public var padding: MTFitBoundsPadding?`

- 

maxZoom

The maximum zoom level that the fit operation can produce.

#### Declaration

Swift
`public var maxZoom: Double?`

- 

linear

Enables linear interpolation instead of the default easing.

#### Declaration

Swift
`public var linear: Bool?`

- 

bearing

Final bearing for the camera after the fit completes.

#### Declaration

Swift
`public var bearing: Double?`

- 

pitch

Final pitch for the camera after the fit completes.

#### Declaration

Swift
`public var pitch: Double?`

- 

animationOptions

Additional animation configuration.

#### Declaration

Swift
`public var animationOptions: MTAnimationOptions?`

- 

init(padding:maxZoom:linear:bearing:pitch:animationOptions:)

Creates a new set of fit bounds options.

#### Declaration

Swift
public init(
padding: MTFitBoundsPadding? = nil,
maxZoom: Double? = nil,
linear: Bool? = nil,
bearing: Double? = nil,
pitch: Double? = nil,
animationOptions: MTAnimationOptions? = nil
)

#### Parameters

| padding | Padding to apply around the fitted bounds. |
| maxZoom | Upper zoom limit for the resulting camera. |
| linear | Boolean indicating whether to animate linearly. |
| bearing | Target bearing after the fit completes. |
| pitch | Target pitch after the fit completes. |
| animationOptions | Extra animation parameters. |

- 

init(from:)

#### Declaration

Swift
`public init(from decoder: any Decoder) throws`

- 

encode(to:)

#### Declaration

Swift
`public func encode(to encoder: Encoder) throws`

---

## File: Structs/MTFlyToOptions.html

---
layout: mobile_sdk
title: "MTFlyToOptions"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Options describing the destination and animation of the flyTo transition."
id: mtflytooptions
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTFlyToOptions

`public struct MTFlyToOptions : Sendable, Codable`

Options describing the destination and animation of the flyTo transition.

- 

curve

The zooming “curve” that will occur along the flight path.

#### Declaration

Swift
`public var curve: Double?`

- 

minZoom

The zero-based zoom level at the peak of the flight path.

#### Declaration

Swift
`public var minZoom: Double?`

- 

speed

The average speed of the animation defined in relation to curve.

#### Declaration

Swift
`public var speed: Double?`

- 

screenSpeed

The average speed of the animation measured in screenfuls per second, assuming a linear timing curve.

#### Declaration

Swift
`public var screenSpeed: Double?`

- 

maxDuration

The animation’s maximum duration, measured in milliseconds.

#### Declaration

Swift
`public var maxDuration: Double?`

- 

init(curve:minZoom:speed:screenSpeed:maxDuration:)

Initializes the options.

#### Declaration

Swift
public init(
curve: Double? = nil,
minZoom: Double? = nil,
speed: Double? = nil,
screenSpeed: Double? = nil,
maxDuration: Double? = nil
)

---

## File: Structs/MTHalo.html

---
layout: mobile_sdk
title: "MTHalo"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Configuration for the atmospheric glow (halo)."
id: mthalo
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTHalo

`public struct MTHalo : Sendable, Codable`

Configuration for the atmospheric glow (halo).

- 

scale

Controls the overall halo size.

#### Declaration

Swift
`public var scale: Double?`

- 

stops

Radial gradient definition expressed as ordered stops.

#### Declaration

Swift
`public var stops: [MTHaloStop]?`

- 

init(scale:stops:)

Undocumented

#### Declaration

Swift
`public init(scale: Double? = nil, stops: [MTHaloStop]? = nil)`

---

## File: Structs/MTHaloStop.html

---
layout: mobile_sdk
title: "MTHaloStop"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "One stop in the halo radial gradient: position in [0,1] and color."
id: mthalostop
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTHaloStop

`public struct MTHaloStop : Sendable, Codable`

One stop in the halo radial gradient: position in [0,1] and color.

- 

position

Undocumented

#### Declaration

Swift
`public var position: Double`

- 

color

Undocumented

#### Declaration

Swift
`public var color: MTColor`

- 

init(position:color:)

Undocumented

#### Declaration

Swift
`public init(position: Double, color: MTColor)`

- 

init(from:)

#### Declaration

Swift
`public init(from decoder: any Decoder) throws`

- 

encode(to:)

#### Declaration

Swift
`public func encode(to encoder: Encoder) throws`

---

## File: Structs/MTHeatmapLayerOptions.html

---
layout: mobile_sdk
title: "MTHeatmapLayerOptions"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Options for building a heatmap visualization layer through the helper."
id: mtheatmaplayeroptions
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTHeatmapLayerOptions

`public struct MTHeatmapLayerOptions : Codable, Sendable`

Options for building a heatmap visualization layer through the helper.

- 

data

Undocumented

#### Declaration

Swift
`public var data: String`

- 

layerId

Undocumented

#### Declaration

Swift
`public var layerId: String?`

- 

sourceId

Undocumented

#### Declaration

Swift
`public var sourceId: String?`

- 

beforeId

Undocumented

#### Declaration

Swift
`public var beforeId: String?`

- 

minzoom

Undocumented

#### Declaration

Swift
`public var minzoom: Double?`

- 

maxzoom

Undocumented

#### Declaration

Swift
`public var maxzoom: Double?`

- 

property

Undocumented

#### Declaration

Swift
`public var property: String?`

- 

weight

Undocumented

#### Declaration

Swift
`public var weight: MTNumberOrPropertyValues?`

- 

radius

Undocumented

#### Declaration

Swift
`public var radius: MTRadiusOption?`

- 

opacity

Undocumented

#### Declaration

Swift
`public var opacity: MTNumberOrZoomNumberValues?`

- 

intensity

Undocumented

#### Declaration

Swift
`public var intensity: MTNumberOrZoomNumberValues?`

- 

zoomCompensation

Undocumented

#### Declaration

Swift
`public var zoomCompensation: Bool?`

- 

init(data:layerId:sourceId:beforeId:minzoom:maxzoom:property:weight:radius:opacity:intensity:zoomCompensation:)

Undocumented

#### Declaration

Swift
public init(
data: String,
layerId: String? = nil,
sourceId: String? = nil,
beforeId: String? = nil,
minzoom: Double? = nil,
maxzoom: Double? = nil,
property: String? = nil,
weight: Double? = nil,
radius: Double? = nil,
opacity: Double? = nil,
intensity: Double? = nil,
zoomCompensation: Bool? = nil
)

- 

init(data:layerId:sourceId:beforeId:minzoom:maxzoom:property:weight:radius:opacity:intensity:zoomCompensation:)

Convenience initializer accepting ramp-capable types.

#### Declaration

Swift
public init(
data: String,
layerId: String? = nil,
sourceId: String? = nil,
beforeId: String? = nil,
minzoom: Double? = nil,
maxzoom: Double? = nil,
property: String? = nil,
weight: MTNumberOrPropertyValues? = nil,
radius: MTRadiusOption? = nil,
opacity: MTNumberOrZoomNumberValues? = nil,
intensity: MTNumberOrZoomNumberValues? = nil,
zoomCompensation: Bool? = nil
)

---

## File: Structs/MTHelperPropertyValue.html

---
layout: mobile_sdk
title: "MTHelperPropertyValue"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "A single mapping from a property value to an associated numeric value."
id: mthelperpropertyvalue
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTHelperPropertyValue

`public struct MTHelperPropertyValue : Codable, Sendable`

A single mapping from a property value to an associated numeric value.

- 

propertyValue

Value of the property (input)

#### Declaration

Swift
`public var propertyValue: Double`

- 

value

Value to associate it with (output)

#### Declaration

Swift
`public var value: Double`

- 

init(propertyValue:value:)

Undocumented

#### Declaration

Swift
`public init(propertyValue: Double, value: Double)`

---

## File: Structs/MTLight.html

---
layout: mobile_sdk
title: "MTLight"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "A style’s light property provides a global light source for that style."
id: mtlight
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTLight

`public struct MTLight : Sendable, Codable`

A style’s light property provides a global light source for that style.

- 

init(anchor:color:intensity:position:)

Undocumented

#### Declaration

Swift
public init(
anchor: MTLightAnchor? = nil,
color: MTColor? = nil,
intensity: Double? = nil,
position: [Double]? = nil
)

- 

init(from:)

#### Declaration

Swift
`public init(from decoder: any Decoder) throws`

- 

encode(to:)

#### Declaration

Swift
`public func encode(to encoder: Encoder) throws`

---

## File: Structs/MTLog.html

---
layout: mobile_sdk
title: "MTLog"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Log object used with MTLogger."
id: mtlog
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTLog

`public struct MTLog`

Log object used with MTLogger.

- 

message

Log message.

#### Declaration

Swift
`public var message: String`

- 

type

Type of the log.

#### Declaration

Swift
`public var type: MTLogType`

- 

printLog()

Prints the log to the console.

#### Declaration

Swift
`public func printLog()`

---

## File: Structs/MTMapContentBuilder.html

---
layout: mobile_sdk
title: "MTMapContentBuilder"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Map view content builder."
id: mtmapcontentbuilder
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTMapContentBuilder

@resultBuilder
public struct MTMapContentBuilder

Map view content builder.

- 

buildBlock(_:)

Undocumented

#### Declaration

Swift
`public static func buildBlock(_ components: MTMapViewContent...) -> [MTMapViewContent]`

- 

buildOptionals(_:)

Undocumented

#### Declaration

Swift
`public static func buildOptionals(_ components: [MTMapViewContent]?) -> [MTMapViewContent]`

- 

buildEither(first:)

Undocumented

#### Declaration

Swift
`public static func buildEither(first components: [MTMapViewContent]) -> [MTMapViewContent]`

- 

buildEither(second:)

Undocumented

#### Declaration

Swift
`public static func buildEither(second components: [MTMapViewContent]) -> [MTMapViewContent]`

- 

buildArray(_:)

Undocumented

#### Declaration

Swift
`public static func buildArray(_ components: [[MTMapViewContent]]) -> [any MTMapViewContent]`

---

## File: Structs/MTMapOptions.html

---
layout: mobile_sdk
title: "MTMapOptions"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Parameters of the map object."
id: mtmapoptions
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTMapOptions

`public struct MTMapOptions : Sendable`
`extension MTMapOptions: Codable`

Parameters of the map object.

- 

language

The language of the map.

This applies only for the map instance, supersedes the primaryLanguage from config.

#### Declaration

Swift
`public private(set) var language: MTLanguage? { get }`

- 

center

The geographical centerpoint of the map.

If center is not specified, SDK will look for it in the map style object.
If it is not specified in the style, it will default to (latitude: 0.0, longitude: 0.0).

#### Declaration

Swift
`public private(set) var center: CLLocationCoordinate2D? { get }`

- 

bounds

Geographic bounds that should be visible by default when the map loads.

#### Declaration

Swift
`public private(set) var bounds: MTBounds? { get }`

- 

projection

Projection type of the map object.

This will overwrite the projection property from the style (if any).

#### Declaration

Swift
`public private(set) var projection: MTProjectionType? { get }`

- 

zoom

The zoom level of the map.

If zoom is not specified, SDK will look for it in the map style object.
If it is not specified in the style, it will default to 0.0.

#### Declaration

Swift
`public private(set) var zoom: Double? { get }`

- 

maxZoom

The maximum zoom level of the map (0-24).

#### Declaration

Swift
`public private(set) var maxZoom: Double? { get }`

- 

minZoom

The minimum zoom level of the map (0-24).

#### Declaration

Swift
`public private(set) var minZoom: Double? { get }`

- 

maxBounds

Maximum geographical bounds that the user can pan the map to.

#### Declaration

Swift
`public private(set) var maxBounds: MTBounds? { get }`

- 

bearing

The bearing of the map, measured in degrees counter-clockwise from north.

If bearing is not specified, SDK will look for it in the map style object.
If it is not specified in the style, it will default to 0.0.

#### Declaration

Swift
`public private(set) var bearing: Double? { get }`

- 

bearingSnap

The threshold, measured in degrees, that determines when the map’s bearing will snap to north.

#### Declaration

Swift
`public private(set) var bearingSnap: Double? { get }`

- 

pitch

The pitch (tilt) of the map, measured in degrees away from the plane of the screen (0-85).

If pitch is not specified, SDK will look for it in the map style object.
If it is not specified in the style, it will default to 0.0.

#### Declaration

Swift
`public private(set) var pitch: Double? { get }`

- 

maxPitch

The maximum pitch of the map (0-180).

#### Declaration

Swift
`public private(set) var maxPitch: Double? { get }`

- 

minPitch

The minimum pitch of the map (0-85).

#### Declaration

Swift
`public private(set) var minPitch: Double? { get }`

- 

roll

The roll angle of the map, measured in degrees counter-clockwise about the camera boresight.

If roll is not specified, SDK will look for it in the map style object.
If it is not specified in the style, it will default to 0.0.

#### Declaration

Swift
`public private(set) var roll: Double? { get }`

- 

rollIsEnabled

Boolean indicating whether the map’s roll control with “drag to rotate” interaction is enabled.

#### Declaration

Swift
`public private(set) var rollIsEnabled: Bool? { get }`

- 

elevation

The elevation of the geographical centerpoint of the map, in meters above sea level.

If elevation is not specified, SDK will look for it in the map style object.
If it is not specified in the style, it will default to 0.0.

#### Declaration

Swift
`public private(set) var elevation: Double? { get }`

- 

terrainIsEnabled

Boolean indicating whether 3D terrain is enabled.

#### Declaration

Swift
`public private(set) var terrainIsEnabled: Bool? { get }`

- 

terrainExaggeration

3D terrain exaggeration factor.

#### Declaration

Swift
`public private(set) var terrainExaggeration: Double? { get }`

- 

cancelPendingTileRequestsWhileZooming

Determines whether to cancel, or retain, tiles from the current viewport which are still loading
but which belong to a farther (smaller) zoom level than the current one.

If true, when zooming in, tiles which didn’t manage to load for previous zoom levels will become canceled.
This might save some computing resources for slower devices, but the map details might appear more
abruptly at the end of the zoom. If false, when zooming in, the previous zoom level(s) tiles will progressively
appear, giving a smoother map details experience. However, more tiles will be rendered
in a short period of time.

#### Declaration

Swift
`public private(set) var cancelPendingTileRequestsWhileZooming: Bool? { get }`

- 

isCenterClampedToGround

Boolen indicating whether center is clamped to the ground.

If true, the elevation of the center point will automatically be set to the terrain elevation
(or zero if terrain is not enabled). If false, the elevation of the center point will default
to sea level and will not automatically update.
Needs to be set to false to keep the camera above ground when pitch > 90 degrees.

#### Declaration

Swift
`public private(set) var isCenterClampedToGround: Bool? { get }`

- 

shouldCollectResourceTiming

Boolean indicating whether Resource Timing API information will be collected.

#### Declaration

Swift
`public private(set) var shouldCollectResourceTiming: Bool? { get }`

- 

crossSourceCollisionsAreEnabled

Boolean indicating whether cross source collisions are enabled.

If true, symbols from multiple sources can collide with each other during collision detection.
If false, collision detection is run separately for the symbols in each source.

#### Declaration

Swift
`public private(set) var crossSourceCollisionsAreEnabled: Bool? { get }`

- 

fadeDuration

The duration of the fade-in/fade-out animation for label collisions, in milliseconds.

This setting affects all symbol layers. This setting does not affect the duration of runtime
styling transitions or raster tile cross-fading.

#### Declaration

Swift
`public private(set) var fadeDuration: Double? { get }`

- 

pixelRatio

Pixel ratio to use when rendering the map.

Defaults to the device pixel ratio if not specified.

#### Declaration

Swift
`public private(set) var pixelRatio: Double? { get }`

- 

isInteractionEnabled

Undocumented

#### Declaration

Swift
`public private(set) var isInteractionEnabled: Bool? { get }`

- 

logoPosition

A value representing the position of the MapTiler wordmark on the map.

#### Declaration

Swift
`public private(set) var logoPosition: MTMapCorner? { get }`

- 

maptilerLogoIsVisible

Boolean indicating whether MapTiler logo is visible on the map.

If true, the MapTiler logo will be shown. false will only work on premium accounts

#### Declaration

Swift
`public private(set) var maptilerLogoIsVisible: Bool? { get }`

- 

maxTileCacheSize

The maximum number of tiles stored in the tile cache for a given source.

If omitted, the cache will be dynamically sized based on the current viewport.

#### Declaration

Swift
`public private(set) var maxTileCacheSize: Double? { get }`

- 

maxTileCacheZoomLevels

The maximum number of zoom levels for which to store tiles for a given source.

Tile cache dynamic size is calculated by multiplying maxTileCacheZoomLevels
with the approximate number of tiles in the viewport for a given source.

#### Declaration

Swift
`public private(set) var maxTileCacheZoomLevels: Double? { get }`

- 

shouldPitchWithRotate

Boolean indicating whether the map’s pitch control
with drag to rotate interaction will be disabled.

#### Declaration

Swift
`public private(set) var shouldPitchWithRotate: Bool? { get }`

- 

shouldRefreshExpiredTiles

Boolean indicating whether the map won’t attempt to re-request tiles once they expire.

#### Declaration

Swift
`public private(set) var shouldRefreshExpiredTiles: Bool? { get }`

- 

shouldRenderWorldCopies

Boolean indicating whether multiple copies of the world will be rendered side by side
beyond -180 and 180 degrees longitude.

#### Declaration

Swift
`public private(set) var shouldRenderWorldCopies: Bool? { get }`

- 

shouldDragToPitch

Boolean indicating whether the drag to pitch" nteraction is enabled.

#### Declaration

Swift
`public private(set) var shouldDragToPitch: Bool? { get }`

- 

shouldPinchToRotateAndZoom

Boolean indicating whether the pinch to rotate and zoom interaction is enabled.

#### Declaration

Swift
`public private(set) var shouldPinchToRotateAndZoom: Bool? { get }`

- 

doubleTapShouldZoom

Boolean indicating whether the double tap to zoom interaction is enabled.

#### Declaration

Swift
`public private(set) var doubleTapShouldZoom: Bool? { get }`

- 

dragPanIsEnabled

Boolean indicating whether the drag to pan interaction is enabled.

#### Declaration

Swift
`public private(set) var dragPanIsEnabled: Bool? { get }`

- 

dragRotateIsEnabled

Boolean indicating whether the drag to rotate interaction is enabled.

#### Declaration

Swift
`public private(set) var dragRotateIsEnabled: Bool? { get }`

- 

shouldValidateStyle

Boolean indicating whether style should be validated.

Useful in production environment.

#### Declaration

Swift
`public private(set) var shouldValidateStyle: Bool? { get }`

- 

minimapIsVisible

Boolean indicating whether minimap control is added directly to the map.

#### Declaration

Swift
`public private(set) var minimapIsVisible: Bool? { get }`

- 

attributionControlIsVisible

Boolean indicating whether attribution control is added directly to the map.

#### Declaration

Swift
`public private(set) var attributionControlIsVisible: Bool? { get }`

- 

geolocateControlIsVisible

Boolean indicating whether geolocate control is added directly to the map.

#### Declaration

Swift
`public private(set) var geolocateControlIsVisible: Bool? { get }`

- 

navigationControlIsVisible

Boolean indicating whether navigation control is added directly to the map.

#### Declaration

Swift
`public private(set) var navigationControlIsVisible: Bool? { get }`

- 

projectionControlIsVisible

Boolean indicating whether projection control is added directly to the map.

#### Declaration

Swift
`public private(set) var projectionControlIsVisible: Bool? { get }`

- 

scaleControlIsVisible

Boolean indicating whether scale control is added directly to the map.

#### Declaration

Swift
`public private(set) var scaleControlIsVisible: Bool? { get }`

- 

terrainControlIsVisible

Boolean indicating whether terrain control is added directly to the map.

#### Declaration

Swift
`public private(set) var terrainControlIsVisible: Bool? { get }`

- 

isSessionLogicEnabled

Boolean indicating whether session logic is enabled.

This allows MapTiler to enable “session based billing”.

Note
Defaults to true.

See also
`https://docs.maptiler.com/guides/maps-apis/maps-platform/what-is-map-session-in-maptiler-cloud/`

#### Declaration

Swift
`public private(set) var isSessionLogicEnabled: Bool { get }`

- 

space

Space background configuration for globe (cubemap/spacebox).

#### Declaration

Swift
`public private(set) var space: MTSpaceOption? { get }`

- 

halo

Atmospheric glow (halo) configuration for globe.

#### Declaration

Swift
`public private(set) var halo: MTHaloOption? { get }`

- 

eventLevel

Controls which map events are sent from the map object.

#### Declaration

Swift
`public private(set) var eventLevel: MTEventLevel { get }`

- 

highFrequencyEventThrottleMs

Optional throttle in milliseconds applied to high-frequency events when [eventLevel] is
[MTEventLevel.all] or [MTEventLevel.cameraOnly]. A value of 0 disables throttling.

#### Declaration

Swift
`public private(set) var highFrequencyEventThrottleMs: Int? { get }`

- 

init(center:zoom:)

Initializes the map options with center and zoom.

#### Declaration

Swift
`public init(center: CLLocationCoordinate2D?, zoom: Double?)`

- 

init(center:zoom:terrainIsEnabled:terrainExaggeration:)

Initializes the map options with center, zoom and terrain.

#### Declaration

Swift
`public init(center: CLLocationCoordinate2D?, zoom: Double?, terrainIsEnabled: Bool?, terrainExaggeration: Double?)`

- 

init(center:zoom:projection:)

Initializes the map options with center, zoom and projection.

#### Declaration

Swift
`public init(center: CLLocationCoordinate2D?, zoom: Double?, projection: MTProjectionType?)`

- 

init(center:zoom:bearing:pitch:)

Initializes the map options with center, zoom, bearing, and pitch.

#### Declaration

Swift
`public init(center: CLLocationCoordinate2D?, zoom: Double?, bearing: Double?, pitch: Double?)`

- 

init(language:center:bounds:projection:zoom:maxZoom:minZoom:maxBounds:bearing:bearingSnap:pitch:maxPitch:minPitch:roll:rollIsEnabled:elevation:terrainIsEnabled:terrainExaggeration:cancelPendingTileRequestsWhileZooming:isCenterClampedToGround:shouldCollectResourceTiming:crossSourceCollisionsAreEnabled:fadeDuration:pixelRatio:isInteractionEnabled:logoPosition:maptilerLogoIsVisible:maxTileCacheSize:maxTileCacheZoomLevels:shouldPitchWithRotate:shouldRefreshExpiredTiles:shouldRenderWorldCopies:shouldDragToPitch:shouldPinchToRotateAndZoom:doubleTapShouldZoom:dragPanIsEnabled:dragRotateIsEnabled:shouldValidateStyle:minimapIsVisible:attributionControlIsVisible:geolocateControlIsVisible:navigationControlIsVisible:projectionControlIsVisible:scaleControlIsVisible:terrainControlIsVisible:isSessionLogicEnabled:space:halo:eventLevel:highFrequencyEventThrottleMs:)

Initializes the map options.

#### Declaration

Swift
public init(
language: MTLanguage? = nil,
center: CLLocationCoordinate2D? = nil,
bounds: MTBounds? = nil,
projection: MTProjectionType? = nil,
zoom: Double? = nil,
maxZoom: Double? = nil,
minZoom: Double? = nil,
maxBounds: MTBounds? = nil,
bearing: Double? = nil,
bearingSnap: Double? = nil,
pitch: Double? = nil,
maxPitch: Double? = nil,
minPitch: Double? = nil,
roll: Double? = nil,
rollIsEnabled: Bool? = nil,
elevation: Double? = nil,
terrainIsEnabled: Bool? = nil,
terrainExaggeration: Double? = nil,
cancelPendingTileRequestsWhileZooming: Bool? = nil,
isCenterClampedToGround: Bool? = nil,
shouldCollectResourceTiming: Bool? = nil,
crossSourceCollisionsAreEnabled: Bool? = nil,
fadeDuration: Double? = nil,
pixelRatio: Double? = nil,
isInteractionEnabled: Bool? = nil,
logoPosition: MTMapCorner? = nil,
maptilerLogoIsVisible: Bool? = nil,
maxTileCacheSize: Double? = nil,
maxTileCacheZoomLevels: Double? = nil,
shouldPitchWithRotate: Bool? = nil,
shouldRefreshExpiredTiles: Bool? = nil,
shouldRenderWorldCopies: Bool? = nil,
shouldDragToPitch: Bool? = nil,
shouldPinchToRotateAndZoom: Bool? = nil,
doubleTapShouldZoom: Bool? = nil,
dragPanIsEnabled: Bool? = nil,
dragRotateIsEnabled: Bool? = nil,
shouldValidateStyle: Bool? = nil,
minimapIsVisible: Bool? = false,
attributionControlIsVisible: Bool? = nil,
geolocateControlIsVisible: Bool? = false,
navigationControlIsVisible: Bool? = false,
projectionControlIsVisible: Bool? = false,
scaleControlIsVisible: Bool? = false,
terrainControlIsVisible: Bool? = false,
isSessionLogicEnabled: Bool = true,
space: MTSpaceOption? = nil,
halo: MTHaloOption? = nil,
eventLevel: MTEventLevel = .cameraOnly,
highFrequencyEventThrottleMs: Int? = 10
)

- 

withLeanPerformanceDefaults()

Applies the lean performance preset over this instance, returning a new options object.

#### Declaration

Swift
`func withLeanPerformanceDefaults() -> MTMapOptions`

- 

withBalancedPerformanceDefaults()

Returns a new [MTMapOptions] with balanced performance defaults applied over this instance.

#### Declaration

Swift
`func withBalancedPerformanceDefaults() -> MTMapOptions`

- 

withHighFidelityDefaults()

Returns a new [MTMapOptions] with high-fidelity defaults applied over this instance.

#### Declaration

Swift
`func withHighFidelityDefaults() -> MTMapOptions`

---

## File: Structs/MTMapViewContainer.html

---
layout: mobile_sdk
title: "MTMapViewContainer"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Declarative Map view for use in SwiftUI"
id: mtmapviewcontainer
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTMapViewContainer

@MainActor
public struct MTMapViewContainer : View

Declarative Map view for use in SwiftUI

- 

map

Undocumented

#### Declaration

Swift
@MainActor
public var map: MTMapView

- 

init(map:content:)

Undocumented

#### Declaration

Swift
@MainActor
public init(map: MTMapView, @MTMapContentBuilder content: () -> [MTMapViewContent])

- 

body

#### Declaration

Swift
@MainActor
public var body: some View { get }

- 

referenceStyle(_:)

Undocumented

#### Declaration

Swift
@MainActor
public func referenceStyle(_ style: MTMapReferenceStyle) -> MTMapViewContainer

- 

styleVariant(_:)

Undocumented

#### Declaration

Swift
@MainActor
public func styleVariant(_ variant: MTMapStyleVariant?) -> MTMapViewContainer

- 

didTriggerEvent(_:)

Undocumented

#### Declaration

Swift
@MainActor
public func didTriggerEvent(_ closure: @escaping (_ event: MTEvent, _ data: MTData?) -> Void) -> MTMapViewContainer

- 

didInitialize(_:)

Undocumented

#### Declaration

Swift
@MainActor
public func didInitialize(_ closure: @escaping () -> Void) -> MTMapViewContainer

- 

didUpdateLocation(_:)

Undocumented

#### Declaration

Swift
@MainActor
public func didUpdateLocation(_ closure: @escaping (_ location: CLLocation) -> Void) -> MTMapViewContainer

---

## File: Structs/MTPaddingOptions.html

---
layout: mobile_sdk
title: "MTPaddingOptions"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Options for setting padding on calls to map methods."
id: mtpaddingoptions
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTPaddingOptions

`public struct MTPaddingOptions : Sendable, Codable, Equatable`

Options for setting padding on calls to map methods.

- 

init(left:top:right:bottom:)

Initializes the padding options.

#### Declaration

Swift
public init(
left: Double? = nil,
top: Double? = nil,
right: Double? = nil,
bottom: Double? = nil
)

---

## File: Structs/MTPinchRotateAndZoomGesture.html

---
layout: mobile_sdk
title: "MTPinchRotateAndZoomGesture"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Handles zoom and rotate by pinching with two fingers."
id: mtpinchrotateandzoomgesture
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTPinchRotateAndZoomGesture

@MainActor
public struct MTPinchRotateAndZoomGesture : MTGesture

Handles zoom and rotate by pinching with two fingers.

- 

type

Type of the gesture.

#### Declaration

Swift
@MainActor
public var type: MTGestureType

- 

disable()

Asynchronous

Disables the gesture on the map.

#### Declaration

Swift
@MainActor
public func disable() async

- 

enable()

Asynchronous

Enables the gesture on the map.

#### Declaration

Swift
@MainActor
public func enable() async

---

## File: Structs/MTPoint.html

---
layout: mobile_sdk
title: "MTPoint"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Two numbers representing x and y screen coordinates in pixels."
id: mtpoint
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTPoint

`public struct MTPoint : Codable, Sendable`

Two numbers representing x and y screen coordinates in pixels.

- 

init(x:y:)

Initializes the point with x and y values.

#### Declaration

Swift
`public init(x: Double, y: Double)`

---

## File: Structs/MTPointLayerOptions.html

---
layout: mobile_sdk
title: "MTPointLayerOptions"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Options for building a point visualization layer through the helper."
id: mtpointlayeroptions
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTPointLayerOptions

`public struct MTPointLayerOptions : Codable, Sendable`

Options for building a point visualization layer through the helper.

Mirrors the available configuration including common shape options.

- 

data

Undocumented

#### Declaration

Swift
`public var data: String`

- 

layerId

Undocumented

#### Declaration

Swift
`public var layerId: String?`

- 

sourceId

Undocumented

#### Declaration

Swift
`public var sourceId: String?`

- 

beforeId

Undocumented

#### Declaration

Swift
`public var beforeId: String?`

- 

minzoom

Undocumented

#### Declaration

Swift
`public var minzoom: Double?`

- 

maxzoom

Undocumented

#### Declaration

Swift
`public var maxzoom: Double?`

- 

outline

Undocumented

#### Declaration

Swift
`public var outline: Bool?`

- 

outlineColor

Undocumented

#### Declaration

Swift
`public var outlineColor: MTStringOrZoomStringValues?`

- 

outlineWidth

Undocumented

#### Declaration

Swift
`public var outlineWidth: MTNumberOrZoomNumberValues?`

- 

outlineOpacity

Undocumented

#### Declaration

Swift
`public var outlineOpacity: MTNumberOrZoomNumberValues?`

- 

pointColor

Undocumented

#### Declaration

Swift
`public var pointColor: MTColorValue?`

- 

pointRadius

Undocumented

#### Declaration

Swift
`public var pointRadius: MTNumberOrZoomNumberValues?`

- 

minPointRadius

Undocumented

#### Declaration

Swift
`public var minPointRadius: Double?`

- 

maxPointRadius

Undocumented

#### Declaration

Swift
`public var maxPointRadius: Double?`

- 

property

Undocumented

#### Declaration

Swift
`public var property: String?`

- 

pointOpacity

Undocumented

#### Declaration

Swift
`public var pointOpacity: MTNumberOrZoomNumberValues?`

- 

alignOnViewport

Undocumented

#### Declaration

Swift
`public var alignOnViewport: Bool?`

- 

cluster

Undocumented

#### Declaration

Swift
`public var cluster: Bool?`

- 

showLabel

Undocumented

#### Declaration

Swift
`public var showLabel: Bool?`

- 

labelColor

Undocumented

#### Declaration

Swift
`public var labelColor: MTColorValue?`

- 

labelSize

Undocumented

#### Declaration

Swift
`public var labelSize: Double?`

- 

zoomCompensation

Undocumented

#### Declaration

Swift
`public var zoomCompensation: Bool?`

- 

init(data:layerId:sourceId:beforeId:minzoom:maxzoom:outline:outlineColor:outlineWidth:outlineOpacity:pointColor:pointRadius:minPointRadius:maxPointRadius:property:pointOpacity:alignOnViewport:cluster:showLabel:labelColor:labelSize:zoomCompensation:)

Undocumented

#### Declaration

Swift
public init(
data: String,
layerId: String? = nil,
sourceId: String? = nil,
beforeId: String? = nil,
minzoom: Double? = nil,
maxzoom: Double? = nil,
outline: Bool? = nil,
outlineColor: String? = nil,
outlineWidth: Double? = nil,
outlineOpacity: Double? = nil,
pointColor: String? = nil,
pointRadius: Double? = nil,
minPointRadius: Double? = nil,
maxPointRadius: Double? = nil,
property: String? = nil,
pointOpacity: Double? = nil,
alignOnViewport: Bool? = nil,
cluster: Bool? = nil,
showLabel: Bool? = nil,
labelColor: String? = nil,
labelSize: Double? = nil,
zoomCompensation: Bool? = nil
)

- 

init(data:layerId:sourceId:beforeId:minzoom:maxzoom:outline:outlineColor:outlineWidth:outlineOpacity:pointColor:pointRadius:minPointRadius:maxPointRadius:property:pointOpacity:alignOnViewport:cluster:showLabel:labelColor:labelSize:zoomCompensation:)

Convenience initializer accepting ramp-capable types for outline and point values.

#### Declaration

Swift
public init(
data: String,
layerId: String? = nil,
sourceId: String? = nil,
beforeId: String? = nil,
minzoom: Double? = nil,
maxzoom: Double? = nil,
outline: Bool? = nil,
outlineColor: MTStringOrZoomStringValues? = nil,
outlineWidth: MTNumberOrZoomNumberValues? = nil,
outlineOpacity: MTNumberOrZoomNumberValues? = nil,
pointColor: MTColorValue? = nil,
pointRadius: MTNumberOrZoomNumberValues? = nil,
minPointRadius: Double? = nil,
maxPointRadius: Double? = nil,
property: String? = nil,
pointOpacity: MTNumberOrZoomNumberValues? = nil,
alignOnViewport: Bool? = nil,
cluster: Bool? = nil,
showLabel: Bool? = nil,
labelColor: MTColorValue? = nil,
labelSize: Double? = nil,
zoomCompensation: Bool? = nil
)

---

## File: Structs/MTPolygonLayerOptions.html

---
layout: mobile_sdk
title: "MTPolygonLayerOptions"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Options for building a polygon (fill) visualization layer through the helper."
id: mtpolygonlayeroptions
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTPolygonLayerOptions

`public struct MTPolygonLayerOptions : Codable, Sendable`

Options for building a polygon (fill) visualization layer through the helper.

- 

data

Undocumented

#### Declaration

Swift
`public var data: String`

- 

layerId

Undocumented

#### Declaration

Swift
`public var layerId: String?`

- 

sourceId

Undocumented

#### Declaration

Swift
`public var sourceId: String?`

- 

beforeId

Undocumented

#### Declaration

Swift
`public var beforeId: String?`

- 

minzoom

Undocumented

#### Declaration

Swift
`public var minzoom: Double?`

- 

maxzoom

Undocumented

#### Declaration

Swift
`public var maxzoom: Double?`

- 

outline

Undocumented

#### Declaration

Swift
`public var outline: Bool?`

- 

outlineColor

Undocumented

#### Declaration

Swift
`public var outlineColor: MTStringOrZoomStringValues?`

- 

outlineWidth

Undocumented

#### Declaration

Swift
`public var outlineWidth: MTNumberOrZoomNumberValues?`

- 

outlineOpacity

Undocumented

#### Declaration

Swift
`public var outlineOpacity: MTNumberOrZoomNumberValues?`

- 

fillColor

Undocumented

#### Declaration

Swift
`public var fillColor: MTStringOrZoomStringValues?`

- 

fillOpacity

Undocumented

#### Declaration

Swift
`public var fillOpacity: MTNumberOrZoomNumberValues?`

- 

outlinePosition

Undocumented

#### Declaration

Swift
`public var outlinePosition: String?`

- 

outlineDashArray

Undocumented

#### Declaration

Swift
`public var outlineDashArray: MTDashArrayValue?`

- 

outlineCap

Undocumented

#### Declaration

Swift
`public var outlineCap: String?`

- 

outlineJoin

Undocumented

#### Declaration

Swift
`public var outlineJoin: String?`

- 

pattern

Undocumented

#### Declaration

Swift
`public var pattern: String?`

- 

outlineBlur

Undocumented

#### Declaration

Swift
`public var outlineBlur: MTNumberOrZoomNumberValues?`

- 

init(data:layerId:sourceId:beforeId:minzoom:maxzoom:outline:outlineColor:outlineWidth:outlineOpacity:fillColor:fillOpacity:outlinePosition:outlineDashArray:outlineCap:outlineJoin:pattern:outlineBlur:)

Undocumented

#### Declaration

Swift
public init(
data: String,
layerId: String? = nil,
sourceId: String? = nil,
beforeId: String? = nil,
minzoom: Double? = nil,
maxzoom: Double? = nil,
outline: Bool? = nil,
outlineColor: String? = nil,
outlineWidth: Double? = nil,
outlineOpacity: Double? = nil,
fillColor: String? = nil,
fillOpacity: Double? = nil,
outlinePosition: String? = nil,
outlineDashArray: String? = nil,
outlineCap: String? = nil,
outlineJoin: String? = nil,
pattern: String? = nil,
outlineBlur: Double? = nil
)

- 

init(data:layerId:sourceId:beforeId:minzoom:maxzoom:outline:outlineColor:outlineWidth:outlineOpacity:fillColor:fillOpacity:outlinePosition:outlineDashArray:outlineCap:outlineJoin:pattern:outlineBlur:)

Convenience initializer accepting ramp-capable types and union values directly.

#### Declaration

Swift
public init(
data: String,
layerId: String? = nil,
sourceId: String? = nil,
beforeId: String? = nil,
minzoom: Double? = nil,
maxzoom: Double? = nil,
outline: Bool? = nil,
outlineColor: MTStringOrZoomStringValues? = nil,
outlineWidth: MTNumberOrZoomNumberValues? = nil,
outlineOpacity: MTNumberOrZoomNumberValues? = nil,
fillColor: MTStringOrZoomStringValues? = nil,
fillOpacity: MTNumberOrZoomNumberValues? = nil,
outlinePosition: String? = nil,
outlineDashArray: MTDashArrayValue? = nil,
outlineCap: String? = nil,
outlineJoin: String? = nil,
pattern: String? = nil,
outlineBlur: MTNumberOrZoomNumberValues? = nil
)

---

## File: Structs/MTPolylineLayerOptions.html

---
layout: mobile_sdk
title: "MTPolylineLayerOptions"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Options for building a polyline (line) visualization layer through the helper."
id: mtpolylinelayeroptions
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTPolylineLayerOptions

`public struct MTPolylineLayerOptions : Codable, Sendable`

Options for building a polyline (line) visualization layer through the helper.

- 

data

Undocumented

#### Declaration

Swift
`public var data: String`

- 

layerId

Undocumented

#### Declaration

Swift
`public var layerId: String?`

- 

sourceId

Undocumented

#### Declaration

Swift
`public var sourceId: String?`

- 

beforeId

Undocumented

#### Declaration

Swift
`public var beforeId: String?`

- 

minzoom

Undocumented

#### Declaration

Swift
`public var minzoom: Double?`

- 

maxzoom

Undocumented

#### Declaration

Swift
`public var maxzoom: Double?`

- 

outline

Undocumented

#### Declaration

Swift
`public var outline: Bool?`

- 

outlineColor

Undocumented

#### Declaration

Swift
`public var outlineColor: MTStringOrZoomStringValues?`

- 

outlineWidth

Undocumented

#### Declaration

Swift
`public var outlineWidth: MTNumberOrZoomNumberValues?`

- 

outlineOpacity

Undocumented

#### Declaration

Swift
`public var outlineOpacity: MTNumberOrZoomNumberValues?`

- 

lineColor

Undocumented

#### Declaration

Swift
`public var lineColor: MTStringOrZoomStringValues?`

- 

lineWidth

Undocumented

#### Declaration

Swift
`public var lineWidth: MTNumberOrZoomNumberValues?`

- 

lineOpacity

Undocumented

#### Declaration

Swift
`public var lineOpacity: MTNumberOrZoomNumberValues?`

- 

lineBlur

Undocumented

#### Declaration

Swift
`public var lineBlur: MTNumberOrZoomNumberValues?`

- 

lineGapWidth

Undocumented

#### Declaration

Swift
`public var lineGapWidth: MTNumberOrZoomNumberValues?`

- 

lineDashArray

Undocumented

#### Declaration

Swift
`public var lineDashArray: MTDashArrayValue?`

- 

lineCap

Undocumented

#### Declaration

Swift
`public var lineCap: String?`

- 

lineJoin

Undocumented

#### Declaration

Swift
`public var lineJoin: String?`

- 

outlineBlur

Undocumented

#### Declaration

Swift
`public var outlineBlur: MTNumberOrZoomNumberValues?`

- 

init(data:layerId:sourceId:beforeId:minzoom:maxzoom:outline:outlineColor:outlineWidth:outlineOpacity:lineColor:lineWidth:lineOpacity:lineBlur:lineGapWidth:lineDashArray:lineCap:lineJoin:outlineBlur:)

Undocumented

#### Declaration

Swift
public init(
data: String,
layerId: String? = nil,
sourceId: String? = nil,
beforeId: String? = nil,
minzoom: Double? = nil,
maxzoom: Double? = nil,
outline: Bool? = nil,
outlineColor: String? = nil,
outlineWidth: Double? = nil,
outlineOpacity: Double? = nil,
lineColor: String? = nil,
lineWidth: Double? = nil,
lineOpacity: Double? = nil,
lineBlur: Double? = nil,
lineGapWidth: Double? = nil,
lineDashArray: String? = nil,
lineCap: String? = nil,
lineJoin: String? = nil,
outlineBlur: Double? = nil
)

- 

init(data:layerId:sourceId:beforeId:minzoom:maxzoom:outline:outlineColor:outlineWidth:outlineOpacity:lineColor:lineWidth:lineOpacity:lineBlur:lineGapWidth:lineDashArray:lineCap:lineJoin:outlineBlur:)

Convenience initializer accepting ramp-capable types and union values directly.

#### Declaration

Swift
public init(
data: String,
layerId: String? = nil,
sourceId: String? = nil,
beforeId: String? = nil,
minzoom: Double? = nil,
maxzoom: Double? = nil,
outline: Bool? = nil,
outlineColor: MTStringOrZoomStringValues? = nil,
outlineWidth: MTNumberOrZoomNumberValues? = nil,
outlineOpacity: MTNumberOrZoomNumberValues? = nil,
lineColor: MTStringOrZoomStringValues? = nil,
lineWidth: MTNumberOrZoomNumberValues? = nil,
lineOpacity: MTNumberOrZoomNumberValues? = nil,
lineBlur: MTNumberOrZoomNumberValues? = nil,
lineGapWidth: MTNumberOrZoomNumberValues? = nil,
lineDashArray: MTDashArrayValue? = nil,
lineCap: String? = nil,
lineJoin: String? = nil,
outlineBlur: MTNumberOrZoomNumberValues? = nil
)

---

## File: Structs/MTRGBAColor.html

---
layout: mobile_sdk
title: "MTRGBAColor"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "RGBA color represented by 0…255 components."
id: mtrgbacolor
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTRGBAColor

`public struct MTRGBAColor : Sendable, Codable`

RGBA color represented by 0…255 components.

- 

red

Undocumented

#### Declaration

Swift
`public var red: Int`

- 

green

Undocumented

#### Declaration

Swift
`public var green: Int`

- 

blue

Undocumented

#### Declaration

Swift
`public var blue: Int`

- 

alpha

Undocumented

#### Declaration

Swift
`public var alpha: Int?`

- 

init(red:green:blue:alpha:)

Initializes the color with individual components.

#### Declaration

Swift
`public init(red: Int, green: Int, blue: Int, alpha: Int? = nil)`

- 

init(color:)

Initializes the color from `UIColor`, preserving alpha.

#### Declaration

Swift
`public init(color: UIColor)`

- 

init(from:)

#### Declaration

Swift
`public init(from decoder: any Decoder) throws`

- 

encode(to:)

#### Declaration

Swift
`public func encode(to encoder: Encoder) throws`

---

## File: Structs/MTSky.html

---
layout: mobile_sdk
title: "MTSky"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Sky configuration used by map.setSky."
id: mtsky
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTSky

`public struct MTSky : Sendable, Codable, Equatable`

Sky configuration used by `map.setSky`.

- 

skyColor

The base color of the sky.

#### Declaration

Swift
`public var skyColor: MTSkyColorValue?`

- 

skyHorizonBlend

How to blend the sky color with the horizon in the [0, 1] range.

#### Declaration

Swift
`public var skyHorizonBlend: MTSkyNumberValue?`

- 

horizonColor

The base color at the horizon.

#### Declaration

Swift
`public var horizonColor: MTSkyColorValue?`

- 

horizonFogBlend

How to blend the fog and horizon colors in the [0, 1] range.

#### Declaration

Swift
`public var horizonFogBlend: MTSkyNumberValue?`

- 

fogColor

The base color for the fog (requires 3D terrain).

#### Declaration

Swift
`public var fogColor: MTSkyColorValue?`

- 

fogGroundBlend

How to blend fog over the terrain in the [0, 1] range.

#### Declaration

Swift
`public var fogGroundBlend: MTSkyNumberValue?`

- 

atmosphereBlend

How to blend the atmosphere in the [0, 1] range.

#### Declaration

Swift
`public var atmosphereBlend: MTSkyNumberValue?`

- 

init(skyColor:skyHorizonBlend:horizonColor:horizonFogBlend:fogColor:fogGroundBlend:atmosphereBlend:)

Undocumented

#### Declaration

Swift
public init(
skyColor: MTSkyColorValue? = nil,
skyHorizonBlend: MTSkyNumberValue? = nil,
horizonColor: MTSkyColorValue? = nil,
horizonFogBlend: MTSkyNumberValue? = nil,
fogColor: MTSkyColorValue? = nil,
fogGroundBlend: MTSkyNumberValue? = nil,
atmosphereBlend: MTSkyNumberValue? = nil
)

- 

init(from:)

#### Declaration

Swift
`public init(from decoder: any Decoder) throws`

- 

encode(to:)

#### Declaration

Swift
`public func encode(to encoder: Encoder) throws`

---

## File: Structs/MTSourceData.html

---
layout: mobile_sdk
title: "MTSourceData"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "The style spec representation of the source if the event has a dataType of source ."
id: mtsourcedata
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTSourceData

`public struct MTSourceData : Codable`

The style spec representation of the source if the event has a dataType of source .

- 

init(from:)

#### Declaration

Swift
`public init(from decoder: any Decoder) throws`

---

## File: Structs/MTSpace.html

---
layout: mobile_sdk
title: "MTSpace"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Configuration for the “space” background."
id: mtspace
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTSpace

`public struct MTSpace : Sendable, Codable`

Configuration for the “space” background.

- 

color

Optional color to apply to the background and/or stars depending on preset.

#### Declaration

Swift
`public var color: MTColor?`

- 

preset

Optional cubemap preset.

#### Declaration

Swift
`public var preset: MTSpacePreset?`

- 

faces

Optional faces definition for a custom cubemap.

#### Declaration

Swift
`public var faces: MTSpaceFaces?`

- 

path

Optional path definition for a custom cubemap.

#### Declaration

Swift
`public var path: MTSpacePath?`

- 

init(color:preset:faces:path:)

Undocumented

#### Declaration

Swift
public init(
color: MTColor? = nil,
preset: MTSpacePreset? = nil,
faces: MTSpaceFaces? = nil,
path: MTSpacePath? = nil
)

- 

init(from:)

#### Declaration

Swift
`public init(from decoder: any Decoder) throws`

- 

encode(to:)

#### Declaration

Swift
`public func encode(to encoder: Encoder) throws`

---

## File: Structs/MTSpaceFaces.html

---
layout: mobile_sdk
title: "MTSpaceFaces"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Faces definition for a custom cubemap."
id: mtspacefaces
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTSpaceFaces

`public struct MTSpaceFaces : Sendable, Codable`

Faces definition for a custom cubemap.

- 

pX

Undocumented

#### Declaration

Swift
`public var pX: URL`

- 

nX

Undocumented

#### Declaration

Swift
`public var nX: URL`

- 

pY

Undocumented

#### Declaration

Swift
`public var pY: URL`

- 

nY

Undocumented

#### Declaration

Swift
`public var nY: URL`

- 

pZ

Undocumented

#### Declaration

Swift
`public var pZ: URL`

- 

nZ

Undocumented

#### Declaration

Swift
`public var nZ: URL`

- 

init(pX:nX:pY:nY:pZ:nZ:)

Undocumented

#### Declaration

Swift
`public init(pX: URL, nX: URL, pY: URL, nY: URL, pZ: URL, nZ: URL)`

---

## File: Structs/MTSpacePath.html

---
layout: mobile_sdk
title: "MTSpacePath"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Path-based configuration for cubemap files."
id: mtspacepath
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTSpacePath

`public struct MTSpacePath : Sendable, Codable`

Path-based configuration for cubemap files.

This fetches all images from a path, this assumes all files are named px, nx, py, ny, pz, nz
and suffixed with the appropriate extension specified in format.

- 

baseUrl

Undocumented

#### Declaration

Swift
`public var baseUrl: URL`

- 

format

Undocumented

#### Declaration

Swift
`public var format: String?`

- 

init(baseUrl:format:)

Undocumented

#### Declaration

Swift
`public init(baseUrl: URL, format: String? = nil)`

---

## File: Structs/MTStyleImageOptions/Content.html

---
layout: mobile_sdk
title: "Content"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Insets that describe the stretchable area of the image."
id: content
breadcrumb: "Mobile SDK/iOS/Reference/MTStyleImageOptions"
---

# Content

`struct Content : Codable, Equatable, Sendable`

Insets that describe the stretchable area of the image.

- 

left

Left inset.

#### Declaration

Swift
`public var left: Double`

- 

top

Top inset.

#### Declaration

Swift
`public var top: Double`

- 

right

Right inset.

#### Declaration

Swift
`public var right: Double`

- 

bottom

Bottom inset.

#### Declaration

Swift
`public var bottom: Double`

- 

init(left:top:right:bottom:)

Creates a new content inset definition.

#### Declaration

Swift
`public init(left: Double, top: Double, right: Double, bottom: Double)`

#### Parameters

| left | Left inset. |
| top | Top inset. |
| right | Right inset. |
| bottom | Bottom inset. |

- 

encode(to:)

#### Declaration

Swift
`public func encode(to encoder: Encoder) throws`

- 

init(from:)

#### Declaration

Swift
`public init(from decoder: Decoder) throws`

---

## File: Structs/MTStyleImageOptions/Stretch.html

---
layout: mobile_sdk
title: "Stretch"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Describes a stretchable segment on an axis."
id: stretch
breadcrumb: "Mobile SDK/iOS/Reference/MTStyleImageOptions"
---

# Stretch

`struct Stretch : Codable, Equatable, Sendable`

Describes a stretchable segment on an axis.

- 

from

Starting point of the stretch range.

#### Declaration

Swift
`public var from: Double`

- 

to

Ending point of the stretch range.

#### Declaration

Swift
`public var to: Double`

- 

init(from:to:)

Creates a new stretch segment.

#### Declaration

Swift
`public init(from: Double, to: Double)`

#### Parameters

| from | Starting point of the stretch range. |
| to | Ending point of the stretch range. |

- 

encode(to:)

#### Declaration

Swift
`public func encode(to encoder: Encoder) throws`

- 

init(from:)

#### Declaration

Swift
`public init(from decoder: Decoder) throws`

---

## File: Structs/MTStyleImageOptions.html

---
layout: mobile_sdk
title: "MTStyleImageOptions"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Configuration that controls how an image is registered within the MapTiler style."
id: mtstyleimageoptions
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTStyleImageOptions

`public struct MTStyleImageOptions : Codable, Equatable, Sendable`

Configuration that controls how an image is registered within the MapTiler style.

- 

pixelRatio

Pixel ratio of the supplied image. Values below zero are ignored.

#### Declaration

Swift
`public var pixelRatio: Double?`

- 

sdf

Indicates whether the image should be interpreted as a signed distance field.

#### Declaration

Swift
`public var sdf: Bool?`

- 

stretchX

Horizontal stretch ranges applied when rendering the image.

#### Declaration

Swift
`public var stretchX: [Stretch]?`

- 

stretchY

Vertical stretch ranges applied when rendering the image.

#### Declaration

Swift
`public var stretchY: [Stretch]?`

- 

content

Content insets that describe the stretchable area of the image.

#### Declaration

Swift
`public var content: Content?`

- 

init(pixelRatio:sdf:stretchX:stretchY:content:)

Creates a new set of image options.

#### Declaration

Swift
public init(
pixelRatio: Double? = nil,
sdf: Bool? = nil,
stretchX: [Stretch]? = nil,
stretchY: [Stretch]? = nil,
content: Content? = nil
)

#### Parameters

| pixelRatio | Pixel ratio of the supplied image. |
| sdf | Indicates whether the image should be interpreted as a signed distance field. |
| stretchX | Horizontal stretch ranges applied when rendering the image. |
| stretchY | Vertical stretch ranges applied when rendering the image. |
| content | Insets describing the stretchable area of the image. |

- 

Stretch

Describes a stretchable segment on an axis.

See more

#### Declaration

Swift
`struct Stretch : Codable, Equatable, Sendable`

- 

Content

Insets that describe the stretchable area of the image.

See more

#### Declaration

Swift
`struct Content : Codable, Equatable, Sendable`

---

## File: Structs/MTStyleSetterOptions.html

---
layout: mobile_sdk
title: "MTStyleSetterOptions"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Supporting type to add validation to another style related type."
id: mtstylesetteroptions
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTStyleSetterOptions

`public struct MTStyleSetterOptions : Sendable, Codable`

Supporting type to add validation to another style related type.

- 

shouldValidate

Boolean indicating whether filter conforms to the MapLibre Style Specification.

Disabling validation is a performance optimization that should only be used
if you have previously validated the values you will be passing to this function.

#### Declaration

Swift
`public var shouldValidate: Bool`

- 

init(shouldValidate:)

Initializes the setter options.

#### Declaration

Swift
`public init(shouldValidate: Bool)`

---

## File: Structs/MTTwoFingersDragPitchGesture.html

---
layout: mobile_sdk
title: "MTTwoFingersDragPitchGesture"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Handles changing the pitch by dragging with two fingers."
id: mttwofingersdragpitchgesture
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTTwoFingersDragPitchGesture

@MainActor
public struct MTTwoFingersDragPitchGesture : MTGesture

Handles changing the pitch by dragging with two fingers.

- 

type

Type of the gesture.

#### Declaration

Swift
@MainActor
public var type: MTGestureType

- 

disable()

Asynchronous

Disables the gesture on the map.

#### Declaration

Swift
@MainActor
public func disable() async

- 

enable()

Asynchronous

Enables the gesture on the map.

#### Declaration

Swift
@MainActor
public func enable() async

---

## File: Structs/MTZoomNumberValue.html

---
layout: mobile_sdk
title: "MTZoomNumberValue"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "A single numeric value at a given zoom level."
id: mtzoomnumbervalue
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTZoomNumberValue

`public struct MTZoomNumberValue : Codable, Sendable`

A single numeric value at a given zoom level.

- 

zoom

Zoom level

#### Declaration

Swift
`public var zoom: Double`

- 

value

Value for the given zoom level

#### Declaration

Swift
`public var value: Double`

- 

init(zoom:value:)

Undocumented

#### Declaration

Swift
`public init(zoom: Double, value: Double)`

---

## File: Structs/MTZoomStringValue.html

---
layout: mobile_sdk
title: "MTZoomStringValue"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "A single string value at a given zoom level."
id: mtzoomstringvalue
breadcrumb: "Mobile SDK/iOS/Reference/Structs"
---

# MTZoomStringValue

`public struct MTZoomStringValue : Codable, Sendable`

A single string value at a given zoom level.

- 

zoom

Zoom level

#### Declaration

Swift
`public var zoom: Double`

- 

value

Value for the given zoom level

#### Declaration

Swift
`public var value: String`

- 

init(zoom:value:)

Undocumented

#### Declaration

Swift
`public init(zoom: Double, value: String)`

---

