\ifndef{theDeathOfTheProgrammer}
\define{theDeathOfTheProgrammer}

\editme

\subsection{The Death of the Programmer}

\figure{\includejpg{\diagramsDir/ai/lemortedarthur}{40%}}{Malory's book "Le Morte d'Arthur. A guide to team building in the age of chivalry.}{arthur-book}


\notes{By "The Death of the Programmer" we are giving a nod to ["The Death of
the Author"](https://en.wikipedia.org/wiki/The_Death_of_the_Author), a
literary criticism essay which argues that readers must separate a
literary work from the author.[^2] That the interpretation of a work depends
on the impression on the reader, rather than the intention of the
author. "The Death of the Programmer" occurs in the service-oriented
architecture framework, because whatever the intent of the team that
built and maintains each individual service, once it is deployed the
service can be consumed for whichever purpose. It is beyond the control
of the original programmers. This is a challenge because notions of
interpretability, bias and fairness rely on context. The context is
controlled by the consumer of these services not by the programmers of
these services. So however well-intentioned the work of ensuring
fairness was in an individual model, once it is consumed the authors'
best intentions can be sacrificed as the service is repurposed for a
role beyond the original programmers' understanding.

[^2]: The essay is originally in French, *La mort de l'auteur* and is a play on the Malory book *Le Mort d'Arthur*.

So even if we deploy a component that we consider to be fair and
explainable for the role for which it was intended, but since the
consumers of the service don't have access to the intent of the
programmers, in practice the service will fail to be fair or
explainable.}

\endif
