# MapTiler Android SDK API Reference - com.maptiler.maptilersdk.logging

This document is a part of the Android SDK API reference documentation, covering the `com.maptiler.maptilersdk.logging` package.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log/-m-t-log.html

---
layout: mobile_sdk
title: "MTLog"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTLog"
id: -m-t-log
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log"
---
# MTLog

constructor(message: String, type: MTLogType)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log/index.html

---
layout: mobile_sdk
title: "MTLog"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTLog"
id: -m-t-log
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log"
---
# MTLog

data class MTLog(val message: String, val type: MTLogType)Log object used with MTLogger.

Members

## Constructors

MTLog

constructor(message: String, type: MTLogType)

## Properties

message

val message: StringLog message.

type

val type: MTLogTypeType of the log.

## Functions

printLog

fun printLog()Prints the log to the console.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log/message.html

---
layout: mobile_sdk
title: "message"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "message"
id: message
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log"
---
# message

val message: String

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log/print-log.html

---
layout: mobile_sdk
title: "printLog"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "printLog"
id: print-log
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log"
---
# printLog

fun printLog()Prints the log to the console.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log/type.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log"
---
# type

val type: MTLogType

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log-level/-debug/-debug.html

---
layout: mobile_sdk
title: "Debug"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Debug"
id: -debug
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log-level/-debug"
---
# Debug

constructor(verbose: Boolean = false)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log-level/-debug/index.html

---
layout: mobile_sdk
title: "Debug"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Debug"
id: -debug
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log-level/-debug"
---
# Debug

data class Debug(val verbose: Boolean = false) : MTLogLevelAll logs will be printed.

Members

## Constructors

Debug

constructor(verbose: Boolean = false)

## Properties

verbose

val verbose: Boolean = false

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log-level/-debug/verbose.html

---
layout: mobile_sdk
title: "verbose"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "verbose"
id: verbose
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log-level/-debug"
---
# verbose

val verbose: Boolean = false

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log-level/-info/index.html

---
layout: mobile_sdk
title: "Info"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Info"
id: -info
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log-level/-info"
---
# Info

object Info : MTLogLevelOnly information logs will be printed.

Members

## Functions

equals

open operator override fun equals(other: Any?): Boolean

hashCode

open override fun hashCode(): Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log-level/-none/index.html

---
layout: mobile_sdk
title: "None"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "None"
id: -none
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log-level/-none"
---
# None

object None : MTLogLevelNo logs will be printed.

Members

## Functions

equals

open operator override fun equals(other: Any?): Boolean

hashCode

open override fun hashCode(): Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log-level/equals.html

---
layout: mobile_sdk
title: "equals"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "equals"
id: equals
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log-level"
---
# equals

open operator override fun equals(other: Any?): Boolean

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log-level/hash-code.html

---
layout: mobile_sdk
title: "hashCode"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "hashCode"
id: hash-code
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log-level"
---
# hashCode

open override fun hashCode(): Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log-level/index.html

---
layout: mobile_sdk
title: "MTLogLevel"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTLogLevel"
id: -m-t-log-level
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log-level"
---
# MTLogLevel

sealed class MTLogLevelSDK log level.
#### Inheritors

NoneInfoDebug

Members

## Types

Debug

data class Debug(val verbose: Boolean = false) : MTLogLevelAll logs will be printed.

Info

object Info : MTLogLevelOnly information logs will be printed.

None

object None : MTLogLevelNo logs will be printed.

## Functions

equals

open operator override fun equals(other: Any?): Boolean

hashCode

open override fun hashCode(): Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log-type/-c-r-i-t-i-c-a-l_-e-r-r-o-r/index.html

---
layout: mobile_sdk
title: "CRITICAL_ERROR"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "CRITICAL_ERROR"
id: -c-r-i-t-i-c-a-l_-e-r-r-o-r
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log-type/-c-r-i-t-i-c-a-l_-e-r-r-o-r"
---
# CRITICAL_ERROR

CRITICAL_ERRORCritical SDK errors.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log-type/-e-r-r-o-r/index.html

---
layout: mobile_sdk
title: "ERROR"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "ERROR"
id: -e-r-r-o-r
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log-type/-e-r-r-o-r"
---
# ERROR

ERRORSDK Errors.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log-type/-e-v-e-n-t/index.html

---
layout: mobile_sdk
title: "EVENT"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "EVENT"
id: -e-v-e-n-t
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log-type/-e-v-e-n-t"
---
# EVENT

EVENTEvent messages.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log-type/-i-n-f-o/index.html

---
layout: mobile_sdk
title: "INFO"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "INFO"
id: -i-n-f-o
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log-type/-i-n-f-o"
---
# INFO

INFOInformational messages.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log-type/-w-a-r-n-i-n-g/index.html

---
layout: mobile_sdk
title: "WARNING"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "WARNING"
id: -w-a-r-n-i-n-g
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log-type/-w-a-r-n-i-n-g"
---
# WARNING

WARNINGWarning messages.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log-type/entries.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log-type"
---
# entries

