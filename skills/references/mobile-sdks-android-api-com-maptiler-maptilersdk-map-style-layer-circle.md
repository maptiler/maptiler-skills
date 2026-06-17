# MapTiler Android SDK API Reference - com.maptiler.maptilersdk.map.style.layer.circle

This document is a part of the Android SDK API reference documentation, covering the `com.maptiler.maptilersdk.map.style.layer.circle` package.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer/-m-t-circle-layer.html

---
layout: mobile_sdk
title: "MTCircleLayer"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTCircleLayer"
id: -m-t-circle-layer
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer"
---
# MTCircleLayer

constructor(identifier: String, sourceIdentifier: String)constructor(identifier: String, sourceIdentifier: String, maxZoom: Double, minZoom: Double, sourceLayer: String)constructor(identifier: String, type: MTLayerType, sourceIdentifier: String, maxZoom: Double?, minZoom: Double?, sourceLayer: String?, blur: Double?, color: StyleValue?, opacity: Double?, radius: StyleValue?, strokeColor: Int?, strokeOpacity: Double?, strokeWidth: Double?, translate: DoubleArray?, translateAnchor: MTCircleTranslateAnchor?, pitchAlignment: MTCirclePitchAlignment?, pitchScale: MTCirclePitchScale?, sortKey: Double?, visibility: MTLayerVisibility)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer/blur.html

---
layout: mobile_sdk
title: "blur"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "blur"
id: blur
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer"
---
# blur

var blur: Double?Amount to blur the circle.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer/color.html

---
layout: mobile_sdk
title: "color"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "color"
id: color
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer"
---
# color

var color: StyleValue?The color of the circle (constant or expression).

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer/identifier.html

---
layout: mobile_sdk
title: "identifier"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "identifier"
id: identifier
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer"
---
# identifier

@SerialName(value = "id")open override var identifier: StringUnique layer identifier.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer/index.html

---
layout: mobile_sdk
title: "MTCircleLayer"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTCircleLayer"
id: -m-t-circle-layer
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer"
---
# MTCircleLayer

@Serializableclass MTCircleLayer : MTLayerCircle style layer that renders filled circles.

MembersMembers & Extensions

## Constructors

MTCircleLayer

constructor(identifier: String, sourceIdentifier: String)constructor(identifier: String, sourceIdentifier: String, maxZoom: Double, minZoom: Double, sourceLayer: String)constructor(identifier: String, type: MTLayerType, sourceIdentifier: String, maxZoom: Double?, minZoom: Double?, sourceLayer: String?, blur: Double?, color: StyleValue?, opacity: Double?, radius: StyleValue?, strokeColor: Int?, strokeOpacity: Double?, strokeWidth: Double?, translate: DoubleArray?, translateAnchor: MTCircleTranslateAnchor?, pitchAlignment: MTCirclePitchAlignment?, pitchScale: MTCirclePitchScale?, sortKey: Double?, visibility: MTLayerVisibility)

## Properties

blur

var blur: Double?Amount to blur the circle.

color

var color: StyleValue?The color of the circle (constant or expression).

identifier

@SerialName(value = "id")open override var identifier: StringUnique layer identifier.

maxZoom

@SerialName(value = "maxzoom")open override var maxZoom: Double?The maximum zoom level for the layer.

minZoom

@SerialName(value = "minzoom")open override var minZoom: Double?The minimum zoom level for the layer.

opacity

var opacity: Double?The opacity of the circle.

pitchAlignment

var pitchAlignment: MTCirclePitchAlignment?Controls the alignment of circles when map is pitched.

pitchScale

var pitchScale: MTCirclePitchScale?Controls the scaling of circles when map is pitched.

radius

var radius: StyleValue?The radius of the circle in pixels (constant or expression).

sortKey

var sortKey: Double?Sort key to determine rendering order.

sourceIdentifier

@SerialName(value = "source")open override var sourceIdentifier: StringIdentifier of the source to be used for this layer.

sourceLayer

@SerialName(value = "source-layer")open override var sourceLayer: String?Vector tile source layer name, if applicable.

strokeColor

@Serializable(with = ColorAsHexSerializer::class)var strokeColor: Int?The stroke color of the circle.

strokeOpacity

var strokeOpacity: Double?The stroke opacity of the circle.

strokeWidth

var strokeWidth: Double?The stroke width of the circle.

translate

var translate: DoubleArray?The geometry’s offset. Values are x, y.

translateAnchor

var translateAnchor: MTCircleTranslateAnchor?Controls the frame of reference for translate.

type

open override var type: MTLayerTypeType of the layer.

visibility

var visibility: MTLayerVisibilityVisibility of the layer.

## Functions

colorConst

fun MTCircleLayer.colorConst(color: Int): MTCircleLayer

colorExpr

