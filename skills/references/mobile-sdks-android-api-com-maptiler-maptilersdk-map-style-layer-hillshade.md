# MapTiler Android SDK API Reference - com.maptiler.maptilersdk.map.style.layer.hillshade

This document is a part of the Android SDK API reference documentation, covering the `com.maptiler.maptilersdk.map.style.layer.hillshade` package.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-illumination-anchor/-m-a-p/index.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-illumination-anchor/-m-a-p"
---
# MAP

@SerialName(value = "map")MAP

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-illumination-anchor/-v-i-e-w-p-o-r-t/index.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-illumination-anchor/-v-i-e-w-p-o-r-t"
---
# VIEWPORT

@SerialName(value = "viewport")VIEWPORT

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-illumination-anchor/entries.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-illumination-anchor"
---
# entries

val entries: EnumEntries<MTHillshadeIlluminationAnchor>Returns a representation of an immutable list of all enum entries, in the order they're declared.This method may be used to iterate over the enum entries.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-illumination-anchor/index.html

---
layout: mobile_sdk
title: "MTHillshadeIlluminationAnchor"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTHillshadeIlluminationAnchor"
id: -m-t-hillshade-illumination-anchor
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-illumination-anchor"
---
# MTHillshadeIlluminationAnchor

@Serializableenum MTHillshadeIlluminationAnchor : Enum<MTHillshadeIlluminationAnchor> Direction frame for hillshade illumination when the map is rotated.- MAP: Illumination relative to north.
- VIEWPORT: Illumination relative to the top of the viewport.

MembersEntries

## Entries

MAP

@SerialName(value = "map")MAP

VIEWPORT

@SerialName(value = "viewport")VIEWPORT

## Properties

entries

val entries: EnumEntries<MTHillshadeIlluminationAnchor>Returns a representation of an immutable list of all enum entries, in the order they're declared.

name

val name: String

ordinal

val ordinal: Int

## Functions

valueOf

fun valueOf(value: String): MTHillshadeIlluminationAnchorReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

values

fun values(): Array<MTHillshadeIlluminationAnchor>Returns an array containing the constants of this enum type, in the order they're declared.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-illumination-anchor/value-of.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-illumination-anchor"
---
# valueOf

fun valueOf(value: String): MTHillshadeIlluminationAnchorReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
#### Throws

IllegalArgumentExceptionif this enum type has no constant with the specified name

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-illumination-anchor/values.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-illumination-anchor"
---
# values

fun values(): Array<MTHillshadeIlluminationAnchor>Returns an array containing the constants of this enum type, in the order they're declared.This method may be used to iterate over the constants.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-layer/-m-t-hillshade-layer.html

---
layout: mobile_sdk
title: "MTHillshadeLayer"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTHillshadeLayer"
id: -m-t-hillshade-layer
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-layer"
---
# MTHillshadeLayer

constructor(identifier: String, sourceIdentifier: String)constructor(identifier: String, sourceIdentifier: String, maxZoom: Double, minZoom: Double, sourceLayer: String)constructor(identifier: String, type: MTLayerType, sourceIdentifier: String, maxZoom: Double?, minZoom: Double?, sourceLayer: String?, accentColor: Int?, exaggeration: Double?, highlightColor: Int?, illuminationAnchor: MTHillshadeIlluminationAnchor?, illuminationDirection: Double?, shadowColor: Int?, visibility: MTLayerVisibility)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-layer/accent-color.html

---
layout: mobile_sdk
title: "accentColor"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "accentColor"
id: accent-color
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-layer"
---
# accentColor

@Serializable(with = ColorAsHexSerializer::class)var accentColor: Int?The shading color used to accentuate rugged terrain like sharp cliffs and gorges.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-layer/exaggeration.html

---
layout: mobile_sdk
title: "exaggeration"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "exaggeration"
id: exaggeration
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-layer"
---
# exaggeration

var exaggeration: Double?Intensity of the hillshade in 0, 1.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-layer/highlight-color.html

---
layout: mobile_sdk
title: "highlightColor"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "highlightColor"
id: highlight-color
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-layer"
---
# highlightColor

@Serializable(with = ColorAsHexSerializer::class)var highlightColor: Int?The shading color of areas that face towards the light source.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-layer/identifier.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-layer"
---
# identifier

@SerialName(value = "id")open override var identifier: StringUnique layer identifier.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-layer/illumination-anchor.html

---
layout: mobile_sdk
title: "illuminationAnchor"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "illuminationAnchor"
id: illumination-anchor
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-layer"
---
# illuminationAnchor

var illuminationAnchor: MTHillshadeIlluminationAnchor?Direction frame for illumination when map is rotated.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-layer/illumination-direction.html

