# MapTiler Android SDK API Reference - com.maptiler.maptilersdk.events

This document is a part of the Android SDK API reference documentation, covering the `com.maptiler.maptilersdk.events` package.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-event-processor/-event-processor.html

---
layout: mobile_sdk
title: "EventProcessor"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "EventProcessor"
id: -event-processor
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-event-processor"
---
# EventProcessor

constructor()

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-event-processor/delegate.html

---
layout: mobile_sdk
title: "delegate"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "delegate"
id: delegate
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-event-processor"
---
# delegate

var delegate: EventProcessorDelegate?

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-event-processor/index.html

---
layout: mobile_sdk
title: "EventProcessor"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "EventProcessor"
id: -event-processor
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-event-processor"
---
# EventProcessor

class EventProcessor

Members

## Constructors

EventProcessor

constructor()

## Properties

delegate

var delegate: EventProcessorDelegate?

## Functions

registerEvent

fun registerEvent(event: MTEvent?, data: MTData? = null)

setDoubleTapSensitivity

fun setDoubleTapSensitivity(sensitivity: Double)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-event-processor/register-event.html

---
layout: mobile_sdk
title: "registerEvent"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "registerEvent"
id: register-event
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-event-processor"
---
# registerEvent

fun registerEvent(event: MTEvent?, data: MTData? = null)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-event-processor/set-double-tap-sensitivity.html

---
layout: mobile_sdk
title: "setDoubleTapSensitivity"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setDoubleTapSensitivity"
id: set-double-tap-sensitivity
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-event-processor"
---
# setDoubleTapSensitivity

fun setDoubleTapSensitivity(sensitivity: Double)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-event-processor-delegate/index.html

---
layout: mobile_sdk
title: "EventProcessorDelegate"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "EventProcessorDelegate"
id: -event-processor-delegate
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-event-processor-delegate"
---
# EventProcessorDelegate

interface EventProcessorDelegate
#### Inheritors

MTMapViewController

Members

## Functions

onEventTriggered

abstract fun onEventTriggered(processor: EventProcessor, event: MTEvent, data: MTData? = null)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-event-processor-delegate/on-event-triggered.html

---
layout: mobile_sdk
title: "onEventTriggered"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "onEventTriggered"
id: on-event-triggered
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-event-processor-delegate"
---
# onEventTriggered

abstract fun onEventTriggered(processor: EventProcessor, event: MTEvent, data: MTData? = null)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-b-o-x_-z-o-o-m_-c-a-n-c-e-l/index.html

---
layout: mobile_sdk
title: "ON_BOX_ZOOM_CANCEL"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_BOX_ZOOM_CANCEL"
id: -o-n_-b-o-x_-z-o-o-m_-c-a-n-c-e-l
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-b-o-x_-z-o-o-m_-c-a-n-c-e-l"
---
# ON_BOX_ZOOM_CANCEL

@SerialName(value = "boxzoomcancel")ON_BOX_ZOOM_CANCELTriggered when the user cancels a "box zoom" interaction, or when the bounding box does not meet the minimum size threshold.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-b-o-x_-z-o-o-m_-e-n-d/index.html

---
layout: mobile_sdk
title: "ON_BOX_ZOOM_END"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_BOX_ZOOM_END"
id: -o-n_-b-o-x_-z-o-o-m_-e-n-d
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-b-o-x_-z-o-o-m_-e-n-d"
---
# ON_BOX_ZOOM_END

@SerialName(value = "boxzoomend")ON_BOX_ZOOM_ENDTriggered when a "box zoom" interaction ends.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-b-o-x_-z-o-o-m_-s-t-a-r-t/index.html

---
layout: mobile_sdk
title: "ON_BOX_ZOOM_START"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_BOX_ZOOM_START"
id: -o-n_-b-o-x_-z-o-o-m_-s-t-a-r-t
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-b-o-x_-z-o-o-m_-s-t-a-r-t"
---
# ON_BOX_ZOOM_START

@SerialName(value = "boxzoomstart")ON_BOX_ZOOM_STARTTriggered when a "box zoom" interaction starts.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-c-o-o-p-e-r-a-t-i-v-e_-g-e-s-t-u-r-e_-p-r-e-v-e-n-t-e-d/index.html

---
layout: mobile_sdk
title: "ON_COOPERATIVE_GESTURE_PREVENTED"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_COOPERATIVE_GESTURE_PREVENTED"
id: -o-n_-c-o-o-p-e-r-a-t-i-v-e_-g-e-s-t-u-r-e_-p-r-e-v-e-n-t-e-d
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-c-o-o-p-e-r-a-t-i-v-e_-g-e-s-t-u-r-e_-p-r-e-v-e-n-t-e-d"
---
# ON_COOPERATIVE_GESTURE_PREVENTED

