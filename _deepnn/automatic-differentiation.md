---
layout: lecture
title: More Generalisation and Automatic Differentiation
week: 2
session: 1
author:
- given: Ferenc
  family: Huszár
  institution: University of Cambridge
  url: https://www.inference.vc/about/
abstract: >
  This lecture will cover the foundations of automatic differentiation as well as the different frameworks that exist for building models.
talkscam:
youtube: m3KZLPed7aM
hackmdslides: fhuszar/H1WZ70kl_#/
hackmdnotes: fhuszar/SyHTInWeu
hackmdworksheet: fhuszar/S1UdOvZe_
time: "14:00"
start: "14:00"
end: "15:00"
date: 2021-01-28
---

\include{talk-macros.gpp}

\notes{* [Slides are here](https://hackmd.io/@fhuszar/H1WZ70kl_#/)
* [Approximating with ReLU notes are here](https://hackmd.io/@fhuszar/S1UdOvZe_)
* [Automatic Differentiaton notes are here](https://hackmd.io/@fhuszar/SyHTInWeu)
* [Google Colab Is Available Here](https://colab.research.google.com/drive/1qioPLq-dxOwudPKXU3MxpHr2s4Su3dxI?usp=sharing)


* Nice review paper from <https://jmlr.org/papers/v18/17-468.html> @Baydin-autodiff18 (See Figure 2)}

\subsection{Reddit Group}

[https://www.reddit.com/r/CST_DeepNN/](https://www.reddit.com/r/CST_DeepNN/)


## Approximation


### Basic Multilayer Perceptron

\begin{align}
f_l(x) &= \phi(W_l f_{l-1}(x) + b_l)\\
f_0(x) &= x
\end{align}


### Basic Multilayer Perceptron

$$
\small
f_L(x) = \phi\left(b_L + W_L \phi\left(b_{L-1} + W_{L-1} \phi\left( \cdots \phi\left(b_1 + W_1 x\right) \cdots \right)\right)\right)
$$


### Rectified Linear Unit

$$
\phi(x) = \left\{\matrix{0&\text{when }x\leq 0\\x&\text{when }x>0}\right.
$$

![](https://i.imgur.com/SxKdrzb.png)



### What can these networks represent?


$$
\operatorname{ReLU}(\mathbf{w}_1x - \mathbf{b}_1)
$$

![](https://i.imgur.com/rN5wRVJ.png)


### What can these networks represent?

$$
f(x) = \mathbf{w}^T_2 \operatorname{ReLU}(\mathbf{w}_1x - \mathbf{b}_1)
$$

![](https://i.imgur.com/kX3nuYg.png)


### Single hidden layer

number of kinks $\approx O($ width of network $)$


### Example: "sawtooth" network


\begin{align}
f_l(x) &= 2\vert f_{l-1}(x)\vert - 2 \\
f_0(x) &= x
\end{align}



### Sawtooth network

\begin{align}
f_l(x) &= 2 \operatorname{ReLU}(f_{l-1}(x)) + 2 \operatorname{ReLU}(-f_{l-1}(x)) - 2\\
f_0(x) &= x
\end{align}


### $0$-layer network

![](https://i.imgur.com/bRUYJD7.png)


### $1$-layer network

![](https://i.imgur.com/bQpM1dg.png)


### $2$-layer network

![](https://i.imgur.com/NxNj7VG.png)


### $3$-layer network

![](https://i.imgur.com/xlcpyP7.png)



### $4$-layer network

![](https://i.imgur.com/9GF52j7.png)


### $5$-layer network

![](https://i.imgur.com/Ku8aamk.png)


### Deep ReLU networks

number of kinks $\approx O(2^\text{depth of network})$


### In higher dimensions

![](https://i.imgur.com/0NVHFEN.png)


### In higher dimensions

![](https://i.imgur.com/DJtv5Yj.jpg)


### Approximation: summary

* depth increases model complexity more than width
* model clas defined by deep networks is VERY LARGE
* both an advantage, but and cause for concern
* "complex models don't generalize"


## Generalization


## Generalization

![](https://i.imgur.com/Tu5SHpr.png)


## Generalization

![](https://i.imgur.com/8bkhxAv.png)


## Generalization

![](https://i.imgur.com/YHedAr6.png)


## Generalization: deep nets

![](https://i.imgur.com/bfyRBsx.png)


## Generalization: deep nets
![](https://i.imgur.com/fzLYvHe.png)


## Generalization: summary

* **classical view:** generalization is property of model class and loss function
* **new view:** it is also a property of the optimization algorithm


## Generalization

* optimization is core to deep learning
* new tools and insights:
    * infinite width neural networks
    * neural tangent kernel [(Jacot et al, 2018)](https://arxiv.org/abs/1806.07572)
    * deep linear models ([e.g. Arora et al, 2019](https://arxiv.org/abs/1905.13655))
    * importance of initialization
    * effect of gradient noise


## Gradient-based optimization

$$
\mathcal{L}(\theta) = \sum_{n=1}^N \ell(y_n, f(x_n, \theta))
$$

$$
\theta_t = \theta_t - \eta \nabla_\theta L(\theta)
$$


### Basic Multilayer Perceptron

$$
\small
f_L(x) = \phi\left(b_L + W_L \phi\left(b_{L-1} + W_{L-1} \phi\left( \cdots \phi\left(b_1 + W_1 x\right) \cdots \right)\right)\right)
$$


## General deep function composition

$$
f_L(f_{L-1}(\cdots f_1(\mathbb{w})))
$$

How do I calculate the derivative of $f_L(\mathbb{w})$ with respect to $\mathbb{w}$?


## Chain rule

$$
\frac{\partial \mathbf{f}_L}{\partial \mathbb{w}} = \frac{\partial \mathbf{f}_L}{\partial \mathbf{f}_{L-1}} \frac{\partial \mathbf{f}_{L-1}}{\partial \mathbf{f}_{L-2}} \frac{\partial \mathbf{f}_{L-2}}{\partial \mathbf{f}_{L-3}} \cdots \frac{\partial \mathbf{f}_3}{\partial \mathbf{f}_{2}} \frac{\partial \mathbf{f}_2}{\partial \mathbf{f}_{1}} \frac{\partial \mathbf{f}_1}{\partial \mathbf{w}} 
$$


## How to evaluate this?

$$
\frac{\partial \mathbf{f}_L}{\partial \mathbb{w}} = \frac{\partial \mathbf{f}_L}{\partial \mathbf{f}_{L-1}} \frac{\partial \mathbf{f}_{L-1}}{\partial \mathbf{f}_{L-2}} \frac{\partial \mathbf{f}_{L-2}}{\partial \mathbf{f}_{L-3}} \cdots \frac{\partial \mathbf{f}_3}{\partial \mathbf{f}_{2}} \frac{\partial \mathbf{f}_2}{\partial \mathbf{f}_{1}} \frac{\partial \mathbf{f}_1}{\partial \mathbf{w}} 
$$

$$
\small
\frac{\partial \mathbf{f}_L}{\partial \mathbb{w}} = \frac{\partial \mathbf{f}_L}{\partial \mathbf{f}_{L-1}} \left( \frac{\partial \mathbf{f}_{L-1}}{\partial \mathbf{f}_{L-2}} \left( \frac{\partial \mathbf{f}_{L-2}}{\partial \mathbf{f}_{L-3}} \cdots \left( \frac{\partial \mathbf{f}_3}{\partial \mathbf{f}_{2}} \left( \frac{\partial \mathbf{f}_2}{\partial \mathbf{f}_{1}} \frac{\partial \mathbf{f}_1}{\partial \mathbf{w}} \right) \right) \cdots \right) \right)
$$


## Or like this?

$$
\frac{\partial \mathbf{f}_L}{\partial \mathbb{w}} = \frac{\partial \mathbf{f}_L}{\partial \mathbf{f}_{L-1}} \frac{\partial \mathbf{f}_{L-1}}{\partial \mathbf{f}_{L-2}} \frac{\partial \mathbf{f}_{L-2}}{\partial \mathbf{f}_{L-3}} \cdots \frac{\partial \mathbf{f}_3}{\partial \mathbf{f}_{2}} \frac{\partial \mathbf{f}_2}{\partial \mathbf{f}_{1}} \frac{\partial \mathbf{f}_1}{\partial \mathbf{w}} 
$$

$$
\small
\frac{\partial \mathbf{f}_L}{\partial \mathbb{w}} = \left( \left( \cdots \left( \left( \frac{\partial \mathbf{f}_L}{\partial \mathbf{f}_{L-1}} \frac{\partial \mathbf{f}_{L-1}}{\partial \mathbf{f}_{L-2}}  \right) \frac{\partial \mathbf{f}_{L-2}}{\partial \mathbf{f}_{L-3}} \right) \cdots \frac{\partial \mathbf{f}_3}{\partial \mathbf{f}_{2}} \right) \frac{\partial \mathbf{f}_2}{\partial \mathbf{f}_{1}} \right) \frac{\partial \mathbf{f}_1}{\partial \mathbf{w}} 
$$


## Or in a funky way?

$$
\frac{\partial \mathbf{f}_L}{\partial \mathbb{w}} = \frac{\partial \mathbf{f}_L}{\partial \mathbf{f}_{L-1}} \frac{\partial \mathbf{f}_{L-1}}{\partial \mathbf{f}_{L-2}} \frac{\partial \mathbf{f}_{L-2}}{\partial \mathbf{f}_{L-3}} \cdots \frac{\partial \mathbf{f}_3}{\partial \mathbf{f}_{2}} \frac{\partial \mathbf{f}_2}{\partial \mathbf{f}_{1}} \frac{\partial \mathbf{f}_1}{\partial \mathbf{w}} 
$$

$$
\small
\frac{\partial \mathbf{f}_L}{\partial \mathbb{w}} = \frac{\partial \mathbf{f}_L}{\partial \mathbf{f}_{L-1}} \left( \left( \left( \frac{\partial \mathbf{f}_{L-1}}{\partial \mathbf{f}_{L-2}}  \right) \frac{\partial \mathbf{f}_{L-2}}{\partial \mathbf{f}_{L-3}} \right) \left( \left( \cdots \frac{\partial \mathbf{f}_3}{\partial \mathbf{f}_{2}} \right) \frac{\partial \mathbf{f}_2}{\partial \mathbf{f}_{1}} \right) \right)\frac{\partial \mathbf{f}_1}{\partial \mathbf{w}} 
$$


## Automatic differentiation

### Forward-mode

$$
\small
\frac{\partial \mathbf{f}_L}{\partial \mathbb{w}} = \frac{\partial \mathbf{f}_L}{\partial \mathbf{f}_{L-1}} \left( \frac{\partial \mathbf{f}_{L-1}}{\partial \mathbf{f}_{L-2}} \left( \frac{\partial \mathbf{f}_{L-2}}{\partial \mathbf{f}_{L-3}} \cdots \left( \frac{\partial \mathbf{f}_3}{\partial \mathbf{f}_{2}} \left( \frac{\partial \mathbf{f}_2}{\partial \mathbf{f}_{1}} \frac{\partial \mathbf{f}_1}{\partial \mathbf{w}} \right) \right) \cdots \right) \right)
$$

Cost: 
$$
\small
d_0d_1d_2 + d_0d_2d_3 + \ldots + d_0d_{L-1}d_L = d_0 \sum_{l=2}^{L}d_ld_{l-1}
$$


## Automatic differentiation

### Reverse-mode 

$$
\small
\frac{\partial \mathbf{f}_L}{\partial \mathbb{w}} = \left( \left( \cdots \left( \left( \frac{\partial \mathbf{f}_L}{\partial \mathbf{f}_{L-1}} \frac{\partial \mathbf{f}_{L-1}}{\partial \mathbf{f}_{L-2}}  \right) \frac{\partial \mathbf{f}_{L-2}}{\partial \mathbf{f}_{L-3}} \right) \cdots \frac{\partial \mathbf{f}_3}{\partial \mathbf{f}_{2}} \right) \frac{\partial \mathbf{f}_2}{\partial \mathbf{f}_{1}} \right) \frac{\partial \mathbf{f}_1}{\partial \mathbf{w}} 
$$

Cost:
$$
\small
d_Ld_{L-1}d_{L-2} + d_{L}d_{L-2}d_{L-3} + \ldots + d_Ld_{1}d_0 = d_L \sum_{l=0}^{L-2}d_ld_{l+1}
$$


## Automatic differentiation

* in deep learning we're most interested in scalar objectives
* $d_L=1$, consequently, backward mode is always optimal
* in the context of neural networks: **backpropagation**
* backprop has higher memory cost than forwardprop


## Example: calculating a Hessian

$$
H(\mathbb{w}) = \frac{\partial^2}{\partial\mathbf{w}\partial\mathbf{w}^T} L(\mathbf{w})
= \frac{\partial}{\partial\mathbf{w}} \mathbf{g}(\mathbf{w})
$$


## Example: Hessian-vector product

$$
\mathbf{v}^TH(\mathbf{w}) = \frac{\partial}{\partial\mathbf{w}} \left( \mathbf{v}^T \mathbf{g}(\mathbf{w}) \right)
$$

