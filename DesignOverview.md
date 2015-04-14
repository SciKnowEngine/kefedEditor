# BioScholar Design #

BioScholar is designed using a client-server architecture.  User interaction is via a graphical interface running in a web browser using Adobe Flash.  This interface communicates with a web server that also provides access to backend storage, a reasoning engine, an ontology search service and the PubMed publication database.

![http://bioscholar.googlecode.com/svn/wiki/images/kefed-block-diagram.png](http://bioscholar.googlecode.com/svn/wiki/images/kefed-block-diagram.png)

## External Components ##

  * [Persevere storage engine](http://www.persvr.org/Page/Persevere).  Used to store experiment designs and data.
  * [PowerLoom reasoning engine](http://www.isi.edu/isd/LOOM/PowerLoom/).  Used to support specific interpretations of data.  This requires a customized interface and domain model.
  * [BAMS](http://brancusi.usc.edu/bkms/). Source of the brain atlas information used for reasoning by the PowerLoom system.  Primarily used for part-of reasoning over brain regions.
  * [NCBO BioPortal](http://bioportal.bioontology.org/). Used for looking up ontology terms for annotation of experimental design model elements.
  * [PubMed](http://www.ncbi.nlm.nih.gov/pubmed/).  Used to provide access to publication information and abstracts from the interpretation of data in specialized interfaces.
  * [Kapit Diagrammer](http://lab.kapit.fr/display/kalileo/Diagrammer+v1+Developer+Guide).  Provides the graphical library for drawing and interacting with experimental designs.
  * [Prefuse Flare](http://flare.prefuse.org/). Graph library for analyzing the experimental design graphs to compute variable dependencies.
  * [Jetty Web Server](http://jetty.codehaus.org/jetty/). Provides the embedded stand alone web server for the BioScholar server.
  * [JGoodies Forms](http://www.jgoodies.com/freeware/forms/). Layout of the stand alone server interface.

## Additional Tools ##

Additional tools are used by BioScholar to build and package the releases.  Those tools are:
  * [Adobe Flex 3.5 SDK](http://opensource.adobe.com/wiki/display/flexsdk/Download+Flex+3) used to compile the main Flex interface for BioScholar.
  * [Launch4J](http://launch4j.sourceforge.net/) to build windows executables.
  * [JarBundler](http://informagen.com/JarBundler/) to build MacOS executables.
  * [izPack](http://izpack.org/) to create installer programs.