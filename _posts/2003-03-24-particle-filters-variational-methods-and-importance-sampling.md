---
title: Particle Filters, Variational methods and Importance Sampling
abstract: 'Particle filters allow tracking of systems with highly non-linear, multi-modal
  posterior distributions, however they are prone to failure when model likelihoods
  are sharply peaked or state spaces are high dimensional. This failure is caused
  by a mismatch between the proposal distribution and the true posterior. The number
  of particles of samples then required to accurately represent the posterior increases
  dramatically and with it the computational demands of the algorithm. By formulating
  the problem within the framework of variational inference we derive an algorithm
  in which the proposal naturally adapts to more accurately reflect the true posterior.
  This is achieved by replacing intractable moment evaluations, arising from the highly
  non-linear nature of the likelihood functions, with sample based approximations.
  In this talk we shall first introduce the approach in a static setting: Bayesian
  processing of cDNA microarray images. We will then add dynamics to the model and
  demonstrate a marked improvement over standard approaches on both synthetic and
  real-world tracking examples.'
venue: Machine Learning and Perception Group, Microsoft Research, Cambridge, U.K.
year: '2003'
month: 3
day: '24'
layout: talk
key: Lawrence:msr03
categories:
- Lawrence:msr03
authors:
- firstname: Neil D.
  lastname: Lawrence
  url: http://inverseprobability.com
  institute: University of Sheffield
published: 2003-03-24
---
