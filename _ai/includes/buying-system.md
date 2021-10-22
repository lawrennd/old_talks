\ifndef{buyingSystem}
\define{buyingSystem}

\editme

\subsection{Buying System}


\notes{An example of a complex decision-making system might be an automated buying system. In such a system, the idea is to match demand for products to supply of products.

The matching of demand and supply is a repetitive theme for decision making systems. Not only does it occur in automated buying, but also in the allocation of drivers to riders in a ride sharing system. Or in the allocation of compute resource to users in a cloud system. 

The components of any of these system include predictions of the demand for the product, the drivers, or the compute. Predictions of the supply. Decisions are then made for how much material to keep in stock, or how many drivers to have on the road, or how much computer capacity to have in your data centers. These decisions have cost implications. The optimal amount of product will depend on the cost of making it available. For a buying system this is the storage costs. 

Decisions are made based on the supply and demand to make new orders, to encourage more drivers to come into the system or to build new data centers or rent more computational power.}

\figure{\includediagram{\diagramsDir/software/buying-schematic}{40%}}{The components of a putative automated buying system}{buying-system-components}

\include{_ai/includes/aws-soa.md}


\notes{This is the landscape we now find ourselves in with regard to software development. In practice, each of these services is often 'owned' and maintained by an individual team. The team is judged by the quality of their service provision. They work to detailed specifications on what their service should output, what its availability should be and other objectives like speed of response. This allows for conditional independence between teams and for faster development.}


\endif
