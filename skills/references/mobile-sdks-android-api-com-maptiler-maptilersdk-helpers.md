# MapTiler Android SDK API Reference - com.maptiler.maptilersdk.helpers

This document is a part of the Android SDK API reference documentation, covering the `com.maptiler.maptilersdk.helpers` package.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-json-config/index.html

---
layout: mobile_sdk
title: "JsonConfig"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "JsonConfig"
id: -json-config
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-json-config"
---
# JsonConfig

object JsonConfig

Members

## Properties

json

val json: Json

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-json-config/json.html

---
layout: mobile_sdk
title: "json"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "json"
id: json
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-json-config"
---
# json

val json: Json

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-benchmark/-m-t-benchmark.html

---
layout: mobile_sdk
title: "MTBenchmark"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTBenchmark"
id: -m-t-benchmark
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-benchmark"
---
# MTBenchmark

constructor(context: Context)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-benchmark/-map.html

---
layout: mobile_sdk
title: "Map"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Map"
id: -map
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-benchmark"
---
# Map

@Composablefun Map(modifier: Modifier = Modifier, styleVariant: MTMapStyleVariant? = null)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-benchmark/benchmark-j-s.html

---
layout: mobile_sdk
title: "benchmarkJS"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "benchmarkJS"
id: benchmark-j-s
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-benchmark"
---
# benchmarkJS

suspend fun benchmarkJS()

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-benchmark/benchmark-kotlin.html

---
layout: mobile_sdk
title: "benchmarkKotlin"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "benchmarkKotlin"
id: benchmark-kotlin
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-benchmark"
---
# benchmarkKotlin

suspend fun benchmarkKotlin()

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-benchmark/benchmark-single-source-multiple-layers.html

---
layout: mobile_sdk
title: "benchmarkSingleSourceMultipleLayers"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "benchmarkSingleSourceMultipleLayers"
id: benchmark-single-source-multiple-layers
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-benchmark"
---
# benchmarkSingleSourceMultipleLayers

suspend fun benchmarkSingleSourceMultipleLayers(tileTemplate: String = ARCGIS_TILE_TEMPLATE, sourceLayerName: String = "Parcels")

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-benchmark/controller.html

---
layout: mobile_sdk
title: "controller"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "controller"
id: controller
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-benchmark"
---
# controller

val controller: MTMapViewController

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-benchmark/index.html

---
layout: mobile_sdk
title: "MTBenchmark"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTBenchmark"
id: -m-t-benchmark
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-benchmark"
---
# MTBenchmark

class MTBenchmark(context: Context) : MTMapViewDelegateBasic benchmarking helper for Kotlin SDK.

Members

## Constructors

MTBenchmark

constructor(context: Context)

## Properties

controller

val controller: MTMapViewController

onLog

var onLog: (String) -> Unit?

options

val options: MTMapOptions

referenceStyle

val referenceStyle: MTMapReferenceStyle

## Functions

benchmarkJS

suspend fun benchmarkJS()

benchmarkKotlin

suspend fun benchmarkKotlin()

benchmarkSingleSourceMultipleLayers

suspend fun benchmarkSingleSourceMultipleLayers(tileTemplate: String = ARCGIS_TILE_TEMPLATE, sourceLayerName: String = "Parcels")

Map

@Composablefun Map(modifier: Modifier = Modifier, styleVariant: MTMapStyleVariant? = null)

onEventTriggered

open override fun onEventTriggered(event: MTEvent, data: MTData?)

onMapViewInitialized

open override fun onMapViewInitialized()

runGeoJSONSingleSourceMultipleSymbolLayers

suspend fun runGeoJSONSingleSourceMultipleSymbolLayers(count: Int, dataUrl: String = "https://docs.maptiler.com/sdk-js/assets/earthquakes.geojson")

runMultipleSourceAndMultipleLayers

suspend fun runMultipleSourceAndMultipleLayers()

runSingleSourceMultipleLayers

suspend fun runSingleSourceMultipleLayers(count: Int, tileTemplate: String = ARCGIS_TILE_TEMPLATE, sourceLayerName: String = "Parcels")

setApiKey

fun setApiKey(key: String)

startStressTest

suspend fun startStressTest(iterations: Int, markersAreOn: Boolean, markerCount: Int)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-benchmark/on-event-triggered.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-benchmark"
---
# onEventTriggered

open override fun onEventTriggered(event: MTEvent, data: MTData?)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-benchmark/on-log.html

---
layout: mobile_sdk
title: "onLog"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "onLog"
id: on-log
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-benchmark"
---
# onLog

var onLog: (String) -> Unit?

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-benchmark/on-map-view-initialized.html

---
layout: mobile_sdk
title: "onMapViewInitialized"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "onMapViewInitialized"
id: on-map-view-initialized
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-benchmark"
---
# onMapViewInitialized

open override fun onMapViewInitialized()

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-benchmark/options.html

---
layout: mobile_sdk
title: "options"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "options"
id: options
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-benchmark"
---
# options

val options: MTMapOptions

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-benchmark/reference-style.html

---
layout: mobile_sdk
title: "referenceStyle"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "referenceStyle"
id: reference-style
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-benchmark"
---
# referenceStyle

val referenceStyle: MTMapReferenceStyle

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-benchmark/run-geo-j-s-o-n-single-source-multiple-symbol-layers.html

---
layout: mobile_sdk
title: "runGeoJSONSingleSourceMultipleSymbolLayers"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "runGeoJSONSingleSourceMultipleSymbolLayers"
id: run-geo-j-s-o-n-single-source-multiple-symbol-layers
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-benchmark"
---
# runGeoJSONSingleSourceMultipleSymbolLayers

suspend fun runGeoJSONSingleSourceMultipleSymbolLayers(count: Int, dataUrl: String = "https://docs.maptiler.com/sdk-js/assets/earthquakes.geojson")

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-benchmark/run-multiple-source-and-multiple-layers.html

---
layout: mobile_sdk
title: "runMultipleSourceAndMultipleLayers"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "runMultipleSourceAndMultipleLayers"
id: run-multiple-source-and-multiple-layers
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-benchmark"
---
# runMultipleSourceAndMultipleLayers

suspend fun runMultipleSourceAndMultipleLayers()

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-benchmark/run-single-source-multiple-layers.html

---
layout: mobile_sdk
title: "runSingleSourceMultipleLayers"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "runSingleSourceMultipleLayers"
id: run-single-source-multiple-layers
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-benchmark"
---
# runSingleSourceMultipleLayers

suspend fun runSingleSourceMultipleLayers(count: Int, tileTemplate: String = ARCGIS_TILE_TEMPLATE, sourceLayerName: String = "Parcels")

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-benchmark/set-api-key.html

---
layout: mobile_sdk
title: "setApiKey"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setApiKey"
id: set-api-key
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-benchmark"
---
# setApiKey

fun setApiKey(key: String)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-benchmark/start-stress-test.html

---
layout: mobile_sdk
title: "startStressTest"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "startStressTest"
id: start-stress-test
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-benchmark"
---
# startStressTest

suspend fun startStressTest(iterations: Int, markersAreOn: Boolean, markerCount: Int)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-color-value/-companion/from-color-int.html

---
layout: mobile_sdk
title: "fromColorInt"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "fromColorInt"
id: from-color-int
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-color-value/-companion"
---
# fromColorInt

fun fromColorInt(@ColorInt color: Int): MTColorValue

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-color-value/-companion/index.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-color-value/-companion"
---
# Companion

object Companion

Members

## Functions

fromColorInt

fun fromColorInt(@ColorInt color: Int): MTColorValue

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-color-value/-m-t-color-value.html

---
layout: mobile_sdk
title: "MTColorValue"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTColorValue"
id: -m-t-color-value
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-color-value"
---
# MTColorValue

constructor(raw: String)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-color-value/index.html

---
layout: mobile_sdk
title: "MTColorValue"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTColorValue"
id: -m-t-color-value
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-color-value"
---
# MTColorValue

@Serializable(with = MTColorValueAsStringSerializer::class)data class MTColorValue(val raw: String)Color wrapper that always encodes as a hex string. Accepts #RRGGBB or #RRGGBBAA (CSS hex). When constructed from a color int, outputs #RRGGBB if opaque, otherwise #RRGGBBAA (alpha at the end).

Members

## Constructors

MTColorValue

constructor(raw: String)

## Types

Companion

object Companion

## Properties

raw

val raw: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-color-value/raw.html

---
layout: mobile_sdk
title: "raw"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "raw"
id: raw
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-color-value"
---
# raw

val raw: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-color-value-as-string-serializer/descriptor.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-color-value-as-string-serializer"
---
# descriptor

open override val descriptor: SerialDescriptor

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-color-value-as-string-serializer/deserialize.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-color-value-as-string-serializer"
---
# deserialize

open override fun deserialize(decoder: Decoder): MTColorValue

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-color-value-as-string-serializer/index.html

---
layout: mobile_sdk
title: "MTColorValueAsStringSerializer"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTColorValueAsStringSerializer"
id: -m-t-color-value-as-string-serializer
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-color-value-as-string-serializer"
---
# MTColorValueAsStringSerializer

object MTColorValueAsStringSerializer : KSerializer<MTColorValue> 

Members

## Properties

descriptor

open override val descriptor: SerialDescriptor

## Functions

deserialize

open override fun deserialize(decoder: Decoder): MTColorValue

serialize

open override fun serialize(encoder: Encoder, value: MTColorValue)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-color-value-as-string-serializer/serialize.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-color-value-as-string-serializer"
---
# serialize

open override fun serialize(encoder: Encoder, value: MTColorValue)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-dash-array-option/-numbers/-numbers.html

---
layout: mobile_sdk
title: "Numbers"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Numbers"
id: -numbers
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-dash-array-option/-numbers"
---
# Numbers

constructor(values: List<Double>)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-dash-array-option/-numbers/index.html

---
layout: mobile_sdk
title: "Numbers"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Numbers"
id: -numbers
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-dash-array-option/-numbers"
---
# Numbers

data class Numbers(val values: List<Double>) : MTDashArrayOption

Members

## Constructors

Numbers

constructor(values: List<Double>)

## Properties

values

val values: List<Double>

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-dash-array-option/-numbers/values.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-dash-array-option/-numbers"
---
# values

val values: List<Double>

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-dash-array-option/-string-value/-string-value.html

---
layout: mobile_sdk
title: "StringValue"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "StringValue"
id: -string-value
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-dash-array-option/-string-value"
---
# StringValue

constructor(pattern: String)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-dash-array-option/-string-value/index.html

---
layout: mobile_sdk
title: "StringValue"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "StringValue"
id: -string-value
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-dash-array-option/-string-value"
---
# StringValue

data class StringValue(val pattern: String) : MTDashArrayOption

Members

## Constructors

StringValue

constructor(pattern: String)

## Properties

pattern

val pattern: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-dash-array-option/-string-value/pattern.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-dash-array-option/-string-value"
---
# pattern

val pattern: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-dash-array-option/index.html

---
layout: mobile_sdk
title: "MTDashArrayOption"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTDashArrayOption"
id: -m-t-dash-array-option
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-dash-array-option"
---
# MTDashArrayOption

@Serializable(with = MTDashArrayOptionSerializer::class)sealed class MTDashArrayOptionDash array option accepting either an array of numbers or the underscore/space pattern string.
#### Inheritors

NumbersStringValue

