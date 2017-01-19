---
layout: slides
title: "Computational Perspectives: Fairness and Awareness in Data Analysis"
author: Neil D. Lawrence
---

## Computational Perspectives: Fairness and Awareness in Data Analysis
### Royal Statistical Society
### 2016-10-27
### London, UK
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


## Background: Big Data

* Data is Pervasive phenomenon that affects all aspects of our activities

* Data diffusiveness is both a challenge and an opportunity



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


## Effects

* This phenomenon has already revolutionised biology.

* Large scale data acquisition and distribution.

* Transcriptomics, genomics, epigenomics, 'rich phenomics'.


## Societal Effects

* Automated decision making within the computer based only on the data.

* A requirement to better understand our own subjective biases to ensure that the human to computer interface formulates the correct conclusions from the data.



## Societal Effects

* Shift in dynamic from the direct pathway between human and data to indirect pathway between human and data via the computer

* This change of dynamics gives us the modern and emerging domain of data science


## Challenges

1. Paradoxes of the Data Society

2. Quantifying the Value of Data

3. Privacy, loss of control, marginalization


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

$$ \mathbf{Y} = \begin{bmatrix}
y_{1, 1} & y_{1, 2} &\dots & y_{1,p}\\
y_{2, 1} & y_{2, 2} &\dots & y_{2,p}\\
\vdots & \vdots &\dots & \vdots\\
y_{n, 1} & y_{n, 2} &\dots & y_{n,p}
\end{bmatrix} \in \Re^{n\times p}
$$

## General index on $y$

$$y_\mathbf{x}$$

where $\mathbf{x}$ might include time, spatial location ...

Streaming data. Joint model of past, $\mathbf{y}$ and future $\mathbf{y}_*$

$$p(\mathbf{y}, \mathbf{y}_*)$$

Prediction through: 

$$p(\mathbf{y}_*|\mathbf{y})$$


## Kolmogorov Consistency

* From the sum rule of probability we have
\begin{align*}
p(\mathbf{y}|n^*) = \int p(\mathbf{y}, \mathbf{y}^*) \text{d}\mathbf{y}^*
\end{align*}
$n^*$ is length of $\mathbf{y}^*$.

* Consistent if $p(\mathbf{y}|n^*) = p(\mathbf{y})$

* Prediction then given by product rule
\begin{align*}
p(\mathbf{y}^*|\mathbf{y}) = \frac{p(\mathbf{y}, \mathbf{y}^*)}{p(\mathbf{y})}
\end{align*}

## $p(\mathbf{y}^*|\mathbf{y})$

<!-- where the dependence of the marginal distribution for $\mathbf{y}$ aries from the fact that we are forming an $n^*$ dimensional integral over $\mathbf{y}^*$. If our distribution is Kolmogorov consistent, then we know that the distribution over $\mathbf{y}$ is *independent* of the value of $n^*$. So in other words $p(\mathbf{y}|n*)=p(\mathbf{y})$. So Kolmogorov consistency says that the form of $p(\mathbf{y})$ remains the same *regardless* of the number of observations of the world that are yet to come.  -->

## Parametric Models

* Kolmogorov consistency trivial in parametric model.
\begin{align*}
p(\mathbf{y}, \mathbf{y}^*) = \int \prod_{i=1}^n p(y_{i} | \boldsymbol{\theta})\prod_{i=1}^{n^*}p(y^*_i|\boldsymbol{\theta}) p(\boldsymbol{\theta}) \text{d}\boldsymbol{\theta}
\end{align*}

* Marginalizing
\begin{align*}
p(\mathbf{y}) = \int \prod_{i=1}^n p(y_{i} | \boldsymbol{\theta})\prod_{i=1}^{n^*} \int p(y^*_i|\boldsymbol{\theta}) \text{d}y^*_i p(\boldsymbol{\theta}) \text{d}\boldsymbol{\theta}
\end{align*}


## Parametric Bottleneck

* Bayesian methods suggest a prior over $\boldsymbol{\theta}$ and use posterior, $p(\boldsymbol{\theta}|\mathbf{y})$ for making predictions.
\begin{align*}
p(\mathbf{y}^*|\mathbf{y}) = \int \prod_i p(y_i^* | \boldsymbol{\theta}) p(\boldsymbol{\theta}|\mathbf{y})\text{d}\boldsymbol{\theta} 
\end{align*}

* Design time problem: *parametric bottleneck*. 
$$p(\boldsymbol{\theta} | \mathbf{y})$$

* Streaming data could turn out to be more complex than we imagine.

## Finite Storage

* Despite our large interconnected brains, we only have finite storage. 

* Similar for digital computers. So we need to assume that we can only store a finite number of things about the data $\mathbf{y}$. 

* This pushes us back towards *parametric* models. 

## Inducing Variables

* Choose to go a different way. 

* Introduce a set of auxiliary variables, $\mathbf{u}$, which are $m$ in length. 

* They are like "artificial data".

* Used to *induce* a distribution: $q(\mathbf{u}|\mathbf{y})$ 

## Making Parameters non-Parametric

* Introduce variable set which is *finite* dimensional. 
$$
p(\mathbf{y}^*|\mathbf{y}) \approx \int p(\mathbf{y}^*|\mathbf{u}) q(\mathbf{u}|\mathbf{y}) \text{d}\mathbf{u}
$$

