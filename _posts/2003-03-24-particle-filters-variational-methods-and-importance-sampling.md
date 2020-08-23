---
title: Particle Filters, Variational methods and Importance Sampling
venue: Machine Learning and Perception Group, Microsoft Research, Cambridge, U.K.
abstract: |
  Particle filters allow tracking of systems with highly non-linear,
  multi-modal posterior distributions, however they are prone to
  failure when model likelihoods are sharply peaked or state spaces
  are high dimensional. This failure is caused by a mismatch between
  the proposal distribution and the true posterior. The number of
  particles of samples then required to accurately represent the
  posterior increases dramatically and with it the computational
  demands of the algorithm. By formulating the problem within the
  framework of variational inference we derive an algorithm in which
  the proposal naturally adapts to more accurately reflect the true
  posterior.  This is achieved by replacing intractable moment
  evaluations, arising from the highly non-linear nature of the
  likelihood functions, with sample based approximations.  In this
  talk we shall first introduce the approach in a static setting:
  Bayesian processing of cDNA microarray images. We will then add
  dynamics to the model and demonstrate a marked improvement over
  standard approaches on both synthetic and real-world tracking
  examples.
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
layout: talk
published: 2003-03-24
date: 2003-03-24
---
