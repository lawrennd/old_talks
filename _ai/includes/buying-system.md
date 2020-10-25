\ifndef{buyingSystem}
\define{buyingSystem}

\editme

\subsection{Buying System}

\notes{An example of a complex decision making system might be an automated buying system. In such a system, the idea is to match demand for products to supply of products.

The matching of demand and supply is a repetetive theme for decision making systems. Not only does it occur in automated buying, but also in the allocation of drivers to riders in a ride sharing system. Or in the allocation of compute resource to users in a cloud system. 

The components of any of these system include: predictions of the demand for the product, or the drivers or the compute. Then predictions of the supply. Decisions are then made for how much material to keep in stock, or how many drivers to have on the road, or how much computer capacity to have in your data centres. These decisions have cost implications. The optimal amount of product will depend on the cost of making it available. For a buying system this is the storage costs. 

Decisions are made on the basis of the supply and demand to make new orders, to encourage more drivers to come into the system or to build new data centers or rent more computational power.}

\figure{\includediagram{\diagramsDir/software/buying-schematic}{40%}}{The components of a putative automated buying system}{buying-system-components}

\subsection{Monolithic System}

\notes{The classical approach to building these systems was a 'monolithic system'. Built in a similar way to the successful applicaitons software such as Excel or Word, or large operating systems, a single code base was constructed. The complexity of such code bases run to many lines. 

In practice, shared dynamically linked libraries may be used for aspects such as user interface, or networking, but the software often has many millions of lines of code. For example, the Microsoft Office suite is said to contain over 30 millions of lines of code.}

\figure{\includediagram{\diagramsDir/ai/ml-system-monolith-purchasing}{60%}}{A potential path of models in a machine learning system.}{ml-system-monolith}

\includes{_software/includes/separation-of-concerns.md}


\subsection{Service Oriented Architecture}

\notes{Such software is not only difficult to develop, it is difficult to scale when computation demands increase. Amazon's original website software (called Obidos) was a [monolithic design](https://en.wikipedia.org/wiki/Obidos_(software)) but by the early noughties it was becoming difficult to sustain and maintain. The software was phased out in 2006 to be replaced by a modularized software known as a 'service oriented architecture'. 

In Service Oriented Architecture, or "Software as a Service" the idea is that code bases are modularized and communicate with one another using network requests. A standard approach is to use a [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer). So, rather than a single monolithic code base, the code is developed with individual services that handle the different requests.}


\figure{\includediagram{\diagramsDir/ai/ml-system-downstream-purchasing000}{60%}}{A potential path of models in a machine learning system.}{ml-system-downstream-purchasing}

\notes{This is the landscape we now find ourselves in with regard to software development. In practice, each of these services is often 'owned' and maintained by an individual team. The team is judged by the quality of their service provision. They work to detailed specifications on what their service should output, what its availability should be and other objectives like speed of response. This allows for conditional independence between teams and for faster development.}


\endif
