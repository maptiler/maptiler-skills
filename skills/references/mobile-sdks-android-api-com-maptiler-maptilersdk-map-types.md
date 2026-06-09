# MapTiler Android SDK API Reference - com.maptiler.maptilersdk.map.types

This document is a part of the Android SDK API reference documentation, covering the `com.maptiler.maptilersdk.map.types` package.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-bounds/-m-t-bounds.html

---
layout: mobile_sdk
title: "MTBounds"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTBounds"
id: -m-t-bounds
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-bounds"
---
# MTBounds

constructor(west: Double, south: Double, east: Double, north: Double)Convenience constructor accepting west, south, east and north edges in degrees.constructor(southwest: LngLat, northeast: LngLat)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-bounds/contains.html

---
layout: mobile_sdk
title: "contains"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "contains"
id: contains
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-bounds"
---
# contains

fun contains(point: LngLat): BooleanCheck if the bounds contain a point.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-bounds/index.html

---
layout: mobile_sdk
title: "MTBounds"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTBounds"
id: -m-t-bounds
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-bounds"
---
# MTBounds

@Serializable(with = MTBoundsSerializer::class)data class MTBounds(val southwest: LngLat, val northeast: LngLat)Geographical bounding box represented by south-west and north-east corners.

Members

## Constructors

MTBounds

constructor(west: Double, south: Double, east: Double, north: Double)Convenience constructor accepting west, south, east and north edges in degrees.constructor(southwest: LngLat, northeast: LngLat)

## Properties

northeast

val northeast: LngLat

southwest

val southwest: LngLat

## Functions

contains

fun contains(point: LngLat): BooleanCheck if the bounds contain a point.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-bounds/northeast.html

---
layout: mobile_sdk
title: "northeast"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "northeast"
id: northeast
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-bounds"
---
# northeast

val northeast: LngLat

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-bounds/southwest.html

---
layout: mobile_sdk
title: "southwest"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "southwest"
id: southwest
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-bounds"
---
# southwest

val southwest: LngLat

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-a-l-b-a-n-i-a-n/index.html

---
layout: mobile_sdk
title: "ALBANIAN"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ALBANIAN"
id: -a-l-b-a-n-i-a-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-a-l-b-a-n-i-a-n"
---
# ALBANIAN

ALBANIAN

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-a-m-h-a-r-i-c/index.html

---
layout: mobile_sdk
title: "AMHARIC"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "AMHARIC"
id: -a-m-h-a-r-i-c
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-a-m-h-a-r-i-c"
---
# AMHARIC

AMHARIC

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-a-r-a-b-i-c/index.html

---
layout: mobile_sdk
title: "ARABIC"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ARABIC"
id: -a-r-a-b-i-c
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-a-r-a-b-i-c"
---
# ARABIC

ARABIC

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-a-r-m-e-n-i-a-n/index.html

---
layout: mobile_sdk
title: "ARMENIAN"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ARMENIAN"
id: -a-r-m-e-n-i-a-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-a-r-m-e-n-i-a-n"
---
# ARMENIAN

ARMENIAN

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-a-z-e-r-b-a-i-j-a-n-i/index.html

---
layout: mobile_sdk
title: "AZERBAIJANI"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "AZERBAIJANI"
id: -a-z-e-r-b-a-i-j-a-n-i
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-a-z-e-r-b-a-i-j-a-n-i"
---
# AZERBAIJANI

AZERBAIJANI

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-b-a-s-q-u-e/index.html

---
layout: mobile_sdk
title: "BASQUE"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "BASQUE"
id: -b-a-s-q-u-e
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-b-a-s-q-u-e"
---
# BASQUE

BASQUE

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-b-e-l-a-r-u-s-i-a-n/index.html

---
layout: mobile_sdk
title: "BELARUSIAN"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "BELARUSIAN"
id: -b-e-l-a-r-u-s-i-a-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-b-e-l-a-r-u-s-i-a-n"
---
# BELARUSIAN

BELARUSIAN

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-b-e-n-g-a-l-i/index.html

---
layout: mobile_sdk
title: "BENGALI"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "BENGALI"
id: -b-e-n-g-a-l-i
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-b-e-n-g-a-l-i"
---
# BENGALI

BENGALI

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-b-o-s-n-i-a-n/index.html

---
layout: mobile_sdk
title: "BOSNIAN"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "BOSNIAN"
id: -b-o-s-n-i-a-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-b-o-s-n-i-a-n"
---
# BOSNIAN

BOSNIAN

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-b-r-e-t-o-n/index.html

---
layout: mobile_sdk
title: "BRETON"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "BRETON"
id: -b-r-e-t-o-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-b-r-e-t-o-n"
---
# BRETON

BRETON

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-b-u-l-g-a-r-i-a-n/index.html

---
layout: mobile_sdk
title: "BULGARIAN"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "BULGARIAN"
id: -b-u-l-g-a-r-i-a-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-b-u-l-g-a-r-i-a-n"
---
# BULGARIAN

BULGARIAN

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-c-a-t-a-l-a-n/index.html

---
layout: mobile_sdk
title: "CATALAN"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "CATALAN"
id: -c-a-t-a-l-a-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-c-a-t-a-l-a-n"
---
# CATALAN

CATALAN

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-c-h-i-n-e-s-e/index.html

---
layout: mobile_sdk
title: "CHINESE"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "CHINESE"
id: -c-h-i-n-e-s-e
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-c-h-i-n-e-s-e"
---
# CHINESE

CHINESE

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-c-l-a-s-s-i-c-a-l_-l-a-t-i-n/index.html

---
layout: mobile_sdk
title: "CLASSICAL_LATIN"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "CLASSICAL_LATIN"
id: -c-l-a-s-s-i-c-a-l_-l-a-t-i-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-c-l-a-s-s-i-c-a-l_-l-a-t-i-n"
---
# CLASSICAL_LATIN

CLASSICAL_LATIN

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-c-o-r-s-i-c-a-n/index.html

---
layout: mobile_sdk
title: "CORSICAN"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "CORSICAN"
id: -c-o-r-s-i-c-a-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-c-o-r-s-i-c-a-n"
---
# CORSICAN

CORSICAN

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-c-r-o-a-t-i-a-n/index.html

