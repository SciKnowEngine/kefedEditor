# Introduction #

The KEfED Editor is a software component to aid in the design of experimental protocols, with an emphasis o n the data flow.  That provides an organizing principle that we exploit for constructing a data management tool.

The KEfED model is work is designed to provide a lightweight representation for scientific knowledge that is (a) generalizable, (b) a suitable target for text-mining approaches, (c) relatively semantically simple, and (d) is based on the way that scientist plan experiments and should therefore be intuitively understandable to non-computational bench scientists.

# Implementation #

We have the initial implementation of this component.  This is deployed as a rich internet application based on a web server.  It includes the following parts.
  * The KEfED editor itself, a flash-based graphical user interface that allows the creation of KEfED models of experimental designs, the generation of data entry forms for adding data based on those designs and the entry of data.
  * A backend storage system for storing experimental designs and also for storing the data associated with those designs.  Currently this is handled by a [Persevere DB](http://www.persvr.org/) but this will change to a different technology in a subsequent release.
  * A reasoning engine based on PowerLoom with an implementation of reasoning for NeuralConnectivity based on TractTracing data.
  * A variety of export formats will be supported.  Currently we have an ability to export to PowerLoom and have an OWL exporter under development.

# Releases #

We currently have two release packages.
  * One is a fully self-contained application server, based on Jetty.  This is available as a set of three platform specific installers.  Each one will install a full self-contained server.
  * The second is a set of `*.war` files for the KEfED editor, persevere database and NeuralConnectivity reasoner.

These are suitable for use in an existing web server such as Tomcat or Jetty.

See the [Downloads](https://code.google.com/p/bioscholar/downloads/list) link.

# System Requirements #

The KEfED Editor is based on an [Adobe Flex](http://www.Adobe.com/Flex) client.  This requires a web browser with the [Adobe Flash](http://www.adobe.com/products/flashplayer/) player, version 10 or greater.

The standalone server requires a Java 1.6 implementation.

The existing server files require a web server such as [Apache Tomcat](http://tomcat.apache.org/) or [Jetty](http://sourceforge.net/projects/jetty) that can deploy `*.war` files.  The content of the war files effectively requires the use of Java for proper operation.

# External Components #

We use the following external libraries in the KEfED Editor.
  * The [Kapit Diagrammer](http://lab.kapit.fr/display/diagrammer/Diagrammer) graphic library from [KapLab](http://lab.kapit.fr/) under their [Community License](http://lab.kapit.fr/display/Store/Free+License).
  * The [Prefuse Flare](http://flare.prefuse.org/) graph manipulation and visualization library from the [UC Berkeley Visualization Lab](http://vis.berkeley.edu/) under the [BSD License](http://flare.prefuse.org/license-flare.txt)

We use the following external code in the BioScholar server:
  * The [Jetty](http://jetty.codehaus.org/jetty/) web server, licensed under the [Apache license](http://www.eclipse.org/jetty/licenses.php).