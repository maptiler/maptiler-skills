# MapTiler Android SDK API Reference - com.maptiler.maptilersdk.map.options

This document is a part of the Android SDK API reference documentation, covering the `com.maptiler.maptilersdk.map.options` package.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-animation-options/-m-t-animation-options.html

---
layout: mobile_sdk
title: "MTAnimationOptions"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTAnimationOptions"
id: -m-t-animation-options
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-animation-options"
---
# MTAnimationOptions

constructor(duration: Double? = null, animate: Boolean? = null, essential: Boolean? = null, offset: MTPoint? = null)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-animation-options/animate.html

---
layout: mobile_sdk
title: "animate"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "animate"
id: animate
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-animation-options"
---
# animate

val animate: Boolean? = nullIf false, no animation will occur.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-animation-options/duration.html

---
layout: mobile_sdk
title: "duration"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "duration"
id: duration
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-animation-options"
---
# duration

val duration: Double? = nullThe animation's duration, measured in milliseconds.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-animation-options/essential.html

---
layout: mobile_sdk
title: "essential"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "essential"
id: essential
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-animation-options"
---
# essential

val essential: Boolean? = nullIf true, then the animation is considered essential and will not be affected by prefers-reduced-motion.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-animation-options/index.html

---
layout: mobile_sdk
title: "MTAnimationOptions"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTAnimationOptions"
id: -m-t-animation-options
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-animation-options"
---
# MTAnimationOptions

@Serializabledata class MTAnimationOptions(val duration: Double? = null, val animate: Boolean? = null, val essential: Boolean? = null, val offset: MTPoint? = null)Options describing the animation of the transition.

Members

## Constructors

MTAnimationOptions

constructor(duration: Double? = null, animate: Boolean? = null, essential: Boolean? = null, offset: MTPoint? = null)

## Properties

animate

val animate: Boolean? = nullIf false, no animation will occur.

duration

val duration: Double? = nullThe animation's duration, measured in milliseconds.

essential

val essential: Boolean? = nullIf true, then the animation is considered essential and will not be affected by prefers-reduced-motion.

offset

val offset: MTPoint? = nullThe center of the given bounds relative to the map's center, measured in pixels.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-animation-options/offset.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-animation-options"
---
# offset

val offset: MTPoint? = nullThe center of the given bounds relative to the map's center, measured in pixels.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-camera-options/-m-t-camera-options.html

---
layout: mobile_sdk
title: "MTCameraOptions"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTCameraOptions"
id: -m-t-camera-options
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-camera-options"
---
# MTCameraOptions

constructor(center: LngLat, zoom: Double? = null, bearing: Double? = null, pitch: Double? = null)Initializes camera options with center, zoom, bearing and pitch.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-camera-options/bearing.html

---
layout: mobile_sdk
title: "bearing"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "bearing"
id: bearing
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-camera-options"
---
# bearing

var bearing: Double?The bearing of the map, measured in degrees counter-clockwise from north.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-camera-options/center.html

---
layout: mobile_sdk
title: "center"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "center"
id: center
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-camera-options"
---
# center

var center: LngLatGeographical center of the map.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-camera-options/index.html

---
layout: mobile_sdk
title: "MTCameraOptions"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTCameraOptions"
id: -m-t-camera-options
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-camera-options"
---
# MTCameraOptions

@Serializableclass MTCameraOptionsOptions for controlling the desired location, zoom, bearing, and pitch of the camera.

Members

## Constructors

MTCameraOptions

constructor(center: LngLat, zoom: Double? = null, bearing: Double? = null, pitch: Double? = null)Initializes camera options with center, zoom, bearing and pitch.

## Properties

bearing

var bearing: Double?The bearing of the map, measured in degrees counter-clockwise from north.

center

var center: LngLatGeographical center of the map.

pitch

var pitch: Double?The pitch (tilt) of the map, measured in degrees away from the plane of the screen (0-85).

zoom

var zoom: Double?Zoom level of the map.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-camera-options/pitch.html

---
layout: mobile_sdk
title: "pitch"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "pitch"
id: pitch
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-camera-options"
---
# pitch

var pitch: Double?The pitch (tilt) of the map, measured in degrees away from the plane of the screen (0-85).

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-camera-options/zoom.html

---
layout: mobile_sdk
title: "zoom"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "zoom"
id: zoom
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-camera-options"
---
# zoom

var zoom: Double?Zoom level of the map.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-drag-pan-options/-m-t-drag-pan-options.html

---
layout: mobile_sdk
title: "MTDragPanOptions"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTDragPanOptions"
id: -m-t-drag-pan-options
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-drag-pan-options"
---
# MTDragPanOptions

constructor(linearity: Double? = null, maxSpeed: Double? = null, deceleration: Double? = null)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-drag-pan-options/deceleration.html

---
layout: mobile_sdk
title: "deceleration"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "deceleration"
id: deceleration
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-drag-pan-options"
---
# deceleration

val deceleration: Double? = nullThe rate at which the speed reduces after the pan ends.Default: 2500

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-drag-pan-options/index.html

---
layout: mobile_sdk
title: "MTDragPanOptions"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTDragPanOptions"
id: -m-t-drag-pan-options
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-drag-pan-options"
---
# MTDragPanOptions

