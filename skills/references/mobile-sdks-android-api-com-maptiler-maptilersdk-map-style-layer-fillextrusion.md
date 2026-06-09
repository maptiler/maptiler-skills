# MapTiler Android SDK API Reference - com.maptiler.maptilersdk.map.style.layer.fillextrusion

This document is a part of the Android SDK API reference documentation, covering the `com.maptiler.maptilersdk.map.style.layer.fillextrusion` package.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer/-m-t-fill-extrusion-layer.html

---
layout: mobile_sdk
title: "MTFillExtrusionLayer"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTFillExtrusionLayer"
id: -m-t-fill-extrusion-layer
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer"
---
# MTFillExtrusionLayer

constructor(identifier: String, sourceIdentifier: String)constructor(identifier: String, sourceIdentifier: String, maxZoom: Double, minZoom: Double, sourceLayer: String)constructor(identifier: String, type: MTLayerType, sourceIdentifier: String, maxZoom: Double?, minZoom: Double?, sourceLayer: String?, base: Double?, color: Int?, height: Double?, opacity: Double?, pattern: String?, translate: DoubleArray?, translateAnchor: MTFillExtrusionTranslateAnchor?, verticalGradient: Boolean?, visibility: MTLayerVisibility)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer/base-const.html

---
layout: mobile_sdk
title: "baseConst"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "baseConst"
id: base-const
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer"
---
# baseConst

fun baseConst(value: Double): MTFillExtrusionLayer

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer/base-expr.html

---
layout: mobile_sdk
title: "baseExpr"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "baseExpr"
id: base-expr
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer"
---
# baseExpr

fun baseExpr(expr: PropertyValue): MTFillExtrusionLayer

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer/base.html

---
layout: mobile_sdk
title: "base"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "base"
id: base
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer"
---
# base

var base: Double?The height with which to extrude the base of this layer. Units in meters. Must be ≤ height. Defaults to 0. Requires height.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer/color-const.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer"
---
# colorConst

fun colorConst(color: Int): MTFillExtrusionLayer

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer/color-expr.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer"
---
# colorExpr

fun colorExpr(expr: PropertyValue): MTFillExtrusionLayer

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer/color.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer"
---
# color

@Serializable(with = ColorAsHexSerializer::class)var color: Int?The base color of the extruded fill. Defaults to black. Note: If specified as rgba with alpha, alpha is ignored; use opacity.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer/height-const.html

---
layout: mobile_sdk
title: "heightConst"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "heightConst"
id: height-const
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer"
---
# heightConst

fun heightConst(value: Double): MTFillExtrusionLayer

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer/height-expr.html

---
layout: mobile_sdk
title: "heightExpr"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "heightExpr"
id: height-expr
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer"
---
# heightExpr

fun heightExpr(expr: PropertyValue): MTFillExtrusionLayer

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer/height.html

---
layout: mobile_sdk
title: "height"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "height"
id: height
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer"
---
# height

var height: Double?The height with which to extrude this layer. Units in meters. Defaults to 0.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer/identifier.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer"
---
# identifier

@SerialName(value = "id")open override var identifier: StringUnique layer identifier.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer/index.html

---
layout: mobile_sdk
title: "MTFillExtrusionLayer"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTFillExtrusionLayer"
id: -m-t-fill-extrusion-layer
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer"
---
# MTFillExtrusionLayer

@Serializableclass MTFillExtrusionLayer : MTLayerA fill-extrusion style layer renders one or more filled (and optionally stroked) extruded (3D) polygons on a map.You can use a fill-extrusion layer to configure the extrusion and visual appearance of polygon or multipolygon features.

Members

## Constructors

MTFillExtrusionLayer

constructor(identifier: String, sourceIdentifier: String)constructor(identifier: String, sourceIdentifier: String, maxZoom: Double, minZoom: Double, sourceLayer: String)constructor(identifier: String, type: MTLayerType, sourceIdentifier: String, maxZoom: Double?, minZoom: Double?, sourceLayer: String?, base: Double?, color: Int?, height: Double?, opacity: Double?, pattern: String?, translate: DoubleArray?, translateAnchor: MTFillExtrusionTranslateAnchor?, verticalGradient: Boolean?, visibility: MTLayerVisibility)

