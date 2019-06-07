---
title: Peppercorns and Machine Learning System Design
abstract: >
  Machine learning is fundamental to two important
  technological domains, artificial intelligence and data science. In
  this talk we will attempt to make a simple definition to distinguish
  between the two, then we will focus on the challenges of machine
  learning in *application* to artificial intelligence particularly from 
  the perspective of systems design. We expect a particular challenge to 
  be the deployment of such systems in real environment, where 
  unforeseen consequences of interaction with real world environments
  will produce embarrassing failures. Because these failures are not
  bugs, in that the system will be performing as designed, but
  failures of imagination of the designers we introduce a new term for
  them: "peppercorns". 
published: 2017-06-02
venue: Sheffield ML Research Retreat
layout: slides
author: Neil D. Lawrence
affiliation: Amazon Research Cambridge and University of Sheffield
---

### Peppercorns and Machine Learning System Design
### 2017-06-02
### Neil D. Lawrence
### Amazon Research Cambridge and University of Sheffield
```@lawrennd``` [inverseprobability.com](http://inverseprobability.com)
<!--  pandoc -s -S -c talks.css -t revealjs --mathjax="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" -o 2017-06-02-peppercorns-and-machine-learning-system-design.md.slides.html 2017-06-02-peppercorns-and-machine-learning-system-design.md.md
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

## Data Science and Artificial Intelligence {.slide: data-transition="none"}

* Data Science: arises from the fact that we now capture data by happenstance.

* Artificial intelligence: emulation of human behaviour.

* Data acquisition: Internet of Things

## Data Science and Artificial Intelligence {.slide: data-transition="none"}

* Arise from the fact that we now capture data by happenstance.

* Artificial intelligence: emulation of human behaviour.

* Data preprocessing: __Internet of Things__

## Data Science and Artificial Intelligence {.slide: data-transition="none"}

* Arise from the fact that we now capture data by happenstance.

* Artificial intelligence: emulation of human behaviour.

* Data acquisition: Internet of People


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

## Peppercorns

* A new name for system failures which aren't bugs.

* Difference between finding a fly in your soup vs a peppercorn in
  your soup. 

## Conclusion

* Difference between Artificial Intelligence and Data Science are fundamentally different.

* In one you are dealing with data collected by happenstance.

* In the other you are trying to build systems in the real world, often by actively collecting data.

* Our approaches to systems design are building powerful machines that 
**Many solutions rely on education and awareness**

* There are particular challenges around the Internet of Intelligence. 

## Thanks!

* twitter: @lawrennd
* blog: [http://inverseprobability.com](http://inverseprobability.com/blog.html)
