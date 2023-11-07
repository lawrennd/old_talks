---
title: "Machine Learning and Data Readiness Levels"
abstract: >
  In this talk we will look at the challenges facing deployment of machine learning, with a particular focus on the reuse of data and data quality. We suggest data readiness levels as a mechanism for monitoring data quality.
author: Neil D. Lawrence
author:
- given: Neil D.
  family: Lawrence
  url: http://inverseprobability.com
  institute: Amazon Cambridge and University of Sheffield
  twitter: lawrennd
  gscholar: r3SJcvoAAAAJ
  orchid: 
date: 2018-01-25
layout: talk
geometry: ["a4paper", "margin=2cm"]
papersize: a4paper
transition: None
categories:
- notes
---


\include{_ml/includes/what-is-ml.md}
\include{_ml/includes/data-science-vs-ai.md}
\include{_ai/includes/embodiment-factors.md}
\include{_data-science/includes/evolved-relationship.md}
\include{_ml/includes/what-does-machine-learning-do.md}
\include{_ml/includes/deep-learning-overview.md}
\include{_data-science/includes/a-time-for-professionalisation.md}
\include{_data-science/includes/the-data-crisis.md}

\newslide{Rest of this Talk: Two Areas of Focus}
\slides{
* Reusability of Data

* Deployment of Machine Learning Systems
}
\notes{For deploying machine learning in practice there are many changes required to the way we create and deploy our systems, but for the rest of this talk, I'll focus on one of these only: the reusabililty of data.}

\newslide{Rest of this Talk: Two Areas of Focus}
\slides{
* Reusability of Data

* <s>Deployment of Machine Learning Systems</s>
}
\include{_data-science/includes/data-readiness-levels.md}

<!--include{_ai/includes/deploying-ai.md}-->

<!--include{_ai/includes/ml-systems-design-long.md}-->

\newslide{Conclusion}
\slides{
* Artificial Intelligence and Data Science are fundamentally different.

* In one you are dealing with data collected by happenstance.

* In the other you are trying to build systems in the real world, often by actively collecting data.

* Our ability to exploit ML will be limited in the near term by the poor quality of our data infrastructures.
}
\notes{Artificial Intelligence and Data Science are fundamentally different. In one you are dealing with data collected by happenstance. In the other you are trying to build systems in the real world, often by actively collecting data.

Our ability to exploit ML will be limited in the near term by the poor quality of our data infrastructures.}


\thanks

\references
