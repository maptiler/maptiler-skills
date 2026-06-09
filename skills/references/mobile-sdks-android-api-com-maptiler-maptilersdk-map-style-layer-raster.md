# MapTiler Android SDK API Reference - com.maptiler.maptilersdk.map.style.layer.raster

This document is a part of the Android SDK API reference documentation, covering the `com.maptiler.maptilersdk.map.style.layer.raster` package.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-layer/-m-t-raster-layer.html

---
layout: mobile_sdk
title: "MTRasterLayer"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTRasterLayer"
id: -m-t-raster-layer
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-layer"
---
# MTRasterLayer

constructor(identifier: String, sourceIdentifier: String)constructor(identifier: String, sourceIdentifier: String, maxZoom: Double, minZoom: Double, sourceLayer: String)constructor(identifier: String, type: MTLayerType, sourceIdentifier: String, maxZoom: Double?, minZoom: Double?, sourceLayer: String?, brightnessMax: Double?, brightnessMin: Double?, contrast: Double?, fadeDuration: Double?, hueRotate: Double?, opacity: Double?, resampling: MTRasterResampling?, saturation: Double?, visibility: MTLayerVisibility)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-layer/brightness-max.html

---
layout: mobile_sdk
title: "brightnessMax"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "brightnessMax"
id: brightness-max
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-layer"
---
# brightnessMax

var brightnessMax: Double?Increase or reduce the brightness of the image. The value is the maximum brightness. Optional number between 0 and 1 inclusive. Defaults to 1.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-layer/brightness-min.html

---
layout: mobile_sdk
title: "brightnessMin"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "brightnessMin"
id: brightness-min
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-layer"
---
# brightnessMin

var brightnessMin: Double?Increase or reduce the brightness of the image. The value is the minimum brightness. Optional number between 0 and 1 inclusive. Defaults to 0.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-layer/contrast.html

---
layout: mobile_sdk
title: "contrast"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "contrast"
id: contrast
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-layer"
---
# contrast

var contrast: Double?Increase or reduce the contrast of the image. Optional number between -1 and 1 inclusive. Defaults to 0.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-layer/fade-duration.html

---
layout: mobile_sdk
title: "fadeDuration"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "fadeDuration"
id: fade-duration
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-layer"
---
# fadeDuration

var fadeDuration: Double?Fade duration when a new tile is added. Optional number greater than or equal to 0. Units in milliseconds. Defaults to 300.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-layer/hue-rotate.html

---
layout: mobile_sdk
title: "hueRotate"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "hueRotate"
id: hue-rotate
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-layer"
---
# hueRotate

var hueRotate: Double?Rotates hues around the color wheel. Units in degrees. Defaults to 0.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-layer/identifier.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-layer"
---
# identifier

@SerialName(value = "id")open override var identifier: StringUnique layer identifier.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-layer/index.html

---
layout: mobile_sdk
title: "MTRasterLayer"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTRasterLayer"
id: -m-t-raster-layer
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-layer"
---
# MTRasterLayer

@Serializableclass MTRasterLayer : MTLayerThe raster style layer that renders raster map textures such as satellite imagery.Supports paint properties like brightness, contrast, fade duration, hue rotation, opacity, resampling and saturation, and a layout visibility flag.

Members

## Constructors

MTRasterLayer

constructor(identifier: String, sourceIdentifier: String)constructor(identifier: String, sourceIdentifier: String, maxZoom: Double, minZoom: Double, sourceLayer: String)constructor(identifier: String, type: MTLayerType, sourceIdentifier: String, maxZoom: Double?, minZoom: Double?, sourceLayer: String?, brightnessMax: Double?, brightnessMin: Double?, contrast: Double?, fadeDuration: Double?, hueRotate: Double?, opacity: Double?, resampling: MTRasterResampling?, saturation: Double?, visibility: MTLayerVisibility)

## Properties

brightnessMax

var brightnessMax: Double?Increase or reduce the brightness of the image. The value is the maximum brightness. Optional number between 0 and 1 inclusive. Defaults to 1.

brightnessMin

var brightnessMin: Double?Increase or reduce the brightness of the image. The value is the minimum brightness. Optional number between 0 and 1 inclusive. Defaults to 0.

contrast

var contrast: Double?Increase or reduce the contrast of the image. Optional number between -1 and 1 inclusive. Defaults to 0.

fadeDuration

var fadeDuration: Double?Fade duration when a new tile is added. Optional number greater than or equal to 0. Units in milliseconds. Defaults to 300.

hueRotate

var hueRotate: Double?Rotates hues around the color wheel. Units in degrees. Defaults to 0.

identifier

@SerialName(value = "id")open override var identifier: StringUnique layer identifier.

maxZoom

@SerialName(value = "maxzoom")open override var maxZoom: Double?The maximum zoom level for the layer. Optional number between 0 and 24. At zoom levels equal to or greater than the maxzoom, the layer will be hidden.

minZoom

@SerialName(value = "minzoom")open override var minZoom: Double?The minimum zoom level for the layer. Optional number between 0 and 24. At zoom levels less than the minzoom, the layer will be hidden.

opacity

var opacity: Double?The opacity at which the image will be drawn. Optional number between 0 and 1 inclusive. Defaults to 1.

