# MapTiler Android SDK API Reference - com.maptiler.maptilersdk.map.style.layer.symbol

This document is a part of the Android SDK API reference documentation, covering the `com.maptiler.maptilersdk.map.style.layer.symbol` package.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer/-m-t-symbol-layer.html

---
layout: mobile_sdk
title: "MTSymbolLayer"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTSymbolLayer"
id: -m-t-symbol-layer
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer"
---
# MTSymbolLayer

constructor(identifier: String, sourceIdentifier: String)constructor(identifier: String, sourceIdentifier: String, icon: Bitmap)constructor(identifier: String, sourceIdentifier: String, maxZoom: Double, minZoom: Double, sourceLayer: String)constructor(identifier: String, sourceIdentifier: String, maxZoom: Double, minZoom: Double, sourceLayer: String, icon: Bitmap, visibility: MTLayerVisibility)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer/icon-allow-overlap.html

---
layout: mobile_sdk
title: "iconAllowOverlap"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "iconAllowOverlap"
id: icon-allow-overlap
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer"
---
# iconAllowOverlap

var iconAllowOverlap: Boolean?If true, the icon will be visible even if it collides with other symbols. Defaults to style spec default (false) when not set.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer/icon-ignore-placement.html

---
layout: mobile_sdk
title: "iconIgnorePlacement"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "iconIgnorePlacement"
id: icon-ignore-placement
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer"
---
# iconIgnorePlacement

var iconIgnorePlacement: Boolean?If true, the icon will be visible and will not affect placement of other symbols. Defaults to style spec default (false) when not set.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer/icon.html

---
layout: mobile_sdk
title: "icon"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "icon"
id: icon
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer"
---
# icon

@Transientvar icon: Bitmap?Icon to use for the layer.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer/identifier.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer"
---
# identifier

@SerialName(value = "id")open override var identifier: StringUnique layer identifier.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer/index.html

---
layout: mobile_sdk
title: "MTSymbolLayer"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTSymbolLayer"
id: -m-t-symbol-layer
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer"
---
# MTSymbolLayer

@Serializableclass MTSymbolLayer : MTLayerThe symbol style that layer renders icon and text labels at points or along lines on a map.

MembersMembers & Extensions

## Constructors

MTSymbolLayer

constructor(identifier: String, sourceIdentifier: String)constructor(identifier: String, sourceIdentifier: String, icon: Bitmap)constructor(identifier: String, sourceIdentifier: String, maxZoom: Double, minZoom: Double, sourceLayer: String)constructor(identifier: String, sourceIdentifier: String, maxZoom: Double, minZoom: Double, sourceLayer: String, icon: Bitmap, visibility: MTLayerVisibility)

## Properties

icon

@Transientvar icon: Bitmap?Icon to use for the layer.

iconAllowOverlap

var iconAllowOverlap: Boolean?If true, the icon will be visible even if it collides with other symbols. Defaults to style spec default (false) when not set.

iconIgnorePlacement

var iconIgnorePlacement: Boolean?If true, the icon will be visible and will not affect placement of other symbols. Defaults to style spec default (false) when not set.

identifier

@SerialName(value = "id")open override var identifier: StringUnique layer identifier.

maxZoom

@SerialName(value = "maxzoom")open override var maxZoom: Double?The maximum zoom level for the layer.

minZoom

@SerialName(value = "minzoom")open override var minZoom: Double?The minimum zoom level for the layer.

sourceIdentifier

@SerialName(value = "source")open override var sourceIdentifier: StringIdentifier of the source to be used for this layer.

sourceLayer

@SerialName(value = "source-layer")open override var sourceLayer: String?Layer to use from a vector tile source.

textAllowOverlap

var textAllowOverlap: Boolean?If true, the text will be visible even if it collides with other symbols. Defaults to style spec default (false) when not set.

textAnchor

var textAnchor: MTTextAnchor?Anchor position of the text relative to the symbol anchor. For example, use MTTextAnchor.TOP with a positive Y textOffset to render text below the icon.

textColor

var textColor: StyleValue?Text color (constant or expression), written under paint as text-color.

textField

var textField: String?Label text to render for each feature, e.g. "{point_count_abbreviated}" for clusters.

textFont

var textFont: List<String>?Text fonts as style-spec family names.

textIgnorePlacement

var textIgnorePlacement: Boolean?If true, the text will be visible and will not affect placement of other symbols. Defaults to style spec default (false) when not set.

textOffset

