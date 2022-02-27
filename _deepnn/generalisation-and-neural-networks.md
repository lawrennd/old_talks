---
layout: lecture
title: Generalization and Neural Networks
week: 1
session: 2
date: 2022-01-25
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
venue: LT1, William Gates Building
hackmdslides: fhuszar/r1HxvooMd#/
youtube: WaauyjcSNhc
oldyoutube: 
- code: tk9qM00Bs_o
  year: 2021
reveal: True
ipynb: True
time: "14:00"
start: "14:00"
end: "15:00"
---

\define{\errorFunction}{L}
\define{\designVector}{\boldsymbol{\phi}}

talk-macros.gpp}eepnn/includes/deepnn-notebook-setup.md}

\subsection{Quadratic Loss and Linear System}

\notes{We will consider a simplified system, to remind us of some of the linear algebra involved, and introduce some of the fundamental issues.}

talk-macros.gpp}l/includes/expected-loss.md}
\notes{talk-macros.gpp}l/includes/linear-regression-log-likelihood.md}
talk-macros.gpp}l/includes/olympic-marathon-linear-regression.md}
\define{designVector}{\basisVector}
\define{designVariable}{Phi}
\define{designMatrix}{\basisMatrix}
\define{noNoiseTerm}
talk-macros.gpp}l/includes/linear-regression-direct-solution.md}
talk-macros.gpp}l/includes/linear-regression-objective-optimisation.md}
talk-macros.gpp}l/includes/linear-regression-hessian.md}

talk-macros.gpp}l/includes/nigeria-nmis-linear-regression.md}

\notes{\section{Aside}}
\define{designMatrix}{\basisMatrix}

\notes{Just for informational purposes, the actual approach used in software for fitting a linear model *should* be a QR decomposition.}

\notes{talk-macros.gpp}l/includes/qr-decomposition-regression.md}}
}

\subsection{Basis Function Models}

\notes{We are reviewing models that are *linear* in the parameters. Very often we are interested in *non-linear* predictions. We can make models that are linear in the parameters and given non-linear predictions by introducing non-linear *basis functions*. A common example is the polynomial basis.}

talk-macros.gpp}l/includes/polynomial-basis.md}

\notes{The predictions from this model,
$$
\mappingFunction(\inputScalar) = \mappingScalar_0 + \mappingScalar_1 \inputScalar} + \mappingScalar_2 \inputScalar^2 + \mappingScalar_3 \inputScalar^3 + \mappingScalar_4 \inputScalar^4
$$
are *linear* in the parameters, $\mappingVector$, but *non-linear* in the input $\inputScalar^3$. Here we are showing a polynomial basis for a 1-dimensional input, $\inputScalar$, but basis functions can also be constructed for multidimensional inputs, $\inputVector$.}

\notes{In the neural network models, the "RELU function" is normally used as a basis function, but for illustration we will continue with the polynomial basis for these linear models.}

\undef{olympicMarathonData}
talk-macros.gpp}l/includes/olympic-marathon-polynomial.md}

talk-macros.gpp}l/includes/the-bootstrap.md}

talk-macros.gpp}l/includes/olympic-marathon-bootstrap-polynomial.md}

\define{biasVariancePlots}

talk-macros.gpp}l/includes/bias-variance-dilemma.md}

\notes{Also related on generalization error is the so called 'no free lunch theorem', which refers to our inability to decide what a better learning algorithm is without making assumptions about the data [@Wolpert:lack96] (see also @Wolpert-supervised02).}

\define{designVector}{\basisVector}
\define{designVariable}{Phi}
\define{designMatrix}{\basisMatrix}

talk-macros.gpp}l/includes/linear-regression-regularisation.md}
talk-macros.gpp}l/includes/training-with-noise-tikhonov-regularisation.md}
<!--include{_ml/includes/bayesian-interpretation-of-regularisation.md}-->

\subsection{Shallow and Deep Learning}

\notes{So far, we have been talking about *linear models* or *shallow learning* as we might think of it. Let's pause for a moment and consider a *fully connected* deep neural network model to relate the two ideas.}

talk-macros.gpp}eepnn/includes/deep-neural-network.md}

\newslide{Neural Network Prediction Function}

\notes{Under our basis function perspective, we can see that our deep neural network is mathematical composition of basis function models. Each layer contains a separate basis function set, so}
$$
 \mappingFunction(\inputVector; \mappingMatrix)  =  \mappingVector_4 ^\top\basisFunction\left(\mappingMatrix_3 \basisFunction\left(\mappingMatrix_2\basisFunction\left(\mappingMatrix_1 \inputVector\right)\right)\right).
$$

\notes{In this course there are two reasons for looking at the shallow model. Firstly, it is easier to introduce the concepts of regularisation in the linear model regime. Secondly, the matrix forms we see, e.g., expressions like $\basisMatrix^\top \basisMatrix$, appear in both models.}

\notes{For deep learning, we can no longer optimize the parameters of the model through solving a linear system[^quadratic]. Instead, we need to turn to non-linear optimization algorithms. For deep learning, that's typically stochastic gradient descent.

[^quadratic]: Apart from the last layer of parmeters in models with quadratic loss functions.}

\notes{While it's possible to compute the Hessian in a neural network, @Bishop-exact92, we also find that it varies across the parameter space and will not normally be positive definite. In practice, the number of parameters is normally so large that storing the Hessian is impossible (it has quadratic cost in the number of weights/parameters) due to memory constraints.}

\notes{This means that while the theory of minima in optimization is well understood, empirical experiments with large neural networks are hard and the lessons of small models do not all translate to the very large systems.}

\notes{We can stay within the framework of linear models but take a step closer to neural network models by introducing functions that are non-linear in the inputs, $\inputVector$, known as *basis functions*.}


\subsection{Overparameterised Systems}

\slides{* Neural networks are highly overparameterised.
* If we *could* examine their Hessian at "optimum"
  * Very low (or negative) eigenvalues.
  * Error function is not sensitive to changes in parameters.
  * Implies parmeters are *badly determined*}
  

\notes{If we could examine the Hessian of a neural network at its minimum, we can speculate about what we would find. In particular, we would find that it would have very many low (or negative) eigenvalues in many directions. This is indicative of the parameters being *badly determined* because of the neural network model being heavily *overparameterized*. So how does it generalize?}

\newslide{Whence Generalisation?}

\slides{* Not enough regularisation in our objective functions to explain.
* Neural network models are *not* using traditional generalisation approaches.
* The ability of these models to generalise *must* be coming somehow from the algorithm*
* How to explain it and control it is perhaps the most interesting theoretical question for neural networks.}

\notes{Simply put, there is not enough regularization encoded in the objective function of the neural network models we are using to explain the generalization performance. There must be something in the algorithms we are using that causes these highly overparameterized models to generalise well.}

talk-macros.gpp}eepnn/includes/double-descent.md}
talk-macros.gpp}eepnn/includes/neural-tangent-kernel.md}

talk-macros.gpp}eepnn/includes/regularisation-in-optimisation.md}

\thanks

\references



bootstrap




David Hogg's lecture <https://speakerdeck.com/dwhgg/linear-regression-with-huge-numbers-of-parameters>



The Deep Bootstrap <https://twitter.com/PreetumNakkiran/status/1318007088321335297?s=20>

Aki Vehtari on Leave One Out Uncertainty: <https://arxiv.org/abs/2008.10296> (check for his references).