fun MTCircleLayer.colorExpr(expr: PropertyValue): MTCircleLayer

radiusConst

fun MTCircleLayer.radiusConst(value: Double): MTCircleLayer

radiusExpr

fun MTCircleLayer.radiusExpr(expr: PropertyValue): MTCircleLayer

withFilter

fun withFilter(expr: PropertyValue)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer/max-zoom.html

---
layout: mobile_sdk
title: "maxZoom"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "maxZoom"
id: max-zoom
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer"
---
# maxZoom

@SerialName(value = "maxzoom")open override var maxZoom: Double?The maximum zoom level for the layer.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer/min-zoom.html

---
layout: mobile_sdk
title: "minZoom"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "minZoom"
id: min-zoom
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer"
---
# minZoom

@SerialName(value = "minzoom")open override var minZoom: Double?The minimum zoom level for the layer.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer/opacity.html

---
layout: mobile_sdk
title: "opacity"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "opacity"
id: opacity
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer"
---
# opacity

var opacity: Double?The opacity of the circle.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer/pitch-alignment.html

---
layout: mobile_sdk
title: "pitchAlignment"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "pitchAlignment"
id: pitch-alignment
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer"
---
# pitchAlignment

var pitchAlignment: MTCirclePitchAlignment?Controls the alignment of circles when map is pitched.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer/pitch-scale.html

---
layout: mobile_sdk
title: "pitchScale"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "pitchScale"
id: pitch-scale
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer"
---
# pitchScale

var pitchScale: MTCirclePitchScale?Controls the scaling of circles when map is pitched.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer/radius.html

---
layout: mobile_sdk
title: "radius"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "radius"
id: radius
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer"
---
# radius

var radius: StyleValue?The radius of the circle in pixels (constant or expression).

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer/sort-key.html

---
layout: mobile_sdk
title: "sortKey"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "sortKey"
id: sort-key
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer"
---
# sortKey

var sortKey: Double?Sort key to determine rendering order.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer/source-identifier.html

---
layout: mobile_sdk
title: "sourceIdentifier"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "sourceIdentifier"
id: source-identifier
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer"
---
# sourceIdentifier

@SerialName(value = "source")open override var sourceIdentifier: StringIdentifier of the source to be used for this layer.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer/source-layer.html

---
layout: mobile_sdk
title: "sourceLayer"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "sourceLayer"
id: source-layer
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer"
---
# sourceLayer

@SerialName(value = "source-layer")open override var sourceLayer: String?Vector tile source layer name, if applicable.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer/stroke-color.html

---
layout: mobile_sdk
title: "strokeColor"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "strokeColor"
id: stroke-color
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer"
---
# strokeColor

@Serializable(with = ColorAsHexSerializer::class)var strokeColor: Int?The stroke color of the circle.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer/stroke-opacity.html

---
layout: mobile_sdk
title: "strokeOpacity"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "strokeOpacity"
id: stroke-opacity
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer"
---
# strokeOpacity

var strokeOpacity: Double?The stroke opacity of the circle.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer/stroke-width.html

---
layout: mobile_sdk
title: "strokeWidth"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "strokeWidth"
id: stroke-width
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer"
---
# strokeWidth

var strokeWidth: Double?The stroke width of the circle.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer/translate-anchor.html

---
layout: mobile_sdk
title: "translateAnchor"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "translateAnchor"
id: translate-anchor
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer"
---
# translateAnchor

var translateAnchor: MTCircleTranslateAnchor?Controls the frame of reference for translate.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer/translate.html

---
layout: mobile_sdk
title: "translate"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "translate"
id: translate
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer"
---
# translate

var translate: DoubleArray?The geometry’s offset. Values are x, y.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer/type.html

---
layout: mobile_sdk
title: "type"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "type"
id: type
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer"
---
# type

open override var type: MTLayerTypeType of the layer.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer/visibility.html

---
layout: mobile_sdk
title: "visibility"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "visibility"
id: visibility
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer"
---
# visibility

var visibility: MTLayerVisibilityVisibility of the layer.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer/with-filter.html

---
layout: mobile_sdk
title: "withFilter"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "withFilter"
id: with-filter
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-layer"
---
# withFilter

fun withFilter(expr: PropertyValue)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-pitch-alignment/-m-a-p/index.html

---
layout: mobile_sdk
title: "MAP"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MAP"
id: -m-a-p
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-pitch-alignment/-m-a-p"
---
# MAP

@SerialName(value = "map")MAPCircles are aligned to the map.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-pitch-alignment/-v-i-e-w-p-o-r-t/index.html

---
layout: mobile_sdk
title: "VIEWPORT"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "VIEWPORT"
id: -v-i-e-w-p-o-r-t
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-pitch-alignment/-v-i-e-w-p-o-r-t"
---
# VIEWPORT

