\ifndef{centrifugalGovernor}
\define{centrifugalGovernor}
\editme

\notes{\subsection{The Centrifugal Governor}}

\include{_ai/includes/holborn-science-centrifugal-governor.md}
\include{_ai/includes/watt-steam-engine.md}

\notes{The centrifugal governor was made famous by Boulton and Watt when it was deployed in the steam engine. Studying stability in the governor is the main subject of James Clerk Maxwell's paper on the theoretical analysis of governors [@Maxwell:governors1867]. This paper is a founding paper of control theory. In an acknowledgment of its influence, Wiener used the name [*cybernetics*](https://en.wikipedia.org/wiki/Cybernetics) to describe the field of control and communication in animals and the machine [@Wiener:cybernetics48]. Cybernetics is the Greek word for governor, which comes from the latin for helmsman.}

\notes{A governor is one of the simplest artificial intelligence systems. It senses the speed of an engine, and acts to change the position of the valve on the engine to slow it down.}

\notes{Although it's a mechanical system a governor can be seen as automating a role that a human would have traditionally played. It is an early example of artificial intelligence.}

\notes{The centrifugal governor has several parameters, the weight of the balls used, the length of the linkages and the limits on the balls movement.}

\notes{Two principle differences exist between the centrifugal governor and artificial intelligence systems of today.

1. The centrifugal governor is a physical system and it is an integral part of a wider physical system that it regulates (the engine).
2. The parameters of the governor were set by hand, our modern artificial intelligence systems have their parameters set by *data*.
}

\newslide{}

\figure{\includepng{\diagramsDir/Centrifugal_governor}{70%}{negate}}{The centrifugal governor, an early example of a decision making system. The parameters of the governor include the lengths of the linkages (which effect how far the throttle opens in response to movement in the balls), the weight of the balls (which effects inertia) and the limits of to which the balls can rise.}{centrifugal-governor}


\notes{This has the basic components of sense and act that we expect in an intelligent system, and this system saved the need for a human operator to manually adjust the system in the case of overspeed. Overspeed has the potential to destroy an engine, so the governor operates as a safety device.

The first wave of automation did bring about sabotoage as a worker's response. But if machinery was sabotaged, for example, if the linkage between sensor (the spinning balls) and action (the valve closure) was broken, this would be obvious to the engine operator at start up time. The machine could be repaired before operation.}


\endif
