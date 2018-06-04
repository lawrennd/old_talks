---
title: Probabilistic Non-linear Component Analysis through Gaussian Process Latent Variable Models
venue: University of California, Berkeley, U.S.A.
abstract: |
  It is known that Principal Component Analysis has an underlying
  probabilistic representation based on a latent variable model. PCA
  is recovered when the latent variables are integrated out and the
  parameters of the model are optimised by maximum likelihood. It is
  less well known that the dual approach of integrating out the
  parameters and optimising with respect to the latent variables also
  leads to PCA.  The marginalised likelihood in this case takes the
  form of Gaussian process mappings, with linear Covariance functions,
  from a latent space to an observed space, which we refer to as a
  Gaussian Process Latent Variable Model (GPLVM) [@Lawrence:gplvm03]. 
  It is straightforward to *non-linearise* this model by
  substituting the linear covariance function for a non-linear
  one. The result is a non-linear probabilistic PCA model. In this
  talk we will present a practical algorithm for optimising the latent
  variables in a non-linear GPLVM and discuss some relations with
  other models. Finally we will present results from a SIGGRAPH paper
  which uses the GPLVM to learn styles in an inverse kinematics
  problem [@Grochow:styleik04].
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
categories:
- Lawrence-ucbgplvm03
layout: talk
published: 2004-05-06
date: 2004-05-06
---