var textOffset: MTPoint?Amount to offset the text from its anchor in ems. X is right, Y is down. Example: 0.0, 1.2 with textAnchor = MTTextAnchor.TOP places text under the icon.

textSize

var textSize: Double?Label text size in pixels.

type

@EncodeDefault(mode = EncodeDefault.Mode.ALWAYS)open override var type: MTLayerTypeType of the layer.

visibility

var visibility: MTLayerVisibilityEnum controlling whether this layer is displayed.

## Functions

setFilterHas

fun setFilterHas(field: String)Sets filter to "has", field.

setFilterNotHas

fun setFilterNotHas(field: String)Sets filter to ["!", "has", field].

textAllowOverlap

fun MTSymbolLayer.textAllowOverlap(value: Boolean): MTSymbolLayer

textAnchor

fun MTSymbolLayer.textAnchor(value: MTTextAnchor): MTSymbolLayer

textColorConst

fun MTSymbolLayer.textColorConst(color: Int): MTSymbolLayer

textColorExpr

fun MTSymbolLayer.textColorExpr(expr: PropertyValue): MTSymbolLayer

textField

fun MTSymbolLayer.textField(token: MTTextToken): MTSymbolLayerfun MTSymbolLayer.textField(value: String): MTSymbolLayer

textFont

fun MTSymbolLayer.textFont(value: List<String>): MTSymbolLayer

textSize

fun MTSymbolLayer.textSize(value: Double): MTSymbolLayer

withFilter

fun withFilter(expr: PropertyValue)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer/max-zoom.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer"
---
# maxZoom

@SerialName(value = "maxzoom")open override var maxZoom: Double?The maximum zoom level for the layer.Optional number between 0 and 24. At zoom levels equal to or greater than the maxzoom, the layer will be hidden.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer/min-zoom.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer"
---
# minZoom

@SerialName(value = "minzoom")open override var minZoom: Double?The minimum zoom level for the layer.Optional number between 0 and 24. At zoom levels less than the minzoom, the layer will be hidden.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer/set-filter-has.html

---
layout: mobile_sdk
title: "setFilterHas"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setFilterHas"
id: set-filter-has
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer"
---
# setFilterHas

fun setFilterHas(field: String)Sets filter to "has", field.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer/set-filter-not-has.html

---
layout: mobile_sdk
title: "setFilterNotHas"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setFilterNotHas"
id: set-filter-not-has
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer"
---
# setFilterNotHas

fun setFilterNotHas(field: String)Sets filter to ["!", "has", field].

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer/source-identifier.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer"
---
# sourceIdentifier

@SerialName(value = "source")open override var sourceIdentifier: StringIdentifier of the source to be used for this layer.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer/source-layer.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer"
---
# sourceLayer

@SerialName(value = "source-layer")open override var sourceLayer: String?Layer to use from a vector tile source.Required for vector tile sources; prohibited for all other source types, including GeoJSON sources.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer/text-allow-overlap.html

---
layout: mobile_sdk
title: "textAllowOverlap"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "textAllowOverlap"
id: text-allow-overlap
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer"
---
# textAllowOverlap

var textAllowOverlap: Boolean?If true, the text will be visible even if it collides with other symbols. Defaults to style spec default (false) when not set.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer/text-anchor.html

---
layout: mobile_sdk
title: "textAnchor"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "textAnchor"
id: text-anchor
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer"
---
# textAnchor

var textAnchor: MTTextAnchor?Anchor position of the text relative to the symbol anchor. For example, use MTTextAnchor.TOP with a positive Y textOffset to render text below the icon.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer/text-color.html

---
layout: mobile_sdk
title: "textColor"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "textColor"
id: text-color
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer"
---
# textColor

var textColor: StyleValue?Text color (constant or expression), written under paint as text-color.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer/text-field.html

---
layout: mobile_sdk
title: "textField"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "textField"
id: text-field
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer"
---
# textField

var textField: String?Label text to render for each feature, e.g. "{point_count_abbreviated}" for clusters.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer/text-font.html

---
layout: mobile_sdk
title: "textFont"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "textFont"
id: text-font
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer"
---
# textFont

var textFont: List<String>?Text fonts as style-spec family names.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer/text-ignore-placement.html

---
layout: mobile_sdk
title: "textIgnorePlacement"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "textIgnorePlacement"
id: text-ignore-placement
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer"
---
# textIgnorePlacement

var textIgnorePlacement: Boolean?If true, the text will be visible and will not affect placement of other symbols. Defaults to style spec default (false) when not set.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer/text-offset.html

---
layout: mobile_sdk
title: "textOffset"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "textOffset"
id: text-offset
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer"
---
# textOffset