@Serializabledata class MTDragPanOptions(val linearity: Double? = null, val maxSpeed: Double? = null, val deceleration: Double? = null)

Members

## Constructors

MTDragPanOptions

constructor(linearity: Double? = null, maxSpeed: Double? = null, deceleration: Double? = null)

## Properties

deceleration

val deceleration: Double? = nullThe rate at which the speed reduces after the pan ends.

linearity

val linearity: Double? = nullFactor used to scale the drag velocity.

maxSpeed

val maxSpeed: Double? = nullThe maximum value of the drag velocity.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-drag-pan-options/linearity.html

---
layout: mobile_sdk
title: "linearity"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "linearity"
id: linearity
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-drag-pan-options"
---
# linearity

val linearity: Double? = nullFactor used to scale the drag velocity.Default: 0.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-drag-pan-options/max-speed.html

---
layout: mobile_sdk
title: "maxSpeed"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "maxSpeed"
id: max-speed
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-drag-pan-options"
---
# maxSpeed

val maxSpeed: Double? = nullThe maximum value of the drag velocity.Default: 1400

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-event-level/-a-l-l/index.html

---
layout: mobile_sdk
title: "ALL"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ALL"
id: -a-l-l
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-event-level/-a-l-l"
---
# ALL

ALL

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-event-level/-c-a-m-e-r-a_-o-n-l-y/index.html

---
layout: mobile_sdk
title: "CAMERA_ONLY"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "CAMERA_ONLY"
id: -c-a-m-e-r-a_-o-n-l-y
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-event-level/-c-a-m-e-r-a_-o-n-l-y"
---
# CAMERA_ONLY

CAMERA_ONLYForwards only camera motion events (move, zoom) plus minimal lifecycle (ready/load is implicit). Use this to support overlays that track camera without wiring all touch/render events.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-event-level/-e-s-s-e-n-t-i-a-l/index.html

---
layout: mobile_sdk
title: "ESSENTIAL"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ESSENTIAL"
id: -e-s-s-e-n-t-i-a-l
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-event-level/-e-s-s-e-n-t-i-a-l"
---
# ESSENTIAL

ESSENTIAL

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-event-level/-o-f-f/index.html

---
layout: mobile_sdk
title: "OFF"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "OFF"
id: -o-f-f
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-event-level/-o-f-f"
---
# OFF

OFF

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-event-level/entries.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-event-level"
---
# entries

val entries: EnumEntries<MTEventLevel>Returns a representation of an immutable list of all enum entries, in the order they're declared.This method may be used to iterate over the enum entries.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-event-level/index.html

---
layout: mobile_sdk
title: "MTEventLevel"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTEventLevel"
id: -m-t-event-level
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-event-level"
---
# MTEventLevel

enum MTEventLevel : Enum<MTEventLevel> Controls which map events are forwarded from the map object.- ESSENTIAL: Low-frequency lifecycle events only (ready, load, moveend, etc.) plus taps.
- CAMERA_ONLY: Forwards only camera events (move, zoom) in addition to minimal lifecycle.
- ALL: Default. Forwards all events including high-frequency move/zoom/touch/render (use with caution on low-end devices).
- OFF: Minimal wiring to keep internal lifecycle (ready/load) functioning; all other events are suppressed.

MembersEntries

## Entries

ESSENTIAL

ESSENTIAL

CAMERA_ONLY

CAMERA_ONLYForwards only camera motion events (move, zoom) plus minimal lifecycle (ready/load is implicit). Use this to support overlays that track camera without wiring all touch/render events.

ALL

ALL

OFF

OFF

## Properties

entries

val entries: EnumEntries<MTEventLevel>Returns a representation of an immutable list of all enum entries, in the order they're declared.

name

val name: String

ordinal

val ordinal: Int

## Functions

valueOf

fun valueOf(value: String): MTEventLevelReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

values

fun values(): Array<MTEventLevel>Returns an array containing the constants of this enum type, in the order they're declared.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-event-level/value-of.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-event-level"
---
# valueOf

fun valueOf(value: String): MTEventLevelReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
#### Throws

IllegalArgumentExceptionif this enum type has no constant with the specified name

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-event-level/values.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-event-level"
---
# values

fun values(): Array<MTEventLevel>Returns an array containing the constants of this enum type, in the order they're declared.This method may be used to iterate over the constants.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-fit-bounds-options/-m-t-fit-bounds-options.html

---
layout: mobile_sdk
title: "MTFitBoundsOptions"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTFitBoundsOptions"
id: -m-t-fit-bounds-options
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-fit-bounds-options"
---
# MTFitBoundsOptions

constructor(padding: MTPaddingOptions? = null, maxZoom: Double? = null, linear: Boolean? = null, offset: MTPoint? = null, duration: Double? = null, bearing: Double? = null, pitch: Double? = null, zoom: Double? = null)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-fit-bounds-options/bearing.html

---
layout: mobile_sdk
title: "bearing"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "bearing"
id: bearing
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-fit-bounds-options"
---
# bearing

val bearing: Double? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-fit-bounds-options/duration.html

---
layout: mobile_sdk
title: "duration"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "duration"
id: duration
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-fit-bounds-options"
---
# duration

