# MapTiler Android SDK API Reference - com.maptiler.maptilersdk.map.style.dsl

This document is a part of the Android SDK API reference documentation, covering the `com.maptiler.maptilersdk.map.style.dsl` package.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-expression/get.html

---
layout: mobile_sdk
title: "get"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "get"
id: get
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-expression"
---
# get

fun get(key: MTFeatureKey): PropertyValue

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-expression/index.html

---
layout: mobile_sdk
title: "MTExpression"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTExpression"
id: -m-t-expression
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-expression"
---
# MTExpression

object MTExpressionSimple typed expression helpers that encode to JSON arrays.

Members

## Functions

get

fun get(key: MTFeatureKey): PropertyValue

step

fun step(input: PropertyValue, default: PropertyValue, stops: List<Pair<Double, PropertyValue>>): PropertyValue

toString

fun toString(value: PropertyValue): PropertyValue

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-expression/step.html

---
layout: mobile_sdk
title: "step"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "step"
id: step
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-expression"
---
# step

fun step(input: PropertyValue, default: PropertyValue, stops: List<Pair<Double, PropertyValue>>): PropertyValue

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-expression/to-string.html

---
layout: mobile_sdk
title: "toString"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "toString"
id: to-string
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-expression"
---
# toString

fun toString(value: PropertyValue): PropertyValue

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-feature-key/-c-l-u-s-t-e-r_-i-d/index.html

---
layout: mobile_sdk
title: "CLUSTER_ID"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "CLUSTER_ID"
id: -c-l-u-s-t-e-r_-i-d
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-feature-key/-c-l-u-s-t-e-r_-i-d"
---
# CLUSTER_ID

CLUSTER_ID

Members

## Properties

key

val key: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-feature-key/-p-o-i-n-t_-c-o-u-n-t/index.html

---
layout: mobile_sdk
title: "POINT_COUNT"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "POINT_COUNT"
id: -p-o-i-n-t_-c-o-u-n-t
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-feature-key/-p-o-i-n-t_-c-o-u-n-t"
---
# POINT_COUNT

POINT_COUNT

Members

## Properties

key

val key: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-feature-key/entries.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-feature-key"
---
# entries

val entries: EnumEntries<MTFeatureKey>Returns a representation of an immutable list of all enum entries, in the order they're declared.This method may be used to iterate over the enum entries.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-feature-key/index.html

---
layout: mobile_sdk
title: "MTFeatureKey"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTFeatureKey"
id: -m-t-feature-key
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-feature-key"
---
# MTFeatureKey

enum MTFeatureKey : Enum<MTFeatureKey> Common GeoJSON feature keys used in clustering.

MembersEntries

## Entries

POINT_COUNT

POINT_COUNT

CLUSTER_ID

CLUSTER_ID

## Properties

entries

val entries: EnumEntries<MTFeatureKey>Returns a representation of an immutable list of all enum entries, in the order they're declared.

key

val key: String

name

val name: String

ordinal

val ordinal: Int

## Functions

valueOf

fun valueOf(value: String): MTFeatureKeyReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

values

fun values(): Array<MTFeatureKey>Returns an array containing the constants of this enum type, in the order they're declared.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-feature-key/key.html

---
layout: mobile_sdk
title: "key"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "key"
id: key
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-feature-key"
---
# key

val key: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-feature-key/value-of.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-feature-key"
---
# valueOf

fun valueOf(value: String): MTFeatureKeyReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
#### Throws

IllegalArgumentExceptionif this enum type has no constant with the specified name

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-feature-key/values.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-feature-key"
---
# values

fun values(): Array<MTFeatureKey>Returns an array containing the constants of this enum type, in the order they're declared.This method may be used to iterate over the constants.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-filter/all.html

---
layout: mobile_sdk
title: "all"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "all"
id: all
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-filter"
---
# all

fun all(vararg filters: PropertyValue): PropertyValue

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-filter/any.html

---
layout: mobile_sdk
title: "any"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "any"
id: any
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-filter"
---
# any

fun any(vararg filters: PropertyValue): PropertyValue

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-filter/clusters.html

---
layout: mobile_sdk
title: "clusters"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "clusters"
id: clusters
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-filter"
---
# clusters

fun clusters(): PropertyValue

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-filter/eq.html

---
layout: mobile_sdk
title: "eq"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "eq"
id: eq
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-filter"
---
# eq

fun eq(key: MTFeatureKey, value: PropertyValue): PropertyValue

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-filter/has.html

