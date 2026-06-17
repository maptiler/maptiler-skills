# Source: https://docs.maptiler.com/engine/license-activation/

# License activation

## [Software activation online](#software-activation-online)

After a purchase of the software, when you receive your license key, it is necessary to activate MapTiler Engine. After activation, the demo version no longer enforces the “MapTiler DEMO” overlays.

To perform the online activation, use the following command:

##### [-activate [YOUR-OWN-LICENSE-KEY]](#-activate-your-own-license-key)
Activates MapTiler Engine with a proper license key. You can get your [license key online here](https://www.maptiler.com/pricing/).

Example:

``` bash
  maptiler-engine -activate YOUR-OWN-LICENSE-KEY
```

**In case you require to reinstall the computer, use the** `-deactivate` **command to be able to re-activate the license later on.**

The software activation for MapTiler Engine Pro via GUI [is described here](https://support.maptiler.com/i56-license-activation).

### [Software activation in a virtual machine](#software-activation-in-a-virtual-machine)

The activation process for MapTiler Engine running in a virtual machine requires online activation only via environment variable `MAPTILER_LICENSE`. The software will be automatically deactivated in the end.

The `MAPTILER_LICENSE` environment variable needs to be set before calling MapTiler Engine. There are two ways to do so. The first (and recommended) way is to add the `MAPTILER_LICENSE` variable to the system environment variables list. Then, you can call MapTiler Engine directly, like:

``` bash
  maptiler-engine ...
```

Alternatively, when you are calling MapTiler Engine from a script, or using it manually in a command line session, you need to set the `MAPTILER_LICENSE` environment variable before calling MapTiler Engine:

**Example on Windows OS (in command prompt)**

``` bash
  set MAPTILER_LICENSE=YOUR-OWN-LICENSE-KEY
  maptiler-engine ...
```
**Example on Windows OS (in Powershell)**

``` bash
  set $env:MAPTILER_LICENSE = 'YOUR-OWN-LICENSE ...
```


**Example on Linux / macOS**

``` bash
  export MAPTILER_LICENSE=YOUR-OWN-LICENSE-KEY
  maptiler-engine ...
```

**Notice:** This activation process via environment variable requires a **not-activated MapTiler Engine** instance on that computer! Starting MapTiler Engine application without setting this environment variable `MAPTILER_LICENSE`, you should see either **MapTiler Engine Pro Demo**, or **Your trial period has expired** error message.

You can also run MapTiler Engine in Docker. To learn more, please refer to [this documentation article](/guides/map-tiling-hosting/data-processing/maptiler-engine-in-docker).

## [Software deactivation online](#software-deactivation-online)

You can deactivate MapTiler Engine via command line, in order to transfer the application to another computer. Note that after the deactivation, MapTiler Engine will continue to run in DEMO mode, but the trial period of 14 days will **NOT** start again.

To do the online deactivation, use the following command:

##### [-deactivate](#-deactivate)
Deactivates activated MapTiler Engine software. MapTiler Engine can be used in Demo mode, if trial period has not expired.

Example:

``` bash
  maptiler-engine -deactivate
```

You can deactivate MapTiler Engine Pro [in GUI via License dialog described here](https://support.maptiler.com/i449-license-deactivation).

## [Demo trial extension](#demo-trial-extension)

The demo version of MapTiler Engine Pro is fully usable for 14 days after the first start. In case this trial period for testing the software before purchase expires and you would like to continue to test the demo, it is necessary to submit a request for a trial extension. The process for the GUI application is described [in this support article](/guides/map-tiling-hosting/data-processing/how-to-activate-trial-period-in-maptiler-engine). 

If you're running MapTiler Engine on a headless machine, you'll need to generate a report with the `maptiler-engine -report` command, save the output, and include it in a [request sent to the MapTiler Support](/support/requests/). 

## [License information](#license-information)

To check your license information, use the following command:

##### [-license](#-license)
Prints your license information for activated MapTiler Engine.

Example

``` bash
  > maptiler-engine -license
  License key: <your license key>
  License email: <your email>
  Subscribed plan: <your plan, with <your payment option> payment
  License active until <date>, X days remaining.
  Purchased CPU cores: 4
  Logical CPU cores: 4 available
```

This argument may print additional texts, depending on your License, for example:

``` bash
  Activated offline, please use -deactivate_request command in order to deactivate your license.
```