val duration: Double? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-fit-bounds-options/index.html

---
layout: mobile_sdk
title: "MTFitBoundsOptions"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTFitBoundsOptions"
id: -m-t-fit-bounds-options
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-fit-bounds-options"
---
# MTFitBoundsOptions

@Serializabledata class MTFitBoundsOptions(val padding: MTPaddingOptions? = null, val maxZoom: Double? = null, val linear: Boolean? = null, val offset: MTPoint? = null, val duration: Double? = null, val bearing: Double? = null, val pitch: Double? = null, val zoom: Double? = null)Options that control how the map camera fits a set of bounds.

Members

## Constructors

MTFitBoundsOptions

constructor(padding: MTPaddingOptions? = null, maxZoom: Double? = null, linear: Boolean? = null, offset: MTPoint? = null, duration: Double? = null, bearing: Double? = null, pitch: Double? = null, zoom: Double? = null)

## Properties

bearing

val bearing: Double? = null

duration

val duration: Double? = null

linear

val linear: Boolean? = null

maxZoom

val maxZoom: Double? = null

offset

val offset: MTPoint? = null

padding

val padding: MTPaddingOptions? = null

pitch

val pitch: Double? = null

zoom

val zoom: Double? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-fit-bounds-options/linear.html

---
layout: mobile_sdk
title: "linear"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "linear"
id: linear
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-fit-bounds-options"
---
# linear

val linear: Boolean? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-fit-bounds-options/max-zoom.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-fit-bounds-options"
---
# maxZoom

val maxZoom: Double? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-fit-bounds-options/offset.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-fit-bounds-options"
---
# offset

val offset: MTPoint? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-fit-bounds-options/padding.html

---
layout: mobile_sdk
title: "padding"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "padding"
id: padding
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-fit-bounds-options"
---
# padding

val padding: MTPaddingOptions? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-fit-bounds-options/pitch.html

---
layout: mobile_sdk
title: "pitch"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "pitch"
id: pitch
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-fit-bounds-options"
---
# pitch

val pitch: Double? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-fit-bounds-options/zoom.html

---
layout: mobile_sdk
title: "zoom"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "zoom"
id: zoom
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-fit-bounds-options"
---
# zoom

val zoom: Double? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-fly-to-options/-m-t-fly-to-options.html

---
layout: mobile_sdk
title: "MTFlyToOptions"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTFlyToOptions"
id: -m-t-fly-to-options
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-fly-to-options"
---
# MTFlyToOptions

constructor(curve: Double?, minZoom: Double?, speed: Double?, screenSpeed: Double?, maxDuration: Double?)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-fly-to-options/curve.html

---
layout: mobile_sdk
title: "curve"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "curve"
id: curve
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-fly-to-options"
---
# curve

var curve: Double?

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-fly-to-options/index.html

---
layout: mobile_sdk
title: "MTFlyToOptions"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTFlyToOptions"
id: -m-t-fly-to-options
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-fly-to-options"
---
# MTFlyToOptions

@Serializableclass MTFlyToOptionsOptions describing the destination and animation of the transition.

Members

## Constructors

MTFlyToOptions

constructor(curve: Double?, minZoom: Double?, speed: Double?, screenSpeed: Double?, maxDuration: Double?)

## Properties

curve

var curve: Double?

maxDuration

var maxDuration: Double?

minZoom

var minZoom: Double?

screenSpeed

var screenSpeed: Double?

speed

var speed: Double?

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-fly-to-options/max-duration.html

---
layout: mobile_sdk
title: "maxDuration"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "maxDuration"
id: max-duration
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-fly-to-options"
---
# maxDuration

var maxDuration: Double?

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-fly-to-options/min-zoom.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-fly-to-options"
---
# minZoom

var minZoom: Double?

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-fly-to-options/screen-speed.html

---
layout: mobile_sdk
title: "screenSpeed"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "screenSpeed"
id: screen-speed
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-fly-to-options"
---
# screenSpeed

var screenSpeed: Double?

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-fly-to-options/speed.html

---
layout: mobile_sdk
title: "speed"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "speed"
id: speed
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-fly-to-options"
---
# speed

var speed: Double?

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-halo/-m-t-halo.html

---
layout: mobile_sdk
title: "MTHalo"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTHalo"
id: -m-t-halo
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-halo"
---
# MTHalo

constructor(scale: Double? = null, stops: List<MTHaloStop>? = null)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-halo/index.html

---
layout: mobile_sdk
title: "MTHalo"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTHalo"
id: -m-t-halo
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-halo"
---
# MTHalo

class MTHalo(val scale: Double? = null, val stops: List<MTHaloStop>? = null)Halo (atmospheric glow) configuration for the globe.When enabled, renders a radial gradient-based glow around the globe. Requires globe projection to be visible. Prefer setting via map options at initialization or dynamically via MTStyle.setHalo.

Members

## Constructors

MTHalo

constructor(scale: Double? = null, stops: List<MTHaloStop>? = null)

## Properties

scale

val scale: Double? = nullControls the halo size. Typical range is 0.0..2.0.

stops

val stops: List<MTHaloStop>? = nullDefines the radial gradient as a list of stops, each as a pair of normalized position (0..1) and a color string (e.g., "transparent", "#RRGGBB", "rgba(r,g,b,a)").

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-halo/scale.html

