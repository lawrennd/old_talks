---
session: 2
title: "Introduction to Machine Learning Systems"
abstract: "This notebook introduces some of the challenges of building machine learning data systems. It will introduce you to concepts around joining of databases together. The storage and manipulation of data is at the core of machine learning systems and data science. The goal of this notebook is to introduce the reader to these concepts, not to authoritatively answer any questions about the state of Nigerian health facilities or Covid19, but it may give you ideas about how to try and do that in your own country."
author:
- given: Eric
  family: Meissner
  url: https://www.linkedin.com/in/meissnereric/
  twitter: meissner_eric_7 
- given: Andrei
  family: Paleyes
  url: https://www.linkedin.com/in/andreipaleyes/
- given: Neil D.
  family: Lawrence
  twitter: lawrennd
  url: http://inverseprobability.com
date: 2020-07-24
ipynb: true
venue: Virtual DSA
transition: None
---

\include{talk-macros.tex}

\slides{\section{AI via ML Systems}

\include{_ai/includes/supply-chain-system.md}
\include{_ai/includes/aws-soa.md}
\include{_ai/includes/dsa-systems.md}
}

\notes{
\include{_systems/includes/nigeria-health-intro.md}
\include{_systems/includes/nigeria-nmis-installs.md}
\include{_systems/includes/databases-and-joins.md}
\include{_systems/includes/nigeria-nmis-data-systems.md}
\include{_systems/includes/nigeria-nmis-spatial-join.md}
\define{databaseType}{sqlite}
\include{_systems/includes/nigeria-nmis-sql.md}
\include{_systems/includes/nigeria-nmis-covid-join.md}
}

\thanks

\references