Members

## Types

Numbers

data class Numbers(val values: List<Double>) : MTDashArrayOption

StringValue

data class StringValue(val pattern: String) : MTDashArrayOption

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-dash-array-option-serializer/descriptor.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-dash-array-option-serializer"
---
# descriptor

open override val descriptor: SerialDescriptor

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-dash-array-option-serializer/deserialize.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-dash-array-option-serializer"
---
# deserialize

open override fun deserialize(decoder: Decoder): MTDashArrayOption

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-dash-array-option-serializer/index.html

---
layout: mobile_sdk
title: "MTDashArrayOptionSerializer"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTDashArrayOptionSerializer"
id: -m-t-dash-array-option-serializer
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-dash-array-option-serializer"
---
# MTDashArrayOptionSerializer

object MTDashArrayOptionSerializer : KSerializer<MTDashArrayOption> 

Members

## Properties

descriptor

open override val descriptor: SerialDescriptor

## Functions

deserialize

open override fun deserialize(decoder: Decoder): MTDashArrayOption

serialize

open override fun serialize(encoder: Encoder, value: MTDashArrayOption)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-dash-array-option-serializer/serialize.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-dash-array-option-serializer"
---
# serialize

open override fun serialize(encoder: Encoder, value: MTDashArrayOption)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-heatmap-layer-helper/-m-t-heatmap-layer-helper.html

---
layout: mobile_sdk
title: "MTHeatmapLayerHelper"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTHeatmapLayerHelper"
id: -m-t-heatmap-layer-helper
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-heatmap-layer-helper"
---
# MTHeatmapLayerHelper

constructor(style: MTStyle)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-heatmap-layer-helper/add-heatmap.html

---
layout: mobile_sdk
title: "addHeatmap"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "addHeatmap"
id: add-heatmap
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-heatmap-layer-helper"
---
# addHeatmap

fun addHeatmap(options: MTHeatmapLayerOptions)Adds a heatmap layer based on the provided options.fun addHeatmap(options: MTHeatmapLayerOptions, colorRamp: MTColorRamp?)Adds a heatmap layer using a color ramp.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-heatmap-layer-helper/index.html

---
layout: mobile_sdk
title: "MTHeatmapLayerHelper"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTHeatmapLayerHelper"
id: -m-t-heatmap-layer-helper
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-heatmap-layer-helper"
---
# MTHeatmapLayerHelper

class MTHeatmapLayerHelper(style: MTStyle) : MTVectorLayerHelperHelper for creating a heatmap visualization layer from data and styling options.

Members

## Constructors

MTHeatmapLayerHelper

constructor(style: MTStyle)

## Properties

defaultMaxZoom

open val defaultMaxZoom: Double

defaultMinZoom

open val defaultMinZoom: Double

defaultOutline

open val defaultOutline: Boolean

defaultOutlineColor

open val defaultOutlineColor: MTStringOrZoomStringValues

defaultOutlineOpacity

open val defaultOutlineOpacity: MTNumberOrZoomNumberValues

defaultOutlineWidth

open val defaultOutlineWidth: MTNumberOrZoomNumberValues

## Functions

addHeatmap

fun addHeatmap(options: MTHeatmapLayerOptions)Adds a heatmap layer based on the provided options.fun addHeatmap(options: MTHeatmapLayerOptions, colorRamp: MTColorRamp?)Adds a heatmap layer using a color ramp.

withCommonDefaults

open fun withCommonDefaults(options: MTHeatmapLayerOptions): MTHeatmapLayerOptionsApply common defaults to heatmap helper options when not provided.open fun withCommonDefaults(options: MTPointLayerOptions): MTPointLayerOptionsApply common defaults to point helper options when not provided.open fun withCommonDefaults(options: MTPolygonLayerOptions): MTPolygonLayerOptionsApply common defaults to polygon helper options when not provided.open fun withCommonDefaults(options: MTPolylineLayerOptions): MTPolylineLayerOptionsApply common defaults to polyline helper options when not provided.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-heatmap-layer-options/-m-t-heatmap-layer-options.html

---
layout: mobile_sdk
title: "MTHeatmapLayerOptions"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTHeatmapLayerOptions"
id: -m-t-heatmap-layer-options
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-heatmap-layer-options"
---
# MTHeatmapLayerOptions

constructor(data: String, layerId: String? = null, sourceId: String? = null, beforeId: String? = null, minzoom: Double? = null, maxzoom: Double? = null, colorRamp: MTColorRamp? = null, property: String? = null, weight: Double? = null, radius: Double? = null, opacity: Double? = null, intensity: Double? = null, zoomCompensation: Boolean? = null)constructor(data: String, layerId: String? = null, sourceId: String? = null, beforeId: String? = null, minzoom: Double? = null, maxzoom: Double? = null, colorRamp: MTColorRamp? = null, property: String? = null, weight: MTNumberOrPropertyValues? = null, radius: MTRadiusOption? = null, opacity: MTNumberOrZoomNumberValues? = null, intensity: MTNumberOrZoomNumberValues? = null, zoomCompensation: Boolean? = null)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-heatmap-layer-options/before-id.html

---
layout: mobile_sdk
title: "beforeId"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "beforeId"
id: before-id
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-heatmap-layer-options"
---
# beforeId

val beforeId: String? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-heatmap-layer-options/color-ramp.html

---
layout: mobile_sdk
title: "colorRamp"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "colorRamp"
id: color-ramp
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-heatmap-layer-options"
---
# colorRamp

val colorRamp: MTColorRamp? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-heatmap-layer-options/data.html

---
layout: mobile_sdk
title: "data"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "data"
id: data
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-heatmap-layer-options"
---
# data

val data: StringA geojson feature collection string or URL/UUID to be resolved.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-heatmap-layer-options/index.html

---
layout: mobile_sdk
title: "MTHeatmapLayerOptions"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTHeatmapLayerOptions"
id: -m-t-heatmap-layer-options
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-heatmap-layer-options"
---
# MTHeatmapLayerOptions

data class MTHeatmapLayerOptions(val data: String, val layerId: String? = null, val sourceId: String? = null, val beforeId: String? = null, val minzoom: Double? = null, val maxzoom: Double? = null, val colorRamp: MTColorRamp? = null, val property: String? = null, val weight: MTNumberOrPropertyValues? = null, val radius: MTRadiusOption? = null, val opacity: MTNumberOrZoomNumberValues? = null, val intensity: MTNumberOrZoomNumberValues? = null, val zoomCompensation: Boolean? = null)Options for building a heatmap visualization layer through the helper.

Members

## Constructors

MTHeatmapLayerOptions

constructor(data: String, layerId: String? = null, sourceId: String? = null, beforeId: String? = null, minzoom: Double? = null, maxzoom: Double? = null, colorRamp: MTColorRamp? = null, property: String? = null, weight: Double? = null, radius: Double? = null, opacity: Double? = null, intensity: Double? = null, zoomCompensation: Boolean? = null)constructor(data: String, layerId: String? = null, sourceId: String? = null, beforeId: String? = null, minzoom: Double? = null, maxzoom: Double? = null, colorRamp: MTColorRamp? = null, property: String? = null, weight: MTNumberOrPropertyValues? = null, radius: MTRadiusOption? = null, opacity: MTNumberOrZoomNumberValues? = null, intensity: MTNumberOrZoomNumberValues? = null, zoomCompensation: Boolean? = null)

## Properties

beforeId

val beforeId: String? = null

colorRamp

val colorRamp: MTColorRamp? = null

data

val data: StringA geojson feature collection string or URL/UUID to be resolved.

intensity

val intensity: MTNumberOrZoomNumberValues? = null

layerId

val layerId: String? = null

maxzoom

val maxzoom: Double? = null

minzoom

val minzoom: Double? = null

opacity

val opacity: MTNumberOrZoomNumberValues? = null

property

val property: String? = null

radius

val radius: MTRadiusOption? = null

sourceId

val sourceId: String? = null

weight

val weight: MTNumberOrPropertyValues? = null

zoomCompensation

val zoomCompensation: Boolean? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-heatmap-layer-options/intensity.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-heatmap-layer-options"
---
# intensity

val intensity: MTNumberOrZoomNumberValues? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-heatmap-layer-options/layer-id.html

---
layout: mobile_sdk
title: "layerId"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "layerId"
id: layer-id
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-heatmap-layer-options"
---
# layerId

val layerId: String? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-heatmap-layer-options/maxzoom.html

---
layout: mobile_sdk
title: "maxzoom"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "maxzoom"
id: maxzoom
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-heatmap-layer-options"
---
# maxzoom

val maxzoom: Double? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-heatmap-layer-options/minzoom.html

---
layout: mobile_sdk
title: "minzoom"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "minzoom"
id: minzoom
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-heatmap-layer-options"
---
# minzoom

val minzoom: Double? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-heatmap-layer-options/opacity.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-heatmap-layer-options"
---
# opacity

val opacity: MTNumberOrZoomNumberValues? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-heatmap-layer-options/property.html

---
layout: mobile_sdk
title: "property"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "property"
id: property
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-heatmap-layer-options"
---
# property

val property: String? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-heatmap-layer-options/radius.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-heatmap-layer-options"
---
# radius

val radius: MTRadiusOption? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-heatmap-layer-options/source-id.html

---
layout: mobile_sdk
title: "sourceId"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "sourceId"
id: source-id
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-heatmap-layer-options"
---
# sourceId

val sourceId: String? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-heatmap-layer-options/weight.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-heatmap-layer-options"
---
# weight

val weight: MTNumberOrPropertyValues? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-heatmap-layer-options/zoom-compensation.html

---
layout: mobile_sdk
title: "zoomCompensation"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "zoomCompensation"
id: zoom-compensation
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-heatmap-layer-options"
---
# zoomCompensation

val zoomCompensation: Boolean? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-helper-property-value/-m-t-helper-property-value.html

---
layout: mobile_sdk
title: "MTHelperPropertyValue"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTHelperPropertyValue"
id: -m-t-helper-property-value
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-helper-property-value"
---
# MTHelperPropertyValue

constructor(propertyValue: Double, value: Double)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-helper-property-value/index.html

---
layout: mobile_sdk
title: "MTHelperPropertyValue"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTHelperPropertyValue"
id: -m-t-helper-property-value
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-helper-property-value"
---
# MTHelperPropertyValue

@Serializabledata class MTHelperPropertyValue(val propertyValue: Double, val value: Double)Property/value pair for data-driven styles.

Members

## Constructors

MTHelperPropertyValue

constructor(propertyValue: Double, value: Double)

## Properties

propertyValue

val propertyValue: Double

value

val value: Double

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-helper-property-value/property-value.html

---
layout: mobile_sdk
title: "propertyValue"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "propertyValue"
id: property-value
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-helper-property-value"
---
# propertyValue

val propertyValue: Double

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-helper-property-value/value.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-helper-property-value"
---
# value

val value: Double

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-property-values/-number/-number.html

---
layout: mobile_sdk
title: "Number"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Number"
id: -number
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-property-values/-number"
---
# Number

constructor(value: Double)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-property-values/-number/index.html

---
layout: mobile_sdk
title: "Number"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Number"
id: -number
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-property-values/-number"
---
# Number

data class Number(val value: Double) : MTNumberOrPropertyValues

Members

## Constructors

Number

constructor(value: Double)

## Properties

value

val value: Double

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-property-values/-number/value.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-property-values/-number"
---
# value

