---
title: "The Data Landscape"
author: Neil D. Lawrence
date: 2016-12-15
venue: "Defra Science Advisory Council: Data Sub Group"
layout: slides
---

### Defra Science Advisory Council
### 2016-12-15
### Nobel House, London
### Neil D. Lawrence
### Amazon and University of Sheffield
```@lawrennd``` [inverseprobability.com](http://inverseprobability.com)
<!--  pandoc -s -S -c talks.css -t revealjs --mathjax="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" -o 2016-10-27-computational-perspectives-fairness-and-awareness-in-the-analysis-of-data.slides.html 2016-10-27-computational-perspectives-fairness-and-awareness-in-the-analysis-of-data.md
-->


## {.slide: data-transition="none"}

> There are three types of lies: lies, damned lies and statistics
>
> ??

## {.slide: data-transition="none"}


> There are three types of lies: lies, damned lies and statistics
>
> Benjamin Disraeli

## {.slide: data-transition="none"}

> There are three types of lies: lies, damned lies and statistics
>
> Benjamin Disraeli 1804-1881


## *Mathematical* Statistics

* 'Founded' by Karl Pearson (1857-1936)

<img src="./diagrams/Portrait_of_Karl_Pearson.jpg" align="center" width="30%" style="background:none; border:none; box-shadow:none;">

## {.slide: data-transition="none"}

> There are three types of lies: lies, damned lies and 'big data'
>
> Neil Lawrence 1972-?


## 'Mathematical Data Science'

* 'Founded' by ? (?-?)

<img src="./diagrams/Question_mark.png" align="center" width="30%" style="background:none; border:none; box-shadow:none;">

## Today

* Challenges of understanding and interpreting big data today are similar to those that Disraeli faced in with statistics in latter part of the 19th century. 

* Data is elusive: it can promise much but deliver little.



## Stetson Hats

* What's the most common hat worn in the west?
<center>
<table>
<tr><td><img src="./diagrams/bowler.jpg" width="70%"></td><td><img src="./diagrams/stetson.jpg" width="70%"></td></tr>
</table>
<center>

## The Three 'A's

* Data Awareness

* Data Availability

* Data Analysis

## Data Awareness

* What data you have and where its stored. 

* May need to chance *conception* of what data is and how to obtain it.

* Production lines, smart phones.

* Locked away: manual log books, *confidential* data, *personal* data. 

* An internal audit (you are ahead here!).

* The key to any successful campaign is a good map. 

## Data Availability 

* How well are the data sources interconnected? 

* How well curated are they? 

* Curse of Disraeli was associated with unreliable data and *unreliable statistics*. 

* Misrepresentation is worse than absence of data.

* Need an improved sense of data and its value.

## Data Analysis

* accumulation of the necessary expertise to digest what the data tells us. 

* data requires intepretation, and interpretation requires experience. 

* Analysis is a bottleneck due to a skill shortage.

* Ideally, analysis should be carried out by individuals not only skilled in data science but also equipped with the domain knowledge.


## Evolved Relationship {.slide: data-transition="none"}

<object type="image/svg+xml" data="./diagrams/data-science-information-flow_neg001.svg">
</object>

## Evolved Relationship {.slide: data-transition="none"}

<object type="image/svg+xml" data="./diagrams/data-science-information-flow_neg002.svg">
</object>

## Evolved Relationship {.slide: data-transition="none"}

<object type="image/svg+xml" data="./diagrams/data-science-information-flow_neg003.svg">
</object>

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
<td>communicate</td><td align="center">~1 gigbit/s</td><td align="center">~ 100 bit/s</tr>
<td>embodiment<br>(compute/communicate)</td><td align="center">10</td><td align="center">~ 10<sup>13</sup></tr>
</table>


## Evolved Relationship 

<object type="image/svg+xml" data="./diagrams/data-science-information-flow_neg003.svg">
</object>

## Societal Effects

* Automated decision making in the computer based  on data.

* Need to better understand our own subjective biases better.

* Particularly important where societal interventions are prescribed.

* But what is a societal intervention in the modern era? Much more subtle than before.

## Societal Effects

* Shift in dynamic from the direct pathway between human and data to indirect pathway between human and data via the computer

* This change of dynamics gives us the modern and emerging domain of data science


## Societal Challenges

1. Paradoxes of the Data Society

2. Quantifying the Value of Data

3. Privacy, Transparency, Fairness, Equality


## Challenge 1) Breadth vs Depth Paradox

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

## Also need

* More classical statistics!
    * Like the 'paperless office'

* A better characterization of human (see later)

* Larger studies (100,000 genome)
    * Combined with complex models: algorithmic challenges

## Challenge 2) Quantifying the Value of Data

There's a sea of data, but most of it is undrinkable

<img src="./diagrams/sea-water-ocean-waves.jpg" width="50%">

We require data-desalination before it can be consumed!


## Value

* How do we measure value in the data economy?
* How do we encourage data workers: curation and management
  * Incentivization for sharing and production.
  * Quantifying the value in the contribution of *each actor*.


## Credit Allocation

* Direct work on data generates an enormous amount of 'value' in the data economy but this is unaccounted in the economy

* Hard because data is difficult to 'embody'

* Value of shared data: [Wellcome Trust 2010 Joint Statement](https://wellcome.ac.uk/what-we-do/our-work/sharing-research-data-improve-public-health-full-joint-statement-funders-health) (from the "Foggy Bottom" meeting)

## Solutions

* Encourage greater interaction between application domains and data scientists

* Encourage visualization of data

* Adoption of 'data readiness levels'

* Implications for incentivization schemes


## Privacy, Loss of Control and Marginalization

* Society is becoming harder to monitor

* Individual is becoming easier to monitor

* What does it mean if a computer can predict us better than we can ourselves?


## Discrimination

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

## Societal Challenges

* Paradoxes of the Data Society

* Quantifying the value in the Data

* Privacy, Transparency, Fairness, Equality


## Solutions

* Software: TensorFlow, scikit-learn (python), R, Spark.

* Education

* Automating the Data Science Pipeline:
  * The Automatic Statistician
  * AutoML

## Conclusion

* Alone 'big data' promises much and delivers little.

* Data needs to be cared for: it needs to be curated and evaluated. 

* Thee stages: 
  1. Awareness
  2. Availability
  3. Analysis 
  
## Conclusion (2)  
  
* Hand waving about big data solutions leads to self-deception. 

* The castles we build on our data landscapes must be based on firm foundations.


## Thanks!

* twitter: @lawrennd
* blog: [http://inverseprobability.com](http://inverseprobability.com/blog.html)