---
layout: mobile_sdk
title: "CROATIAN"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "CROATIAN"
id: -c-r-o-a-t-i-a-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-c-r-o-a-t-i-a-n"
---
# CROATIAN

CROATIAN

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-c-z-e-c-h/index.html

---
layout: mobile_sdk
title: "CZECH"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "CZECH"
id: -c-z-e-c-h
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-c-z-e-c-h"
---
# CZECH

CZECH

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-d-a-n-i-s-h/index.html

---
layout: mobile_sdk
title: "DANISH"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "DANISH"
id: -d-a-n-i-s-h
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-d-a-n-i-s-h"
---
# DANISH

DANISH

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-d-u-t-c-h/index.html

---
layout: mobile_sdk
title: "DUTCH"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "DUTCH"
id: -d-u-t-c-h
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-d-u-t-c-h"
---
# DUTCH

DUTCH

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-e-n-g-l-i-s-h/index.html

---
layout: mobile_sdk
title: "ENGLISH"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ENGLISH"
id: -e-n-g-l-i-s-h
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-e-n-g-l-i-s-h"
---
# ENGLISH

ENGLISH

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-e-s-p-e-r-a-n-t-o/index.html

---
layout: mobile_sdk
title: "ESPERANTO"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ESPERANTO"
id: -e-s-p-e-r-a-n-t-o
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-e-s-p-e-r-a-n-t-o"
---
# ESPERANTO

ESPERANTO

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-e-s-t-o-n-i-a-n/index.html

---
layout: mobile_sdk
title: "ESTONIAN"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ESTONIAN"
id: -e-s-t-o-n-i-a-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-e-s-t-o-n-i-a-n"
---
# ESTONIAN

ESTONIAN

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-f-i-n-n-i-s-h/index.html

---
layout: mobile_sdk
title: "FINNISH"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "FINNISH"
id: -f-i-n-n-i-s-h
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-f-i-n-n-i-s-h"
---
# FINNISH

FINNISH

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-f-r-e-n-c-h/index.html

---
layout: mobile_sdk
title: "FRENCH"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "FRENCH"
id: -f-r-e-n-c-h
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-f-r-e-n-c-h"
---
# FRENCH

FRENCH

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-f-r-i-s-i-a-n/index.html

---
layout: mobile_sdk
title: "FRISIAN"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "FRISIAN"
id: -f-r-i-s-i-a-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-f-r-i-s-i-a-n"
---
# FRISIAN

FRISIAN

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-g-a-l-i-c-i-a-n/index.html

---
layout: mobile_sdk
title: "GALICIAN"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "GALICIAN"
id: -g-a-l-i-c-i-a-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-g-a-l-i-c-i-a-n"
---
# GALICIAN

GALICIAN

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-g-e-o-r-g-i-a-n/index.html

---
layout: mobile_sdk
title: "GEORGIAN"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "GEORGIAN"
id: -g-e-o-r-g-i-a-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-g-e-o-r-g-i-a-n"
---
# GEORGIAN

GEORGIAN

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-g-e-r-m-a-n/index.html

---
layout: mobile_sdk
title: "GERMAN"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "GERMAN"
id: -g-e-r-m-a-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-g-e-r-m-a-n"
---
# GERMAN

GERMAN

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-g-r-e-e-k/index.html

---
layout: mobile_sdk
title: "GREEK"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "GREEK"
id: -g-r-e-e-k
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-g-r-e-e-k"
---
# GREEK

GREEK

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-h-e-b-r-e-w/index.html

---
layout: mobile_sdk
title: "HEBREW"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "HEBREW"
id: -h-e-b-r-e-w
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-h-e-b-r-e-w"
---
# HEBREW

HEBREW

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-h-i-n-d-i/index.html

---
layout: mobile_sdk
title: "HINDI"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "HINDI"
id: -h-i-n-d-i
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-h-i-n-d-i"
---
# HINDI

HINDI

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-h-u-n-g-a-r-i-a-n/index.html

---
layout: mobile_sdk
title: "HUNGARIAN"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "HUNGARIAN"
id: -h-u-n-g-a-r-i-a-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-h-u-n-g-a-r-i-a-n"
---
# HUNGARIAN

HUNGARIAN

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-i-c-e-l-a-n-d-i-c/index.html

---
layout: mobile_sdk
title: "ICELANDIC"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ICELANDIC"
id: -i-c-e-l-a-n-d-i-c
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-i-c-e-l-a-n-d-i-c"
---
# ICELANDIC

ICELANDIC

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-i-n-d-o-n-e-s-i-a-n/index.html

---
layout: mobile_sdk
title: "INDONESIAN"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "INDONESIAN"
id: -i-n-d-o-n-e-s-i-a-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-i-n-d-o-n-e-s-i-a-n"
---
# INDONESIAN

INDONESIAN

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-i-r-i-s-h/index.html

---
layout: mobile_sdk
title: "IRISH"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "IRISH"
id: -i-r-i-s-h
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-i-r-i-s-h"
---
# IRISH

IRISH

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-i-t-a-l-i-a-n/index.html

---
layout: mobile_sdk
title: "ITALIAN"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ITALIAN"
id: -i-t-a-l-i-a-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-i-t-a-l-i-a-n"
---
# ITALIAN

ITALIAN

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-j-a-p-a-n-e-s-e/index.html

---
layout: mobile_sdk
title: "JAPANESE"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "JAPANESE"
id: -j-a-p-a-n-e-s-e
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-j-a-p-a-n-e-s-e"
---
# JAPANESE

JAPANESE

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-j-a-p-a-n-e-s-e_-h-i-r-a-g-a-n-a/index.html

---
layout: mobile_sdk
title: "JAPANESE_HIRAGANA"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "JAPANESE_HIRAGANA"
id: -j-a-p-a-n-e-s-e_-h-i-r-a-g-a-n-a
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-j-a-p-a-n-e-s-e_-h-i-r-a-g-a-n-a"
---
# JAPANESE_HIRAGANA

JAPANESE_HIRAGANA

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-j-a-p-a-n-e-s-e_-k-a-n-a/index.html