val value: Double

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-property-values/-property-map/-property-map.html

---
layout: mobile_sdk
title: "PropertyMap"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "PropertyMap"
id: -property-map
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-property-values/-property-map"
---
# PropertyMap

constructor(values: MTPropertyValues)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-property-values/-property-map/index.html

---
layout: mobile_sdk
title: "PropertyMap"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "PropertyMap"
id: -property-map
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-property-values/-property-map"
---
# PropertyMap

data class PropertyMap(val values: MTPropertyValues) : MTNumberOrPropertyValues

Members

## Constructors

PropertyMap

constructor(values: MTPropertyValues)

## Properties

values

val values: MTPropertyValues

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-property-values/-property-map/values.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-property-values/-property-map"
---
# values

val values: MTPropertyValues

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-property-values/index.html

---
layout: mobile_sdk
title: "MTNumberOrPropertyValues"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTNumberOrPropertyValues"
id: -m-t-number-or-property-values
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-property-values"
---
# MTNumberOrPropertyValues

@Serializable(with = MTNumberOrPropertyValuesSerializer::class)sealed class MTNumberOrPropertyValuesnumber | PropertyValues
#### Inheritors

NumberPropertyMap

Members

## Types

Number

data class Number(val value: Double) : MTNumberOrPropertyValues

PropertyMap

data class PropertyMap(val values: MTPropertyValues) : MTNumberOrPropertyValues

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-property-values-serializer/descriptor.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-property-values-serializer"
---
# descriptor

open override val descriptor: SerialDescriptor

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-property-values-serializer/deserialize.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-property-values-serializer"
---
# deserialize

open override fun deserialize(decoder: Decoder): MTNumberOrPropertyValues

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-property-values-serializer/index.html

---
layout: mobile_sdk
title: "MTNumberOrPropertyValuesSerializer"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTNumberOrPropertyValuesSerializer"
id: -m-t-number-or-property-values-serializer
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-property-values-serializer"
---
# MTNumberOrPropertyValuesSerializer

object MTNumberOrPropertyValuesSerializer : KSerializer<MTNumberOrPropertyValues> 

Members

## Properties

descriptor

open override val descriptor: SerialDescriptor

## Functions

deserialize

open override fun deserialize(decoder: Decoder): MTNumberOrPropertyValues

serialize

open override fun serialize(encoder: Encoder, value: MTNumberOrPropertyValues)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-property-values-serializer/serialize.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-property-values-serializer"
---
# serialize

open override fun serialize(encoder: Encoder, value: MTNumberOrPropertyValues)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-zoom-number-values/-number/-number.html

---
layout: mobile_sdk
title: "Number"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Number"
id: -number
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-zoom-number-values/-number"
---
# Number

constructor(value: Double)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-zoom-number-values/-number/index.html

---
layout: mobile_sdk
title: "Number"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Number"
id: -number
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-zoom-number-values/-number"
---
# Number

data class Number(val value: Double) : MTNumberOrZoomNumberValues

Members

## Constructors

Number

constructor(value: Double)

## Properties

value

val value: Double

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-zoom-number-values/-number/value.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-zoom-number-values/-number"
---
# value

val value: Double

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-zoom-number-values/-ramp/-ramp.html

---
layout: mobile_sdk
title: "Ramp"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Ramp"
id: -ramp
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-zoom-number-values/-ramp"
---
# Ramp

constructor(values: MTZoomNumberValues)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-zoom-number-values/-ramp/index.html

---
layout: mobile_sdk
title: "Ramp"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Ramp"
id: -ramp
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-zoom-number-values/-ramp"
---
# Ramp

data class Ramp(val values: MTZoomNumberValues) : MTNumberOrZoomNumberValues

Members

## Constructors

Ramp

constructor(values: MTZoomNumberValues)

## Properties

values

val values: MTZoomNumberValues

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-zoom-number-values/-ramp/values.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-zoom-number-values/-ramp"
---
# values

val values: MTZoomNumberValues

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-zoom-number-values/index.html

---
layout: mobile_sdk
title: "MTNumberOrZoomNumberValues"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTNumberOrZoomNumberValues"
id: -m-t-number-or-zoom-number-values
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-zoom-number-values"
---
# MTNumberOrZoomNumberValues

@Serializable(with = MTNumberOrZoomNumberValuesSerializer::class)sealed class MTNumberOrZoomNumberValuesnumber | ZoomNumberValues
#### Inheritors

NumberRamp

Members

## Types

Number

data class Number(val value: Double) : MTNumberOrZoomNumberValues

Ramp

data class Ramp(val values: MTZoomNumberValues) : MTNumberOrZoomNumberValues

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-zoom-number-values-serializer/descriptor.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-zoom-number-values-serializer"
---
# descriptor

open override val descriptor: SerialDescriptor

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-zoom-number-values-serializer/deserialize.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-zoom-number-values-serializer"
---
# deserialize

open override fun deserialize(decoder: Decoder): MTNumberOrZoomNumberValues

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-zoom-number-values-serializer/index.html

---
layout: mobile_sdk
title: "MTNumberOrZoomNumberValuesSerializer"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTNumberOrZoomNumberValuesSerializer"
id: -m-t-number-or-zoom-number-values-serializer
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-zoom-number-values-serializer"
---
# MTNumberOrZoomNumberValuesSerializer

object MTNumberOrZoomNumberValuesSerializer : KSerializer<MTNumberOrZoomNumberValues> 

Members

## Properties

descriptor

open override val descriptor: SerialDescriptor

## Functions

deserialize

open override fun deserialize(decoder: Decoder): MTNumberOrZoomNumberValues

serialize

open override fun serialize(encoder: Encoder, value: MTNumberOrZoomNumberValues)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-zoom-number-values-serializer/serialize.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-number-or-zoom-number-values-serializer"
---
# serialize

open override fun serialize(encoder: Encoder, value: MTNumberOrZoomNumberValues)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-outline-position/-c-e-n-t-e-r/index.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-outline-position/-c-e-n-t-e-r"
---
# CENTER

CENTER

Members

## Properties

jsName

val jsName: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-outline-position/-i-n-s-i-d-e/index.html

---
layout: mobile_sdk
title: "INSIDE"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "INSIDE"
id: -i-n-s-i-d-e
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-outline-position/-i-n-s-i-d-e"
---
# INSIDE

INSIDE

Members

## Properties

jsName

val jsName: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-outline-position/-o-u-t-s-i-d-e/index.html

---
layout: mobile_sdk
title: "OUTSIDE"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "OUTSIDE"
id: -o-u-t-s-i-d-e
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-outline-position/-o-u-t-s-i-d-e"
---
# OUTSIDE

OUTSIDE

Members

## Properties

jsName

val jsName: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-outline-position/entries.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-outline-position"
---
# entries

val entries: EnumEntries<MTOutlinePosition>Returns a representation of an immutable list of all enum entries, in the order they're declared.This method may be used to iterate over the enum entries.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-outline-position/index.html

---
layout: mobile_sdk
title: "MTOutlinePosition"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTOutlinePosition"
id: -m-t-outline-position
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-outline-position"
---
# MTOutlinePosition

@Serializableenum MTOutlinePosition : Enum<MTOutlinePosition> Outline position relative to polygon edge.

MembersEntries

## Entries

CENTER

CENTER

INSIDE

INSIDE

OUTSIDE

OUTSIDE

## Properties

entries

val entries: EnumEntries<MTOutlinePosition>Returns a representation of an immutable list of all enum entries, in the order they're declared.

jsName

val jsName: String

name

val name: String

ordinal

val ordinal: Int

## Functions

valueOf

fun valueOf(value: String): MTOutlinePositionReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

values

fun values(): Array<MTOutlinePosition>Returns an array containing the constants of this enum type, in the order they're declared.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-outline-position/js-name.html

---
layout: mobile_sdk
title: "jsName"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "jsName"
id: js-name
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-outline-position"
---
# jsName

val jsName: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-outline-position/value-of.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-outline-position"
---
# valueOf

fun valueOf(value: String): MTOutlinePositionReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
#### Throws

IllegalArgumentExceptionif this enum type has no constant with the specified name

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-outline-position/values.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-outline-position"
---
# values

fun values(): Array<MTOutlinePosition>Returns an array containing the constants of this enum type, in the order they're declared.This method may be used to iterate over the constants.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-performance-presets/balanced-performance.html

---
layout: mobile_sdk
title: "balancedPerformance"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "balancedPerformance"
id: balanced-performance
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-performance-presets"
---
# balancedPerformance

fun balancedPerformance(base: MTMapOptions = MTMapOptions()): MTMapOptionsReturns a new MTMapOptions based on base with balanced performance defaults.Keeps crisper rendering by using a higher pixel ratio.Applied overrides:- pixelRatio = base.pixelRatio ?: 1.5 (sharper than 1.0)
- shouldRefreshExpiredTiles = false
- cancelPendingTileRequestsWhileZooming = true
- maxTileCacheZoomLevels = 4.0 (if unset)
- crossSourceCollisionsAreEnabled = false
- eventLevel = ESSENTIAL (per-frame events opt-in)
- highFrequencyEventThrottleMs = 150 (when ALL is enabled)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-performance-presets/high-fidelity.html

---
layout: mobile_sdk
title: "highFidelity"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "highFidelity"
id: high-fidelity
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-performance-presets"
---
# highFidelity

fun highFidelity(base: MTMapOptions = MTMapOptions()): MTMapOptionsReturns a new MTMapOptions based on base tuned for higher-end devices.Focuses on visual fidelity while keeping sensible performance guardrails.Applied overrides:- pixelRatio = base.pixelRatio ?: 2.0 (very crisp; test for memory on low-end)
- shouldRefreshExpiredTiles = true (prefer up-to-date tiles)
- cancelPendingTileRequestsWhileZooming = false (allow progressive detail during zoom)
- maxTileCacheZoomLevels = 6.0 (if unset) to reduce churn when navigating
- crossSourceCollisionsAreEnabled = base.crossSourceCollisionsAreEnabled ?: true
- eventLevel = ALL
- highFrequencyEventThrottleMs = 100 (slightly more responsive when ALL is enabled)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-performance-presets/index.html

---
layout: mobile_sdk
title: "MTPerformancePresets"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTPerformancePresets"
id: -m-t-performance-presets
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-performance-presets"
---
# MTPerformancePresets

object MTPerformancePresetsPerformance-oriented presets for MapTiler Kotlin SDK.

Members

## Functions

balancedPerformance

fun balancedPerformance(base: MTMapOptions = MTMapOptions()): MTMapOptionsReturns a new MTMapOptions based on base with balanced performance defaults.

highFidelity

fun highFidelity(base: MTMapOptions = MTMapOptions()): MTMapOptionsReturns a new MTMapOptions based on base tuned for higher-end devices.

leanPerformance

fun leanPerformance(base: MTMapOptions = MTMapOptions()): MTMapOptionsLean performance preset: prioritize responsiveness and bytes over fidelity.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-performance-presets/lean-performance.html

---
layout: mobile_sdk
title: "leanPerformance"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "leanPerformance"
id: lean-performance
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-performance-presets"
---
# leanPerformance