@SerialName(value = "cooperativegestureprevented")ON_COOPERATIVE_GESTURE_PREVENTEDTriggered whenever the cooperativeGestures option prevents a gesture from being handled by the map.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-d-a-t-a_-u-p-d-a-t-e/index.html

---
layout: mobile_sdk
title: "ON_DATA_UPDATE"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_DATA_UPDATE"
id: -o-n_-d-a-t-a_-u-p-d-a-t-e
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-d-a-t-a_-u-p-d-a-t-e"
---
# ON_DATA_UPDATE

@SerialName(value = "data")ON_DATA_UPDATETriggered when any map data loads or changes.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-d-a-t-a_-u-p-d-a-t-e_-a-b-o-r-t/index.html

---
layout: mobile_sdk
title: "ON_DATA_UPDATE_ABORT"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_DATA_UPDATE_ABORT"
id: -o-n_-d-a-t-a_-u-p-d-a-t-e_-a-b-o-r-t
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-d-a-t-a_-u-p-d-a-t-e_-a-b-o-r-t"
---
# ON_DATA_UPDATE_ABORT

@SerialName(value = "dataabort")ON_DATA_UPDATE_ABORTTriggered when a request for one of the map's sources' tiles is aborted. Triggered when a request for one of the map's sources' data is aborted.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-d-a-t-a_-u-p-d-a-t-e_-s-t-a-r-t/index.html

---
layout: mobile_sdk
title: "ON_DATA_UPDATE_START"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_DATA_UPDATE_START"
id: -o-n_-d-a-t-a_-u-p-d-a-t-e_-s-t-a-r-t
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-d-a-t-a_-u-p-d-a-t-e_-s-t-a-r-t"
---
# ON_DATA_UPDATE_START

@SerialName(value = "dataloading")ON_DATA_UPDATE_STARTTriggered when any map data (style, source, tile, etc) begins loading or changing asynchronously. All dataloading events are followed by a dataDidUpdate, dataUpdateDidAbort or error events.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-d-o-u-b-l-e_-t-a-p/index.html

---
layout: mobile_sdk
title: "ON_DOUBLE_TAP"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_DOUBLE_TAP"
id: -o-n_-d-o-u-b-l-e_-t-a-p
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-d-o-u-b-l-e_-t-a-p"
---
# ON_DOUBLE_TAP

@SerialName(value = "dblclick")ON_DOUBLE_TAPTriggered when a user taps and releases twice at the same point on the map in rapid succession.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-d-r-a-g/index.html

---
layout: mobile_sdk
title: "ON_DRAG"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_DRAG"
id: -o-n_-d-r-a-g
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-d-r-a-g"
---
# ON_DRAG

@SerialName(value = "drag")ON_DRAGTriggered repeatedly during a "drag to pan" interaction.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-d-r-a-g_-e-n-d/index.html

---
layout: mobile_sdk
title: "ON_DRAG_END"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_DRAG_END"
id: -o-n_-d-r-a-g_-e-n-d
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-d-r-a-g_-e-n-d"
---
# ON_DRAG_END

@SerialName(value = "dragend")ON_DRAG_ENDTriggered when a "drag to pan" interaction ends.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-d-r-a-g_-s-t-a-r-t/index.html

---
layout: mobile_sdk
title: "ON_DRAG_START"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_DRAG_START"
id: -o-n_-d-r-a-g_-s-t-a-r-t
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-d-r-a-g_-s-t-a-r-t"
---
# ON_DRAG_START

@SerialName(value = "dragstart")ON_DRAG_STARTTriggered when a "drag to pan" interaction starts.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-i-d-l-e/index.html

---
layout: mobile_sdk
title: "ON_IDLE"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_IDLE"
id: -o-n_-i-d-l-e
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-i-d-l-e"
---
# ON_IDLE

@SerialName(value = "idle")ON_IDLETriggered after the last frame rendered before the map enters an "idle" state. Idle state means that no camera transitions are in progress, all currently requested tiles have loaded, and all fade/transition animations have completed.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-l-o-a-d/index.html

---
layout: mobile_sdk
title: "ON_LOAD"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_LOAD"
id: -o-n_-l-o-a-d
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-l-o-a-d"
---
# ON_LOAD

@SerialName(value = "load")ON_LOADTriggered immediately after all necessary resources have been downloaded and the first visually complete rendering of the map has occurred.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-l-o-a-d_-w-i-t-h_-t-e-r-r-a-i-n/index.html

---
layout: mobile_sdk
title: "ON_LOAD_WITH_TERRAIN"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_LOAD_WITH_TERRAIN"
id: -o-n_-l-o-a-d_-w-i-t-h_-t-e-r-r-a-i-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-l-o-a-d_-w-i-t-h_-t-e-r-r-a-i-n"
---
# ON_LOAD_WITH_TERRAIN

