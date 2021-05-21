\ifndef{simulationSystem}
\define{simulationSystem}

\editme

\subsection{Simulation System}

\notes{An example of a complex decision making system might be a climate model, in such a system there are separate models for the atmospher, the ocean and the land.

The components of any of these system include: flowing of currents, chemical interactions in the upper atmospher, evaporation of water etc.}

\figure{\includejpg{\diagramsDir/simulation/carbon_cycle}{60%}}{Representation of the Carbon Cycle from the US National Oceanic and Atmospheric Administration. While everything is interconnected in the system, we can decompose into separate models for atmosphere, ocean, land.}{carbon-cycle-noaa}

\notes{The influence of human activity also needs to be incorporated and modelled so we can make judgments about how to mitigate the effects of global warming.}

\newslide{}

\figure{\includediagram{\diagramsDir/simulation/simulation-schematic}{40%}}{The components of a simulation system for climate modelling. *Diagram from US National Oceanic and Atmospheric Administration*}{simulation-system-components}

\subsection{Monolithic System}

\notes{The classical approach to building these systems was a 'monolithic system'. Built in a similar way to the successful applicaitons software such as Excel or Word, or large operating systems, a single code base was constructed. The complexity of such code bases run to many lines. 

In practice, shared dynamically linked libraries may be used for aspects such as user interface, or networking, but the software often has many millions of lines of code. For example, the Microsoft Office suite is said to contain over 30 millions of lines of code.}

\figure{\includediagram{\diagramsDir/simulation/ml-system-monolith-simulation}{60%}}{A potential path of models in a machine learning system.}{ml-system-monolith-simulation}

\includes{_software/includes/separation-of-concerns.md}


\subsection{Service Oriented Architecture}

\notes{Such software is not only difficult to develop, it is difficult to scale when computation demands increase. For example, Amazon's original website software (called Obidos) was a [monolithic design](https://en.wikipedia.org/wiki/Obidos_(software)) but by the early noughties it was becoming difficult to sustain and maintain. The software was phased out in 2006 to be replaced by a modularized software known as a 'service oriented architecture'. 

In Service Oriented Architecture, or "Software as a Service" the idea is that code bases are modularized and communicate with one another using network requests. A standard approach is to use a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). So, rather than a single monolithic code base, the code is developed with individual services that handle the different requests.}

\notes{The simulation software is turned inside out to expose the individual components to the operator.}


\figure{\includediagram{\diagramsDir/simulation/ml-system-downstream-simulation000}{60%}}{A potential path of models in a machine learning system.}{ml-system-downstream-simulation}

\notes{This is the landscape we now find ourselves in with regard to software development. In practice, each of these services is often 'owned' and maintained by an individual team. The team is judged by the quality of their service provision. They work to detailed specifications on what their service should output, what its availability should be and other objectives like speed of response. This allows for conditional independence between teams and for faster development.}

\notes{One question is to what extent is the same approach possible/desirable for scientific models? In reality, the components we listed above are already separated and often run independently. But those components themselves are made up of other sub-components that could also be exposed in a similar manner to software-as-a-service, giving us the notion of "simulation as a service".}


\endif
