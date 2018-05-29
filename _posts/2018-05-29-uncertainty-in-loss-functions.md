---
title: "Uncertainty in Loss Functions"
abstract: >
  Bayesian formalisms deal with uncertainty in parameters, frequentist formalisms deal with the *risk* of a data set, uncertainty in the data sample. In this talk, we consider uncertainty in the *loss function*. Uncertainty in the loss function. We introduce uncertainty through linear weightings of terms in the loss function and show how a distribution over the loss can be maintained through the *maximum entropy principle*. This allows us minimize the expected loss under our maximumm entropy distribution of the loss function. We recover weighted least squares and a LOESS-like regression from the formalism.
venue: IWCV 2018
transition: None
reveal: 2018-05-29-uncertainty-in-loss-functions.slides.html
published: 2018-05-29
layout: talk
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: Amazon Cambridge and University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
published: 2018-05-29
---


$$\newcommand{\Amatrix}{\mathbf{A}}
\newcommand{\KL}[2]{\text{KL}\left( #1\,\|\,#2 \right)}
\newcommand{\Kaast}{\kernelMatrix_{\mathbf{ \ast}\mathbf{ \ast}}}
\newcommand{\Kastu}{\kernelMatrix_{\mathbf{\ast} \inducingVector}}
\newcommand{\Kff}{\kernelMatrix_{\mappingFunctionVector \mappingFunctionVector}}
\newcommand{\Kfu}{\kernelMatrix_{\mappingFunctionVector \inducingVector}}
\newcommand{\Kuast}{\kernelMatrix_{\inducingVector \bf\ast}}
\newcommand{\Kuf}{\kernelMatrix_{\inducingVector \mappingFunctionVector}}
\newcommand{\Kuu}{\kernelMatrix_{\inducingVector \inducingVector}}
\newcommand{\Kuui}{\Kuu^{-1}}
\newcommand{\aMatrix}{\mathbf{A}}
\newcommand{\aScalar}{a}
\newcommand{\aVector}{\mathbf{a}}
\newcommand{\acceleration}{a}
\newcommand{\bMatrix}{\mathbf{B}}
\newcommand{\bScalar}{b}
\newcommand{\bVector}{\mathbf{b}}
\newcommand{\basisFunc}{\phi}
\newcommand{\basisFuncVector}{\boldsymbol{\basisFunc}}
\newcommand{\basisFunction}{\phi}
\newcommand{\basisLocation}{\mu}
\newcommand{\basisMatrix}{\boldsymbol{\Phi}}
\newcommand{\basisScalar}{\basisFunction}
\newcommand{\basisVector}{\boldsymbol{\basisFunction}}
\newcommand{\activationFunction}{\phi}
\newcommand{\activationMatrix}{\boldsymbol{\Phi}}
\newcommand{\activationScalar}{\basisFunction}
\newcommand{\activationVector}{\boldsymbol{\basisFunction}}
\newcommand{\bigO}{\mathcal{O}}
\newcommand{\binomProb}{\pi}
\newcommand{\cMatrix}{\mathbf{C}}
\newcommand{\cbasisMatrix}{\hat{\boldsymbol{\Phi}}}
\newcommand{\cdataMatrix}{\hat{\dataMatrix}}
\newcommand{\cdataScalar}{\hat{\dataScalar}}
\newcommand{\cdataVector}{\hat{\dataVector}}
\newcommand{\centeredKernelMatrix}{\mathbf{\MakeUppercase{\centeredKernelScalar}}}
\newcommand{\centeredKernelScalar}{b}
\newcommand{\centeredKernelVector}{\centeredKernelScalar}
\newcommand{\centeringMatrix}{\mathbf{H}}
\newcommand{\chiSquaredDist}[2]{\chi_{#1}^{2}\left(#2\right)}
\newcommand{\chiSquaredSamp}[1]{\chi_{#1}^{2}}
\newcommand{\conditionalCovariance}{\boldsymbol{\Sigma}}
\newcommand{\coregionalizationMatrix}{\mathbf{B}}
\newcommand{\coregionalizationScalar}{b}
\newcommand{\coregionalizationVector}{\mathbf{\coregionalizationScalar}}
\newcommand{\covDist}[2]{\text{cov}_{#2}\left(#1\right)}
\newcommand{\covSamp}[1]{\text{cov}\left(#1\right)}
\newcommand{\covarianceScalar}{c}
\newcommand{\covarianceVector}{\mathbf{\covarianceScalar}}
\newcommand{\covarianceMatrix}{\mathbf{C}}
\newcommand{\covarianceMatrixTwo}{\boldsymbol{\Sigma}}
\newcommand{\croupierScalar}{s}
\newcommand{\croupierVector}{\mathbf{\croupierScalar}}
\newcommand{\croupierMatrix}{\mathbf{\MakeUppercase{\croupierScalar}}}
\newcommand{\dataDim}{p}
\newcommand{\dataIndex}{i}
\newcommand{\dataIndexTwo}{j}
\newcommand{\dataMatrix}{\mathbf{Y}}
\newcommand{\dataScalar}{y}
\newcommand{\dataSet}{\mathcal{D}}
\newcommand{\dataStd}{\sigma}
\newcommand{\dataVector}{\mathbf{\dataScalar}}
\newcommand{\decayRate}{d}
\newcommand{\degreeMatrix}{\mathbf{\MakeUppercase{\degreeScalar}}}
\newcommand{\degreeScalar}{d}
\newcommand{\degreeVector}{\mathbf{\degreeScalar}}
% Already defined by latex
%\newcommand{\det}[1]{\left|#1\right|}
\newcommand{\diag}[1]{\text{diag}\left(#1\right)}
\newcommand{\diagonalMatrix}{\mathbf{D}}
\newcommand{\diff}[2]{\frac{\text{d}#1}{\text{d}#2}}
\newcommand{\diffTwo}[2]{\frac{\text{d}^2#1}{\text{d}#2^2}}
\newcommand{\displacement}{x}
\newcommand{\displacementVector}{\textbf{\displacement}}
\newcommand{\distanceMatrix}{\mathbf{\MakeUppercase{\distanceScalar}}}
\newcommand{\distanceScalar}{d}
\newcommand{\distanceVector}{\mathbf{\distanceScalar}}
\newcommand{\eigenvaltwo}{\ell}
\newcommand{\eigenvaltwoMatrix}{\mathbf{L}}
\newcommand{\eigenvaltwoVector}{\mathbf{l}}
\newcommand{\eigenvalue}{\lambda}
\newcommand{\eigenvalueMatrix}{\boldsymbol{\Lambda}}
\newcommand{\eigenvalueVector}{\boldsymbol{\lambda}}
\newcommand{\eigenvector}{\mathbf{\eigenvectorScalar}}
\newcommand{\eigenvectorMatrix}{\mathbf{U}}
\newcommand{\eigenvectorScalar}{u}
\newcommand{\eigenvectwo}{\mathbf{v}}
\newcommand{\eigenvectwoMatrix}{\mathbf{V}}
\newcommand{\eigenvectwoScalar}{v}
\newcommand{\entropy}[1]{\mathcal{H}\left(#1\right)}
\newcommand{\errorFunction}{E}
\newcommand{\expDist}[2]{\left<#1\right>_{#2}}
\newcommand{\expSamp}[1]{\left<#1\right>}
\newcommand{\expectation}[1]{\left\langle #1 \right\rangle }
\newcommand{\expectationDist}[2]{\left\langle #1 \right\rangle _{#2}}
\newcommand{\expectedDistanceMatrix}{\mathcal{D}}
\newcommand{\eye}{\mathbf{I}}
\newcommand{\fantasyDim}{r}
\newcommand{\fantasyMatrix}{\mathbf{\MakeUppercase{\fantasyScalar}}}
\newcommand{\fantasyScalar}{z}
\newcommand{\fantasyVector}{\mathbf{\fantasyScalar}}
\newcommand{\featureStd}{\varsigma}
\newcommand{\gammaCdf}[3]{\mathcal{GAMMA CDF}\left(#1|#2,#3\right)}
\newcommand{\gammaDist}[3]{\mathcal{G}\left(#1|#2,#3\right)}
\newcommand{\gammaSamp}[2]{\mathcal{G}\left(#1,#2\right)}
\newcommand{\gaussianDist}[3]{\mathcal{N}\left(#1|#2,#3\right)}
\newcommand{\gaussianSamp}[2]{\mathcal{N}\left(#1,#2\right)}
\newcommand{\given}{|}
\newcommand{\half}{\frac{1}{2}}
\newcommand{\heaviside}{H}
\newcommand{\hiddenMatrix}{\mathbf{\MakeUppercase{\hiddenScalar}}}
\newcommand{\hiddenScalar}{h}
\newcommand{\hiddenVector}{\mathbf{\hiddenScalar}}
\newcommand{\identityMatrix}{\eye}
\newcommand{\inducingInputScalar}{z}
\newcommand{\inducingInputVector}{\mathbf{\inducingInputScalar}}
\newcommand{\inducingInputMatrix}{\mathbf{Z}}
\newcommand{\inducingScalar}{u}
\newcommand{\inducingVector}{\mathbf{\inducingScalar}}
\newcommand{\inducingMatrix}{\mathbf{U}}
\newcommand{\inlineDiff}[2]{\text{d}#1/\text{d}#2}
\newcommand{\inputDim}{q}
\newcommand{\inputMatrix}{\mathbf{X}}
\newcommand{\inputScalar}{x}
\newcommand{\inputSpace}{\mathcal{X}}
\newcommand{\inputVals}{\inputVector}
\newcommand{\inputVector}{\mathbf{\inputScalar}}
\newcommand{\iterNum}{k}
\newcommand{\kernel}{\kernelScalar}
\newcommand{\kernelMatrix}{\mathbf{K}}
\newcommand{\kernelScalar}{k}
\newcommand{\kernelVector}{\mathbf{\kernelScalar}}
\newcommand{\kff}{\kernelScalar_{\mappingFunction \mappingFunction}}
\newcommand{\kfu}{\kernelVector_{\mappingFunction \inducingScalar}}
\newcommand{\kuf}{\kernelVector_{\inducingScalar \mappingFunction}}
\newcommand{\kuu}{\kernelVector_{\inducingScalar \inducingScalar}}
\newcommand{\lagrangeMultiplier}{\lambda}
\newcommand{\lagrangeMultiplierMatrix}{\boldsymbol{\Lambda}}
\newcommand{\lagrangian}{L}
\newcommand{\laplacianFactor}{\mathbf{\MakeUppercase{\laplacianFactorScalar}}}
\newcommand{\laplacianFactorScalar}{m}
\newcommand{\laplacianFactorVector}{\mathbf{\laplacianFactorScalar}}
\newcommand{\laplacianMatrix}{\mathbf{L}}
\newcommand{\laplacianScalar}{\ell}
\newcommand{\laplacianVector}{\mathbf{\ell}}
\newcommand{\latentDim}{q}
\newcommand{\latentDistanceMatrix}{\boldsymbol{\Delta}}
\newcommand{\latentDistanceScalar}{\delta}
\newcommand{\latentDistanceVector}{\boldsymbol{\delta}}
\newcommand{\latentForce}{f}
\newcommand{\latentFunction}{u}
\newcommand{\latentFunctionVector}{\mathbf{\latentFunction}}
\newcommand{\latentFunctionMatrix}{\mathbf{\MakeUppercase{\latentFunction}}}
\newcommand{\latentIndex}{j}
\newcommand{\latentScalar}{z}
\newcommand{\latentVector}{\mathbf{\latentScalar}}
\newcommand{\latentMatrix}{\mathbf{Z}}
\newcommand{\learnRate}{\eta}
\newcommand{\lengthScale}{\ell}
\newcommand{\rbfWidth}{\ell}
\newcommand{\likelihoodBound}{\mathcal{L}}
\newcommand{\likelihoodFunction}{L}
\newcommand{\locationScalar}{\mu}
\newcommand{\locationVector}{\boldsymbol{\locationScalar}}
\newcommand{\locationMatrix}{\mathbf{M}}
\newcommand{\variance}[1]{\text{var}\left( #1 \right)}
\newcommand{\mappingFunction}{f}
\newcommand{\mappingFunctionMatrix}{\mathbf{F}}
\newcommand{\mappingFunctionTwo}{g}
\newcommand{\mappingFunctionTwoMatrix}{\mathbf{G}}
\newcommand{\mappingFunctionTwoVector}{\mathbf{\mappingFunctionTwo}}
\newcommand{\mappingFunctionVector}{\mathbf{\mappingFunction}}
\newcommand{\scaleScalar}{s}
\newcommand{\mappingScalar}{w}
\newcommand{\mappingVector}{\mathbf{\mappingScalar}}
\newcommand{\mappingMatrix}{\mathbf{W}}
\newcommand{\mappingScalarTwo}{v}
\newcommand{\mappingVectorTwo}{\mathbf{\mappingScalarTwo}}
\newcommand{\mappingMatrixTwo}{\mathbf{V}}
\newcommand{\maxIters}{K}
\newcommand{\meanMatrix}{\mathbf{M}}
\newcommand{\meanScalar}{\mu}
\newcommand{\meanTwoMatrix}{\mathbf{M}}
\newcommand{\meanTwoScalar}{m}
\newcommand{\meanTwoVector}{\mathbf{\meanTwoScalar}}
\newcommand{\meanVector}{\boldsymbol{\meanScalar}}
\newcommand{\mrnaConcentration}{m}
\newcommand{\naturalFrequency}{\omega}
\newcommand{\neighborhood}[1]{\mathcal{N}\left( #1 \right)}
\newcommand{\neilurl}{http://inverseprobability.com/}
\newcommand{\noiseMatrix}{\boldsymbol{E}}
\newcommand{\noiseScalar}{\epsilon}
\newcommand{\noiseVector}{\boldsymbol{\epsilon}}
\newcommand{\norm}[1]{\left\Vert #1 \right\Vert}
\newcommand{\normalizedLaplacianMatrix}{\hat{\mathbf{L}}}
\newcommand{\normalizedLaplacianScalar}{\hat{\ell}}
\newcommand{\normalizedLaplacianVector}{\hat{\mathbf{\ell}}}
\newcommand{\numActive}{m}
\newcommand{\numBasisFunc}{m}
\newcommand{\numComponents}{m}
\newcommand{\numComps}{K}
\newcommand{\numData}{n}
\newcommand{\numFeatures}{K}
\newcommand{\numHidden}{h}
\newcommand{\numInducing}{m}
\newcommand{\numLayers}{\ell}
\newcommand{\numNeighbors}{K}
\newcommand{\numSequences}{s}
\newcommand{\numSuccess}{s}
\newcommand{\numTasks}{m}
\newcommand{\numTime}{T}
\newcommand{\numTrials}{S}
\newcommand{\outputIndex}{j}
\newcommand{\paramVector}{\boldsymbol{\theta}}
\newcommand{\parameterMatrix}{\boldsymbol{\Theta}}
\newcommand{\parameterScalar}{\theta}
\newcommand{\parameterVector}{\boldsymbol{\parameterScalar}}
\newcommand{\partDiff}[2]{\frac{\partial#1}{\partial#2}}
\newcommand{\precisionScalar}{j}
\newcommand{\precisionVector}{\mathbf{\precisionScalar}}
\newcommand{\precisionMatrix}{\mathbf{J}}
\newcommand{\pseudotargetScalar}{\widetilde{y}}
\newcommand{\pseudotargetVector}{\mathbf{\pseudotargetScalar}}
\newcommand{\pseudotargetMatrix}{\mathbf{\widetilde{Y}}}
\newcommand{\rank}[1]{\text{rank}\left(#1\right)}
\newcommand{\rayleighDist}[2]{\mathcal{R}\left(#1|#2\right)}
\newcommand{\rayleighSamp}[1]{\mathcal{R}\left(#1\right)}
\newcommand{\responsibility}{r}
\newcommand{\rotationScalar}{r}
\newcommand{\rotationVector}{\mathbf{\rotationScalar}}
\newcommand{\rotationMatrix}{\mathbf{R}}
\newcommand{\sampleCovScalar}{s}
\newcommand{\sampleCovVector}{\mathbf{\sampleCovScalar}}
\newcommand{\sampleCovMatrix}{\mathbf{s}}
\newcommand{\scalarProduct}[2]{\left\langle{#1},{#2}\right\rangle}
\newcommand{\sign}[1]{\text{sign}\left(#1\right)}
\newcommand{\sigmoid}[1]{\sigma\left(#1\right)}
\newcommand{\singularvalue}{\ell}
\newcommand{\singularvalueMatrix}{\mathbf{L}}
\newcommand{\singularvalueVector}{\mathbf{l}}
\newcommand{\sorth}{\mathbf{u}}
\newcommand{\spar}{\lambda}
\newcommand{\trace}[1]{\text{tr}\left(#1\right)}
\newcommand{\BasalRate}{B}
\newcommand{\DampingCoefficient}{C}
\newcommand{\DecayRate}{D}
\newcommand{\Displacement}{X}
\newcommand{\LatentForce}{F}
\newcommand{\Mass}{M}
\newcommand{\Sensitivity}{S}
\newcommand{\basalRate}{b}
\newcommand{\dampingCoefficient}{c}
\newcommand{\mass}{m}
\newcommand{\sensitivity}{s}
\newcommand{\springScalar}{\kappa}
\newcommand{\springVector}{\boldsymbol{\kappa}}
\newcommand{\springMatrix}{\boldsymbol{\mathcal{K}}}
\newcommand{\tfConcentration}{p}
\newcommand{\tfDecayRate}{\delta}
\newcommand{\tfMrnaConcentration}{f}
\newcommand{\tfVector}{{\bf \tfConcentration}}
\newcommand{\velocity}{v}
\newcommand{\sufficientStatsScalar}{g}
\newcommand{\sufficientStatsVector}{\mathbf{\sufficientStatsScalar}}
\newcommand{\sufficientStatsMatrix}{\mathbf{G}}
\newcommand{\switchScalar}{s}
\newcommand{\switchVector}{\mathbf{\switchScalar}}
\newcommand{\switchMatrix}{\mathbf{S}}
\newcommand{\tr}[1]{\text{tr}\left(#1\right)}
\newcommand{\loneNorm}[1]{\left\Vert #1 \right\Vert_1}
\newcommand{\ltwoNorm}[1]{\left\Vert #1 \right\Vert_2}
\newcommand{\onenorm}[1]{\left\vert#1\right\vert_1}
\newcommand{\twonorm}[1]{\left\Vert #1 \right\Vert}
\newcommand{\vScalar}{v}
\newcommand{\vVector}{\mathbf{v}}
\newcommand{\vMatrix}{\mathbf{V}}
\newcommand{\varianceDist}[2]{\text{var}_{#2}\left( #1 \right)}
% Already defined by latex
%\newcommand{\vec}{#1:}
\newcommand{\vecb}[1]{\left(#1\right):}
\newcommand{\weightScalar}{w}
\newcommand{\weightVector}{\mathbf{\weightScalar}}
\newcommand{\weightMatrix}{\mathbf{W}}
\newcommand{\weightedAdjacencyMatrix}{\mathbf{A}}
\newcommand{\weightedAdjacencyScalar}{a}
\newcommand{\weightedAdjacencyVector}{\mathbf{\weightedAdjacencyScalar}}
\newcommand{\onesVector}{\mathbf{1}}
\newcommand{\zerosVector}{\mathbf{0}}
$$

## What is Machine Learning?

What is machine learning? At its most basic level machine learning is a combination of

$$ \text{data} + \text{model} \xrightarrow{\text{compute}} \text{prediction}$$

where *data* is our observations. They can be actively or passively
acquired (meta-data). The *model* contains our assumptions, based on
previous experience. That experience can be other data, it can come
from transfer learning, or it can merely be our beliefs about the
regularities of the universe. In humans our models include our
inductive biases. The *prediction* is an action to be taken or a
categorization or a quality score. The reason that machine learning
has become a mainstay of artificial intelligence is the importance of
predictions in artificial intelligence. The data and the model are combined through computation.


In practice we normally perform machine learning using two functions. To combine data with a model we typically make use of:

**a prediction function** a function which is used to make the predictions. It includes our beliefs about the regularities of the universe, our assumptions about how the world works, e.g. smoothness, spatial similarities, temporal similarities.

**an objective function** a function which defines the cost of misprediction. Typically it includes knowledge about the world's generating processes (probabilistic objectives) or the costs we pay for mispredictions (empiricial risk minimization).

The combination of data and model through the prediction function and the objectie function leads to a *learning algorithm*. The class of prediction functions and objective functions we can make use of is restricted by the algorithms they lead to. If the prediction function or the objective function are too complex, then it can be difficult to find an appropriate learning algorithm. Much of the acdemic field of machine learning is the quest for new learning algorithms that allow us to bring different types of models and data together.

A useful reference for state of the art in machine learning is the UK Royal Society Report, [Machine Learning: Power and Promise of Computers that Learn by Example](https://royalsociety.org/~/media/policy/projects/machine-learning/publications/machine-learning-report.pdf).

You can also check my blog post on ["What is Machine Learning?"](http://inverseprobability.com/2017/07/17/what-is-machine-learning)



Uncertainty in the prediction function is handled by Bayesian inference, here we consider uncertainty arising in the objective functions, $E(\cdot)$.

Consider a loss function which decomposes across individual observations, $\dataScalar_{k,j}$, each of which is
dependent on some set of features, $\inputVector_k$.

$$
\errorFunction(\dataVector, \inputMatrix) = \sum_{k}\sum_{j}
L(\dataScalar_{k,j}, \inputVector_k)
$$
Assume that the loss function depends on the features through some mapping function, $\mappingFunction_j(\cdot)$ which
we call the *prediction function*.
$$
\errorFunction(\dataVector, \inputMatrix) = \sum_{k}\sum_{j} L(\dataScalar_{k,j},
\mappingFunction_j(\inputVector_k))
$$
without loss of generality, we can move
the index to the inputs, so we have $\inputVector_i =\left[\inputVector \quad
j\right]$, and we set $\dataScalar_i = \dataScalar_{k, j}$. So we have
$$
\errorFunction(\dataVector, \inputMatrix) = \sum_{i} L(\dataScalar_i, \mappingFunction(\inputVector_i))
$$
Bayesian inference considers uncertainty in $\mappingFunction$, often through
parameterizing it, $\mappingFunction(\inputVector; \parameterVector)$, and
considering a *prior* distribution for the parameters, $p(\parameterVector)$,
this in turn implies a distribution over functions, $p(\mappingFunction)$.
Process models, such as Gaussian processes specify this distribution, known as a
process, directly. 

Bayesian inference proceeds by specifying a *likelihood*
which relates the data, $\dataScalar$, to the parameters. Here we choose not to
do this, but instead we only consider the *loss* function for our objective. The
loss is the cost we pay for a misclassification. 

The *risk function* is the expectation of the loss under the distribution of the data. Here we are using
the framework of *empirical risk* minimization, because we have a sample based
approximation. The new expectation we are considering is around the loss
function itself, not the uncertainty in the data.

The loss function and the log
likelihood may take a mathematically similar form but they are philosophically
very different. The log likelihood assumes something about the *generating*
function of the data, whereas the loss function assumes something about the cost
we pay. Importantly the loss function in Bayesian inference only normally enters
at the point of decision.

The key idea in Bayesian inference is that the
probabilistic inference can be performed *without* knowing the loss becasue if
the model is correct, then the form of the loss function is irrelevant when
performing inference. In practice, however, the model is *never* correct.

Some
of the maths below looks similar to the maths we can find in Bayesian methods,
in particular variational Bayes, but that is merely a consequence of the
availability of analytical mathematics. There are only particular ways of
developing tractable algorithms, one route involves linear algebra. However, the
similarity of the mathematics belies a difference in interpretation. It is
similar to travelling a road (e.g. Ermine Street) in a wild landscape. We travel
together because that is where efficient progress is to be made, but in practice
a our destinations (Lincoln, York), may be different.

### Introduce Uncertainty

To introduce uncertainty we consider a weighted version of the loss function, we introduce positive weights, $\left\{\scaleScalar_i\right\}_{i=1}^\numData$.
$$
\errorFunction(\dataVector, \inputMatrix) = \sum_{i}
\scaleScalar_i L(\dataScalar_i, \mappingFunction(\inputVector_i))
$$
We now assume that tmake the assumption that these weights are drawn from a distribution, $q(\scaleScalar)$. Instead of looking to minimize the loss direction, we look at the expected loss under this distribution.

$$
\begin{align*}
\errorFunction(\dataVector, \inputMatrix) = & \sum_{i}\expectationDist{\scaleScalar_i L(\dataScalar_i,
\mappingFunction(\inputVector_i))}{q(\scaleScalar)}\\
&
=\sum_{i}\expectationDist{\scaleScalar_i }{q(\scaleScalar)}L(\dataScalar_i,
\mappingFunction(\inputVector_i))
\end{align*}
$$
We will assume that our process, $q(\scaleScalar)$ can depend on a variety of inputs such as $\dataVector$, $\inputMatrix$ and time, $t$.

### Principle of Maximum Entropy 

To maximize uncertainty in $q(w)$ we maximize its entropy. Following Jaynes formalism of maximum entropy, in the continuous space we do this with respect to an invariant measure,
$$
H(\scaleScalar)= - \int q(\scaleScalar) \log
\frac{q(\scaleScalar)}{m(\scaleScalar)} \text{d}\scaleScalar
$$
and since we minimize the loss, we balance this by adding in this term to form
$$
\begin{align*}
\errorFunction = & \beta\sum_{i}\expectationDist{\scaleScalar_i
}{q(\scaleScalar)}L(\dataScalar_i, \mappingFunction(\inputVector_i)) -
H(\scaleScalar)\\
&= \beta\sum_{i}\expectationDist{\scaleScalar_i
}{q(\scaleScalar)}L(\dataScalar_i, \mappingFunction(\inputVector_i)) +  \int
q(\scaleScalar) \log \frac{q(\scaleScalar)}{m(\scaleScalar)}
\text{d}\scaleScalar
\end{align*}
$$
where $\beta$ serves to weight the relative
contribution of the entropy term and the loss term.

We can now minimize this modified loss with respect to the density
$q(\scaleScalar)$, the freeform optimization over this term leads to
$$
\begin{align*}
q(\scaleScalar) \propto & \exp\left(- \beta \sum_{i=1}^\numData
\scaleScalar_i L(\dataScalar_i, \mappingFunction(\inputVector_i)) \right)
m(\scaleScalar)\\
 \propto & \prod_{i=1}^\numData \exp\left(- \beta
\scaleScalar_i L(\dataScalar_i, \mappingFunction(\inputVector_i)) \right)
m(\scaleScalar)
\end{align*}
$$

### Example

Assume 
$$
m(\scaleScalar) = \prod_i
\lambda\exp\left(-\lambda\scaleScalar_i\right)
$$
which is the distribution with
the maximum entropy for a given mean, $\scaleScalar$. Then we have
$$
q(\scaleScalar) = \prod_i q(\scaleScalar_i)
$$
$$
q(\scaleScalar_i) \propto
\frac{1}{\lambda+\beta L_i} \exp\left(-(\lambda+\beta L_i) \scaleScalar_i\right)
$$
and we can compute
$$
\expectationDist{\scaleScalar_i}{q(\scaleScalar)} =
\frac{1}{\lambda + \beta L_i}
$$

### Coordinate Ascent

We can optimize with respect to $q(\scaleScalar)$ recovering,
$$
q(\scaleScalar_i) = \frac{1}{\lambda+\beta L_i}
\exp\left(-(\lambda+\beta L_i) \scaleScalar_i\right)
$$
allowing us to compute the expectation of $\scaleScalar$,
$$
\expectationDist{\scaleScalar_i}{q(\scaleScalar_i)} = \frac{1}{\lambda+\beta
L_i}
$$
then, we can maximize our expected loss with respect to $\mappingFunction(\cdot)$
$$
\beta \sum_{i=1}^\numData
\expectationDist{\scaleScalar_i}{q(\scaleScalar_i)} L(\dataScalar_i,
\mappingFunction(\inputVector_i))
$$
If the loss is the *squared loss*, then this is recognised as a *reweighted least squares algorithm*. However, the loss can be of any form as long as $q(\scaleScalar)$ defined above exists.

In addition to the above, in our example below, we updated $\beta$ to normalize the expected loss to be $\numData$ at each iteration, so we
have
$$
\beta = \frac{\numData}{\sum_{i=1}^\numData
\expectationDist{\scaleScalar_i}{q(\scaleScalar_i)} L(\dataScalar_i,
\mappingFunction(\inputVector_i))}
$$

```{.python}
import pods
import matplotlib.pyplot as plt
```


### Olympic Marathon Data

The first thing we will do is load a standard data set for regression modelling. The data consists of the pace of Olympic Gold Medal Marathon winners for the Olympics from 1896 to present. First we load in the data and plot.



```{.python}
data = pods.datasets.olympic_marathon_men()
x = data['X']
y = data['Y']

offset = y.mean()
scale = np.sqrt(y.var())

xlim = (1875,2030)
ylim = (2.5, 6.5)
yhat = (y-offset)/scale

fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
_ = ax.plot(x, y, 'r.',markersize=10)
ax.set_xlabel('year', fontsize=20)
ax.set_ylabel('pace min/km', fontsize=20)
ax.set_xlim(xlim)
ax.set_ylim(ylim)

mlai.write_figure(figure=fig, filename='../slides/diagrams/datasets/olympic-marathon.svg', transparent=True, frameon=True)

```

### Olympic Marathon Data

<table><tr><td width="70%">
-   Gold medal times for Olympic Marathon since 1896.

-   Marathons before 1924 didn’t have a standardised distance.

-   Present results using pace per km.

-   In 1904 Marathon was badly organised leading to very slow times.
</td><td width="30%">
![image](../slides/diagrams/Stephen_Kiprotich.jpg)
<small>Image from Wikimedia Commons <http://bit.ly/16kMKHQ></small>
</td></tr></table>


<object class="svgplot" align="" data="../slides/diagrams/ml/olympic_marathon.svg"></object>


Things to notice about the data include the outlier in 1904, in this year, the olympics was in St Louis, USA. Organizational problems and challenges with dust kicked up by the cars following the race meant that participants got lost, and only very few participants completed. 

More recent years see more consistently quick marathons.



### Example: Linear Regression

```{.python}
import mlai
import numpy as np
import scipy as sp
```

Create a weighted linear regression class, inheriting from the ```mlai.LM```
class.

```{.python}
class LML(mlai.LM):
    """Linear model with evolving loss
    :param X: input values
    :type X: numpy.ndarray
    :param y: target values
    :type y: numpy.ndarray
    :param basis: basis function 
    :param type: function
    :param beta: weight of the loss function
    :param type: float"""

    def __init__(self, X, y, basis=None, beta=1.0, lambd=1.0):
        "Initialise"
        if basis is None:
            basis = mlai.basis(mlai.polynomial, number=2)
        mlai.LM.__init__(self, X, y, basis)
        self.s = np.ones((self.num_data, 1))#np.random.rand(self.num_data, 1)>0.5       
        self.update_w()
        self.sigma2 = 1/beta
        self.beta = beta
        self.name = 'LML_'+basis.function.__name__
        self.objective_name = 'Weighted Sum of Square Training Error'
        self.lambd = lambd

    def update_QR(self):
        "Perform the QR decomposition on the basis matrix."
        self.Q, self.R = np.linalg.qr(self.Phi*np.sqrt(self.s))

    def fit(self):
        """Minimize the objective function with respect to the parameters"""
        for i in range(30):
            self.update_w() # In the linear regression clas
            self.update_s()
        
    def update_w(self):
        self.update_QR()
        self.w_star = sp.linalg.solve_triangular(self.R, np.dot(self.Q.T, self.y*np.sqrt(self.s)))
        self.update_losses()

    def predict(self, X):
        """Return the result of the prediction function."""
        return np.dot(self.basis.Phi(X), self.w_star), None
        
    def update_s(self):
        """Update the weights"""
        self.s = 1/(self.lambd + self.beta*self.losses)
                                                 
    def update_losses(self):
        """Compute the loss functions for each data point."""
        self.update_f()
        self.losses = ((self.y-self.f)**2)
        self.beta = 1/(self.losses*self.s).mean()
        
    def objective(self):
        """Compute the objective function."""
        self.update_losses()
        return (self.losses*self.s).sum()
```


Set up a linear model (polynomial with two basis functions).

```{.python}
num_basis=2 
data_limits=[1890, 2020]
basis = mlai.basis(mlai.polynomial, num_basis, data_limits=data_limits)
model = LML(x, y, basis=basis, lambd=1, beta=1)
model2 = mlai.LM(x, y, basis=basis)
```

```{.python}
model.fit()
model2.fit()
```

```{.python}
import matplotlib.pyplot as plt
```

```{.python}
x_test = np.linspace(data_limits[0], data_limits[1], 130)[:, None]
f_test, f_var = model.predict(x_test)
f2_test, f2_var = model2.predict(x_test)
```

```{.python}
import teaching_plots as plot
from matplotlib import rc, rcParams
rcParams.update({'font.size': 22})
rc('text', usetex=True)
```

```{.python}

fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.plot(x_test, f2_test, linewidth=3, color='r')
ax.plot(x, y, 'g.', markersize=10)
ax.set_xlim(data_limits[0], data_limits[1])
ax.set_xlabel('year')
ax.set_ylabel('pace min/km')
_ = ax.set_ylim(2, 6)
mlai.write_figure('../slides/diagrams/ml/olympic-loss-linear-regression000.svg', transparent=True)
ax.plot(x_test, f_test, linewidth=3, color='b')
ax.plot(x, y, 'g.', markersize=10)
ax2 = ax.twinx()
ax2.bar(x.flatten(), model.s.flatten(), width=2, color='b')
ax2.set_ylim(0, 4)
ax2.set_yticks([0, 1, 2])
ax2.set_ylabel('$\langle s_i \\rangle$')
mlai.write_figure('../slides/diagrams/ml/olympic-loss-linear-regression001.svg', transparent=True)

```

```{.python}
import pods
pods.notebook.display_plots('olympic-loss-linear-regression{number:0>3}.svg', 
                            directory='../slides/diagrams/ml', number=(0, 1))
```
<object class="svgplot" align="" data="../slides/diagrams/ml/olympic-loss-linear-regression001.svg"></object>

### Parameter Uncertainty


Classical Bayesian inference is concerned with
parameter uncertainty, which equates to uncertainty in the *prediction
function*, $\mappingFunction(\inputVector)$. The prediction function is normally
an estimate of the value of $\dataScalar$ or constructs a probability density
for $\dataScalar$. 

Uncertainty in the prediction function can arise through
uncertainty in our loss function, but also through uncertainty in parameters in
the classical Bayesian sense. The full maximum entropy formalism would now be
$$
\expectationDist{\beta \scaleScalar_i L(\dataScalar_i,
\mappingFunction(\inputVector_i))}{q(\scaleScalar, \mappingFunction)} + \int
q(\scaleScalar, \mappingFunction) \log \frac{q(\scaleScalar,
\mappingFunction)}{m(\scaleScalar)m(\mappingFunction)}\text{d}\scaleScalar
\text{d}\mappingFunction
$$

$$
q(\mappingFunction, \scaleScalar) \propto
\prod_{i=1}^\numData \exp\left(- \beta \scaleScalar_i L(\dataScalar_i,
\mappingFunction(\inputVector_i)) \right) m(\scaleScalar)m(\mappingFunction)
$$

### Approximation

* Generally intractable, so assume:
$$
q(\mappingFunction, \scaleScalar) = q(\mappingFunction)q(\scaleScalar)
$$

* Entropy maximization proceeds as before but with
$$
q(\scaleScalar) \propto
\prod_{i=1}^\numData \exp\left(- \beta \scaleScalar_i \expectationDist{L(\dataScalar_i,
\mappingFunction(\inputVector_i))}{q(\mappingFunction)} \right) m(\scaleScalar)
$$
and
$$
q(\mappingFunction) \propto
\prod_{i=1}^\numData \exp\left(- \beta \expectationDist{\scaleScalar_i}{q(\scaleScalar)} L(\dataScalar_i,
\mappingFunction(\inputVector_i)) \right) m(\mappingFunction)
$$



* Can now proceed with iteration between $q(\scaleScalar)$, $q(\mappingFunction)$

```{.python}
class BLML(mlai.BLM):
    """Bayesian Linear model with evolving loss
    :param X: input values
    :type X: numpy.ndarray
    :param y: target values
    :type y: numpy.ndarray
    :param basis: basis function 
    :param type: function
    :param beta: weight of the loss function
    :param type: float"""

    def __init__(self, X, y, basis=None, alpha=1.0, beta=1.0, lambd=1.0):
        "Initialise"
        if basis is None:
            basis = mlai.basis(mlai.polynomial, number=2)
        mlai.BLM.__init__(self, X, y, basis=basis, alpha=alpha, sigma2=1/beta)
        self.s = np.ones((self.num_data, 1))#np.random.rand(self.num_data, 1)>0.5       
        self.update_w()
        self.beta = beta
        self.name = 'BLML_'+basis.function.__name__
        self.objective_name = 'Weighted Sum of Square Training Error'
        self.lambd = lambd     

    def update_QR(self):
        "Perform the QR decomposition on the basis matrix."
        self.Q, self.R = np.linalg.qr(np.vstack([self.Phi*np.sqrt(self.s), np.sqrt(self.sigma2/self.alpha)*np.eye(self.basis.number)]))

    def fit(self):
        """Minimize the objective function with respect to the parameters"""
        for i in range(30):
            self.update_w()
            self.update_s()
        
    def update_w(self):
        self.update_QR()
        self.QTy = np.dot(self.Q[:self.y.shape[0], :].T, self.y*np.sqrt(self.s))
        self.mu_w = sp.linalg.solve_triangular(self.R, self.QTy)
        self.RTinv = sp.linalg.solve_triangular(self.R, np.eye(self.R.shape[0]), trans='T')
        self.C_w = np.dot(self.RTinv, self.RTinv.T)
        self.update_losses()

    def update_s(self):
        """Update the weights"""
        self.s = 1/(self.lambd + self.beta*self.losses)
                                                 
    def update_losses(self):
        """Compute the loss functions for each data point."""
        self.update_f()
        self.losses = ((self.y-self.f_bar)**2) + self.f_cov[:, np.newaxis]
        self.beta = 1/(self.losses*self.s).mean()
        self.sigma2=1/self.beta
        

 
```

```{.python}
model = BLML(x, y, basis=basis, alpha=1000, lambd=1, beta=1)
model2 = mlai.BLM(x, y, basis=basis, alpha=1000, sigma2=1)
```

```{.python}
model.fit()
model2.fit()
```

```{.python}
x_test = np.linspace(data_limits[0], data_limits[1], 130)[:, None]
f_test, f_var = model.predict(x_test)
f2_test, f2_var = model2.predict(x_test)
```

```{.python}
import gp_tutorial
```

```{.python}
fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
from matplotlib import rc, rcParams
rcParams.update({'font.size': 22})
rc('text', usetex=True)
gp_tutorial.gpplot(x_test, f2_test, f2_test - 2*np.sqrt(f2_var), f2_test + 2*np.sqrt(f2_var), ax=ax, edgecol='r', fillcol='#CC3300')
ax.plot(x, y, 'g.', markersize=10)
ax.set_xlim(data_limits[0], data_limits[1])
ax.set_xlabel('year')
ax.set_ylabel('pace min/km')
_ = ax.set_ylim(2, 6)
mlai.write_figure('../slides/diagrams/ml/olympic-loss-bayes-linear-regression000.svg', transparent=True)
gp_tutorial.gpplot(x_test, f_test, f_test - 2*np.sqrt(f_var), f_test + 2*np.sqrt(f_var), ax=ax, edgecol='b', fillcol='#0033CC')
#ax.plot(x_test, f_test, linewidth=3, color='b')
ax.plot(x, y, 'g.', markersize=10)
ax2 = ax.twinx()
ax2.bar(x.flatten(), model.s.flatten(), width=2, color='b')
ax2.set_ylim(0, 0.2)
ax2.set_yticks([0, 0.1, 0.2])
ax2.set_ylabel('$\langle s_i \\rangle$')
mlai.write_figure('../slides/diagrams/ml/olympic-loss-bayes-linear-regression001.svg', transparent=True)

```

```{.python}
import pods
pods.notebook.display_plots('olympic-loss-bayes-linear-regression{number:0>3}.svg', 
                            directory='../slides/diagrams/ml', number=(0, 1))
```


<object class="svgplot" align="" data="../slides/diagrams/ml/olympic-loss-bayes-linear-regression001.svg"></object>

### Correlated Scales

Going beyond independence between weights, we now consider
$m(\vScalar)$ to be a Gaussian process, and scale by the *square* of $\vScalar$,
$\scaleScalar=\vScalar^2$
$$
\vScalar \sim \mathcal{GP}\left(\meanScalar(\inputVector), \kernel(\inputVector, \inputVector^\prime)\right)
$$



$$
q(\vScalar) \propto
\prod_{i=1}^\numData \exp\left(- \beta \vScalar_i^2 L(\dataScalar_i,
\mappingFunction(\inputVector_i)) \right)
\exp\left(-\frac{1}{2}(\vVector-\meanVector)^\top \kernelMatrix^{-1}
(\vVector-\meanVector)\right)
$$
where $\kernelMatrix$ is the covariance of the
process made up of elements taken from the covariance function,
$\kernelScalar(\inputVector, t, \dataVector; \inputVector^\prime, t^\prime,
\dataVector^\prime)$ so $q(\vScalar)$ itself is Gaussian with covariance
$$
\covarianceMatrix = \left(\beta\mathbf{L} + \kernelMatrix^{-1}\right)^{-1}
$$
and mean
$$
\meanTwoVector = \beta\covarianceMatrix\mathbf{L}\meanVector
$$
where $\mathbf{L}$ is a matrix containing the loss functions, $L(\dataScalar_i,
\mappingFunction(\inputVector_i))$ along its diagonal elements with zeros
elsewhere.

The update is given by 
$$
\expectationDist{\vScalar_i^2}{q(\vScalar)} = \meanTwoScalar_i^2 +
\covarianceScalar_{i, i}.
$$
To compare with before, if the mean of the measure $m(\vScalar)$  was zero and the prior covariance was spherical, $\kernelMatrix=\lambda^{-1}\eye$. Then this would equate to an update,
$$
\expectationDist{\vScalar_i^2}{q(\vScalar)} = \frac{1}{\lambda + \beta L_i}
$$
which is the same as we had before for the exponential prior over
$\scaleScalar$.

### Conditioning the Measure

Now that we have defined a process over $\vScalar$, we could define a region in which we're certain that we would like the weights to be high. For example, if we were looking to have a test point at location $\inputVector_\ast$, we could update our measure to be a Gaussian process that is conditioned on the observation of $\vScalar_\ast$ set appropriately at $\inputScalar_\ast$. In this case we have,

$$
\kernelMatrix^\prime = \kernelMatrix - \frac{\kernelVector_\ast\kernelVector^\top_\ast}{\kernelScalar_{*,*}}
$$
and 
$$
\meanVector^\prime = \meanVector + \frac{\kernelVector_\ast}{\kernelScalar_{*,*}}
(\vScalar_\ast-\meanScalar)
$$
where $\kernelScalar_\ast$ is the vector computed
through the covariance function between the training data $\inputMatrix$ and the
proposed point that we are conditioning the scale upon, $\inputVector_\ast$ and
$\kernelScalar_{*,*}$ is the covariance function computed for $\inputVector_\ast$.
Now the updated mean and covariance can be used in the maximum entropy
formulation as before.
$$
q(\vScalar) \propto \prod_{i=1}^\numData \exp\left(-
\beta \vScalar_i^2 L(\dataScalar_i, \mappingFunction(\inputVector_i)) \right)
\exp\left(-\frac{1}{2}(\vVector-\meanVector^\prime)^\top
\left.\kernelMatrix^\prime\right.^{-1} (\vVector-\meanVector^\prime)\right)
$$


We will consider the same data set as above. We first create a
Gaussian process model for the update.

```{.python}
class GPL(mlai.GP):
    def __init__(self, X, losses, kernel, beta=1.0, mu=0.0, X_star=None, v_star=None):
        # Bring together locations
        self.kernel = kernel
        self.K = self.kernel.K(X)
        self.mu = np.ones((X.shape[0],1))*mu
        self.beta = beta
        if X_star is not None:
            kstar = kernel.K(X, X_star)
            kstarstar = kernel.K(X_star, X_star)
            kstarstarInv = np.linalg.inv(kstarstar)
            kskssInv = np.dot(kstar, kstarstarInv)
            self.K -= np.dot(kskssInv,kstar.T)
            if v_star is not None:
                self.mu = kskssInv*(v_star-self.mu)+self.mu
                Xaug = np.vstack((X, X_star))
            else:
                raise ValueError("v_star should not be None when X_star is None")
```

```{.python}
class BLMLGP(BLML):
    def __init__(self, X, y, basis=None, kernel=None, beta=1.0, mu=0.0, alpha=1.0, X_star=None, v_star=None):
        BLML.__init__(self, X, y, basis=basis, alpha=alpha, beta=beta, lambd=None)
        self.gp_model=GPL(self.X, self.losses, kernel=kernel, beta=beta, mu=mu, X_star=X_star, v_star=v_star)
    def update_s(self):
        """Update the weights"""
        self.gp_model.C = sp.linalg.inv(sp.linalg.inv(self.gp_model.K+np.eye(self.X.shape[0])*1e-6) + self.beta*np.diag(self.losses.flatten()))
        self.gp_model.diagC = np.diag(self.gp_model.C)[:, np.newaxis]
        self.gp_model.f = self.gp_model.beta*np.dot(np.dot(self.gp_model.C,np.diag(self.losses.flatten())),self.gp_model.mu) +self.gp_model.mu
        
        #f, v = self.gp_model.K self.gp_model.predict(self.X)
        self.s = self.gp_model.f*self.gp_model.f + self.gp_model.diagC # + 1.0/(self.losses*self.gp_model.beta)
```

```{.python}
model = BLMLGP(x, y, 
           basis=basis, 
           kernel=mlai.kernel(mlai.eq_cov, lengthscale=20, variance=1.0),
           mu=0.0,
           beta=1.0, 
           alpha=1000,
           X_star=np.asarray([[2020]]), 
           v_star=np.asarray([[1]]))
```

```{.python}
model.fit()
```

```{.python}
f_test, f_var = model.predict(x_test)
```

```{.python}
fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.cla()
from matplotlib import rc, rcParams
rcParams.update({'font.size': 22})
rc('text', usetex=True)
gp_tutorial.gpplot(x_test, f2_test, f2_test - 2*np.sqrt(f2_var), f2_test + 2*np.sqrt(f2_var), ax=ax, edgecol='r', fillcol='#CC3300')
ax.plot(x, y, 'g.', markersize=10)
ax.set_xlim(data_limits[0], data_limits[1])
ax.set_xlabel('year')
ax.set_ylabel('pace min/km')
_ = ax.set_ylim(2, 6)
mlai.write_figure('../slides/diagrams/ml/olympic-gp-loss-bayes-linear-regression000.svg', transparent=True)
gp_tutorial.gpplot(x_test, f_test, f_test - 2*np.sqrt(f_var), f_test + 2*np.sqrt(f_var), ax=ax, edgecol='b', fillcol='#0033CC')
#ax.plot(x_test, f_test, linewidth=3, color='b')
ax.plot(x, y, 'g.', markersize=10)
ax2 = ax.twinx()
ax2.bar(x.flatten(), model.s.flatten(), width=2, color='b')
ax2.set_ylim(0, 3)
ax2.set_yticks([0, 0.5, 1])
ax2.set_ylabel('$\langle s_i \\rangle$')
mlai.write_figure('../slides/diagrams/ml/olympic-gp-loss-bayes-linear-regression001.svg', transparent=True)
```

```{.python}
import pods
```
```{.python}
pods.notebook.display_plots('olympic-gp-loss-bayes-linear-regression{number:0>3}.svg', 
                            directory='../slides/diagrams/ml', number=(0, 1))
```


<object class="svgplot" align="" data="../slides/diagrams/ml/olympic-gp-loss-bayes-linear-regression001.svg"></object>


Finally we make an attempt to show the joint uncertainty by first of all sampling from

```{.python}
fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
num_samps=10
samps=np.random.multivariate_normal(model.gp_model.f.flatten(), model.gp_model.C, size=100).T**2
ax.plot(x, samps, '-x', markersize=10, linewidth=2)
ax.set_xlim(data_limits[0], data_limits[1])
ax.set_xlabel('year')
_ = ax.set_ylabel('$s_i$')
mlai.write_figure('../slides/diagrams/ml/olympic-gp-loss-samples.svg', transparent=True)
```

<object class="svgplot" align="" data="../slides/diagrams/ml/olympic-gp-loss-samples.svg"></object>

```{.python}
fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.plot(x, y, 'r.', markersize=10)
ax.set_xlim(data_limits[0], data_limits[1])
ax.set_ylim(2, 6)
ax.set_xlabel('year')
ax.set_ylabel('pace min/km')
gp_tutorial.gpplot(x_test, f_test, f_test - 2*np.sqrt(f_var), f_test + 2*np.sqrt(f_var), ax=ax, edgecol='b', fillcol='#0033CC')
mlai.write_figure('../slides/diagrams/ml/olympic-gp-loss-bayes-linear-regression-and-samples000.svg', transparent=True)
allsamps = []
for i in range(samps.shape[1]):
    model.s = samps[:, i:i+1]
    model.update_w()
    f_bar, f_cov =model.predict(x_test, full_cov=True)
    f_samp = np.random.multivariate_normal(f_bar.flatten(), f_cov, size=10).T
    ax.plot(x_test, f_samp, linewidth=0.5, color='k')
    allsamps+=list(f_samp[-1, :])
mlai.write_figure('../slides/diagrams/ml/olympic-gp-loss-bayes-linear-regression-and-samples001.svg', transparent=True)
```

```{.python}
import pods
pods.notebook.display_plots('olympic-gp-loss-bayes-linear-regression-and-samples{number:0>3}.svg', 
                            directory='../slides/diagrams/ml', number=(0, 1))
```



```{.python}
fig, ax = plt.subplots(figsize=plot.big_figsize)
ax.hist(np.asarray(allsamps), bins=30, density=True)
ax.set_xlabel='pace min/kim'
mlai.write_figure('../slides/diagrams/ml/olympic-gp-loss-histogram-2020.svg', transparent=True)
```

### Histogram of Predictions from 2020

<object class="svgplot" align="" data="../slides/diagrams/ml/olympic-gp-loss-histogram-2020.svg"></object>

### Conclusions

* Maximum Entropy Framework for uncertainty in 
    * Loss functions
    * Prediction functions


### Thanks!

* twitter: @lawrennd
* blog: [http://inverseprobability.com](http://inverseprobability.com/blog.html)
