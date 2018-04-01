---
layout: slides
title: "DRAFT SLIDES: Deep Gaussian Processes"
author: Neil D. Lawrence
---

### DRAFT SLIDES

\include{../talk-macros.tex}

<!--Introduction-->

\include{../_deepgp/includes/deep_nn_gp.md}
\include{../_gp/includes/gp_extremely_short.md}

\newcommand{\hiddenScalar}{f}
\newcommand{\latentScalar}{x}

<!--Deep Gaussian Process Models-->

\include{../_deepgp/includes/deeptheory.md}
\include{../_gp/includes/gp-variational-complexity.md}

<!--Parametric Bottleneck-->

\include{../_gp/includes/bottleneck.md}
\include{../_gp/includes/low-rank-motivation.md}

### Information capture

[Everything we want to do with a GP involves marginalising
$\mappingFunctionVector$]

-   Predictions

-   Marginal likelihood

-   Estimating covariance parameters

The posterior of $\mappingFunctionVector$ is the central object. This
means inverting $\Kff$.

\include{../_gp/includes/nystrom.md}
\include{../_gp/includes/inducing-notation.md}
\include{../_gp/includes/inducing-introduction.md}

### The alternative posterior

[Instead of doing]{}
$$p(\mappingFunctionVector\given\dataVector,\inputMatrix) = \frac{p(\dataVector\given\mappingFunctionVector)p(\mappingFunctionVector\given\inputMatrix)}{\int p(\dataVector\given\mappingFunctionVector)p(\mappingFunctionVector\given\inputMatrix){\text{d}\mappingFunctionVector}}$$
[We’ll do]{}
$$p(\inducingVector\given\dataVector,\inducingInputMatrix) = \frac{p(\dataVector\given\inducingVector)p(\inducingVector\given\inducingInputMatrix)}{\int p(\dataVector\given\inducingVector)p(\inducingVector\given\inducingInputMatrix){\text{d}\inducingVector}}$$
\pause
\centering\alert{but $p(\dataVector\given\inducingVector)$ involves inverting $\Kff$}

<!--Flexible Parametric Approximation-->

\include{../_gp/includes/larger_graph_intro.md}
\include{../_gp/includes/larger_variational.md}
\include{../_gp/includes/larger_factorize.md}


###

\LARGE$$\mappingFunctionVector, \inducingVector \sim \gaussianSamp{\mathbf{0}}{\begin{bmatrix}\Kff & \Kfu\\\Kuf & \Kuu\end{bmatrix}}$$
$$\dataVector|\mappingFunctionVector = \prod_{i} \gaussianSamp{\mappingFunction}{\dataStd^2}$$

<!--Variational Compression-->

\include{../_gp/includes/variational_compression.md}
\include{../_gp/includes/low_rank_variational.md}
\include{../_gplvm/includes/bayes_gplvm_intro.md}
\include{../_gplvm/includes/variational_bayes_gplvm_long.md}
\include{../_gplvm/includes/nested_variational_compression.md}
\include{../_gp/includes/larger_gaussian.md}

<!--Bayesian GP-LVM-->


\include{../_gplvm/includes/ard_gplvm.md}
\include{../_gplvm/includes/bayes_gplvm_intro.md}
\include{../_gplvm/includes/variational_bayes_gplvm_long.md}

\include{../_gp/includes/gp_big_data_technical.md}
\include{../_gp/includes/gp_big_data.md}

\include{../_deepgp/includes/deep_gps.md}

\include{../_deepgp/includes/deep-step-function.md}
\include{../_deepgp/includes/deep-loop-detection.md}

\newcommand{\latentScalar}{f}

\include{../_health/includes/deep-health-model.md}


<!--Conclusions-->

\include{../_gplvm/includes/ard_model.md}
\include{../_gplvm/includes/ard_results.md}

<!--Gaussian Process Dynamical Systems-->

\include{../_gplvm/includes/gpds.md}

<!--Shared GP-LVM-->

\include{../_gplvm/includes/mrd_gplvm.md}
\include{../_deepgp/includes/stack-gp-intro.md}
\include{../_deepgp/includes/stacked-pca.md}
\include{../_deepgp/includes/stacked-gp.md}
\include{../_deepgp/includes/deep-pathologies.md}
\include{../_deepgp/includes/deep-results.md}

### What Can We Do that Google Can’t?

-   Google’s resources give them access to volumes of data (or Facebook,
    or Microsoft, or Amazon).

-   Is there anything for Universities to contribute?

-   Assimilation of multiple views of the patient: each perhaps from a
    different patient.

-   This may be done by small companies (with support of Universities).

-   A Facebook app for your personalised health.

-   These methodologies are part of that picture.

\include{../_health/includes/deep_health_model.md}
\include{../_health/includes/deep_health_rangers.md}

Summary
-------

### Summary {#summary}

-   Deep Gaussian Processes allow unsupervised and supervised deep
    learning.

-   They can be easily adapted to handle multitask learning.

-   Data dimensionality turns out to not be a computational bottleneck.

-   Variational compression algorithms show promise for scaling these
    models to *massive* data sets.

### References {.allowframebreaks data-background="../slides/diagrams/pres_bg.png"}


\bibliographystyle{pdf_abbrvnat}
\bibliography{lawrence,other,zbooks}
  


### Thanks!

* twitter: @lawrennd
* blog: [http://inverseprobability.com](http://inverseprobability.com/blog.html)