---
layout: mobile_sdk
title: "JAPANESE_KANA"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "JAPANESE_KANA"
id: -j-a-p-a-n-e-s-e_-k-a-n-a
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-j-a-p-a-n-e-s-e_-k-a-n-a"
---
# JAPANESE_KANA

JAPANESE_KANA

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-j-a-p-a-n-e-s-e_-l-a-t-i-n/index.html

---
layout: mobile_sdk
title: "JAPANESE_LATIN"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "JAPANESE_LATIN"
id: -j-a-p-a-n-e-s-e_-l-a-t-i-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-j-a-p-a-n-e-s-e_-l-a-t-i-n"
---
# JAPANESE_LATIN

JAPANESE_LATIN

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-k-a-n-n-a-d-a/index.html

---
layout: mobile_sdk
title: "KANNADA"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "KANNADA"
id: -k-a-n-n-a-d-a
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-k-a-n-n-a-d-a"
---
# KANNADA

KANNADA

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-k-a-z-a-k-h/index.html

---
layout: mobile_sdk
title: "KAZAKH"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "KAZAKH"
id: -k-a-z-a-k-h
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-k-a-z-a-k-h"
---
# KAZAKH

KAZAKH

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-k-o-r-e-a-n/index.html

---
layout: mobile_sdk
title: "KOREAN"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "KOREAN"
id: -k-o-r-e-a-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-k-o-r-e-a-n"
---
# KOREAN

KOREAN

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-k-o-r-e-a-n_-l-a-t-i-n/index.html

---
layout: mobile_sdk
title: "KOREAN_LATIN"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "KOREAN_LATIN"
id: -k-o-r-e-a-n_-l-a-t-i-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-k-o-r-e-a-n_-l-a-t-i-n"
---
# KOREAN_LATIN

KOREAN_LATIN

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-k-u-r-d-i-s-h/index.html

---
layout: mobile_sdk
title: "KURDISH"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "KURDISH"
id: -k-u-r-d-i-s-h
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-k-u-r-d-i-s-h"
---
# KURDISH

KURDISH

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-l-a-t-v-i-a-n/index.html

---
layout: mobile_sdk
title: "LATVIAN"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "LATVIAN"
id: -l-a-t-v-i-a-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-l-a-t-v-i-a-n"
---
# LATVIAN

LATVIAN

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-l-i-t-h-u-a-n-i-a-n/index.html

---
layout: mobile_sdk
title: "LITHUANIAN"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "LITHUANIAN"
id: -l-i-t-h-u-a-n-i-a-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-l-i-t-h-u-a-n-i-a-n"
---
# LITHUANIAN

LITHUANIAN

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-l-u-x-e-m-b-o-u-r-g-i-s-h/index.html

---
layout: mobile_sdk
title: "LUXEMBOURGISH"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "LUXEMBOURGISH"
id: -l-u-x-e-m-b-o-u-r-g-i-s-h
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-l-u-x-e-m-b-o-u-r-g-i-s-h"
---
# LUXEMBOURGISH

LUXEMBOURGISH

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-m-a-c-e-d-o-n-i-a-n/index.html

---
layout: mobile_sdk
title: "MACEDONIAN"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MACEDONIAN"
id: -m-a-c-e-d-o-n-i-a-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-m-a-c-e-d-o-n-i-a-n"
---
# MACEDONIAN

MACEDONIAN

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-m-a-l-a-y/index.html

---
layout: mobile_sdk
title: "MALAY"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MALAY"
id: -m-a-l-a-y
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-m-a-l-a-y"
---
# MALAY

MALAY

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-m-a-l-t-e-s-e/index.html

---
layout: mobile_sdk
title: "MALTESE"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MALTESE"
id: -m-a-l-t-e-s-e
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-m-a-l-t-e-s-e"
---
# MALTESE

MALTESE

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-m-a-r-a-t-h-i/index.html

---
layout: mobile_sdk
title: "MARATHI"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MARATHI"
id: -m-a-r-a-t-h-i
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-m-a-r-a-t-h-i"
---
# MARATHI

MARATHI

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-m-o-n-g-o-l-i-a-n/index.html

---
layout: mobile_sdk
title: "MONGOLIAN"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MONGOLIAN"
id: -m-o-n-g-o-l-i-a-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-m-o-n-g-o-l-i-a-n"
---
# MONGOLIAN

MONGOLIAN

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-n-e-p-a-l-i/index.html

---
layout: mobile_sdk
title: "NEPALI"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "NEPALI"
id: -n-e-p-a-l-i
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-n-e-p-a-l-i"
---
# NEPALI

NEPALI

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-n-o-r-w-e-g-i-a-n/index.html

---
layout: mobile_sdk
title: "NORWEGIAN"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "NORWEGIAN"
id: -n-o-r-w-e-g-i-a-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-n-o-r-w-e-g-i-a-n"
---
# NORWEGIAN

NORWEGIAN

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-o-c-c-i-t-a-n/index.html

---
layout: mobile_sdk
title: "OCCITAN"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "OCCITAN"
id: -o-c-c-i-t-a-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-o-c-c-i-t-a-n"
---
# OCCITAN

OCCITAN

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-p-e-r-s-i-a-n/index.html

---
layout: mobile_sdk
title: "PERSIAN"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "PERSIAN"
id: -p-e-r-s-i-a-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-p-e-r-s-i-a-n"
---
# PERSIAN

PERSIAN

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-p-o-l-i-s-h/index.html

---
layout: mobile_sdk
title: "POLISH"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "POLISH"
id: -p-o-l-i-s-h
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-p-o-l-i-s-h"
---
# POLISH

POLISH

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-p-o-r-t-u-g-u-e-s-e/index.html

---
layout: mobile_sdk
title: "PORTUGUESE"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "PORTUGUESE"
id: -p-o-r-t-u-g-u-e-s-e
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-p-o-r-t-u-g-u-e-s-e"
---
# PORTUGUESE

PORTUGUESE

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-p-u-n-j-a-b-i/index.html

---
layout: mobile_sdk
title: "PUNJABI"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "PUNJABI"
id: -p-u-n-j-a-b-i
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-p-u-n-j-a-b-i"
---
# PUNJABI

PUNJABI

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-r-o-m-a-n-i-a-n/index.html

