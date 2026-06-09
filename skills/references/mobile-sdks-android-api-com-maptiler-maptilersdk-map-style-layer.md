# MapTiler Android SDK API Reference - com.maptiler.maptilersdk.map.style.layer

This document is a part of the Android SDK API reference documentation, covering the `com.maptiler.maptilersdk.map.style.layer` package.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer/identifier.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer"
---
# identifier

abstract var identifier: StringUnique id of the layer.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer/index.html

---
layout: mobile_sdk
title: "MTLayer"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTLayer"
id: -m-t-layer
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer"
---
# MTLayer

interface MTLayerProtocol requirements for all types of Layers.
#### Inheritors

MTBackgroundLayerMTCircleLayerMTFillLayerMTFillExtrusionLayerMTHeatmapLayerMTHillshadeLayerMTLineLayerMTRasterLayerMTSymbolLayer

Members

## Properties

identifier

abstract var identifier: StringUnique id of the layer.

maxZoom

abstract var maxZoom: Double?Max zoom of the layer.

minZoom

abstract var minZoom: Double?Min zoom of the layer.

sourceIdentifier

abstract var sourceIdentifier: StringIdentifier of the source.

sourceLayer

abstract var sourceLayer: String?Identifier of the source (main) layer to use.

type

abstract val type: MTLayerTypeType of the layer.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer/max-zoom.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer"
---
# maxZoom

abstract var maxZoom: Double?Max zoom of the layer.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer/min-zoom.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer"
---
# minZoom

abstract var minZoom: Double?Min zoom of the layer.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer/source-identifier.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer"
---
# sourceIdentifier

abstract var sourceIdentifier: StringIdentifier of the source.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer/source-layer.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer"
---
# sourceLayer

abstract var sourceLayer: String?Identifier of the source (main) layer to use.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer/type.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer"
---
# type

abstract val type: MTLayerTypeType of the layer.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-type/-b-a-c-k-g-r-o-u-n-d/index.html

---
layout: mobile_sdk
title: "BACKGROUND"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "BACKGROUND"
id: -b-a-c-k-g-r-o-u-n-d
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-type/-b-a-c-k-g-r-o-u-n-d"
---
# BACKGROUND

@SerialName(value = "background")BACKGROUNDThe background color or pattern of the map.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-type/-c-i-r-c-l-e/index.html

---
layout: mobile_sdk
title: "CIRCLE"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "CIRCLE"
id: -c-i-r-c-l-e
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-type/-c-i-r-c-l-e"
---
# CIRCLE

@SerialName(value = "circle")CIRCLEA filled circle.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-type/-f-i-l-l/index.html

---
layout: mobile_sdk
title: "FILL"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "FILL"
id: -f-i-l-l
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-type/-f-i-l-l"
---
# FILL

@SerialName(value = "fill")FILLA filled polygon with an optional stroked border.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-type/-f-i-l-l_-e-x-t-r-u-s-i-o-n/index.html

---
layout: mobile_sdk
title: "FILL_EXTRUSION"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "FILL_EXTRUSION"
id: -f-i-l-l_-e-x-t-r-u-s-i-o-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-type/-f-i-l-l_-e-x-t-r-u-s-i-o-n"
---
# FILL_EXTRUSION

@SerialName(value = "fill-extrusion")FILL_EXTRUSIONAn extruded (3D) polygon.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-type/-h-e-a-t-m-a-p/index.html

---
layout: mobile_sdk
title: "HEATMAP"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "HEATMAP"
id: -h-e-a-t-m-a-p
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-type/-h-e-a-t-m-a-p"
---
# HEATMAP

@SerialName(value = "heatmap")HEATMAPA heatmap.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-type/-h-i-l-l-s-h-a-d-e/index.html

---
layout: mobile_sdk
title: "HILLSHADE"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "HILLSHADE"
id: -h-i-l-l-s-h-a-d-e
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-type/-h-i-l-l-s-h-a-d-e"
---
# HILLSHADE

@SerialName(value = "hillshade")HILLSHADEClient-side hillshading visualization based on DEM data.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-type/-l-i-n-e/index.html

---
layout: mobile_sdk
title: "LINE"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "LINE"
id: -l-i-n-e
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-type/-l-i-n-e"
---
# LINE

@SerialName(value = "line")LINEA stroked line.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-type/-r-a-s-t-e-r/index.html

---
layout: mobile_sdk
title: "RASTER"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "RASTER"
id: -r-a-s-t-e-r
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-type/-r-a-s-t-e-r"
---
# RASTER

@SerialName(value = "raster")RASTERRaster map textures such as satellite imagery.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-type/-s-y-m-b-o-l/index.html

---
layout: mobile_sdk
title: "SYMBOL"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "SYMBOL"
id: -s-y-m-b-o-l
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-type/-s-y-m-b-o-l"
---
# SYMBOL

@SerialName(value = "symbol")SYMBOLAn icon or a text label.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-type/entries.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-type"
---
# entries

val entries: EnumEntries<MTLayerType>Returns a representation of an immutable list of all enum entries, in the order they're declared.This method may be used to iterate over the enum entries.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-type/index.html

