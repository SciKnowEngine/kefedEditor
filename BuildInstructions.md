# Build Instructions #

Instructions for building BioScholar from source code.

The source code is divided into three sections.
  * **editor** This is the main BioScholar application code.  It runs the interface and communicates with the external resources.  Generates the code which goes into the `blazeds.war` file
  * **reasoning** This is the specialized PowerLoom code that performs the reasoning task to interpret tract-tracing experiments.  Includes the knowledge bases (KBs) for the reasoning part of the system.  Generates the code which goes into the `ploom.war` file.
  * **server** This is the stand alone server code that uses the Jetty web server.

The source files include `ant` scripts for compiling and building the code.

## The editor subsystem ##

Code is in `editor`

The editor subsystem builds an Adobe Flash based interface.  The code is compiled using the [Flex 3.5 SDK](http://opensource.adobe.com/wiki/display/flexsdk/Download+Flex+3), which must be installed and a system variable named `FLEX_HOME` be configured to point to that installation location.

The file `configuration-sample.xml` must be copied to `configuration.xml`.  (The `configuration.xml` file is not being kept under `svn` control so that any local modifications will not be overwritten when updating the sources.)

**Requires**: Flex 3.5 SDK, ant

The `ant` build file supports the following targets:
  * compile     - compiles the entire set of applications
  * compile-app - compile a single app specified by APP parameter (BioScholar)
  * war         - generate blazeds.war file with all applications
  * dist        - compile files and generate a war (DEFAULT)
  * doc         - generate ASDOC files
  * clean       - remove all compiled files, war file and generated documentation

## The reasoning subsystem ##

Code is in `reasoning/neuralconnectivity`

The reasoning subsystem uses [PowerLoom](http://www.isi.edu/isd/LOOM/PowerLoom) as its reasoning engine.  The source code is configured to build a PowerLoom web service with a set of knowledge bases that will perform the connection reasoning for [tract-tracing experiments](https://wiki.birncommunity.org:8443/display/NEWBIRNCC/KEfED+Neural+Connectivity+and+Tract-Tracing+Experiments).

**Requires**: `ant`

The `ant` build file supports the following targets:
  * dist        - compile files and generate a war (DEFAULT)
  * clean       - remove all compiled files, war file and generated documentation

## The server subsystem ##

Code is in `server`

This is a very simple system that has a small Java class that implements an embedded server and deploys war files that are in a particular directory.  The build script will construct the application.

**Requires**: A Java 1.6 development environment, ant and  [Launch4J](http://launch4j.sourceforge.net/).

Also included is a patch for persevere version 0.9.25 that will allow this to run in situations where there is a space in the directory name (mainly Windows) or where a plus sign appears in generated temporary directory names (mainly MacOS).

**External Software**:  Uses  [Launch4J](http://launch4j.sourceforge.net/) to build windows executables, [JarBundler](http://informagen.com/JarBundler/) to build MacOS executables, and [izPack](http://izpack.org/) to create the installer programs.

A full build of the stand-alone application and installers requires that [Launch4J](http://launch4j.sourceforge.net/) be installed and a system variable named `LAUNCH4J_HOME` be configured to point to that installation location.  !izPack and JarBundler are self-contained in the source code repository.

The `ant` build file supports the following targets:
  * compile     - compiles the basic Java server.
  * app         - generate executables for Linux, MacOS and Windows
  * dist        - compile files, generate executables and builds distribution directories.
  * doc         - generate javadoc files for server
  * installer   - dist and doc and generates installers for the distributions (DEFAULT)
  * clean       - remove all compiled files, war file and generated documentation

## Persevere configuration ##

BioScholar version 1.0 uses the Persevere 0.9.25 database storage system.

The Persevere system will require only minimal configuration.  It will be necessary to create tables in persevere to handle and store the KEfED model designs and data.  By default these tables are called `KefedModel` and `KefedExperiment`, but other names can be used.  If other names are used, then the configuration file for the editor subsystem will need to be modified to reflect the differences.