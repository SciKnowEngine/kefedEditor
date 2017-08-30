# KEfED Editor
This was the original `BioScholar` web application, described in 
[Russ et al. 2011](http://www.biomedcentral.com/1471-2105/12/351).

_Note:_ This system has been trimmed down from the version described in the BMC Bioinformatics paper. We have removed the Server and Reasoning components and focussed on developing this as an intermediary system, designed to operate within the `kefed.io` architecture. 
This is now a maven project using FlexMojos to permit the code to be built easily from the command line. 

This version of the KefedEditor will only run as a componenet part of the kefed.io system (since it requires the server-side interactions with the embedded ElasticSearch server of that system). 

Thus, this is now legacy code and will be maintained as long as we need to use the Flex system in `kefed.io`. 

[kefed.io](https://github.com/SciKnowEngine/kefed.io) will be our desired platform going forward, which is based on Javascript components only (mxGraph and polymer). 

This KefedEditor implementation is designed to be built and copied to the `kefed.io/src/main/webapp/kefed/v1` subdirectory and then you should point your browser at `http://servername:8080/v1/KefedEditor.html` to use the system as is.  
