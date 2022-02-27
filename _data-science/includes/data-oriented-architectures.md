\ifndef{dataOrientedArchitectures}
\define{dataOrientedArchitectures}

\editme

talk-macros.gpp}ata-science/includes/data-oriented-architectures-intro.md}
talk-macros.gpp}ata-science/includes/apache-flink.md}
talk-macros.gpp}ata-science/includes/milan.md}
talk-macros.gpp}ata-science/includes/hypothetical-trading-system.md}
talk-macros.gpp}i/includes/safe-boda.md}
talk-macros.gpp}i/includes/ride-allocation-prediction.md}


\notes{Let's consider a ride sharing app, for example the SafeBoda system. 

Anne is on her way home now; she wishes to hail a car using a ride sharing app. 

The app is designed in the following way. On opening her app Anne is notified about drivers in the nearby neighborhood. She is given an estimate of the time a ride may take to come.

Given this information about driver availability, Anne may feel encouraged to enter a destination. Given this destination, a price estimate can be given. This price is conditioned on other riders that may wish to go in the same direction, but the price estimate needs to be made before the user agrees to the ride. 

Business customer service constraints dictate that this price may not change after Anne's order is confirmed. 

In this simple system, several decisions are being made, each of them on the basis of a hypothetical.

When Anne calls for a ride, she is provided with an estimate based on the expected time a ride can be with her. But this estimate is made without knowing where Anne wants to go. There are constraints on drivers imposed by regional boundaries, reaching the end of their shift, or their current passengers mean that this estimate can only be a best guess.

This best guess may well be driven by previous data.}

talk-macros.gpp}ata-science/includes/ride-sharing-soa-doa.md}
talk-macros.gpp}ata-science/includes/information-dynamics.md}



\endif