@SerialName(value = "loadWithTerrain")ON_LOAD_WITH_TERRAINTriggered only once in a Map instance lifecycle, when both the load event and the terrain event with non-null terrain are triggered.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-m-a-r-k-e-r_-d-r-a-g/index.html

---
layout: mobile_sdk
title: "ON_MARKER_DRAG"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_MARKER_DRAG"
id: -o-n_-m-a-r-k-e-r_-d-r-a-g
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-m-a-r-k-e-r_-d-r-a-g"
---
# ON_MARKER_DRAG

@SerialName(value = "marker.drag")ON_MARKER_DRAGTriggered repeatedly while a marker is being dragged.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-m-a-r-k-e-r_-d-r-a-g_-e-n-d/index.html

---
layout: mobile_sdk
title: "ON_MARKER_DRAG_END"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_MARKER_DRAG_END"
id: -o-n_-m-a-r-k-e-r_-d-r-a-g_-e-n-d
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-m-a-r-k-e-r_-d-r-a-g_-e-n-d"
---
# ON_MARKER_DRAG_END

@SerialName(value = "marker.dragend")ON_MARKER_DRAG_ENDTriggered when marker dragging ends.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-m-a-r-k-e-r_-d-r-a-g_-s-t-a-r-t/index.html

---
layout: mobile_sdk
title: "ON_MARKER_DRAG_START"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_MARKER_DRAG_START"
id: -o-n_-m-a-r-k-e-r_-d-r-a-g_-s-t-a-r-t
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-m-a-r-k-e-r_-d-r-a-g_-s-t-a-r-t"
---
# ON_MARKER_DRAG_START

@SerialName(value = "marker.dragstart")ON_MARKER_DRAG_STARTTriggered when marker dragging starts.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-m-o-v-e/index.html

---
layout: mobile_sdk
title: "ON_MOVE"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_MOVE"
id: -o-n_-m-o-v-e
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-m-o-v-e"
---
# ON_MOVE

@SerialName(value = "move")ON_MOVETriggered repeatedly during an animated transition from one view to another, as the result of either user interaction or methods such as flyTo.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-m-o-v-e_-e-n-d/index.html

---
layout: mobile_sdk
title: "ON_MOVE_END"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_MOVE_END"
id: -o-n_-m-o-v-e_-e-n-d
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-m-o-v-e_-e-n-d"
---
# ON_MOVE_END

@SerialName(value = "moveend")ON_MOVE_ENDTriggered just after the map completes a transition from one view to another, as the result of either user interaction or methods such as jumpTo.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-m-o-v-e_-s-t-a-r-t/index.html

---
layout: mobile_sdk
title: "ON_MOVE_START"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_MOVE_START"
id: -o-n_-m-o-v-e_-s-t-a-r-t
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-m-o-v-e_-s-t-a-r-t"
---
# ON_MOVE_START

@SerialName(value = "movestart")ON_MOVE_STARTTriggered just before the map begins a transition from one view to another, as the result of either user interaction or methods such as jumpTo.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-p-i-t-c-h_-u-p-d-a-t-e/index.html

---
layout: mobile_sdk
title: "ON_PITCH_UPDATE"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_PITCH_UPDATE"
id: -o-n_-p-i-t-c-h_-u-p-d-a-t-e
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-p-i-t-c-h_-u-p-d-a-t-e"
---
# ON_PITCH_UPDATE

@SerialName(value = "pitch")ON_PITCH_UPDATETriggered repeatedly during the map's pitch (tilt) animation between one state and another as the result of either user interaction or methods such as flyTo.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-p-i-t-c-h_-u-p-d-a-t-e_-e-n-d/index.html

---
layout: mobile_sdk
title: "ON_PITCH_UPDATE_END"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_PITCH_UPDATE_END"
id: -o-n_-p-i-t-c-h_-u-p-d-a-t-e_-e-n-d
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-p-i-t-c-h_-u-p-d-a-t-e_-e-n-d"
---
# ON_PITCH_UPDATE_END

@SerialName(value = "pitchend")ON_PITCH_UPDATE_ENDTriggered immediately after the map's pitch (tilt) finishes changing as the result of either user interaction or methods such as flyTo.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-p-i-t-c-h_-u-p-d-a-t-e_-s-t-a-r-t/index.html

---
layout: mobile_sdk
title: "ON_PITCH_UPDATE_START"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_PITCH_UPDATE_START"
id: -o-n_-p-i-t-c-h_-u-p-d-a-t-e_-s-t-a-r-t
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-p-i-t-c-h_-u-p-d-a-t-e_-s-t-a-r-t"
---
# ON_PITCH_UPDATE_START

@SerialName(value = "pitchstart")ON_PITCH_UPDATE_STARTTriggered whenever the map's pitch (tilt) begins a change as the result of either user interaction or methods such as flyTo.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-p-o-p-u-p_-c-l-o-s-e/index.html

