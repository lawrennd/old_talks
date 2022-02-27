---
title: Two Challenges for Deep Learning
venue: Deep Probabilistic Models Workshop, Cambridge
author: Neil D. Lawrence
abstract: |
  In this talk we consider two challenges for the field of deep learning. 
date: 2017-09-15
transition: None
categories:
- Lawrence-deepchallenges17
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: Amazon Cambridge and University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
transition: None
incremental: True
---

talk-macros.gpp}lk-macros.gpp}

\section{Introduction}

\newslide{Introduction}

* Promise of deep learning: automated abstraction.

* Layered models


\subsection{Challenges for Deep Learning}

1. Massively Missing Data: Dealing with Unknown Unknowns

2. Assimilation of Data at Different Levels of Abstraction


\subsection{Prediction is Probability}

<large>$$p(\dataVector)$$</large>

$\dataVector$ is *known* data

\newslide{Prediction is Probability}

<large>$$p(\dataVector_*, \dataVector)$$</large>

$\dataVector_*$ is *unknown* data

\newslide{Prediction is Probability}

<large>$$p(\dataVector_* | \dataVector)$$</large>

$\dataVector_*$ is *unknown* data

\subsection{How to solve [AlphaGo](https://en.wikipedia.org/wiki/AlphaGo_versus_Lee_Sedol)}

$\dataScalar_{t=?, \text{action}=\text{beat world champion}} = \texttt{true}$

$\dataScalar_{t=2010/09/23, \text{action} = \text{start new company}} = ?$


\newslide{How to solve [AlphaGo](https://en.wikipedia.org/wiki/AlphaGo_versus_Lee_Sedol)}

$\dataScalar_{t=?, \text{action}=\text{solve artificial intelligence}} = \texttt{true}$

$\dataScalar_{t=2010/09/23, \text{action}=\text{start new company}} = ?$


\subsection{If you want to solve General AI}

* Define your goal

* Don't go directly for your goal

    * Explore/Exploit trade offs

\newslide{All $y$ in between}

* Integrate over all actions *including* unknown unknowns.

* Implies some form of *non-parametrics*.

\subsection{Non parametrics}

$$ p(\dataVector_* | \dataVector) = \frac{p(\dataVector_*, \dataVector)}{p(\dataVector)}$$

\newslide{Non parametrics}

$$ p(\dataVector) = \int p(\dataVector_*, \dataVector) \text{d} \dataVector_*$$

marginalize the known unknowns

\newslide{Non parametrics}

$$ p(\dataVector_*, \dataVector) = \int p(\dataVector_* |\weightVector) p(\dataVector|\weightVector) p(\weightVector) \text{d} \weightVector$$

This is parametric approach

\newslide{Non parametrics}

$$ p(\dataVector_* | \dataVector) = \int p(\dataVector_* | \weightVector) p(\weightVector |\dataVector) \text{d} \weightVector$$

This is parametric approach

\newslide{Unknown Unknowns}

* Now need to define $p(\dataVector_*|\weightVector)$ for *unknown* unknowns at design time.

$$p_{\mathcal{A}*}(\dataVector) = \int p(\dataVector_{\mathcal{A}*}, \dataVector) \text{d}\dataVector_{\mathcal{A}*}$$

Need $$p_{\mathcal{A}*}(\dataVector) = p(\dataVector)$$

\newslide{Models Must Be}

* Non Parametric

\newslide{Models Must Be *Deep*}

\thanks

\references
