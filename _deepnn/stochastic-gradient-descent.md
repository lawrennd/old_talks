---
layout: lecture
title: Stochastic Optimization
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
youtube: GDyD8KwSfvk
reveal: true
time: "14:00"
start: "14:00"
end: "15:00"
date: 2022-02-01
---


\notes{You can find the [slides here](https://hackmd.io/@fhuszar/Hy69Wvrg_) and the [notes here](https://hackmd.io/@fhuszar/rJWAWC7gO).}

\slides{
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

\subsection{Improving SGD: Two key ideas}

* idea 1: momentum
    * **problem:**
        * high variance of gradients due to stochasticity
        * oscillation in narrow valley situation
    * **solution**: maintain running average of gradients

https://distill.pub/2017/momentum/

\subsection{Improving SGD: two key ideas}

* idea 2: adaptive stepsizes
    * **problem**:
        * parameters have different magnitude gradients
        * some parameters tolerate high learning rates, others don't
    * **solution**: normalize by running average of gradient magnitudes

\subsection{Adam: combines the two ideas}

![](https://i.imgur.com/MpiCllk.png)

\subsection{How good is Adam?}

optimization vs. generalisation

\subsection{How good is Adam?}

![](https://i.imgur.com/0yelxmm.png)

\subsection{How good is Adam?}

![](https://i.imgur.com/5rAyMYc.png)

\subsection{Revisiting the cartoon example}

![](https://i.imgur.com/xRYHk0m.png =1200x)

\subsection{Can we describe SGD's behaviour?}

![](https://i.imgur.com/AyrSiFZ.png)

\subsection{Analysis of mean iterate}

![](https://i.imgur.com/9j85UIv.png)

([Smith et al, 2021](https://arxiv.org/abs/2101.12176)) "On the Origin of Implicit Regularization in Stochastic Gradient Descent"

\subsection{Implicit regularization in SGD}

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

\subsection{Is Stochastic Training Necessary?}

![](https://i.imgur.com/1WThiku.png)

\subsection{Is Stochastic Training Necessary?}

![](https://i.imgur.com/dHJKsKS.png)

* reg $\approx$ flatness of minimum
* bs32 $\approx$ variance of gradients size 32 batches

\subsection{SGD summary}

* gradient noise is a feature not bug
* SGD avoids regions with high gradient noise
* this may help with generalization
* improved SGD, like Adam, may not always help
* an optimization algorithm can be "too good"
}
\notes{
# Stochastic Gradient Descent

In previous lectures we described gradient descent as follows:

$$
\mathbb{w}_{t+1} = \mathbf{w}_t - \eta \nabla_\mathbf{w}\hat{L}(\mathbf{w}, \mathcal{D}),
$$

where $\hat{L}$ is the empirical loss function evaluated at the training data $\mathcal{D}$. For models trained on large datasets this is both computationally prohibitive and unneccessary:
* Calculating $\hat{L}$ requies us to sum up the loss on all datapoints. There might be too many datapoints in our training example to loop through for a each gradient update of our parameters.
* If the gradients are to be calculated on a GPU or similarr device, we have to move the data close to the computation, which limits the amount of data we can use at once, because the device memory is limited.
* Since the empirical loss is a sum over datapoints, even a sample of data will give you a good estimate of the empirical loss.

So instead, in deep learning we use stochastic gradient descent, in particular something like this:

$$
\mathbb{w}_{t+1} = \mathbf{w}_t - \eta \nabla_\mathbf{w}\hat{L}(\mathbf{w}, \mathcal{D}_t),
$$

where $\mathcal{D}_t$ is a random subset (called a minibatch) of training data at each step. The empirical loss, and its gradient, evaluated on a minibatch is an *unbiased* estimate of the empirical loss on the whole training set. This means that in expectation, we get the same result. The method is called stochastic because it uses random gradient estimates. The smaller the minibatch, the larger the variance of this random gradient is going to be in each step - the more stochastic the optimization algorithm becomes.

## Convergence

Turns out, stochastic gradient descent (SGD) still converges, despite the random gradient estimates. But to analyse SGD convergence, we need different types of theorems, and also different notions of convergence.

A core tool for proving SGD convergence are Doob's martingale convergence theorems. A martingale is a stochastic process (sequence of random variables) $X_1, X_2, \ldots$ such that the following equality holds:

$$
\mathbb{E}[X_n \vert X_{n-1}, \ldots, X_1] = X_{n-1}
$$

In other words, a martingale's doesn't grow or shrink in expectation. SGD is going to be a super-martingale, which has the following property:

$$
\mathbb{E}[X_n \vert X_{n-1}, \ldots, X_1] \leq X_{n-1},
$$

that is, it's a stochastic process that on average decreases its value (this is of course a very informal description).

Doob's martingale convergence theorem states that if a super-martingale has a finite lower-bound, it will converge in probability to a limiting random variable $X_\infty$.

Unbiased-ness of gradients is an immportant property that guarantees that the empirical loss in SGD is non-decreasing on average, that it forms a super-martingale. This is a rough sketch of the type of proof one can construct.

First of all, consider the Taylor expansion of the empirical loss $\hat{L}$ around the current parameter $\mathbf{w}_t$ and express the loss of the next iterate $\mathbf{w}_{t+1}$

\begin{align}
\hat{L}(\mathbf{w}_{t+1}, \mathcal{D}) &= \hat{L}(\mathbf{w}_{t} - \eta \mathbf{g}_t, \mathcal{D})\\
& \leq \hat{L}(\mathbf{w}_t, \mathcal{D}) - \eta\mathbf{g}^T_t\nabla_\theta\hat{L}(\mathbf{w}_t, \mathcal{D}) + \eta^2 C(\mathbf{w}_t),
\end{align}

where $\mathbf{g}_t$ is the stochastic gradient at step $t$, and $\eta^2 C(\hat{L})$ is an upper bound on the error of the first-order Taylor expansion. The term $C(\mathbf{w}_t)$ depends on the curvature of the empirical loss $\hat{L}$ around $\mathbf{w}_t$.

What we need to show for the super-martingale property is that the second term $\mathbf{g}^T_t\nabla_\theta\hat{L}(\mathbf{w}_t, \mathcal{D})$ is non-negative on average. This is true since:

$$
\mathbb{E}\left[\mathbf{g}^T_t\nabla_\theta\hat{L}(\mathbf{w}_t, \mathcal{D})\right] = \mathbb{E}\left[\mathbf{g}^T_t\right]\nabla_\theta\hat{L}(\mathbf{w}_t, \mathcal{D}) = \left\|\nabla_\theta\hat{L}(\mathbf{w}_t, \mathcal{D})\right\|^2 \geq 0
$$

### Note on second-order SGD

The above argument for convergence still holds so long as

$$
\mathbb{E}\left[\left(\mathbf{w}_{t+1} - \mathbf{w}_{t}\right)^T\nabla_\theta\hat{L}(\mathbf{w}_t, \mathcal{D})\vert \mathbf{w}_t\right] \geq 0$
$$

This means that if $F(\mathbf{w})$ is a positive definite matrix , convergence of the following second-order SGD is also guaranteed:

$$
\mathbf{w}_{t+1} = \mathbf{w}_t - \eta F(\mathbf{w}_t)\nabla_\mathbf{w}\hat{L}(\mathbf{w}, \mathcal{D}_t)
$$

An example of such second order methods in deep learning is natural gradient descent.

## Behaviour of SGD

So we know that SGD works in the sense that it converges, but does it converge to the same things gradient descent does? The answer is yes and no. SGD, like GD converges to local minima of the loss, for sufficiently small learning rates. However, they may have a different preference as to which local minimum they will find. Consider two local minima illustrated in the cartoon drawings below:

![](https://i.imgur.com/xRYHk0m.png =1200x)

Both panels illustrate a local minimum of the empirical loss $\hat{L}(\mathbf{w}, \mathcal{D})$ (yellow curve). I drew this so that that both minima have the same curvature, and the same general shape - the yellow curves on left-hand and right-hand panels are exactly the same.

However, the same average loss arises in very different ways in the two situations. In the left-hand situation, all minibatches (blue and purple curves) largely agree on what the loss is. The variance of loss gradients across minibatches is small. On the right-hand panel the average loss is the average of lots of very different minibatch losses. The minibatches disagree substantially, and the variance of the gradients is high.

Intuitively we expect SGD to have an easier time converging when it is in the situation illustrated in the left-hand panel, while it will have a hard time with the right-hand situation. It's likely that a large gradient will catapult it out of the vicinity of that minimum before it could converge.

Deep learning loss functions contain multiple local minima. As discussed earlier, many of these local minima could be virtually indistinguishably good on the training set. However, it is concievable that the different local minnima behave very differently in terms of the noise distribution of minibatch gradients, i.e. the same loss function can have multiple local minima, some behaving like the left-hand panel, some like the right-hand panel.

Between these different minima, the training loss function (and gradient descent) may not be able to differentiate, they look equally good. But SGD may have a preference. In this sense, the behaviour of SGD is not explained by just looking at the behaviour of the empirical loss surface. We will return to this idea later on in the notes.

## Variants of SGD

### Momentum

Momentum is an idea that can be used not just in stochastic optimization, but in gradient-based optimization in general. The figure below, taken from from ([Goh, 2017](https://distill.pub/2017/momentum/)), illustrates the typical 'narrow valley' motivating example 

![](https://i.imgur.com/0Yca4kQ.png)

Imagine that a local mimimum is inside a narrow valley, i.e. in a region where the loss function is very flat along one direction of space, but increases very sharply ina perpendicular direction.

In a narrow valley, the problem is that gradient descent can get into an oscillatory behaviour. Since the gradients perpendicular to the valley grow faster, the algorithm can keep bouncing off the walls as shown by the red curve in the figure. If we set the learning rate too high, this oscillation can be so extreme that we are catapulted out of the vicinity of the valley, never being able to converge to the minimum. The oscillation can be remedied by reducing the learning rate. This, however, also slows down progress along the direction where gradients are much smaller, so we will converge but very slowly, as the blue curve illustrates.

Momentum helps by accumulating and averaging gradients from multiple timesteps. This way, along directions where the gradient keeps changing direction or is very noisy, momentum averages these oscillations out so we are less sensitive to the individual large gradients. In dimensions where the gradient points consistently in the same direction, momentum is able to continue taking steps.

The version of momentum that the best known SGD variant Adam uses is based on exponential moving averages:

\begin{align}
\mathbf{m}_{t+1} &= \beta \mathbf{m}_{t} + (1-\beta) \nabla_\mathbf{w}\hat{L}(\mathbf{w}_t, \mathcal{D}_t)\\
\mathbf{w}_{t+1} &= \mathbf{w}_t - \eta \mathbf{m}_t
\end{align}

The figure above was taken from the excellent illustration by ([Goh, 2017](https://distill.pub/2017/momentum/)), where you can play with different parameters and see how gradient descent with momentum behaves. I encourage you to check this out as well as some of the other great content on [Distill](https://distill.pub/).

Note by: Mathematically, the narrow valley happens when the largest and smallest eigenvalues of the Hessian are very different. The eigenvalues of the Hessian describe the rate of change in the gradient along the direction described by the corresponding eigenvector. So if the largest eigenvalue is much larger than the smallest, we are in a "narrow valley" situation within the 2D slice of the loss function along the eigenvectors corresponding to those eigenvalues. The ratio of the largest and smallest eigenvalue is called the [condition number](https://en.wikipedia.org/wiki/Condition_number), and when this is very high, we call the problem ill-conditioned.

### Adaptive learning rates

Another issue with gradient descent is that gradients along different directions can vary greatly in magnitude. This means that, since we have a single learning rate $\eta$ to control the speed of movement, along some directions we move around much faster than others. A common technique is to adjust the speed of movement, i.e. effective learning rate, along each dimensions, so that the algorithm roughly takes the same amount of progress along each coordinate in each step.

Adam and RMSProp do this by keeping a moving average of the square gradient around each coordinate, and then dividing the update by the square root of this average. Here is a longer blogpost motivating the [RMSProp algorithm](https://towardsdatascience.com/understanding-rmsprop-faster-neural-network-learning-62e116fcf29a).

### Adam

Adam is a very commonly used optimization algorithm which conbines the idea of momentum with the adaptive learning rate idea from RMSProp. A basic version of the algorithm works as follows:

\begin{align}
\mathbf{m}_{t+1} &= \beta_1 \mathbf{m}_{t} + (1-\beta_1) \nabla_\mathbf{w}\hat{L}(\mathbf{w}_t, \mathcal{D}_t)\\
\mathbf{v}_{t+1} &= \beta_2 \mathbf{v}_{t}+ (1-\beta_2) \nabla_\mathbf{w}\hat{L}(\mathbf{w}_t, \mathcal{D}_t)^2\\
\mathbf{w}_{t+1} &= \mathbf{w}_t - \eta \frac{\mathbf{m}_t}{\sqrt{v_t} + \epsilon}
\end{align}

In the second line, $\nabla_\mathbf{w}\hat{L}(\mathbf{w}_t, \mathcal{D}_t)^2$ denotes taking the square of each coordinate of the gradient. The small constant $\epsilon$ is needed so that when $v_t$ is small, the updates don't grow out of control. The version of Adam I presented above is a simplified versionn, there are extra bias correction steps which are important at the beginning where $\mathbf{m}_t$ and $\mathbf{v}_t$ haven't yet converged to stable moving averages.

$\beta_1, \beta_2$ and $\epsilon$ are parameters of Adam. In practice, the default values implemented in deep learning frameworks mostly work very well, and people rarely change them. The learning rate $\eta$ needs to be tuned or chosen carefully.

One of the main benefits of Adam is that it works better  and more reliably out of the box than many other optimisers. It is somewhat less sensitive to choosing the right learning rate than vanilla versions of SGD, somewhat less sensitive to poor initialization, and tends to find a minimum quicker. This made Adam the default choice for many deep learning practicioners.

### But is Adam good at learning?

While Adam is superior as an optimization algorithm (i.e. converges to a minimum of the empirical loss quicker and is less sensitive to parameter choices), it has been questioned whether it is also good from a generalisation perspective. As discussed in the notes on [deep learning generalisation](https://hackmd.io/75gt3X6WQbu1_A3pF8svWg), and in lecture 3, deep learning generalisation may critically depend on which local minimum the optimisation algorithm finds, not how quickly and robustly a minimum is found.

The question whether Adam and similar algorithms have a positive or negative effect on generalisation was first studied by [Wilson et al (2018)](https://arxiv.org/pdf/1705.08292.pdf). The conclusion of that paper is that from the perspective of generalisation, well-tuned versions of basic stochastic gradient descent often outperform Adam. So be aware of this.

What people often do is use Adam in the first phase of development or when developing a minimal working example or proof of concept of an idea. But when performance is important, and once the architecture/loss function is unlikely to change, people often switch to other optimisation techniques, including well-tuned basic versions of SGD.

### An optimizer can be too good at optimizing

Adam is not the only example of a learning algorithm that is good at optimizing stochastic objectives, but won't improve or outright hurt performance in deep learning. Another example was a self-tuning optimizer by [Chen et al, (2021)](https://openreview.net/pdf?id=eHDmRRDkP7C), which was recently presented at the ["I Can't Believe It's Not Better" workshop at NeurIPS](https://i-cant-believe-its-not-better.github.io/).

### Why better optimizers may not work better?

Let's return to the cartoon example of the two local minima - one with low gradient noise, and one with high gradient noise.

![](https://i.imgur.com/xRYHk0m.png =1200x)

I wrote before that SGD may have a tendency to find minima with lower gradient noise (left panel). Adam "fixes" this, and helps converge even in situations where the gradients are noisier. But is it worth doing?

An intuitive argument can be made that minima with lower minibatch noise may be preferrable from the perspective of generalisation. Regions where the loss function is not very sensitive to the particular minibatch we pick will also probably be less sensitive to whether we evaluate the loss on training or on test data. One can use the variance of minibatch losses as a rough proxy for the difference between training and test loss, which is generalisation.

So what we intuitively think is going on:
1. SGD has a built-in preference for minima that have lower gradient noise across minibatches
2. minima with lower gradient noise may generalise better
3. Adam "improves" SGD so that it can now more easily converge to local minima with higher gradient noise. 

As a consequence, Adam may have inadvertently taken out the magic sauce that made SGD work so well from the perspective of generalisation.

## Further Reading

The paper I covered in the lecture on the analysis of the mean iterate in SGD is an interesting read: ([Smith et al, 2021](https://arxiv.org/abs/2101.12176)) "On the Origin of Implicit Regularization in Stochastic Gradient Descent". I don't cover this in the notes because the paper itself is clearly written. The summary is that it is possible to analyse the behaviour of SGD "on average". The resulting analysis confirms our intuitive story that SGD converges to minima where the minibatch noise is lower.

An extensive review of stochastic optimisation can be found in ([Buttou et al, 2017](https://arxiv.org/pdf/1606.04838.pdf)), which I highly recommend.

Here is a [blog post](https://www.jeremyjordan.me/nn-learning-rate/) on setting learning rates, cyclical learning rates and more. The post itself has some more links to other resources on this

As to the question of how big your batchsize should be, this has been a topic of several investigations. There are papers, like ([Keskar et al, 2017](https://arxiv.org/pdf/1609.04836.pdf)) that argue for smaller batch sizes and claim that large batchsize degrades performance. However, others have found no evidence of this empirically, and argue that large batchsizes can work, too ([Shallue et al, 2019](https://www.jmlr.org/papers/v20/18-789.html)).}
