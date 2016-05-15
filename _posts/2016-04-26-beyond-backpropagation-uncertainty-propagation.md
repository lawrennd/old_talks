---
title: 'Beyond Backpropagation: Uncertainty Propagation'
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
year: '2016'
month: 4
day: '26'
demo: demo_2016_04_26_msr.m
venue: Microsoft Research, New England, USA
pdf: 2016-04-26-UncertaintyPropagation.pdf
ppt: 2016-04-26-UncertaintyPropagation.pptx
layout: talk
key: Lawrence:msrne16b
categories:
- Lawrence:msrne16b
authors:
- firstname: Neil D.
  lastname: Lawrence
  url: http://inverseprobability.com
  institute: University of Sheffield
  twitter: lawrennd
  gscholar: r3SJcvoAAAAJ
published: 2016-04-26
---