---
layout: mobile_sdk
title: "scale"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "scale"
id: scale
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-halo"
---
# scale

val scale: Double? = nullControls the halo size. Typical range is 0.0..2.0.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-halo/stops.html

---
layout: mobile_sdk
title: "stops"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "stops"
id: stops
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-halo"
---
# stops

val stops: List<MTHaloStop>? = nullDefines the radial gradient as a list of stops, each as a pair of normalized position (0..1) and a color string (e.g., "transparent", "#RRGGBB", "rgba(r,g,b,a)").

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-halo-option/-config/-config.html

---
layout: mobile_sdk
title: "Config"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Config"
id: -config
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-halo-option/-config"
---
# Config

constructor(value: MTHalo)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-halo-option/-config/index.html

---
layout: mobile_sdk
title: "Config"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Config"
id: -config
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-halo-option/-config"
---
# Config

data class Config(val value: MTHalo) : MTHaloOptionProvide a full configuration.

Members

## Constructors

Config

constructor(value: MTHalo)

## Properties

value

val value: MTHalo

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-halo-option/-config/value.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-halo-option/-config"
---
# value

val value: MTHalo

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-halo-option/-enabled/index.html

---
layout: mobile_sdk
title: "Enabled"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Enabled"
id: -enabled
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-halo-option/-enabled"
---
# Enabled

data object Enabled : MTHaloOptionEnable halo with default gradient.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-halo-option/index.html

---
layout: mobile_sdk
title: "MTHaloOption"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTHaloOption"
id: -m-t-halo-option
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-halo-option"
---
# MTHaloOption

@Serializable(with = MTHaloOptionSerializer::class)sealed class MTHaloOptionUnion wrapper for halo option: can be a simple enable flag or a full config object.
#### Inheritors

EnabledConfig

Members

## Types

Config

data class Config(val value: MTHalo) : MTHaloOptionProvide a full configuration.

Enabled

data object Enabled : MTHaloOptionEnable halo with default gradient.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-halo-option-serializer/descriptor.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-halo-option-serializer"
---
# descriptor

open override val descriptor: SerialDescriptor

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-halo-option-serializer/deserialize.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-halo-option-serializer"
---
# deserialize

open override fun deserialize(decoder: Decoder): MTHaloOption

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-halo-option-serializer/index.html

---
layout: mobile_sdk
title: "MTHaloOptionSerializer"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTHaloOptionSerializer"
id: -m-t-halo-option-serializer
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-halo-option-serializer"
---
# MTHaloOptionSerializer

object MTHaloOptionSerializer : KSerializer<MTHaloOption> 

Members

## Properties

descriptor

open override val descriptor: SerialDescriptor

## Functions

deserialize

open override fun deserialize(decoder: Decoder): MTHaloOption

serialize

open override fun serialize(encoder: Encoder, value: MTHaloOption)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-halo-option-serializer/serialize.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-halo-option-serializer"
---
# serialize

open override fun serialize(encoder: Encoder, value: MTHaloOption)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-halo-stop/-m-t-halo-stop.html

---
layout: mobile_sdk
title: "MTHaloStop"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTHaloStop"
id: -m-t-halo-stop
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-halo-stop"
---
# MTHaloStop

constructor(position: Double, color: String)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-halo-stop/color.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-halo-stop"
---
# color

val color: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-halo-stop/index.html

---
layout: mobile_sdk
title: "MTHaloStop"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTHaloStop"
id: -m-t-halo-stop
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-halo-stop"
---
# MTHaloStop

data class MTHaloStop(val position: Double, val color: String)A single halo gradient stop at a normalized distance with a color string.

Members

## Constructors

MTHaloStop

constructor(position: Double, color: String)

## Properties

color

val color: String

position

val position: Double

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-halo-stop/position.html

---
layout: mobile_sdk
title: "position"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "position"
id: position
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-halo-stop"
---
# position

val position: Double

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-padding-options/-m-t-padding-options.html

---
layout: mobile_sdk
title: "MTPaddingOptions"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTPaddingOptions"
id: -m-t-padding-options
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-padding-options"
---
# MTPaddingOptions

constructor(left: Double, top: Double, right: Double, bottom: Double)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-padding-options/bottom.html

---
layout: mobile_sdk
title: "bottom"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "bottom"
id: bottom
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-padding-options"
---
# bottom

val bottom: Double

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-padding-options/index.html

---
layout: mobile_sdk
title: "MTPaddingOptions"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTPaddingOptions"
id: -m-t-padding-options
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-padding-options"
---
# MTPaddingOptions

@Serializabledata class MTPaddingOptions(val left: Double, val top: Double, val right: Double, val bottom: Double)Options for setting padding on calls to map methods.

Members

## Constructors

MTPaddingOptions

constructor(left: Double, top: Double, right: Double, bottom: Double)

## Properties

bottom

val bottom: Double

left

val left: Double

right

val right: Double

top

val top: Double

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-padding-options/left.html

---
layout: mobile_sdk
title: "left"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "left"
id: left
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-padding-options"
---
# left

val left: Double

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-padding-options/right.html

---
layout: mobile_sdk
title: "right"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "right"
id: right
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-padding-options"
---
# right