fun leanPerformance(base: MTMapOptions = MTMapOptions()): MTMapOptionsLean performance preset: prioritize responsiveness and bytes over fidelity.Applied overrides (favor performance over fidelity):- pixelRatio = 1.0
- shouldRefreshExpiredTiles = false
- cancelPendingTileRequestsWhileZooming = true
- maxTileCacheZoomLevels = 4.0 (if unset)
- crossSourceCollisionsAreEnabled = false
- eventLevel = ESSENTIAL (keeps low-frequency events; per-frame events opt-in)
- highFrequencyEventThrottleMs = 150 (when ALL is enabled)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-pitch-limit-helper/index.html

---
layout: mobile_sdk
title: "MTPitchLimitHelper"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTPitchLimitHelper"
id: -m-t-pitch-limit-helper
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-pitch-limit-helper"
---
# MTPitchLimitHelper

object MTPitchLimitHelperHelper object to configure pitch limits on the map.

Members

## Functions

limitPitch

fun limitPitch(controller: MTMapViewController, minPitch: Double = 0.0, maxPitch: Double = 85.0)Easily limits the pitch of the map.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-pitch-limit-helper/limit-pitch.html

---
layout: mobile_sdk
title: "limitPitch"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "limitPitch"
id: limit-pitch
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-pitch-limit-helper"
---
# limitPitch

fun limitPitch(controller: MTMapViewController, minPitch: Double = 0.0, maxPitch: Double = 85.0)Easily limits the pitch of the map.
#### Parameters

controllerThe map view controller to apply the limits to.minPitchThe minimum pitch limit (0 to 85 degrees). Defaults to 0.0.maxPitchThe maximum pitch limit (0 to 180 degrees). Defaults to 85.0.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-helper/-m-t-point-layer-helper.html

---
layout: mobile_sdk
title: "MTPointLayerHelper"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTPointLayerHelper"
id: -m-t-point-layer-helper
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-helper"
---
# MTPointLayerHelper

constructor(style: MTStyle)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-helper/add-point.html

---
layout: mobile_sdk
title: "addPoint"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "addPoint"
id: add-point
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-helper"
---
# addPoint

fun addPoint(options: MTPointLayerOptions)Adds a point layer based on the provided options.fun addPoint(options: MTPointLayerOptions, colorRamp: MTColorRamp)Adds a point layer using a color ramp for pointColor.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-helper/index.html

---
layout: mobile_sdk
title: "MTPointLayerHelper"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTPointLayerHelper"
id: -m-t-point-layer-helper
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-helper"
---
# MTPointLayerHelper

class MTPointLayerHelper(style: MTStyle) : MTVectorLayerHelperHelper for creating a point visualization layer from data and styling options.This uses the current style to create the underlying source and layers.

Members

## Constructors

MTPointLayerHelper

constructor(style: MTStyle)

## Properties

defaultMaxZoom

open val defaultMaxZoom: Double

defaultMinZoom

open val defaultMinZoom: Double

defaultOutline

open val defaultOutline: Boolean

defaultOutlineColor

open val defaultOutlineColor: MTStringOrZoomStringValues

defaultOutlineOpacity

open val defaultOutlineOpacity: MTNumberOrZoomNumberValues

defaultOutlineWidth

open val defaultOutlineWidth: MTNumberOrZoomNumberValues

## Functions

addPoint

fun addPoint(options: MTPointLayerOptions)Adds a point layer based on the provided options.fun addPoint(options: MTPointLayerOptions, colorRamp: MTColorRamp)Adds a point layer using a color ramp for pointColor.

withCommonDefaults

open fun withCommonDefaults(options: MTHeatmapLayerOptions): MTHeatmapLayerOptionsApply common defaults to heatmap helper options when not provided.open fun withCommonDefaults(options: MTPointLayerOptions): MTPointLayerOptionsApply common defaults to point helper options when not provided.open fun withCommonDefaults(options: MTPolygonLayerOptions): MTPolygonLayerOptionsApply common defaults to polygon helper options when not provided.open fun withCommonDefaults(options: MTPolylineLayerOptions): MTPolylineLayerOptionsApply common defaults to polyline helper options when not provided.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options/-m-t-point-layer-options.html

---
layout: mobile_sdk
title: "MTPointLayerOptions"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTPointLayerOptions"
id: -m-t-point-layer-options
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options"
---
# MTPointLayerOptions

constructor(data: String, layerId: String? = null, sourceId: String? = null, beforeId: String? = null, minzoom: Double? = null, maxzoom: Double? = null, outline: Boolean? = null, outlineColor: String? = null, outlineWidth: Double? = null, outlineOpacity: Double? = null, pointColor: String? = null, pointColorRamp: MTColorRamp? = null, pointRadius: Double? = null, minPointRadius: Double? = null, maxPointRadius: Double? = null, property: String? = null, pointOpacity: Double? = null, alignOnViewport: Boolean? = null, cluster: Boolean? = null, showLabel: Boolean? = null, labelColor: String? = null, labelSize: Double? = null, zoomCompensation: Boolean? = null)constructor(data: String, layerId: String? = null, sourceId: String? = null, beforeId: String? = null, minzoom: Double? = null, maxzoom: Double? = null, outline: Boolean? = null, outlineColor: MTStringOrZoomStringValues? = null, outlineWidth: MTNumberOrZoomNumberValues? = null, outlineOpacity: MTNumberOrZoomNumberValues? = null, pointColor: MTColorValue? = null, pointColorRamp: MTColorRamp? = null, pointRadius: MTNumberOrZoomNumberValues? = null, minPointRadius: Double? = null, maxPointRadius: Double? = null, property: String? = null, pointOpacity: MTNumberOrZoomNumberValues? = null, alignOnViewport: Boolean? = null, cluster: Boolean? = null, showLabel: Boolean? = null, labelColor: MTColorValue? = null, labelSize: Double? = null, zoomCompensation: Boolean? = null)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options/align-on-viewport.html

---
layout: mobile_sdk
title: "alignOnViewport"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "alignOnViewport"
id: align-on-viewport
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options"
---
# alignOnViewport

val alignOnViewport: Boolean? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options/before-id.html

---
layout: mobile_sdk
title: "beforeId"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "beforeId"
id: before-id
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options"
---
# beforeId

val beforeId: String? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options/cluster.html

---
layout: mobile_sdk
title: "cluster"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "cluster"
id: cluster
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options"
---
# cluster

val cluster: Boolean? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options/data.html

---
layout: mobile_sdk
title: "data"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "data"
id: data
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options"
---
# data

val data: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options/index.html

---
layout: mobile_sdk
title: "MTPointLayerOptions"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTPointLayerOptions"
id: -m-t-point-layer-options
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options"
---
# MTPointLayerOptions

@Serializabledata class MTPointLayerOptions(val data: String, val layerId: String? = null, val sourceId: String? = null, val beforeId: String? = null, val minzoom: Double? = null, val maxzoom: Double? = null, val outline: Boolean? = null, val outlineColor: MTStringOrZoomStringValues? = null, val outlineWidth: MTNumberOrZoomNumberValues? = null, val outlineOpacity: MTNumberOrZoomNumberValues? = null, val pointColor: MTColorValue? = null, val pointColorRamp: MTColorRamp? = null, val pointRadius: MTNumberOrZoomNumberValues? = null, val minPointRadius: Double? = null, val maxPointRadius: Double? = null, val property: String? = null, val pointOpacity: MTNumberOrZoomNumberValues? = null, val alignOnViewport: Boolean? = null, val cluster: Boolean? = null, val showLabel: Boolean? = null, val labelColor: MTColorValue? = null, val labelSize: Double? = null, val zoomCompensation: Boolean? = null)Options for building a point visualization layer through the helper.This mirrors the available configuration including common shape options.

Members

## Constructors

MTPointLayerOptions

constructor(data: String, layerId: String? = null, sourceId: String? = null, beforeId: String? = null, minzoom: Double? = null, maxzoom: Double? = null, outline: Boolean? = null, outlineColor: String? = null, outlineWidth: Double? = null, outlineOpacity: Double? = null, pointColor: String? = null, pointColorRamp: MTColorRamp? = null, pointRadius: Double? = null, minPointRadius: Double? = null, maxPointRadius: Double? = null, property: String? = null, pointOpacity: Double? = null, alignOnViewport: Boolean? = null, cluster: Boolean? = null, showLabel: Boolean? = null, labelColor: String? = null, labelSize: Double? = null, zoomCompensation: Boolean? = null)constructor(data: String, layerId: String? = null, sourceId: String? = null, beforeId: String? = null, minzoom: Double? = null, maxzoom: Double? = null, outline: Boolean? = null, outlineColor: MTStringOrZoomStringValues? = null, outlineWidth: MTNumberOrZoomNumberValues? = null, outlineOpacity: MTNumberOrZoomNumberValues? = null, pointColor: MTColorValue? = null, pointColorRamp: MTColorRamp? = null, pointRadius: MTNumberOrZoomNumberValues? = null, minPointRadius: Double? = null, maxPointRadius: Double? = null, property: String? = null, pointOpacity: MTNumberOrZoomNumberValues? = null, alignOnViewport: Boolean? = null, cluster: Boolean? = null, showLabel: Boolean? = null, labelColor: MTColorValue? = null, labelSize: Double? = null, zoomCompensation: Boolean? = null)

## Properties

alignOnViewport

val alignOnViewport: Boolean? = null

beforeId

val beforeId: String? = null

cluster

val cluster: Boolean? = null

data

val data: String

labelColor

val labelColor: MTColorValue? = null

labelSize

val labelSize: Double? = null

layerId

val layerId: String? = null

maxPointRadius

val maxPointRadius: Double? = null

maxzoom

val maxzoom: Double? = null

minPointRadius

val minPointRadius: Double? = null

minzoom

val minzoom: Double? = null

outline

val outline: Boolean? = null

outlineColor

val outlineColor: MTStringOrZoomStringValues? = null

outlineOpacity

val outlineOpacity: MTNumberOrZoomNumberValues? = null

outlineWidth

val outlineWidth: MTNumberOrZoomNumberValues? = null

pointColor

val pointColor: MTColorValue? = null

pointColorRamp

val pointColorRamp: MTColorRamp? = null

pointOpacity

val pointOpacity: MTNumberOrZoomNumberValues? = null

pointRadius

val pointRadius: MTNumberOrZoomNumberValues? = null

property

val property: String? = null

showLabel

val showLabel: Boolean? = null

sourceId

val sourceId: String? = null

zoomCompensation

val zoomCompensation: Boolean? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options/label-color.html

---
layout: mobile_sdk
title: "labelColor"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "labelColor"
id: label-color
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options"
---
# labelColor

val labelColor: MTColorValue? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options/label-size.html

---
layout: mobile_sdk
title: "labelSize"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "labelSize"
id: label-size
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options"
---
# labelSize

val labelSize: Double? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options/layer-id.html

---
layout: mobile_sdk
title: "layerId"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "layerId"
id: layer-id
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options"
---
# layerId

val layerId: String? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options/max-point-radius.html

---
layout: mobile_sdk
title: "maxPointRadius"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "maxPointRadius"
id: max-point-radius
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options"
---
# maxPointRadius

val maxPointRadius: Double? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options/maxzoom.html

---
layout: mobile_sdk
title: "maxzoom"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "maxzoom"
id: maxzoom
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options"
---
# maxzoom

val maxzoom: Double? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options/min-point-radius.html

---
layout: mobile_sdk
title: "minPointRadius"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "minPointRadius"
id: min-point-radius
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options"
---
# minPointRadius