@SerialName(value = "viewport")VIEWPORTCircles are aligned to the viewport.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-pitch-alignment/entries.html

---
layout: mobile_sdk
title: "entries"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "entries"
id: entries
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-pitch-alignment"
---
# entries

val entries: EnumEntries<MTCirclePitchAlignment>Returns a representation of an immutable list of all enum entries, in the order they're declared.This method may be used to iterate over the enum entries.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-pitch-alignment/index.html

---
layout: mobile_sdk
title: "MTCirclePitchAlignment"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTCirclePitchAlignment"
id: -m-t-circle-pitch-alignment
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-pitch-alignment"
---
# MTCirclePitchAlignment

@Serializableenum MTCirclePitchAlignment : Enum<MTCirclePitchAlignment> Controls the alignment of circles when the map pitch is applied.

MembersEntries

## Entries

VIEWPORT

@SerialName(value = "viewport")VIEWPORTCircles are aligned to the viewport.

MAP

@SerialName(value = "map")MAPCircles are aligned to the map.

## Properties

entries

val entries: EnumEntries<MTCirclePitchAlignment>Returns a representation of an immutable list of all enum entries, in the order they're declared.

name

val name: String

ordinal

val ordinal: Int

## Functions

valueOf

fun valueOf(value: String): MTCirclePitchAlignmentReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

values

fun values(): Array<MTCirclePitchAlignment>Returns an array containing the constants of this enum type, in the order they're declared.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-pitch-alignment/value-of.html

---
layout: mobile_sdk
title: "valueOf"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "valueOf"
id: value-of
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-pitch-alignment"
---
# valueOf

fun valueOf(value: String): MTCirclePitchAlignmentReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
#### Throws

IllegalArgumentExceptionif this enum type has no constant with the specified name

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-pitch-alignment/values.html

---
layout: mobile_sdk
title: "values"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "values"
id: values
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-pitch-alignment"
---
# values

fun values(): Array<MTCirclePitchAlignment>Returns an array containing the constants of this enum type, in the order they're declared.This method may be used to iterate over the constants.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-pitch-scale/-m-a-p/index.html

---
layout: mobile_sdk
title: "MAP"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MAP"
id: -m-a-p
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-pitch-scale/-m-a-p"
---
# MAP

@SerialName(value = "map")MAPCircles are scaled according to the map.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-pitch-scale/-v-i-e-w-p-o-r-t/index.html

---
layout: mobile_sdk
title: "VIEWPORT"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "VIEWPORT"
id: -v-i-e-w-p-o-r-t
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-pitch-scale/-v-i-e-w-p-o-r-t"
---
# VIEWPORT

@SerialName(value = "viewport")VIEWPORTCircles are scaled according to the viewport.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-pitch-scale/entries.html

---
layout: mobile_sdk
title: "entries"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "entries"
id: entries
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-pitch-scale"
---
# entries

val entries: EnumEntries<MTCirclePitchScale>Returns a representation of an immutable list of all enum entries, in the order they're declared.This method may be used to iterate over the enum entries.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-pitch-scale/index.html

---
layout: mobile_sdk
title: "MTCirclePitchScale"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTCirclePitchScale"
id: -m-t-circle-pitch-scale
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-pitch-scale"
---
# MTCirclePitchScale

@Serializableenum MTCirclePitchScale : Enum<MTCirclePitchScale> Controls the scaling of circles when the map pitch is applied.

MembersEntries

## Entries

VIEWPORT

@SerialName(value = "viewport")VIEWPORTCircles are scaled according to the viewport.

MAP

@SerialName(value = "map")MAPCircles are scaled according to the map.

## Properties

entries

val entries: EnumEntries<MTCirclePitchScale>Returns a representation of an immutable list of all enum entries, in the order they're declared.

name

val name: String

ordinal

val ordinal: Int

## Functions

valueOf

fun valueOf(value: String): MTCirclePitchScaleReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

values

fun values(): Array<MTCirclePitchScale>Returns an array containing the constants of this enum type, in the order they're declared.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-pitch-scale/value-of.html

---
layout: mobile_sdk
title: "valueOf"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "valueOf"
id: value-of
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-pitch-scale"
---
# valueOf

fun valueOf(value: String): MTCirclePitchScaleReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
#### Throws

IllegalArgumentExceptionif this enum type has no constant with the specified name

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-pitch-scale/values.html

---
layout: mobile_sdk
title: "values"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "values"
id: values
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-pitch-scale"
---
# values

fun values(): Array<MTCirclePitchScale>Returns an array containing the constants of this enum type, in the order they're declared.This method may be used to iterate over the constants.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-translate-anchor/-m-a-p/index.html

---
layout: mobile_sdk
title: "MAP"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MAP"
id: -m-a-p
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-translate-anchor/-m-a-p"
---
# MAP

