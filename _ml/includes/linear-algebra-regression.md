### Regression: Linear Releationship

$$\dataScalar_i = m \inputScalar_i + c$$

* $\dataScalar_i$ : winning
time/pace.

* $\inputScalar_i$ : year of Olympics.

* $m$ : rate of improvement over
time.

* $c$ : winning time at year 0.

### Overdetermined System

\setupcode{import teaching_plots as plot}
\plotcode{plot.over_determined_system(diagrams='../slides/diagrams/ml')}

\displaycode{pods.notebook.display_plots('over_determined_system{samp:0>3}.svg', directory='../slides/diagrams/ml', samp=(1, 7))}

### $y = mx + c$

point 1: $x = 1$, $y=3$ $$3 = m + c$$ 
point 2: $x = 3$, $y=1$
$$1 = 3m + c$$ 
point 3: $x = 2$, $y=2.5$ $$2.5 = 2m + c$$

\includeimg{../slides/diagrams/Pierre-Simon_Laplace.png}{50%}

### $y = mx + c + \epsilon$

point 1: $x = 1$, $y=3$ 
$$3 = m + c + \epsilon_1$$
point 2: $x = 3$, $y=1$ 
$$1 = 3m + c + \epsilon_2$$ 

point 3: $x = 2$, $y=2.5$
$$2.5 = 2m + c + \epsilon_3$$

### The Gaussian Density

* Perhaps the most common probability density.
\begin{align*}
p(y| \mu, \sigma^2) & =
\frac{1}{\sqrt{2\pi\sigma^2}}\exp\left(-\frac{(y - \mu)^2}{2\sigma^2}\right)\\
&
\buildrel\triangle\over = \mathcal{N}(y|\mu, \sigma^2)
\end{align*}

* The Gaussian density.

\code{plot.gaussian_of_height()}

### Gaussian Density

\includesvg{../slides/diagrams/gaussian_of_height.svg}

The Gaussian PDF with $\mu=1.7$ and variance $\sigma^2=0.0225$. Mean shown as red line. It could represent the heights of a population of students.

### Gaussian Density

$$
\mathcal{N}(y|\mu, \sigma^2) =
\frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(y-\mu)^2}{2\sigma^2}\right)
$$

$\sigma^2$ is the variance of the density and $\mu$ is the mean.


### Two Important Gaussian Properties

**Sum of Gaussian**

* Sum of Gaussian variables is also Gaussian.
    $$\dataScalar_i \sim \mathcal{N}(\mu, \sigma^2)$$ 
    And the sum is distributed as
    $$\sum_{i=1}^{\numData} \dataScalar_i \sim
