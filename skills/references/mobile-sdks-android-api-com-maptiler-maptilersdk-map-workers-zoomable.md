# MapTiler Android SDK API Reference - com.maptiler.maptilersdk.map.workers.zoomable

This document is a part of the Android SDK API reference documentation, covering the `com.maptiler.maptilersdk.map.workers.zoomable` package.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.zoomable/-m-t-zoomable/get-max-zoom.html

---
layout: mobile_sdk
title: "getMaxZoom"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "getMaxZoom"
id: get-max-zoom
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.zoomable/-m-t-zoomable"
---
# getMaxZoom

abstract suspend fun getMaxZoom(): DoubleReturns the map's maximum zoom level.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.zoomable/-m-t-zoomable/get-min-zoom.html

---
layout: mobile_sdk
title: "getMinZoom"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "getMinZoom"
id: get-min-zoom
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.zoomable/-m-t-zoomable"
---
# getMinZoom

abstract suspend fun getMinZoom(): DoubleReturns the map's minimum zoom level.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.zoomable/-m-t-zoomable/get-zoom.html

---
layout: mobile_sdk
title: "getZoom"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "getZoom"
id: get-zoom
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.zoomable/-m-t-zoomable"
---
# getZoom

abstract suspend fun getZoom(): DoubleReturns the map's current zoom level.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.zoomable/-m-t-zoomable/index.html

---
layout: mobile_sdk
title: "MTZoomable"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTZoomable"
id: -m-t-zoomable
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.zoomable/-m-t-zoomable"
---
# MTZoomable

interface MTZoomableDefines methods for manipulating zoom level.
#### Inheritors

MTMapViewController

Members

## Functions

getMaxZoom

abstract suspend fun getMaxZoom(): DoubleReturns the map's maximum zoom level.

getMinZoom

abstract suspend fun getMinZoom(): DoubleReturns the map's minimum zoom level.

getZoom

abstract suspend fun getZoom(): DoubleReturns the map's current zoom level.

setMaxZoom

abstract fun setMaxZoom(maxZoom: Double)Sets the map's maximum zoom level.

setMinZoom

abstract fun setMinZoom(minZoom: Double)Sets the map's minimum zoom level.

setZoom

abstract fun setZoom(zoom: Double)Sets the map's zoom level.

zoomIn

abstract fun zoomIn()Increases the map's zoom level by 1.

zoomOut

abstract fun zoomOut()Decreases the map's zoom level by 1.

zoomTo

abstract fun zoomTo(zoom: Double, options: MTAnimationOptions? = null)Zooms the map to the specified zoom level, with an optional animation.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.zoomable/-m-t-zoomable/set-max-zoom.html

---
layout: mobile_sdk
title: "setMaxZoom"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setMaxZoom"
id: set-max-zoom
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.zoomable/-m-t-zoomable"
---
# setMaxZoom

abstract fun setMaxZoom(maxZoom: Double)Sets the map's maximum zoom level.
#### Parameters

maxZoomThe max zoom level to set (0-20).

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.zoomable/-m-t-zoomable/set-min-zoom.html

---
layout: mobile_sdk
title: "setMinZoom"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setMinZoom"
id: set-min-zoom
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.zoomable/-m-t-zoomable"
---
# setMinZoom

abstract fun setMinZoom(minZoom: Double)Sets the map's minimum zoom level.
#### Parameters

minZoomThe min zoom level to set (0-20).

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.zoomable/-m-t-zoomable/set-zoom.html

---
layout: mobile_sdk
title: "setZoom"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setZoom"
id: set-zoom
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.zoomable/-m-t-zoomable"
---
# setZoom

abstract fun setZoom(zoom: Double)Sets the map's zoom level.
#### Parameters

zoomThe zoom level to set (0-20).

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.zoomable/-m-t-zoomable/zoom-in.html

---
layout: mobile_sdk
title: "zoomIn"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "zoomIn"
id: zoom-in
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.zoomable/-m-t-zoomable"
---
# zoomIn

abstract fun zoomIn()Increases the map's zoom level by 1.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.zoomable/-m-t-zoomable/zoom-out.html

---
layout: mobile_sdk
title: "zoomOut"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "zoomOut"
id: zoom-out
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.zoomable/-m-t-zoomable"
---
# zoomOut

abstract fun zoomOut()Decreases the map's zoom level by 1.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.zoomable/-m-t-zoomable/zoom-to.html

---
layout: mobile_sdk
title: "zoomTo"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "zoomTo"
id: zoom-to
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.zoomable/-m-t-zoomable"
---
# zoomTo

abstract fun zoomTo(zoom: Double, options: MTAnimationOptions? = null)Zooms the map to the specified zoom level, with an optional animation.
#### Parameters

zoomThe zoom level to transition to.optionsOptions object describing the destination and animation of the transition.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.zoomable/index.html

---
layout: mobile_sdk
title: "com.maptiler.maptilersdk.map.workers.zoomable"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "com.maptiler.maptilersdk.map.workers.zoomable"
id: com.maptiler.maptilersdk.map.workers.zoomable
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.zoomable"
---
# com.maptiler.maptilersdk.map.workers.zoomable

Types

## Types

MTZoomable

interface MTZoomableDefines methods for manipulating zoom level.

---

