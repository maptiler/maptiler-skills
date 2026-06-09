# MapTiler Android SDK API Reference - com.maptiler.maptilersdk.map.style.layer.fill

This document is a part of the Android SDK API reference documentation, covering the `com.maptiler.maptilersdk.map.style.layer.fill` package.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-color-as-hex-serializer/descriptor.html

---
layout: mobile_sdk
title: "descriptor"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "descriptor"
id: descriptor
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-color-as-hex-serializer"
---
# descriptor

open override val descriptor: SerialDescriptor

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-color-as-hex-serializer/deserialize.html

---
layout: mobile_sdk
title: "deserialize"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "deserialize"
id: deserialize
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-color-as-hex-serializer"
---
# deserialize

open override fun deserialize(decoder: Decoder): Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-color-as-hex-serializer/index.html

---
layout: mobile_sdk
title: "ColorAsHexSerializer"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ColorAsHexSerializer"
id: -color-as-hex-serializer
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-color-as-hex-serializer"
---
# ColorAsHexSerializer

@Serializer(forClass = Int::class)object ColorAsHexSerializer : KSerializer<Int> 

Members

## Properties

descriptor

open override val descriptor: SerialDescriptor

## Functions

deserialize

open override fun deserialize(decoder: Decoder): Int

serialize

open override fun serialize(encoder: Encoder, value: Int)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-color-as-hex-serializer/serialize.html

---
layout: mobile_sdk
title: "serialize"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "serialize"
id: serialize
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-color-as-hex-serializer"
---
# serialize

open override fun serialize(encoder: Encoder, value: Int)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-layer/-m-t-fill-layer.html

---
layout: mobile_sdk
title: "MTFillLayer"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTFillLayer"
id: -m-t-fill-layer
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-layer"
---
# MTFillLayer

constructor(identifier: String, sourceIdentifier: String, maxZoom: Double, minZoom: Double, sourceLayer: String)constructor(identifier: String, sourceIdentifier: String)constructor(identifier: String, type: MTLayerType, sourceIdentifier: String, maxZoom: Double?, minZoom: Double?, sourceLayer: String?, shouldBeAntialised: Boolean?, color: Int?, opacity: Double?, outlineColor: Int?, translate: DoubleArray?, translateAnchor: MTFillTranslateAnchor?, sortKey: Double?, visibility: MTLayerVisibility)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-layer/color.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-layer"
---
# color

@Serializable(with = ColorAsHexSerializer::class)var color: Int?The color of the filled part of this layer.Defaults to black.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-layer/identifier.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-layer"
---
# identifier

@SerialName(value = "id")open override var identifier: StringUnique layer identifier.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-layer/index.html

---
layout: mobile_sdk
title: "MTFillLayer"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTFillLayer"
id: -m-t-fill-layer
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-layer"
---
# MTFillLayer

@Serializableclass MTFillLayer : MTLayerThe fill style layer that renders one or more filled (and optionally stroked) polygons on a map.

Members

## Constructors

MTFillLayer

constructor(identifier: String, sourceIdentifier: String, maxZoom: Double, minZoom: Double, sourceLayer: String)constructor(identifier: String, sourceIdentifier: String)constructor(identifier: String, type: MTLayerType, sourceIdentifier: String, maxZoom: Double?, minZoom: Double?, sourceLayer: String?, shouldBeAntialised: Boolean?, color: Int?, opacity: Double?, outlineColor: Int?, translate: DoubleArray?, translateAnchor: MTFillTranslateAnchor?, sortKey: Double?, visibility: MTLayerVisibility)

## Properties

color

@Serializable(with = ColorAsHexSerializer::class)var color: Int?The color of the filled part of this layer.

identifier

@SerialName(value = "id")open override var identifier: StringUnique layer identifier.

maxZoom

@SerialName(value = "maxzoom")open override var maxZoom: Double?The maximum zoom level for the layer.

minZoom

@SerialName(value = "minzoom")open override var minZoom: Double?The minimum zoom level for the layer.

opacity

var opacity: Double?The opacity of the entire fill layer.

outlineColor

@Serializable(with = ColorAsHexSerializer::class)var outlineColor: Int?The outline color of the fill.

shouldBeAntialised

var shouldBeAntialised: Boolean?Boolean indicating whether or not the fill should be antialiased.

sortKey

var sortKey: Double?Key for sorting features.

sourceIdentifier

@SerialName(value = "source")open override var sourceIdentifier: StringIdentifier of the source to be used for this layer.

sourceLayer

@SerialName(value = "source-layer")open override var sourceLayer: String?Layer to use from a vector tile source.

translate

var translate: DoubleArray?The geometry’s offset.

translateAnchor

var translateAnchor: MTFillTranslateAnchor?Enum controlling the frame of reference for translate.

type

open override var type: MTLayerTypeType of the layer.

visibility

var visibility: MTLayerVisibilityEnum controlling whether this layer is displayed.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-layer/max-zoom.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-layer"
---
# maxZoom

@SerialName(value = "maxzoom")open override var maxZoom: Double?The maximum zoom level for the layer.Optional number between 0 and 24. At zoom levels equal to or greater than the maxzoom, the layer will be hidden.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-layer/min-zoom.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-layer"
---
# minZoom

