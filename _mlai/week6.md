---
layout: lectures
title: "Generalization: Model Validation"
author: Neil D. Lawrence
date: 2015/11/4
transition: None
---

\include{talk-macros.tex}

\setupcode{import pods
import mlai
import numpy as np
import matplotlib.pyplot as plt
import teaching_plots as plot
%matplotlib inline}

### Two Simultaneous Equations

A system of two simultaneous equations with two unknowns.

How do we deal with three simultaneous equations with only two unknowns?

$$\begin{aligned}
        \dataScalar_1 = & m\inputScalar_1 + c\\
        \dataScalar_2 = & m\inputScalar_2 + c
\end{aligned}$$ 
      
$$\begin{aligned}
        \dataScalar_1-\dataScalar_2 = & m(\inputScalar_1 - \inputScalar_2)
\end{aligned}$$  
      
$$\begin{aligned}
        \frac{\dataScalar_1-\dataScalar_2}{\inputScalar_1 - \inputScalar_2} = & m
      \end{aligned}$$ 
      
$$\begin{aligned}
        m & =\frac{\dataScalar_2-\dataScalar_1}{\inputScalar_2 - \inputScalar_1}\\
        c & = \dataScalar_1 - m \inputScalar_1
      \end{aligned}$$
$$\begin{aligned}
        \dataScalar_1 = & m\inputScalar_1 + c\\
        \dataScalar_2 = & m\inputScalar_2 + c\\
\dataScalar_3 = & m\inputScalar_3 + c
      \end{aligned}$$

\code{plot.under_determined_system()}

### Underdetermined System
* What about two unknowns and *one* observation?
  $$\dataScalar_1 =  m\inputScalar_1 + c$$

\displaycode{pods.notebook.display_plots('under_determined_system{samp:0>3}.svg', directory='./diagrams', samp=(0, 10))}

### Underdetermined System
* Can compute $m$ given $c$.
  $$m = \frac{\dataScalar_1 -c}{x}$$

### Underdetermined System

* Can compute $m$ given $c$.

Assume 
$$c \sim \gaussianSamp{0}{4},$$

### Overdetermined System

* With two unknowns and two observations:
$$\begin{aligned}
          \dataScalar_1 = & m\inputScalar_1 + c\\
          \dataScalar_2 = & m\inputScalar_2 + c
\end{aligned}$$

* Additional observation leads to *overdetermined* system.
  $$\dataScalar_3 =  m\inputScalar_3 + c$$

* This problem is solved through a noise model $\noiseScalar \sim \gaussianSamp{0}{\dataStd^2}$ 
  $$
  \begin{aligned}
  \dataScalar_1 = m\inputScalar_1 + c + \noiseScalar_1\\
          \dataScalar_2 = m\inputScalar_2 + c + \noiseScalar_2\\
          \dataScalar_3 = m\inputScalar_3 + c + \noiseScalar_3
        \end{aligned}
  $$

### Noise Models

* We aren’t modeling entire system.
* Noise model gives mismatch between model and data.
* Gaussian model justified by appeal to central limit theorem.
* Other models also possible (Student-$t$ for heavy tails).
* Maximum likelihood with Gaussian noise leads to *least squares*.

### Different Types of Uncertainty

* The first type of uncertainty we are assuming is *aleatoric* uncertainty.
* The second type of uncertainty we are assuming is *epistemic* uncertainty.

### Aleatoric Uncertainty

* This is uncertainty we couldn’t know even if we wanted to. e.g. the result of a football match before it’s played.
* Where a sheet of paper might land on the floor.

### Epistemic Uncertainty

* This is uncertainty we could in principal know the answer too. We just haven’t observed enough yet, e.g. the result of a football match *after* it’s played.
* What colour socks your lecturer is wearing.

### Reading

* @Bishop:book06 Section 1.2.3 (pg 21–24).
* @Bishop:book06 Section 1.2.6 (start from just past eq 1.64 pg 30-32).
* @Rogers:book11 use an example of a coin toss for introducing Bayesian inference Chapter 3, Sections 3.1-3.4 (pg 95-117). Although you also need the beta density which we haven’t yet discussed. This is also the example that @Laplace:memoire74 used.

<!-- -->

* Bayesian Inference
  - @Rogers:book11 use an example of a coin toss for introducing Bayesian inference Chapter 3, Sections 3.1-3.4 (pg 95-117). Although you also need the beta density which we haven’t yet discussed. This is also the example that @Laplace:memoire74 used.
  - @Bishop:book06 Section 1.2.3 (pg 21–24).
* @Bishop:book06 Section 1.2.6 (start from just past eq 1.64 pg 30-32).

### Prior Distribution

* Bayesian inference requires a prior on the parameters.
* The prior represents your belief *before* you see the data of the likely value of the parameters.
* For linear regression, consider a Gaussian prior on the intercept:
  $$c \sim \gaussianSamp{0}{\alpha_1}$$

### Posterior Distribution

* Posterior distribution is found by combining the prior with the likelihood.
* Posterior distribution is your belief *after* you see the data of the likely value of the parameters.
* The posterior is found through **Bayes’ Rule**
  $$p(c|y) = \frac{p(y|c)p(c)}{p(y)}$$

### Bayes Update

\plotcode{plot.bayes_update()}

\displaycode{pods.notebook.display_plots('dem_gaussian{stage:0>2}.svg', './diagrams/', IntSlider(1, 1, 3, 1))}

### Stages to Derivation of the Posterior

* Multiply likelihood by prior
* they are "exponentiated quadratics", the answer is always also an exponentiated quadratic because
  $$\exp(a^2)\exp(b^2) = \exp(a^2 + b^2)$$
* Complete the square to get the resulting density in the form of a Gaussian.
* Recognise the mean and (co)variance of the Gaussian. This is the estimate of the posterior.

### Main Trick

$$p(c) = \frac{1}{\sqrt{2\pi\alpha_1}} \exp\left(-\frac{1}{2\alpha_1}c^2\right)$$
$$p(\dataVector|\inputVector, c, m, \dataStd^2) = \frac{1}{\left(2\pi\dataStd^2\right)^{\frac{n}{2}}} \exp\left(-\frac{1}{2\dataStd^2}\sum_{i=1}^n(\dataScalar_i - m\inputScalar_i - c)^2\right)$$

$$p(c| \dataVector, \inputVector, m, \dataStd^2) = \frac{p(\dataVector|\inputVector, c, m, \dataStd^2)p(c)}{p(\dataVector|\inputVector, m, \dataStd^2)}$$

$$p(c| \dataVector, \inputVector, m, \dataStd^2) =  \frac{p(\dataVector|\inputVector, c, m, \dataStd^2)p(c)}{\int p(\dataVector|\inputVector, c, m, \dataStd^2)p(c) \text{d} c}$$

$$p(c| \dataVector, \inputVector, m, \dataStd^2) \propto  p(\dataVector|\inputVector, c, m, \dataStd^2)p(c)$$

