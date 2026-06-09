# MapTiler Android SDK API Reference - com.maptiler.maptilersdk.map.style.layer.line

This document is a part of the Android SDK API reference documentation, covering the `com.maptiler.maptilersdk.map.style.layer.line` package.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-cap/-b-u-t-t/index.html

---
layout: mobile_sdk
title: "BUTT"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "BUTT"
id: -b-u-t-t
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-cap/-b-u-t-t"
---
# BUTT

@SerialName(value = "butt")BUTTA cap with a squared-off end which is drawn to the exact endpoint of the line.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-cap/-r-o-u-n-d/index.html

---
layout: mobile_sdk
title: "ROUND"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ROUND"
id: -r-o-u-n-d
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-cap/-r-o-u-n-d"
---
# ROUND

@SerialName(value = "round")ROUNDA cap with a rounded end which is drawn beyond the endpoint of the line at a radius of one-half of the line’s width and centered on the endpoint of the line.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-cap/-s-q-u-a-r-e/index.html

---
layout: mobile_sdk
title: "SQUARE"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "SQUARE"
id: -s-q-u-a-r-e
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-cap/-s-q-u-a-r-e"
---
# SQUARE

@SerialName(value = "square")SQUAREA cap with a squared-off end which is drawn beyond the endpoint of the line at a distance of one-half of the line’s width.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-cap/entries.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-cap"
---
# entries

val entries: EnumEntries<MTLineCap>Returns a representation of an immutable list of all enum entries, in the order they're declared.This method may be used to iterate over the enum entries.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-cap/index.html

---
layout: mobile_sdk
title: "MTLineCap"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTLineCap"
id: -m-t-line-cap
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-cap"
---
# MTLineCap

@Serializableenum MTLineCap : Enum<MTLineCap> The display of line endings.

MembersEntries

## Entries

BUTT

@SerialName(value = "butt")BUTTA cap with a squared-off end which is drawn to the exact endpoint of the line.

ROUND

@SerialName(value = "round")ROUNDA cap with a rounded end which is drawn beyond the endpoint of the line at a radius of one-half of the line’s width and centered on the endpoint of the line.

SQUARE

@SerialName(value = "square")SQUAREA cap with a squared-off end which is drawn beyond the endpoint of the line at a distance of one-half of the line’s width.

## Properties

entries

val entries: EnumEntries<MTLineCap>Returns a representation of an immutable list of all enum entries, in the order they're declared.

name

val name: String

ordinal

val ordinal: Int

## Functions

valueOf

fun valueOf(value: String): MTLineCapReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

values

fun values(): Array<MTLineCap>Returns an array containing the constants of this enum type, in the order they're declared.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-cap/value-of.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-cap"
---
# valueOf

fun valueOf(value: String): MTLineCapReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
#### Throws

IllegalArgumentExceptionif this enum type has no constant with the specified name

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-cap/values.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-cap"
---
# values

fun values(): Array<MTLineCap>Returns an array containing the constants of this enum type, in the order they're declared.This method may be used to iterate over the constants.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-join/-b-e-v-e-l/index.html

---
layout: mobile_sdk
title: "BEVEL"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "BEVEL"
id: -b-e-v-e-l
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-join/-b-e-v-e-l"
---
# BEVEL

@SerialName(value = "bevel")BEVELA join with a squared-off end which is drawn beyond the endpoint of the line at a distance of one-half of the line’s width.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-join/-m-i-t-e-r/index.html

---
layout: mobile_sdk
title: "MITER"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MITER"
id: -m-i-t-e-r
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-join/-m-i-t-e-r"
---
# MITER

@SerialName(value = "miter")MITERA join with a sharp, angled corner which is drawn with the outer sides beyond the endpoint of the path until they meet.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-join/-r-o-u-n-d/index.html

---
layout: mobile_sdk
title: "ROUND"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ROUND"
id: -r-o-u-n-d
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-join/-r-o-u-n-d"
---
# ROUND

@SerialName(value = "round")ROUNDA join with a rounded end which is drawn beyond the endpoint of the line at a radius of one-half of the line’s width and centered on the endpoint of the line.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-join/entries.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-join"
---
# entries

