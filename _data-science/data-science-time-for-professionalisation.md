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
#### 2017-10-13
#### Neil D. Lawrence
#### Amazon Research Cambridge and University of Sheffield
```@lawrennd``` [inverseprobability.com](http://inverseprobability.com)

<!--  pandoc -s -S -c talks.css -t revealjs --mathjax="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" -o 2017-06-27-data-science-time-for-professionalisation.slides.html 2017-06-27-data-science-time-for-professionalisation.md
-->


### What is Machine Learning?

$$ \text{data} + \text{model} \rightarrow \text{prediction}$$

* Royal Society Report:
[Machine Learning: Power and Promise of Computers that Learn by Example](https://royalsociety.org/~/media/policy/projects/machine-learning/publications/machine-learning-report.pdf)

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

### "Embodiment Factors"

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

### Evolved Relationship {.slide: data-transition="none"}

<object type="image/svg+xml" data="./diagrams/data-science-information-flow_neg001.svg">
</object>

### Evolved Relationship {.slide: data-transition="none"}

<object type="image/svg+xml" data="./diagrams/data-science-information-flow_neg002.svg">
</object>

### Evolved Relationship {.slide: data-transition="none"}

<object type="image/svg+xml" data="./diagrams/data-science-information-flow_neg003.svg">
</object>

### What does Machine Learning do?

* We scale by codifying processes and automating them.

    * Ensure components are compatible (Whitworth threads)

    * Then interconnect them as efficiently as possible.

    * cf Colt 45, Ford Model T


### Codify Through Mathematical Functions 

* How does machine learning work?

* Jumper (jersey/sweater) purchase with logistic regression

$$ \text{odds} = \frac{\text{bought}}{\text{not bought}} $$

$$ \log \text{odds}  = \beta_0 + \beta_1 \text{age} + \beta_2 \text{latitude}$$


### Codify Through Mathematical Functions {.slide: data-transition="none"}

* How does machine learning work?

* Jumper (jersey/sweater) purchase with logistic regression

$$ p(\text{bought}) =  f\left(\beta_0 + \beta_1 \text{age} + \beta_2 \text{lattitude}\right)$$


### Codify Through Mathematical Functions {.slide: data-transition="none"}

* How does machine learning work?

* Jumper (jersey/sweater) purchase with logistic regression

$$ p(\text{bought}) =  f\left(\boldsymbol{\beta}^\top \mathbf{x}\right)$$


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

### The Software Crisis

>The major cause of the software crisis is that the machines have
>become several orders of magnitude more powerful! To put it quite
>bluntly: as long as there were no machines, programming was no problem
>at all; when we had a few weak computers, programming became a mild
>problem, and now we have gigantic computers, programming has become an
>equally gigantic problem.
>
> Edsger Dijkstra, The Humble Programmer

### The Data Crisis

>The major cause of the data crisis is that machines have become more
>interconnected than ever before. Data access is therefore cheap, but
>data quality is often poor. What we need is cheap high quality
>data. That implies that we develop processes for improving and
>verifying data quality that are efficient.
>
>There would seem to be two ways for improving efficiency. Firstly, we
>should not duplicate work. Secondly, where possible we should automate
>work. 
>
> Me

### Rest of this Talk: Two Areas of Focus {.slide: data-transition="none" }

* Reusability of Data

* Deployment of Machine Learning Systems

### Rest of this Talk: Two Areas of Focus {.slide: data-transition="none" }

* <s>Reusability of Data</s>

* Deployment of Machine Learning Systems

<!--\include{../_data-science/includes/data-readiness-levels.md}-->

### Artificial Intelligence

* Challenges in deploying AI.

* Currently this is in the form of "machine learning systems"

### Internet of People

* Fog computing: barrier between cloud and device blurring.

* Complex feedback between algorithm and implementation
  
### Deploying ML in Real World: Machine Learning Systems Design

* Major new challenge for systems designers.

* Internet of Intelligence but currently:

	* AI systems are *fragile*

\include{../_ai/includes/ml-systems-design-long.md}

### Conclusion

* Difference between Artificial Intelligence and Data Science are fundamentally different.

* In one you are dealing with data collected by happenstance.

* In the other you are trying to build systems in the real world, often by actively collecting data.

* Our approaches to systems design are building powerful machines that
will be deployed in evolving environments.


### Thanks!

* twitter: @lawrennd
* blog: [http://inverseprobability.com](http://inverseprobability.com/blog.html)
