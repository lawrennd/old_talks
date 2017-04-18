---
title: The Data Science Process
abstract: In this talk we will focus on challenges in facilitating the data science pipeline. Drawing on experience from projects in computational biology, the developing world and Amazon I’ll propose different ideas for facilitating the data science process including analogies that help software engineers understand the challenges for data science and formalizations, such as data readiness levels, which allow management to reason about the obstacles in the process.
published: 2017-04-18
venue: DALI Data Science Process Workshop
layout: slides
author: Neil D. Lawrence
affiliation: Amazon Research Cambridge and University of Sheffield
---

### DALI
### 2017-04-18
### Neil D. Lawrence
### Amazon Research Cambridge and University of Sheffield
```@lawrennd``` [inverseprobability.com](http://inverseprobability.com)
<!--  pandoc -s -S -c talks.css -t revealjs --mathjax="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" -o 2017-04-18-the-data-science-process.slides.html 2017-04-18-the-data-science-process.md
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


## "Embodiment Factors"

<table>
<tr><td></td><td align="center">
<img src="./diagrams/IBM_Blue_Gene_P_supercomputer.jpg" width="60%" style="background:none; border:none; box-shadow:none;" align="center">
</td>
<td align="center">
<img src="./diagrams/ClaudeShannon_MFO3807.jpg" width="100%" style="background:none; border:none; box-shadow:none;" align="center">
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


## Evolved Relationship 

<object type="image/svg+xml" data="./diagrams/data-science-information-flow_neg003.svg">
</object>


## Effects

* This phenomenon has already revolutionised biology.

* Large scale data acquisition and distribution.


## Challenges

1. Paradoxes of the Data Society

2. Quantifying the Value of Data

3. Privacy, loss of control, marginalisation

## Challenges {.slide: data-transition="none"}

1. ~~Paradoxes of the Data Society~~

2. Quantifying the Value of Data

3. ~~Privacy, loss of control, marginalisation~~

4. Why this could be very importan: Challenges in Deploying AI.


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


## Embodiment: [Data Readiness Levels](http://inverseprobability.com/2017/01/12/data-readiness-levels)

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
* At the end of Band C data is ready to be loaded into analysis software (R, SPSS, Matlab, Python, Mathematica)

## Validity: Band B

*  faithfulness and representation
* visualisations.
* noise characterisation.
* Missing values.
* Example, was a column or columns accidentally perturbed (e.g. through a sort operation that missed one or more columns)? Or was a [gene name accidentally converted to a date](http://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-5-80)?
* At the end of Band B, ready to define a candidate question, the context.

## Usability: Band A

* The usability of data
* Band A is about data in context.
* Consider appropriateness of a given data set to answer a particular
question or to be subject to a particular analysis.
* At the end of Band A it's ready for RAMP, Kaggle, etc

## Recursive Effects

* Band A may also require
    * active collection of new data. 
    * annotation of data by human experts
    * revisiting the collection (and running through the appropriate stages again)

## Also ...

* Encourage greater interaction between application domains and data scientists

* Encourage *visualization* of data

* Incentivise the delivery of data.

* Analogies: For SDEs [describe data science as *debugging*](http://inverseprobability.com/2017/03/14/data-science-as-debugging).

## See Also ...

* Data Joel Tests
    * [proposal by Damon Civin](https://medium.com/@damoncivin/the-joel-test-for-data-readiness-4882aae64753) and
    * [proposal by Nick Elprin](https://blog.dominodatalab.com/joel-test-data-science/)


## Internet of People

* Fog computing: barrier between cloud and device blurring.

* Stuxnet: Adversarial and Security implications for intelligent systems.

* Complex feedback between algorithm and implementation
  
## Deploying ML in Real World: Machine Learning Systems Design

* Major new challenge for systems designers.

* Internet of Intelligence but currently:

	* AI systems are currently *fragile*

## Fragility of AI Systems

* They are componentwise built from ML Capabilities.

* Each capability is independently constructed and verified.

   * Pedestrian detection
   * Road line detection

* Important for verification purposes.

## Rapid Reimplementation

* Whole systems are being deployed.

* But they change their environment.

* The experience evolved adversarial behaviour.

## Machine Learning Systems Design

<img src="./diagrams/SteamEngine_Boulton&Watt_1784_neg.png" width="50%" style="border:none">

## Turnaround And Update

* There is a massive need for turn around and update

* A redeploy of the entire system.
     *  This involves changing the way we design and deploy.

* Interface between security engineering and machine learning.

## Conclusion

* Data science offers a great deal of promise.
* There are challenges and pitfalls
* It is incumbent on us to avoid them

**Many solutions rely on education and awareness**

* There are particular challenges around the Internet of Intelligence. 

## Thanks!

* twitter: @lawrennd
* blog: [http://inverseprobability.com](http://inverseprobability.com/blog.html)