---
layout: mobile_sdk
title: "ROMANIAN"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ROMANIAN"
id: -r-o-m-a-n-i-a-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-r-o-m-a-n-i-a-n"
---
# ROMANIAN

ROMANIAN

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-r-o-m-a-n-s-h/index.html

---
layout: mobile_sdk
title: "ROMANSH"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ROMANSH"
id: -r-o-m-a-n-s-h
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-r-o-m-a-n-s-h"
---
# ROMANSH

ROMANSH

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-r-u-s-s-i-a-n/index.html

---
layout: mobile_sdk
title: "RUSSIAN"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "RUSSIAN"
id: -r-u-s-s-i-a-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-r-u-s-s-i-a-n"
---
# RUSSIAN

RUSSIAN

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-s-a-r-d-i-n-i-a-n/index.html

---
layout: mobile_sdk
title: "SARDINIAN"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "SARDINIAN"
id: -s-a-r-d-i-n-i-a-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-s-a-r-d-i-n-i-a-n"
---
# SARDINIAN

SARDINIAN

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-s-c-o-t-t-i-s-h_-g-a-e-l-i-c/index.html

---
layout: mobile_sdk
title: "SCOTTISH_GAELIC"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "SCOTTISH_GAELIC"
id: -s-c-o-t-t-i-s-h_-g-a-e-l-i-c
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-s-c-o-t-t-i-s-h_-g-a-e-l-i-c"
---
# SCOTTISH_GAELIC

SCOTTISH_GAELIC

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-s-e-r-b-i-a-n_-c-y-r-i-l-l-i-c/index.html

---
layout: mobile_sdk
title: "SERBIAN_CYRILLIC"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "SERBIAN_CYRILLIC"
id: -s-e-r-b-i-a-n_-c-y-r-i-l-l-i-c
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-s-e-r-b-i-a-n_-c-y-r-i-l-l-i-c"
---
# SERBIAN_CYRILLIC

SERBIAN_CYRILLIC

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-s-e-r-b-i-a-n_-l-a-t-i-n/index.html

---
layout: mobile_sdk
title: "SERBIAN_LATIN"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "SERBIAN_LATIN"
id: -s-e-r-b-i-a-n_-l-a-t-i-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-s-e-r-b-i-a-n_-l-a-t-i-n"
---
# SERBIAN_LATIN

SERBIAN_LATIN

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-s-i-m-p-l-i-f-i-e-d_-c-h-i-n-e-s-e/index.html

---
layout: mobile_sdk
title: "SIMPLIFIED_CHINESE"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "SIMPLIFIED_CHINESE"
id: -s-i-m-p-l-i-f-i-e-d_-c-h-i-n-e-s-e
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-s-i-m-p-l-i-f-i-e-d_-c-h-i-n-e-s-e"
---
# SIMPLIFIED_CHINESE

SIMPLIFIED_CHINESE

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-s-l-o-v-a-k/index.html

---
layout: mobile_sdk
title: "SLOVAK"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "SLOVAK"
id: -s-l-o-v-a-k
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-s-l-o-v-a-k"
---
# SLOVAK

SLOVAK

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-s-l-o-v-e-n-e/index.html

---
layout: mobile_sdk
title: "SLOVENE"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "SLOVENE"
id: -s-l-o-v-e-n-e
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-s-l-o-v-e-n-e"
---
# SLOVENE

SLOVENE

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-s-p-a-n-i-s-h/index.html

---
layout: mobile_sdk
title: "SPANISH"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "SPANISH"
id: -s-p-a-n-i-s-h
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-s-p-a-n-i-s-h"
---
# SPANISH

SPANISH

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-s-w-a-h-i-l-i/index.html

---
layout: mobile_sdk
title: "SWAHILI"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "SWAHILI"
id: -s-w-a-h-i-l-i
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-s-w-a-h-i-l-i"
---
# SWAHILI

SWAHILI

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-s-w-e-d-i-s-h/index.html

---
layout: mobile_sdk
title: "SWEDISH"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "SWEDISH"
id: -s-w-e-d-i-s-h
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-s-w-e-d-i-s-h"
---
# SWEDISH

SWEDISH

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-t-a-g-a-l-o-g/index.html

---
layout: mobile_sdk
title: "TAGALOG"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "TAGALOG"
id: -t-a-g-a-l-o-g
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-t-a-g-a-l-o-g"
---
# TAGALOG

TAGALOG

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-t-a-m-i-l/index.html

---
layout: mobile_sdk
title: "TAMIL"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "TAMIL"
id: -t-a-m-i-l
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-t-a-m-i-l"
---
# TAMIL

TAMIL

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-t-e-l-u-g-u/index.html

---
layout: mobile_sdk
title: "TELUGU"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "TELUGU"
id: -t-e-l-u-g-u
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-t-e-l-u-g-u"
---
# TELUGU

TELUGU

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-t-h-a-i/index.html

---
layout: mobile_sdk
title: "THAI"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "THAI"
id: -t-h-a-i
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-t-h-a-i"
---
# THAI

THAI

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-t-r-a-d-i-t-i-o-n-a-l_-c-h-i-n-e-s-e/index.html

---
layout: mobile_sdk
title: "TRADITIONAL_CHINESE"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "TRADITIONAL_CHINESE"
id: -t-r-a-d-i-t-i-o-n-a-l_-c-h-i-n-e-s-e
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-t-r-a-d-i-t-i-o-n-a-l_-c-h-i-n-e-s-e"
---
# TRADITIONAL_CHINESE

TRADITIONAL_CHINESE

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-t-u-r-k-i-s-h/index.html

---
layout: mobile_sdk
title: "TURKISH"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "TURKISH"
id: -t-u-r-k-i-s-h
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-t-u-r-k-i-s-h"
---
# TURKISH

TURKISH

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-u-k-r-a-i-n-i-a-n/index.html

---
layout: mobile_sdk
title: "UKRAINIAN"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "UKRAINIAN"
id: -u-k-r-a-i-n-i-a-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-u-k-r-a-i-n-i-a-n"
---
# UKRAINIAN

UKRAINIAN

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-u-r-d-u/index.html

---
layout: mobile_sdk
title: "URDU"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "URDU"
id: -u-r-d-u
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-u-r-d-u"
---
# URDU