@SerialName(value = "map")MAPThe circle is translated relative to the map.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-translate-anchor/-v-i-e-w-p-o-r-t/index.html

---
layout: mobile_sdk
title: "VIEWPORT"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "VIEWPORT"
id: -v-i-e-w-p-o-r-t
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-translate-anchor/-v-i-e-w-p-o-r-t"
---
# VIEWPORT

@SerialName(value = "viewport")VIEWPORTThe circle is translated relative to the viewport.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-translate-anchor/entries.html

---
layout: mobile_sdk
title: "entries"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "entries"
id: entries
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-translate-anchor"
---
# entries

val entries: EnumEntries<MTCircleTranslateAnchor>Returns a representation of an immutable list of all enum entries, in the order they're declared.This method may be used to iterate over the enum entries.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-translate-anchor/index.html

---
layout: mobile_sdk
title: "MTCircleTranslateAnchor"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTCircleTranslateAnchor"
id: -m-t-circle-translate-anchor
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-translate-anchor"
---
# MTCircleTranslateAnchor

@Serializableenum MTCircleTranslateAnchor : Enum<MTCircleTranslateAnchor> Controls the frame of reference for circle-translate.

MembersEntries

## Entries

MAP

@SerialName(value = "map")MAPThe circle is translated relative to the map.

VIEWPORT

@SerialName(value = "viewport")VIEWPORTThe circle is translated relative to the viewport.

## Properties

entries

val entries: EnumEntries<MTCircleTranslateAnchor>Returns a representation of an immutable list of all enum entries, in the order they're declared.

name

val name: String

ordinal

val ordinal: Int

## Functions

valueOf

fun valueOf(value: String): MTCircleTranslateAnchorReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

values

fun values(): Array<MTCircleTranslateAnchor>Returns an array containing the constants of this enum type, in the order they're declared.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-translate-anchor/value-of.html

---
layout: mobile_sdk
title: "valueOf"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "valueOf"
id: value-of
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-translate-anchor"
---
# valueOf

fun valueOf(value: String): MTCircleTranslateAnchorReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
#### Throws

IllegalArgumentExceptionif this enum type has no constant with the specified name

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-translate-anchor/values.html

---
layout: mobile_sdk
title: "values"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "values"
id: values
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/-m-t-circle-translate-anchor"
---
# values

fun values(): Array<MTCircleTranslateAnchor>Returns an array containing the constants of this enum type, in the order they're declared.This method may be used to iterate over the constants.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/color-const.html

---
layout: mobile_sdk
title: "colorConst"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "colorConst"
id: color-const
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle"
---
# colorConst

fun MTCircleLayer.colorConst(color: Int): MTCircleLayer

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/color-expr.html

---
layout: mobile_sdk
title: "colorExpr"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "colorExpr"
id: color-expr
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle"
---
# colorExpr

fun MTCircleLayer.colorExpr(expr: PropertyValue): MTCircleLayer

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/index.html

---
layout: mobile_sdk
title: "com.maptiler.maptilersdk.map.style.layer.circle"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "com.maptiler.maptilersdk.map.style.layer.circle"
id: com.maptiler.maptilersdk.map.style.layer.circle
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle"
---
# com.maptiler.maptilersdk.map.style.layer.circle

TypesFunctions

## Types

MTCircleLayer

@Serializableclass MTCircleLayer : MTLayerCircle style layer that renders filled circles.

MTCirclePitchAlignment

@Serializableenum MTCirclePitchAlignment : Enum<MTCirclePitchAlignment> Controls the alignment of circles when the map pitch is applied.

MTCirclePitchScale

@Serializableenum MTCirclePitchScale : Enum<MTCirclePitchScale> Controls the scaling of circles when the map pitch is applied.

MTCircleTranslateAnchor

@Serializableenum MTCircleTranslateAnchor : Enum<MTCircleTranslateAnchor> Controls the frame of reference for circle-translate.

## Functions

colorConst

fun MTCircleLayer.colorConst(color: Int): MTCircleLayer

colorExpr

fun MTCircleLayer.colorExpr(expr: PropertyValue): MTCircleLayer

radiusConst

fun MTCircleLayer.radiusConst(value: Double): MTCircleLayer

radiusExpr

fun MTCircleLayer.radiusExpr(expr: PropertyValue): MTCircleLayer

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/radius-const.html

---
layout: mobile_sdk
title: "radiusConst"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "radiusConst"
id: radius-const
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle"
---
# radiusConst

fun MTCircleLayer.radiusConst(value: Double): MTCircleLayer

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle/radius-expr.html

---
layout: mobile_sdk
title: "radiusExpr"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "radiusExpr"
id: radius-expr
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.circle"
---
# radiusExpr

fun MTCircleLayer.radiusExpr(expr: PropertyValue): MTCircleLayer

---