---
layout: mobile_sdk
title: "has"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "has"
id: has
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-filter"
---
# has

fun has(key: MTFeatureKey): PropertyValue

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-filter/index.html

---
layout: mobile_sdk
title: "MTFilter"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTFilter"
id: -m-t-filter
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-filter"
---
# MTFilter

object MTFilterFilter helpers that build GL-style filter arrays.

Members

## Functions

all

fun all(vararg filters: PropertyValue): PropertyValue

any

fun any(vararg filters: PropertyValue): PropertyValue

clusters

fun clusters(): PropertyValue

eq

fun eq(key: MTFeatureKey, value: PropertyValue): PropertyValue

has

fun has(key: MTFeatureKey): PropertyValue

not

fun not(filter: PropertyValue): PropertyValue

unclustered

fun unclustered(): PropertyValue

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-filter/not.html

---
layout: mobile_sdk
title: "not"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "not"
id: not
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-filter"
---
# not

fun not(filter: PropertyValue): PropertyValue

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-filter/unclustered.html

---
layout: mobile_sdk
title: "unclustered"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "unclustered"
id: unclustered
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-filter"
---
# unclustered

fun unclustered(): PropertyValue

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-text-token/-p-o-i-n-t_-c-o-u-n-t_-a-b-b-r-e-v-i-a-t-e-d/index.html

---
layout: mobile_sdk
title: "POINT_COUNT_ABBREVIATED"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "POINT_COUNT_ABBREVIATED"
id: -p-o-i-n-t_-c-o-u-n-t_-a-b-b-r-e-v-i-a-t-e-d
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-text-token/-p-o-i-n-t_-c-o-u-n-t_-a-b-b-r-e-v-i-a-t-e-d"
---
# POINT_COUNT_ABBREVIATED

POINT_COUNT_ABBREVIATED

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

token

val token: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-text-token/entries.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-text-token"
---
# entries

val entries: EnumEntries<MTTextToken>Returns a representation of an immutable list of all enum entries, in the order they're declared.This method may be used to iterate over the enum entries.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-text-token/index.html

---
layout: mobile_sdk
title: "MTTextToken"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTTextToken"
id: -m-t-text-token
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-text-token"
---
# MTTextToken

enum MTTextToken : Enum<MTTextToken> Tokens for text-field convenience.

MembersEntries

## Entries

POINT_COUNT_ABBREVIATED

POINT_COUNT_ABBREVIATED

## Properties

entries

val entries: EnumEntries<MTTextToken>Returns a representation of an immutable list of all enum entries, in the order they're declared.

name

val name: String

ordinal

val ordinal: Int

token

val token: String

## Functions

valueOf

fun valueOf(value: String): MTTextTokenReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

values

fun values(): Array<MTTextToken>Returns an array containing the constants of this enum type, in the order they're declared.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-text-token/token.html

---
layout: mobile_sdk
title: "token"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "token"
id: token
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-text-token"
---
# token

val token: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-text-token/value-of.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-text-token"
---
# valueOf

fun valueOf(value: String): MTTextTokenReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
#### Throws

IllegalArgumentExceptionif this enum type has no constant with the specified name

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-text-token/values.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-m-t-text-token"
---
# values

fun values(): Array<MTTextToken>Returns an array containing the constants of this enum type, in the order they're declared.This method may be used to iterate over the constants.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-arr/-arr.html

---
layout: mobile_sdk
title: "Arr"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Arr"
id: -arr
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-arr"
---
# Arr

constructor(values: List<PropertyValue>)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-arr/index.html

---
layout: mobile_sdk
title: "Arr"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Arr"
id: -arr
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-arr"
---
# Arr

data class Arr(val values: List<PropertyValue>) : PropertyValue

Members

## Constructors

Arr

constructor(values: List<PropertyValue>)

## Properties

values

val values: List<PropertyValue>

## Functions

asCode

fun asCode(): String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-arr/values.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-arr"
---
# values

val values: List<PropertyValue>

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-bool/-bool.html

---
layout: mobile_sdk
title: "Bool"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Bool"
id: -bool
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-bool"
---
# Bool

constructor(value: Boolean)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-bool/index.html

---
layout: mobile_sdk
title: "Bool"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Bool"
id: -bool
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-bool"
---
# Bool

data class Bool(val value: Boolean) : PropertyValue

Members

## Constructors

Bool

constructor(value: Boolean)

## Properties

