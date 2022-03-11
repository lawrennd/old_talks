---
week: 8
title: "Dimensionality Reduction: Latent Variable Modelling"
abstract: "In this lecture we turn to *unsupervised learning*. Specifically, we introduce the idea of a latent variable model. Latent variable models are a probabilistic perspective on unsupervised learning which lead to dimensionality reduction algorithms. "
youtube: 0mtK2_rc0IY
---

\include{talk-macros.gpp}

\include{_mlai/includes/mlai-notebook-setup.md}

\subsection{Review}

\slides{* Last time: Looked at Bayesian Regression.
* Introduced priors and marginal likelihoods.
* This time: Unsupervised Learning}

\notes{So far in our classes we have focussed mainly on regression
problems, which are examples of supervised learning. We have considered the
relationship between the likelihood and the objective function and we have shown
how we can find paramters by maximizing the likelihood (equivalent to minimizing
the objective function) and in the last session we saw how we can *marginalize*
the parameters in a process known as Bayesian inference.}


\include{_ml/includes/clustering.md}

\include{_dimred/includes/high-dimensional-data.md}
\include{_dimred/includes/latent-variables.md}
\include{_dimred/includes/principal-component-analysis.md}

\include{_dimred/includes/probabilistic-pca.md}

\include{_dimred/includes/mocap-ppca.md}
\include{_dimred/includes/robot-wireless-ppca.md}
\include{_dimred/includes/ppca-interpretations.md}
\include{_dimred/includes/pca-in-practice.md}
\include{_dimred/includes/ppca-marginal-likelihood.md}
\include{_dimred/includes/ppca-reconstruction.md}

\reading

\thanks

\references