val minPointRadius: Double? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options/minzoom.html

---
layout: mobile_sdk
title: "minzoom"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "minzoom"
id: minzoom
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options"
---
# minzoom

val minzoom: Double? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options/outline-color.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options"
---
# outlineColor

val outlineColor: MTStringOrZoomStringValues? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options/outline-opacity.html

---
layout: mobile_sdk
title: "outlineOpacity"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "outlineOpacity"
id: outline-opacity
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options"
---
# outlineOpacity

val outlineOpacity: MTNumberOrZoomNumberValues? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options/outline-width.html

---
layout: mobile_sdk
title: "outlineWidth"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "outlineWidth"
id: outline-width
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options"
---
# outlineWidth

val outlineWidth: MTNumberOrZoomNumberValues? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options/outline.html

---
layout: mobile_sdk
title: "outline"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "outline"
id: outline
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options"
---
# outline

val outline: Boolean? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options/point-color-ramp.html

---
layout: mobile_sdk
title: "pointColorRamp"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "pointColorRamp"
id: point-color-ramp
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options"
---
# pointColorRamp

val pointColorRamp: MTColorRamp? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options/point-color.html

---
layout: mobile_sdk
title: "pointColor"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "pointColor"
id: point-color
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options"
---
# pointColor

val pointColor: MTColorValue? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options/point-opacity.html

---
layout: mobile_sdk
title: "pointOpacity"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "pointOpacity"
id: point-opacity
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options"
---
# pointOpacity

val pointOpacity: MTNumberOrZoomNumberValues? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options/point-radius.html

---
layout: mobile_sdk
title: "pointRadius"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "pointRadius"
id: point-radius
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options"
---
# pointRadius

val pointRadius: MTNumberOrZoomNumberValues? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options/property.html

---
layout: mobile_sdk
title: "property"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "property"
id: property
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options"
---
# property

val property: String? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options/show-label.html

---
layout: mobile_sdk
title: "showLabel"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "showLabel"
id: show-label
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options"
---
# showLabel

val showLabel: Boolean? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options/source-id.html

---
layout: mobile_sdk
title: "sourceId"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "sourceId"
id: source-id
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options"
---
# sourceId

val sourceId: String? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options/zoom-compensation.html

---
layout: mobile_sdk
title: "zoomCompensation"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "zoomCompensation"
id: zoom-compensation
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-point-layer-options"
---
# zoomCompensation

val zoomCompensation: Boolean? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-helper/-m-t-polygon-layer-helper.html

---
layout: mobile_sdk
title: "MTPolygonLayerHelper"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTPolygonLayerHelper"
id: -m-t-polygon-layer-helper
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-helper"
---
# MTPolygonLayerHelper

constructor(style: MTStyle)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-helper/add-polygon.html

---
layout: mobile_sdk
title: "addPolygon"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "addPolygon"
id: add-polygon
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-helper"
---
# addPolygon

fun addPolygon(options: MTPolygonLayerOptions)Adds a polygon layer based on the provided options.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-helper/index.html

---
layout: mobile_sdk
title: "MTPolygonLayerHelper"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTPolygonLayerHelper"
id: -m-t-polygon-layer-helper
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-helper"
---
# MTPolygonLayerHelper

class MTPolygonLayerHelper(style: MTStyle) : MTVectorLayerHelperHelper for creating a polygon visualization layer from data and styling options.This uses the current style to create the underlying source and layers.

Members

## Constructors

MTPolygonLayerHelper

constructor(style: MTStyle)

## Properties

defaultMaxZoom

open val defaultMaxZoom: Double

defaultMinZoom

open val defaultMinZoom: Double

defaultOutline

open val defaultOutline: Boolean

defaultOutlineColor

open val defaultOutlineColor: MTStringOrZoomStringValues

defaultOutlineOpacity

open val defaultOutlineOpacity: MTNumberOrZoomNumberValues

defaultOutlineWidth

open val defaultOutlineWidth: MTNumberOrZoomNumberValues

## Functions

addPolygon

fun addPolygon(options: MTPolygonLayerOptions)Adds a polygon layer based on the provided options.

withCommonDefaults

open fun withCommonDefaults(options: MTHeatmapLayerOptions): MTHeatmapLayerOptionsApply common defaults to heatmap helper options when not provided.open fun withCommonDefaults(options: MTPointLayerOptions): MTPointLayerOptionsApply common defaults to point helper options when not provided.open fun withCommonDefaults(options: MTPolygonLayerOptions): MTPolygonLayerOptionsApply common defaults to polygon helper options when not provided.open fun withCommonDefaults(options: MTPolylineLayerOptions): MTPolylineLayerOptionsApply common defaults to polyline helper options when not provided.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options/-m-t-polygon-layer-options.html

---
layout: mobile_sdk
title: "MTPolygonLayerOptions"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTPolygonLayerOptions"
id: -m-t-polygon-layer-options
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options"
---
# MTPolygonLayerOptions

constructor(data: String, layerId: String? = null, sourceId: String? = null, beforeId: String? = null, minzoom: Double? = null, maxzoom: Double? = null, outline: Boolean? = null, outlineColor: String? = null, outlineWidth: Double? = null, outlineOpacity: Double? = null, fillColor: String? = null, fillOpacity: Double? = null, outlinePosition: String? = null, outlineDashPattern: String? = null, outlineCap: String? = null, outlineJoin: String? = null, pattern: String? = null, outlineBlur: Double? = null)Convenience constructor for simpler types (String colors and Double numerics, dash/cap/join/pattern as strings).constructor(data: String, layerId: String? = null, sourceId: String? = null, beforeId: String? = null, minzoom: Double? = null, maxzoom: Double? = null, outline: Boolean? = null, outlineColor: MTStringOrZoomStringValues? = null, outlineWidth: MTNumberOrZoomNumberValues? = null, outlineOpacity: MTNumberOrZoomNumberValues? = null, fillColor: MTStringOrZoomStringValues? = null, fillOpacity: MTNumberOrZoomNumberValues? = null, outlinePosition: MTOutlinePosition? = null, outlineDashArray: MTDashArrayOption? = null, outlineCap: MTLineCap? = null, outlineJoin: MTLineJoin? = null, pattern: String? = null, outlineBlur: MTNumberOrZoomNumberValues? = null)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options/before-id.html

---
layout: mobile_sdk
title: "beforeId"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "beforeId"
id: before-id
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options"
---
# beforeId

val beforeId: String? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options/data.html

---
layout: mobile_sdk
title: "data"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "data"
id: data
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options"
---
# data

val data: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options/fill-color.html

---
layout: mobile_sdk
title: "fillColor"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "fillColor"
id: fill-color
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options"
---
# fillColor

val fillColor: MTStringOrZoomStringValues? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options/fill-opacity.html

---
layout: mobile_sdk
title: "fillOpacity"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "fillOpacity"
id: fill-opacity
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options"
---
# fillOpacity

val fillOpacity: MTNumberOrZoomNumberValues? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options/index.html

---
layout: mobile_sdk
title: "MTPolygonLayerOptions"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTPolygonLayerOptions"
id: -m-t-polygon-layer-options
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options"
---
# MTPolygonLayerOptions

@Serializabledata class MTPolygonLayerOptions(val data: String, val layerId: String? = null, val sourceId: String? = null, val beforeId: String? = null, val minzoom: Double? = null, val maxzoom: Double? = null, val outline: Boolean? = null, val outlineColor: MTStringOrZoomStringValues? = null, val outlineWidth: MTNumberOrZoomNumberValues? = null, val outlineOpacity: MTNumberOrZoomNumberValues? = null, val fillColor: MTStringOrZoomStringValues? = null, val fillOpacity: MTNumberOrZoomNumberValues? = null, val outlinePosition: MTOutlinePosition? = null, val outlineDashArray: MTDashArrayOption? = null, val outlineCap: MTLineCap? = null, val outlineJoin: MTLineJoin? = null, val pattern: String? = null, val outlineBlur: MTNumberOrZoomNumberValues? = null)Options for building a polygon visualization layer through the helper.

Members

## Constructors

MTPolygonLayerOptions

constructor(data: String, layerId: String? = null, sourceId: String? = null, beforeId: String? = null, minzoom: Double? = null, maxzoom: Double? = null, outline: Boolean? = null, outlineColor: String? = null, outlineWidth: Double? = null, outlineOpacity: Double? = null, fillColor: String? = null, fillOpacity: Double? = null, outlinePosition: String? = null, outlineDashPattern: String? = null, outlineCap: String? = null, outlineJoin: String? = null, pattern: String? = null, outlineBlur: Double? = null)Convenience constructor for simpler types (String colors and Double numerics, dash/cap/join/pattern as strings).constructor(data: String, layerId: String? = null, sourceId: String? = null, beforeId: String? = null, minzoom: Double? = null, maxzoom: Double? = null, outline: Boolean? = null, outlineColor: MTStringOrZoomStringValues? = null, outlineWidth: MTNumberOrZoomNumberValues? = null, outlineOpacity: MTNumberOrZoomNumberValues? = null, fillColor: MTStringOrZoomStringValues? = null, fillOpacity: MTNumberOrZoomNumberValues? = null, outlinePosition: MTOutlinePosition? = null, outlineDashArray: MTDashArrayOption? = null, outlineCap: MTLineCap? = null, outlineJoin: MTLineJoin? = null, pattern: String? = null, outlineBlur: MTNumberOrZoomNumberValues? = null)

## Properties

beforeId

val beforeId: String? = null

data

val data: String

fillColor

val fillColor: MTStringOrZoomStringValues? = null

fillOpacity

val fillOpacity: MTNumberOrZoomNumberValues? = null

layerId

val layerId: String? = null

maxzoom

val maxzoom: Double? = null

minzoom

val minzoom: Double? = null

outline

val outline: Boolean? = null

outlineBlur

val outlineBlur: MTNumberOrZoomNumberValues? = null

outlineCap

val outlineCap: MTLineCap? = null

outlineColor

val outlineColor: MTStringOrZoomStringValues? = null

outlineDashArray

val outlineDashArray: MTDashArrayOption? = null

outlineJoin

val outlineJoin: MTLineJoin? = null

outlineOpacity

val outlineOpacity: MTNumberOrZoomNumberValues? = null

outlinePosition

val outlinePosition: MTOutlinePosition? = null

outlineWidth

val outlineWidth: MTNumberOrZoomNumberValues? = null

pattern

val pattern: String? = null

sourceId

val sourceId: String? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options/layer-id.html

---
layout: mobile_sdk
title: "layerId"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "layerId"
id: layer-id
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options"
---
# layerId

val layerId: String? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options/maxzoom.html

---
layout: mobile_sdk
title: "maxzoom"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "maxzoom"
id: maxzoom
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options"
---
# maxzoom

val maxzoom: Double? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options/minzoom.html

---
layout: mobile_sdk
title: "minzoom"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "minzoom"
id: minzoom
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options"
---
# minzoom

val minzoom: Double? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options/outline-blur.html

---
layout: mobile_sdk
title: "outlineBlur"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "outlineBlur"
id: outline-blur
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options"
---
# outlineBlur

val outlineBlur: MTNumberOrZoomNumberValues? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options/outline-cap.html

---
layout: mobile_sdk
title: "outlineCap"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "outlineCap"
id: outline-cap
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options"
---
# outlineCap

