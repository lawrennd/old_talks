---
title: Machine Learning, Technology and the Future of Intelligence
abstract: >
  The Leverhulme Centre for the Future of Intelligence is a fulcrum
  around which debate in intelligence technology can be joined across
  the wide range of intereted experts. In this talk I'll give some
  perspectives on machine learning and my interactions with CFI.
published: 2017-06-26
venue: Leverhulme CFI
layout: slides
author: Neil D. Lawrence
affiliation: Amazon Research Cambridge and University of Sheffield
---

### Machine Learning, Technology and the Future of Intelligence 
### 2017-06-26
### Neil D. Lawrence
### Amazon Research Cambridge and University of Sheffield
```@lawrennd``` [inverseprobability.com](http://inverseprobability.com)

<!--  pandoc -s -S -c talks.css -t revealjs --mathjax="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" -o 2017-06-26-machine-learning-technology-and-the-future-of-intelligence.slides.html 2017-06-26-machine-learning-technology-and-the-future-of-intelligence.md -->


## Machine Learning

$$ \text{data} + \text{model} \rightarrow \text{prediction}$$

* Where prediction is carried out through *computation*.

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

## *Thought* and *Intelligence*

$$ \text{philosophy} \rightarrow \text{psychology} \rightarrow \text{social
psychology}$$
$$\rightarrow \text{economics}\ \text{and}\ \text{social science}$$
<center>*must interconnect with*</center>
$$ \text{cognitive science} \rightarrow \text{machine learning}
\rightarrow \text{systems engineering}$$

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

* That presents *challenges* and *opportunities* (especially for
  traditional economics!)

cf
[digital oligarchy](https://www.theguardian.com/media-network/2015/mar/05/digital-oligarchy-algorithms-personal-data)
vs [how Africa can benefit from the data revolution](https://www.theguardian.com/media-network/2015/aug/25/africa-benefit-data-science-information)


## Machine Learning and Mechanical Systems Design

<img src="./diagrams/SteamEngine_Boulton&Watt_1784_neg.png" width="50%" style="border:none">

## Internet of People

* Fog computing: barrier between cloud and device blurring.

* Internet of Intelligence but currently:

	* AI systems are currently *fragile*

## Two Challenges

1. Humans are very complex to work well inference of *intent* is required.

2. In the meantime, humans are likely needed to moderate machine
behaviour.

## Environment of Operation

* Machine assistance in a controlled environment (e.g. car production
line).

* Machine assistance in the real world (e.g. care robot).

* For Autonomous vehicles think
    1. Would likely deploy first on motorways (more controlled
    environment)
	2. Would likely cause chaos in towns (lack of intent inference)
	3. Unable to step out of vehicle and help elderly passenger to
    appointment.

*  "Empathy Cannot be Automatized"

## Peppercorns

* A new name for system failures which aren't bugs.

* Occur because of the impossibility of imagining all circumstances in
  an uncontrolled environment.

* Difference between finding a fly in your soup vs a peppercorn in
  your soup. 

## Conclusion

* Difference between Artificial Intelligence and Data Science are fundamentally different.

    * In one you are dealing with data collected by happenstance.

    * In the other you are trying to build systems in the real world, often by actively collecting data.

* Challenges around our future may be similar for previous
technological waves.

    * Principal effects on those *least mobile* in the work force. 

	* Urgent need for both *education*, *training* and *research*.

## Thanks!

* twitter: @lawrennd
* blog: [http://inverseprobability.com](http://inverseprobability.com/blog.html)
