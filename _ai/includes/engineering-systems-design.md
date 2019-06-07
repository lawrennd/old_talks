\ifndef{engineeringSystemsDesign}

\subsection{Engineering Systems Design}

\slides{
* Major component of all Engineering disciplines.

* Details differ: there is a common theme: achieve your objective with the minimal use of resources to do the job.

* This provides efficiency.

* Engineering designer imagines a solution that requires the minimal set of components to achieve the result.

* A water pump has one route through the pump.
}

\notes{Engineering systems design is a major component of all engineering disciplines, in each domain the details differ, but there is a common theme. The aim is to achieve your objective with the minimal use of resources to do the job. This provides *efficiency*. An engineering designer imagines a solution that requires the minimal set of components to achieve a given result. 

For example, a water pump has a single route through the pump, the mechanism of the pump involves a single non-redundant set of linkages. This minimizes the resources needed for manufacturing the pump.}

\subsection{Don't Fail}

\slides{
* First criterion of a natural intelligence is *don’t fail*.

* In contrast, mantra for artificial systems is to be more efficient.

* Artificial systems are given a single objective (in machine learning it is encoded in a mathematical function)

* Aim to achieve that objective efficiently.
}

\notes{The first criterion of natural intelligence is *don't fail*. This is in contrast to the mantra for artificial systems which is to be more efficient. Artificial systems are typically given a single objective (in machine learning it is encoded in a mathematical function). The aim is to achieve that objective efficiently.}

\newslide{Designing out Failure}
\slides{
* Even if we wanted to incorporate *don’t fail* in some form, it is difficult to design for.

* To design for “don’t fail”, you have to consider every which way in which things can go wrong, if you miss one you fail. These cases are sometimes called corner cases.
}

\notes{Even if we wanted to incorporate *don't fail* in some form, it is surprisingly difficult to design for. You would have to consider every which way in which things can go wrong. If you miss one you will fail. These cases are sometimes called corner cases.}

\newslide{Corners Everywhere }
\slides{
* In an uncontrolled environment, almost everything is a corner.

    * It is difficult to imagine everything that can happen.
    
    * Most of our automated systems operate in controlled environments (e.g.  a factory, a set of rails.)
}
\notes{
In an uncontrolled environment there are corners everywhere. It is difficult to imagine everything that can happen. As a result most of our automated systems operate in controlled environments, e.g. in a factory, on a set of rails. 

We can imagine a driverless car operating on a highway (a more controlled environment), but it is harder to imagine how one would operate in the city centres of Naples, Kampala or Delhi (less controlled environments).}

\newslide{Deployment in Uncontrolled Environments}
\slides{
* Requires a different approach to systems design.

. . .

* One that accounts for uncertainty in the environment

. . .

* One that is robust to unforeseen circumstances. 
}

\notes{Deployment in uncontrolled environments may require a different approach to systems design, one that accounts for uncertainty in the environment and one that is robust to unforeseen circumstances.}
