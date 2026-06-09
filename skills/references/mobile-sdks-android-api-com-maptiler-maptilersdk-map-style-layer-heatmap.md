# MapTiler Android SDK API Reference - com.maptiler.maptilersdk.map.style.layer.heatmap

This document is a part of the Android SDK API reference documentation, covering the `com.maptiler.maptilersdk.map.style.layer.heatmap` package.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/-m-t-heatmap-layer/-m-t-heatmap-layer.html

---
layout: mobile_sdk
title: "MTHeatmapLayer"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTHeatmapLayer"
id: -m-t-heatmap-layer
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/-m-t-heatmap-layer"
---
# MTHeatmapLayer

constructor(identifier: String, sourceIdentifier: String)constructor(identifier: String, sourceIdentifier: String, maxZoom: Double, minZoom: Double, sourceLayer: String)constructor(identifier: String, type: MTLayerType, sourceIdentifier: String, maxZoom: Double?, minZoom: Double?, sourceLayer: String?, color: StyleValue?, intensity: StyleValue?, opacity: StyleValue?, radius: StyleValue?, weight: StyleValue?, visibility: MTLayerVisibility)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/-m-t-heatmap-layer/color.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/-m-t-heatmap-layer"
---
# color

var color: StyleValue?Defines the color of each pixel based on its density value in a heatmap. Should be an expression that uses "heatmap-density" as input.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/-m-t-heatmap-layer/identifier.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/-m-t-heatmap-layer"
---
# identifier

@SerialName(value = "id")open override var identifier: StringUnique layer identifier.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/-m-t-heatmap-layer/index.html

---
layout: mobile_sdk
title: "MTHeatmapLayer"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTHeatmapLayer"
id: -m-t-heatmap-layer
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/-m-t-heatmap-layer"
---
# MTHeatmapLayer

@Serializableclass MTHeatmapLayer : MTLayerA heatmap style layer renders a range of colors to represent the density of points in an area.Supports color ramps and expressions for intensity, radius, opacity, and weight.

MembersMembers & Extensions

## Constructors

MTHeatmapLayer

constructor(identifier: String, sourceIdentifier: String)constructor(identifier: String, sourceIdentifier: String, maxZoom: Double, minZoom: Double, sourceLayer: String)constructor(identifier: String, type: MTLayerType, sourceIdentifier: String, maxZoom: Double?, minZoom: Double?, sourceLayer: String?, color: StyleValue?, intensity: StyleValue?, opacity: StyleValue?, radius: StyleValue?, weight: StyleValue?, visibility: MTLayerVisibility)

## Properties

color

var color: StyleValue?Defines the color of each pixel based on its density value in a heatmap. Should be an expression that uses "heatmap-density" as input.

identifier

@SerialName(value = "id")open override var identifier: StringUnique layer identifier.

intensity

var intensity: StyleValue?Similar to heatmap-weight but controls the intensity of the heatmap globally. Primarily used for adjusting the heatmap based on zoom level.

maxZoom

@SerialName(value = "maxzoom")open override var maxZoom: Double?The maximum zoom level for the layer.

minZoom

@SerialName(value = "minzoom")open override var minZoom: Double?The minimum zoom level for the layer.

opacity

var opacity: StyleValue?The global opacity at which the heatmap layer will be drawn.

radius

var radius: StyleValue?Radius of influence of one heatmap point in pixels. Increasing the value makes the heatmap smoother, but less detailed.

sourceIdentifier

@SerialName(value = "source")open override var sourceIdentifier: StringIdentifier of the source to be used for this layer.

sourceLayer

@SerialName(value = "source-layer")open override var sourceLayer: String?Vector tile source layer name, if applicable.

type

open override var type: MTLayerTypeType of the layer.

visibility

var visibility: MTLayerVisibilityWhether this layer is displayed.

weight

var weight: StyleValue?A measure of how much an individual point contributes to the heatmap.

## Functions

colorConst

fun MTHeatmapLayer.colorConst(color: Int): MTHeatmapLayer

colorExpr

fun MTHeatmapLayer.colorExpr(expr: PropertyValue): MTHeatmapLayer

intensityConst

fun MTHeatmapLayer.intensityConst(value: Double): MTHeatmapLayer

intensityExpr

fun MTHeatmapLayer.intensityExpr(expr: PropertyValue): MTHeatmapLayer

opacityConst

fun MTHeatmapLayer.opacityConst(value: Double): MTHeatmapLayer

opacityExpr

fun MTHeatmapLayer.opacityExpr(expr: PropertyValue): MTHeatmapLayer

radiusConst

fun MTHeatmapLayer.radiusConst(value: Double): MTHeatmapLayer

radiusExpr

fun MTHeatmapLayer.radiusExpr(expr: PropertyValue): MTHeatmapLayer

weightConst

fun MTHeatmapLayer.weightConst(value: Double): MTHeatmapLayer

weightExpr

fun MTHeatmapLayer.weightExpr(expr: PropertyValue): MTHeatmapLayer

withFilter

fun withFilter(expr: PropertyValue)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/-m-t-heatmap-layer/intensity.html

---
layout: mobile_sdk
title: "intensity"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "intensity"
id: intensity
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/-m-t-heatmap-layer"
---
# intensity

var intensity: StyleValue?Similar to heatmap-weight but controls the intensity of the heatmap globally. Primarily used for adjusting the heatmap based on zoom level.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/-m-t-heatmap-layer/max-zoom.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/-m-t-heatmap-layer"
---
# maxZoom