URDU

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-v-i-e-t-n-a-m-e-s-e/index.html

---
layout: mobile_sdk
title: "VIETNAMESE"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "VIETNAMESE"
id: -v-i-e-t-n-a-m-e-s-e
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-v-i-e-t-n-a-m-e-s-e"
---
# VIETNAMESE

VIETNAMESE

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-w-e-l-s-h/index.html

---
layout: mobile_sdk
title: "WELSH"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "WELSH"
id: -w-e-l-s-h
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-w-e-l-s-h"
---
# WELSH

WELSH

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-w-e-s-t-e-r-n_-p-u-n-j-a-b-i/index.html

---
layout: mobile_sdk
title: "WESTERN_PUNJABI"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "WESTERN_PUNJABI"
id: -w-e-s-t-e-r-n_-p-u-n-j-a-b-i
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/-w-e-s-t-e-r-n_-p-u-n-j-a-b-i"
---
# WESTERN_PUNJABI

WESTERN_PUNJABI

Members

## Properties

code

val code: String

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/code.html

---
layout: mobile_sdk
title: "code"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "code"
id: code
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language"
---
# code

val code: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/entries.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language"
---
# entries

val entries: EnumEntries<MTCountryLanguage>Returns a representation of an immutable list of all enum entries, in the order they're declared.This method may be used to iterate over the enum entries.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/index.html

---
layout: mobile_sdk
title: "MTCountryLanguage"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTCountryLanguage"
id: -m-t-country-language
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language"
---
# MTCountryLanguage

@Serializableenum MTCountryLanguage : Enum<MTCountryLanguage> Country-specific map label languages.

MembersEntries

## Entries

ALBANIAN

ALBANIAN

AMHARIC

AMHARIC

ARABIC

ARABIC

ARMENIAN

ARMENIAN

AZERBAIJANI

AZERBAIJANI

BASQUE

BASQUE

BELARUSIAN

BELARUSIAN

BENGALI

BENGALI

BOSNIAN

BOSNIAN

BRETON

BRETON

BULGARIAN

BULGARIAN

CATALAN

CATALAN

CHINESE

CHINESE

TRADITIONAL_CHINESE

TRADITIONAL_CHINESE

SIMPLIFIED_CHINESE

SIMPLIFIED_CHINESE

CORSICAN

CORSICAN

CROATIAN

CROATIAN

CZECH

CZECH

DANISH

DANISH

DUTCH

DUTCH

ENGLISH

ENGLISH

ESPERANTO

ESPERANTO

ESTONIAN

ESTONIAN

FINNISH

FINNISH

FRENCH

FRENCH

FRISIAN

FRISIAN

GALICIAN

GALICIAN

GEORGIAN

GEORGIAN

GERMAN

GERMAN

GREEK

GREEK

HEBREW

HEBREW

HINDI

HINDI

HUNGARIAN

HUNGARIAN

ICELANDIC

ICELANDIC

INDONESIAN

INDONESIAN

IRISH

IRISH

ITALIAN

ITALIAN

JAPANESE

JAPANESE

JAPANESE_HIRAGANA

JAPANESE_HIRAGANA

JAPANESE_LATIN

JAPANESE_LATIN

JAPANESE_KANA

JAPANESE_KANA

KANNADA

KANNADA

KAZAKH

KAZAKH

KOREAN

KOREAN

KOREAN_LATIN

KOREAN_LATIN

KURDISH

KURDISH

CLASSICAL_LATIN

CLASSICAL_LATIN

LATVIAN

LATVIAN

LITHUANIAN

LITHUANIAN

LUXEMBOURGISH

LUXEMBOURGISH

MACEDONIAN

MACEDONIAN

MALAY

MALAY

MALTESE

MALTESE

MARATHI

MARATHI

MONGOLIAN

MONGOLIAN

NEPALI

NEPALI

NORWEGIAN

NORWEGIAN

OCCITAN

OCCITAN

PERSIAN

PERSIAN

POLISH

POLISH

PORTUGUESE

PORTUGUESE

PUNJABI

PUNJABI

WESTERN_PUNJABI

WESTERN_PUNJABI

ROMANIAN

ROMANIAN

ROMANSH

ROMANSH

RUSSIAN

RUSSIAN

SARDINIAN

SARDINIAN

SCOTTISH_GAELIC

SCOTTISH_GAELIC

SERBIAN_CYRILLIC

SERBIAN_CYRILLIC

SERBIAN_LATIN

SERBIAN_LATIN

SLOVAK

SLOVAK

SLOVENE

SLOVENE

SPANISH

SPANISH

SWAHILI

SWAHILI

SWEDISH

SWEDISH

TAGALOG

TAGALOG

TAMIL

TAMIL

TELUGU

TELUGU

THAI

THAI

TURKISH

TURKISH

UKRAINIAN

UKRAINIAN

URDU

URDU

VIETNAMESE

VIETNAMESE

WELSH

WELSH

## Properties

code

val code: String

entries

val entries: EnumEntries<MTCountryLanguage>Returns a representation of an immutable list of all enum entries, in the order they're declared.

name

val name: String

ordinal

val ordinal: Int

## Functions

valueOf

fun valueOf(value: String): MTCountryLanguageReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

values

fun values(): Array<MTCountryLanguage>Returns an array containing the constants of this enum type, in the order they're declared.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/value-of.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language"
---
# valueOf

fun valueOf(value: String): MTCountryLanguageReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
#### Throws

IllegalArgumentExceptionif this enum type has no constant with the specified name

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language/values.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-country-language"
---
# values

fun values(): Array<MTCountryLanguage>Returns an array containing the constants of this enum type, in the order they're declared.This method may be used to iterate over the constants.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-data/-m-t-data.html

---
layout: mobile_sdk
title: "MTData"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTData"
id: -m-t-data
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-data"
---
# MTData

constructor(id: String? = null, coordinate: LngLat? = null, point: MTPoint? = null, dataType: String? = null, isSourceLoaded: Boolean? = null, source: MTSourceData? = null, sourceDataType: String? = null)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-data/coordinate.html

---
layout: mobile_sdk
title: "coordinate"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "coordinate"
id: coordinate
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-data"
---
# coordinate

