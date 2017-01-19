---
abstract: In this talk we will introduce deep Gaussian process (GP) models. Deep GPs
  are a deep belief network based on Gaussian process mappings. The data is modeled
  as the output of a multivariate GP. The inputs to that Gaussian process are then
  governed by another GP. A single layer model is equivalent to a standard GP or the
  GP latent variable model (GPLVM). We perform inference in the model by approximate
  variational marginalization. This results in a strict lower bound on the marginal
  likelihood of the model which we use for model selection (number of layers and nodes
  per layer). Deep belief networks are typically applied to relatively large data
  sets using stochastic gradient descent for optimization. Our fully Bayesian treatment
  allows for the application of deep models even when data is scarce. Model selection
  by our variational bound shows that a five layer hierarchy is justified even when
  modelling a digit data set containing only 150 examples. In the seminar we will
  briefly review dimensionality reduction via Gaussian processes, before showing how
  this framework can be extended to build deep models.
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
categories:
- Lawrence-ncaf13
day: '4'
errata: []
extras: []
key: Lawrence-ncaf13
layout: talk
linkpdf: ftp://ftp.dcs.shef.ac.uk/home/neil/gplvm_ncaf13.pdf
month: 7
published: 2013-07-04
section: pre
title: Deep <span>Gaussian</span> Processes
venue: Natural Computing Applications Forum, University of Oxford
year: '2013'
---