$$\begin{aligned}
    \log p(c | \dataVector, \inputVector, m, \dataStd^2) =&-\frac{1}{2\dataStd^2} \sum_{i=1}^n(\dataScalar_i-c - m\inputScalar_i)^2-\frac{1}{2\alpha_1} c^2 + \text{const}\\
     = &-\frac{1}{2\dataStd^2}\sum_{i=1}^n(\dataScalar_i-m\inputScalar_i)^2 -\left(\frac{n}{2\dataStd^2} + \frac{1}{2\alpha_1}\right)c^2\\     & + c\frac{\sum_{i=1}^n(\dataScalar_i-
m\inputScalar_i)}{\dataStd^2}, \end{aligned}$$
complete the square of the quadratic form to obtain
$$\log p(c | \dataVector, \inputVector, m, \dataStd^2) = -\frac{1}{2\tau^2}(c - \mu)^2 +\text{const},$$
where $\tau^2 = \left(n\dataStd^{-2} +\alpha_1^{-1}\right)^{-1}$
and $\mu = \frac{\tau^2}{\dataStd^2} \sum_{i=1}^n(\dataScalar_i-m\inputScalar_i)$.

### The Joint Density

* Really want to know the *joint* posterior density over the parameters $c$ *and* $m$.

* Could now integrate out over $m$, but it’s easier to consider the multivariate case.

### Height and Weight Models

\plotcode{plot.height_weight()}

![](./diagrams/height_weight_gaussian.svg)

###  Sampling Two Dimensional Variables

\plotcode{plot.independent_height_weight()}

\displaycode{pods.notebook.display_plots('independent_height_weight{fig:0>3}.png', './diagrams/', fig=IntSlider(0, 0, 79, 1))
}

### Independence Assumption

* This assumes height and weight are independent.
  $$p(h, w) = p(h)p(w)$$
* In reality they are dependent (body mass index) $= \frac{w}{h^2}$.

### Sampling Two Dimensional Variables

\plotcode{plot.correlated_height_weight()}

\displaycode{pods.notebook.display_plots('correlated_height_weight{fig:0>3}.png', './diagrams/', fig=(0, 79))}

### Independent Gaussians

$$p(w, h) = p(w)p(h)$$ 
$$p(w, h) = \frac{1}{\sqrt{2\pi \dataStd_1^2}\sqrt{2\pi\dataStd_2^2}} \exp\left(-\frac{1}{2}\left(\frac{(w-\mu_1)^2}{\dataStd_1^2} + \frac{(h-\mu_2)^2}{\dataStd_2^2}\right)\right)$$

### Independent Gaussians

$$p(w, h) = \frac{1}{\sqrt{2\pi\dataStd_1^2 2\pi\dataStd_2^2}} \exp\left(-\frac{1}{2}\left(\begin{bmatrix}w \\ h\end{bmatrix} - \begin{bmatrix}\mu_1 \\ \mu_2\end{bmatrix}\right)^\top\begin{bmatrix}\dataStd_1^2& 0\\0&\dataStd_2^2\end{bmatrix}^{-1}\left(\begin{bmatrix}w \\ h\end{bmatrix} - \begin{bmatrix}\mu_1 \\ \mu_2\end{bmatrix}\right)\right)$$

### Independent Gaussians

$$p(\dataVector) = \frac{1}{\left|2\pi \mathbf{D}\right|^{\frac{1}{2}}} \exp\left(-\frac{1}{2}(\dataVector - \meanVector)^\top\mathbf{D}^{-1}(\dataVector - \meanVector)\right)$$

### Correlated Gaussian

Form correlated from original by rotating the data space using matrix $\mathbf{R}$.

$$p(\dataVector) = \frac{1}{\left|2\pi\mathbf{D}\right|^{\frac{1}{2}}} \exp\left(-\frac{1}{2}(\dataVector - \meanVector)^\top\mathbf{D}^{-1}(\dataVector - \meanVector)\right)$$

### Correlated Gaussian

$$p(\dataVector) = \frac{1}{\left|2\pi\mathbf{D}\right|^{\frac{1}{2}}} \exp\left(-\frac{1}{2}(\mathbf{R}^\top\dataVector - \mathbf{R}^\top\meanVector)^\top\mathbf{D}^{-1}(\mathbf{R}^\top\dataVector - \mathbf{R}^\top\meanVector)\right)$$

### Correlated Gaussian

$$p(\dataVector) = \frac{1}{\left|2\pi\mathbf{D}\right|^{\frac{1}{2}}}
\exp\left(-\frac{1}{2}(\dataVector - \meanVector)^\top\mathbf{R}\mathbf{D}^{-1}\mathbf{R}^\top(\dataVector - \meanVector)\right)$$
this gives a covariance matrix:
$$\covarianceMatrix^{-1} = \mathbf{R} \mathbf{D}^{-1} \mathbf{R}^\top$$

### Correlated Gaussian

$$p(\dataVector) = \frac{1}{\left|{2\pi\covarianceMatrix}\right|^{\frac{1}{2}}} \exp\left(-\frac{1}{2}(\dataVector - \meanVector)^\top\covarianceMatrix^{-1} (\dataVector - \meanVector)\right)$$
this gives a covariance matrix:
$$\covarianceMatrix = \mathbf{R} \mathbf{D} \mathbf{R}^\top$$

### Reading

* Section 2.3 of @Bishop:book06 up to top of pg 85 (multivariate Gaussians).

* Section 3.3 of @Bishop:book06 up to 159 (pg 152–159).

### Revisit Olympics Data

* Use Bayesian approach on olympics data with polynomials.

* Choose a prior $\mappingVector \sim \gaussianSamp{\zerosVector}{\alpha \eye}$ with $\alpha = 1$.

* Choose noise variance $\dataStd^2 = 0.01$

### Sampling the Prior

* Always useful to perform a ‘sanity check’ and sample from the prior before observing the data.

* Since $\dataVector = \basisMatrix \mappingVector + \noiseVector$ just need to sample
  $$w \sim \gaussianSamp{0}{\alpha}$$
  $$\noiseVector \sim \gaussianSamp{\zerosVector}{\dataStd^2}$$ 
  with $\alpha=1$ and $\dataStd^2 = 0.01$.

\code{basis = mlai.polynomial
data = pods.datasets.olympic_marathon_men()
x = data['X']
y = data['Y']
num_data = x.shape[0]

data_limits = [1892, 2020]

max_basis = y.shape[0]}

\plotcode{plot.rmse_fit(x, y, param_name='num_basis', param_range=(1, max_basis+1),  
              model=mlai.BLM, basis=basis, alpha=1, sigma2=0.04, data_limits=data_limits,
              xlim=data_limits, objective_ylim=[0.5,1.6])}

### Olympic Data with Bayesian Polynomials

\displaycode{pods.notebook.display_plots('olympic_BLM_polynomial_num_basis{num_basis:0>3}.svg', 
                            directory='./diagrams', num_basis=(1, max_basis))}

\plotcode{plot.holdout_fit(x, y, param_name='num_basis', param_range=(1, max_basis+1),  
              model=mlai.BLM, basis=basis, alpha=1, sigma2=0.04, data_limits=data_limits,
              xlim=data_limits, objective_ylim=[0.1,0.6], permute=False)}

