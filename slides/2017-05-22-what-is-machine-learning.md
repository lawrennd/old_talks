---
title: What is Machine Learning?
abstract: What is machine learning and how is it useful? I this talk we will focus on where machine learning technologies can be deployed within an industrail context and what needs to be in place to make the most effective use of them.
published: 2017-05-22
venue: CLT UK Meeting
layout: slides
author: Neil D. Lawrence
affiliation: Amazon Research Cambridge and University of Sheffield
---

### CLT UK Meeting
### 2017-05-22
### Neil D. Lawrence
### Amazon Research Cambridge and University of Sheffield
```@lawrennd``` [inverseprobability.com](http://inverseprobability.com)
<!--  pandoc -s -S -c talks.css -t revealjs --mathjax="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" -o 2017-05-22-what-is-machine-learning.slides.html 2017-05-22-what-is-machine-learning.md
-->


## Gartner Hype Cycle

<img src="./diagrams/Gartner_Hype_Cycle-neg.png" align="center" width="70%" style="background:none; border:none; box-shadow:none;">

## {.slide: data-transition="none"}

<object type="image/svg+xml" data="./diagrams/ml-ai-ds-google-trends-000.svg">
</object>

## {.slide: data-transition="none"}

<object type="image/svg+xml" data="./diagrams/ml-ai-ds-google-trends-001.svg">
</object>

## {.slide: data-transition="none"}

<object type="image/svg+xml" data="./diagrams/ml-ai-ds-google-trends-002.svg">
</object>

## {.slide: data-transition="none"}

<object type="image/svg+xml" data="./diagrams/ml-ai-ds-google-trends-003.svg">
</object>

## {.slide: data-transition="none"}

<object type="image/svg+xml" data="./diagrams/ml-ai-ds-google-trends-004.svg">
</object>


## Machine Learning

$$ \text{data} + \text{model} \rightarrow \text{prediction}$$

## Machine Learning

* Normal ML (& stats?) focus: model

* In real world need more focus on: data

* motivation for data science


## Background: Big Data

* The pervasiveness of data brings forward particular challenges.

* Emerging themes: Devolving compute onto device. 

* Data preprocessing: Internet of Intelligence.


## How does ML Help?

* We scale by codifying processes and automating them.

    * Ensure components are compatible (Whitworth threads)

    * Then interconnect them as efficiently as possible.

    * cf Colt 45, Ford Model T, 

## How does ML Help?

* ML Automates through Data

    * *Strongly* related to statistics.

    * Field underpins revolution in *data science* and *AI*

* With AI: logic, robotics, computer vision, speech

* With Data Science: databases, data mining, statistics, visualization


## Codify Through Mathematical Functions 

* How does machine learning work?

* Jumper (jersey/sweater) purchase with logistic regression

$$ \text{odds} = \frac{\text{bought}}{\text{not bought}} $$

$$ \log \text{odds}  = \beta_0 + \beta_1 \text{age} + \beta_2 \text{lattitude}$$


## Codify Through Mathematical Functions {.slide: data-transition="none"}

* How does machine learning work?

* Jumper (jersey/sweater) purchase with logistic regression

$$ p(\text{bought}) =  f\left(\beta_0 + \beta_1 \text{age} + \beta_2 \text{lattitude}\right)$$


## Codify Through Mathematical Functions {.slide: data-transition="none"}

* How does machine learning work?

* Jumper (jersey/sweater) purchase with logistic regression

$$ p(\text{bought}) =  f\left(\boldsymbol{\beta}^\top \mathbf{x}\right)$$


## Deep Learning

* These are interpretable models: vital for disease etc.

* Modern machine learning methods are less interpretable

* Example: face recognition (see also Berlin work on Amazon Fresh)

##

<span class="fragment fade-in"><small>Outline of the DeepFace architecture. A front-end of a single convolution-pooling-convolution filtering on the rectified input, followed by three locally-connected layers and two fully-connected layers. Color illustrates feature maps produced at each layer. The net includes more than 120 million parameters, where more than 95% come from the local and fully connected.</small></span>


<img src="./diagrams/deepface_neg.png" width="100%" style="background:none; border:none; box-shadow:none;" align="center">

<p align="right">
<small>Source: DeepFace</small></p>

## 

<img src="./diagrams/576px-Early_Pinball.jpg" height="576px" style="background:none; border:none; box-shadow:none;" align="center">

##

<object data="./diagrams/pinball-initial.svg" type="image/svg+xml">
</object>


## {.slide: data-transition="none" }

<object data="./diagrams/pinball-final.svg" type="image/svg+xml">
</object>

## When Can ML be Used?

* Data science

    * To get better data we need to improve our processes

* Artificial Intelligence

    * Any sub-task that takes a human less than a second

    * Also important for acquiring data (Mechanical Turk, ADS). 



## What are we doing about it?

* Core ML Team: Berlin, Bangalore, Seattle, Barcelona, Los Angeles and *Cambridge*


* Amazon Research Cambridge

    * The Data Science Laboratory

    * Customer obsession for data scientists


## The Data Science Laboratory

* Challenges of Data Science

   1. Paradoxes of data society
   
   2. Quantifying value of data

   3. Fairness, privacy and marginalization

## Quantifying the Value of Data

There's a sea of data, but most of it is undrinkable

<img src="./diagrams/sea-water-ocean-waves.jpg" width="50%">

We require data-desalination before it can be consumed!


## Data --- Quotes from NIPS Workshop on ML for Healthcare

* 90% of our time is spent on validation and integration (Leo Anthony Celi)
* "The Dirty Work We Don't Want to Think About" (Eric Xing)
* "Voodoo to get it decompressed" (Francisco Giminez)
* In health care clinicians collect the data and often control the direction of research through guardianship of data.

## Quotes from AMLC Data Science Process

* Getting money from management for data collection and annotation can
be a total nightmare.

## Value

* How do we measure value in the data economy?

* How do we encourage data workers: curation and management

	* Incentivization for sharing and production.

	* Quantifying the value in the contribution of *each actor*.


## Embodiment:
   [Data Readiness Levels](http://inverseprobability.com/2017/01/12/data-readiness-levels)
   (see also [arxiv](https://arxiv.org/pdf/1705.02245.pdf))

* Three Bands of Data Readiness:

* Band C - accessibility

* Band B - validity

* Band A - usability



## Contribute!

* http://data-readiness.org

## Also ...

* Encourage greater interaction between application domains and data scientists

* Encourage *visualization* of data

* Incentivise the delivery of data.

* Analogies: For SDEs [describe data science as *debugging*](http://inverseprobability.com/2017/03/14/data-science-as-debugging).

## See Also ...

* Data Joel Tests
    * [proposal by Damon Civin](https://medium.com/@damoncivin/the-joel-test-for-data-readiness-4882aae64753) and
    * [proposal by Nick Elprin](https://blog.dominodatalab.com/joel-test-data-science/)


## Challenges for AI

   * Machine Learning Systems Design

   * Peppercorns (exposed gears!)


## Are you smarter than a 10 year old?


<video class="stretch" src="./diagrams/2017-05-20 09.35.26.mp4"></video>


## Conclusion

* Machine Learning is not a magic trick

    * Two principal areas of deployment:

        1. Data Science

        2. Artificial Intelligence

## Conclusion

* Challenges in each area are different:

    * For AI challenge of peppercorns and systems design

    * For data science challenges of data quality, fairness, privacy and bias.


## Thanks!

* twitter: @lawrennd
* blog: [http://inverseprobability.com](http://inverseprobability.com/blog.html)