val right: Double

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-padding-options/top.html

---
layout: mobile_sdk
title: "top"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "top"
id: top
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-padding-options"
---
# top

val top: Double

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-sky/-companion/color.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-sky/-companion"
---
# color

fun color(value: Int): StyleValueHelper for supplying a hex color int.fun color(value: String): StyleValueHelper for supplying color string (e.g., "#RRGGBB" or "rgba(...)").

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-sky/-companion/expression.html

---
layout: mobile_sdk
title: "expression"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "expression"
id: expression
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-sky/-companion"
---
# expression

fun expression(value: PropertyValue): StyleValueHelper for supplying an expression via PropertyValue.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-sky/-companion/index.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-sky/-companion"
---
# Companion

object Companion

Members

## Functions

color

fun color(value: Int): StyleValueHelper for supplying a hex color int.fun color(value: String): StyleValueHelper for supplying color string (e.g., "#RRGGBB" or "rgba(...)").

expression

fun expression(value: PropertyValue): StyleValueHelper for supplying an expression via PropertyValue.

number

fun number(value: Double): StyleValueHelper for supplying a numeric blend value.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-sky/-companion/number.html

---
layout: mobile_sdk
title: "number"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "number"
id: number
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-sky/-companion"
---
# number

fun number(value: Double): StyleValueHelper for supplying a numeric blend value.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-sky/-m-t-sky.html

---
layout: mobile_sdk
title: "MTSky"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTSky"
id: -m-t-sky
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-sky"
---
# MTSky

constructor(skyColor: StyleValue? = null, skyHorizonBlend: StyleValue? = null, horizonColor: StyleValue? = null, horizonFogBlend: StyleValue? = null, fogColor: StyleValue? = null, fogGroundBlend: StyleValue? = null, atmosphereBlend: StyleValue? = null)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-sky/atmosphere-blend.html

---
layout: mobile_sdk
title: "atmosphereBlend"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "atmosphereBlend"
id: atmosphere-blend
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-sky"
---
# atmosphereBlend

@SerialName(value = "atmosphere-blend")val atmosphereBlend: StyleValue? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-sky/fog-color.html

---
layout: mobile_sdk
title: "fogColor"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "fogColor"
id: fog-color
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-sky"
---
# fogColor

@SerialName(value = "fog-color")val fogColor: StyleValue? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-sky/fog-ground-blend.html

---
layout: mobile_sdk
title: "fogGroundBlend"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "fogGroundBlend"
id: fog-ground-blend
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-sky"
---
# fogGroundBlend

@SerialName(value = "fog-ground-blend")val fogGroundBlend: StyleValue? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-sky/horizon-color.html

---
layout: mobile_sdk
title: "horizonColor"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "horizonColor"
id: horizon-color
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-sky"
---
# horizonColor

@SerialName(value = "horizon-color")val horizonColor: StyleValue? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-sky/horizon-fog-blend.html

---
layout: mobile_sdk
title: "horizonFogBlend"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "horizonFogBlend"
id: horizon-fog-blend
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-sky"
---
# horizonFogBlend

@SerialName(value = "horizon-fog-blend")val horizonFogBlend: StyleValue? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-sky/index.html

---
layout: mobile_sdk
title: "MTSky"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTSky"
id: -m-t-sky
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-sky"
---
# MTSky

@Serializabledata class MTSky(val skyColor: StyleValue? = null, val skyHorizonBlend: StyleValue? = null, val horizonColor: StyleValue? = null, val horizonFogBlend: StyleValue? = null, val fogColor: StyleValue? = null, val fogGroundBlend: StyleValue? = null, val atmosphereBlend: StyleValue? = null)Sky configuration for customizing atmospheric appearance.All properties are optional; unspecified fields keep their previous values. Colors accept strings or hex int values. Blend values are clamped to 0, 1 when provided as plain numbers.

Members

## Constructors

MTSky

constructor(skyColor: StyleValue? = null, skyHorizonBlend: StyleValue? = null, horizonColor: StyleValue? = null, horizonFogBlend: StyleValue? = null, fogColor: StyleValue? = null, fogGroundBlend: StyleValue? = null, atmosphereBlend: StyleValue? = null)

## Types

Companion

object Companion

## Properties

atmosphereBlend

@SerialName(value = "atmosphere-blend")val atmosphereBlend: StyleValue? = null

fogColor

@SerialName(value = "fog-color")val fogColor: StyleValue? = null

fogGroundBlend

@SerialName(value = "fog-ground-blend")val fogGroundBlend: StyleValue? = null

horizonColor

@SerialName(value = "horizon-color")val horizonColor: StyleValue? = null

horizonFogBlend

@SerialName(value = "horizon-fog-blend")val horizonFogBlend: StyleValue? = null

skyColor

@SerialName(value = "sky-color")val skyColor: StyleValue? = null

skyHorizonBlend

@SerialName(value = "sky-horizon-blend")val skyHorizonBlend: StyleValue? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-sky/sky-color.html

---
layout: mobile_sdk
title: "skyColor"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "skyColor"
id: sky-color
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-sky"
---
# skyColor

@SerialName(value = "sky-color")val skyColor: StyleValue? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-sky/sky-horizon-blend.html

