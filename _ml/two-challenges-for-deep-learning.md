---
layout: slides
title: Two Challenges for Deep Learning
venue: Deep Probabilistic Models Workshop, Cambridge
author: Neil D. Lawrence
abstract: >
  In this talk we consider two challenges for the field of deep learning. 
date: 2017-09-15
affiliation: Amazon and University of Sheffield
---

\include{../talk-macros.tex}

### Introduction

* Promise of deep learning: automated abstraction.

* Layered models


### Challenges for Deep Learning

1. Massively Missing Data: Dealing with Unknown Uknowns

2. Assimilation of Data at Different Levels of Abstraction


### Prediction is Probability {data-transition="None"}

<large>$$p(\dataVector)$$</large>

$\dataVector$ is *known* data

### Prediction is Probability {data-transition="None"}

<large>$$p(\dataVector_*, \dataVector)$$</large>

$\dataVector_*$ is *unknown* data

### Prediction is Probability {data-transition="None"}

<large>$$p(\dataVector_* | \dataVector)$$</large>

$\dataVector_*$ is *unknown* data

### How to solve [AlphaGo](https://en.wikipedia.org/wiki/AlphaGo_versus_Lee_Sedol)

$\dataScalar_{t=?, \text{action}=\text{beat world champion}} = \texttt{true}$

$\dataScalar_{t=2010/09/23, \text{action} = \text{start new company}} = ?$


### How to solve [AlphaGo](https://en.wikipedia.org/wiki/AlphaGo_versus_Lee_Sedol)

$\dataScalar_{t=?, \text{action}=\text{solve artificial intelligence}} = \texttt{true}$

$\dataScalar_{t=2010/09/23, \text{action}=\text{start new company}} = ?$


### If you want to solve General AI

* Define your goal

* Don't go directly for your goal

    * Explore/Exploit trade offs

### All $y$ in between

* Integrate over all actions *including* unknown unknowns.

* Implies some form of *non-parametrics*.

### Non parametrics {data-transition="None"}

$$ p(\dataVector_* | \dataVector) = \frac{p(\dataVector_*, \dataVector)}{p(\dataVector)}$$

### Non parametrics {data-transition="None"}

$$ p(\dataVector) = \int p(\dataVector_*, \dataVector) \text{d} \dataVector_*$$

marginalize the known unknowns

### Non parametrics {data-transition="None"}

$$ p(\dataVector_*, \dataVector) = \int p(\dataVector_* |\weightVector) p(\dataVector|\weightVector) p(\weightVector) \text{d} \weightVector$$

This is parametric approach

### Non parametrics {data-transition="None"}

$$ p(\dataVector_* | \dataVector) = \int p(\dataVector_* | \weightVector) p(\weightVector |\dataVector) \text{d} \weightVector$$

This is parametric approach

### Unknown Unknowns

* Now need to define $p(\dataVector_*|\weightVector)$ for *unknown* unknowns at design time.

$$p_{\mathcal{A}*}(\dataVector) = \int p(\dataVector_{\mathcal{A}*}, \dataVector) \text{d}\dataVector_{\mathcal{A}*}$$

Need $$p_{\mathcal{A}*}(\dataVector) = p(\dataVector)$$

### Models Must Be

* Non Parametric

### Models Must Be *Deep*