@SerialName(value = "lngLat")val coordinate: LngLat? = nullCoordinate of the event tap.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-data/data-type.html

---
layout: mobile_sdk
title: "dataType"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "dataType"
id: data-type
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-data"
---
# dataType

val dataType: String? = nullType of the event.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-data/id.html

---
layout: mobile_sdk
title: "id"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "id"
id: id
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-data"
---
# id

val id: String? = nullUnique id.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-data/index.html

---
layout: mobile_sdk
title: "MTData"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTData"
id: -m-t-data
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-data"
---
# MTData

@Serializabledata class MTData(val id: String? = null, val coordinate: LngLat? = null, val point: MTPoint? = null, val dataType: String? = null, val isSourceLoaded: Boolean? = null, val source: MTSourceData? = null, val sourceDataType: String? = null)Object sent together with MTEvent.

Members

## Constructors

MTData

constructor(id: String? = null, coordinate: LngLat? = null, point: MTPoint? = null, dataType: String? = null, isSourceLoaded: Boolean? = null, source: MTSourceData? = null, sourceDataType: String? = null)

## Properties

coordinate

@SerialName(value = "lngLat")val coordinate: LngLat? = nullCoordinate of the event tap.

dataType

val dataType: String? = nullType of the event.

id

val id: String? = nullUnique id.

isSourceLoaded

val isSourceLoaded: Boolean? = nullBoolean indicating if source is fully  loaded.

point

val point: MTPoint? = nullPoint of the event tap.

source

val source: MTSourceData? = nullSource data.

sourceDataType

val sourceDataType: String? = nullType of the source data.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-data/is-source-loaded.html

---
layout: mobile_sdk
title: "isSourceLoaded"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "isSourceLoaded"
id: is-source-loaded
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-data"
---
# isSourceLoaded

val isSourceLoaded: Boolean? = nullBoolean indicating if source is fully  loaded.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-data/point.html

---
layout: mobile_sdk
title: "point"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "point"
id: point
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-data"
---
# point

val point: MTPoint? = nullPoint of the event tap.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-data/source-data-type.html

---
layout: mobile_sdk
title: "sourceDataType"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "sourceDataType"
id: source-data-type
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-data"
---
# sourceDataType

val sourceDataType: String? = nullType of the source data.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-data/source.html

---
layout: mobile_sdk
title: "source"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "source"
id: source
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-data"
---
# source

val source: MTSourceData? = nullSource data.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-language/-country/-country.html

---
layout: mobile_sdk
title: "Country"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Country"
id: -country
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-language/-country"
---
# Country

constructor(language: MTCountryLanguage)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-language/-country/index.html

---
layout: mobile_sdk
title: "Country"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Country"
id: -country
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-language/-country"
---
# Country

@Serializabledata class Country(val language: MTCountryLanguage) : MTLanguageCountry-specific language.

Members

## Constructors

Country

constructor(language: MTCountryLanguage)

## Properties

language

val language: MTCountryLanguage

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-language/-country/language.html

---
layout: mobile_sdk
title: "language"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "language"
id: language
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-language/-country"
---
# language

val language: MTCountryLanguage

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-language/-special/-special.html

---
layout: mobile_sdk
title: "Special"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Special"
id: -special
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-language/-special"
---
# Special

constructor(language: MTSpecialLanguage)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-language/-special/index.html

---
layout: mobile_sdk
title: "Special"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Special"
id: -special
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-language/-special"
---
# Special

@Serializabledata class Special(val language: MTSpecialLanguage) : MTLanguageCustom language options.

Members

## Constructors

Special

constructor(language: MTSpecialLanguage)

## Properties

language

val language: MTSpecialLanguage

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-language/-special/language.html

---
layout: mobile_sdk
title: "language"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "language"
id: language
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-language/-special"
---
# language

val language: MTSpecialLanguage

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-language/index.html

---
layout: mobile_sdk
title: "MTLanguage"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTLanguage"
id: -m-t-language
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-language"
---
# MTLanguage

@Serializable(with = MTLanguageSerializer::class)sealed interface MTLanguageLanguage of the map labels.
#### Inheritors

SpecialCountry

Members

## Types

Country

@Serializabledata class Country(val language: MTCountryLanguage) : MTLanguageCountry-specific language.

Special

@Serializabledata class Special(val language: MTSpecialLanguage) : MTLanguageCustom language options.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-language-serializer/descriptor.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-language-serializer"
---
# descriptor

open override val descriptor: SerialDescriptor

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-language-serializer/deserialize.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-language-serializer"
---
# deserialize

open override fun deserialize(decoder: Decoder): MTLanguage

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-language-serializer/index.html

---
layout: mobile_sdk
title: "MTLanguageSerializer"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTLanguageSerializer"
id: -m-t-language-serializer
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-language-serializer"
---
# MTLanguageSerializer

object MTLanguageSerializer : KSerializer<MTLanguage> 

Members

## Properties

descriptor

open override val descriptor: SerialDescriptor

## Functions

deserialize

open override fun deserialize(decoder: Decoder): MTLanguage

serialize

open override fun serialize(encoder: Encoder, value: MTLanguage)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-language-serializer/serialize.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-language-serializer"
---
# serialize

open override fun serialize(encoder: Encoder, value: MTLanguage)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-map-corner/-b-o-t-t-o-m_-l-e-f-t/index.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-map-corner/-b-o-t-t-o-m_-l-e-f-t"
---
# BOTTOM_LEFT

@SerialName(value = "bottom-left")BOTTOM_LEFTBottom left corner of the map.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-map-corner/-b-o-t-t-o-m_-r-i-g-h-t/index.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-map-corner/-b-o-t-t-o-m_-r-i-g-h-t"
---
# BOTTOM_RIGHT

@SerialName(value = "bottom-right")BOTTOM_RIGHTBottom right corner of the map.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-map-corner/-t-o-p_-l-e-f-t/index.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-map-corner/-t-o-p_-l-e-f-t"
---
# TOP_LEFT

@SerialName(value = "top-left")TOP_LEFTTop left corner of the map.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-map-corner/-t-o-p_-r-i-g-h-t/index.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-map-corner/-t-o-p_-r-i-g-h-t"
---
# TOP_RIGHT