resampling

var resampling: MTRasterResampling?The resampling/interpolation method to use for overscaling. Defaults to LINEAR.

saturation

var saturation: Double?Increase or reduce the saturation of the image. Optional number between -1 and 1 inclusive. Defaults to 0.

sourceIdentifier

@SerialName(value = "source")open override var sourceIdentifier: StringIdentifier of the source to be used for this layer.

sourceLayer

@SerialName(value = "source-layer")open override var sourceLayer: String?Layer to use from a vector tile source. Not used for raster sources.

type

open override var type: MTLayerTypeType of the layer.

visibility

var visibility: MTLayerVisibilityEnum controlling whether this layer is displayed.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-layer/max-zoom.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-layer"
---
# maxZoom

@SerialName(value = "maxzoom")open override var maxZoom: Double?The maximum zoom level for the layer. Optional number between 0 and 24. At zoom levels equal to or greater than the maxzoom, the layer will be hidden.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-layer/min-zoom.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-layer"
---
# minZoom

@SerialName(value = "minzoom")open override var minZoom: Double?The minimum zoom level for the layer. Optional number between 0 and 24. At zoom levels less than the minzoom, the layer will be hidden.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-layer/opacity.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-layer"
---
# opacity

var opacity: Double?The opacity at which the image will be drawn. Optional number between 0 and 1 inclusive. Defaults to 1.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-layer/resampling.html

---
layout: mobile_sdk
title: "resampling"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "resampling"
id: resampling
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-layer"
---
# resampling

var resampling: MTRasterResampling?The resampling/interpolation method to use for overscaling. Defaults to LINEAR.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-layer/saturation.html

---
layout: mobile_sdk
title: "saturation"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "saturation"
id: saturation
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-layer"
---
# saturation

var saturation: Double?Increase or reduce the saturation of the image. Optional number between -1 and 1 inclusive. Defaults to 0.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-layer/source-identifier.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-layer"
---
# sourceIdentifier

@SerialName(value = "source")open override var sourceIdentifier: StringIdentifier of the source to be used for this layer.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-layer/source-layer.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-layer"
---
# sourceLayer

@SerialName(value = "source-layer")open override var sourceLayer: String?Layer to use from a vector tile source. Not used for raster sources.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-layer/type.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-layer"
---
# type

open override var type: MTLayerTypeType of the layer.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-layer/visibility.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-layer"
---
# visibility

var visibility: MTLayerVisibilityEnum controlling whether this layer is displayed.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-resampling/-l-i-n-e-a-r/index.html

---
layout: mobile_sdk
title: "LINEAR"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "LINEAR"
id: -l-i-n-e-a-r
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-resampling/-l-i-n-e-a-r"
---
# LINEAR

@SerialName(value = "linear")LINEAR

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-resampling/-n-e-a-r-e-s-t/index.html

---
layout: mobile_sdk
title: "NEAREST"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "NEAREST"
id: -n-e-a-r-e-s-t
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-resampling/-n-e-a-r-e-s-t"
---
# NEAREST

@SerialName(value = "nearest")NEAREST

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-resampling/entries.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-resampling"
---
# entries

val entries: EnumEntries<MTRasterResampling>Returns a representation of an immutable list of all enum entries, in the order they're declared.This method may be used to iterate over the enum entries.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-resampling/index.html

---
layout: mobile_sdk
title: "MTRasterResampling"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTRasterResampling"
id: -m-t-raster-resampling
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-resampling"
---
# MTRasterResampling

@Serializableenum MTRasterResampling : Enum<MTRasterResampling> The resampling/interpolation method to use for overscaling, also known as texture magnification filter.

MembersEntries

## Entries

LINEAR

@SerialName(value = "linear")LINEAR

NEAREST

@SerialName(value = "nearest")NEAREST

## Properties

entries

val entries: EnumEntries<MTRasterResampling>Returns a representation of an immutable list of all enum entries, in the order they're declared.

name

val name: String

ordinal

val ordinal: Int

## Functions

valueOf

fun valueOf(value: String): MTRasterResamplingReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

values

fun values(): Array<MTRasterResampling>Returns an array containing the constants of this enum type, in the order they're declared.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-resampling/value-of.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-resampling"
---
# valueOf

fun valueOf(value: String): MTRasterResamplingReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
#### Throws

IllegalArgumentExceptionif this enum type has no constant with the specified name

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-resampling/values.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/-m-t-raster-resampling"
---
# values

fun values(): Array<MTRasterResampling>Returns an array containing the constants of this enum type, in the order they're declared.This method may be used to iterate over the constants.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster/index.html

---
layout: mobile_sdk
title: "com.maptiler.maptilersdk.map.style.layer.raster"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "com.maptiler.maptilersdk.map.style.layer.raster"
id: com.maptiler.maptilersdk.map.style.layer.raster
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.raster"
---
# com.maptiler.maptilersdk.map.style.layer.raster

Types

## Types

MTRasterLayer

@Serializableclass MTRasterLayer : MTLayerThe raster style layer that renders raster map textures such as satellite imagery.

MTRasterResampling

@Serializableenum MTRasterResampling : Enum<MTRasterResampling> The resampling/interpolation method to use for overscaling, also known as texture magnification filter.

---