val entries: EnumEntries<MTLineJoin>Returns a representation of an immutable list of all enum entries, in the order they're declared.This method may be used to iterate over the enum entries.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-join/index.html

---
layout: mobile_sdk
title: "MTLineJoin"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTLineJoin"
id: -m-t-line-join
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-join"
---
# MTLineJoin

@Serializableenum MTLineJoin : Enum<MTLineJoin> The display of lines when joining.

MembersEntries

## Entries

BEVEL

@SerialName(value = "bevel")BEVELA join with a squared-off end which is drawn beyond the endpoint of the line at a distance of one-half of the line’s width.

ROUND

@SerialName(value = "round")ROUNDA join with a rounded end which is drawn beyond the endpoint of the line at a radius of one-half of the line’s width and centered on the endpoint of the line.

MITER

@SerialName(value = "miter")MITERA join with a sharp, angled corner which is drawn with the outer sides beyond the endpoint of the path until they meet.

## Properties

entries

val entries: EnumEntries<MTLineJoin>Returns a representation of an immutable list of all enum entries, in the order they're declared.

name

val name: String

ordinal

val ordinal: Int

## Functions

valueOf

fun valueOf(value: String): MTLineJoinReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

values

fun values(): Array<MTLineJoin>Returns an array containing the constants of this enum type, in the order they're declared.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-join/value-of.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-join"
---
# valueOf

fun valueOf(value: String): MTLineJoinReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
#### Throws

IllegalArgumentExceptionif this enum type has no constant with the specified name

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-join/values.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-join"
---
# values

fun values(): Array<MTLineJoin>Returns an array containing the constants of this enum type, in the order they're declared.This method may be used to iterate over the constants.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer/-m-t-line-layer.html

---
layout: mobile_sdk
title: "MTLineLayer"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTLineLayer"
id: -m-t-line-layer
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer"
---
# MTLineLayer

constructor(identifier: String, sourceIdentifier: String)constructor(identifier: String, sourceIdentifier: String, maxZoom: Double, minZoom: Double, sourceLayer: String)constructor(identifier: String, type: MTLayerType, sourceIdentifier: String, maxZoom: Double?, minZoom: Double?, sourceLayer: String?, blur: Double?, cap: MTLineCap?, color: Int?, dashArray: DoubleArray?, gapWidth: Double?, gradient: Int?, join: MTLineJoin?, miterLimit: Double?, offset: Double?, opacity: Double?, roundLimit: Double?, sortKey: Double?, translate: DoubleArray?, translateAnchor: MTLineTranslateAnchor?, width: Double?, visibility: MTLayerVisibility)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer/blur.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer"
---
# blur

var blur: Double?Blur of the line.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer/cap.html

---
layout: mobile_sdk
title: "cap"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "cap"
id: cap
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer"
---
# cap

var cap: MTLineCapThe display of line endings.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer/color.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer"
---
# color

@Serializable(with = ColorAsHexSerializer::class)var color: Int?The color with which the line will be drawn.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer/dash-array.html

---
layout: mobile_sdk
title: "dashArray"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "dashArray"
id: dash-array
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer"
---
# dashArray

var dashArray: DoubleArray?The lengths of the alternating dashes and gaps that form the dash pattern.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer/gap-width.html

---
layout: mobile_sdk
title: "gapWidth"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "gapWidth"
id: gap-width
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer"
---
# gapWidth

var gapWidth: Double?Line casing outside of a line’s actual path.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer/gradient.html

---
layout: mobile_sdk
title: "gradient"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "gradient"
id: gradient
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer"
---
# gradient

@Serializable(with = ColorAsHexSerializer::class)var gradient: Int?The gradient with which to color a line feature. Can only be used with GeoJSON sources that specify "lineMetrics": true.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer/identifier.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer"
---
# identifier

@SerialName(value = "id")open override var identifier: StringUnique layer identifier.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer/index.html

---
layout: mobile_sdk
title: "MTLineLayer"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTLineLayer"
id: -m-t-line-layer
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer"
---
# MTLineLayer

@Serializableclass MTLineLayer : MTLayer

