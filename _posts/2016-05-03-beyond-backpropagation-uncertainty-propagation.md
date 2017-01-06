---
abstract: Deep learning is founded on composable functions that are structured to
  capture regularities in data and can have their parameters optimized by backpropagation
  (differentiation via the chain rule). Their recent success is founded on the increased
  availability of data and computational power. However, they are not very data efficient.
  In low data regimes parameters are not well determined and severe overfitting can
  occur. The solution is to explicitly handle the indeterminacy by converting it to
  parameter uncertainty and propagating it through the model. Uncertainty propagation
  is more involved than backpropagation because it involves convolving the composite
  functions with probability distributions and integration is more challenging than
  differentiation. We will present one approach to fitting such models using Gaussian
  processes. The resulting models perform very well in both supervised and unsupervised
  learning on small data sets. The remaining challenge is to scale the algorithms
  to much larger data.
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
bio: Neil Lawrence is Professor of Machine Learning at the University of Sheffield.
  His expertise is in probabilistic modelling with a particular focus on Gaussian
  processes and a strong interest in bridging the worlds of mechanistic and empirical
  models.
blog: 2016-03-04-deep-learning-and-uncertainty.md
categories:
- Lawrence-iclr16
day: '3'
demo: demo_2016_05_03_iclr.m
errata: []
extras: []
key: Lawrence-iclr16
layout: talk
month: 5
pdf: 2016-05-03-UncertaintyPropagationICLR.pdf
ppt: 2016-05-03-UncertaintyPropagationICLR.pptx
published: 2016-05-03
section: pre
title: 'Beyond Backpropagation: Uncertainty Propagation'
venue: ICLR 2016, San Jaun, Puerto Rico
year: '2016'
---