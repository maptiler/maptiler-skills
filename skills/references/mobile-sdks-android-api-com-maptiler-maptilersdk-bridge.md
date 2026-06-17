# MapTiler Android SDK API Reference - com.maptiler.maptilersdk.bridge

This document is a part of the Android SDK API reference documentation, covering the `com.maptiler.maptilersdk.bridge` package.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-error/-bridge-not-loaded/index.html

---
layout: mobile_sdk
title: "BridgeNotLoaded"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "BridgeNotLoaded"
id: -bridge-not-loaded
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-error/-bridge-not-loaded"
---
# BridgeNotLoaded

data object BridgeNotLoaded : MTErrorMethod execution halted. Bridge and/or Map are not loaded.

Members

## Properties

cause

open val cause: Throwable?

code

val code: IntNumerical code of the exception.

message

open val message: String?

reason

val reason: StringExplanation of the exception.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-error/-exception-error/-exception-error.html

---
layout: mobile_sdk
title: "ExceptionError"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ExceptionError"
id: -exception-error
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-error/-exception-error"
---
# ExceptionError

constructor(body: MTException)
#### Parameters

bodyException details.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-error/-exception-error/body.html

---
layout: mobile_sdk
title: "body"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "body"
id: body
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-error/-exception-error"
---
# body

val body: MTException
#### Parameters

bodyException details.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-error/-exception-error/index.html

---
layout: mobile_sdk
title: "ExceptionError"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ExceptionError"
id: -exception-error
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-error/-exception-error"
---
# ExceptionError

data class ExceptionError(val body: MTException) : MTErrorMethod execution failed with an exception.
#### Parameters

bodyException details.

Members

## Constructors

ExceptionError

constructor(body: MTException)

## Properties

body

val body: MTException

cause

open val cause: Throwable?

code

val code: IntNumerical code of the exception.

message

open val message: String?

reason

val reason: StringExplanation of the exception.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-error/-invalid-result-type/-invalid-result-type.html

---
layout: mobile_sdk
title: "InvalidResultType"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "InvalidResultType"
id: -invalid-result-type
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-error/-invalid-result-type"
---
# InvalidResultType

constructor(description: String)
#### Parameters

descriptionDebug description of the return type.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-error/-invalid-result-type/description.html

---
layout: mobile_sdk
title: "description"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "description"
id: description
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-error/-invalid-result-type"
---
# description

val description: String
#### Parameters

descriptionDebug description of the return type.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-error/-invalid-result-type/index.html

---
layout: mobile_sdk
title: "InvalidResultType"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "InvalidResultType"
id: -invalid-result-type
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-error/-invalid-result-type"
---
# InvalidResultType

data class InvalidResultType(val description: String) : MTErrorMethod execution returned an invalid result.
#### Parameters

descriptionDebug description of the return type.

Members

## Constructors

InvalidResultType

constructor(description: String)

## Properties

cause

open val cause: Throwable?

code

val code: IntNumerical code of the exception.

description

val description: String

message

open val message: String?

reason

val reason: StringExplanation of the exception.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-error/-missing-parent/index.html

---
layout: mobile_sdk
title: "MissingParent"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MissingParent"
id: -missing-parent
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-error/-missing-parent"
---
# MissingParent

data object MissingParent : MTErrorMethod execution failed due to a missing parent entity.

Members

## Properties

cause

open val cause: Throwable?

code

val code: IntNumerical code of the exception.

message

open val message: String?

reason

val reason: StringExplanation of the exception.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-error/-unknown/-unknown.html

---
layout: mobile_sdk
title: "Unknown"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Unknown"
id: -unknown
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-error/-unknown"
---
# Unknown

constructor(description: String)
#### Parameters

descriptionDebug description of the error.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-error/-unknown/description.html

---
layout: mobile_sdk
title: "description"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "description"
id: description
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-error/-unknown"
---
# description

val description: String
#### Parameters

descriptionDebug description of the error.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-error/-unknown/index.html

---
layout: mobile_sdk
title: "Unknown"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Unknown"
id: -unknown
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-error/-unknown"
---
# Unknown

data class Unknown(val description: String) : MTErrorMethod execution resulted in an unknown error.
#### Parameters

descriptionDebug description of the error.

