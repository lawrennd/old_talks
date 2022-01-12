\ifndef{theApiMandateBezos}
\define{theApiMandateBezos}

\editme

\subsection{The API Mandate}

\notes{The API Mandate was a memo issued by Jeff Bezos in 2002. Internet folklore has the memo making five statements:}

* All teams will henceforth expose their data and functionality through service interfaces.
* Teams must communicate with each other through these interfaces.\slides{
\newslide{}}
* There will be no other form of inter-process communication allowed: no direct linking, no direct reads of another team’s data store, no shared-memory model, no back-doors whatsoever. The only communication allowed is via service interface calls over the network.\slides{
\newslide{}}
* It doesn’t matter what technology they use.
* All service interfaces, without exception, must be designed from the ground up to be externalizable. That is to say, the team must plan and design to be able to expose the interface to developers in the outside world. No exceptions.

\notes{The mandate marked a shift in the way Amazon viewed software, moving to a model that dominates the way software is built today, so-called "Software-as-a-Service".}

\newslide{Duality of Corporation and Information}

\slides{* What is less written about is *corporate structure*.
* This *information infrastructure* is reflected in the corporation.
* Two pizza teams with *devolved autonomy*.
* Bound together through *corporate culture*.}

\notes{What is less written about the effect it had on Amazon's organizational structure. Amazon is set up around the notion of the "two pizza team". Teams of 6-10 people that can be theoretically fed by two (American) pizzas. This structure is tightly interconnected with the software. Each of these teams owns one of these "services". Amazon is strict about the team that develops the service *owning* the service in production. This approach is the secret to their scale as a company, and the approach has been adopted by many other large tech companies. The software-as-a-service approach changed the *information infrastructure* of the company. The routes through which information is shared. This had a knock-on effect on the corporate culture.}

\notes{Amazon works through an approach I think of as "devolved autonomy". The culture of the company is widely taught (e.g. Customer Obsession, Ownership, Frugality), a teams inputs and outputs are strictly defined, but within those parameters, teams have a great of autonomy in how they operate. The information infrastructure was devolved, so the autonomy was devolved. The different parts of Amazon are then bound together through shared corporate culture.}

\endif