value

val value: Boolean

## Functions

asCode

fun asCode(): String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-bool/value.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-bool"
---
# value

val value: Boolean

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-color/-color.html

---
layout: mobile_sdk
title: "Color"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Color"
id: -color
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-color"
---
# Color

constructor(argb: Int, includeAlpha: Boolean = false)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-color/argb.html

---
layout: mobile_sdk
title: "argb"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "argb"
id: argb
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-color"
---
# argb

val argb: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-color/include-alpha.html

---
layout: mobile_sdk
title: "includeAlpha"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "includeAlpha"
id: include-alpha
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-color"
---
# includeAlpha

val includeAlpha: Boolean = false

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-color/index.html

---
layout: mobile_sdk
title: "Color"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Color"
id: -color
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-color"
---
# Color

data class Color(val argb: Int, val includeAlpha: Boolean = false) : PropertyValue

Members

## Constructors

Color

constructor(argb: Int, includeAlpha: Boolean = false)

## Properties

argb

val argb: Int

includeAlpha

val includeAlpha: Boolean = false

## Functions

asCode

fun asCode(): String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-companion/array.html

---
layout: mobile_sdk
title: "array"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "array"
id: array
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-companion"
---
# array

fun array(vararg values: PropertyValue): PropertyValue

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-companion/color.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-companion"
---
# color

fun color(value: Int, includeAlpha: Boolean = false): PropertyValue

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-companion/index.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-companion"
---
# Companion

object Companion

Members

## Functions

array

fun array(vararg values: PropertyValue): PropertyValue

color

fun color(value: Int, includeAlpha: Boolean = false): PropertyValue

of

fun of(value: Boolean): PropertyValuefun of(value: Double): PropertyValuefun of(value: Int): PropertyValuefun of(value: String): PropertyValue

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-companion/of.html

---
layout: mobile_sdk
title: "of"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "of"
id: of
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-companion"
---
# of

fun of(value: String): PropertyValuefun of(value: Double): PropertyValuefun of(value: Int): PropertyValuefun of(value: Boolean): PropertyValue

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-num/-num.html

---
layout: mobile_sdk
title: "Num"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Num"
id: -num
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-num"
---
# Num

constructor(value: Double)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-num/index.html

---
layout: mobile_sdk
title: "Num"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Num"
id: -num
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-num"
---
# Num

data class Num(val value: Double) : PropertyValue

Members

## Constructors

Num

constructor(value: Double)

## Properties

value

val value: Double

## Functions

asCode

fun asCode(): String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-num/value.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-num"
---
# value

val value: Double

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-raw-js/-raw-js.html

---
layout: mobile_sdk
title: "RawJs"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "RawJs"
id: -raw-js
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-raw-js"
---
# RawJs

constructor(value: String)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-raw-js/index.html

---
layout: mobile_sdk
title: "RawJs"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "RawJs"
id: -raw-js
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-raw-js"
---
# RawJs

data class RawJs(val value: String) : PropertyValue

Members

## Constructors

RawJs

constructor(value: String)

## Properties

value

val value: String

## Functions

asCode

fun asCode(): String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-raw-js/value.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-raw-js"
---
# value

val value: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-str/-str.html

---
layout: mobile_sdk
title: "Str"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Str"
id: -str
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-str"
---
# Str

constructor(value: String)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-str/index.html

---
layout: mobile_sdk
title: "Str"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Str"
id: -str
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-str"
---
# Str

data class Str(val value: String) : PropertyValue

Members

## Constructors

Str

constructor(value: String)

## Properties

value

val value: String

## Functions

asCode

fun asCode(): String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-str/value.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/-str"
---
# value

val value: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/as-code.html

---
layout: mobile_sdk
title: "asCode"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "asCode"
id: as-code
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value"
---
# asCode

fun asCode(): String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value/index.html

---
layout: mobile_sdk
title: "PropertyValue"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "PropertyValue"
id: -property-value
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-property-value"
---
# PropertyValue

sealed class PropertyValueType-safe representation of style property values.
#### Inheritors

StrNumBoolArrRawJsColor

Members

## Types

Arr

data class Arr(val values: List<PropertyValue>) : PropertyValue

Bool

data class Bool(val value: Boolean) : PropertyValue

Color

data class Color(val argb: Int, val includeAlpha: Boolean = false) : PropertyValue

Companion

object Companion

Num

data class Num(val value: Double) : PropertyValue

RawJs

