---
title: Machine Learning and the Future of Work
abstract: >
  Machine learning is the fundamental driving technology of two important
  technological domains, artificial intelligence and data science,
  both of which effect the future of work. In
  this summary we will attempt to make a simple definition to distinguish
  between the two, give intuitions of what machine learning is, and
  speculate how this technological change differs from previous ones.
published: 2017-06-23
venue: Chatham House
layout: slides
author: Neil D. Lawrence
affiliation: Amazon Research Cambridge and University of Sheffield
---

### Machine Learning and the Future of Work
### 2017-06-23
### Neil D. Lawrence
### Amazon Research Cambridge and University of Sheffield
```@lawrennd``` [inverseprobability.com](http://inverseprobability.com)

<!--  pandoc -s -S -c talks.css -t revealjs --mathjax="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" -o 2017-06-23-machine-learning-and-the-future-of-work.slides.html 2017-06-23-machine-learning-and-the-future-of-work.md
-->


## Machine Learning

$$ \text{data} + \text{model} \rightarrow \text{prediction}$$

* Royal Society Report:
  [Machine Learning: Power and Promise of Computers that Learn by Example](https://royalsociety.org/~/media/policy/projects/machine-learning/publications/machine-learning-report.pdf)

## Data Science and Artificial Intelligence {.slide: data-transition="none"}

* Data Science: arises from the fact that we now capture data by happenstance.

* Artificial intelligence: emulation of human behaviour.


## "Embodiment Factors"

<table>
<tr><td></td><td align="center">
<img src="./diagrams/IBM_Blue_Gene_P_supercomputer.jpg" width="40%" style="background:none; border:none; box-shadow:none;" align="center">
</td>
<td align="center">
<img src="./diagrams/ClaudeShannon_MFO3807.jpg" width="60%" style="background:none; border:none; box-shadow:none;" align="center">
</td>
</tr>
<tr>
<td>compute</td><td align="center">~10 gigaflops</td><td align="center">~ 1000 teraflops?</td>
</tr>
<tr>
<td>communicate</td><td align="center">~1 gigbit/s</td><td align="center">~ 100 bit/s</td>
</tr>
<tr>
<td>embodiment<br>(compute/communicate)</td><td align="center">10</td><td align="center">~ 10<sup>13</sup></td>
</tr>
</table>

See ["Living Together: Mind and Machine Intelligence"](https://arxiv.org/abs/1705.07996)

## What does Machine Learning do?

* We scale by codifying processes and automating them.

    * Ensure components are compatible (Whitworth threads)

    * Then interconnect them as efficiently as possible.

    * cf Colt 45, Ford Model T, 

## What does Machine Learning do?

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

* Example: face recognition

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

## Industrial Revolution 4.0?


* *Industrial Revolution* (1760-1840) term coined by Arnold Toynbee,
late 19th century.

* Maybe: But this one is dominated by *data* not *capital*

* That presents *challenges* and *opportunities* (especially for economists!)

cf
[digital oligarchy](https://www.theguardian.com/media-network/2015/mar/05/digital-oligarchy-algorithms-personal-data)
vs [how Africa can benefit from the data revolution](https://www.theguardian.com/media-network/2015/aug/25/africa-benefit-data-science-information)

* Apple vs Nokia: How you handle disruption.

* A threat to the future of Economists' work???

## Thanks!

* twitter: @lawrennd
* blog: [http://inverseprobability.com](http://inverseprobability.com/blog.html)
