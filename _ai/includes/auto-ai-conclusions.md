\ifndef{dataOrientedConclusions}
\define{dataOrientedConclusions}

\editme

\subsection{Conclusion}
\slides{
* Paradigm shift for computer science.
* Want to study deployed interacting ML systems.
* Need to put the *data flows* at the heart, not models or services.
* Need expertise in 
   * Security, Programming languages, Systems
* Implications for Hardware and network design
}
\notes{Data oriented programming offers a set of development methodologies which ensure that the system designer considers what decisions are required, how they will be made, and critically, declares this within the system architecture.

This allows for monitoring of *data quality*, *fairness*, *model accuracy* and opens the door to a more sophisticated form of auto ML where full redployments of models are considered while analyzing the information dynamics of a complex automated decision-making system.

To deploy these ideas we need expertise from the programming language community for specifying and compiling the interaction of data flows to infer the roles of the services/models. The systems community for maintaining the ecosystem of data flows (likely streaming systems). The security community for managing permissions in these systems. 

There are implications for the hardware and networking communities, because if we can standardise around the specification of a modern data-oriented programming we should expect to be able to compile it to different system architectures at the hardware level (e.g. edge vs cloud computing, TPUs vs GPUs vs CPUs for handign loads etc).
}

\endif