### Hold Out Validation

\displaycode{pods.notebook.display_plots('olympic_val_BLM_polynomial_num_basis{num_basis:0>3}.svg', 
                            directory='./diagrams', num_basis=(1, 27))}

\plotcode{num_parts=5
plot.cv_fit(x, y, param_name='num_basis', param_range=(1, max_basis+1),  
              model=mlai.BLM, basis=basis, alpha=1, sigma2=0.04, data_limits=data_limits,
              xlim=data_limits, objective_ylim=[0.2,0.6], num_parts=num_parts)}

### 5-fold Cross Validation

\code{pods.notebook.display_plots('olympic_5cv{part:0>2}_BLM_polynomial_num_basis{num_basis:0>3}.svg', 
                            directory='./diagrams', part=(0, 5), num_basis=(1, max_basis))}

### Model Fit

* Marginal likelihood doesn’t always increase as model order increases.

* Bayesian model always has 2 parameters, regardless of how many basis functions (and here we didn’t even fit them).

* Maximum likelihood model over fits through increasing number of parameters.

* Revisit maximum likelihood solution with validation set.

### Regularized Mean

* Validation fit here based on mean solution for $\mappingVector$ only.

* For Bayesian solution
  $$\meanVector_w = \left[\dataStd^{-2}\basisMatrix^\top\basisMatrix + \alpha^{-1}\eye\right]^{-1} \dataStd^{-2} \basisMatrix^\top \dataVector$$
  instead of
  $$\mappingVector^* = \left[\basisMatrix^\top\basisMatrix\right]^{-1} \basisMatrix^\top \dataVector$$

* Two are equivalent when $\alpha \rightarrow \infty$.

* Equivalent to a prior for $\mappingVector$ with infinite variance.

* In other cases $\alpha \eye$ *regularizes* the system (keeps parameters smaller).

### Sampling the Posterior

* Now check samples by extracting $\mappingVector$ from the *posterior*.

* Now for $\dataVector = \basisMatrix \mappingVector + \noiseVector$ need
  $$w \sim \gaussianSamp{\meanVector_w}{\covarianceMatrix_w}$$
  with $\covarianceMatrix_w = \left[\dataStd^{-2}\basisMatrix^\top \basisMatrix + \alpha^{-1}\eye\right]^{-1}$
  and $\meanVector_w =\covarianceMatrix_w \dataStd^{-2} \basisMatrix^\top \dataVector$
  $$\noiseVector \sim \gaussianSamp{\zerosVector}{\dataStd^2\eye}$$ 
  with $\alpha=1$ and $\dataStd^2 = 0.01$.

### Marginal Likelihood

* The marginal likelihood can also be computed, it has the form:
  $$p(\dataVector|\inputMatrix, \dataStd^2, \alpha) =
\frac{1}{(2\pi)^\frac{n}{2}\left|\mathbf{K}\right|^\frac{1}{2}}
\exp\left(-\frac{1}{2} \dataVector^\top \mathbf{K}^{-1} \dataVector\right)$$
  where $\mathbf{K} = \alpha \basisMatrix\basisMatrix^\top + \dataStd^2 \eye$.

* So it is a zero mean $n$-dimensional Gaussian with covariance matrix $\mathbf{K}$.

### Computing the Expected Output

* Given the posterior for the parameters, how can we compute the expected output at a given location?

* Output of model at location $\inputVector_i$ is given by
  $$f(\inputVector_i; \mappingVector) = \basisVector_i^\top \mappingVector$$

* We want the expected output under the posterior density, $p(\mappingVector|\dataVector, \inputMatrix, \dataStd^2, \alpha)$.
* Mean of mapping function will be given by 
  $$\begin{aligned} \left\langle f(\inputVector_i; \mappingVector)\right\rangle_{p(\mappingVector|\dataVector, \inputMatrix, \dataStd^2, \alpha)} &= \basisVector_i^\top \left\langle\mappingVector\right\rangle_{p(\mappingVector|\dataVector, \inputMatrix, \dataStd^2, \alpha)} \\  & = \basisVector_i^\top \meanVector_w \end{aligned}$$

### Variance of Expected Output

*   Variance of model at location
$\inputVector_i$ is given by
    $$\begin{aligned}
\text{var}(f(\inputVector_i; \mappingVector)) &= \left\langle(f(\inputVector_i;
\mappingVector))^2\right\rangle - \left\langle f(\inputVector_i;
\mappingVector)\right\rangle^2 \\&= \basisVector_i^\top
\left\langle\mappingVector\mappingVector^\top\right\rangle \basisVector_i -
\basisVector_i^\top
\left\langle\mappingVector\right\rangle\left\langle\mappingVector\right\rangle^\top
\basisVector_i \\&= \basisVector_i^\top
\covarianceMatrix_i\basisVector_i
        \end{aligned}$$ where all these
expectations are taken under the
    posterior density,
$p(\mappingVector|\dataVector, \inputMatrix, \dataStd^2, \alpha)$.

### Reading

*   Section 3.7–3.8 of @Rogers:book11 (pg 122–133).

*   Section
3.4 of @Bishop:book06 (pg 161–165).

