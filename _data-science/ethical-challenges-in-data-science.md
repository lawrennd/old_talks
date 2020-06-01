---
title: Echical Challenges in Data Science
venue: HSBC Briefing
abstract: 
transition: None
date: 2020-06-01
---

\include{talk-macros.tex}

\include{_data-science/includes/evolved-relationship.md}
\include{_ai/includes/embodiment-factors-short.md}

\include{_ml/includes/data-plus-model.md}

\include{_governance/includes/data-governance-toolkit.md}

\newslide{Data and Risk}

\define{\divoptions}{max-width:100vw; max-height:100vh}
\define{\svgstyle}{height:50%}
\define{\stubname}{new-flow-of-information}

\slides{\div{\includediagram{\diagramsDir/governance/risk-framework}{70%}{}{\svgstyle}}{\stubname}{\divoptions}}

\newslide{Data and Risk}

\define{\divoptions}{max-width:100vw; max-height:100vh}
\define{\svgstyle}{height:50%}
\define{\stubname}{new-flow-of-information}

\slides{\div{\includediagram{\diagramsDir/governance/risk-framework2}{70%}{}{\svgstyle}}{\stubname}{\divoptions}}


\newslide{Framework}

* Explainability
* Bias
* Data Sources

\newslide{Explainability}

  * Purpose - define scope and why 'model + data' 
  * Rationale - what features drive outcome?

\newslide{Bias}

  * Unrepresentative data
  * Historic bias 
  * Proxy bias - model indirectly discriminates on protexted characteristics
  
\newslide{Data Sources}

  * Consent - has permission been granted?
  * Third party (Trojan ethics)

\thanks