---
layout: mobile_sdk
title: "MTLayerType"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTLayerType"
id: -m-t-layer-type
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-type"
---
# MTLayerType

@Serializableenum MTLayerType : Enum<MTLayerType> Types of layers.

MembersEntries

## Entries

FILL

@SerialName(value = "fill")FILLA filled polygon with an optional stroked border.

LINE

@SerialName(value = "line")LINEA stroked line.

SYMBOL

@SerialName(value = "symbol")SYMBOLAn icon or a text label.

RASTER

@SerialName(value = "raster")RASTERRaster map textures such as satellite imagery.

CIRCLE

@SerialName(value = "circle")CIRCLEA filled circle.

FILL_EXTRUSION

@SerialName(value = "fill-extrusion")FILL_EXTRUSIONAn extruded (3D) polygon.

HEATMAP

@SerialName(value = "heatmap")HEATMAPA heatmap.

HILLSHADE

@SerialName(value = "hillshade")HILLSHADEClient-side hillshading visualization based on DEM data.

BACKGROUND

@SerialName(value = "background")BACKGROUNDThe background color or pattern of the map.

## Properties

entries

val entries: EnumEntries<MTLayerType>Returns a representation of an immutable list of all enum entries, in the order they're declared.

name

val name: String

ordinal

val ordinal: Int

## Functions

valueOf

fun valueOf(value: String): MTLayerTypeReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

values

fun values(): Array<MTLayerType>Returns an array containing the constants of this enum type, in the order they're declared.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-type/value-of.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-type"
---
# valueOf

fun valueOf(value: String): MTLayerTypeReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
#### Throws

IllegalArgumentExceptionif this enum type has no constant with the specified name

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-type/values.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-type"
---
# values

fun values(): Array<MTLayerType>Returns an array containing the constants of this enum type, in the order they're declared.This method may be used to iterate over the constants.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-visibility/-companion/from.html

---
layout: mobile_sdk
title: "from"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "from"
id: from
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-visibility/-companion"
---
# from

fun from(value: MTLayerVisibility?): MTLayerVisibility?

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-visibility/-companion/index.html

---
layout: mobile_sdk
title: "Companion"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Companion"
id: -companion
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-visibility/-companion"
---
# Companion

object Companion

Members

## Functions

from

fun from(value: MTLayerVisibility?): MTLayerVisibility?

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-visibility/-n-o-n-e/index.html

---
layout: mobile_sdk
title: "NONE"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "NONE"
id: -n-o-n-e
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-visibility/-n-o-n-e"
---
# NONE

@SerialName(value = "none")NONELayer is not shown.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-visibility/-v-i-s-i-b-l-e/index.html

---
layout: mobile_sdk
title: "VISIBLE"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "VISIBLE"
id: -v-i-s-i-b-l-e
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-visibility/-v-i-s-i-b-l-e"
---
# VISIBLE

@SerialName(value = "visible")VISIBLELayer is shown.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-visibility/entries.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-visibility"
---
# entries

val entries: EnumEntries<MTLayerVisibility>Returns a representation of an immutable list of all enum entries, in the order they're declared.This method may be used to iterate over the enum entries.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-visibility/index.html

---
layout: mobile_sdk
title: "MTLayerVisibility"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTLayerVisibility"
id: -m-t-layer-visibility
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-visibility"
---
# MTLayerVisibility

@Serializableenum MTLayerVisibility : Enum<MTLayerVisibility> 

MembersEntries

## Entries

VISIBLE

@SerialName(value = "visible")VISIBLELayer is shown.

NONE

@SerialName(value = "none")NONELayer is not shown.

## Types

Companion

object Companion

## Properties

entries

val entries: EnumEntries<MTLayerVisibility>Returns a representation of an immutable list of all enum entries, in the order they're declared.

name

val name: String

ordinal

val ordinal: Int

## Functions

valueOf

fun valueOf(value: String): MTLayerVisibilityReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

values

fun values(): Array<MTLayerVisibility>Returns an array containing the constants of this enum type, in the order they're declared.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-visibility/value-of.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-visibility"
---
# valueOf

fun valueOf(value: String): MTLayerVisibilityReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
#### Throws

IllegalArgumentExceptionif this enum type has no constant with the specified name

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-visibility/values.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/-m-t-layer-visibility"
---
# values

fun values(): Array<MTLayerVisibility>Returns an array containing the constants of this enum type, in the order they're declared.This method may be used to iterate over the constants.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer/index.html

---
layout: mobile_sdk
title: "com.maptiler.maptilersdk.map.style.layer"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "com.maptiler.maptilersdk.map.style.layer"
id: com.maptiler.maptilersdk.map.style.layer
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer"
---
# com.maptiler.maptilersdk.map.style.layer

Types

## Types

MTLayer

interface MTLayerProtocol requirements for all types of Layers.

MTLayerType

@Serializableenum MTLayerType : Enum<MTLayerType> Types of layers.

MTLayerVisibility

@Serializableenum MTLayerVisibility : Enum<MTLayerVisibility>

---

