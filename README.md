# MATLAB Engine container for Python

This repository contains an Apptainer recipe for containers with MATLAB, Python, and the Python bindings for the MATLAB Engine.

Its intended use-case is to provide a base image that other containers are built on (bootstrapping).

The reason for its existence is that currently there is no easy way to interact with a MATLAB instance inside a container from outside the container.

## Build

To build, you must provide a compatible MATLAB release, Python version, and matlabengine version.
For example, `r2023b`, `3.11.7`, `23.2.1`.
For compatible versions, check `/versions.csv`.
The build will fail with an error if the versions are not compatible.

You can also specify additional MATLAB Toolboxes, as a string of comma separated values, such as `"Signal_Processing_Toolbox,Robotics_System_Toolbox"`.

```
apptainer build \
 --build-arg MATLAB_RELEASE=<matlab_release> \
 --build-arg TOOLBOXES=<toolboxes> \
 --build-arg PYTHON_VERSION=<python_version> \
 --build-arg MATLABENGINE_VERSION=<matlabengine_version> \
  engine_container.sif engine_container.def 
```

## Run

To run, you must bind a MATLAB license to the container and set the `MLM_LICENSE_FILE` environment variable to its location.

```
$> apptainer exec --bind </path/to/licensefile>:/matlab.lic --env MLM_LICENSE_FILE=/matlab.lic engine_container.sif /bin/bash
Apptainer> python
...
>>> import matlab.engine
>>> eng = matlab.engine.start_matlab("-nodisplay")
>>> eng.eval("version", nargout=1)
'9.11.0.2358333 (R2021b) Update 7'
```

## Using as a bootstrap image
TODO