@SerialName(value = "top-right")TOP_RIGHTTop right corner of the map.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-map-corner/entries.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-map-corner"
---
# entries

val entries: EnumEntries<MTMapCorner>Returns a representation of an immutable list of all enum entries, in the order they're declared.This method may be used to iterate over the enum entries.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-map-corner/index.html

---
layout: mobile_sdk
title: "MTMapCorner"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTMapCorner"
id: -m-t-map-corner
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-map-corner"
---
# MTMapCorner

@Serializableenum MTMapCorner : Enum<MTMapCorner> 

MembersEntries

## Entries

TOP_LEFT

@SerialName(value = "top-left")TOP_LEFTTop left corner of the map.

TOP_RIGHT

@SerialName(value = "top-right")TOP_RIGHTTop right corner of the map.

BOTTOM_LEFT

@SerialName(value = "bottom-left")BOTTOM_LEFTBottom left corner of the map.

BOTTOM_RIGHT

@SerialName(value = "bottom-right")BOTTOM_RIGHTBottom right corner of the map.

## Properties

entries

val entries: EnumEntries<MTMapCorner>Returns a representation of an immutable list of all enum entries, in the order they're declared.

name

val name: String

ordinal

val ordinal: Int

## Functions

valueOf

fun valueOf(value: String): MTMapCornerReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

values

fun values(): Array<MTMapCorner>Returns an array containing the constants of this enum type, in the order they're declared.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-map-corner/value-of.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-map-corner"
---
# valueOf

fun valueOf(value: String): MTMapCornerReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
#### Throws

IllegalArgumentExceptionif this enum type has no constant with the specified name

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-map-corner/values.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-map-corner"
---
# values

fun values(): Array<MTMapCorner>Returns an array containing the constants of this enum type, in the order they're declared.This method may be used to iterate over the constants.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-point/-m-t-point.html

---
layout: mobile_sdk
title: "MTPoint"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTPoint"
id: -m-t-point
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-point"
---
# MTPoint

constructor(x: Double, y: Double)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-point/index.html

---
layout: mobile_sdk
title: "MTPoint"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTPoint"
id: -m-t-point
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-point"
---
# MTPoint

@Serializabledata class MTPoint(val x: Double, val y: Double)Two numbers representing x and y screen coordinates in pixels.

Members

## Constructors

MTPoint

constructor(x: Double, y: Double)

## Properties

x

val x: Double

y

val y: Double

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-point/x.html

---
layout: mobile_sdk
title: "x"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "x"
id: x
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-point"
---
# x

val x: Double

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-point/y.html

---
layout: mobile_sdk
title: "y"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "y"
id: y
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-point"
---
# y

val y: Double

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-projection-type/-g-l-o-b-e/index.html

---
layout: mobile_sdk
title: "GLOBE"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "GLOBE"
id: -g-l-o-b-e
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-projection-type/-g-l-o-b-e"
---
# GLOBE

@SerialName(value = "globe")GLOBEGlobe projection.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-projection-type/-m-e-r-c-a-t-o-r/index.html

---
layout: mobile_sdk
title: "MERCATOR"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MERCATOR"
id: -m-e-r-c-a-t-o-r
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-projection-type/-m-e-r-c-a-t-o-r"
---
# MERCATOR

@SerialName(value = "mercator")MERCATORMercator projection.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-projection-type/entries.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-projection-type"
---
# entries

val entries: EnumEntries<MTProjectionType>Returns a representation of an immutable list of all enum entries, in the order they're declared.This method may be used to iterate over the enum entries.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-projection-type/index.html

---
layout: mobile_sdk
title: "MTProjectionType"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTProjectionType"
id: -m-t-projection-type
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-projection-type"
---
# MTProjectionType

@Serializableenum MTProjectionType : Enum<MTProjectionType> 

MembersEntries

## Entries

MERCATOR

@SerialName(value = "mercator")MERCATORMercator projection.

GLOBE

@SerialName(value = "globe")GLOBEGlobe projection.

## Properties

entries

val entries: EnumEntries<MTProjectionType>Returns a representation of an immutable list of all enum entries, in the order they're declared.

name

val name: String

ordinal

val ordinal: Int

## Functions

valueOf

fun valueOf(value: String): MTProjectionTypeReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

values

fun values(): Array<MTProjectionType>Returns an array containing the constants of this enum type, in the order they're declared.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-projection-type/value-of.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-projection-type"
---
# valueOf

fun valueOf(value: String): MTProjectionTypeReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
#### Throws

IllegalArgumentExceptionif this enum type has no constant with the specified name

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-projection-type/values.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-projection-type"
---
# values

fun values(): Array<MTProjectionType>Returns an array containing the constants of this enum type, in the order they're declared.This method may be used to iterate over the constants.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-source-data/-m-t-source-data.html

---
layout: mobile_sdk
title: "MTSourceData"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTSourceData"
id: -m-t-source-data
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-source-data"
---
# MTSourceData

constructor(type: String? = null, url: String? = null, attribution: String? = null)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-source-data/attribution.html

---
layout: mobile_sdk
title: "attribution"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "attribution"
id: attribution
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-source-data"
---
# attribution

val attribution: String? = nullAttribution string.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-source-data/index.html

---
layout: mobile_sdk
title: "MTSourceData"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTSourceData"
id: -m-t-source-data
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-source-data"
---
# MTSourceData

@Serializabledata class MTSourceData(val type: String? = null, val url: String? = null, val attribution: String? = null)The style spec representation of the source if the event has a dataType of source .

Members

## Constructors

MTSourceData

constructor(type: String? = null, url: String? = null, attribution: String? = null)

## Properties

attribution

val attribution: String? = nullAttribution string.

type

val type: String? = nullType of the source.

url

val url: String? = nullUrl of the source resource.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-source-data/type.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-source-data"
---
# type

val type: String? = nullType of the source.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-source-data/url.html

---
layout: mobile_sdk
title: "url"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "url"
id: url
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-source-data"
---
# url

val url: String? = nullUrl of the source resource.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-special-language/-a-u-t-o/index.html