data class RawJs(val value: String) : PropertyValue

Str

data class Str(val value: String) : PropertyValue

## Functions

asCode

fun asCode(): String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-style-value/-bool/-bool.html

---
layout: mobile_sdk
title: "Bool"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Bool"
id: -bool
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-style-value/-bool"
---
# Bool

constructor(value: Boolean)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-style-value/-bool/index.html

---
layout: mobile_sdk
title: "Bool"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Bool"
id: -bool
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-style-value/-bool"
---
# Bool

data class Bool(val value: Boolean) : StyleValue

Members

## Constructors

Bool

constructor(value: Boolean)

## Properties

value

val value: Boolean

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-style-value/-bool/value.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-style-value/-bool"
---
# value

val value: Boolean

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-style-value/-color/-color.html

---
layout: mobile_sdk
title: "Color"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Color"
id: -color
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-style-value/-color"
---
# Color

constructor(value: Int)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-style-value/-color/index.html

---
layout: mobile_sdk
title: "Color"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Color"
id: -color
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-style-value/-color"
---
# Color

data class Color(val value: Int) : StyleValue

Members

## Constructors

Color

constructor(value: Int)

## Properties

value

val value: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-style-value/-color/value.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-style-value/-color"
---
# value

val value: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-style-value/-expression/-expression.html

---
layout: mobile_sdk
title: "Expression"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Expression"
id: -expression
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-style-value/-expression"
---
# Expression

constructor(expr: PropertyValue)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-style-value/-expression/expr.html

---
layout: mobile_sdk
title: "expr"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "expr"
id: expr
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-style-value/-expression"
---
# expr

val expr: PropertyValue

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-style-value/-expression/index.html

---
layout: mobile_sdk
title: "Expression"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Expression"
id: -expression
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-style-value/-expression"
---
# Expression

data class Expression(val expr: PropertyValue) : StyleValue

Members

## Constructors

Expression

constructor(expr: PropertyValue)

## Properties

expr

val expr: PropertyValue

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-style-value/-number/-number.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-style-value/-number"
---
# Number

constructor(value: Double)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-style-value/-number/index.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-style-value/-number"
---
# Number

data class Number(val value: Double) : StyleValue

Members

## Constructors

Number

constructor(value: Double)

## Properties

value

val value: Double

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-style-value/-number/value.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-style-value/-number"
---
# value

val value: Double

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-style-value/-str/-str.html

---
layout: mobile_sdk
title: "Str"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Str"
id: -str
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-style-value/-str"
---
# Str

constructor(value: String)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-style-value/-str/index.html

---
layout: mobile_sdk
title: "Str"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Str"
id: -str
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-style-value/-str"
---
# Str

data class Str(val value: String) : StyleValue

Members

## Constructors

Str

constructor(value: String)

## Properties

value

val value: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-style-value/-str/value.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-style-value/-str"
---
# value

val value: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-style-value/index.html

---
layout: mobile_sdk
title: "StyleValue"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "StyleValue"
id: -style-value
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/-style-value"
---
# StyleValue

@Serializable(with = StyleValueSerializer::class)sealed class StyleValueUnified style value that can be a constant or an expression (array).
#### Inheritors

ColorNumberBoolStrExpression

Members

## Types

Bool

data class Bool(val value: Boolean) : StyleValue

Color

data class Color(val value: Int) : StyleValue

Expression

data class Expression(val expr: PropertyValue) : StyleValue

Number

data class Number(val value: Double) : StyleValue

Str

data class Str(val value: String) : StyleValue

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl/index.html

---
layout: mobile_sdk
title: "com.maptiler.maptilersdk.map.style.dsl"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "com.maptiler.maptilersdk.map.style.dsl"
id: com.maptiler.maptilersdk.map.style.dsl
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.dsl"
---
# com.maptiler.maptilersdk.map.style.dsl

Types

## Types

MTExpression

object MTExpressionSimple typed expression helpers that encode to JSON arrays.

MTFeatureKey

enum MTFeatureKey : Enum<MTFeatureKey> Common GeoJSON feature keys used in clustering.

MTFilter

object MTFilterFilter helpers that build GL-style filter arrays.

MTTextToken

enum MTTextToken : Enum<MTTextToken> Tokens for text-field convenience.

PropertyValue

sealed class PropertyValueType-safe representation of style property values.

StyleValue

@Serializable(with = StyleValueSerializer::class)sealed class StyleValueUnified style value that can be a constant or an expression (array).

---

