---
layout: lecture
title: Generalization and Neural Networks
week: 1
session: 2
date: 2021-01-26
author:
- given: Neil D.
  family: Lawrence
  institution: University of Cambridge
  url: http://inverseprobability.com
abstract: >
  This lecture will cover generalization in machine learning with a particular focus on
  neural architectures. We will review classical generalization and explore what's different
  about neural network models.
talkscam:
reveal: True
ipynb: True
time: "14:00"
start: "14:00"
end: "15:00"
---

\include{talk-macros.gpp}

\include{_deepnn/includes/deepnn-notebook-setup.md}

\subsection{Quadratic Loss and Linear System}

\notes{We will consider a simplified system, to remind us of some of the linear algebra involved, and introduce some of the fundamental issues.}

\include{_ml/includes/expected-loss.md}
\define{designVector}{\basisVector}
\define{designVariable}{Phi}
\define{designMatrix}{\basisMatrix}
\include{_ml/includes/linear-regression-direct-solution.md}
\include{_ml/includes/linear-regression-objective-optimisation.md}
\include{_ml/includes/linear-regression-hessian.md}

\subsection{Shallow and Deep Learning}

\notes{So far we have been talking about *linear models* or *shallow learning* as we might think of it. Let's pause for a moment and consider a *fully connected* deep neural network model to relate the two ideas.}

\include{_deepnn/includes/deep-neural-network.md}

\notes{Under our basis function perspective, we can see that our deep neural network is mathematical composition of basis function models. Each layer contains a separate basis function set, so}
$$
 \mappingFunction(\inputVector; \mappingMatrix)  =  \mappingVector_4 ^\top\basisFunction\left(\mappingMatrix_3 \basisFunction\left(\mappingMatrix_2\basisFunction\left(\mappingMatrix_1 \inputVector\right)\right)\right)
$$

\notes{So, in this course there are two reasons for looking at the shallow model. Firstly, it is easier to introduce the concepts of regulariation in the linear model regime. Secondly, the matrix forms we see (objects like $\basisMatrix^\top \basisMatrix$) which represents the Hessian matrix for the linear model, appear in both models.}

\notes{For deep learning, we can no longer optimize the parameters of the model through solving a linear system[^quadratic]. Instead, we need to turn to non-linear optimization algorithms. For deep learning, that's typically stochastic gradient descient.

[^quadratic]: Apart from the last layer of parmeters in models with quadratic loss functions.}

\include{_ml/includes/nigeria-nmis-linear-regression.md}

\section{Aside}

\notes{Just for informational purposes, the actual approach used in software for fitting a linear model *should* be a QR decomposition.}

\include{_ml/includes/qr-decomposition-regression.md}

\subsection{Basis Function Models}

\notes{We are reviewing models that are *linear* in the parameters. Very often we are interested in *non-linear* predictions. We can make models that are linear in the parameters and given non-linear predictions by introducing non-linear *basis functions*. A common example is the polynomial basis.}

\include{_ml/includes/polynomial-basis.md}

\notes{The predictions from this model,
$$
\mappingFunction(\inputScalar) = \mappingScalar_0 + \mappingScalar_1 \inputScalar} + \mappingScalar_2 \inputScalar^2 + \mappingScalar_3 \inputScalar^3 + \mappingScalar_4 \inputScalar^4
$$
are *linear* in the parameters, $\mappingVector$, but *non-linear* in the input $\inputScalar^3$. Here we are showing a polynomial basis for a 1-dimensional input, $\inputScalar$, but basis functions can also be constructed for multidimensional inputs, $\inputVector$.}

\include{_ml/includes/olympic-marathon-polynomial.md}

\include{_ml/includes/the-bootstrap.md}
\include{_ml/includes/the-jackknife.md}

\include{_ml/includes/olympic-marathon-bootstrap-polynomial.md}

\define{biasVariancePlots}

\include{_ml/includes/bias-variance-dilemma.md}

\notes{Also related on generalisation error is the so called 'no free lunch theorem', which refers to our inability to decide what a better learning algorithm is without making assumptions about the data [@Wolpert:lack96] (see also @Wolpert-supervised02).}

\include{_ml/includes/linear-regression-regularisation.md}
\include{_ml/includes/training-with-noise-tikhonov-regularisation.md}
\include{_ml/includes/bayesian-interpretation-of-regularisation.md}
\include{_deepnn/includes/double-descent.md}
\include{_deepnn/includes/neural-tangent-kernel.md}
\include{_deepnn/includes/regularisation-in-optimisation.md}

\thanks

\references



bootstrap




David Hogg's lecture <https://speakerdeck.com/dwhgg/linear-regression-with-huge-numbers-of-parameters>



The Deep Bootstrap <https://twitter.com/PreetumNakkiran/status/1318007088321335297?s=20>

Aki Vehtari on Leave One Out Uncertainty: <https://arxiv.org/abs/2008.10296> (check for his references).




