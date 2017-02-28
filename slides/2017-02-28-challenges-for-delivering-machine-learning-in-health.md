---
title: Challenges for Delivering Machine Learning in Health
layout: slides
venue: Deep Learning in Healthcare Summit, London
date: 2017-02-28
author: Neil D. Lawrence
affiliation: Amazon and University of Sheffield
---

### Deep Learning in Healthcare Summit 2017
### 2017-02-28
### Neil D. Lawrence
### Amazon and University of Sheffield
```@lawrennd``` [inverseprobability.com](http://inverseprobability.com)
<!--  pandoc -s -S -c talks.css -t revealjs --mathjax="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" -o 2017-02-28-challenges-for-delivering-machine-learning-in-health.slides.html 2017-02-28-challenges-for-delivering-machine-learning-in-health.md
-->



## Gartner Hype Cycle


<img src="./diagrams/Gartner_Hype_Cycle-neg.png" align="center" width="70%" style="background:none; border:none; box-shadow:none;">

## {.slide: data-transition="none"}

<object type="image/svg+xml" data="./diagrams/ai-bd-dl-google-trends-000.svg">
</object>

## {.slide: data-transition="none"}

<object type="image/svg+xml" data="./diagrams/ai-bd-dl-google-trends-001.svg">
</object>

## {.slide: data-transition="none"}

<object type="image/svg+xml" data="./diagrams/ai-bd-dl-google-trends-002.svg">
</object>

## {.slide: data-transition="none"}

<object type="image/svg+xml" data="./diagrams/ai-bd-dl-google-trends-003.svg">
</object>


## Background: Big Data

* The pervasiveness of data brings forward particular challenges.

* Those challenges are most sharply in focus for personalized health.

* Particular opportunities, in challenging areas such as *mental health*.



## Evolved Relationship 

<object type="image/svg+xml" data="./diagrams/data-science-information-flow_neg003.svg">
</object>


## Effects

* This phenomenon has already revolutionised biology.

* Large scale data acquisition and distribution.

* Transcriptomics, genomics, epigenomics, 'rich phenomics'.

* Great *promise* for personalized health.


## Challenges

1. Paradoxes of the Data Society

2. Quantifying the Value of Data

3. Privacy, loss of control, marginalisation


## Breadth vs Depth Paradox

* Able to quantify to a greater and greater degree the actions of individuals

* But less able to characterize society

* As we measure more, we understand less

## What?

* Perhaps greater preponderance of data is making society itself more complex

* Therefore traditional approaches to measurement are failing

* Curate's egg of a society: it is only 'measured in parts'

## Wood or Tree

* Can either see a wood or a tree. 

<img src="./diagrams/Grib_skov.jpg" width="50%" style="border:none">
<!-- https://upload.wikimedia.org/wikipedia/commons/5/5b/Grib_skov.jpg-->

## Examples

* Election polls (UK 2015 elections, EU referendum, US 2016 elections)

* Clinical trials vs personalized medicine: Obtaining statistical power where interventions are subtle. e.g. social media



## Large $p$, Large $n$

* For large $p$ the parameters are badly determined.

* Large $p$ small $n$ problem.

    * Easily dealt with through definition.


## Breadth vs Depth

* Modern Measurement deals with *depth* (many subjects)
    ... or *breadth* lots of detail about subject.
	
* But what about 
    * $p\approx n$?
    * Stratification of populations: batch effects etc.

* Challenge around combination of data sets.
    * E.g. multi-task learning
    * Massively missing data


## Also need

* More classical statistics!
    * Like the 'paperless office'

* A better characterization of human (see later)

* Larger studies (100,000 genome)
    * Combined with complex models: algorithmic challenges

## Quantifying the Value of Data

There's a sea of data, but most of it is undrinkable

<img src="./diagrams/sea-water-ocean-waves.jpg" width="50%">

We require data-desalination before it can be consumed!


## Data --- Quotes from NIPS Workshop on ML for Healthcare

* 90% of our time is spent on validation and integration (Leo Anthony Celi)
* "The Dirty Work We Don't Want to Think About" (Eric Xing)
* "Voodoo to get it decompressed" (Francisco Giminez)
* In health care clinicians collect the data and often control the direction of research through guardianship of data.

## Value

* How do we measure value in the data economy?
* How do we encourage data workers: curation and management
    * Incentivization for sharing and production.
    * Quantifying the value in the contribution of *each actor*.


## Embodiment: Data Readiness Levels

* Three Bands of Data Readiness:

* Band C - accessibility

* Band B - validity

* Band A - usability


## Accessibility: Band C

* Hearsay data.
* Availability, is it actually being recorded?
* privacy or legal constraints on the accessibility of the recorded data, have ethical constraints been alleviated?
* Format: log books, PDF ...
* limitations on access due to topology (e.g. it's distributed across a number of devices)

## Validity: Band B

*  faithfulness and representation
* visualisations.
* noise characterisation.
* Missing values.
* Example, was a column or columns accidentally perturbed (e.g. through a sort operation that missed one or more columns)? Or was a [gene name accidentally converted to a date](http://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-5-80)?

## Usability: Band A

* The usability of data
* Band A is about data in context.
* Consider appropriateness of a given data set to answer a particular
question or to be subject to a particular analysis.

## Recursive Effects

* Band A may also require
    * active collection of new data. 
    * annotation of data by human experts
    * revisiting the collection (and running through the appropriate stages again)

## Also ...

* Encourage greater interaction between application domains and data scientists

* Encourage *visualization* of data

* Incentivise the delivery of data.

## Privacy, Loss of Control and Marginalization

* Society is becoming harder to monitor

* Individual is becoming easier to monitor

## Discrimination

* Marketing can become more sinister when the target of the marketing is well understood and the (digital) environment of the target is also so well controlled

* Potential for explicit and implicit discrimination on the basis of race, religion, sexuality, health status

* All prohibited under European law, but can pass unawares, or be implicit


## Marginalization

* Credit scoring, insurance, medical treatment
* What if certain sectors of society are under-represented in our aanalysis?
* What if Silicon Valley develops everything for us?

## Digital Revolution and Inequality?

<img src="./diagrams/woman-tends-house-in-village-of-uganda-africa.jpg" width="50%" style="border:none">

## Amelioration

* Work to ensure individual retains control of their own data
* We accept privacy in our real lives, need to accept it in our digital
* Control of persona and ability to project

* Need better technological solutions: trust and algorithms.


## Conclusion

* Data science offers a great deal of promise for personalized health
* There are challenges and pitfalls
* It is incumbent on us to avoid them

**Many solutions rely on education and awareness**


## Thanks!

* twitter: @lawrennd
* blog: [http://inverseprobability.com](http://inverseprobability.com/blog.html)
