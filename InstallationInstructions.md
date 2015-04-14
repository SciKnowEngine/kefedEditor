# Installation Instructions #

There are three distributions of the BioScholar code.
  1. A stand-alone web server using Jetty.
  1. A set of `*.war` files suitable for installation in an existing web server.
  1. Source code.
Installation instructions for each option are given below.

## Stand-alone Web Server ##

This is the simplest installation.  We provide installers for MacOS, Windows and Linux and generic Unix systems.  Download the appropriate installer.

### Installer Download ###

  * **MacOS:**  The download is a `zip` file which contains an installer application.  Depending on your browser settings, this `zip` file may expand automatically.  If it doesn't, double-clicking on it will cause it to expand.  The result will be a native Mac installer application that will guide you through the installation process.  Once installation is complete, the server can be started.  **Note:** The installer will not be able to install over an existing installation.

  * **Windows:** The download is a runnable installer application.  Double-clicking on the file will launch the installer.  There may be a dialog indicating an "unknown publisher".  This is expected and should not cause alarm.  You can continue the installation.

  * **Linux, Unix, other:** The download is a jar file.  Install the software by running this jar file.  Run the file  either by double-clicking it (if supported by your operating system) or starting it  with
```
        java -jar install-BioScholarServer-1.0.jar
```


### Running the Server ###

Running the server is done by
  * **MacOS:** Running the native BioScholarServer application.
  * **Windows:** Running the native BioScholarServer.exe application.
  * **Linux, Unix:** Running the shell script run\_BioScholarServer

Once the server is installed, it can be started and will show a simple control panel.  This control panel will allow you to choose a port for running the server.  For most cases, the default port will work fine.  Once the server has completed startup (which can take a couple of minutes), a button will become active that will launch the default web browser and navigate it to the NeuralConnectivity application.

## War Files ##

The `*.war` file distribution contains three `war` files which are configured to work together in a single web server.  They require a web server that is able to use and deploy `*.war` files. These files will need to be installed in the appropriate location for the web server of your choice.  Notes on the installation for [Tomcat](http://tomcat.apache.org/) and [Jetty](http://jetty.codehaus.org/jetty/) follow.

### Tomcat ###

Place the `*.war` files into the Tomcat server's `webapps` directory.  Depending on the settings on your Tomcat server, these will either automatically deploy or you may need to restart the server.  Once deployed, the main BioScholar application will be available at the path `blazeds/bioscholar/BioScholar.html` and the NeuralConnectivity application at the path `blazeds/bioscholar/NeuralConnectivity.html` on your web server.

### Jetty ###

You will need to configure Jetty to scan a directory for the `*.war` files and deploy them.  The instructions can be found in the Jetty documentation.

## Source Code ##

The source code can be downloaded from the source code repository.  There are three systems for which we provide code.   A full build will also require the installation of a [Persevere server](http://www.persvr.org/Page/Persevere).  We provide [ant](http://ant.apache.org/) scripts to automate the building of the system.  Once the source code is installed, see the BuildInstructions.  Building the system will require additional software and development kits to be installed.

The source code is divided into three sections.
  * **server** This is the stand alone server code that uses the Jetty web server.
  * **editor** This is the main BioScholar application code.  It runs the interface and communicates with the external resources.  Generates the code which goes into the `blazeds.war` file
  * **reasoning** This is the specialized PowerLoom code that performs the reasoning task to interpret tract-tracing experiments.  Includes the knowledge bases (KBs) for the reasoning part of the system.  Generates the code which goes into the `ploom.war` file.

The `persevere.war` file is provided as part of the war file distribution and is not built from source.