# Introduction #

The goal of the BioScholar project is to provide software for experimental biomedical scientists that would permit a single scientific worker (at the level of a graduate student or postdoctoral worker) to design, construct and manage a shared knowledge repository for a research group derived from a local store of PDF files.  In addition, the project aims to support the curation of data from scientific experiments conducted within such a research group.   We especially emphasize usability within a laboratory so that this software could provide support to experimental scientists attempting to construct a personalized representation of their own knowledge on a medium scale.

## The Software ##

A more general overview of BioScholar can be found at the home page http://www.bioscholar.org.  This site is directed at software distribution and installation issues.  Here you can find

  * A brief DesignOverview
  * InstallationInstructions
  * BuildInstructions

## Distributions ##

We provide software distributions in three forms:
  1. An installer for a stand-alone web server using Jetty.  The installer will install a full web server based on Jetty with a simple control panel for starting the BioScholar system.
  1. A set of `*.war` files suitable for installation in an existing web server such as [Jetty](http://jetty.codehaus.org/jetty) or [Tomcat](http://tomcat.apache.org/).
  1. The source download for the client and the server.  This will allow you to build the system from the original source files.

## System Requirements ##

  * **Standalone Server:**  The standalone server code requires Java 1.6 or higher to run.  We recommend a machine with 1GB or RAM or more.
  * **War Files:** The war file code requires the use of an existing web server that is able to deploy `*.war` files.  Some examples are [Jetty](http://jetty.codehaus.org/jetty/) and [Tomcat](http://tomcat.apache.org/).
  * **Client:**  The client requires a web browser with [Adobe(R) Flash(R) version 10](http://get.adobe.com/flashplayer/) or higher.

## Acknowledgements ##

BioScholar  is funded under [National Institutes of Health (NIH)](http://www.nih.gov) grant RO1-GM083871.  Additional work on the software was supported by NIH grant RO1-MH079068-01A2 and a [Michael J. Fox Foundation](http://www.michaeljfox.org/) grant .