val outlineCap: MTLineCap? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options/outline-color.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options"
---
# outlineColor

val outlineColor: MTStringOrZoomStringValues? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options/outline-dash-array.html

---
layout: mobile_sdk
title: "outlineDashArray"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "outlineDashArray"
id: outline-dash-array
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options"
---
# outlineDashArray

val outlineDashArray: MTDashArrayOption? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options/outline-join.html

---
layout: mobile_sdk
title: "outlineJoin"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "outlineJoin"
id: outline-join
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options"
---
# outlineJoin

val outlineJoin: MTLineJoin? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options/outline-opacity.html

---
layout: mobile_sdk
title: "outlineOpacity"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "outlineOpacity"
id: outline-opacity
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options"
---
# outlineOpacity

val outlineOpacity: MTNumberOrZoomNumberValues? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options/outline-position.html

---
layout: mobile_sdk
title: "outlinePosition"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "outlinePosition"
id: outline-position
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options"
---
# outlinePosition

val outlinePosition: MTOutlinePosition? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options/outline-width.html

---
layout: mobile_sdk
title: "outlineWidth"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "outlineWidth"
id: outline-width
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options"
---
# outlineWidth

val outlineWidth: MTNumberOrZoomNumberValues? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options/outline.html

---
layout: mobile_sdk
title: "outline"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "outline"
id: outline
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options"
---
# outline

val outline: Boolean? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options/pattern.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options"
---
# pattern

val pattern: String? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options/source-id.html

---
layout: mobile_sdk
title: "sourceId"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "sourceId"
id: source-id
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polygon-layer-options"
---
# sourceId

val sourceId: String? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-helper/-m-t-polyline-layer-helper.html

---
layout: mobile_sdk
title: "MTPolylineLayerHelper"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTPolylineLayerHelper"
id: -m-t-polyline-layer-helper
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-helper"
---
# MTPolylineLayerHelper

constructor(style: MTStyle)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-helper/add-polyline.html

---
layout: mobile_sdk
title: "addPolyline"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "addPolyline"
id: add-polyline
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-helper"
---
# addPolyline

fun addPolyline(options: MTPolylineLayerOptions)Adds a polyline layer based on the provided options.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-helper/index.html

---
layout: mobile_sdk
title: "MTPolylineLayerHelper"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTPolylineLayerHelper"
id: -m-t-polyline-layer-helper
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-helper"
---
# MTPolylineLayerHelper

class MTPolylineLayerHelper(style: MTStyle) : MTVectorLayerHelperHelper for creating a polyline visualization layer from data and styling options.This uses the current style to create the underlying source and layers

Members

## Constructors

MTPolylineLayerHelper

constructor(style: MTStyle)

## Properties

defaultMaxZoom

open val defaultMaxZoom: Double

defaultMinZoom

open val defaultMinZoom: Double

defaultOutline

open val defaultOutline: Boolean

defaultOutlineColor

open val defaultOutlineColor: MTStringOrZoomStringValues

defaultOutlineOpacity

open val defaultOutlineOpacity: MTNumberOrZoomNumberValues

defaultOutlineWidth

open val defaultOutlineWidth: MTNumberOrZoomNumberValues

## Functions

addPolyline

fun addPolyline(options: MTPolylineLayerOptions)Adds a polyline layer based on the provided options.

withCommonDefaults

open fun withCommonDefaults(options: MTHeatmapLayerOptions): MTHeatmapLayerOptionsApply common defaults to heatmap helper options when not provided.open fun withCommonDefaults(options: MTPointLayerOptions): MTPointLayerOptionsApply common defaults to point helper options when not provided.open fun withCommonDefaults(options: MTPolygonLayerOptions): MTPolygonLayerOptionsApply common defaults to polygon helper options when not provided.open fun withCommonDefaults(options: MTPolylineLayerOptions): MTPolylineLayerOptionsApply common defaults to polyline helper options when not provided.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options/-m-t-polyline-layer-options.html

---
layout: mobile_sdk
title: "MTPolylineLayerOptions"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTPolylineLayerOptions"
id: -m-t-polyline-layer-options
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options"
---
# MTPolylineLayerOptions

constructor(data: String, layerId: String? = null, sourceId: String? = null, beforeId: String? = null, minzoom: Double? = null, maxzoom: Double? = null, outline: Boolean? = null, outlineColor: String? = null, outlineWidth: Double? = null, outlineOpacity: Double? = null, lineColor: String? = null, lineWidth: Double? = null, lineOpacity: Double? = null, lineBlur: Double? = null, lineGapWidth: Double? = null, lineDashPattern: String? = null, lineCap: String? = null, lineJoin: String? = null, outlineBlur: Double? = null)constructor(data: String, layerId: String? = null, sourceId: String? = null, beforeId: String? = null, minzoom: Double? = null, maxzoom: Double? = null, outline: Boolean? = null, outlineColor: MTStringOrZoomStringValues? = null, outlineWidth: MTNumberOrZoomNumberValues? = null, outlineOpacity: MTNumberOrZoomNumberValues? = null, lineColor: MTStringOrZoomStringValues? = null, lineWidth: MTNumberOrZoomNumberValues? = null, lineOpacity: MTNumberOrZoomNumberValues? = null, lineBlur: MTNumberOrZoomNumberValues? = null, lineGapWidth: MTNumberOrZoomNumberValues? = null, lineDashArray: MTDashArrayOption? = null, lineCap: MTLineCap? = null, lineJoin: MTLineJoin? = null, outlineBlur: MTNumberOrZoomNumberValues? = null)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options/before-id.html

---
layout: mobile_sdk
title: "beforeId"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "beforeId"
id: before-id
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options"
---
# beforeId

val beforeId: String? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options/data.html

---
layout: mobile_sdk
title: "data"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "data"
id: data
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options"
---
# data

val data: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options/index.html

---
layout: mobile_sdk
title: "MTPolylineLayerOptions"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTPolylineLayerOptions"
id: -m-t-polyline-layer-options
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options"
---
# MTPolylineLayerOptions

@Serializabledata class MTPolylineLayerOptions(val data: String, val layerId: String? = null, val sourceId: String? = null, val beforeId: String? = null, val minzoom: Double? = null, val maxzoom: Double? = null, val outline: Boolean? = null, val outlineColor: MTStringOrZoomStringValues? = null, val outlineWidth: MTNumberOrZoomNumberValues? = null, val outlineOpacity: MTNumberOrZoomNumberValues? = null, val lineColor: MTStringOrZoomStringValues? = null, val lineWidth: MTNumberOrZoomNumberValues? = null, val lineOpacity: MTNumberOrZoomNumberValues? = null, val lineBlur: MTNumberOrZoomNumberValues? = null, val lineGapWidth: MTNumberOrZoomNumberValues? = null, val lineDashArray: MTDashArrayOption? = null, val lineCap: MTLineCap? = null, val lineJoin: MTLineJoin? = null, val outlineBlur: MTNumberOrZoomNumberValues? = null)Options for building a polyline visualization layer through the helper.

Members

## Constructors

MTPolylineLayerOptions

constructor(data: String, layerId: String? = null, sourceId: String? = null, beforeId: String? = null, minzoom: Double? = null, maxzoom: Double? = null, outline: Boolean? = null, outlineColor: String? = null, outlineWidth: Double? = null, outlineOpacity: Double? = null, lineColor: String? = null, lineWidth: Double? = null, lineOpacity: Double? = null, lineBlur: Double? = null, lineGapWidth: Double? = null, lineDashPattern: String? = null, lineCap: String? = null, lineJoin: String? = null, outlineBlur: Double? = null)constructor(data: String, layerId: String? = null, sourceId: String? = null, beforeId: String? = null, minzoom: Double? = null, maxzoom: Double? = null, outline: Boolean? = null, outlineColor: MTStringOrZoomStringValues? = null, outlineWidth: MTNumberOrZoomNumberValues? = null, outlineOpacity: MTNumberOrZoomNumberValues? = null, lineColor: MTStringOrZoomStringValues? = null, lineWidth: MTNumberOrZoomNumberValues? = null, lineOpacity: MTNumberOrZoomNumberValues? = null, lineBlur: MTNumberOrZoomNumberValues? = null, lineGapWidth: MTNumberOrZoomNumberValues? = null, lineDashArray: MTDashArrayOption? = null, lineCap: MTLineCap? = null, lineJoin: MTLineJoin? = null, outlineBlur: MTNumberOrZoomNumberValues? = null)

## Properties

beforeId

val beforeId: String? = null

data

val data: String

layerId

val layerId: String? = null

lineBlur

val lineBlur: MTNumberOrZoomNumberValues? = null

lineCap

val lineCap: MTLineCap? = null

lineColor

val lineColor: MTStringOrZoomStringValues? = null

lineDashArray

val lineDashArray: MTDashArrayOption? = null

lineGapWidth

val lineGapWidth: MTNumberOrZoomNumberValues? = null

lineJoin

val lineJoin: MTLineJoin? = null

lineOpacity

val lineOpacity: MTNumberOrZoomNumberValues? = null

lineWidth

val lineWidth: MTNumberOrZoomNumberValues? = null

maxzoom

val maxzoom: Double? = null

minzoom

val minzoom: Double? = null

outline

val outline: Boolean? = null

outlineBlur

val outlineBlur: MTNumberOrZoomNumberValues? = null

outlineColor

val outlineColor: MTStringOrZoomStringValues? = null

outlineOpacity

val outlineOpacity: MTNumberOrZoomNumberValues? = null

outlineWidth

val outlineWidth: MTNumberOrZoomNumberValues? = null

sourceId

val sourceId: String? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options/layer-id.html

---
layout: mobile_sdk
title: "layerId"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "layerId"
id: layer-id
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options"
---
# layerId

val layerId: String? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options/line-blur.html

---
layout: mobile_sdk
title: "lineBlur"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "lineBlur"
id: line-blur
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options"
---
# lineBlur

val lineBlur: MTNumberOrZoomNumberValues? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options/line-cap.html

---
layout: mobile_sdk
title: "lineCap"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "lineCap"
id: line-cap
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options"
---
# lineCap

val lineCap: MTLineCap? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options/line-color.html

---
layout: mobile_sdk
title: "lineColor"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "lineColor"
id: line-color
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options"
---
# lineColor

val lineColor: MTStringOrZoomStringValues? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options/line-dash-array.html

---
layout: mobile_sdk
title: "lineDashArray"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "lineDashArray"
id: line-dash-array
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options"
---
# lineDashArray

val lineDashArray: MTDashArrayOption? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options/line-gap-width.html

---
layout: mobile_sdk
title: "lineGapWidth"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "lineGapWidth"
id: line-gap-width
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options"
---
# lineGapWidth

val lineGapWidth: MTNumberOrZoomNumberValues? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options/line-join.html

---
layout: mobile_sdk
title: "lineJoin"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "lineJoin"
id: line-join
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options"
---
# lineJoin

val lineJoin: MTLineJoin? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options/line-opacity.html

---
layout: mobile_sdk
title: "lineOpacity"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "lineOpacity"
id: line-opacity
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options"
---
# lineOpacity

val lineOpacity: MTNumberOrZoomNumberValues? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options/line-width.html

---
layout: mobile_sdk
title: "lineWidth"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "lineWidth"
id: line-width
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options"
---
# lineWidth

val lineWidth: MTNumberOrZoomNumberValues? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options/maxzoom.html