---
layout: mobile_sdk
title: "ON_POPUP_CLOSE"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_POPUP_CLOSE"
id: -o-n_-p-o-p-u-p_-c-l-o-s-e
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-p-o-p-u-p_-c-l-o-s-e"
---
# ON_POPUP_CLOSE

@SerialName(value = "popup.close")ON_POPUP_CLOSETriggered when a popup is closed (removed from the map).

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-p-o-p-u-p_-o-p-e-n/index.html

---
layout: mobile_sdk
title: "ON_POPUP_OPEN"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_POPUP_OPEN"
id: -o-n_-p-o-p-u-p_-o-p-e-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-p-o-p-u-p_-o-p-e-n"
---
# ON_POPUP_OPEN

@SerialName(value = "popup.open")ON_POPUP_OPENTriggered when a popup is opened (added to the map).

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-p-r-o-j-e-c-t-i-o-n_-m-o-d-i-f-y/index.html

---
layout: mobile_sdk
title: "ON_PROJECTION_MODIFY"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_PROJECTION_MODIFY"
id: -o-n_-p-r-o-j-e-c-t-i-o-n_-m-o-d-i-f-y
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-p-r-o-j-e-c-t-i-o-n_-m-o-d-i-f-y"
---
# ON_PROJECTION_MODIFY

@SerialName(value = "projectiontransition")ON_PROJECTION_MODIFYTriggered when map's projection is modified in other ways than by map being moved.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-r-e-a-d-y/index.html

---
layout: mobile_sdk
title: "ON_READY"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_READY"
id: -o-n_-r-e-a-d-y
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-r-e-a-d-y"
---
# ON_READY

@SerialName(value = "ready")ON_READYTriggered only once after load and wait for all the controls managed by the Map constructor to be dealt with. Since the ready event waits that all the basic controls are nicely positioned, it is safer to use ready than load if you plan to add other custom controls.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-r-e-m-o-v-e/index.html

---
layout: mobile_sdk
title: "ON_REMOVE"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_REMOVE"
id: -o-n_-r-e-m-o-v-e
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-r-e-m-o-v-e"
---
# ON_REMOVE

@SerialName(value = "remove")ON_REMOVETriggered immediately after the map has been removed.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-r-e-n-d-e-r/index.html

---
layout: mobile_sdk
title: "ON_RENDER"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_RENDER"
id: -o-n_-r-e-n-d-e-r
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-r-e-n-d-e-r"
---
# ON_RENDER

@SerialName(value = "render")ON_RENDERTriggered whenever the map is drawn to the screen. Drawing occurs with a change to the map's position, zoom, pitch, or bearing, a change to the map's style, a change to a GeoJSON source, or the loading of a vector tile, GeoJSON file, glyph, or sprite.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-r-e-s-i-z-e/index.html

---
layout: mobile_sdk
title: "ON_RESIZE"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_RESIZE"
id: -o-n_-r-e-s-i-z-e
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-r-e-s-i-z-e"
---
# ON_RESIZE

@SerialName(value = "resize")ON_RESIZETriggered immediately after the map has been resized.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-r-o-t-a-t-e/index.html

---
layout: mobile_sdk
title: "ON_ROTATE"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_ROTATE"
id: -o-n_-r-o-t-a-t-e
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-r-o-t-a-t-e"
---
# ON_ROTATE

@SerialName(value = "rotate")ON_ROTATETriggered repeatedly during a "drag to rotate" interaction.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-r-o-t-a-t-e_-e-n-d/index.html

---
layout: mobile_sdk
title: "ON_ROTATE_END"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_ROTATE_END"
id: -o-n_-r-o-t-a-t-e_-e-n-d
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-r-o-t-a-t-e_-e-n-d"
---
# ON_ROTATE_END

@SerialName(value = "rotateend")ON_ROTATE_ENDTriggered when a "drag to rotate" interaction ends.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-r-o-t-a-t-e_-s-t-a-r-t/index.html

---
layout: mobile_sdk
title: "ON_ROTATE_START"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_ROTATE_START"
id: -o-n_-r-o-t-a-t-e_-s-t-a-r-t
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-r-o-t-a-t-e_-s-t-a-r-t"
---
# ON_ROTATE_START

@SerialName(value = "rotatestart")ON_ROTATE_STARTTriggered when a "drag to rotate" interaction starts.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-s-o-u-r-c-e_-u-p-d-a-t-e/index.html

---
layout: mobile_sdk
title: "ON_SOURCE_UPDATE"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_SOURCE_UPDATE"
id: -o-n_-s-o-u-r-c-e_-u-p-d-a-t-e
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-s-o-u-r-c-e_-u-p-d-a-t-e"
---
# ON_SOURCE_UPDATE

@SerialName(value = "sourcedata")ON_SOURCE_UPDATETriggered when one of the map's sources loads or changes, including if a tile belonging to a source loads or changes.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-s-o-u-r-c-e_-u-p-d-a-t-e_-a-b-o-r-t/index.html

