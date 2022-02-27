\ifndef{dataOrientedArchitecturesShort}
\define{dataOrientedArchitecturesShort}

\editme

\subsection{Data-oriented Architectures}

\notes{Data-oriented architectures aim to address
the rat's nest that is the current interaction between the services in a
service-oriented architecture. It does this by introducing data-oriented
programming. The data-oriented programming language tracks the movement
of data between each service.

Service-oriented programming style is a necessary, but not sufficient
approach to data-oriented programming. Data-oriented programming is not
only about the individual services, but how they are connected. Which
service is calling which and where the flow of the data through the
system occurs?

If each service has its inputs and outputs declared on a wider
ecosystem, then we can programmatically determine which inputs effect
which decisions. This programmatic discovery is vital because as systems
are built compositionally, the actual inputs that affect a final
decision may not be known to any of the software engineers who are
maintaining the system\ifdef{lancelot} (except perhaps Lancelot)\endif.}

talk-macros.gpp}ata-science/includes/milan.md}

\endif
