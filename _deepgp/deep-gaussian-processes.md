\institute{CSML, University College London} \frame{\maketitle}

\global\long\def\includetalkfile\#1

\global\long\def\latentScalar{f} \global\long\def\hiddenScalar{h}

Introduction
============

\include{../gplvm/includes/deep_nn_gp.md}
\include{../gp/includes/gp_extremely_short.md}
\global\long\def\hiddenScalar{f} \global\long\def\latentScalar{x}

Deep Gaussian Process Models
============================

\include{../gplvm/includes/deeptheory.md}
\include{../gp/includes/gp_variational_complexity.md}

Parametric Bottleneck
=====================

\include{../gp/includes/bottleneck.md}
\include{../gp/includes/low_rank_motivation.md}

<!--frame start-->
### Information capture

[Everything we want to do with a GP involves marginalising
$\mappingFunctionVector$]{}

-   Predictions

-   Marginal likelihood

-   Estimating covariance parameters

The posterior of $\mappingFunctionVector$ is the central object. This
means inverting $\Kff$.

<!--frame end-->
\include{../gp/includes/nystrom.md}
\include{../gp/includes/inducing_notation.md}
\include{../gp/includes/inducing_introduction.md}

<!--frame start-->
### The alternative posterior

[Instead of doing]{}
$$p(\mappingFunctionVector\given\dataVector,\inputMatrix) = \frac{p(\dataVector\given\mappingFunctionVector)p(\mappingFunctionVector\given\inputMatrix)}{\int p(\dataVector\given\mappingFunctionVector)p(\mappingFunctionVector\given\inputMatrix){\text{d}\mappingFunctionVector}}$$
[We’ll do]{}
$$p(\inducingVector\given\dataVector,\inducingInputMatrix) = \frac{p(\dataVector\given\inducingVector)p(\inducingVector\given\inducingInputMatrix)}{\int p(\dataVector\given\inducingVector)p(\inducingVector\given\inducingInputMatrix){\text{d}\inducingVector}}$$
\pause
\centering\alert{but $p(\dataVector\given\inducingVector)$ involves inverting $\Kff$}

<!--frame end-->
Flexible Parametric Approximation
=================================

\include{../gp/includes/larger_graph_intro.md}
\include{../gp/includes/larger_variational.md}
\include{../gp/includes/larger_factorize.md}

<!--frame start-->
\LARGE$$\mappingFunctionVector, \inducingVector \sim \gaussianSamp{\mathbf{0}}{\begin{bmatrix}\Kff & \Kfu\\\Kuf & \Kuu\end{bmatrix}}$$
$$\dataVector|\mappingFunctionVector = \prod_{i} \gaussianSamp{\mappingFunction}{\dataStd^2}$$

<!--frame end-->
Variational Compression
=======================

\include{../gp/includes/variational_compression.md}

\include{../gp/includes/low_rank_variational.md}

\include{../gplvm/includes/bayes_gplvm_intro.md}
\include{../gplvm/includes/variational_bayes_gplvm_long.md}

\include{../gplvm/includes/nested_variational_compression.md}

\include{../gp/includes/larger_gaussian.md}

Bayesian GP-LVM
===============

\include{../gplvm/includes/bayes_gplvm.md}
\include{../gp/includes/gp_big_data_technical.md}
\include{../gp/includes/gp_big_data.md}
\include{../gp/includes/deep_gps.md}
\include{../gplvm/includes/deep_pathologies.md}

\include{../gplvm/includes/deep_step_function.md}
\include{../gplvm/includes/deep_loop_detection.md}
\include{../gplvm/includes/deepresults.md}

\global\long\def\latentScalar{f}

\include{../health/includes/deep_health_model.md}

Conclusions
===========

\include{../gplvm/includes/ard_model.md}
\include{../gplvm/includes/ard_results.md}

Gaussian Process Dynamical Systems
----------------------------------

\include{../gplvm/includes/gpds.md}

Shared GP-LVM
-------------

\include{../gplvm/includes/mrd_gplvm.md}

\include{../gplvm/includes/stack_gp_intro.md}
\include{../gplvm/includes/stacked_pca.md}
\include{../gplvm/includes/stacked_gp.md}
\include{../gplvm/includes/deep_pathologies.md}
\include{../gplvm/includes/deepresults.md}

<!--frame start-->
### What Can We Do that Google Can’t?

-   Google’s resources give them access to volumes of data (or Facebook,
    or Microsoft, or Amazon).

-   Is there anything for Universities to contribute?

-   Assimilation of multiple views of the patient: each perhaps from a
    different patient.

-   This may be done by small companies (with support of Universities).

-   A Facebook app for your personalised health.

-   These methodologies are part of that picture.

<!--frame end-->
\include{../health/includes/deep_health_model.md}
\include{../health/includes/deep_health_rangers.md}

Summary
-------

<!--frame start-->
### Summary {#summary}

-   Deep Gaussian Processes allow unsupervised and supervised deep
    learning.

-   They can be easily adapted to handle multitask learning.

-   Data dimensionality turns out to not be a computational bottleneck.

-   Variational compression algorithms show promise for scaling these
    models to *massive* data sets.

<!--frame end-->
<!--frame failure start-->
[allowframebreaks]  \frametitle{References}

  {\tiny \bibliographystyle{pdf_abbrvnat}
    \bibliography{lawrence,other,zbooks}
  }



<!--frame failure end-->