Members

## Constructors

Unknown

constructor(description: String)

## Properties

cause

open val cause: Throwable?

code

val code: IntNumerical code of the exception.

description

val description: String

message

open val message: String?

reason

val reason: StringExplanation of the exception.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-error/-unsupported-return-type/-unsupported-return-type.html

---
layout: mobile_sdk
title: "UnsupportedReturnType"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "UnsupportedReturnType"
id: -unsupported-return-type
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-error/-unsupported-return-type"
---
# UnsupportedReturnType

constructor(description: String)
#### Parameters

descriptionDebug description of the command that returned an unsupported type.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-error/-unsupported-return-type/description.html

---
layout: mobile_sdk
title: "description"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "description"
id: description
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-error/-unsupported-return-type"
---
# description

val description: String
#### Parameters

descriptionDebug description of the command that returned an unsupported type.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-error/-unsupported-return-type/index.html

---
layout: mobile_sdk
title: "UnsupportedReturnType"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "UnsupportedReturnType"
id: -unsupported-return-type
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-error/-unsupported-return-type"
---
# UnsupportedReturnType

data class UnsupportedReturnType(val description: String) : MTErrorMethod execution returned an unsupported type.
#### Parameters

descriptionDebug description of the command that returned an unsupported type.

Members

## Constructors

UnsupportedReturnType

constructor(description: String)

## Properties

cause

open val cause: Throwable?

code

val code: IntNumerical code of the exception.

description

val description: String

message

open val message: String?

reason

val reason: StringExplanation of the exception.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-error/code.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-error"
---
# code

val code: IntNumerical code of the exception.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-error/index.html

---
layout: mobile_sdk
title: "MTError"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTError"
id: -m-t-error
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-error"
---
# MTError

sealed class MTError : ExceptionRepresents all the errors that can occur in the MapTiler SDK.All methods within the SDK throw MTError.
#### Inheritors

ExceptionErrorInvalidResultTypeUnsupportedReturnTypeUnknownBridgeNotLoadedMissingParent

Members

## Types

BridgeNotLoaded

data object BridgeNotLoaded : MTErrorMethod execution halted. Bridge and/or Map are not loaded.

ExceptionError

data class ExceptionError(val body: MTException) : MTErrorMethod execution failed with an exception.

InvalidResultType

data class InvalidResultType(val description: String) : MTErrorMethod execution returned an invalid result.

MissingParent

data object MissingParent : MTErrorMethod execution failed due to a missing parent entity.

Unknown

data class Unknown(val description: String) : MTErrorMethod execution resulted in an unknown error.

UnsupportedReturnType

data class UnsupportedReturnType(val description: String) : MTErrorMethod execution returned an unsupported type.

## Properties

cause

open val cause: Throwable?

code

val code: IntNumerical code of the exception.

message

open val message: String?

reason

val reason: StringExplanation of the exception.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-error/reason.html

---
layout: mobile_sdk
title: "reason"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "reason"
id: reason
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-error"
---
# reason

val reason: StringExplanation of the exception.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-exception/-m-t-exception.html

---
layout: mobile_sdk
title: "MTException"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTException"
id: -m-t-exception
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-exception"
---
# MTException

constructor(code: Int, reason: String)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-exception/code.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-exception"
---
# code

val code: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-exception/index.html

---
layout: mobile_sdk
title: "MTException"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTException"
id: -m-t-exception
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-exception"
---
# MTException

data class MTException(val code: Int, val reason: String)

Members

## Constructors

MTException

constructor(code: Int, reason: String)

## Properties

code

val code: Int

reason

val reason: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-exception/reason.html

---
layout: mobile_sdk
title: "reason"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "reason"
id: reason
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/-m-t-exception"
---
# reason

val reason: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.bridge/index.html

---
layout: mobile_sdk
title: "com.maptiler.maptilersdk.bridge"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "com.maptiler.maptilersdk.bridge"
id: com.maptiler.maptilersdk.bridge
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.bridge"
---
# com.maptiler.maptilersdk.bridge

Types

## Types

MTError

sealed class MTError : ExceptionRepresents all the errors that can occur in the MapTiler SDK.

MTException

data class MTException(val code: Int, val reason: String)

---