---
layout: mobile_sdk
title: "skyHorizonBlend"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "skyHorizonBlend"
id: sky-horizon-blend
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-sky"
---
# skyHorizonBlend

@SerialName(value = "sky-horizon-blend")val skyHorizonBlend: StyleValue? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space/-m-t-space.html

---
layout: mobile_sdk
title: "MTSpace"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTSpace"
id: -m-t-space
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space"
---
# MTSpace

constructor(color: Int? = null, preset: MTSpacePreset? = null, faces: MTSpaceFaces? = null, path: MTSpacePath? = null)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space/color.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space"
---
# color

@Serializable(with = ColorAsHexSerializer::class)var color: Int?Solid color for the space background or for tinting presets.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space/faces.html

---
layout: mobile_sdk
title: "faces"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "faces"
id: faces
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space"
---
# faces

var faces: MTSpaceFaces?Custom cubemap faces.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space/index.html

---
layout: mobile_sdk
title: "MTSpace"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTSpace"
id: -m-t-space
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space"
---
# MTSpace

@Serializableclass MTSpaceSpace configuration for customizing the globe background (deep space/skybox effects). Requires globe projection to be visible.

Members

## Constructors

MTSpace

constructor(color: Int? = null, preset: MTSpacePreset? = null, faces: MTSpaceFaces? = null, path: MTSpacePath? = null)

## Properties

color

@Serializable(with = ColorAsHexSerializer::class)var color: Int?Solid color for the space background or for tinting presets.

faces

var faces: MTSpaceFaces?Custom cubemap faces.

path

var path: MTSpacePath?Path-based cubemap definition.

preset

var preset: MTSpacePreset?Predefined cubemap preset.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space/path.html

---
layout: mobile_sdk
title: "path"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "path"
id: path
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space"
---
# path

var path: MTSpacePath?Path-based cubemap definition.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space/preset.html

---
layout: mobile_sdk
title: "preset"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "preset"
id: preset
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space"
---
# preset

var preset: MTSpacePreset?Predefined cubemap preset.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-faces/-m-t-space-faces.html

---
layout: mobile_sdk
title: "MTSpaceFaces"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTSpaceFaces"
id: -m-t-space-faces
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-faces"
---
# MTSpaceFaces

constructor(pX: String, nX: String, pY: String, nY: String, pZ: String, nZ: String)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-faces/index.html

---
layout: mobile_sdk
title: "MTSpaceFaces"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTSpaceFaces"
id: -m-t-space-faces
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-faces"
---
# MTSpaceFaces

@Serializableclass MTSpaceFaces(val pX: String, val nX: String, val pY: String, val nY: String, val pZ: String, val nZ: String)Definition of a cubemap using explicit face URLs.All fields should point to accessible image URLs.

Members

## Constructors

MTSpaceFaces

constructor(pX: String, nX: String, pY: String, nY: String, pZ: String, nZ: String)

## Properties

nX

val nX: String

nY

val nY: String

nZ

val nZ: String

pX

val pX: String

pY

val pY: String

pZ

val pZ: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-faces/n-x.html

---
layout: mobile_sdk
title: "nX"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "nX"
id: n-x
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-faces"
---
# nX

val nX: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-faces/n-y.html

---
layout: mobile_sdk
title: "nY"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "nY"
id: n-y
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-faces"
---
# nY

val nY: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-faces/n-z.html

---
layout: mobile_sdk
title: "nZ"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "nZ"
id: n-z
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-faces"
---
# nZ

val nZ: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-faces/p-x.html

---
layout: mobile_sdk
title: "pX"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "pX"
id: p-x
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-faces"
---
# pX

val pX: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-faces/p-y.html

---
layout: mobile_sdk
title: "pY"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "pY"
id: p-y
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-faces"
---
# pY

val pY: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-faces/p-z.html

---
layout: mobile_sdk
title: "pZ"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "pZ"
id: p-z
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-faces"
---
# pZ

val pZ: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-option/-config/-config.html

---
layout: mobile_sdk
title: "Config"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Config"
id: -config
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-option/-config"
---
# Config

constructor(value: MTSpace)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-option/-config/index.html

---
layout: mobile_sdk
title: "Config"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Config"
id: -config
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-option/-config"
---
# Config

data class Config(val value: MTSpace) : MTSpaceOptionProvide a full configuration.

Members

## Constructors

Config

constructor(value: MTSpace)

## Properties

value

val value: MTSpace

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-option/-config/value.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-option/-config"
---
# value

val value: MTSpace

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-option/-enabled/index.html

---
layout: mobile_sdk
title: "Enabled"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Enabled"
id: -enabled
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-option/-enabled"
---
# Enabled

data object Enabled : MTSpaceOptionEnable space with default preset (SDK default).

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-option/index.html

---
layout: mobile_sdk
title: "MTSpaceOption"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTSpaceOption"
id: -m-t-space-option
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-option"
---
# MTSpaceOption

@Serializable(with = MTSpaceOptionSerializer::class)sealed class MTSpaceOptionUnion wrapper for space option: can be a simple enable flag or a full config object.
#### Inheritors

EnabledConfig

Members

## Types

Config

