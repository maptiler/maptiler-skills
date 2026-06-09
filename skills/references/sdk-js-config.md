# Source: https://docs.maptiler.com/sdk-js/api/config/

# 

  
    
    [ src/config.ts](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/config.ts)
  

  The `config` object represents the SDK global settings.
  It exposes properties and options that make it easier to define some values that the SDK will use globally,
  such as the API key, the map units, etc.

Extends [Evented](/sdk-js/api/events/#evented).

Example

  ```
``
```

## [Properties](#properties)

  
| Gets and sets the [MapTiler API key](https://cloud.maptiler.com/account/keys/).           Emits the `apiKey` event when updated. |
| Setting on whether of not the SDK runs with a session logic.             A **"session"** is started at the initialization of the SDK and finished when the browser page             is being refreshed.             When session is enabled, the extra URL param mtsid is added to queries on the MapTiler API.             This allows MapTiler to enable **"session based billing"**. |
| Gets and sets the map units.             When updated, it emits the `unit` event that is caught inside of the             map instances.             Example: to update the scale control |
| Sets the map primary language, use when a Map instance is created.             (default: the language of the web browser is used) |
| Gets and sets a the custom fetch function to replace the default one.             If the `fetch()` function exists (browser or Node >= 18) then it will             be resolved automatically.             A custom `fetch()` function can be provided for early Node versions             (Node |
| The telemetry is very valuable to the team at MapTiler because it shares information              about where to add the extra effort.              It also helps spotting some incompatibility issues that may arise between the SDK              and a specific version of a module.                                   It consists in sending metrics about usage of the following features:                            SDK version [string]               API key [string]               MapTiler sesion ID (if opted-in) [string]               if tile caching is enabled [boolean]               if language specified at initialization [boolean]               if terrain is activated at initialization [boolean]               if globe projection is activated at initialization [boolean]                          In addition, each official module will be added to a list, alongside its version number.                                   Telemetry is enabled by default but can be opted-out by setting to `false`.             ``` `` ``` |