var textOffset: MTPoint?Amount to offset the text from its anchor in ems. X is right, Y is down. Example: 0.0, 1.2 with textAnchor = MTTextAnchor.TOP places text under the icon.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer/text-size.html

---
layout: mobile_sdk
title: "textSize"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "textSize"
id: text-size
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer"
---
# textSize

var textSize: Double?Label text size in pixels.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer/type.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer"
---
# type

@EncodeDefault(mode = EncodeDefault.Mode.ALWAYS)open override var type: MTLayerTypeType of the layer.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer/visibility.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer"
---
# visibility

var visibility: MTLayerVisibilityEnum controlling whether this layer is displayed.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer/with-filter.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-symbol-layer"
---
# withFilter

fun withFilter(expr: PropertyValue)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-text-anchor/-b-o-t-t-o-m/index.html

---
layout: mobile_sdk
title: "BOTTOM"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "BOTTOM"
id: -b-o-t-t-o-m
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-text-anchor/-b-o-t-t-o-m"
---
# BOTTOM

BOTTOM

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

value

val value: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-text-anchor/-b-o-t-t-o-m_-l-e-f-t/index.html

---
layout: mobile_sdk
title: "BOTTOM_LEFT"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "BOTTOM_LEFT"
id: -b-o-t-t-o-m_-l-e-f-t
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-text-anchor/-b-o-t-t-o-m_-l-e-f-t"
---
# BOTTOM_LEFT

BOTTOM_LEFT

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

value

val value: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-text-anchor/-b-o-t-t-o-m_-r-i-g-h-t/index.html

---
layout: mobile_sdk
title: "BOTTOM_RIGHT"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "BOTTOM_RIGHT"
id: -b-o-t-t-o-m_-r-i-g-h-t
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-text-anchor/-b-o-t-t-o-m_-r-i-g-h-t"
---
# BOTTOM_RIGHT

BOTTOM_RIGHT

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

value

val value: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-text-anchor/-c-e-n-t-e-r/index.html

---
layout: mobile_sdk
title: "CENTER"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "CENTER"
id: -c-e-n-t-e-r
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-text-anchor/-c-e-n-t-e-r"
---
# CENTER

CENTER

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

value

val value: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-text-anchor/-companion/from.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-text-anchor/-companion"
---
# from

fun from(raw: String): MTTextAnchor?

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-text-anchor/-companion/index.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-text-anchor/-companion"
---
# Companion

object Companion

Members

## Functions

from

fun from(raw: String): MTTextAnchor?

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-text-anchor/-l-e-f-t/index.html

---
layout: mobile_sdk
title: "LEFT"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "LEFT"
id: -l-e-f-t
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-text-anchor/-l-e-f-t"
---
# LEFT

LEFT

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

value

val value: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-text-anchor/-r-i-g-h-t/index.html

---
layout: mobile_sdk
title: "RIGHT"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "RIGHT"
id: -r-i-g-h-t
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-text-anchor/-r-i-g-h-t"
---
# RIGHT

RIGHT

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

value

val value: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-text-anchor/-t-o-p/index.html

---
layout: mobile_sdk
title: "TOP"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "TOP"
id: -t-o-p
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-text-anchor/-t-o-p"
---
# TOP

TOP

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

value

val value: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-text-anchor/-t-o-p_-l-e-f-t/index.html

---
layout: mobile_sdk
title: "TOP_LEFT"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "TOP_LEFT"
id: -t-o-p_-l-e-f-t
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-text-anchor/-t-o-p_-l-e-f-t"
---
# TOP_LEFT

TOP_LEFT

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

value

val value: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-text-anchor/-t-o-p_-r-i-g-h-t/index.html

---
layout: mobile_sdk
title: "TOP_RIGHT"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "TOP_RIGHT"
id: -t-o-p_-r-i-g-h-t
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-text-anchor/-t-o-p_-r-i-g-h-t"
---
# TOP_RIGHT

TOP_RIGHT

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

value

val value: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-text-anchor/entries.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-text-anchor"
---
# entries

val entries: EnumEntries<MTTextAnchor>Returns a representation of an immutable list of all enum entries, in the order they're declared.This method may be used to iterate over the enum entries.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-text-anchor/index.html

---
layout: mobile_sdk
title: "MTTextAnchor"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTTextAnchor"
id: -m-t-text-anchor
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-text-anchor"
---
# MTTextAnchor

enum MTTextAnchor : Enum<MTTextAnchor> Positions the text relative to the symbol anchor.

MembersEntries