---
layout: mobile_sdk
title: "illuminationDirection"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "illuminationDirection"
id: illumination-direction
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-layer"
---
# illuminationDirection

var illuminationDirection: Double?The direction of the light source (0..359).

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-layer/index.html

---
layout: mobile_sdk
title: "MTHillshadeLayer"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTHillshadeLayer"
id: -m-t-hillshade-layer
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-layer"
---
# MTHillshadeLayer

@Serializableclass MTHillshadeLayer : MTLayerA hillshade style layer renders digital elevation model (DEM) data on the client-side.Supports Terrain RGB and Mapzen Terrarium encodings via a `raster-dem` source.

Members

## Constructors

MTHillshadeLayer

constructor(identifier: String, sourceIdentifier: String)constructor(identifier: String, sourceIdentifier: String, maxZoom: Double, minZoom: Double, sourceLayer: String)constructor(identifier: String, type: MTLayerType, sourceIdentifier: String, maxZoom: Double?, minZoom: Double?, sourceLayer: String?, accentColor: Int?, exaggeration: Double?, highlightColor: Int?, illuminationAnchor: MTHillshadeIlluminationAnchor?, illuminationDirection: Double?, shadowColor: Int?, visibility: MTLayerVisibility)

## Properties

accentColor

@Serializable(with = ColorAsHexSerializer::class)var accentColor: Int?The shading color used to accentuate rugged terrain like sharp cliffs and gorges.

exaggeration

var exaggeration: Double?Intensity of the hillshade in 0, 1.

highlightColor

@Serializable(with = ColorAsHexSerializer::class)var highlightColor: Int?The shading color of areas that face towards the light source.

identifier

@SerialName(value = "id")open override var identifier: StringUnique layer identifier.

illuminationAnchor

var illuminationAnchor: MTHillshadeIlluminationAnchor?Direction frame for illumination when map is rotated.

illuminationDirection

var illuminationDirection: Double?The direction of the light source (0..359).

maxZoom

@SerialName(value = "maxzoom")open override var maxZoom: Double?The maximum zoom level for the layer.

minZoom

@SerialName(value = "minzoom")open override var minZoom: Double?The minimum zoom level for the layer.

shadowColor

@Serializable(with = ColorAsHexSerializer::class)var shadowColor: Int?The shading color of areas that face away from the light source.

sourceIdentifier

@SerialName(value = "source")open override var sourceIdentifier: StringIdentifier of the source to be used for this layer.

sourceLayer

@SerialName(value = "source-layer")open override var sourceLayer: String?Vector tile source layer name (not used for raster-dem).

type

open override var type: MTLayerTypeType of the layer.

visibility

var visibility: MTLayerVisibilityControls whether this layer is displayed.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-layer/max-zoom.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-layer"
---
# maxZoom

@SerialName(value = "maxzoom")open override var maxZoom: Double?The maximum zoom level for the layer.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-layer/min-zoom.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-layer"
---
# minZoom

@SerialName(value = "minzoom")open override var minZoom: Double?The minimum zoom level for the layer.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-layer/shadow-color.html

---
layout: mobile_sdk
title: "shadowColor"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "shadowColor"
id: shadow-color
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-layer"
---
# shadowColor

@Serializable(with = ColorAsHexSerializer::class)var shadowColor: Int?The shading color of areas that face away from the light source.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-layer/source-identifier.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-layer"
---
# sourceIdentifier

@SerialName(value = "source")open override var sourceIdentifier: StringIdentifier of the source to be used for this layer.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-layer/source-layer.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-layer"
---
# sourceLayer

@SerialName(value = "source-layer")open override var sourceLayer: String?Vector tile source layer name (not used for raster-dem).

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-layer/type.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-layer"
---
# type

open override var type: MTLayerTypeType of the layer.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-layer/visibility.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/-m-t-hillshade-layer"
---
# visibility

var visibility: MTLayerVisibilityControls whether this layer is displayed.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade/index.html

---
layout: mobile_sdk
title: "com.maptiler.maptilersdk.map.style.layer.hillshade"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "com.maptiler.maptilersdk.map.style.layer.hillshade"
id: com.maptiler.maptilersdk.map.style.layer.hillshade
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.hillshade"
---
# com.maptiler.maptilersdk.map.style.layer.hillshade

Types

## Types

MTHillshadeIlluminationAnchor

@Serializableenum MTHillshadeIlluminationAnchor : Enum<MTHillshadeIlluminationAnchor> Direction frame for hillshade illumination when the map is rotated.

MTHillshadeLayer

@Serializableclass MTHillshadeLayer : MTLayerA hillshade style layer renders digital elevation model (DEM) data on the client-side.

---