---
layout: mobile_sdk
title: "ON_SOURCE_UPDATE_ABORT"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_SOURCE_UPDATE_ABORT"
id: -o-n_-s-o-u-r-c-e_-u-p-d-a-t-e_-a-b-o-r-t
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-s-o-u-r-c-e_-u-p-d-a-t-e_-a-b-o-r-t"
---
# ON_SOURCE_UPDATE_ABORT

@SerialName(value = "sourcedataabort")ON_SOURCE_UPDATE_ABORTTriggered when a request for one of the map's sources' data is aborted.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-s-o-u-r-c-e_-u-p-d-a-t-e_-s-t-a-r-t/index.html

---
layout: mobile_sdk
title: "ON_SOURCE_UPDATE_START"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_SOURCE_UPDATE_START"
id: -o-n_-s-o-u-r-c-e_-u-p-d-a-t-e_-s-t-a-r-t
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-s-o-u-r-c-e_-u-p-d-a-t-e_-s-t-a-r-t"
---
# ON_SOURCE_UPDATE_START

@SerialName(value = "sourcedataloading")ON_SOURCE_UPDATE_STARTTriggered when one of the map's sources begins loading or changing asynchronously. All sourceUpdateDidStart events are followed by a sourceDidUpdate, sourceUpdateDidAbort or error events.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-s-t-y-l-e_-i-m-a-g-e_-m-i-s-s-i-n-g/index.html

---
layout: mobile_sdk
title: "ON_STYLE_IMAGE_MISSING"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_STYLE_IMAGE_MISSING"
id: -o-n_-s-t-y-l-e_-i-m-a-g-e_-m-i-s-s-i-n-g
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-s-t-y-l-e_-i-m-a-g-e_-m-i-s-s-i-n-g"
---
# ON_STYLE_IMAGE_MISSING

@SerialName(value = "styleimagemissing")ON_STYLE_IMAGE_MISSINGTriggered when an icon or pattern needed by the style is missing.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-s-t-y-l-e_-u-p-d-a-t-e/index.html

---
layout: mobile_sdk
title: "ON_STYLE_UPDATE"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_STYLE_UPDATE"
id: -o-n_-s-t-y-l-e_-u-p-d-a-t-e
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-s-t-y-l-e_-u-p-d-a-t-e"
---
# ON_STYLE_UPDATE

@SerialName(value = "styledata")ON_STYLE_UPDATETriggered when the map's style loads or changes.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-s-t-y-l-e_-u-p-d-a-t-e_-s-t-a-r-t/index.html

---
layout: mobile_sdk
title: "ON_STYLE_UPDATE_START"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_STYLE_UPDATE_START"
id: -o-n_-s-t-y-l-e_-u-p-d-a-t-e_-s-t-a-r-t
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-s-t-y-l-e_-u-p-d-a-t-e_-s-t-a-r-t"
---
# ON_STYLE_UPDATE_START

@SerialName(value = "styledataloading")ON_STYLE_UPDATE_STARTTriggered when the map's style begins loading or changing asynchronously. All styleUpdateDidStart events are followed by a styleDidUpdate or error events.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-t-a-p/index.html

---
layout: mobile_sdk
title: "ON_TAP"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_TAP"
id: -o-n_-t-a-p
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-t-a-p"
---
# ON_TAP

@SerialName(value = "click")ON_TAPTriggered when user taps and releases at the same point on the map.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-t-e-r-r-a-i-n_-a-n-i-m-a-t-i-o-n_-s-t-a-r-t/index.html

---
layout: mobile_sdk
title: "ON_TERRAIN_ANIMATION_START"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_TERRAIN_ANIMATION_START"
id: -o-n_-t-e-r-r-a-i-n_-a-n-i-m-a-t-i-o-n_-s-t-a-r-t
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-t-e-r-r-a-i-n_-a-n-i-m-a-t-i-o-n_-s-t-a-r-t"
---
# ON_TERRAIN_ANIMATION_START

@SerialName(value = "terrainAnimationStart")ON_TERRAIN_ANIMATION_STARTThe terrainAnimationDidStart event is triggered when the animation begins transitioning between terrain and non-terrain states.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-t-e-r-r-a-i-n_-a-n-i-m-a-t-i-o-n_-s-t-o-p/index.html

---
layout: mobile_sdk
title: "ON_TERRAIN_ANIMATION_STOP"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_TERRAIN_ANIMATION_STOP"
id: -o-n_-t-e-r-r-a-i-n_-a-n-i-m-a-t-i-o-n_-s-t-o-p
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-t-e-r-r-a-i-n_-a-n-i-m-a-t-i-o-n_-s-t-o-p"
---
# ON_TERRAIN_ANIMATION_STOP

