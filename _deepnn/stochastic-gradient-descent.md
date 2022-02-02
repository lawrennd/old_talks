---
layout: lecture
title: Optimization and Stochastic Gradient Descent
week: 2
session: 2
author:
- given: Ferenc
  family: Huszár
  institution: University of Cambridge
  url: https://www.inference.vc/about/
abstract: >
  This lecture will cover stochastic gradient descent.
talkscam:
venue: LT1, William Gates Building
hackmdnotes: fhuszar/rJWAWC7gO
hackmdslides: fhuszar/Hy69Wvrg_
youtube: nIvu1s1xQUg
oldyoutube:
- code: GDyD8KwSfvk
  year: 2021
reveal: true
time: "14:00"
start: "14:00"
end: "15:00"
date: 2022-02-01
---


\notes{You can find the [slides here](https://hackmd.io/@fhuszar/Hy69Wvrg_) and the [notes here](https://hackmd.io/@fhuszar/rJWAWC7gO).}


\subsection{Empirical Risk Minimization via gradient descent}

$$
\mathbf{w}_{t+1} = \mathbf{w}_t - \eta \nabla_\mathbf{w} \hat{L}(\mathbf{w_t}, \mathcal{D})
$$

Calculating the gradient:
* takes time to cycle through whole dataset
* limited memory on GPU
* is wasteful: $\hat{L}$ is a sum, CLT applies


\subsection{Stochastic gradient descent}

$$
\mathbf{w}_{t+1} = \mathbf{w}_t - \eta \nabla_\mathbf{w} \hat{L}(\mathbf{w_t}, \mathcal{D}_t)
$$

where $\mathcal{D}_t$ is a random subset (minibatch) of $\mathcal{D}$.

Also known as minibatch-SGD.


\subsection{Does it converge?}

Unbiased gradient estimator:

$$
\mathbb{E}[\hat{L}(\mathbf{w}, \mathcal{D}_t)] = \hat{L}(\mathbf{w}, \mathcal{D})
$$

* empirical risk does not increase in expectation
* $\hat{L}(\mathbf{w}_t)$ is a supermartingale
* Doob's martingale convergence theorem: a.s. convergence.


\subsection{Does it behave the same way?}

![](https://i.imgur.com/xRYHk0m.png =1200x)


\subsection{Analysis of mean iterate}

![](https://i.imgur.com/9j85UIv.png)

([Smith et al, 2021](https://arxiv.org/abs/2101.12176)) "On the Origin of Implicit Regularization in Stochastic Gradient Descent"


\subsection{Analysis of the mean iterate}

$$
\mathbf{w}_{t+1} = \mathbf{w}_t - \eta \nabla_\mathbf{w} \hat{L}(\mathbf{w_t}, \mathcal{D}_t)
$$

mean iterate in SGD:

$$
\mu_t = \mathbb{E}[\mathbf{w}_t]
$$


\subsection{Implicit regularization in SGD}

([Smith et al, 2021](https://arxiv.org/abs/2101.12176)): mean iterate approximated as continuous gradient flow:

$$
\small
\dot{\mu}(t) = -\eta \nabla_\mathbf{w}\tilde{L}_{SGD}(\mu(t), \mathcal{D})
$$

where

$$
\small
\tilde{L}_{SGD}(\mathbf{w}, \mathcal{D}) = \tilde{L}_{GD}(\mathbf{w}, \mathcal{D}) + \frac{\eta}{4}\mathbb{E}\|\nabla_\mathbf{w}\hat{L}(\mathbf{w}, \mathcal{D_t}) - \nabla_\mathbf{w}\hat{L}(\mathbf{w}, \mathcal{D})\|^2
$$


\subsection{Implicit regularization in SGD}

([Smith et al, 2021](https://arxiv.org/abs/2101.12176)): mean iterate approximated as continuous gradient flow:

$$
\small
\dot{\mu}(t) = -\eta \nabla_\mathbf{w}\tilde{L}_{SGD}(\mu(t), \mathcal{D})
$$

where

$$
\small
\tilde{L}_{SGD}(\mathbf{w}, \mathcal{D}) = \tilde{L}_{GD}(\mathbf{w}, \mathcal{D}) + \frac{\eta}{4}\underbrace{\mathbb{E}\|\nabla_\mathbf{w}\hat{L}(\mathbf{w}, \mathcal{D_t}) - \nabla_\mathbf{w}\hat{L}(\mathbf{w}, \mathcal{D})\|^2}_{\text{variance of gradients}}
$$


\subsection{Revisiting cartoon example}

![](https://i.imgur.com/xRYHk0m.png =1200x)


\subsection{Limitations of this analysis}

![](https://i.imgur.com/4Zyb3vy.png)


\subsection{Variants of SGD: Adam}

Motivation:
* momentum
* adapting to the average gradient norm


\subsection{Adam algorithm}

![](https://i.imgur.com/MpiCllk.png)


\subsection{Is Adam any good?}

![](https://i.imgur.com/0yelxmm.png)


\subsection{Remember cartoon example}

![](https://i.imgur.com/xRYHk0m.png =1200x)

\newslide{}

![](https://i.imgur.com/xBNd5Qk.png)

\newslide{}

![](https://i.imgur.com/q9tTe7i.png)


\subsection{SGD summary}

* gradient noise is a feature not bug
* SGD avoids regions with high gradient noise
* this may help with generalization
* improved SGD, like Adam, may not help
* an optimization algorithm can be "too good"



<!--No Free Lunch for Optimization: <https://ti.arc.nasa.gov/m/profile/dhw/papers/78.pdf> <https://link.springer.com/chapter/10.1007%2F978-3-030-12767-1_5>
Survey of Optimization methods for DeepNNs: <https://arxiv.org/abs/2007.01547>


Related publications and links will appear here.

* SGD (why it works, high variance estimator etc)
* Adam
* RMS PropMixed mode-->

