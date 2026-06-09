# Source: https://docs.maptiler.com/engine/getting-started/

# Getting started

The main purpose of the software is to generate tiles in a defined tiling system, given some options and inputs. The only mandatory option is -o for the output directory. This directory must not exist yet when you run MapTiler Engine, to avoid overwriting existing data by mistake. As input, you can just provide the source dataset filename(s)[^1].

``` bash
  maptiler-engine -o output_directory input_file.ext
```

an example:

``` bash
  maptiler-engine -o tiles map.tif
```

To render more files at once, just specify them one after another:

``` bash  
  maptiler-engine -o output_directory input1.tif input2.tif input3.tif
```

If you start the maptiler-engine without arguments or with -help option, it will print all available commands:

``` bash
  maptiler-engine -help
```

## [Command Structure](#command-structure)



The global options apply to all input files, in other words:

**Only arguments specified BEFORE the input filenames are applied to all files!**

Arguments which should be applied only to a single file are specified AFTER the name of such file (for example zoom level range specific only
to that file) and has higher priority than the global options.

## [Setting CPU limits](#setting-cpu-limits)

MapTiler Engine is a multi-threaded program. By default, it will use all the CPUs you have and print the information about the cores. You can also set a limit on the defined number of cores yourself with the `-P` option.

##### [-P [num]](#-p-num)
Set number of CPU cores to be used for render process.

Example:

``` bash
  maptiler-engine -P 4 ...
```

This is especially practical to evaluate the demo application before purchasing a license for a particular number of cores.

The modern CPUs has multiple cores and support of Hyperthreading - which provides multiple logical CPUs per core. This way MapTiler Engine can provide higher performance with `-P` 4 even on a dual-core computer.

[^1]: Depending on your operating system you may need to call the command differently than just maptiler-engine, typically on Linux and Mac in the actual directory as ./maptiler-engine and on Windows as maptiler-engine.exe.