---
layout: mobile_sdk
title: "maxzoom"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "maxzoom"
id: maxzoom
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options"
---
# maxzoom

val maxzoom: Double? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options/minzoom.html

---
layout: mobile_sdk
title: "minzoom"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "minzoom"
id: minzoom
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options"
---
# minzoom

val minzoom: Double? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options/outline-blur.html

---
layout: mobile_sdk
title: "outlineBlur"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "outlineBlur"
id: outline-blur
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options"
---
# outlineBlur

val outlineBlur: MTNumberOrZoomNumberValues? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options/outline-color.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options"
---
# outlineColor

val outlineColor: MTStringOrZoomStringValues? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options/outline-opacity.html

---
layout: mobile_sdk
title: "outlineOpacity"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "outlineOpacity"
id: outline-opacity
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options"
---
# outlineOpacity

val outlineOpacity: MTNumberOrZoomNumberValues? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options/outline-width.html

---
layout: mobile_sdk
title: "outlineWidth"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "outlineWidth"
id: outline-width
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options"
---
# outlineWidth

val outlineWidth: MTNumberOrZoomNumberValues? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options/outline.html

---
layout: mobile_sdk
title: "outline"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "outline"
id: outline
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options"
---
# outline

val outline: Boolean? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options/source-id.html

---
layout: mobile_sdk
title: "sourceId"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "sourceId"
id: source-id
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-polyline-layer-options"
---
# sourceId

val sourceId: String? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-property-values/index.html

---
layout: mobile_sdk
title: "MTPropertyValues"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTPropertyValues"
id: -m-t-property-values
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-property-values"
---
# MTPropertyValues

typealias MTPropertyValues = List<MTHelperPropertyValue>

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-radius-option/-number/-number.html

---
layout: mobile_sdk
title: "Number"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Number"
id: -number
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-radius-option/-number"
---
# Number

constructor(value: Double)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-radius-option/-number/index.html

---
layout: mobile_sdk
title: "Number"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Number"
id: -number
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-radius-option/-number"
---
# Number

data class Number(val value: Double) : MTRadiusOption

Members

## Constructors

Number

constructor(value: Double)

## Properties

value

val value: Double

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-radius-option/-number/value.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-radius-option/-number"
---
# value

val value: Double

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-radius-option/-property/-property.html

---
layout: mobile_sdk
title: "Property"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Property"
id: -property
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-radius-option/-property"
---
# Property

constructor(values: MTPropertyValues)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-radius-option/-property/index.html

---
layout: mobile_sdk
title: "Property"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Property"
id: -property
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-radius-option/-property"
---
# Property

data class Property(val values: MTPropertyValues) : MTRadiusOption

Members

## Constructors

Property

constructor(values: MTPropertyValues)

## Properties

values

val values: MTPropertyValues

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-radius-option/-property/values.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-radius-option/-property"
---
# values

val values: MTPropertyValues

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-radius-option/-zoom/-zoom.html

---
layout: mobile_sdk
title: "Zoom"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Zoom"
id: -zoom
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-radius-option/-zoom"
---
# Zoom

constructor(values: MTZoomNumberValues)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-radius-option/-zoom/index.html

---
layout: mobile_sdk
title: "Zoom"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Zoom"
id: -zoom
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-radius-option/-zoom"
---
# Zoom

data class Zoom(val values: MTZoomNumberValues) : MTRadiusOption

Members

## Constructors

Zoom

constructor(values: MTZoomNumberValues)

## Properties

values

val values: MTZoomNumberValues

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-radius-option/-zoom/values.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-radius-option/-zoom"
---
# values

val values: MTZoomNumberValues

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-radius-option/index.html

---
layout: mobile_sdk
title: "MTRadiusOption"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTRadiusOption"
id: -m-t-radius-option
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-radius-option"
---
# MTRadiusOption

@Serializable(with = MTRadiusOptionSerializer::class)sealed class MTRadiusOptionnumber | ZoomNumberValues | PropertyValues
#### Inheritors

NumberZoomProperty

Members

## Types

Number

data class Number(val value: Double) : MTRadiusOption

Property

data class Property(val values: MTPropertyValues) : MTRadiusOption

Zoom

data class Zoom(val values: MTZoomNumberValues) : MTRadiusOption

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-radius-option-serializer/descriptor.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-radius-option-serializer"
---
# descriptor

open override val descriptor: SerialDescriptor

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-radius-option-serializer/deserialize.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-radius-option-serializer"
---
# deserialize

open override fun deserialize(decoder: Decoder): MTRadiusOption

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-radius-option-serializer/index.html

---
layout: mobile_sdk
title: "MTRadiusOptionSerializer"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTRadiusOptionSerializer"
id: -m-t-radius-option-serializer
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-radius-option-serializer"
---
# MTRadiusOptionSerializer

object MTRadiusOptionSerializer : KSerializer<MTRadiusOption> 

Members

## Properties

descriptor

open override val descriptor: SerialDescriptor

## Functions

deserialize

open override fun deserialize(decoder: Decoder): MTRadiusOption

serialize

open override fun serialize(encoder: Encoder, value: MTRadiusOption)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-radius-option-serializer/serialize.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-radius-option-serializer"
---
# serialize

open override fun serialize(encoder: Encoder, value: MTRadiusOption)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-string-or-zoom-string-values/-color-hex/-color-hex.html

---
layout: mobile_sdk
title: "ColorHex"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ColorHex"
id: -color-hex
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-string-or-zoom-string-values/-color-hex"
---
# ColorHex

constructor(color: MTColorValue)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-string-or-zoom-string-values/-color-hex/color.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-string-or-zoom-string-values/-color-hex"
---
# color

val color: MTColorValue

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-string-or-zoom-string-values/-color-hex/index.html

---
layout: mobile_sdk
title: "ColorHex"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ColorHex"
id: -color-hex
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-string-or-zoom-string-values/-color-hex"
---
# ColorHex

data class ColorHex(val color: MTColorValue) : MTStringOrZoomStringValues

Members

## Constructors

ColorHex

constructor(color: MTColorValue)

## Properties

color

val color: MTColorValue

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-string-or-zoom-string-values/-companion/from-color-int.html

---
layout: mobile_sdk
title: "fromColorInt"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "fromColorInt"
id: from-color-int
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-string-or-zoom-string-values/-companion"
---
# fromColorInt

fun fromColorInt(@ColorInt color: Int): MTStringOrZoomStringValues

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-string-or-zoom-string-values/-companion/index.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-string-or-zoom-string-values/-companion"
---
# Companion

object Companion

Members

## Functions

fromColorInt

fun fromColorInt(@ColorInt color: Int): MTStringOrZoomStringValues

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-string-or-zoom-string-values/-ramp/-ramp.html

---
layout: mobile_sdk
title: "Ramp"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Ramp"
id: -ramp
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-string-or-zoom-string-values/-ramp"
---
# Ramp

constructor(values: MTZoomStringValues)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-string-or-zoom-string-values/-ramp/index.html

---
layout: mobile_sdk
title: "Ramp"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Ramp"
id: -ramp
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-string-or-zoom-string-values/-ramp"
---
# Ramp

data class Ramp(val values: MTZoomStringValues) : MTStringOrZoomStringValues

Members

## Constructors

Ramp

constructor(values: MTZoomStringValues)

## Properties

values

val values: MTZoomStringValues

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-string-or-zoom-string-values/-ramp/values.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-string-or-zoom-string-values/-ramp"
---
# values

val values: MTZoomStringValues

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-string-or-zoom-string-values/-string-value/-string-value.html

---
layout: mobile_sdk
title: "StringValue"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "StringValue"
id: -string-value
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-string-or-zoom-string-values/-string-value"
---
# StringValue

constructor(value: String)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-string-or-zoom-string-values/-string-value/index.html

---
layout: mobile_sdk
title: "StringValue"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "StringValue"
id: -string-value
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-string-or-zoom-string-values/-string-value"
---
# StringValue

data class StringValue(val value: String) : MTStringOrZoomStringValues

Members

## Constructors

StringValue

constructor(value: String)

## Properties

value

val value: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-string-or-zoom-string-values/-string-value/value.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-string-or-zoom-string-values/-string-value"
---
# value

val value: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-string-or-zoom-string-values/index.html

---
layout: mobile_sdk
title: "MTStringOrZoomStringValues"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTStringOrZoomStringValues"
id: -m-t-string-or-zoom-string-values
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-string-or-zoom-string-values"
---
# MTStringOrZoomStringValues

@Serializable(with = MTStringOrZoomStringValuesSerializer::class)sealed class MTStringOrZoomStringValuesstring | ZoomStringValues | Android color
#### Inheritors

StringValueRampColorHex

Members

## Types

ColorHex

data class ColorHex(val color: MTColorValue) : MTStringOrZoomStringValues

Companion

object Companion

Ramp

data class Ramp(val values: MTZoomStringValues) : MTStringOrZoomStringValues

StringValue

data class StringValue(val value: String) : MTStringOrZoomStringValues

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-string-or-zoom-string-values-serializer/descriptor.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-string-or-zoom-string-values-serializer"
---
# descriptor

open override val descriptor: SerialDescriptor

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-string-or-zoom-string-values-serializer/deserialize.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-string-or-zoom-string-values-serializer"
---
# deserialize

open override fun deserialize(decoder: Decoder): MTStringOrZoomStringValues

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-string-or-zoom-string-values-serializer/index.html

---
layout: mobile_sdk
title: "MTStringOrZoomStringValuesSerializer"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTStringOrZoomStringValuesSerializer"
id: -m-t-string-or-zoom-string-values-serializer
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-string-or-zoom-string-values-serializer"
---
# MTStringOrZoomStringValuesSerializer

object MTStringOrZoomStringValuesSerializer : KSerializer<MTStringOrZoomStringValues> 

Members

## Properties

descriptor

open override val descriptor: SerialDescriptor

## Functions

deserialize

open override fun deserialize(decoder: Decoder): MTStringOrZoomStringValues

serialize

open override fun serialize(encoder: Encoder, value: MTStringOrZoomStringValues)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-string-or-zoom-string-values-serializer/serialize.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-string-or-zoom-string-values-serializer"
---
# serialize

open override fun serialize(encoder: Encoder, value: MTStringOrZoomStringValues)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-zoom-number-value/-m-t-zoom-number-value.html

---
layout: mobile_sdk
title: "MTZoomNumberValue"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTZoomNumberValue"
id: -m-t-zoom-number-value
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-zoom-number-value"
---
# MTZoomNumberValue

constructor(zoom: Double, value: Double)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-zoom-number-value/index.html

---
layout: mobile_sdk
title: "MTZoomNumberValue"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTZoomNumberValue"
id: -m-t-zoom-number-value
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-zoom-number-value"
---
# MTZoomNumberValue

@Serializabledata class MTZoomNumberValue(val zoom: Double, val value: Double)Zoom/value pair for number-based ramps.

Members

## Constructors

MTZoomNumberValue

constructor(zoom: Double, value: Double)

## Properties

value

val value: Double

zoom

val zoom: Double

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-zoom-number-value/value.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-zoom-number-value"
---
# value

val value: Double

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-zoom-number-value/zoom.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-zoom-number-value"
---
# zoom

val zoom: Double

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-zoom-number-values/index.html

---
layout: mobile_sdk
title: "MTZoomNumberValues"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTZoomNumberValues"
id: -m-t-zoom-number-values
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-zoom-number-values"
---
# MTZoomNumberValues