@SerialName(value = "terrainAnimationStop")ON_TERRAIN_ANIMATION_STOPThe terrainAnimationDidStop event is triggered when the animation between terrain and non-terrain states ends.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-t-e-r-r-a-i-n_-c-h-a-n-g-e/index.html

---
layout: mobile_sdk
title: "ON_TERRAIN_CHANGE"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_TERRAIN_CHANGE"
id: -o-n_-t-e-r-r-a-i-n_-c-h-a-n-g-e
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-t-e-r-r-a-i-n_-c-h-a-n-g-e"
---
# ON_TERRAIN_CHANGE

@SerialName(value = "terrain")ON_TERRAIN_CHANGETriggered when a terrain event occurs within the map.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-t-o-u-c-h_-c-a-n-c-e-l/index.html

---
layout: mobile_sdk
title: "ON_TOUCH_CANCEL"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_TOUCH_CANCEL"
id: -o-n_-t-o-u-c-h_-c-a-n-c-e-l
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-t-o-u-c-h_-c-a-n-c-e-l"
---
# ON_TOUCH_CANCEL

@SerialName(value = "touchcancel")ON_TOUCH_CANCELTriggered when a touch is cancelled within the map.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-t-o-u-c-h_-e-n-d/index.html

---
layout: mobile_sdk
title: "ON_TOUCH_END"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_TOUCH_END"
id: -o-n_-t-o-u-c-h_-e-n-d
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-t-o-u-c-h_-e-n-d"
---
# ON_TOUCH_END

@SerialName(value = "touchend")ON_TOUCH_ENDTriggered when a touch ends within the map.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-t-o-u-c-h_-m-o-v-e/index.html

---
layout: mobile_sdk
title: "ON_TOUCH_MOVE"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_TOUCH_MOVE"
id: -o-n_-t-o-u-c-h_-m-o-v-e
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-t-o-u-c-h_-m-o-v-e"
---
# ON_TOUCH_MOVE

@SerialName(value = "touchmove")ON_TOUCH_MOVETriggered when a touch moves within the map.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-t-o-u-c-h_-s-t-a-r-t/index.html

---
layout: mobile_sdk
title: "ON_TOUCH_START"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_TOUCH_START"
id: -o-n_-t-o-u-c-h_-s-t-a-r-t
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-t-o-u-c-h_-s-t-a-r-t"
---
# ON_TOUCH_START

@SerialName(value = "touchstart")ON_TOUCH_STARTTriggered when a touch starts within the map.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-z-o-o-m/index.html

---
layout: mobile_sdk
title: "ON_ZOOM"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_ZOOM"
id: -o-n_-z-o-o-m
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-z-o-o-m"
---
# ON_ZOOM

@SerialName(value = "zoom")ON_ZOOMTriggered repeatedly during an animated transition from one zoom level to another, as the result of either user interaction or methods such as flyTo.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-z-o-o-m_-e-n-d/index.html

---
layout: mobile_sdk
title: "ON_ZOOM_END"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_ZOOM_END"
id: -o-n_-z-o-o-m_-e-n-d
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-z-o-o-m_-e-n-d"
---
# ON_ZOOM_END

@SerialName(value = "zoomend")ON_ZOOM_ENDTriggered just after the map completes a transition from one zoom level to another, as the result of either user interaction or methods such as flyTo.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-z-o-o-m_-s-t-a-r-t/index.html

---
layout: mobile_sdk
title: "ON_ZOOM_START"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ON_ZOOM_START"
id: -o-n_-z-o-o-m_-s-t-a-r-t
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/-o-n_-z-o-o-m_-s-t-a-r-t"
---
# ON_ZOOM_START

@SerialName(value = "zoomstart")ON_ZOOM_STARTTriggered just before the map begins a transition from one zoom level to another, as the result of either user interaction or methods such as flyTo.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/entries.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event"
---
# entries

val entries: EnumEntries<MTEvent>Returns a representation of an immutable list of all enum entries, in the order they're declared.This method may be used to iterate over the enum entries.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/index.html

---
layout: mobile_sdk
title: "MTEvent"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTEvent"
id: -m-t-event
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event"
---
# MTEvent

@Serializableenum MTEvent : Enum<MTEvent> Events triggered by the SDK.

MembersEntries

## Entries

ON_BOX_ZOOM_CANCEL

@SerialName(value = "boxzoomcancel")ON_BOX_ZOOM_CANCELTriggered when the user cancels a "box zoom" interaction, or when the bounding box does not meet the minimum size threshold.

ON_BOX_ZOOM_END

@SerialName(value = "boxzoomend")ON_BOX_ZOOM_ENDTriggered when a "box zoom" interaction ends.

ON_BOX_ZOOM_START

@SerialName(value = "boxzoomstart")ON_BOX_ZOOM_STARTTriggered when a "box zoom" interaction starts.

ON_TAP

@SerialName(value = "click")ON_TAPTriggered when user taps and releases at the same point on the map.

