# MapTiler Android SDK API Reference - com.maptiler.maptilersdk.map.style.layer.background

This document is a part of the Android SDK API reference documentation, covering the `com.maptiler.maptilersdk.map.style.layer.background` package.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.background/-m-t-background-layer/-m-t-background-layer.html

---
layout: mobile_sdk
title: "MTBackgroundLayer"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTBackgroundLayer"
id: -m-t-background-layer
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.background/-m-t-background-layer"
---
# MTBackgroundLayer

constructor(identifier: String)constructor(identifier: String, type: MTLayerType, maxZoom: Double?, minZoom: Double?, color: Int?, opacity: Double?, pattern: String?, visibility: MTLayerVisibility)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.background/-m-t-background-layer/color.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.background/-m-t-background-layer"
---
# color

@Serializable(with = ColorAsHexSerializer::class)var color: Int?The color with which the background will be drawn. Defaults to black. Disabled by pattern.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.background/-m-t-background-layer/identifier.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.background/-m-t-background-layer"
---
# identifier

@SerialName(value = "id")open override var identifier: StringUnique layer identifier.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.background/-m-t-background-layer/index.html

---
layout: mobile_sdk
title: "MTBackgroundLayer"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTBackgroundLayer"
id: -m-t-background-layer
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.background/-m-t-background-layer"
---
# MTBackgroundLayer

@Serializableclass MTBackgroundLayer : MTLayerThe background style layer covers the entire map. Use it to configure a color or pattern rendered beneath all other map content. If the background layer is transparent or omitted, any area not covered by another layer is transparent.

Members

## Constructors

MTBackgroundLayer

constructor(identifier: String)constructor(identifier: String, type: MTLayerType, maxZoom: Double?, minZoom: Double?, color: Int?, opacity: Double?, pattern: String?, visibility: MTLayerVisibility)

## Properties

color

@Serializable(with = ColorAsHexSerializer::class)var color: Int?The color with which the background will be drawn. Defaults to black. Disabled by pattern.

identifier

@SerialName(value = "id")open override var identifier: StringUnique layer identifier.

maxZoom

@SerialName(value = "maxzoom")open override var maxZoom: Double?Max zoom of the layer.

minZoom

@SerialName(value = "minzoom")open override var minZoom: Double?Min zoom of the layer.

opacity

var opacity: Double?The opacity at which the background will be drawn. Optional number between 0 and 1 inclusive. Defaults to 1.

pattern

var pattern: String?Name of image in sprite to use for drawing an image background. For seamless patterns, image width and height must be a power of two.

sourceIdentifier

@Transientopen override var sourceIdentifier: StringBackground layers do not have a source. Kept only to satisfy MTLayer contract and excluded from serialization.

sourceLayer

@Transientopen override var sourceLayer: String?Source layer is not applicable for background layers. Excluded from serialization.

type

@EncodeDefault(mode = EncodeDefault.Mode.ALWAYS)open override var type: MTLayerTypeType of the layer. Always MTLayerType.BACKGROUND.

visibility

var visibility: MTLayerVisibilityWhether this layer is displayed.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.background/-m-t-background-layer/max-zoom.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.background/-m-t-background-layer"
---
# maxZoom

@SerialName(value = "maxzoom")open override var maxZoom: Double?Max zoom of the layer.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.background/-m-t-background-layer/min-zoom.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.background/-m-t-background-layer"
---
# minZoom

@SerialName(value = "minzoom")open override var minZoom: Double?Min zoom of the layer.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.background/-m-t-background-layer/opacity.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.background/-m-t-background-layer"
---
# opacity

var opacity: Double?The opacity at which the background will be drawn. Optional number between 0 and 1 inclusive. Defaults to 1.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.background/-m-t-background-layer/pattern.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.background/-m-t-background-layer"
---
# pattern

var pattern: String?Name of image in sprite to use for drawing an image background. For seamless patterns, image width and height must be a power of two.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.background/-m-t-background-layer/source-identifier.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.background/-m-t-background-layer"
---
# sourceIdentifier

@Transientopen override var sourceIdentifier: StringBackground layers do not have a source. Kept only to satisfy MTLayer contract and excluded from serialization.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.background/-m-t-background-layer/source-layer.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.background/-m-t-background-layer"
---
# sourceLayer

@Transientopen override var sourceLayer: String?Source layer is not applicable for background layers. Excluded from serialization.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.background/-m-t-background-layer/type.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.background/-m-t-background-layer"
---
# type

@EncodeDefault(mode = EncodeDefault.Mode.ALWAYS)open override var type: MTLayerTypeType of the layer. Always MTLayerType.BACKGROUND.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.background/-m-t-background-layer/visibility.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.background/-m-t-background-layer"
---
# visibility

var visibility: MTLayerVisibilityWhether this layer is displayed.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.background/index.html

---
layout: mobile_sdk
title: "com.maptiler.maptilersdk.map.style.layer.background"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "com.maptiler.maptilersdk.map.style.layer.background"
id: com.maptiler.maptilersdk.map.style.layer.background
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.layer.background"
---
# com.maptiler.maptilersdk.map.style.layer.background

Types

## Types

MTBackgroundLayer

@Serializableclass MTBackgroundLayer : MTLayerThe background style layer covers the entire map. Use it to configure a color or pattern rendered beneath all other map content. If the background layer is transparent or omitted, any area not covered by another layer is transparent.

---