## Properties

base

var base: Double?The height with which to extrude the base of this layer. Units in meters. Must be ≤ height. Defaults to 0. Requires height.

color

@Serializable(with = ColorAsHexSerializer::class)var color: Int?The base color of the extruded fill. Defaults to black. Note: If specified as rgba with alpha, alpha is ignored; use opacity.

height

var height: Double?The height with which to extrude this layer. Units in meters. Defaults to 0.

identifier

@SerialName(value = "id")open override var identifier: StringUnique layer identifier.

maxZoom

@SerialName(value = "maxzoom")open override var maxZoom: Double?The maximum zoom level for the layer. Optional number between 0 and 24.

minZoom

@SerialName(value = "minzoom")open override var minZoom: Double?The minimum zoom level for the layer. Optional number between 0 and 24.

opacity

var opacity: Double?The opacity of the entire fill extrusion layer. Optional number between 0 and 1 inclusive. Defaults to 1.

pattern

var pattern: String?Name of image in sprite to use for drawing images on extruded fills.

sourceIdentifier

@SerialName(value = "source")open override var sourceIdentifier: StringIdentifier of the source to be used for this layer.

sourceLayer

@SerialName(value = "source-layer")open override var sourceLayer: String?Vector tile source layer name, if applicable. Required for vector tile sources.

translate

var translate: DoubleArray?The geometry’s offset. Units in pixels. Values are x, y where negatives indicate left and up, respectively. Defaults to 0,0.

translateAnchor

var translateAnchor: MTFillExtrusionTranslateAnchor?Controls the frame of reference for translate. Defaults to map.

type

open override var type: MTLayerTypeType of the layer.

verticalGradient

var verticalGradient: Boolean?Whether to apply a vertical gradient to the sides of a fill-extrusion layer. Defaults to true.

visibility

var visibility: MTLayerVisibilityWhether this layer is displayed.

## Functions

baseConst

fun baseConst(value: Double): MTFillExtrusionLayer

baseExpr

fun baseExpr(expr: PropertyValue): MTFillExtrusionLayer

colorConst

fun colorConst(color: Int): MTFillExtrusionLayer

colorExpr

fun colorExpr(expr: PropertyValue): MTFillExtrusionLayer

heightConst

fun heightConst(value: Double): MTFillExtrusionLayer

heightExpr

fun heightExpr(expr: PropertyValue): MTFillExtrusionLayer

opacityConst

fun opacityConst(value: Double): MTFillExtrusionLayer

opacityExpr

fun opacityExpr(expr: PropertyValue): MTFillExtrusionLayer

withFilter

fun withFilter(expr: PropertyValue)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer/max-zoom.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer"
---
# maxZoom

@SerialName(value = "maxzoom")open override var maxZoom: Double?The maximum zoom level for the layer. Optional number between 0 and 24.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer/min-zoom.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer"
---
# minZoom

@SerialName(value = "minzoom")open override var minZoom: Double?The minimum zoom level for the layer. Optional number between 0 and 24.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer/opacity-const.html

---
layout: mobile_sdk
title: "opacityConst"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "opacityConst"
id: opacity-const
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer"
---
# opacityConst

fun opacityConst(value: Double): MTFillExtrusionLayer

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer/opacity-expr.html

---
layout: mobile_sdk
title: "opacityExpr"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "opacityExpr"
id: opacity-expr
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer"
---
# opacityExpr

fun opacityExpr(expr: PropertyValue): MTFillExtrusionLayer

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer/opacity.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer"
---
# opacity

var opacity: Double?The opacity of the entire fill extrusion layer. Optional number between 0 and 1 inclusive. Defaults to 1.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer/pattern.html

---
layout: mobile_sdk
title: "pattern"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "pattern"
id: pattern
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer"
---
# pattern

var pattern: String?Name of image in sprite to use for drawing images on extruded fills.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer/source-identifier.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer"
---
# sourceIdentifier

@SerialName(value = "source")open override var sourceIdentifier: StringIdentifier of the source to be used for this layer.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer/source-layer.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer"
---
# sourceLayer