data class Config(val value: MTSpace) : MTSpaceOptionProvide a full configuration.

Enabled

data object Enabled : MTSpaceOptionEnable space with default preset (SDK default).

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-option-serializer/descriptor.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-option-serializer"
---
# descriptor

open override val descriptor: SerialDescriptor

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-option-serializer/deserialize.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-option-serializer"
---
# deserialize

open override fun deserialize(decoder: Decoder): MTSpaceOption

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-option-serializer/index.html

---
layout: mobile_sdk
title: "MTSpaceOptionSerializer"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTSpaceOptionSerializer"
id: -m-t-space-option-serializer
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-option-serializer"
---
# MTSpaceOptionSerializer

object MTSpaceOptionSerializer : KSerializer<MTSpaceOption> 

Members

## Properties

descriptor

open override val descriptor: SerialDescriptor

## Functions

deserialize

open override fun deserialize(decoder: Decoder): MTSpaceOption

serialize

open override fun serialize(encoder: Encoder, value: MTSpaceOption)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-option-serializer/serialize.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-option-serializer"
---
# serialize

open override fun serialize(encoder: Encoder, value: MTSpaceOption)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-path/-m-t-space-path.html

---
layout: mobile_sdk
title: "MTSpacePath"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTSpacePath"
id: -m-t-space-path
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-path"
---
# MTSpacePath

constructor(baseUrl: String, format: String? = null)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-path/base-url.html

---
layout: mobile_sdk
title: "baseUrl"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "baseUrl"
id: base-url
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-path"
---
# baseUrl

val baseUrl: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-path/format.html

---
layout: mobile_sdk
title: "format"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "format"
id: format
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-path"
---
# format

val format: String? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-path/index.html

---
layout: mobile_sdk
title: "MTSpacePath"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTSpacePath"
id: -m-t-space-path
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-path"
---
# MTSpacePath

@Serializableclass MTSpacePath(val baseUrl: String, val format: String? = null)Definition of a cubemap path. Client must provide a base URL; files are expected to be named px, nx, py, ny, pz, nz with the specified format.

Members

## Constructors

MTSpacePath

constructor(baseUrl: String, format: String? = null)

## Properties

baseUrl

val baseUrl: String

format

val format: String? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-preset/-m-i-l-k-y-w-a-y/index.html

---
layout: mobile_sdk
title: "MILKYWAY"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MILKYWAY"
id: -m-i-l-k-y-w-a-y
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-preset/-m-i-l-k-y-w-a-y"
---
# MILKYWAY

@SerialName(value = "milkyway")MILKYWAYBlack half‑transparent background with standard milky way and stars.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-preset/-m-i-l-k-y-w-a-y_-b-r-i-g-h-t/index.html

---
layout: mobile_sdk
title: "MILKYWAY_BRIGHT"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MILKYWAY_BRIGHT"
id: -m-i-l-k-y-w-a-y_-b-r-i-g-h-t
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-preset/-m-i-l-k-y-w-a-y_-b-r-i-g-h-t"
---
# MILKYWAY_BRIGHT

@SerialName(value = "milkyway-bright")MILKYWAY_BRIGHTBright milky way, more stars.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-preset/-m-i-l-k-y-w-a-y_-c-o-l-o-r-e-d/index.html

---
layout: mobile_sdk
title: "MILKYWAY_COLORED"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MILKYWAY_COLORED"
id: -m-i-l-k-y-w-a-y_-c-o-l-o-r-e-d
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-preset/-m-i-l-k-y-w-a-y_-c-o-l-o-r-e-d"
---
# MILKYWAY_COLORED

@SerialName(value = "milkyway-colored")MILKYWAY_COLOREDFull image with natural colors; space color has no effect.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-preset/-m-i-l-k-y-w-a-y_-s-u-b-t-l-e/index.html

---
layout: mobile_sdk
title: "MILKYWAY_SUBTLE"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MILKYWAY_SUBTLE"
id: -m-i-l-k-y-w-a-y_-s-u-b-t-l-e
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-preset/-m-i-l-k-y-w-a-y_-s-u-b-t-l-e"
---
# MILKYWAY_SUBTLE

@SerialName(value = "milkyway-subtle")MILKYWAY_SUBTLESubtle milky way, fewer stars.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-preset/-s-p-a-c-e/index.html

---
layout: mobile_sdk
title: "SPACE"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "SPACE"
id: -s-p-a-c-e
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-preset/-s-p-a-c-e"
---
# SPACE

@SerialName(value = "space")SPACEDark blue background; stars stay white. Space color changes background color.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-preset/-s-t-a-r-s/index.html

---
layout: mobile_sdk
title: "STARS"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "STARS"
id: -s-t-a-r-s
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-preset/-s-t-a-r-s"
---
# STARS

@SerialName(value = "stars")STARSBlack background; space color changes stars color.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-preset/entries.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-preset"
---
# entries

val entries: EnumEntries<MTSpacePreset>Returns a representation of an immutable list of all enum entries, in the order they're declared.This method may be used to iterate over the enum entries.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-preset/index.html

---
layout: mobile_sdk
title: "MTSpacePreset"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTSpacePreset"
id: -m-t-space-preset
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-preset"
---
# MTSpacePreset