Members

## Constructors

MTLineLayer

constructor(identifier: String, sourceIdentifier: String)constructor(identifier: String, sourceIdentifier: String, maxZoom: Double, minZoom: Double, sourceLayer: String)constructor(identifier: String, type: MTLayerType, sourceIdentifier: String, maxZoom: Double?, minZoom: Double?, sourceLayer: String?, blur: Double?, cap: MTLineCap?, color: Int?, dashArray: DoubleArray?, gapWidth: Double?, gradient: Int?, join: MTLineJoin?, miterLimit: Double?, offset: Double?, opacity: Double?, roundLimit: Double?, sortKey: Double?, translate: DoubleArray?, translateAnchor: MTLineTranslateAnchor?, width: Double?, visibility: MTLayerVisibility)

## Properties

blur

var blur: Double?Blur of the line.

cap

var cap: MTLineCapThe display of line endings.

color

@Serializable(with = ColorAsHexSerializer::class)var color: Int?The color with which the line will be drawn.

dashArray

var dashArray: DoubleArray?The lengths of the alternating dashes and gaps that form the dash pattern.

gapWidth

var gapWidth: Double?Line casing outside of a line’s actual path.

gradient

@Serializable(with = ColorAsHexSerializer::class)var gradient: Int?The gradient with which to color a line feature. Can only be used with GeoJSON sources that specify "lineMetrics": true.

identifier

@SerialName(value = "id")open override var identifier: StringUnique layer identifier.

join

var join: MTLineJoinThe display of lines when joining.

maxZoom

@SerialName(value = "maxzoom")open override var maxZoom: Double?The maximum zoom level for the layer.

minZoom

@SerialName(value = "minzoom")open override var minZoom: Double?The minimum zoom level for the layer.

miterLimit

var miterLimit: Double?Used to automatically convert miter joins to bevel joins for sharp angles. Requires join to be "miter".

offset

var offset: Double?The line’s offset.

opacity

var opacity: Double?Optional number between 0 and 1 inclusive.

roundLimit

var roundLimit: Double?Used to automatically convert round joins to miter joins for shallow angles.

sortKey

var sortKey: Double?Feature ordering value.

sourceIdentifier

@SerialName(value = "source")open override var sourceIdentifier: StringIdentifier of the source to be used for this layer.

sourceLayer

@SerialName(value = "source-layer")open override var sourceLayer: String?Layer to use from a vector tile source.

translate

var translate: DoubleArray?The geometry’s offset. Values are x, y.

translateAnchor

var translateAnchor: MTLineTranslateAnchor?Controls the frame of reference for translate.

type

open override var type: MTLayerTypeType of the layer.

visibility

var visibility: MTLayerVisibilityEnum controlling whether this layer is displayed.

width

var width: Double?Width of the line.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer/join.html

---
layout: mobile_sdk
title: "join"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "join"
id: join
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer"
---
# join

var join: MTLineJoinThe display of lines when joining.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer/max-zoom.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer"
---
# maxZoom

@SerialName(value = "maxzoom")open override var maxZoom: Double?The maximum zoom level for the layer.Optional number between 0 and 24. At zoom levels equal to or greater than the maxzoom, the layer will be hidden.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer/min-zoom.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer"
---
# minZoom

@SerialName(value = "minzoom")open override var minZoom: Double?The minimum zoom level for the layer.Optional number between 0 and 24. At zoom levels less than the minzoom, the layer will be hidden.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer/miter-limit.html

---
layout: mobile_sdk
title: "miterLimit"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "miterLimit"
id: miter-limit
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer"
---
# miterLimit

var miterLimit: Double?Used to automatically convert miter joins to bevel joins for sharp angles. Requires join to be "miter".

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer/offset.html

---
layout: mobile_sdk
title: "offset"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "offset"
id: offset
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer"
---
# offset

var offset: Double?The line’s offset.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer/opacity.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer"
---
# opacity

var opacity: Double?Optional number between 0 and 1 inclusive.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer/round-limit.html

---
layout: mobile_sdk
title: "roundLimit"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "roundLimit"
id: round-limit
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer"
---
# roundLimit