@SerialName(value = "maxzoom")open override var maxZoom: Double?The maximum zoom level for the layer.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/-m-t-heatmap-layer/min-zoom.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/-m-t-heatmap-layer"
---
# minZoom

@SerialName(value = "minzoom")open override var minZoom: Double?The minimum zoom level for the layer.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/-m-t-heatmap-layer/opacity.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/-m-t-heatmap-layer"
---
# opacity

var opacity: StyleValue?The global opacity at which the heatmap layer will be drawn.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/-m-t-heatmap-layer/radius.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/-m-t-heatmap-layer"
---
# radius

var radius: StyleValue?Radius of influence of one heatmap point in pixels. Increasing the value makes the heatmap smoother, but less detailed.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/-m-t-heatmap-layer/source-identifier.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/-m-t-heatmap-layer"
---
# sourceIdentifier

@SerialName(value = "source")open override var sourceIdentifier: StringIdentifier of the source to be used for this layer.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/-m-t-heatmap-layer/source-layer.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/-m-t-heatmap-layer"
---
# sourceLayer

@SerialName(value = "source-layer")open override var sourceLayer: String?Vector tile source layer name, if applicable.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/-m-t-heatmap-layer/type.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/-m-t-heatmap-layer"
---
# type

open override var type: MTLayerTypeType of the layer.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/-m-t-heatmap-layer/visibility.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/-m-t-heatmap-layer"
---
# visibility

var visibility: MTLayerVisibilityWhether this layer is displayed.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/-m-t-heatmap-layer/weight.html

---
layout: mobile_sdk
title: "weight"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "weight"
id: weight
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/-m-t-heatmap-layer"
---
# weight

var weight: StyleValue?A measure of how much an individual point contributes to the heatmap.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/-m-t-heatmap-layer/with-filter.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/-m-t-heatmap-layer"
---
# withFilter

fun withFilter(expr: PropertyValue)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/color-const.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap"
---
# colorConst

fun MTHeatmapLayer.colorConst(color: Int): MTHeatmapLayer

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/color-expr.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap"
---
# colorExpr

fun MTHeatmapLayer.colorExpr(expr: PropertyValue): MTHeatmapLayer

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/index.html

---
layout: mobile_sdk
title: "com.maptiler.maptilersdk.map.style.layer.heatmap"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "com.maptiler.maptilersdk.map.style.layer.heatmap"
id: com.maptiler.maptilersdk.map.style.layer.heatmap
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap"
---
# com.maptiler.maptilersdk.map.style.layer.heatmap

TypesFunctions

## Types

MTHeatmapLayer

@Serializableclass MTHeatmapLayer : MTLayerA heatmap style layer renders a range of colors to represent the density of points in an area.

## Functions

colorConst

fun MTHeatmapLayer.colorConst(color: Int): MTHeatmapLayer

colorExpr

fun MTHeatmapLayer.colorExpr(expr: PropertyValue): MTHeatmapLayer

intensityConst

fun MTHeatmapLayer.intensityConst(value: Double): MTHeatmapLayer

intensityExpr

fun MTHeatmapLayer.intensityExpr(expr: PropertyValue): MTHeatmapLayer

opacityConst

fun MTHeatmapLayer.opacityConst(value: Double): MTHeatmapLayer

opacityExpr

fun MTHeatmapLayer.opacityExpr(expr: PropertyValue): MTHeatmapLayer

radiusConst

fun MTHeatmapLayer.radiusConst(value: Double): MTHeatmapLayer

radiusExpr

fun MTHeatmapLayer.radiusExpr(expr: PropertyValue): MTHeatmapLayer

weightConst

fun MTHeatmapLayer.weightConst(value: Double): MTHeatmapLayer

weightExpr

fun MTHeatmapLayer.weightExpr(expr: PropertyValue): MTHeatmapLayer

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/intensity-const.html

---
layout: mobile_sdk
title: "intensityConst"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "intensityConst"
id: intensity-const
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap"
---
# intensityConst

fun MTHeatmapLayer.intensityConst(value: Double): MTHeatmapLayer

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/intensity-expr.html

---
layout: mobile_sdk
title: "intensityExpr"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "intensityExpr"
id: intensity-expr
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap"
---
# intensityExpr

fun MTHeatmapLayer.intensityExpr(expr: PropertyValue): MTHeatmapLayer

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/opacity-const.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap"
---
# opacityConst

fun MTHeatmapLayer.opacityConst(value: Double): MTHeatmapLayer

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/opacity-expr.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap"
---
# opacityExpr

fun MTHeatmapLayer.opacityExpr(expr: PropertyValue): MTHeatmapLayer

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/radius-const.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap"
---
# radiusConst

fun MTHeatmapLayer.radiusConst(value: Double): MTHeatmapLayer

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/radius-expr.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap"
---
# radiusExpr

fun MTHeatmapLayer.radiusExpr(expr: PropertyValue): MTHeatmapLayer

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/weight-const.html

---
layout: mobile_sdk
title: "weightConst"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "weightConst"
id: weight-const
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap"
---
# weightConst

fun MTHeatmapLayer.weightConst(value: Double): MTHeatmapLayer

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap/weight-expr.html

---
layout: mobile_sdk
title: "weightExpr"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "weightExpr"
id: weight-expr
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.heatmap"
---
# weightExpr

fun MTHeatmapLayer.weightExpr(expr: PropertyValue): MTHeatmapLayer

---

