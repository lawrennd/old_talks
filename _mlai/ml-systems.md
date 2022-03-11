---
week: 4
title: "Data and Machine Learning Systems"
abstract: "So far we have introduced objective functions, and (linear) prediction functions. This gives us two key ingredients of the machine learning formula. But to build machine learning systems you also need data. This lecture introduces some of the challenges of building machine learning data systems. It will introduce (or review) for you the concepts around joining of databases together. The storage and manipulation of data is at the core of machine learning systems and data science. Note: the notebook makes use of Covid19 data from Nigeria, but the goal of this notebook is to introduce the reader to these concepts, not to authoritatively answer any questions about the state of Nigerian health facilities or Covid19, but to give you an understanding of data infrastructures and bringing data sets together."
author:
- given: Eric
  family: Meissner
  url: https://www.linkedin.com/in/meissnereric/
  twitter: meissner_eric_7 
  institute: University of Cambridge
- given: Andrei
  family: Paleyes
  url: https://www.linkedin.com/in/andreipaleyes/
  institute: University of Cambridge
- given: Neil D.
  family: Lawrence
  twitter: lawrennd
  url: http://inverseprobability.com
  institute: University of Cambridge
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
\define{databaseType}{mariadb}
\include{_systems/includes/nigeria-nmis-sql.md}
\include{_systems/includes/nigeria-nmis-covid-join.md}
}

\thanks

\references