ON_COOPERATIVE_GESTURE_PREVENTED

@SerialName(value = "cooperativegestureprevented")ON_COOPERATIVE_GESTURE_PREVENTEDTriggered whenever the cooperativeGestures option prevents a gesture from being handled by the map.

ON_DATA_UPDATE

@SerialName(value = "data")ON_DATA_UPDATETriggered when any map data loads or changes.

ON_DATA_UPDATE_ABORT

@SerialName(value = "dataabort")ON_DATA_UPDATE_ABORTTriggered when a request for one of the map's sources' tiles is aborted. Triggered when a request for one of the map's sources' data is aborted.

ON_DATA_UPDATE_START

@SerialName(value = "dataloading")ON_DATA_UPDATE_STARTTriggered when any map data (style, source, tile, etc) begins loading or changing asynchronously. All dataloading events are followed by a dataDidUpdate, dataUpdateDidAbort or error events.

ON_DOUBLE_TAP

@SerialName(value = "dblclick")ON_DOUBLE_TAPTriggered when a user taps and releases twice at the same point on the map in rapid succession.

ON_DRAG

@SerialName(value = "drag")ON_DRAGTriggered repeatedly during a "drag to pan" interaction.

ON_POPUP_OPEN

@SerialName(value = "popup.open")ON_POPUP_OPENTriggered when a popup is opened (added to the map).

ON_POPUP_CLOSE

@SerialName(value = "popup.close")ON_POPUP_CLOSETriggered when a popup is closed (removed from the map).

ON_DRAG_END

@SerialName(value = "dragend")ON_DRAG_ENDTriggered when a "drag to pan" interaction ends.

ON_DRAG_START

@SerialName(value = "dragstart")ON_DRAG_STARTTriggered when a "drag to pan" interaction starts.

ON_MARKER_DRAG

@SerialName(value = "marker.drag")ON_MARKER_DRAGTriggered repeatedly while a marker is being dragged.

ON_MARKER_DRAG_END

@SerialName(value = "marker.dragend")ON_MARKER_DRAG_ENDTriggered when marker dragging ends.

ON_MARKER_DRAG_START

@SerialName(value = "marker.dragstart")ON_MARKER_DRAG_STARTTriggered when marker dragging starts.

ON_IDLE

@SerialName(value = "idle")ON_IDLETriggered after the last frame rendered before the map enters an "idle" state. Idle state means that no camera transitions are in progress, all currently requested tiles have loaded, and all fade/transition animations have completed.

ON_LOAD

@SerialName(value = "load")ON_LOADTriggered immediately after all necessary resources have been downloaded and the first visually complete rendering of the map has occurred.

ON_LOAD_WITH_TERRAIN

@SerialName(value = "loadWithTerrain")ON_LOAD_WITH_TERRAINTriggered only once in a Map instance lifecycle, when both the load event and the terrain event with non-null terrain are triggered.

ON_MOVE

@SerialName(value = "move")ON_MOVETriggered repeatedly during an animated transition from one view to another, as the result of either user interaction or methods such as flyTo.

ON_MOVE_END

@SerialName(value = "moveend")ON_MOVE_ENDTriggered just after the map completes a transition from one view to another, as the result of either user interaction or methods such as jumpTo.

ON_MOVE_START

@SerialName(value = "movestart")ON_MOVE_STARTTriggered just before the map begins a transition from one view to another, as the result of either user interaction or methods such as jumpTo.

ON_PITCH_UPDATE

@SerialName(value = "pitch")ON_PITCH_UPDATETriggered repeatedly during the map's pitch (tilt) animation between one state and another as the result of either user interaction or methods such as flyTo.

ON_PITCH_UPDATE_END

@SerialName(value = "pitchend")ON_PITCH_UPDATE_ENDTriggered immediately after the map's pitch (tilt) finishes changing as the result of either user interaction or methods such as flyTo.

ON_PITCH_UPDATE_START

@SerialName(value = "pitchstart")ON_PITCH_UPDATE_STARTTriggered whenever the map's pitch (tilt) begins a change as the result of either user interaction or methods such as flyTo.

ON_PROJECTION_MODIFY

@SerialName(value = "projectiontransition")ON_PROJECTION_MODIFYTriggered when map's projection is modified in other ways than by map being moved.

ON_READY

@SerialName(value = "ready")ON_READYTriggered only once after load and wait for all the controls managed by the Map constructor to be dealt with. Since the ready event waits that all the basic controls are nicely positioned, it is safer to use ready than load if you plan to add other custom controls.

ON_REMOVE

@SerialName(value = "remove")ON_REMOVETriggered immediately after the map has been removed.

ON_RENDER

@SerialName(value = "render")ON_RENDERTriggered whenever the map is drawn to the screen. Drawing occurs with a change to the map's position, zoom, pitch, or bearing, a change to the map's style, a change to a GeoJSON source, or the loading of a vector tile, GeoJSON file, glyph, or sprite.

