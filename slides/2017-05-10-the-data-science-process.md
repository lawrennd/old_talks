---
title: The Data Science Process
abstract: In this talk we will focus on challenges in facilitating the data science pipeline. Drawing on experience from projects in computational biology, the developing world and Amazon I’ll propose different ideas for facilitating the data science process including analogies that help software engineers understand the challenges for data science and formalizations, such as data readiness levels, which allow management to reason about the obstacles in the process.
published: 2017-05-10
venue: AMLC Data Science Process Workshop, Seattle
layout: slides
author: Neil D. Lawrence
affiliation: Amazon Research Cambridge and University of Sheffield
---

### AMLC Data Science Workshop Address
### 2017-05-10
### Neil D. Lawrence
### Amazon Research Cambridge and University of Sheffield
```@lawrennd``` [inverseprobability.com](http://inverseprobability.com)
<!--  pandoc -s -S -c talks.css -t revealjs --mathjax="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" -o 2017-05-10-the-data-science-process.slides.html 2017-05-10-the-data-science-process.md
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


## Challenges

1. Paradoxes of the Data Society

2. Quantifying the Value of Data

3. Privacy, loss of control, marginalisation

## Challenges {.slide: data-transition="none"}

1. Paradoxes of the Data Society

2. Quantifying the Value of Data

3. ~~Privacy, loss of control, marginalisation~~

4. Machine Learning Systems Design


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

* Clinical trial and personalized medicine

* Social media memes

* Filter bubbles and echo chambers


## The Maths {.slide: data-transition="none"}

$$ \mathbf{Y} = \begin{bmatrix}
y_{1, 1} & y_{1, 2} &\dots & y_{1,p}\\
y_{2, 1} & y_{2, 2} &\dots & y_{2,p}\\
\vdots & \vdots &\dots & \vdots\\
y_{n, 1} & y_{n, 2} &\dots & y_{n,p}
\end{bmatrix} \in \Re^{n\times p}
$$

## The Maths {.slide: data-transition="none"}

$$ \mathbf{Y} = \begin{bmatrix}
\mathbf{y}^\top_{1, :} \\
\mathbf{y}^\top_{2, :} \\
\vdots \\
\mathbf{y}^\top_{n, :}
\end{bmatrix} \in \Re^{n\times p}
$$

## The Maths {.slide: data-transition="none"}

$$ \mathbf{Y} = \begin{bmatrix}
\mathbf{y}_{:, 1} &
\mathbf{y}_{:, 2} &
\dots &
\mathbf{y}_{:, p}
\end{bmatrix} \in \Re^{n\times p}
$$


<!-- This is the nature of modern streaming data, what has been called big data, although in the UK it looks like that term will gain a more diffuse meaning now that the government has associated a putative 189 billion pounds of funding to it. But the characteristic of massive missing data is particularly obvious when we look at clinical domains. EMIS, a Yorkshire based provider of software to General Practitioners, has 39 million patient records. When we consider clinical measurements, we need to build models that not only take into account all current clinical tests, but all tests that will be invented in the future. This leads to the idea of massive missing data. The classical statistical table of data is merely the special case where someone has filled in a block of information.  -->

<!-- To deal with massively missing data we need to think about the *Kolmogorov consistency* of a process. Let me introduce Kolmogorov consistency by way of an example heard from Tony O'Hagan, but one that he credits originally to Michael Goldstein. Imagine you are on jury duty. You are asked to adjudicate on the guilt or innocence of Lord Safebury, and you are going to base your judgement on a model that is weighing all the evidence. You are just about to pronounce your decision when a maid comes running in and shouts "He didn't do it! He didn't do it!". The maid wasn't on the witness list and isn't accounted for in your model. How does this effect your inference? The pragmatists answer might be: not at all, because the maid wasn't in the model. But in the interests of justice we might want to include this information in our inference process. If, as a result of the maid's entry, we now think it is less likely that Lord Safebury committed the crime, then necessarily every time that the (unannounced) maid doesn't enter the room we have to assume that it is more likely that Safebury commited the crime (to ensure that the conditional probability of guilt given the maid's evidence normalizes. But we didn't know about the maid, so how can we account for this? Further, how can we account for all possible other surprise evidence, from the announced butlers, gardners, chauffeurs and footmen? Kolmogorov consistency (@Kolmogorov:grundbegriffe33) says that the net effect of marginalizing for all these potential bits of new information is null. It is a particular property of the model. Making it (only slightly) more formal, we can consider Kolmogorov consistency as a marginalization property of the model. We take the $n$ dimensional vector, $\mathbf{y}$, to be an (indexed) vector of all our instantiated observations of the world that we have *at the current time*. Then we take the $n^*$ dimensional vector, $\mathbf{y}^*$ to be the observations of the world that we are *yet to see*. --> 

## The Maths {.slide: data-transition="none"}

$$p(\mathbf{Y}|\boldsymbol{\theta}) = \prod_{i=1}^n p(\mathbf{y}_{i, :}|\boldsymbol{\theta})$$


## The Maths {.slide: data-transition="none"}

$$p(\mathbf{Y}|\boldsymbol{\theta}) = \prod_{i=1}^n p(\mathbf{y}_{i, :}|\boldsymbol{\theta})$$

$$\log p(\mathbf{Y}|\boldsymbol{\theta}) = \sum_{i=1}^n \log p(\mathbf{y}_{i, :}|\boldsymbol{\theta})$$

## Consistency

* Typically $\boldsymbol{\theta} \in \Re^{\mathcal{O}(p)}$

* Consistency reliant on large sample approximation of KL divergence

$$ \text{KL}(P(\mathbf{Y})|| p(\mathbf{Y}|\boldsymbol{\theta}))$$

* Minimization is equivalent to maximization of likelihood.

* A foundation stone of classical statistics.

## Large $p$

* For large $p$ the parameters are badly determined.

* Large $p$ small $n$ problem.

* Easily dealt with through definition.

## The Maths {.slide: data-transition="none"}

$$p(\mathbf{Y}|\boldsymbol{\theta}) = \prod_{j=1}^p p(\mathbf{y}_{:, j}|\boldsymbol{\theta})$$

$$\log p(\mathbf{Y}|\boldsymbol{\theta}) = \sum_{j=1}^p \log p(\mathbf{y}_{:, j}|\boldsymbol{\theta})$$

## Breadth vs Depth

* Modern Measurement deals with *depth* (many subjects)
    ... or *breadth* lots of detail about subject.
	
* But what about 
    * $p\approx n$?
    * Stratification of populations: batch effects etc.

## Does $p$ Even Exist?

* Massively missing data.

* Classical bias towards tables.

* Streaming data.

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

## Quotes from Today

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


## Accessibility: Band C

* Hearsay data.
* Availability, is it actually being recorded?
* privacy or legal constraints on the accessibility of the recorded data, have ethical constraints been alleviated?
* Format: log books, PDF ...
* limitations on access due to topology (e.g. it's distributed across a number of devices)
* At the end of Band C data is ready to be loaded into analysis software (R, SPSS, Matlab, Python, Mathematica)

## Validity: Band B

* faithfulness and representation
* visualisations.
* exploratory data analysis
* noise characterisation.
* Missing values.
* Schema alignment, record linkage, data fusion? (Luna's talk)
* Example, was a column or columns accidentally perturbed (e.g. through a sort operation that missed one or more columns)? Or was a [gene name accidentally converted to a date](http://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-5-80)?
* At the end of Band B, ready to define a candidate question, the
  context, load into OpenML

## Usability: Band A

* The usability of data
* Band A is about data in context.
* Consider appropriateness of a given data set to answer a particular
question or to be subject to a particular analysis.
* Greg's talk, Enrica's talk, data integration?
* At the end of Band A it's ready for RAMP, Kaggle, define a *task* in OpenML.

## Recursive Effects

* Band A may also require

    * active collection of new data. 

	* annotation of data by human experts (Enrica)

	* revisiting the collection (and running through the appropriate stages again)

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