---
layout: mobile_sdk
title: "AUTO"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "AUTO"
id: -a-u-t-o
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-special-language/-a-u-t-o"
---
# AUTO

AUTOThe default language of the device.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-special-language/-i-n-t-e-r-n-a-t-i-o-n-a-l/index.html

---
layout: mobile_sdk
title: "INTERNATIONAL"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "INTERNATIONAL"
id: -i-n-t-e-r-n-a-t-i-o-n-a-l
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-special-language/-i-n-t-e-r-n-a-t-i-o-n-a-l"
---
# INTERNATIONAL

INTERNATIONALThe international name. This option is equivalent to OSM's name int_name.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-special-language/-l-a-t-i-n/index.html

---
layout: mobile_sdk
title: "LATIN"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "LATIN"
id: -l-a-t-i-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-special-language/-l-a-t-i-n"
---
# LATIN

LATINDefault fallback language in the Latin charset.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-special-language/-l-o-c-a-l/index.html

---
layout: mobile_sdk
title: "LOCAL"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "LOCAL"
id: -l-o-c-a-l
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-special-language/-l-o-c-a-l"
---
# LOCAL

LOCALLocal language for each country.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-special-language/-n-o-n_-l-a-t-i-n/index.html

---
layout: mobile_sdk
title: "NON_LATIN"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "NON_LATIN"
id: -n-o-n_-l-a-t-i-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-special-language/-n-o-n_-l-a-t-i-n"
---
# NON_LATIN

NON_LATINFallback language in a non-Latin charset.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-special-language/-s-t-y-l-e/index.html

---
layout: mobile_sdk
title: "STYLE"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "STYLE"
id: -s-t-y-l-e
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-special-language/-s-t-y-l-e"
---
# STYLE

STYLELanguage defined by the style.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-special-language/-v-i-s-i-t-o-r/index.html

---
layout: mobile_sdk
title: "VISITOR"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "VISITOR"
id: -v-i-s-i-t-o-r
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-special-language/-v-i-s-i-t-o-r"
---
# VISITOR

VISITORPreferred user setting with default name.Useful when traveling to access both local and English names.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-special-language/-v-i-s-i-t-o-r_-e-n-g-l-i-s-h/index.html

---
layout: mobile_sdk
title: "VISITOR_ENGLISH"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "VISITOR_ENGLISH"
id: -v-i-s-i-t-o-r_-e-n-g-l-i-s-h
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-special-language/-v-i-s-i-t-o-r_-e-n-g-l-i-s-h"
---
# VISITOR_ENGLISH

VISITOR_ENGLISHEnglish + default name.Useful for multilingual context during travel.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-special-language/entries.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-special-language"
---
# entries

val entries: EnumEntries<MTSpecialLanguage>Returns a representation of an immutable list of all enum entries, in the order they're declared.This method may be used to iterate over the enum entries.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-special-language/index.html

---
layout: mobile_sdk
title: "MTSpecialLanguage"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTSpecialLanguage"
id: -m-t-special-language
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-special-language"
---
# MTSpecialLanguage

@Serializableenum MTSpecialLanguage : Enum<MTSpecialLanguage> Custom language options.

MembersEntries

## Entries

AUTO

AUTOThe default language of the device.

INTERNATIONAL

INTERNATIONALThe international name. This option is equivalent to OSM's name int_name.

LATIN

LATINDefault fallback language in the Latin charset.

LOCAL

LOCALLocal language for each country.

NON_LATIN

NON_LATINFallback language in a non-Latin charset.

STYLE

STYLELanguage defined by the style.

VISITOR

VISITORPreferred user setting with default name.

VISITOR_ENGLISH

VISITOR_ENGLISHEnglish + default name.

## Properties

entries

val entries: EnumEntries<MTSpecialLanguage>Returns a representation of an immutable list of all enum entries, in the order they're declared.

name

val name: String

ordinal

val ordinal: Int

## Functions

valueOf

fun valueOf(value: String): MTSpecialLanguageReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

values

fun values(): Array<MTSpecialLanguage>Returns an array containing the constants of this enum type, in the order they're declared.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-special-language/value-of.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-special-language"
---
# valueOf

fun valueOf(value: String): MTSpecialLanguageReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
#### Throws

IllegalArgumentExceptionif this enum type has no constant with the specified name

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-special-language/values.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/-m-t-special-language"
---
# values

fun values(): Array<MTSpecialLanguage>Returns an array containing the constants of this enum type, in the order they're declared.This method may be used to iterate over the constants.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.types/index.html

---
layout: mobile_sdk
title: "com.maptiler.maptilersdk.map.types"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "com.maptiler.maptilersdk.map.types"
id: com.maptiler.maptilersdk.map.types
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.types"
---
# com.maptiler.maptilersdk.map.types

Types

## Types

MTBounds

@Serializable(with = MTBoundsSerializer::class)data class MTBounds(val southwest: LngLat, val northeast: LngLat)Geographical bounding box represented by south-west and north-east corners.

MTCountryLanguage

@Serializableenum MTCountryLanguage : Enum<MTCountryLanguage> Country-specific map label languages.

MTData

@Serializabledata class MTData(val id: String? = null, val coordinate: LngLat? = null, val point: MTPoint? = null, val dataType: String? = null, val isSourceLoaded: Boolean? = null, val source: MTSourceData? = null, val sourceDataType: String? = null)Object sent together with MTEvent.

MTLanguage

@Serializable(with = MTLanguageSerializer::class)sealed interface MTLanguageLanguage of the map labels.

MTLanguageSerializer

object MTLanguageSerializer : KSerializer<MTLanguage> 

MTMapCorner

@Serializableenum MTMapCorner : Enum<MTMapCorner> 

MTPoint

@Serializabledata class MTPoint(val x: Double, val y: Double)Two numbers representing x and y screen coordinates in pixels.

MTProjectionType

@Serializableenum MTProjectionType : Enum<MTProjectionType> 

MTSourceData

@Serializabledata class MTSourceData(val type: String? = null, val url: String? = null, val attribution: String? = null)The style spec representation of the source if the event has a dataType of source .

MTSpecialLanguage

@Serializableenum MTSpecialLanguage : Enum<MTSpecialLanguage> Custom language options.

---

