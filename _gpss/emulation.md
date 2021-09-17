---
title: Emulation
session: 13
abstract: In this session we introduce the notion of emulation and systems modeling with Gaussian processes.
date: 2021-09-15
venue: Virtual GPSS
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Cambridge
  twitter: lawrennd
  orcid: 0000-0001-9258-1030
  url: http://inverseprobability.com
postsdir: ../_posts/
slidesdir: ../slides/
notesdir: ../_notes/
notebooksdir: ../_notebooks/
writediagramsdir: .
diagramsdir: ./slides/diagrams/
transition: None
layout: talk
---


\newslide{}

> We may regard the present state of the universe as the effect of its
> past and the cause of its future. An intellect which at a certain
> moment would know all forces that set nature in motion, and all
> positions of all items of which nature is composed, ...
\newslide{}
> ... if this intellect
> were also vast enough to submit these data to analysis, it would
> embrace in a single formula the movements of the greatest bodies of
> the universe and those of the tiniest atom; for such an intellect
> nothing would be uncertain and the future just like the past would be
> present before its eyes.
>
> --- Pierre Simon Laplace [@Laplace-essai14]


\include{_simulation/includes/game-of-life.md}

\speakernotes{Laplace's demon requires us to also know positions of all items and to submit the data to analysis.}

\newslide{}

\notes{We summarize this notion as}
$$
\text{data} + \text{model} \stackrel{\text{compute}}{\rightarrow} \text{prediction}
$$
\notes{As we pointed out, there is an irony in Laplace's demon forming the cornerstone of a movement known as 'determinism', because Laplace wrote about this idea in an essay on probabilities. The more important quote in the essay was }

\include{_physics/includes/laplaces-gremlin.md}

\include{_simulation/includes/simulation-system.md}
\include{_data-science/includes/experiment-analyze-design.md}
\include{_uq/includes/emulation.md}
\notes{\include{_gp/includes/gpy-emulation.md}}
\include{_software/includes/emukit-software.md}
\include{_uq/includes/emukit-vision.md}
\include{_uq/includes/emukit-playground.md}
\notes{\include{_uq/includes/emukit-tutorial.md}}
\notes{\include{_uq/includes/emukit-sensitivity-analysis.md}}
\notes{\include{_uq/includes/catapult-sensitivity-analysis.md}}

\thanks

\references