ON_RESIZE

@SerialName(value = "resize")ON_RESIZETriggered immediately after the map has been resized.

ON_ROTATE

@SerialName(value = "rotate")ON_ROTATETriggered repeatedly during a "drag to rotate" interaction.

ON_ROTATE_END

@SerialName(value = "rotateend")ON_ROTATE_ENDTriggered when a "drag to rotate" interaction ends.

ON_ROTATE_START

@SerialName(value = "rotatestart")ON_ROTATE_STARTTriggered when a "drag to rotate" interaction starts.

ON_SOURCE_UPDATE

@SerialName(value = "sourcedata")ON_SOURCE_UPDATETriggered when one of the map's sources loads or changes, including if a tile belonging to a source loads or changes.

ON_SOURCE_UPDATE_ABORT

@SerialName(value = "sourcedataabort")ON_SOURCE_UPDATE_ABORTTriggered when a request for one of the map's sources' data is aborted.

ON_SOURCE_UPDATE_START

@SerialName(value = "sourcedataloading")ON_SOURCE_UPDATE_STARTTriggered when one of the map's sources begins loading or changing asynchronously. All sourceUpdateDidStart events are followed by a sourceDidUpdate, sourceUpdateDidAbort or error events.

ON_STYLE_UPDATE

@SerialName(value = "styledata")ON_STYLE_UPDATETriggered when the map's style loads or changes.

ON_STYLE_UPDATE_START

@SerialName(value = "styledataloading")ON_STYLE_UPDATE_STARTTriggered when the map's style begins loading or changing asynchronously. All styleUpdateDidStart events are followed by a styleDidUpdate or error events.

ON_STYLE_IMAGE_MISSING

@SerialName(value = "styleimagemissing")ON_STYLE_IMAGE_MISSINGTriggered when an icon or pattern needed by the style is missing.

ON_TERRAIN_CHANGE

@SerialName(value = "terrain")ON_TERRAIN_CHANGETriggered when a terrain event occurs within the map.

ON_TERRAIN_ANIMATION_START

@SerialName(value = "terrainAnimationStart")ON_TERRAIN_ANIMATION_STARTThe terrainAnimationDidStart event is triggered when the animation begins transitioning between terrain and non-terrain states.

ON_TERRAIN_ANIMATION_STOP

@SerialName(value = "terrainAnimationStop")ON_TERRAIN_ANIMATION_STOPThe terrainAnimationDidStop event is triggered when the animation between terrain and non-terrain states ends.

ON_TOUCH_CANCEL

@SerialName(value = "touchcancel")ON_TOUCH_CANCELTriggered when a touch is cancelled within the map.

ON_TOUCH_END

@SerialName(value = "touchend")ON_TOUCH_ENDTriggered when a touch ends within the map.

ON_TOUCH_MOVE

@SerialName(value = "touchmove")ON_TOUCH_MOVETriggered when a touch moves within the map.

ON_TOUCH_START

@SerialName(value = "touchstart")ON_TOUCH_STARTTriggered when a touch starts within the map.

ON_ZOOM

@SerialName(value = "zoom")ON_ZOOMTriggered repeatedly during an animated transition from one zoom level to another, as the result of either user interaction or methods such as flyTo.

ON_ZOOM_END

@SerialName(value = "zoomend")ON_ZOOM_ENDTriggered just after the map completes a transition from one zoom level to another, as the result of either user interaction or methods such as flyTo.

ON_ZOOM_START

@SerialName(value = "zoomstart")ON_ZOOM_STARTTriggered just before the map begins a transition from one zoom level to another, as the result of either user interaction or methods such as flyTo.

## Properties

entries

val entries: EnumEntries<MTEvent>Returns a representation of an immutable list of all enum entries, in the order they're declared.

name

val name: String

ordinal

val ordinal: Int

## Functions

valueOf

fun valueOf(value: String): MTEventReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

values

fun values(): Array<MTEvent>Returns an array containing the constants of this enum type, in the order they're declared.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/value-of.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event"
---
# valueOf

fun valueOf(value: String): MTEventReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
#### Throws

IllegalArgumentExceptionif this enum type has no constant with the specified name

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event/values.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events/-m-t-event"
---
# values

fun values(): Array<MTEvent>Returns an array containing the constants of this enum type, in the order they're declared.This method may be used to iterate over the constants.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.events/index.html

---
layout: mobile_sdk
title: "com.maptiler.maptilersdk.events"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "com.maptiler.maptilersdk.events"
id: com.maptiler.maptilersdk.events
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.events"
---
# com.maptiler.maptilersdk.events

Types

## Types

EventProcessor

class EventProcessor

EventProcessorDelegate

interface EventProcessorDelegate

MTEvent

@Serializableenum MTEvent : Enum<MTEvent> Events triggered by the SDK.

---

