---
title: "Data Science: Is it Time for Professionalisation?"
abstract: >
  Machine learning methods and software are becoming widely
  deployed. But how are we sharing expertise about bottlenecks and
  pain points in deploying solutions? In terms of the practice of data
  science, we seem to be at a similar point today as software
  engineering was in the early 1980s. Best practice is not widely
  understood or deployed. In this talk we will focus on two particular
  components of data science solutions: the preparation of data snd
  the deployment of machine learning systems. 
author: Neil D. Lawrence
affiliation: Amazon Research Cambridge and University of Sheffield
---

#### Data Science: Time for Professionalisation?
#### 2018-03-27
#### Neil D. Lawrence
#### Amazon Research Cambridge and University of Sheffield
```@lawrennd``` [inverseprobability.com](http://inverseprobability.com)

<!--  pandoc -s -S -c talks.css -t revealjs --mathjax="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" -o 2017-06-27-data-science-time-for-professionalisation.slides.html 2017-06-27-data-science-time-for-professionalisation.md
-->

\include{../talk-macros.tex}
\include{../_ml/includes/what-is-ml.md}
\include{../_ml/includes/data-science-vs-ai.md}
\include{../_ai/includes/embodiment-factors.md}
\include{../_data-science/includes/evolved-relationship.md}
\include{../_ml/includes/what-does-machine-learning-do.md}

### Deep Learning

* These are interpretable models: vital for disease etc.

* Modern machine learning methods are less interpretable

* Example: face recognition

\include{../_ml/includes/deep-learning-overview.md}

\include{_data-science/includes/a-time-for-professionalisation.md}

\include{../_data-science/includes/the-data-crisis.md}

### Rest of this Talk: Two Areas of Focus {.slide: data-transition="none" }

* Reusability of Data

* Deployment of Machine Learning Systems

\include{../_data-science/includes/data-readiness-levels.md}
\include{../_data-science/includes/data-joel-tests.md}
\include{../_ai/includes/deploying-ai.md}
\include{../_ai/includes/ml-systems-design-long.md}

### Conclusion

* Difference between Artificial Intelligence and Data Science are fundamentally different.

* In one you are dealing with data collected by happenstance.

* In the other you are trying to build systems in the real world, often by actively collecting data.

* Our approaches to systems design are building powerful machines that
will be deployed in evolving environments.


### Thanks!

* twitter: \@lawrennd
* blog: [http://inverseprobability.com](http://inverseprobability.com/blog.html)