typealias MTZoomNumberValues = List<MTZoomNumberValue>

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-zoom-string-value/-m-t-zoom-string-value.html

---
layout: mobile_sdk
title: "MTZoomStringValue"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTZoomStringValue"
id: -m-t-zoom-string-value
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-zoom-string-value"
---
# MTZoomStringValue

constructor(zoom: Double, value: String)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-zoom-string-value/index.html

---
layout: mobile_sdk
title: "MTZoomStringValue"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTZoomStringValue"
id: -m-t-zoom-string-value
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-zoom-string-value"
---
# MTZoomStringValue

@Serializabledata class MTZoomStringValue(val zoom: Double, val value: String)Zoom/value pair for string-based ramps.

Members

## Constructors

MTZoomStringValue

constructor(zoom: Double, value: String)

## Properties

value

val value: String

zoom

val zoom: Double

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-zoom-string-value/value.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-zoom-string-value"
---
# value

val value: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-zoom-string-value/zoom.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-zoom-string-value"
---
# zoom

val zoom: Double

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-zoom-string-values/index.html

---
layout: mobile_sdk
title: "MTZoomStringValues"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTZoomStringValues"
id: -m-t-zoom-string-values
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/-m-t-zoom-string-values"
---
# MTZoomStringValues

typealias MTZoomStringValues = List<MTZoomStringValue>

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/index.html

---
layout: mobile_sdk
title: "com.maptiler.maptilersdk.helpers"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "com.maptiler.maptilersdk.helpers"
id: com.maptiler.maptilersdk.helpers
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers"
---
# com.maptiler.maptilersdk.helpers

TypesFunctions

## Types

JsonConfig

object JsonConfig

MTBenchmark

class MTBenchmark(context: Context) : MTMapViewDelegateBasic benchmarking helper for Kotlin SDK.

MTColorValue

@Serializable(with = MTColorValueAsStringSerializer::class)data class MTColorValue(val raw: String)Color wrapper that always encodes as a hex string. Accepts #RRGGBB or #RRGGBBAA (CSS hex). When constructed from a color int, outputs #RRGGBB if opaque, otherwise #RRGGBBAA (alpha at the end).

MTColorValueAsStringSerializer

object MTColorValueAsStringSerializer : KSerializer<MTColorValue> 

MTDashArrayOption

@Serializable(with = MTDashArrayOptionSerializer::class)sealed class MTDashArrayOptionDash array option accepting either an array of numbers or the underscore/space pattern string.

MTDashArrayOptionSerializer

object MTDashArrayOptionSerializer : KSerializer<MTDashArrayOption> 

MTHeatmapLayerHelper

class MTHeatmapLayerHelper(style: MTStyle) : MTVectorLayerHelperHelper for creating a heatmap visualization layer from data and styling options.

MTHeatmapLayerOptions

data class MTHeatmapLayerOptions(val data: String, val layerId: String? = null, val sourceId: String? = null, val beforeId: String? = null, val minzoom: Double? = null, val maxzoom: Double? = null, val colorRamp: MTColorRamp? = null, val property: String? = null, val weight: MTNumberOrPropertyValues? = null, val radius: MTRadiusOption? = null, val opacity: MTNumberOrZoomNumberValues? = null, val intensity: MTNumberOrZoomNumberValues? = null, val zoomCompensation: Boolean? = null)Options for building a heatmap visualization layer through the helper.

MTHelperPropertyValue

@Serializabledata class MTHelperPropertyValue(val propertyValue: Double, val value: Double)Property/value pair for data-driven styles.

MTNumberOrPropertyValues

@Serializable(with = MTNumberOrPropertyValuesSerializer::class)sealed class MTNumberOrPropertyValuesnumber | PropertyValues

MTNumberOrPropertyValuesSerializer

object MTNumberOrPropertyValuesSerializer : KSerializer<MTNumberOrPropertyValues> 

MTNumberOrZoomNumberValues

@Serializable(with = MTNumberOrZoomNumberValuesSerializer::class)sealed class MTNumberOrZoomNumberValuesnumber | ZoomNumberValues

MTNumberOrZoomNumberValuesSerializer

object MTNumberOrZoomNumberValuesSerializer : KSerializer<MTNumberOrZoomNumberValues> 

MTOutlinePosition

@Serializableenum MTOutlinePosition : Enum<MTOutlinePosition> Outline position relative to polygon edge.

MTPerformancePresets

object MTPerformancePresetsPerformance-oriented presets for MapTiler Kotlin SDK.

MTPitchLimitHelper

object MTPitchLimitHelperHelper object to configure pitch limits on the map.

MTPointLayerHelper

class MTPointLayerHelper(style: MTStyle) : MTVectorLayerHelperHelper for creating a point visualization layer from data and styling options.

MTPointLayerOptions

@Serializabledata class MTPointLayerOptions(val data: String, val layerId: String? = null, val sourceId: String? = null, val beforeId: String? = null, val minzoom: Double? = null, val maxzoom: Double? = null, val outline: Boolean? = null, val outlineColor: MTStringOrZoomStringValues? = null, val outlineWidth: MTNumberOrZoomNumberValues? = null, val outlineOpacity: MTNumberOrZoomNumberValues? = null, val pointColor: MTColorValue? = null, val pointColorRamp: MTColorRamp? = null, val pointRadius: MTNumberOrZoomNumberValues? = null, val minPointRadius: Double? = null, val maxPointRadius: Double? = null, val property: String? = null, val pointOpacity: MTNumberOrZoomNumberValues? = null, val alignOnViewport: Boolean? = null, val cluster: Boolean? = null, val showLabel: Boolean? = null, val labelColor: MTColorValue? = null, val labelSize: Double? = null, val zoomCompensation: Boolean? = null)Options for building a point visualization layer through the helper.

MTPolygonLayerHelper

class MTPolygonLayerHelper(style: MTStyle) : MTVectorLayerHelperHelper for creating a polygon visualization layer from data and styling options.

MTPolygonLayerOptions

@Serializabledata class MTPolygonLayerOptions(val data: String, val layerId: String? = null, val sourceId: String? = null, val beforeId: String? = null, val minzoom: Double? = null, val maxzoom: Double? = null, val outline: Boolean? = null, val outlineColor: MTStringOrZoomStringValues? = null, val outlineWidth: MTNumberOrZoomNumberValues? = null, val outlineOpacity: MTNumberOrZoomNumberValues? = null, val fillColor: MTStringOrZoomStringValues? = null, val fillOpacity: MTNumberOrZoomNumberValues? = null, val outlinePosition: MTOutlinePosition? = null, val outlineDashArray: MTDashArrayOption? = null, val outlineCap: MTLineCap? = null, val outlineJoin: MTLineJoin? = null, val pattern: String? = null, val outlineBlur: MTNumberOrZoomNumberValues? = null)Options for building a polygon visualization layer through the helper.

MTPolylineLayerHelper

class MTPolylineLayerHelper(style: MTStyle) : MTVectorLayerHelperHelper for creating a polyline visualization layer from data and styling options.

MTPolylineLayerOptions

@Serializabledata class MTPolylineLayerOptions(val data: String, val layerId: String? = null, val sourceId: String? = null, val beforeId: String? = null, val minzoom: Double? = null, val maxzoom: Double? = null, val outline: Boolean? = null, val outlineColor: MTStringOrZoomStringValues? = null, val outlineWidth: MTNumberOrZoomNumberValues? = null, val outlineOpacity: MTNumberOrZoomNumberValues? = null, val lineColor: MTStringOrZoomStringValues? = null, val lineWidth: MTNumberOrZoomNumberValues? = null, val lineOpacity: MTNumberOrZoomNumberValues? = null, val lineBlur: MTNumberOrZoomNumberValues? = null, val lineGapWidth: MTNumberOrZoomNumberValues? = null, val lineDashArray: MTDashArrayOption? = null, val lineCap: MTLineCap? = null, val lineJoin: MTLineJoin? = null, val outlineBlur: MTNumberOrZoomNumberValues? = null)Options for building a polyline visualization layer through the helper.

MTPropertyValues

typealias MTPropertyValues = List<MTHelperPropertyValue>

MTRadiusOption

@Serializable(with = MTRadiusOptionSerializer::class)sealed class MTRadiusOptionnumber | ZoomNumberValues | PropertyValues

MTRadiusOptionSerializer

object MTRadiusOptionSerializer : KSerializer<MTRadiusOption> 

MTStringOrZoomStringValues

@Serializable(with = MTStringOrZoomStringValuesSerializer::class)sealed class MTStringOrZoomStringValuesstring | ZoomStringValues | Android color

MTStringOrZoomStringValuesSerializer

object MTStringOrZoomStringValuesSerializer : KSerializer<MTStringOrZoomStringValues> 

MTZoomNumberValue

@Serializabledata class MTZoomNumberValue(val zoom: Double, val value: Double)Zoom/value pair for number-based ramps.

MTZoomNumberValues

typealias MTZoomNumberValues = List<MTZoomNumberValue>

MTZoomStringValue

@Serializabledata class MTZoomStringValue(val zoom: Double, val value: String)Zoom/value pair for string-based ramps.

MTZoomStringValues

typealias MTZoomStringValues = List<MTZoomStringValue>

## Functions

toHexString

fun Int.toHexString(withAlpha: Boolean = false, withHexPrefix: Boolean = true): String

withBalancedPerformanceDefaults

fun MTMapOptions.withBalancedPerformanceDefaults(): MTMapOptionsReturns a new MTMapOptions with balanced performance defaults applied over this instance.

withHighFidelityDefaults

fun MTMapOptions.withHighFidelityDefaults(): MTMapOptionsReturns a new MTMapOptions with high-fidelity defaults applied over this instance.

withLeanPerformanceDefaults

fun MTMapOptions.withLeanPerformanceDefaults(): MTMapOptionsApplies the lean performance preset over this instance, returning a new options object.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/to-hex-string.html

---
layout: mobile_sdk
title: "toHexString"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "toHexString"
id: to-hex-string
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers"
---
# toHexString

fun Int.toHexString(withAlpha: Boolean = false, withHexPrefix: Boolean = true): String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/with-balanced-performance-defaults.html

---
layout: mobile_sdk
title: "withBalancedPerformanceDefaults"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "withBalancedPerformanceDefaults"
id: with-balanced-performance-defaults
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers"
---
# withBalancedPerformanceDefaults

fun MTMapOptions.withBalancedPerformanceDefaults(): MTMapOptionsReturns a new MTMapOptions with balanced performance defaults applied over this instance.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/with-high-fidelity-defaults.html

---
layout: mobile_sdk
title: "withHighFidelityDefaults"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "withHighFidelityDefaults"
id: with-high-fidelity-defaults
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers"
---
# withHighFidelityDefaults

fun MTMapOptions.withHighFidelityDefaults(): MTMapOptionsReturns a new MTMapOptions with high-fidelity defaults applied over this instance.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.helpers/with-lean-performance-defaults.html

---
layout: mobile_sdk
title: "withLeanPerformanceDefaults"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "withLeanPerformanceDefaults"
id: with-lean-performance-defaults
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.helpers"
---
# withLeanPerformanceDefaults

fun MTMapOptions.withLeanPerformanceDefaults(): MTMapOptionsApplies the lean performance preset over this instance, returning a new options object.

---

