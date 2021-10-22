\ifndef{awsSoa}
\define{awsSoa}

\editme

\subsection{Monolithic System}

\notes{The classical approach to building these systems was a 'monolithic system'. Built in a similar way to the successful applications software such as Excel or Word, or large operating systems, a single code base was constructed. The complexity of such code bases run to many lines. 

In practice, shared dynamically linked libraries may be used for aspects such as user interface, or networking, but the software often has many millions of lines of code. For example, the Microsoft Office suite is said to contain over 30 million lines of code.}

\centerdiv{\charlieBellPicture{15%}\peterVosshallPicture{15%}}

\figure{\includediagram{\diagramsDir/ai/ml-system-monolith-purchasing}{60%}}{A potential path of models in a machine learning system.}{ml-system-monolith}

\notes{Such software is not only difficult to develop, but also to scale when computation demands increase. Amazon's original website software (called Obidos) was a [monolithic design](https://en.wikipedia.org/wiki/Obidos_(software)) but by the early noughties it was becoming difficult to sustain and maintain. The software was phased out in 2006 to be replaced by a modularized software known as a 'service-oriented architecture'.}

\includes{_software/includes/separation-of-concerns.md}

\subsection{Service Oriented Architecture}

\centerdiv{\charlieBellPicture{15%}\peterVosshallPicture{15%}}

\notes{In Service Oriented Architecture, or "Software as a Service" the idea is that code bases are modularized and communicate with one another using network requests. A standard approach is to use a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). So, rather than a single monolithic code base, the code is developed with individual services that handle the different requests.}

\figure{\includediagram{\diagramsDir/ai/ml-system-downstream-purchasing000}{60%}}{A potential path of models in a machine learning system.}{ml-system-downstream-purchasing}

\notes{Modern software development uses an approach known as *service-oriented architecture* to build highly complex systems. Such systems have similar emergent properties to Conway's "Game of Life". Understanding these emergent properties is vitally important when diagnosing problems in the system.}

\notes{In the context of machine learning and complex systems, Jonathan Zittrain has coined the term ["Intellectual Debt"](https://medium.com/berkman-klein-center/from-technical-debt-to-intellectual-debt-in-ai-e05ac56a502c) to describe the challenge of understanding what you've created.}


\endif