@SerialName(value = "minzoom")open override var minZoom: Double?The minimum zoom level for the layer.Optional number between 0 and 24. At zoom levels less than the minzoom, the layer will be hidden.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-layer/opacity.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-layer"
---
# opacity

var opacity: Double?The opacity of the entire fill layer.Optional number between 0 and 1 inclusive. Defaults to 1.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-layer/outline-color.html

---
layout: mobile_sdk
title: "outlineColor"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "outlineColor"
id: outline-color
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-layer"
---
# outlineColor

@Serializable(with = ColorAsHexSerializer::class)var outlineColor: Int?The outline color of the fill.Matches the value of fill-color if unspecified.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-layer/should-be-antialised.html

---
layout: mobile_sdk
title: "shouldBeAntialised"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "shouldBeAntialised"
id: should-be-antialised
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-layer"
---
# shouldBeAntialised

var shouldBeAntialised: Boolean?Boolean indicating whether or not the fill should be antialiased.Defaults to true.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-layer/sort-key.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-layer"
---
# sortKey

var sortKey: Double?Key for sorting features.Features with a higher sort key will appear above features with a lower sort key.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-layer/source-identifier.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-layer"
---
# sourceIdentifier

@SerialName(value = "source")open override var sourceIdentifier: StringIdentifier of the source to be used for this layer.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-layer/source-layer.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-layer"
---
# sourceLayer

@SerialName(value = "source-layer")open override var sourceLayer: String?Layer to use from a vector tile source.Required for vector tile sources; prohibited for all other source types, including GeoJSON sources.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-layer/translate-anchor.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-layer"
---
# translateAnchor

var translateAnchor: MTFillTranslateAnchor?Enum controlling the frame of reference for translate.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-layer/translate.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-layer"
---
# translate

var translate: DoubleArray?The geometry’s offset.Units in pixels. Values are x, y where negatives indicate left and up, respectively. Defaults to 0,0.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-layer/type.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-layer"
---
# type

open override var type: MTLayerTypeType of the layer.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-layer/visibility.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-layer"
---
# visibility

var visibility: MTLayerVisibilityEnum controlling whether this layer is displayed.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-translate-anchor/-m-a-p/index.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-translate-anchor/-m-a-p"
---
# MAP

@SerialName(value = "map")MAPThe fill is translated relative to the map.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-translate-anchor/-v-i-e-w-p-o-r-t/index.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-translate-anchor/-v-i-e-w-p-o-r-t"
---
# VIEWPORT

@SerialName(value = "viewport")VIEWPORTThe fill is translated relative to the viewport.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-translate-anchor/entries.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-translate-anchor"
---
# entries

val entries: EnumEntries<MTFillTranslateAnchor>Returns a representation of an immutable list of all enum entries, in the order they're declared.This method may be used to iterate over the enum entries.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-translate-anchor/index.html

---
layout: mobile_sdk
title: "MTFillTranslateAnchor"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTFillTranslateAnchor"
id: -m-t-fill-translate-anchor
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-translate-anchor"
---
# MTFillTranslateAnchor

@Serializableenum MTFillTranslateAnchor : Enum<MTFillTranslateAnchor> Enum controlling the frame of reference for fill translate.

MembersEntries

## Entries

MAP

@SerialName(value = "map")MAPThe fill is translated relative to the map.

VIEWPORT

@SerialName(value = "viewport")VIEWPORTThe fill is translated relative to the viewport.

## Properties

entries

val entries: EnumEntries<MTFillTranslateAnchor>Returns a representation of an immutable list of all enum entries, in the order they're declared.

name

val name: String

ordinal

val ordinal: Int

## Functions

valueOf

fun valueOf(value: String): MTFillTranslateAnchorReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

values

fun values(): Array<MTFillTranslateAnchor>Returns an array containing the constants of this enum type, in the order they're declared.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-translate-anchor/value-of.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-translate-anchor"
---
# valueOf

fun valueOf(value: String): MTFillTranslateAnchorReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
#### Throws

IllegalArgumentExceptionif this enum type has no constant with the specified name

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-translate-anchor/values.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/-m-t-fill-translate-anchor"
---
# values

fun values(): Array<MTFillTranslateAnchor>Returns an array containing the constants of this enum type, in the order they're declared.This method may be used to iterate over the constants.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill/index.html

---
layout: mobile_sdk
title: "com.maptiler.maptilersdk.map.style.layer.fill"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "com.maptiler.maptilersdk.map.style.layer.fill"
id: com.maptiler.maptilersdk.map.style.layer.fill
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.fill"
---
# com.maptiler.maptilersdk.map.style.layer.fill

Types

## Types

ColorAsHexSerializer

@Serializer(forClass = Int::class)object ColorAsHexSerializer : KSerializer<Int> 

MTFillLayer

@Serializableclass MTFillLayer : MTLayerThe fill style layer that renders one or more filled (and optionally stroked) polygons on a map.

MTFillTranslateAnchor

@Serializableenum MTFillTranslateAnchor : Enum<MTFillTranslateAnchor> Enum controlling the frame of reference for fill translate.

---

