# Source: https://docs.maptiler.com/engine/installation/

# Installation

MapTiler Engine command line utility comes as part of [MapTiler Engine](https://www.maptiler.com/engine/){:target="_blank" rel="noopener"} product and it is available from the **Pro** subscription plan as *maptiler-engine*.

## [Windows](#windows)

Get the installation package from the [MapTiler Engine download page](https://www.maptiler.com/engine/download/){:target="_blank" rel="noopener"} and start the installation wizard. Once it's finished, run MapTiler Engine from the standard Command Prompt application in Windows:

``` bash
> maptiler-engine
```

### Silent install

To install MapTiler Engine on Windows workstations remotely without the end users' interaction, use the `VERYSILENT` argument in CLI. The installation **requires admin rights**. 

``` bash
> <path_to_the_installer_exe> /VERYSILENT
```

By default, MapTiler Engine gets installed to **C:\Program Files**. If you need to change the location, use the `DIR` argument: 

``` bash
> <path_to_the_installer_exe> /VERYSILENT /DIR=<path_to_custom_installation_directory>
```

Note that even though the installation itself is silent, the end user might [get a prompt to set firewall rules](/guides/map-tiling-hosting/data-processing/installation-on-windows/#windows-firewall) when they run MapTiler Engine for the first time.

## [macOS](#macos)

Get the installation disk image (DMG) from the [MapTiler Engine download page](https://www.maptiler.com/engine/download/){:target="_blank" rel="noopener"}. Open the disk image in macOS and drag the "MapTiler Engine Pro" icon into your "Application" folder. The command line interface can be started from Terminal application:

``` bash
$  /Applications/MapTiler Engine.app/Contents/MacOS/maptiler-engine
```

All versions of macOS higher than 10.12 (Sierra) are supported.

## [Linux](#linux)

Get the installation package from the [MapTiler Engine download page](https://www.maptiler.com/engine/download/){:target="_blank" rel="noopener"}. We provide a DEB package for Debian-based Linux distributions (Ubuntu, Debian) and RPM package for RedHat-based distributions (Fedora, CentOS). Then run the installation:

- For DEB packages, use: `sudo dpkg -i maptiler-engine-x.x.x-app-linux.deb` 
- For RPM packages, use: `sudo rpm -i maptiler-engine-x.x.x-app-linux.rpm`
	
The command line utility gets installed in the standard binary location `/usr/bin/`. To start it, run:

``` bash
$ maptiler-engine
```

Another option for running the latest MapTiler Engine on any Linux distribution is via the [Docker container](https://hub.docker.com/r/maptiler/engine/).


