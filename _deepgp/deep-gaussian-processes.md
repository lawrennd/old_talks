---
title: "DRAFT SLIDES: Deep Gaussian Processes"
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: Amazon and University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
date: 1970-01-01
---

### DRAFT SLIDES

talk-macros.gpp}/talk-macros.tex}

<!--Introduction-->

talk-macros.gpp}eepgp/includes/deep_nn_gp.md}
talk-macros.gpp}p/includes/gp_extremely_short.md}

\newcommand{\hiddenScalar}{f}
\newcommand{\latentScalar}{x}

<!--Deep Gaussian Process Models-->

talk-macros.gpp}eepgp/includes/deeptheory.md}
talk-macros.gpp}p/includes/gp-variational-complexity.md}

<!--Parametric Bottleneck-->

talk-macros.gpp}p/includes/bottleneck.md}
talk-macros.gpp}p/includes/low-rank-motivation.md}

### Information capture

[Everything we want to do with a GP involves marginalising
$\mappingFunctionVector$]

-   Predictions

-   Marginal likelihood

-   Estimating covariance parameters

The posterior of $\mappingFunctionVector$ is the central object. This
means inverting $\Kff$.

talk-macros.gpp}p/includes/nystrom.md}
talk-macros.gpp}p/includes/inducing-notation.md}
talk-macros.gpp}p/includes/inducing-introduction.md}

### The alternative posterior

[Instead of doing]{}
$$p(\mappingFunctionVector\given\dataVector,\inputMatrix) = \frac{p(\dataVector\given\mappingFunctionVector)p(\mappingFunctionVector\given\inputMatrix)}{\int p(\dataVector\given\mappingFunctionVector)p(\mappingFunctionVector\given\inputMatrix){\text{d}\mappingFunctionVector}}$$
[We’ll do]{}
$$p(\inducingVector\given\dataVector,\inducingInputMatrix) = \frac{p(\dataVector\given\inducingVector)p(\inducingVector\given\inducingInputMatrix)}{\int p(\dataVector\given\inducingVector)p(\inducingVector\given\inducingInputMatrix){\text{d}\inducingVector}}$$
\pause
\centering\alert{but $p(\dataVector\given\inducingVector)$ involves inverting $\Kff$}

<!--Flexible Parametric Approximation-->

talk-macros.gpp}p/includes/larger-graph-intro.md}
talk-macros.gpp}p/includes/larger-variational.md}
talk-macros.gpp}p/includes/larger-factorize.md}


###

\LARGE$$\mappingFunctionVector, \inducingVector \sim \gaussianSamp{\mathbf{0}}{\begin{bmatrix}\Kff & \Kfu\\\Kuf & \Kuu\end{bmatrix}}$$
$$\dataVector|\mappingFunctionVector = \prod_{i} \gaussianSamp{\mappingFunction}{\dataStd^2}$$

<!--Variational Compression-->

talk-macros.gpp}p/includes/variational-compression.md}
talk-macros.gpp}p/includes/low-rank-variational.md}
talk-macros.gpp}plvm/includes/bayes-gplvm-intro.md}
talk-macros.gpp}plvm/includes/variational-bayes-gplvm-long.md}
talk-macros.gpp}plvm/includes/nested-variational-compression.md}
talk-macros.gpp}p/includes/larger-gaussian.md}

<!--Bayesian GP-LVM-->


talk-macros.gpp}plvm/includes/ard-gplvm.md}
talk-macros.gpp}plvm/includes/bayes-gplvm-intro.md}
talk-macros.gpp}plvm/includes/variational-bayes-gplvm-long.md}

talk-macros.gpp}p/includes/gp-big-data-technical.md}
talk-macros.gpp}p/includes/gp-big-data.md}

talk-macros.gpp}eepgp/includes/deep-gps.md}

talk-macros.gpp}eepgp/includes/deep-step-function.md}
talk-macros.gpp}eepgp/includes/deep-loop-detection.md}

\newcommand{\latentScalar}{f}

talk-macros.gpp}ealth/includes/deep-health-model.md}


<!--Conclusions-->

talk-macros.gpp}plvm/includes/ard_model.md}
talk-macros.gpp}plvm/includes/ard_results.md}

<!--Gaussian Process Dynamical Systems-->

talk-macros.gpp}plvm/includes/gpds.md}

<!--Shared GP-LVM-->

talk-macros.gpp}plvm/includes/mrd-gplvm.md}
talk-macros.gpp}eepgp/includes/stack-gp-intro.md}
talk-macros.gpp}eepgp/includes/stacked-pca.md}
talk-macros.gpp}eepgp/includes/stacked-gp.md}
talk-macros.gpp}eepgp/includes/deep-pathologies.md}
talk-macros.gpp}eepgp/includes/deep-results.md}

\section{What Can We Do that Google Can’t?}

-   Google’s resources give them access to volumes of data (or Facebook,
    or Microsoft, or Amazon).

-   Is there anything for Universities to contribute?

-   Assimilation of multiple views of the patient: each perhaps from a
    different patient.

-   This may be done by small companies (with support of Universities).

-   A Facebook app for your personalised health.

-   These methodologies are part of that picture.

talk-macros.gpp}ealth/includes/deep-health-model.md}
talk-macros.gpp}ealth/includes/deep-health-rangers.md}

\section{Summary}

-   Deep Gaussian Processes allow unsupervised and supervised deep
    learning.

-   They can be easily adapted to handle multitask learning.

-   Data dimensionality turns out to not be a computational bottleneck.

-   Variational compression algorithms show promise for scaling these
    models to *massive* data sets.

\references


\thanks