@Serializableenum MTSpacePreset : Enum<MTSpacePreset> Predefined space cubemap presets.

MembersEntries

## Entries

SPACE

@SerialName(value = "space")SPACEDark blue background; stars stay white. Space color changes background color.

STARS

@SerialName(value = "stars")STARSBlack background; space color changes stars color.

MILKYWAY

@SerialName(value = "milkyway")MILKYWAYBlack half‑transparent background with standard milky way and stars.

MILKYWAY_SUBTLE

@SerialName(value = "milkyway-subtle")MILKYWAY_SUBTLESubtle milky way, fewer stars.

MILKYWAY_BRIGHT

@SerialName(value = "milkyway-bright")MILKYWAY_BRIGHTBright milky way, more stars.

MILKYWAY_COLORED

@SerialName(value = "milkyway-colored")MILKYWAY_COLOREDFull image with natural colors; space color has no effect.

## Properties

entries

val entries: EnumEntries<MTSpacePreset>Returns a representation of an immutable list of all enum entries, in the order they're declared.

name

val name: String

ordinal

val ordinal: Int

## Functions

valueOf

fun valueOf(value: String): MTSpacePresetReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

values

fun values(): Array<MTSpacePreset>Returns an array containing the constants of this enum type, in the order they're declared.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-preset/value-of.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-preset"
---
# valueOf

fun valueOf(value: String): MTSpacePresetReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
#### Throws

IllegalArgumentExceptionif this enum type has no constant with the specified name

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-preset/values.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/-m-t-space-preset"
---
# values

fun values(): Array<MTSpacePreset>Returns an array containing the constants of this enum type, in the order they're declared.This method may be used to iterate over the constants.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.options/index.html

---
layout: mobile_sdk
title: "com.maptiler.maptilersdk.map.options"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "com.maptiler.maptilersdk.map.options"
id: com.maptiler.maptilersdk.map.options
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.options"
---
# com.maptiler.maptilersdk.map.options

Types

## Types

MTAnimationOptions

@Serializabledata class MTAnimationOptions(val duration: Double? = null, val animate: Boolean? = null, val essential: Boolean? = null, val offset: MTPoint? = null)Options describing the animation of the transition.

MTCameraOptions

@Serializableclass MTCameraOptionsOptions for controlling the desired location, zoom, bearing, and pitch of the camera.

MTDragPanOptions

@Serializabledata class MTDragPanOptions(val linearity: Double? = null, val maxSpeed: Double? = null, val deceleration: Double? = null)

MTEventLevel

enum MTEventLevel : Enum<MTEventLevel> Controls which map events are forwarded from the map object.

MTFitBoundsOptions

@Serializabledata class MTFitBoundsOptions(val padding: MTPaddingOptions? = null, val maxZoom: Double? = null, val linear: Boolean? = null, val offset: MTPoint? = null, val duration: Double? = null, val bearing: Double? = null, val pitch: Double? = null, val zoom: Double? = null)Options that control how the map camera fits a set of bounds.

MTFlyToOptions

@Serializableclass MTFlyToOptionsOptions describing the destination and animation of the transition.

MTHalo

class MTHalo(val scale: Double? = null, val stops: List<MTHaloStop>? = null)Halo (atmospheric glow) configuration for the globe.

MTHaloOption

@Serializable(with = MTHaloOptionSerializer::class)sealed class MTHaloOptionUnion wrapper for halo option: can be a simple enable flag or a full config object.

MTHaloOptionSerializer

object MTHaloOptionSerializer : KSerializer<MTHaloOption> 

MTHaloStop

data class MTHaloStop(val position: Double, val color: String)A single halo gradient stop at a normalized distance with a color string.

MTPaddingOptions

@Serializabledata class MTPaddingOptions(val left: Double, val top: Double, val right: Double, val bottom: Double)Options for setting padding on calls to map methods.

MTSky

@Serializabledata class MTSky(val skyColor: StyleValue? = null, val skyHorizonBlend: StyleValue? = null, val horizonColor: StyleValue? = null, val horizonFogBlend: StyleValue? = null, val fogColor: StyleValue? = null, val fogGroundBlend: StyleValue? = null, val atmosphereBlend: StyleValue? = null)Sky configuration for customizing atmospheric appearance.

MTSpace

@Serializableclass MTSpaceSpace configuration for customizing the globe background (deep space/skybox effects). Requires globe projection to be visible.

MTSpaceFaces

@Serializableclass MTSpaceFaces(val pX: String, val nX: String, val pY: String, val nY: String, val pZ: String, val nZ: String)Definition of a cubemap using explicit face URLs.

MTSpaceOption

@Serializable(with = MTSpaceOptionSerializer::class)sealed class MTSpaceOptionUnion wrapper for space option: can be a simple enable flag or a full config object.

MTSpaceOptionSerializer

object MTSpaceOptionSerializer : KSerializer<MTSpaceOption> 

MTSpacePath

@Serializableclass MTSpacePath(val baseUrl: String, val format: String? = null)Definition of a cubemap path. Client must provide a base URL; files are expected to be named px, nx, py, ny, pz, nz with the specified format.

MTSpacePreset

@Serializableenum MTSpacePreset : Enum<MTSpacePreset> Predefined space cubemap presets.

---