## Entries

CENTER

CENTER

LEFT

LEFT

RIGHT

RIGHT

TOP

TOP

BOTTOM

BOTTOM

TOP_LEFT

TOP_LEFT

TOP_RIGHT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_LEFT

BOTTOM_RIGHT

BOTTOM_RIGHT

## Types

Companion

object Companion

## Properties

entries

val entries: EnumEntries<MTTextAnchor>Returns a representation of an immutable list of all enum entries, in the order they're declared.

name

val name: String

ordinal

val ordinal: Int

value

val value: String

## Functions

valueOf

fun valueOf(value: String): MTTextAnchorReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

values

fun values(): Array<MTTextAnchor>Returns an array containing the constants of this enum type, in the order they're declared.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-text-anchor/value-of.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-text-anchor"
---
# valueOf

fun valueOf(value: String): MTTextAnchorReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
#### Throws

IllegalArgumentExceptionif this enum type has no constant with the specified name

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-text-anchor/value.html

---
layout: mobile_sdk
title: "value"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "value"
id: value
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-text-anchor"
---
# value

val value: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-text-anchor/values.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/-m-t-text-anchor"
---
# values

fun values(): Array<MTTextAnchor>Returns an array containing the constants of this enum type, in the order they're declared.This method may be used to iterate over the constants.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/index.html

---
layout: mobile_sdk
title: "com.maptiler.maptilersdk.map.style.layer.symbol"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "com.maptiler.maptilersdk.map.style.layer.symbol"
id: com.maptiler.maptilersdk.map.style.layer.symbol
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol"
---
# com.maptiler.maptilersdk.map.style.layer.symbol

TypesFunctions

## Types

MTSymbolLayer

@Serializableclass MTSymbolLayer : MTLayerThe symbol style that layer renders icon and text labels at points or along lines on a map.

MTTextAnchor

enum MTTextAnchor : Enum<MTTextAnchor> Positions the text relative to the symbol anchor.

## Functions

textAllowOverlap

fun MTSymbolLayer.textAllowOverlap(value: Boolean): MTSymbolLayer

textAnchor

fun MTSymbolLayer.textAnchor(value: MTTextAnchor): MTSymbolLayer

textColorConst

fun MTSymbolLayer.textColorConst(color: Int): MTSymbolLayer

textColorExpr

fun MTSymbolLayer.textColorExpr(expr: PropertyValue): MTSymbolLayer

textField

fun MTSymbolLayer.textField(token: MTTextToken): MTSymbolLayerfun MTSymbolLayer.textField(value: String): MTSymbolLayer

textFont

fun MTSymbolLayer.textFont(value: List<String>): MTSymbolLayer

textSize

fun MTSymbolLayer.textSize(value: Double): MTSymbolLayer

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/text-allow-overlap.html

---
layout: mobile_sdk
title: "textAllowOverlap"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "textAllowOverlap"
id: text-allow-overlap
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol"
---
# textAllowOverlap

fun MTSymbolLayer.textAllowOverlap(value: Boolean): MTSymbolLayer

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/text-anchor.html

---
layout: mobile_sdk
title: "textAnchor"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "textAnchor"
id: text-anchor
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol"
---
# textAnchor

fun MTSymbolLayer.textAnchor(value: MTTextAnchor): MTSymbolLayer

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/text-color-const.html

---
layout: mobile_sdk
title: "textColorConst"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "textColorConst"
id: text-color-const
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol"
---
# textColorConst

fun MTSymbolLayer.textColorConst(color: Int): MTSymbolLayer

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/text-color-expr.html

---
layout: mobile_sdk
title: "textColorExpr"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "textColorExpr"
id: text-color-expr
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol"
---
# textColorExpr

fun MTSymbolLayer.textColorExpr(expr: PropertyValue): MTSymbolLayer

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/text-field.html

---
layout: mobile_sdk
title: "textField"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "textField"
id: text-field
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol"
---
# textField

fun MTSymbolLayer.textField(value: String): MTSymbolLayerfun MTSymbolLayer.textField(token: MTTextToken): MTSymbolLayer

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/text-font.html

---
layout: mobile_sdk
title: "textFont"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "textFont"
id: text-font
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol"
---
# textFont

fun MTSymbolLayer.textFont(value: List<String>): MTSymbolLayer

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol/text-size.html

---
layout: mobile_sdk
title: "textSize"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "textSize"
id: text-size
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.symbol"
---
# textSize

fun MTSymbolLayer.textSize(value: Double): MTSymbolLayer

---