var roundLimit: Double?Used to automatically convert round joins to miter joins for shallow angles.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer/sort-key.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer"
---
# sortKey

var sortKey: Double?Feature ordering value.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer/source-identifier.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer"
---
# sourceIdentifier

@SerialName(value = "source")open override var sourceIdentifier: StringIdentifier of the source to be used for this layer.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer/source-layer.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer"
---
# sourceLayer

@SerialName(value = "source-layer")open override var sourceLayer: String?Layer to use from a vector tile source.Required for vector tile sources; prohibited for all other source types, including GeoJSON sources.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer/translate-anchor.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer"
---
# translateAnchor

var translateAnchor: MTLineTranslateAnchor?Controls the frame of reference for translate.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer/translate.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer"
---
# translate

var translate: DoubleArray?The geometry’s offset. Values are x, y.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer/type.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer"
---
# type

open override var type: MTLayerTypeType of the layer.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer/visibility.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer"
---
# visibility

var visibility: MTLayerVisibilityEnum controlling whether this layer is displayed.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer/width.html

---
layout: mobile_sdk
title: "width"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "width"
id: width
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-layer"
---
# width

var width: Double?Width of the line.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-translate-anchor/-m-a-p/index.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-translate-anchor/-m-a-p"
---
# MAP

@SerialName(value = "map")MAPThe line is translated relative to the map.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-translate-anchor/-v-i-e-w-p-o-r-t/index.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-translate-anchor/-v-i-e-w-p-o-r-t"
---
# VIEWPORT

@SerialName(value = "viewport")VIEWPORTThe line is translated relative to the viewport.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-translate-anchor/entries.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-translate-anchor"
---
# entries

val entries: EnumEntries<MTLineTranslateAnchor>Returns a representation of an immutable list of all enum entries, in the order they're declared.This method may be used to iterate over the enum entries.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-translate-anchor/index.html

---
layout: mobile_sdk
title: "MTLineTranslateAnchor"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTLineTranslateAnchor"
id: -m-t-line-translate-anchor
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-translate-anchor"
---
# MTLineTranslateAnchor

@Serializableenum MTLineTranslateAnchor : Enum<MTLineTranslateAnchor> Controls the frame of reference for line translate.

MembersEntries

## Entries

MAP

@SerialName(value = "map")MAPThe line is translated relative to the map.

VIEWPORT

@SerialName(value = "viewport")VIEWPORTThe line is translated relative to the viewport.

## Properties

entries

val entries: EnumEntries<MTLineTranslateAnchor>Returns a representation of an immutable list of all enum entries, in the order they're declared.

name

val name: String

ordinal

val ordinal: Int

## Functions

valueOf

fun valueOf(value: String): MTLineTranslateAnchorReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

values

fun values(): Array<MTLineTranslateAnchor>Returns an array containing the constants of this enum type, in the order they're declared.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-translate-anchor/value-of.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-translate-anchor"
---
# valueOf

fun valueOf(value: String): MTLineTranslateAnchorReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
#### Throws

IllegalArgumentExceptionif this enum type has no constant with the specified name

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-translate-anchor/values.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/-m-t-line-translate-anchor"
---
# values

fun values(): Array<MTLineTranslateAnchor>Returns an array containing the constants of this enum type, in the order they're declared.This method may be used to iterate over the constants.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line/index.html

---
layout: mobile_sdk
title: "com.maptiler.maptilersdk.map.style.layer.line"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "com.maptiler.maptilersdk.map.style.layer.line"
id: com.maptiler.maptilersdk.map.style.layer.line
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.line"
---
# com.maptiler.maptilersdk.map.style.layer.line

Types

## Types

MTLineCap

@Serializableenum MTLineCap : Enum<MTLineCap> The display of line endings.

MTLineJoin

@Serializableenum MTLineJoin : Enum<MTLineJoin> The display of lines when joining.

MTLineLayer

@Serializableclass MTLineLayer : MTLayer

MTLineTranslateAnchor

@Serializableenum MTLineTranslateAnchor : Enum<MTLineTranslateAnchor> Controls the frame of reference for line translate.

---