* But dimensionality of $\mathbf{u}$ can be changed to improve approximation.

## Variational Compression {.slide: data-transition="none"}

* Model for our data, $\mathbf{y}$

$$p(\mathbf{y})$$
<br><object type="image/svg+xml" data="./diagrams/py.svg">
</object>

## Variational Compression {.slide: data-transition="none"}

* Prior density over $\mathbf{f}$. Likelihood relates data, $\mathbf{y}$, to $\mathbf{f}$.

$$p(\mathbf{y})=\int p(\mathbf{y}|\mathbf{f})p(\mathbf{f})\text{d}\mathbf{f}$$<br>
<object type="image/svg+xml" data="./diagrams/pygfpf.svg">
</object>

## Variational Compression {.slide: data-transition="none"}

* Prior density over $\mathbf{f}$. Likelihood relates data, $\mathbf{y}$, to $\mathbf{f}$.

$$p(\mathbf{y})=\int p(\mathbf{y}|\mathbf{f})p(\mathbf{u}|\mathbf{f})p(\mathbf{f})\text{d}\mathbf{f}\text{d}\mathbf{u}$$<br>
<object type="image/svg+xml" data="./diagrams/pygfpugfpf.svg">
</object></td></tr>
</table>

## Variational Compression {.slide: data-transition="none"}

$$p(\mathbf{y})=\int \int p(\mathbf{y}|\mathbf{f})p(\mathbf{f}|\mathbf{u})\text{d}\mathbf{f}p(\mathbf{u})\text{d}\mathbf{u}$$
<br><object type="image/svg+xml" data="./diagrams/pygfpfgupu.svg">
</object>

## Variational Compression {.slide: data-transition="none"}

$$p(\mathbf{y})=\int \int p(\mathbf{y}|\mathbf{f})p(\mathbf{f}|\mathbf{u})\text{d}\mathbf{f}p(\mathbf{u})\text{d}\mathbf{u}$$<br>
<object type="image/svg+xml" data="./diagrams/pygfpfgupu2.svg">
</object>

## Variational Compression {.slide: data-transition="none"}

$$p(\mathbf{y}|\mathbf{u})=\int p(\mathbf{y}|\mathbf{f})p(\mathbf{f}|\mathbf{u})\text{d}\mathbf{f}$$<br>
<object type="image/svg+xml" data="./diagrams/pygfpfgu.svg">
</object>

## Variational Compression {.slide: data-transition="none"}

$$p(\mathbf{y}|\mathbf{u})$$<br>
<object type="image/svg+xml" data="./diagrams/pygu.svg">
</object>

## Variational Compression {.slide: data-transition="none"}

$$p(\mathbf{y}|\boldsymbol{\theta})$$<br>
<object type="image/svg+xml" data="./diagrams/pygtheta.svg">
</object>

## Compression

* Replace true $p(\mathbf{u}|\mathbf{y})$ with approximation $q(\mathbf{u}|\mathbf{y})$.

* Minimize KL divergence between approximation and truth.

* This is similar to the Bayesian posterior distribution.

* But it's placed over a set of 'pseudo-observations'.

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


## Value

* How do we measure value in the data economy?
* How do we encourage data workers: curation and management
  * Incentivization
  * Quantifying the value in their contribution


## {.slide: data-transition="none"}

<object type="image/svg+xml" data="./diagrams/pomdp001.svg">
</object>

## {.slide: data-transition="none"}

<object type="image/svg+xml" data="./diagrams/pomdp002.svg">
</object>

## {.slide: data-transition="none"}

<object type="image/svg+xml" data="./diagrams/pomdp003.svg">
</object>

## {.slide: data-transition="none"}

<object type="image/svg+xml" data="./diagrams/pomdp004.svg">
</object>


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


## Conversation {.slide: data-transition="none"}

<object type="image/svg+xml" data="./diagrams/anne_bob001.svg">
</object>

## Conversation {.slide: data-transition="none"}

<object type="image/svg+xml" data="./diagrams/anne_bob002.svg">
</object>

## Conversation {.slide: data-transition="none"}

<object type="image/svg+xml" data="./diagrams/anne_bob003.svg">
</object>

## Modelling

<object type="image/svg+xml" data="./diagrams/anne.svg">
</object>

## Modelling

<object type="image/svg+xml" data="./diagrams/bob.svg">
</object>


## Hate Speech or Political Dissent?

* social media monitoring for 'hate speech' can be easily turned to political dissent monitoring


## Marketing

* can become more sinister when the target of the marketing is well understood and the (digital) environment of the target is also so well controlled


## Free Will

*  What does it mean if a computer can predict our individual behavior better than we ourselves can?


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

## Awareness

* Need to increase awareness of the pitfalls among researchers
* Need to ensure that technological solutions are being delivered not merely for few (#FirstWorldProblems)
* Address a wider set of challenges that the greater part of the world's population is facing


## Conclusion

* Data science offers a great deal of promise
* There are challenges and pitfalls
* It is incumbent on us to avoid them
* Need new ways of thinking! 
* *Mathematical* Data Science

**Many solutions rely on education and awareness**


## Thanks!

* twitter: @lawrennd
* blog: [http://inverseprobability.com](http://inverseprobability.com/blog.html)