@SerialName(value = "source-layer")open override var sourceLayer: String?Vector tile source layer name, if applicable. Required for vector tile sources.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer/translate-anchor.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer"
---
# translateAnchor

var translateAnchor: MTFillExtrusionTranslateAnchor?Controls the frame of reference for translate. Defaults to map.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer/translate.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer"
---
# translate

var translate: DoubleArray?The geometry’s offset. Units in pixels. Values are x, y where negatives indicate left and up, respectively. Defaults to 0,0.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer/type.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer"
---
# type

open override var type: MTLayerTypeType of the layer.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer/vertical-gradient.html

---
layout: mobile_sdk
title: "verticalGradient"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "verticalGradient"
id: vertical-gradient
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer"
---
# verticalGradient

var verticalGradient: Boolean?Whether to apply a vertical gradient to the sides of a fill-extrusion layer. Defaults to true.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer/visibility.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer"
---
# visibility

var visibility: MTLayerVisibilityWhether this layer is displayed.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer/with-filter.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-layer"
---
# withFilter

fun withFilter(expr: PropertyValue)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-translate-anchor/-m-a-p/index.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-translate-anchor/-m-a-p"
---
# MAP

@SerialName(value = "map")MAPThe fill extrusion is translated relative to the map.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-translate-anchor/-v-i-e-w-p-o-r-t/index.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-translate-anchor/-v-i-e-w-p-o-r-t"
---
# VIEWPORT

@SerialName(value = "viewport")VIEWPORTThe fill extrusion is translated relative to the viewport.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-translate-anchor/entries.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-translate-anchor"
---
# entries

val entries: EnumEntries<MTFillExtrusionTranslateAnchor>Returns a representation of an immutable list of all enum entries, in the order they're declared.This method may be used to iterate over the enum entries.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-translate-anchor/index.html

---
layout: mobile_sdk
title: "MTFillExtrusionTranslateAnchor"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTFillExtrusionTranslateAnchor"
id: -m-t-fill-extrusion-translate-anchor
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-translate-anchor"
---
# MTFillExtrusionTranslateAnchor

@Serializableenum MTFillExtrusionTranslateAnchor : Enum<MTFillExtrusionTranslateAnchor> Enum controlling the frame of reference for fill-extrusion translate.

MembersEntries

## Entries

MAP

@SerialName(value = "map")MAPThe fill extrusion is translated relative to the map.

VIEWPORT

@SerialName(value = "viewport")VIEWPORTThe fill extrusion is translated relative to the viewport.

## Properties

entries

val entries: EnumEntries<MTFillExtrusionTranslateAnchor>Returns a representation of an immutable list of all enum entries, in the order they're declared.

name

val name: String

ordinal

val ordinal: Int

## Functions

valueOf

fun valueOf(value: String): MTFillExtrusionTranslateAnchorReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

values

fun values(): Array<MTFillExtrusionTranslateAnchor>Returns an array containing the constants of this enum type, in the order they're declared.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-translate-anchor/value-of.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-translate-anchor"
---
# valueOf

fun valueOf(value: String): MTFillExtrusionTranslateAnchorReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
#### Throws

IllegalArgumentExceptionif this enum type has no constant with the specified name

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-translate-anchor/values.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/-m-t-fill-extrusion-translate-anchor"
---
# values

fun values(): Array<MTFillExtrusionTranslateAnchor>Returns an array containing the constants of this enum type, in the order they're declared.This method may be used to iterate over the constants.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion/index.html

---
layout: mobile_sdk
title: "com.maptiler.maptilersdk.map.style.layer.fillextrusion"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "com.maptiler.maptilersdk.map.style.layer.fillextrusion"
id: com.maptiler.maptilersdk.map.style.layer.fillextrusion
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fillextrusion"
---
# com.maptiler.maptilersdk.map.style.layer.fillextrusion

Types

## Types

MTFillExtrusionLayer

@Serializableclass MTFillExtrusionLayer : MTLayerA fill-extrusion style layer renders one or more filled (and optionally stroked) extruded (3D) polygons on a map.

MTFillExtrusionTranslateAnchor

@Serializableenum MTFillExtrusionTranslateAnchor : Enum<MTFillExtrusionTranslateAnchor> Enum controlling the frame of reference for fill-extrusion translate.

---