val entries: EnumEntries<MTLogType>Returns a representation of an immutable list of all enum entries, in the order they're declared.This method may be used to iterate over the enum entries.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log-type/index.html

---
layout: mobile_sdk
title: "MTLogType"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTLogType"
id: -m-t-log-type
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log-type"
---
# MTLogType

enum MTLogType : Enum<MTLogType> Type of log messages in the SDK.

MembersEntries

## Entries

INFO

INFOInformational messages.

WARNING

WARNINGWarning messages.

ERROR

ERRORSDK Errors.

CRITICAL_ERROR

CRITICAL_ERRORCritical SDK errors.

EVENT

EVENTEvent messages.

## Properties

entries

val entries: EnumEntries<MTLogType>Returns a representation of an immutable list of all enum entries, in the order they're declared.

name

val name: String

ordinal

val ordinal: Int

## Functions

valueOf

fun valueOf(value: String): MTLogTypeReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

values

fun values(): Array<MTLogType>Returns an array containing the constants of this enum type, in the order they're declared.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log-type/value-of.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log-type"
---
# valueOf

fun valueOf(value: String): MTLogTypeReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
#### Throws

IllegalArgumentExceptionif this enum type has no constant with the specified name

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log-type/values.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-log-type"
---
# values

fun values(): Array<MTLogType>Returns an array containing the constants of this enum type, in the order they're declared.This method may be used to iterate over the constants.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-loggable/index.html

---
layout: mobile_sdk
title: "MTLoggable"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTLoggable"
id: -m-t-loggable
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-loggable"
---
# MTLoggable

interface MTLoggableProtocol requirement for all Logger objects.
#### Inheritors

OSLogger

Members

## Functions

log

abstract fun log(message: String, type: MTLogType)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-loggable/log.html

---
layout: mobile_sdk
title: "log"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "log"
id: log
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-loggable"
---
# log

abstract fun log(message: String, type: MTLogType)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-logger/-i-n-f-o_-m-a-r-k-e-r.html

---
layout: mobile_sdk
title: "INFO_MARKER"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "INFO_MARKER"
id: -i-n-f-o_-m-a-r-k-e-r
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-logger"
---
# INFO_MARKER

const val INFO_MARKER: StringLog marker for information messages.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-logger/index.html

---
layout: mobile_sdk
title: "MTLogger"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTLogger"
id: -m-t-logger
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-logger"
---
# MTLogger

object MTLoggerLogger class used for SDK logs.

Members

## Properties

INFO_MARKER

const val INFO_MARKER: StringLog marker for information messages.

## Functions

log

fun log(message: String, type: MTLogType)Adds a log.

printLogs

fun printLogs()Prints all current logs to the console.

setCustomLogger

fun setCustomLogger(logger: MTLoggable)Injects a custom logger conforming to the MTLoggable protocol.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-logger/log.html

---
layout: mobile_sdk
title: "log"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "log"
id: log
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-logger"
---
# log

fun log(message: String, type: MTLogType)Adds a log.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-logger/print-logs.html

---
layout: mobile_sdk
title: "printLogs"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "printLogs"
id: print-logs
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-logger"
---
# printLogs

fun printLogs()Prints all current logs to the console.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-logger/set-custom-logger.html

---
layout: mobile_sdk
title: "setCustomLogger"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setCustomLogger"
id: set-custom-logger
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-m-t-logger"
---
# setCustomLogger

fun setCustomLogger(logger: MTLoggable)Injects a custom logger conforming to the MTLoggable protocol.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-o-s-logger/-o-s-logger.html

---
layout: mobile_sdk
title: "OSLogger"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "OSLogger"
id: -o-s-logger
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-o-s-logger"
---
# OSLogger

constructor()

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-o-s-logger/index.html

---
layout: mobile_sdk
title: "OSLogger"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "OSLogger"
id: -o-s-logger
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-o-s-logger"
---
# OSLogger

class OSLogger : MTLoggable

Members

## Constructors

OSLogger

constructor()

## Functions

log

open override fun log(message: String, type: MTLogType)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-o-s-logger/log.html

---
layout: mobile_sdk
title: "log"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "log"
id: log
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.logging/-o-s-logger"
---
# log

open override fun log(message: String, type: MTLogType)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.logging/index.html

---
layout: mobile_sdk
title: "com.maptiler.maptilersdk.logging"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "com.maptiler.maptilersdk.logging"
id: com.maptiler.maptilersdk.logging
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.logging"
---
# com.maptiler.maptilersdk.logging

Types

## Types

MTLog

data class MTLog(val message: String, val type: MTLogType)Log object used with MTLogger.

MTLoggable

interface MTLoggableProtocol requirement for all Logger objects.

MTLogger

object MTLoggerLogger class used for SDK logs.

MTLogLevel

sealed class MTLogLevelSDK log level.

MTLogType

enum MTLogType : Enum<MTLogType> Type of log messages in the SDK.

OSLogger

class OSLogger : MTLoggable

---