\mathcal{N}\left(\sum_{i=1}^\numData \mu_i,\sum_{i=1}^\numData \sigma_i^2\right)$$
(*Aside*: As sum increases, sum of non-Gaussian, finite variance variables is
also Gaussian [central limit theorem](https://en.wikipedia.org/wiki/Central_limit_theorem).)

### Two Important Gaussian Properties

**Scaling a Gaussian**

* Scaling a Gaussian leads to a Gaussian.
    $$y \sim \mathcal{N}(\mu, \sigma^2)$$
    And the scaled density is distributed as
    $$w y \sim \mathcal{N}(w\mu,w^2 \sigma^2)$$

\section{Laplace's Idea}

### A Probabilistic Process

* Set the mean of Gaussian to be a function.
    $$p\left(\dataScalar_i|\inputScalar_i\right)=\frac{1}{\sqrt{2\pi\sigma^2}}\exp
\left(-\frac{\left(\dataScalar_i-f\left(\inputScalar_i\right)\right)^{2}}{2\sigma^2}\right).$$

* This gives us a ‘noisy function’.

* This is known as a stochastic process.

### Height as a Function of Weight

* In the standard Gaussian, parametized by
mean and variance.

* Make the mean a linear function of an *input*.

* This leads to a regression model. 
\begin{align*}
  \dataScalar_i=&f\left(\inputScalar_i\right)+\epsilon_i,\\
         \epsilon_i \sim &\mathcal{N}(0,
\sigma^2).
     \end{align*}
        
* Assume $\dataScalar_i$ is height and $\inputScalar_i$ is weight.

### Data Point Likelihood

* Likelihood of an individual data point
$$p\left(\dataScalar_i|\inputScalar_i,m,c\right)=\frac{1}{\sqrt{2\pi \sigma^2}}\exp
\left(-\frac{\left(\dataScalar_i-m\inputScalar_i-c\right)^{2}}{2\sigma^2}\right).$$

* Parameters are gradient, $m$, offset, $c$ of the function and noise variance $\sigma^2$.

### Data Set Likelihood

* If the noise, $\epsilon_i$ is sampled independently
for each
    data point.

* Each data point is independent (given $m$ and
$c$).

* For independent variables:
    $$p(\dataVector) = \prod_{i=1}^\numData
p(\dataScalar_i)$$
    $$p(\dataVector|\inputVector, m, c) = \prod_{i=1}^\numData p(\dataScalar_i|\inputScalar_i, m, c)$$

### For Gaussian 

* i.i.d. assumption   
  $$p(\dataVector|\inputVector, m, c)
= \prod_{i=1}^\numData \frac{1}{\sqrt{2\pi \sigma^2}}\exp \left(-\frac{\left(\dataScalar_i-
m\inputScalar_i-c\right)^{2}}{2\sigma^2}\right).$$
    $$p(\dataVector|\inputVector, m, c) =
\frac{1}{\left(2\pi \sigma^2\right)^{\frac{\numData}{2}}}\exp
\left(-\frac{\sum_{i=1}^\numData\left(\dataScalar_i-m\inputScalar_i-c\right)^{2}}{2\sigma^2}\right).$$

### Log Likelihood Function

* Normally work with the log likelihood:
$$L(m,c,\sigma^{2})=-\frac{\numData}{2}\log 2\pi -\frac{\numData}{2}\log \sigma^2 -\sum
_{i=1}^{\numData}\frac{\left(\dataScalar_i-m\inputScalar_i-c\right)^{2}}{2\sigma^2}.$$

### Consistency of Maximum Likelihood


* If data was really generated
according to probability we specified.

* Correct parameters will be recovered
in limit as
    $n \rightarrow \infty$.

* This can be proven through sample
based approximations (law of
    large numbers) of “KL divergences”.

* Mainstay of classical statistics.

### Probabilistic Interpretation of the Error Function

* Probabilistic Interpretation for Error Function is Negative Log Likelihood.

* *Minimizing* error function is equivalent to *maximizing* log likelihood.

* Maximizing *log likelihood* is equivalent to maximizing the *likelihood*
because $\log$ is monotonic.

* Probabilistic interpretation: Minimizing error function is equivalent to maximum likelihood with respect to parameters.

### Error Function

* Negative log likelihood is the error function leading to an error function 
  $$\errorFunction(m,c,\sigma^{2})=\frac{\numData}{2}\log \sigma^2+\frac{1}{2\sigma^2}\sum _{i=1}^{\numData}\left(\dataScalar_i-m\inputScalar_i-c\right)^{2}.$$

* Learning proceeds by minimizing this error function for the data set provided.

### Connection: Sum of Squares Error

* Ignoring terms which don’t depend on $m$ and $c$ gives
  $$\errorFunction(m, c) \propto \sum_{i=1}^\numData (\dataScalar_i - \mappingFunction(\inputScalar_i))^2$$
  where $\mappingFunction(\inputScalar_i) = m\inputScalar_i + c$.

* This is known as the *sum of squares* error function.

* Commonly used and is closely associated with the Gaussian likelihood.

### Reminder

* Two functions involved:
  * Prediction function: $\mappingFunction(\inputScalar_i)$
  * Error, or Objective function: $\errorFunction(m, c)$
* Error function depends on parameters through prediction function.

### Mathematical Interpretation

* What is the mathematical interpretation?
* There is a cost function.
  * It expresses mismatch between your
prediction and reality.
  $$\errorFunction(m, c)=\sum_{i=1}^\numData \left(\dataScalar_i - m\inputScalar_i
-c\right)^2$$

  * This is known as the sum of squares error.

### Learning is Optimization

* Learning is minimization of the cost function.
* At the minima the gradient is zero.
* Coordinate ascent, find gradient in each coordinate and set to zero.
  $$\frac{\text{d}\errorFunction(m)}{\text{d}m} = -2\sum_{i=1}^\numData \inputScalar_i\left(\dataScalar_i- m \inputScalar_i - c \right)$$
  $$0 = -2\sum_{i=1}^\numData \inputScalar_i \left(\dataScalar_i-m \inputScalar_i - c \right)$$

### Learning is Optimization

* Fixed point equations
  $$0 = -2\sum_{i=1}^\numData \inputScalar_i\dataScalar_i+2\sum_{i=1}^\numData m \inputScalar_i^2+2\sum_{i=1}^\numData c\inputScalar_i$$
    $$m  =    \frac{\sum_{i=1}^\numData \left(\dataScalar_i -c\right)\inputScalar_i}{\sum_{i=1}^\numData\inputScalar_i^2}$$

### Learning is Optimization

* Learning is minimization of the cost function.
* At the minima the gradient is zero.
* Coordinate ascent, find gradient in each coordinate and set to zero.
  $$\frac{\text{d}\errorFunction(c)}{\text{d}c} = -2\sum_{i=1}^\numData \left(\dataScalar_i- m \inputScalar_i - c \right)$$
  $$0 = -2\sum_{i=1}^\numData\left(\dataScalar_i-
            m \inputScalar_i - c \right)$$

### Learning is Optimization

* Fixed point equations
  $$0 = -2\sum_{i=1}^\numData \dataScalar_i +2\sum_{i=1}^\numData m \inputScalar_i +2n c$$
  $$c = \frac{\sum_{i=1}^\numData \left(\dataScalar_i - m\inputScalar_i\right)}{\numData}$$

### Fixed Point Updates

Worked example. 
$$\begin{aligned}
    c^{*}=&\frac{\sum
_{i=1}^{\numData}\left(\dataScalar_i-m^{*}\inputScalar_i\right)}{\numData},\\
    m^{*}=&\frac{\sum
_{i=1}^{\numData}\inputScalar_i\left(\dataScalar_i-c^{*}\right)}{\sum _{i=1}^{\numData}\inputScalar_i^{2}},\\
\left.\sigma^2\right.^{*}=&\frac{\sum
_{i=1}^{\numData}\left(\dataScalar_i-m^{*}\inputScalar_i-c^{*}\right)^{2}}{\numData}
\end{aligned}$$

### Important Concepts Not Covered

* Other optimization methods:
  * Second order methods, conjugate gradient, quasi-Newton and Newton.
* Effective heuristics such as momentum.
* Local vs global solutions.

### Reading

* Section 1.1-1.2 of @Rogers:book11 for fitting linear models. 
* Section 1.2.5 of @Bishop:book06 up to equation 1.65.

### Multi-dimensional Inputs

* Multivariate functions involve more than one input.
* Height might be a function of weight and gender.
* There could be other contributory factors.
* Place these factors in a feature vector $\inputVector_i$.
* Linear function is now defined as
  $$\mappingFunction(\inputVector_i) = \sum_{j=1}^p w_j \inputScalar_{i, j} + c$$

### Vector Notation

* Write in vector notation,
  $$\mappingFunction(\inputVector_i) = \mappingVector^\top \inputVector_i + c$$

* Can absorb $c$ into $\mappingVector$ by assuming extra input $\inputScalar_0$
  which is always 1.
  $$\mappingFunction(\inputVector_i) = \mappingVector^\top \inputVector_i$$

### Log Likelihood for Multivariate Regression

* The likelihood of a single data point is
  $$p\left(\dataScalar_i|\inputScalar_i\right)=\frac{1}{\sqrt{2\pi\sigma^2}}\exp
\left(-\frac{\left(\dataScalar_i-\mappingVector^{\top}\inputVector_i\right)^{2}}{2\sigma^2}\right).$$
* Leading to a log likelihood for the data set of
  $$L(\mappingVector,\sigma^2)= -\frac{\numData}{2}\log \sigma^2-\frac{\numData}{2}\log 2\pi -\frac{\sum_{i=1}^{\numData}\left(\dataScalar_i-\mappingVector^{\top}\inputVector_i\right)^{2}}{2\sigma^2}.$$

* And a corresponding error function of
  $$\errorFunction(\mappingVector,\sigma^2)=\frac{\numData}{2}\log\sigma^2 + \frac{\sum_{i=1}^{\numData}\left(\dataScalar_i-\mappingVector^{\top}\inputVector_i\right)^{2}}{2\sigma^2}.$$

### Expand the Brackets

\begin{align*}
  \errorFunction(\mappingVector,\sigma^2)  = &
\frac{\numData}{2}\log \sigma^2 + \frac{1}{2\sigma^2}\sum
_{i=1}^{\numData}\dataScalar_i^{2}-\frac{1}{\sigma^2}\sum
_{i=1}^{\numData}\dataScalar_i\mappingVector^{\top}\inputVector_i\\&+\frac{1}{2\sigma^2}\sum
_{i=1}^{\numData}\mappingVector^{\top}\inputVector_i\inputVector_i^{\top}\mappingVector
+\text{const}.\\
    = & \frac{\numData}{2}\log \sigma^2 + \frac{1}{2\sigma^2}\sum
_{i=1}^{\numData}\dataScalar_i^{2}-\frac{1}{\sigma^2}
\mappingVector^\top\sum_{i=1}^{\numData}\inputVector_i\dataScalar_i\\&+\frac{1}{2\sigma^2}
\mappingVector^{\top}\left[\sum
_{i=1}^{\numData}\inputVector_i\inputVector_i^{\top}\right]\mappingVector +\text{const}.
\end{align*}

### Multivariate Derivatives

* We will need some multivariate calculus.
* For now some simple multivariate differentiation:
$$\frac{\text{d}{\mathbf{a}^{\top}}{\mappingVector}}{\text{d}\mappingVector}=\mathbf{a}$$
and
$$\frac{\mappingVector^{\top}\mathbf{A}\mappingVector}{\text{d}\mappingVector}=\left(\mathbf{A}+\mathbf{A}^{\top}\right)\mappingVector$$
or if $\mathbf{A}$ is symmetric (*i.e.*
    $\mathbf{A}=\mathbf{A}^{\top}$)
$$\frac{\text{d}\mappingVector^{\top}\mathbf{A}\mappingVector}{\text{d}\mappingVector}=2\mathbf{A}\mappingVector.$$

### Differentiate

Differentiating with respect to the vector $\mappingVector$ we obtain
$$\frac{\partial L\left(\mappingVector,\sigma^2 \right)}{\partial
\mappingVector}=\frac{1}{\sigma^2} \sum _{i=1}^{\numData}\inputVector_i \dataScalar_i-\frac{1}{\sigma^2}
\left[\sum _{i=1}^{\numData}\inputVector_i\inputVector_i^{\top}\right]\mappingVector$$
Leading to
$$\mappingVector^{*}=\left[\sum
_{i=1}^{\numData}\inputVector_i\inputVector_i^{\top}\right]^{-1}\sum
_{i=1}^{\numData}\inputVector_i\dataScalar_i,$$
Rewrite in matrix notation:
$$\sum_{i=1}^{\numData}\inputVector_i\inputVector_i^\top = \inputMatrix^\top \inputMatrix$$
$$\sum_{i=1}^{\numData}\inputVector_i\dataScalar_i = \inputMatrix^\top \dataVector$$

### Update Equations

* Update for $\mappingVector^{*}$.
    $$\mappingVector^{*} = \left(\inputMatrix^\top \inputMatrix\right)^{-1} \inputMatrix^\top \dataVector$$
* The equation for $\left.\sigma^2\right.^{*}$ may also be found
$$\left.\sigma^2\right.^{{*}}=\frac{\sum_{i=1}^{\numData}\left(\dataScalar_i-\left.\mappingVector^{*}\right.^{\top}\inputVector_i\right)^{2}}{\numData}.$$

### Reading

* Section 1.3 of @Rogers:book11 for Matrix & Vector Review.