At the beginning of this course, we motivated the introduction of probability by considering systems where there were more observations than unknowns. In particular we though about the simple fitting of the gradient and an offset of a line,
$$ y= mx +c $$
and what happens if we have three pairs of observations of $x$ and $y$, $\{\inputScalar_i, \dataScalar_i\}_{i=1}^3$. We solved this issue by introducing a type of [slack variable](http://en.wikipedia.org/wiki/Slack_variable), $\noiseScalar_i$, known as noise, such that for each observation we had the equation,
$$\dataScalar_i = m\inputScalar_i + c + \noiseScalar_i.$$

### Underdetermined System

In contrast, today we'd like to consider the situation where you have more parameters than data in your simultaneous equation. So we have an *underdetermined* system. In fact this set up is in some sense *easier* to solve, because we don't need to think about introducing a slack variable (although it might make a lot of sense from a *modelling* perspective to do so).

In the overdetermined system, we resolved the problem by introducing slack variables, $\noiseScalar_i$, which needed to be estimated for each point. The slack variable represented the difference between our actual prediction and the true observation. This is known as the *residual*. By introducing the slack variable we now have an additional $n$ variables to estimate, one for each data point, $\{\noiseScalar_i\}$. This actually turns the overdetermined system into an underdetermined system. Introduction of $n$ variables, plus the original $m$ and $c$ gives us $n+2$ parameters to be estimated from $n$ observations, which actually makes the system *underdetermined*. However, we then made a probabilistic assumption about the slack variables, we assumed that the slack variables were distributed according to a probability density. And for the moment we have been assuming that density was the Gaussian, 
$$\noiseScalar_i \sim \gaussianSamp{0}{\dataStd^2},$$ 
with zero mean and variance $\dataStd^2$. 

#### Sum of Squares and Probability

In the overdetermined system we introduced a new set of slack variables, $\{\noiseScalar_i\}_{i=1}^n$, on top of our parameters $m$ and $c$. We dealt with the variables by placing a probability distribution over them. This gives rise to the likelihood and for the case of Gaussian distributed variables, it gives rise to the sum of squares error. It was Gauss who first made this connection in his volume on "Theoria Motus Corprum Coelestium" (written in Latin)

\code{import pods
pods.notebook.display_google_book(id='ORUOAAAAQAAJ', page='213')}

The relevant section roughly translates as

... It is clear, that for the product $\Omega = h^\mu \pi ^{-frac{1}{2}\mu} e^{-hh(vv + v^\prime v^\prime + v^{\prime\prime} v^{\prime\prime} + \dots)}$ to be maximised the sum $vv + v ^\prime v^\prime + v^{\prime\prime} v^{\prime\prime} + \text{etc}.$ ought to be minimized. *Therefore, the most probable values of the unknown quantities $p , q, r , s \text{etc}.$, should be that in which the sum of the squares of the differences between the functions $V, V^\prime, V^{\prime\prime} \text{etc}$, and the observed values is minimized*, for all observations of the same degree of precision is presumed.

It's on the strength of this paragraph that the density is known as the Gaussian, despite the fact that four pages later Gauss credits the necessary integral for the density to Laplace, and it was also Laplace that did a lot of the original work on dealing with these errors through probability. [Stephen Stigler's book on the measurement of uncertainty before 1900](http://www.hup.harvard.edu/catalog.php?isbn=9780674403413) has a nice chapter on this.

\code{pods.notebook.display_google_book(id='ORUOAAAAQAAJ', page='217')}

where the crediting to the Laplace is about halfway through the last paragraph. This book was published in 1809, four years after [Legendre presented least squares](./week3.ipynb) in an appendix to one of his chapters on the orbit of comets. Gauss goes on to make a claim for priority on the method on page 221 (towards the end of the first paragraph ...).

\code{pods.notebook.display_google_book(id='ORUOAAAAQAAJ', page='221')}

### A Philosophical Dispute: Probabilistic Treatment of Parameters?

The follow up question is whether we can do the same thing with the parameters. If we have two parameters and only one unknown can we place a probability distribution over the parameters, as we did with the slack variables? The answer is yes, and from a philosophical perspective placing a probability distribution over the *parameters* is known as the *Bayesian* approach. This is because Thomas Bayes, in a [1763 essay](http://en.wikipedia.org/wiki/An_Essay_towards_solving_a_Problem_in_the_Doctrine_of_Chances) published at the Royal Society introduced the [Bernoulli distribution](http://en.wikipedia.org/wiki/Bernoulli_distribution) with a probabilistic interpretation for the *parameters*. Later statisticians such as [Ronald Fisher](http://en.wikipedia.org/wiki/Ronald_Fisher) objected to the use of probability distributions for *parameters*, and so in an effort to discredit the approach the referred to it as Bayesian. However, the earliest practioners of modelling, such as Laplace applied the approach as the most natural thing to do for dealing with unknowns (whether they were parameters or variables). Unfortunately, this dispute led to a split in the modelling community that still has echoes today. It is known as the Bayesian vs Frequentist controversy. From my own perspective, I think that it is a false dichotomy, and that the two approaches are actually complementary. My own focus research focus is on *modelling* and in that context, the use of probability is vital. For frequenstist statisticians, such as Fisher, the emphasis was on the value of the evidence in the data for a particular hypothesis. This is known as hypothesis testing. The two approaches can be unified because one of the most important approaches to hypothesis testing is to [compute the ratio of the likelihoods](http://en.wikipedia.org/wiki/Likelihood-ratio_test), and the result of applying a probability distribution to the parameters is merely to arrive at a different form of the likelihood.

### The Bayesian Approach

The aim of this notebook is to study Bayesian approaches to regression. In the Bayesian approach we define a *prior* densityover our parameters, $m$ and $c$ or more generally $\mappingVector$. This prior distribution gives us a range of expected values for our parameter *before* we have seen the data. The object in Bayesian inference is to then compute the*posterior* density which is the effect on the density of having observed the data. In standard probability notation we write the prior distribution as, 
$$p(\mappingVector),$$
so it is the *marginal* distribution for the parameters, i.e. the distribution we have for the parameters without any knowledge about the data. The posterior distribution is written as, 
$$p(\mappingVector|\dataVector, \inputMatrix).$$
So the posterior distribution is the *conditional* distribution for the parameters given the data (which in this case consists of pairs of observations including response variables (or targets), $\dataScalar_i$, and covariates (or inputs) $\inputVector_i$. Where here we are allowing the inputs to be multivariate. 

The posterior is recovered from the prior using *Bayes' rule*. Which is simply a rewriting of the product rule. We can recover Bayes' rule as follows. The product rule of probability tells us that the joint distribution is given as the product of the conditional and the marginal. Dropping the inputs from our conditioning for the moment we have,
$$
p(\mappingVector, \dataVector)=p(\dataVector|\mappingVector)p(\mappingVector),
$$
where we see we have related the joint density to the prior density and the *likelihood* from our previous investigation of regression,
$$
p(\dataVector|\mappingVector) = \prod_{i=1}^\numData\gaussianDist{\dataScalar_i}{\mappingVector^\top \inputVector_i}{ \dataStd^2}
$$
which arises from the assumption that our observation is given by
$$
\dataScalar_i = \mappingVector^\top \inputVector_i + \noiseScalar_i.
$$
In other words this is the Gaussian likelihood we have been fitting by minimizing the sum of squares. Have a look at [the session on multivariate regression](./week3.ipynb) as a reminder.

We've introduce the likelihood, but we don't have  relationship with the posterior, however, the product rule can also be written in the following way 
$$
p(\mappingVector, \dataVector) = p(\mappingVector|\dataVector)p(\dataVector),
$$
where here we have simply used the opposite conditioning. We've already introduced the *posterior* density above. This is the density that represents our belief about the parameters *after* observing the data. This is combined with the *marginal likelihood*, sometimes also known as the evidence. It is the marginal likelihood, because it is the original likelihood of the data with the parameters marginalised, $p(\dataVector)$. Here it's conditioned on nothing, but in practice you should always remember that everything here is conditioned on things like model choice: which set of basis functions. Because it's a regression problem, its also conditioned on the inputs. Using the equalitybetween the two different forms of the joint density  we recover
$$
p(\mappingVector|\dataVector) = \frac{p(\dataVector|\mappingVector)p(\mappingVector)}{p(\dataVector)}
$$
where we divided both sides by $p(\dataVector)$ to recover this result. Let's re-introduce the conditioning on the input locations (or covariates), $\inputMatrix$ to write the full form of Bayes' rule for the regression problem. 
$$
p(\mappingVector|\dataVector, \inputMatrix) = \frac{p(\dataVector|\mappingVector, \inputMatrix)p(\mappingVector)}{p(\dataVector|\inputMatrix)}
$$
where the posterior density for the parameters given the data is $p(\mappingVector|\dataVector, \inputMatrix)$, the marginal likelihood is $p(\dataVector|\inputMatrix)$, the prior density is $p(\mappingVector)$ and our original regression likelihood is given by $p(\dataVector|\mappingVector, \inputMatrix)$. It turns out that to compute the posterior the only things we need to do are define the prior and the likelihood. The other term on the right hand side can be computed by *the sum rule*. It is one of the key equations of Bayesian inference, the expectation of the likelihood under the prior, this process is known as marginalisation,
$$
p(\dataVector|\inputMatrix) = \int p(\dataVector|\mappingVector,\inputMatrix)p(\mappingVector)
\text{d}\mappingVector
$$
I like the term marginalisation, and the description of the probability as the *marginal likelihood*, because (for me) it somewhat has the implication that the variable name has been removed, and (perhaps) written in the margin. Marginalisation of a variable goes from a likelihood where the variable is in place, to a new likelihood where all possible values of that variable (under the prior) have been considered and weighted in the integral. This implies that all we need for specifying our model is to define the likelihood and the prior. We already have our likelihood from our earlier discussion, so our focus now turns to the prior density.

### The Bayesian Controversy: Philosophical Underpinnings

A segment from the lecture in 2012 on philsophical underpinnings.

\code{from datetime import timedelta
start=int(timedelta(hours=0, minutes=20, seconds=15).total_seconds())
from IPython.display import YouTubeVideo
YouTubeVideo('AvlnFnvFw_0',start=start)}

### The Prior Density

Let's assume that the prior density is given by a zero mean Gaussian, which is independent across each of the parameters, 
$$\mappingVector \sim \gaussianSamp{\zerosVector}{\alpha \eye}$$ 
In other words, we are assuming, for the prior, that each element of the parameters vector, $\mappingScalar_i$, was drawn from a Gaussian density as follows
$$\mappingScalar_i \sim \gaussianSamp{0}{\alpha}$$
Let's start by assigning the parameter of the prior distribution, which is the variance of the prior distribution, $\alpha$.

\code{# set prior variance on w
alpha = 4.
# set the order of the polynomial basis set
order = 5
# set the noise variance
sigma2 = 0.01}

### Generating from the Model

A very important aspect of probabilistic modelling is to *sample* from your model to see what type of assumptions you are making about your data. In this case that involves a two stage process.

1. Sample a candiate parameter vector from the prior.
2. Place the candidate parameter vector in the likelihood and sample functions conditiond on that candidate vector.
3. Repeat to try and characterise the type of functions you are generating.

Given a prior variance (as defined above) we can now  sample from the prior distribution and combine with a basis set to see what assumptions we are making about the functions *a priori* (i.e. before we've seen the data). Firstly we compute the basis function matrix. We will do it both for our training data, and for a range of prediction locations (`x_pred`).

\code{import numpy as np
data = pods.datasets.olympic_marathon_men()
x = data['X']
y = data['Y']
num_data = x.shape[0]
num_pred_data = 100 # how many points to use for plotting predictions
x_pred = np.linspace(1890, 2016, num_pred_data)[:, None] # input locations for predictions}

now let's build the basis matrices. We define the polynomial basis as follows.

\code{def polynomial(x, degree, loc, scale):
    degrees = np.arange(degree+1)
    return ((x-loc)/scale)**degrees}

\code{loc = 1950.
scale = 1.
degree = 5. 
Phi_pred = polynomial(x_pred, degree=degree, loc=loc, scale=scale)
Phi = polynomial(x, degree=degree, loc=loc, scale=scale)
}

### Sampling from the Prior

Now we will sample from the prior to produce a vector $\mappingVector$ and use it to plot a function which is representative of our belief *before* we fit the data. To do this we are going to use the properties of the Gaussian density and a sample from a *standard normal* using the function `np.random.normal`.

### Scaling Gaussian-distributed Variables

First, let's consider the case where we have one data point and one feature in our basis set. In otherwords $\mappingFunctionVector$ would be a scalar, $\mappingVector$ would be a scalar and $\basisMatrix$ would be a scalar. In this case we have 
$$\mappingFunctionScalar = \basisScalar \mappingScalar$$
If $\mappingScalar$ is drawn from a normal density, 
$$\mappingScalar \sim \gaussianSamp{\meanScalar_\mappingScalar}{c_\mappingScalar}$$
and $\basisScalar$ is a scalar value which we are given, then properties of the Gaussian density tell us that 
$$\basisScalar \mappingScalar \sim \gaussianSamp{\basisScalar\meanScalar_\mappingScalar}{\basisScalar^2c_\mappingScalar}$$
Let's test this out numerically. First we will draw 200 samples from a standard normal,

\code{w_vec = np.random.normal(size=200)}

We can compute the mean of these samples and their variance

\code{print('w sample mean is ', w_vec.mean())
print('w sample variance is ', w_vec.var())}

These are close to zero (the mean) and one (the variance) as you'd expect. Now compute the mean and variance of the scaled version,

\code{phi = 7
f_vec = phi*w_vec
print('True mean should be phi*0 = 0.')
print('True variance should be phi*phi*1 = ', phi*phi)
print('f sample mean is ', f_vec.mean())
print('f sample variance is ', f_vec.var())}

If you increase the number of samples then you will see that the sample mean and the sample variance begin to converge towards the true mean and the true variance. Obviously adding an offset to a sample from `np.random.normal` will change the mean. So if you want to sample from a Gaussian with mean `mu` and standard deviation `sigma` one way of doing it is to sample from the standard normal and scale and shift the result, so to sample a set of $\mappingScalar$ from a Gaussian with mean $\meanScalar$ and variance $\alpha$,
$$\mappingScalar \sim \gaussianSamp{\meanScalar}{\alpha}$$
We can simply scale and offset samples from the *standard normal*.

\code{mu = 4 # mean of the distribution
alpha = 2 # variance of the distribution
w_vec = np.random.normal(size=200)*np.sqrt(alpha) + mu
print('w sample mean is ', w_vec.mean())
print('w sample variance is ', w_vec.var())}

Here the `np.sqrt` is necesssary because we need to multiply by the standard deviation and we specified the variance as `alpha`. So scaling and offsetting a Gaussian distributed variable keeps the variable Gaussian, but it effects the mean and variance of the resulting variable. 

To get an idea of the overall shape of the resulting distribution, let's do the same thing with a histogram of the results.

\setupcode{# First the standard normal
import matplotlib.pyplot as plt
%matplotlib inline}

\plotcode{z_vec = np.random.normal(size=1000) # by convention, in statistics, z is often used to denote samples from the standard normal
w_vec = z_vec*np.sqrt(alpha) + mu
# plot normalized histogram of w, and then normalized histogram of z on top
plt.hist(w_vec, bins=30, normed=True)
plt.hist(z_vec, bins=30, normed=True)
plt.legend(('$w$', '$z$'))}

Now re-run this histogram with 100,000 samples and check that the both histograms look qualitatively Gaussian.

### Sampling from the Prior

Let's use this way of constructing samples from a Gaussian to check what functions look like *a priori*. The process will be as follows. First, we sample a random vector $K$ dimensional from `np.random.normal`. Then we scale it by $\sqrt{\alpha}$ to obtain a prior sample of $\mappingVector$.

\code{K = degree + 1
z_vec = np.random.normal(size=K)
w_sample = z_vec*np.sqrt(alpha)
print(w_sample)}

Now we can combine our sample from the prior with the basis functions to create a function,

\plotcode{f_sample = np.dot(Phi_pred,w_sample)
plt.plot(x_pred.flatten(), f_sample.flatten(), 'r-')}

This shows the recurring problem with the polynomial basis. Our prior allows relatively large coefficients for the basis associated with high polynomial degrees. Because we are operating with input values of around 2000, this leads to output functions of very high values. The fix we have used for this before is to rescale our data before we apply the polynomial basis to it. Above, we set the scale of the basis to 1. Here let's set it to 100 and try again.

\code{scale = 100.
Phi_pred = polynomial(x_pred, degree=degree, loc=loc, scale=scale)
Phi = polynomial(x, degree=degree, loc=loc, scale=scale)
}

Now we need to recompute the basis functions from above,

\plotcode{f_sample = np.dot(Phi_pred, w_sample)
plt.plot(x_pred.flatten(), f_sample.flatten(), 'r-')}

Now let's loop through some samples and plot various functions as samples from this system,

\plotcode{num_samples = 10
K = degree+1
for i in range(num_samples):
    z_vec = np.random.normal(size=K)
    w_sample = z_vec*np.sqrt(alpha)
    f_sample = np.dot(Phi_pred,w_sample)
    plt.plot(x_pred.flatten(), f_sample.flatten())
}

The predictions for the mean output can now be computed. We want the expected value of the predictions under the posterior distribution. In matrix form, the predictions can be computed as
$$\mappingFunctionVector = \basisMatrix \mappingVector.$$ 
This involves a matrix multiplication between a fixed matrix $\basisMatrix$ and a vector that is drawn from a distribution $\mappingVector$. Because $\mappingVector$ is drawn from a distribution, this imples that $\mappingFunctionVector$ should also be drawn from a distribution. There are two distributions we are interested in though. We have just been sampling from the *prior* distribution to see what sort of functions we get *before* looking at the data. In Bayesian inference, we need to computer the *posterior* distribution and sample from that density.

### Computing the Posterior

We will now attampt to compute the *posterior distribution*. In the lecture we went through the maths that allows us to compute the posterior distribution for $\mappingVector$. This distribution is also Gaussian,
$$p(\mappingVector | \dataVector, \inputVector, \dataStd^2) = \gaussianDist{\mappingVector}{\meanVector_\mappingScalar}{\covarianceMatrix_\mappingScalar}$$
with covariance, $\covarianceMatrix_\mappingScalar$, given by
$$\covarianceMatrix_\mappingScalar
= \left(\dataStd^{-2}\basisMatrix^\top \basisMatrix + \alpha^{-1}
\eye\right)^{-1}$$ 
whilst the mean is given by
$$\meanVector_\mappingScalar = \covarianceMatrix_\mappingScalar \dataStd^{-2}\basisMatrix^\top \dataVector$$ 
Let's compute the posterior covariance and mean, then we'll sample from these densities to have a look at the posterior belief about $\mappingVector$ once the data has been accounted for. Remember, the process of Bayesian inference involves combining the prior, $p(\mappingVector)$ with the likelihood, $p(\dataVector|\inputVector, \mappingVector)$ to form the posterior, $p(\mappingVector | \dataVector, \inputVector)$ through Bayes' rule,
$$p(\mappingVector|\dataVector, \inputVector) = \frac{p(\dataVector|\inputVector, \mappingVector)p(\mappingVector)}{p(\dataVector)}$$
We've looked at the samples for our function $\mappingFunctionVector = \basisMatrix\mappingVector$, which forms the mean of the Gaussian likelihood, under the prior distribution. I.e. we've sampled from $p(\mappingVector)$ and multiplied the result by the basis matrix. Now we will sample from the posterior density, $p(\mappingVector|\dataVector, \inputVector)$, and check that the new samples fit do correspond to the data, i.e. we want to check that the updated distribution includes information from the data set. First we need to compute the posterior mean and *covariance*.

### Bayesian Inference in the Univariate Case

This video talks about Bayesian inference across the single parameter, the offset $c$, illustrating how the prior and the likelihood combine in one dimension to form a posterior.

\code{from datetime import timedelta
start=int(timedelta(hours=0, minutes=0, seconds=15).total_seconds())
YouTubeVideo('AvlnFnvFw_0',start=start)
}

### Multivariate Bayesian Inference

This section of the lecture talks about how we extend the idea of Bayesian inference for the multivariate case. It goes through the multivariate Gaussian and how to complete the square in the linear algebra as we managed below.

\code{start=int(timedelta(hours=0, minutes=22, seconds=42).total_seconds())
YouTubeVideo('Os1iqgpelPw', start=start)}

The lecture informs us the the posterior density for $\mappingVector$ is given by a Gaussian density with covariance
$$
\covarianceMatrix_w =
\left(\dataStd^{-2}\basisMatrix^\top \basisMatrix + \alpha^{-1}
\eye\right)^{-1}
$$
and mean 
$$
\meanVector_w =
\covarianceMatrix_w\dataStd^{-2}\basisMatrix^\top \dataVector.
$$

\codeassignment{Compute the covariance for $\mappingVector$ given the training data, call the resulting variable `w_cov`. Compute the mean for $\mappingVector$ given the training data. Call the resulting variable `w_mean`. Assume that $\dataStd^2 = 0.01$}{1}{10}

\code{# Question 1 Answer Code
# Write code for you answer to this question in this box
# Do not delete these comments, otherwise you will get zero for this answer.
# Make sure your code has run and the answer is correct *before* submitting your notebook for marking.
sigma2 = 
w_cov = 
w_mean = }

### Sampling from the Posterior

Before we were able to sample the prior values for the mean *independently* from a Gaussian using `np.random.normal` and scaling the result. However, observing the data *correlates* the parameters. Recall this from the first lab where we had a correlation between the offset, $c$ and the slope $m$ which caused such problems with the coordinate ascent algorithm. We need to sample from a *correlated* Gaussian. For this we can use `np.random.multivariate_normal`.

\code{w_sample = np.random.multivariate_normal(w_mean.flatten(), w_cov)
f_sample = np.dot(Phi_pred,w_sample)
plt.plot(x_pred.flatten(), f_sample.flatten(), 'r-')
plt.plot(x, y, 'rx') # plot data to show fit.}

Now let's sample several functions and plot them all to see how the predictions fluctuate.

\code{for i in range(num_samples):
    w_sample = np.random.multivariate_normal(w_mean.flatten(), w_cov)
    f_sample = np.dot(Phi_pred,w_sample)
    plt.plot(x_pred.flatten(), f_sample.flatten())
plt.plot(x, y, 'rx') # plot data to show fit.}

This gives us an idea of what our predictions are. These are the predictions that are consistent with data and our prior. Try plotting different numbers of predictions. You can also try plotting beyond the range of where the data is and see what the functions do there. 

Rather than sampling from the posterior each time to compute our predictions, it might be better if we just summarised the predictions by the expected value of the output funciton, $f(x)$, for any particular input. If we can get formulae for this we don't need to sample the values of $f(x)$ we might be able to compute the distribution directly. Fortunately, in the Gaussian case, we can use properties of multivariate Gaussians to compute both the mean and the variance of these samples.

### Properties of Gaussian Variables

Gaussian variables have very particular properties, that many other densities don't exhibit. Perhaps foremost amoungst them is that the sum of any Gaussian distributed set of random variables also turns out to be Gaussian distributed. This property is much rarer than you might expect.

### Sum of Gaussian-distributed Variables

The sum of Gaussian random variables is also Gaussian, so if we have a random variable $\dataScalar_i$ drawn from a Gaussian density with mean $\meanScalar_i$ and variance $\dataStd^2_i$, 
$$\dataScalar_i \sim \gaussianSamp{\meanScalar_i}{\dataStd^2_i}$$
Then the sum of $K$ independently sampled values of $\dataScalar_i$ will be drawn from a Gaussian with mean $\sum_{i=1}^K \mu_i$ and variance $\sum_{i=1}^K \dataStd_i^2$,


$$\sum_{i=1}^K \dataScalar_i \sim \gaussianSamp{\sum_{i=1}^K \meanScalar_i}{\sum_{i=1}^K \dataStd_i^2}.$$
Let's try that experimentally. First let's generate a vector of samples from a standard normal distribution, $z \sim \gaussianSamp{0}{1}$,  then we will scale and offset them, then keep adding them into a vector `y_vec`.

#### Sampling from Gaussians and Summing Up

\code{K = 10 # how many Gaussians to add.
num_samples = 1000 # how many samples to have in y_vec
mus = np.linspace(0, 5, K) # mean values generated linearly spaced between 0 and 5
sigmas = np.linspace(0.5, 2, K) # sigmas generated linearly spaced between 0.5 and 2
y_vec = np.zeros(num_samples)
for mu, sigma in zip(mus, sigmas):
    z_vec = np.random.normal(size=num_samples) # z is from standard normal
    y_vec += z_vec*sigma + mu # add to y z*sigma + mu

# now y_vec is the sum of each scaled and off set z.
print('Sample mean is ', y_vec.mean(), ' and sample variance is ', y_vec.var())
print('True mean should be ', mus.sum())
print('True variance should be ', (sigmas**2).sum(), ' standard deviation ', np.sqrt((sigmas**2).sum())) }

Of course, we can histogram `y_vec` as well.

\code{plt.hist(y_vec, bins=30, normed=True)
plt.legend('$y$')}

### Matrix Multiplication of Gaussian Variables

We are interested in what our model is saying about the sort of functions we are observing. The fact that summing of Gaussian variables leads to new Gaussian variables, and scaling of Gaussian variables *also* leads to Gaussian variables means that matrix multiplication (which is just a series of sums and scales) also leads to Gaussian densities. Matrix multiplication is just adding and scaling together, in the formula, $\mappingFunctionVector = \basisMatrix \mappingVector$ we can extract the first element from $\mappingFunctionVector$ as
$$\mappingFunctionScalar_i = \basisVector_i^\top \mappingVector$$
where $\basisVector$ is a column vector from the $i$th row of $\basisMatrix$ and $\mappingFunctionScalar_i$ is the $i$th element of $\mappingFunctionVector$.This vector inner product itself merely implies that 
$$\mappingFunctionScalar_i = \sum_{j=1}^K \mappingScalar_j \basisScalar_{i, j}$$
and if we now say that $\mappingScalar_i$ is Gaussian distributed, then because a scaled Gaussian is also Gaussian, and because a sum of Gaussians is also Gaussian, we know that $\mappingFunctionScalar_i$ is also Gaussian distributed. It merely remains to work out its mean and covariance. We can do this by looking at the expectation under a Gaussian distribution. The expectation of the mean vector is given by 
$$\expDist{\mappingFunctionVector}{\gaussianDist{\mappingVector}{\meanVector}{\covarianceMatrix}} = \int \mappingFunctionVector
\gaussianDist{\mappingVector}{\meanVector}{\covarianceMatrix}
\text{d}\mappingVector = \int \basisMatrix\mappingVector
\gaussianDist{\mappingVector}{\meanVector}{\covarianceMatrix}
\text{d}\mappingVector = \basisMatrix \int \mappingVector
\gaussianDist{\mappingVector}{\meanVector}{\covarianceMatrix}
\text{d}\mappingVector = \basisMatrix \meanVector$$

Which is straightforward. The expectation of $\mappingFunctionVector=\basisMatrix\mappingVector$ under the Gaussian distribution for $\mappingFunctionVector$ is simply $\mappingFunctionVector=\basisMatrix\meanVector$, where $\meanVector$ is the *mean* of the Gaussian density for $\mappingVector$. Because our prior distribution was Gaussian with zero mean, the expectation under the prior is given by 
$$\expDist{\mappingFunctionVector}{\gaussianDist{\mappingVector}{\zerosVector}{\alpha\eye}} = \zerosVector$$

The covariance is a little more complicated. A covariance matrix is defined as
$$\text{cov}\left(\mappingFunctionVector\right)_{\gaussianDist{\mappingVector}{\meanVector}{\covarianceMatrix}}
= \expDist{\mappingFunctionVector\mappingFunctionVector^\top}{\gaussianDist{\mappingVector}{\meanVector}{\covarianceMatrix}}
- \expDist{\mappingFunctionVector}{\gaussianDist{\mappingVector}{\meanVector}{\covarianceMatrix}}\expDist{\mappingFunctionVector}{\gaussianDist{\mappingVector}{\meanVector}{\covarianceMatrix}}^\top$$
we've already computed
$\expDist{\mappingFunctionVector}{\gaussianDist{\mappingVector}{\meanVector}{\covarianceMatrix}}=\basisMatrix
\meanVector$ so we can substitute that in to recover
$$
\text{cov}\left(\mappingFunctionVector\right)_{\gaussianDist{\mappingVector}{\meanVector}{\covarianceMatrix}} = \expDist{\mappingFunctionVector\mappingFunctionVector^\top}{\gaussianDist{\mappingVector}{\meanVector}{\covarianceMatrix}} - \basisMatrix \meanVector \meanVector^\top \basisMatrix^\top
$$

So we need the expectation of $\mappingFunctionVector\mappingFunctionVector^\top$. Substituting in $\mappingFunctionVector = \basisMatrix \mappingVector$ we have
$$
\text{cov}\left(\mappingFunctionVector\right)_{\gaussianDist{\mappingVector}{\meanVector}{\covarianceMatrix}} = \expDist{\basisMatrix\mappingVector\mappingVector^\top \basisMatrix^\top}{\gaussianDist{\mappingVector}{\meanVector}{\covarianceMatrix}} - \basisMatrix \meanVector \meanVector^\top \basisMatrix^\top
$$
$$
\text{cov}\left(\mappingFunctionVector\right)_{\gaussianDist{\mappingVector}{\meanVector}{\covarianceMatrix}} = \basisMatrix\expDist{\mappingVector\mappingVector^\top}{\gaussianDist{\mappingVector}{\meanVector}{\covarianceMatrix}} \basisMatrix^\top - \basisMatrix \meanVector \meanVector^\top\basisMatrix^\top
$$
Which is dependent on the second moment of the Gaussian,
$$
\expDist{\mappingVector\mappingVector^\top}{\gaussianDist{\mappingVector}{\meanVector}{\covarianceMatrix}} = \covarianceMatrix + \meanVector\meanVector^\top
$$
that can be substituted in to recover, 
$$
\text{cov}\left(\mappingFunctionVector\right)_{\gaussianDist{\mappingVector}{\meanVector}{\covarianceMatrix}} = \basisMatrix\covarianceMatrix \basisMatrix^\top
$$
so in the case of the prior distribution, where we have $\covarianceMatrix = \alpha \eye$ we can write 
$$
\text{cov}\left(\mappingFunctionVector\right)_{\gaussianDist{\mappingVector}{\zerosVector}{\alpha \eye}} = \alpha \basisMatrix \basisMatrix^\top
$$

This implies that the prior we have suggested for $\mappingVector$, which is Gaussian with a mean of zero and covariance of $\alpha \eye$ suggests that the distribution for $\mappingVector$ is also Gaussian with a mean of zero and covariance of $\alpha \basisMatrix\basisMatrix^\top$. Since our observed output, $\dataVector$, is given by a noise corrupted variation of $\mappingFunctionVector$, the final distribution for $\dataVector$ is given as 
$$
\dataVector = \mappingFunctionVector + \noiseVector
$$
where the noise, $\noiseVector$, is sampled from a Gaussian density: $\noiseVector \sim \gaussianSamp{\zerosVector}{\dataStd^2\eye}$. So, in other words, we are taking a Gaussian distributed random value $\mappingFunctionVector$, 
$$
\mappingFunctionVector \sim \gaussianSamp{\zerosVector}{\alpha\basisMatrix\basisMatrix^\top}
$$
and adding to it another Gaussian distributed value, $\noiseVector \sim \gaussianSamp{\zerosVector}{\dataStd^2\eye}$, to form our data observations, $\dataVector$. Once again the sum of two (multivariate) Gaussian distributed variables is also Gaussian, with a mean given by the sum of the means (both zero in this case) and the covariance given by the sum of the covariances. So we now have that the marginal likelihood for the data, $p(\dataVector)$ is given by
$$
p(\dataVector) = \gaussianDist{\dataVector}{\zerosVector}{\alpha \basisMatrix \basisMatrix^\top + \dataStd^2\eye}
$$
This is our *implicit* assumption for $\dataVector$ given our prior assumption for $\mappingVector$.

### Computing the Mean and Error Bars of the Functions

These ideas together, now allow us to compute the mean and error bars of the predictions. The mean prediction, before corrupting by noise is given by,
$$
\mappingFunctionVector = \basisMatrix\mappingVector
$$
in matrix form. This gives you enough information to compute the predictive mean.

\codeassignment{Compute the predictive mean for the function at all
the values of the basis function given by `Phi_pred`. Call the vector of
predictions `\mappingFunction_pred_mean`. Plot the predictions alongside the data. We can also
compute what the training error was. Use the output from your model to compute
the predictive mean, and then compute the sum of squares error of that
predictive mean.
$$
E = \sum_{i=1}^n (\dataScalar_i - \langle \mappingFunction_i\rangle)^2
$$
where
$\langle \mappingFunction_i\rangle$ is the expected output of the model at point $\inputScalar_i$.}{2}{15}

\code{# Question 2 Answer Code
# Write code for you answer to this question in this box
# Do not delete these comments, otherwise you will get zero for this answer.
# Make sure your code has run and the answer is correct *before* submitting your notebook for marking.

# compute mean under posterior density
f_pred_mean = 

# plot the predictions

# compute mean at the training data and sum of squares error
f_mean = 
sum_squares = 
print('The error is: ', sum_squares)}

### Computing Error Bars

Finally, we can compute error bars for the predictions. The error bars are the standard deviations of the predictions for $\mappingFunctionVector=\basisMatrix\mappingVector$ under the posterior density for $\mappingVector$. The standard deviations of these predictions can be found from the variance of the prediction at each point. Those variances are the diagonal entries of the covariance matrix. We've already computed the form of the covariance under Gaussian expectations, 
$$
\text{cov}\left(\mappingFunctionVector\right)_{\gaussianDist{\mappingVector}{\meanVector}{\covarianceMatrix}} = \basisMatrix\covarianceMatrix \basisMatrix^\top
$$
which under the posterior density is given by
$$
\text{cov}\left(\mappingFunctionVector\right)_{\gaussianDist{\mappingVector}{\meanVector_w}{\covarianceMatrix_w}} = \basisMatrix\covarianceMatrix_w \basisMatrix^\top
$$

\codeassignment{The error bars are given by computing the standard
deviation of the predictions, $\mappingFunction$. For a given prediction $\mappingFunction_i$ the variance is
$\text{var}(\mappingFunction_i) = \langle \mappingFunction_i^2\rangle - \langle \mappingFunction_i \rangle^2$. This is given
by the diagonal element of the covariance of $\mappingFunctionVector$,
$$
\text{var}(\mappingFunction_i) =
\basisVector_{i, :}^\top \covarianceMatrix_w \basisVector_{i, :}
$$
where
$\basisVector_{i, :}$ is the basis vector associated with the input
location, $\inputVector_i$.

Plot the mean function and the error bars for your
basis.}{3}{20}

\code{# Question 3 Answer Code
# Write code for you answer to this question in this box
# Do not delete these comments, otherwise you will get zero for this answer.
# Make sure your code has run and the answer is correct *before* submitting your notebook for marking.

# Compute variance at function values
f_pred_var = 
f_pred_std = 

# plot the mean and error bars at 2 standard deviations above and below the mean
}

### Validation

Now we will test the generalisation ability of these models.  Firstly we are going to use hold out validation to attempt to see which model is best for extrapolating.

\codeassignment{Now split the data into training and *hold out* validation sets. Hold out the data for years after 1980. Compute the predictions for different model orders between 0 and 8. Find the model order which fits best according to *hold out* validation. Is it the same as the maximum likelihood result fom last week?}{4}{25}

\codeassignment{Now we will use leave one out cross validation to attempt to see which model is best at interpolating. Do you get the same result as for hold out validation? Compare plots of the hold out validation area for different degrees and the cross validation error for different degrees. Why are they so different? Select a suitable polynomial for characterising the differences in the predictions. Plot the mean function and the error bars for the full data set (to represent the leave one out solution) and the training data from the hold out experiment. Discuss your answer.}{5}{30}
