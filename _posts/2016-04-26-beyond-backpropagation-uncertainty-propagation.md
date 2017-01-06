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
blog: 2016-03-04-deep-learning-and-uncertainty.md
categories:
- Lawrence-msrne16b
day: '26'
demo: demo_2016_04_26_msr.m
errata: []
extras: []
key: Lawrence-msrne16b
layout: talk
month: 4
pdf: 2016-04-26-UncertaintyPropagation.pdf
ppt: 2016-04-26-UncertaintyPropagation.pptx
published: 2016-04-26
section: pre
title: 'Beyond Backpropagation: Uncertainty Propagation'
venue: Microsoft Research, New England, USA
year: '2016'
---