---
title: "Machine Learning and Data Readiness Levels"
abstract: >
  In this talk we will look at the challenges facing deployment of machine learning, with a particular focus on the reuse of data and data quality. We suggest data readiness levels as a mechanism for monitoring data quality.
author: Neil D. Lawrence
affiliation: Amazon Research Cambridge and University of Sheffield
---

#### Machine Learning and Data Readiness Levels
#### 2018-01-25
#### Neil D. Lawrence
#### Amazon Research Cambridge and University of Sheffield
```@lawrennd``` [inverseprobability.com](http://inverseprobability.com)


\include{../_ml/includes/what-is-ml.md}

### Machine Learning as the Driver ... {.slide: data-transition="none"}


... of two different domains

1. *Data Science*: arises from the fact that we now capture data by happenstance.

2. *Artificial Intelligence*: emulation of human behaviour.


### What does Machine Learning do?

* ML Automates through Data

    * *Strongly* related to statistics.

    * Field underpins revolution in *data science* and *AI*

* With AI: logic, robotics, computer vision, speech

* With Data Science: databases, data mining, statistics, visualization

\include{../_ai/includes/embodiment-factors.md}

\include{../_data-science/includes/evolved-relationship.md}

\include{../_ml/includes/what-does-machine-learning-do.md}

\include{../_ml/includes/deep-learning-overview.md}



### Deep Learning

* These are interpretable models: vital for disease etc.

* Modern machine learning methods are less interpretable

* Example: face recognition

###

<span class="fragment fade-in"><small>Outline of the DeepFace architecture. A front-end of a single convolution-pooling-convolution filtering on the rectified input, followed by three locally-connected layers and two fully-connected layers. Color illustrates feature maps produced at each layer. The net includes more than 120 million parameters, where more than 95% come from the local and fully connected.</small></span>


<img src="./diagrams/deepface_neg.png" width="100%" style="background:none; border:none; box-shadow:none;" align="center">

<p align="right">
<small>Source: DeepFace</small></p>

### 

<img src="./diagrams/576px-Early_Pinball.jpg" height="576px" style="background:none; border:none; box-shadow:none;" align="center">

###

<object data="./diagrams/pinball-initial.svg" type="image/svg+xml">
</object>


### {.slide: data-transition="none" }

<object data="./diagrams/pinball-final.svg" type="image/svg+xml">
</object>


### Data Science

* Industrial Revolution 4.0?

* *Industrial Revolution* (1760-1840) term coined by Arnold Toynbee,
late 19th century.

* Maybe: But this one is dominated by *data* not *capital*

* That presents *challenges* and *opportunities* 

cf
[digital oligarchy](https://www.theguardian.com/media-network/2015/mar/05/digital-oligarchy-algorithms-personal-data)
vs [how Africa can benefit from the data revolution](https://www.theguardian.com/media-network/2015/aug/25/africa-benefit-data-science-information)

* Apple vs Nokia: How you handle disruption.


### A Time for Professionalisation?

* New technologies historically led to new professions:

    * Brunel (born 1806): Civil, mechanical, naval

    * Tesla (born 1856): Electrical and power
 
    * William Shockley (born 1910): Electronic 

    * Watts S. Humphrey (born 1927): Software

### Why?

* Codification of best practice.

* Developing trust

### Where are we?

* Perhaps around the 1980s of programming.

    * We understand if, for, procedures

    * But we don't share best practice.

* Let's *avoid* the over formalisation of software engineering.

\include{../_data-science/includes/the-data-crisis.md}

### Rest of this Talk: Two Areas of Focus {.slide: data-transition="none" }

* Reusability of Data

* Deployment of Machine Learning Systems

### Rest of this Talk: Two Areas of Focus {.slide: data-transition="none" }

* Reusability of Data

* <s>Deployment of Machine Learning Systems</s>

\include{../_data-science/includes/data-readiness-levels.md}

<!--\include{../_ai/includes/deploying-ai.md}-->

<!--\include{../_ai/includes/ml-systems-design-long.md}-->

### Conclusion

* Artificial Intelligence and Data Science are fundamentally different.

* In one you are dealing with data collected by happenstance.

* In the other you are trying to build systems in the real world, often by actively collecting data.

* Our ability to exploit ML will be limited in the near term by the poor quality of our data infrastructures.

### Thanks!

* twitter: \@lawrennd
* blog: [http://inverseprobability.com](http://inverseprobability.com/blog.html)
