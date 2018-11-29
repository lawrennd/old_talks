# Week 12: Gaussian Processes

### Neil D. Lawrence

### 15th December 2015

```{.python .input}
## Replace with material from GPSS (in prep)
```

```{.python .input}
import numpy as np
import pandas as pd
import pods
import matplotlib.pyplot as plt
import mlai
%matplotlib inline
```

### Review

* Last week: Logistic Regression and Generalised Linear Models
*
Introduced link functions and different transformations.
* Showed examples in
classification and mentioned possibilities for disease rate models (Come to
tonight's Data Hide for more!).
* This week: 
    * Gaussian Processes: non
parametric Bayesian modelling

### Gaussian Processes

* Basis function models give non-linear predictions.
*
Need to choose number and location of basis functions. 
* Gaussian processes is
a general framework (basis functions special case)
* Within the framework you
can consider models with infinite basis functions.

### Sampling a Function

**Multi-variate Gaussians**

* We will consider a
Gaussian with a particular structure of covariance
    matrix.
* Generate a
single sample from this 25 dimensional Gaussian distribution,
$\mathbf{f}=\left[f_{1},f_{2}\dots f_{25}\right]$.

* We will plot these points
against their index.

```{.python .input}
# %load -s compute_kernel mlai.py
def compute_kernel(X, X2, kernel, **kwargs):
    K = np.zeros((X.shape[0], X2.shape[0]))
    for i in np.arange(X.shape[0]):
        for j in np.arange(X2.shape[0]):
            K[i, j] = kernel(X[i, :], X2[j, :], **kwargs)
        
    return K

```

```{.python .input}
# %load -s exponentiated_quadratic mlai.py
def exponentiated_quadratic(x, x_prime, variance=1., lengthscale=1.):
    "Exponentiated quadratic covariance function."
    squared_distance = ((x-x_prime)**2).sum()
    return variance*np.exp((-0.5*squared_distance)/lengthscale**2)        

```

```{.python .input}
fig, ax = plt.subplots(figsize=((5,5)))
x = np.linspace(-1, 1, 25)[:, None]
K = compute_kernel(x, x, exponentiated_quadratic, lengthscale=0.3)
ax.matshow(K)
ax.set_xlabel('$i$',fontsize=16)
ax.set_ylabel('$j$',fontsize=16)
#ax.set_co
```

```{.python .input}
close all
K = kernCompute(kern, x);
ax = axes('position', [0 0 1 1])
plotMatrix(K, ax, 'none', 'imagesc')
colorbar

t = [];
t = [t xlabel('$\dataIndex$')];
t = [t ylabel('$\dataIndexTwo$')];
printLatexPlot('gpSampleCovariance', '../../../gp/tex/diagrams/', 0.4*textWidth);

clf
% need to take the real part of the sample as the kernel is numerically less than full rank 
f = real(gsamp(zeros(1, size(x, 1)), K, 1))';

a = plot(f, 'x', 'color', blackColor);
t = [t xlabel('$\dataIndex$')];
t = [t ylabel('$\mappingFunction_\dataIndex$')];
set(gca, 'ylim', [-2 2])
set(gca, 'xlim', [0 26])
set(gca, 'ytick', [-2 -1 0 1 2])
set(a,'markersize', 5)
set(a, 'linewidth', 6)
box off
xlim = get(gca, 'xlim');
ylim = get(gca, 'ylim');
line([xlim(1) xlim(1)], ylim, 'color', blackColor)
line(xlim, [ylim(1) ylim(1)], 'color', blackColor)

printLatexPlot('gpSampleValue', '../../../gp/tex/diagrams/', 0.4*textWidth);
yLim = get(gca, 'ylim');
xLim = get(gca, 'xlim');
ySpan = yLim(2) - yLim(1);
xSpan = xLim(2) - xLim(1);
chand = oval([1 f(1)], 0.025*xSpan, 0.025*ySpan);
chand = [chand oval([2 f(2)], 0.025*xSpan, 0.025*ySpan)];
set(chand, 'color', magentaColor, 'linewidth', 3)
printLatexPlot('gpSampleValue12', '../../../gp/tex/diagrams/', 0.4*textWidth);

clf
options = plotMatrixOptions;
options.color = blackColor;
options.highlight.on = true;
options.highlight.row = [1 2];
options.highlight.col= [1 2];
options.highlight.color = magentaColor;
options.highlight.width = 10;
ax = axes('position', [0 0 1 1])      
plotMatrix(K, ax, 'none', 'imagesc', options)
colorbar
printLatexPlot('gpSampleCovariance12a', '../../../gp/tex/diagrams/', 0.4*textWidth);

options.zoom.on = true;
options.zoom.row = [1 10];
options.zoom.col = [1 10];

cla(ax)
plotMatrix(K, ax, 'none', 'imagesc', options)
colorbar
printLatexPlot('gpSampleCovariance12b', '../../../gp/tex/diagrams/', 0.4*textWidth);

options.zoom.on = true;
options.zoom.row = [1 5];
options.zoom.col = [1 5];

cla(ax)
plotMatrix(K, ax, 'none', 'imagesc', options)
colorbar
printLatexPlot('gpSampleCovariance12c', '../../../gp/tex/diagrams/', 0.4*textWidth);

options.zoom.on = true;
options.zoom.row = [1 3];
options.zoom.col = [1 3];

plotMatrix(K, ax, 'none', 'imagesc', options)
colorbar 
printLatexPlot('gpSampleCovariance12d', '../../../gp/tex/diagrams/', 0.4*
textWidth);

options.zoom.on = true;
options.zoom.row = [1 2];
options.zoom.col = [1 2];

plotMatrix(K, ax, 'none', 'imagesc', options)
colorbar 
printLatexPlot('gpSampleCovariance12e', '../../../gp/tex/diagrams/', 0.4*
textWidth);

clf
options.highlight.on = false;
options.zoom.on = false;
options.bracketWidth = 10;
ax = axes('position', [0 0 1 1])      
plotMatrix(K([1 2], [1 2]), ax, 'square', 'values', options)
printLatexPlot('gpSampleCovariance12f', '../../../gp/tex/diagrams/', 0.4*textWidth);


clf
options.highlight.on = false;
options.zoom.on = false;
options.bracketWidth = 10;
ax = axes('position', [0 0 1 1])      
plotMatrix(K([1 5], [1 5]), ax, 'square', 'values', options)
printLatexPlot('gpSampleCovariance15f', '../../../gp/tex/diagrams/', 0.4*textWidth);

save gpdistfunc K x f
  
```

### Gaussian Distribution Sample

## Log Odds

* model the *log-odds* with the basis functions.
*
[odds](http://en.wikipedia.org/wiki/Odds) are defined as the ratio of the
probability of a positive outcome, to the probability of a negative outcome. 
*
Probability is between zero and one, odds are:
    $$ \frac{\pi}{1-\pi} $$
*
Odds are between $0$ and $\infty$. 
* Logarithm of odds maps them to $-\infty$
to $\infty$.

### Logit Link Function

* The [Logit
function](http://en.wikipedia.org/wiki/Logit), $$g^{-1}(\pi_i) =
\log\frac{\pi_i}{1-\pi_i}.$$ This function is known as a *link function*.

* For
a standard regression we take,
    $$f(\mathbf{x}_i) = \mathbf{w}^\top
\boldsymbol{\phi}(\mathbf{x}_i),$$
* For classification we perform a logistic
regression. 
    $$\log \frac{\pi_i}{1-\pi_i} = \mathbf{w}^\top
\boldsymbol{\phi}(\mathbf{x}_i)$$

### Inverse Link Function

We have defined the link function as taking the form
$g^{-1}(\cdot)$ implying that the inverse link function is given by $g(\cdot)$.
Since we have defined,
$$
g^{-1}(\pi(\mathbf{x})) = \mathbf{w}^\top
\boldsymbol{\phi}(\mathbf{x})
$$
we can write $\pi$ in terms of the *inverse
link* function, $g(\cdot)$ as 
$$
\pi(\mathbf{x}) = g(\mathbf{w}^\top
\boldsymbol{\phi}(\mathbf{x})).
$$

```{.python .input}
fig, ax = plt.subplots(figsize=(14,7))
f = np.linspace(-8, 8, 100)
g = 1/(1+np.exp(-f))

ax.plot(f, g, 'r-')
ax.set_title('Logistic Function', fontsize=20)
ax.set_xlabel('$f_i$', fontsize=20)
ax.set_ylabel('$g_i$', fontsize=20)
plt.savefig('./diagrams/logistic.svg')
```

### Logistic function

*
[Logistic](http://en.wikipedia.org/wiki/Logistic_function) (or sigmoid) squashes
real line to between 0   & 1. Sometimes also called a 'squashing function'.
![](./diagrams/logistic.svg)


### Prediction Function
* Can now write $\pi$ as a function of the input and
the parameter vector as, $$\pi(\mathbf{x},\mathbf{w}) = \frac{1}{1+
\exp\left(-\mathbf{w}^\top \boldsymbol{\phi}(\mathbf{x})\right)}.$$

* Compute
the output of a standard linear basis function composition ($\mathbf{w}^\top
\boldsymbol{\phi}(\mathbf{x})$, as we did for linear regression)

* Apply the
inverse link function, $g(\mathbf{w}^\top \boldsymbol{\phi}(\mathbf{x}))$. 

*
Use this value in a Bernoulli distribution to form the likelihood.

### Bernoulli Reminder

* From last time $$P(y_i|\mathbf{w}, \mathbf{x}) =
\pi_i^{y_i} (1-\pi_i)^{1-y_i}$$

* Trick for switching betwen probabilities
```python
def bernoulli(y, pi):
    if y == 1:
        return pi
    else:
return 1-pi
```

### Maximum Likelihood


* Conditional independence of
data:$$P(\mathbf{y}|\mathbf{w}, \mathbf{X}) = \prod_{i=1}^n P(y_i|\mathbf{w},
\mathbf{x}_i). $$

### Log Likelihood

\begin{align*}
\log P(\mathbf{y}|\mathbf{w}, \mathbf{X}) = &
\sum_{i=1}^n \log P(y_i|\mathbf{w}, \mathbf{x}_i) \\ = &\sum_{i=1}^n y_i \log
\pi_i \\ & + \sum_{i=1}^n (1-y_i)\log (1-\pi_i)
\end{align*}

### Objective Function

* Probability of positive outcome for the $i$th data
point $$\pi_i = g\left(\mathbf{w}^\top \boldsymbol{\phi}(\mathbf{x}_i)\right),$$
where $g(\cdot)$ is the *inverse* link function

* Objective function of the
form \begin{align*}
E(\mathbf{w}) = & -  \sum_{i=1}^n y_i \log
g\left(\mathbf{w}^\top \boldsymbol{\phi}(\mathbf{x}_i)\right) \\& -
\sum_{i=1}^n(1-y_i)\log \left(1-g\left(\mathbf{w}^\top
\boldsymbol{\phi}(\mathbf{x}_i)\right)\right).
\end{align*}

### Minimize Objective

* Grdient wrt  $\pi(\mathbf{x};\mathbf{w})$
\begin{align*}
\frac{\text{d}E(\mathbf{w})}{\text{d}\mathbf{w}} = &
-\sum_{i=1}^n \frac{y_i}{g\left(\mathbf{w}^\top
\boldsymbol{\phi}(\mathbf{x})\right)}\frac{\text{d}g(f_i)}{\text{d}f_i}
\boldsymbol{\phi(\mathbf{x}_i)} \\ & +  \sum_{i=1}^n
\frac{1-y_i}{1-g\left(\mathbf{w}^\top
\boldsymbol{\phi}(\mathbf{x})\right)}\frac{\text{d}g(f_i)}{\text{d}f_i}
\boldsymbol{\phi(\mathbf{x}_i)}
\end{align*}

### Link Function Gradient

* Also need gradient of inverse link function wrt
parameters.
\begin{align*}
g(f_i) &= \frac{1}{1+\exp(-f_i)}\\
&=(1+\exp(-f_i))^{-1}
\end{align*}
and the gradient can be computed as
\begin{align*}
\frac{\text{d}g(f_i)}{\text{d} f_i} & =
\exp(-f_i)(1+\exp(-f_i))^{-2}\\
& = \frac{1}{1+\exp(-f_i)}
\frac{\exp(-f_i)}{1+\exp(-f_i)} \\
& = g(f_i) (1-g(f_i))
\end{align*}

### Objective Gradient

\begin{align*}
\frac{\text{d}E(\mathbf{w})}{\text{d}\mathbf{w}} = & -\sum_{i=1}^n
y_i\left(1-g\left(\mathbf{w}^\top \boldsymbol{\phi}(\mathbf{x})\right)\right)
\boldsymbol{\phi(\mathbf{x}_i)} \\ & + \sum_{i=1}^n
(1-y_i)\left(g\left(\mathbf{w}^\top \boldsymbol{\phi}(\mathbf{x})\right)\right)
\boldsymbol{\phi(\mathbf{x}_i)}.
\end{align*}

### Optimization of the Function

* Can't find a stationary point of the
objective function analytically.

* Optimization has to proceed by *numerical
methods*. 
    * [Newton's
method](http://en.wikipedia.org/wiki/Newton%27s_method) or 
    * [gradient
based optimization methods](http://en.wikipedia.org/wiki/Gradient_method)
* Similarly to matrix factorization, for large data *stochastic gradient
descent*  (Robbins Munroe optimization procedure) works well.

### Ad Matching for Facebook

* This approach used in many internet companies.
* Example: ad matching for Facebook.
    * Millions of advertisers
    *
Billions of users
    * How do you choose who to show what?
    
* Logistic
regression used in combination with [decision trees]()

* [Paper available
here](http://www.herbrich.me/papers/adclicksfacebook.pdf)

### Other GLMs

* Logistic regression is part of a family known as *generalized
linear models*

* They all take the form $$g^{-1}(f_i(x)) = \mathbf{w}^\top
\boldsymbol{\phi}(\mathbf{x}_i)$$

* As another example let's look at *Poisson
regression*.

### Poisson Distribution

* Poisson distribution is used for 'count data'. For
non-negative integers, $y$, $$P(y) = \frac{\lambda^y}{y!}\exp(-y)$$

* Here
$\lambda$ is a *rate* parameter that can be thought of as the number of arrivals
per unit time.

* Poisson distributions can be used for disease count data. E.g.
number of incidence of malaria in a district.

```{.python .input}
from scipy.stats import poisson
fig, ax = plt.subplots(figsize=(14,7))
y = np.asarray(range(0, 16))
p1 = poisson.pmf(y, mu=1.)
p3 = poisson.pmf(y, mu=3.)
p10 = poisson.pmf(y, mu=10.)

ax.plot(y, p1, 'r.-', markersize=20, label='$\lambda=1$')
ax.plot(y, p3, 'g.-', markersize=20, label='$\lambda=3$')
ax.plot(y, p10, 'b.-', markersize=20, label='$\lambda=10$')
ax.set_title('Poisson Distribution', fontsize=20)
ax.set_xlabel('$y_i$', fontsize=20)
ax.set_ylabel('$p(y_i)$', fontsize=20)
ax.legend(fontsize=20)
plt.savefig('./diagrams/poisson.svg')

```

### Poisson Distribution

![](./diagrams/poisson.svg)

### Poisson Regression

* In a Poisson regression make rate a function of
space/time.$$\log \lambda(\mathbf{x}, t) = \mathbf{w}_x^\top
\boldsymbol{\phi_x(\mathbf{x})} + \mathbf{w}_t^\top \boldsymbol(\phi_t(t))$$

*
This is known as a *log linear* or *log additive* model. 

* The link function
is a logarithm.

* We can rewrite such a function as 
$$\log \lambda(\mathbf{x},
t) = f_x(\mathbf{x}) + f_t(t)$$

### Multiplicative Model

* Be careful though ... a log additive model is really
multiplicative.
$$\log \lambda(\mathbf{x}, t) = f_x(\mathbf{x}) + f_t(t)$$

*
Becomes $$\lambda(\mathbf{x}, t) = \exp(f_x(\mathbf{x}) + f_t(t))$$

* Which is
equivalent to  $$\lambda(\mathbf{x}, t) = \exp(f_x(\mathbf{x}))\exp(f_t(t))$$

*
Link functions can be deceptive in this way.

#### Reading

- Section 5.2.2 of @Rogers:book11 up to pg 182.
