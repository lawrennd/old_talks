---
abstract: |
    Bayesian formalisms deal with uncertainty in parameters, frequentist
    formalisms deal with the *risk* of a data set, uncertainty in the data
    sample. In this talk, we consider uncertainty in the *loss function*.
    Uncertainty in the loss function. We introduce uncertainty through
    linear weightings of terms in the loss function and show how a
    distribution over the loss can be maintained through the *maximum
    entropy principle*. This allows us minimize the expected loss under our
    maximumm entropy distribution of the loss function. We recover weighted
    least squares and a LOESS-like regression from the formalism.
affiliation: 'University of Sheffield and Amazon, Cambridge'
author: 'Neil D. Lawrence'
bibliography:
- '../other.bib'
- '../lawrence.bib'
- '../zbooks.bib'
csl: '../elsevier-harvard.csl'
header-includes: |
        <script type="text/x-mathjax-config">
        MathJax.Hub.Config({ TeX: { extensions: ["color.js"] }});
        </script>
        <script>

    function setDivs(group) {
      var frame = document.getElementById("range-".concat(group)).value
      slideIndex = parseInt(frame)
      showDivs(slideIndex, group);
    }

    function plusDivs(n, group) {
      showDivs(slideIndex += n, group);
    }

    function showDivs(n,group) {
      var i;
      var x = document.getElementsByClassName(group);
      if (n > x.length) {slideIndex = 1}    
      if (n < 1) {slideIndex = x.length}
      for (i = 0; i < x.length; i++) {
         x[i].style.display = "none";  
      }
      x[slideIndex-1].style.display = "block";  
    }
        </script>
title: Uncertainty in Loss Functions
transition: None
venue: IWCV 2018
---

    <script type="text/x-mathjax-config">
    MathJax.Hub.Config({ TeX: { extensions: ["color.js"] }});
    </script>
    <script>

function setDivs(group) {
  var frame = document.getElementById("range-".concat(group)).value
  slideIndex = parseInt(frame)
  showDivs(slideIndex, group);
}

function plusDivs(n, group) {
  showDivs(slideIndex += n, group);
}

function showDivs(n,group) {
  var i;
  var x = document.getElementsByClassName(group);
  if (n > x.length) {slideIndex = 1}    
  if (n < 1) {slideIndex = x.length}
  for (i = 0; i < x.length; i++) {
     x[i].style.display = "none";  
  }
  x[slideIndex-1].style.display = "block";  
}
    </script>

#### Uncertainty in Loss Functions

#### 2018-05-29

#### Neil D. Lawrence

#### Amazon Cambridge and **University of Sheffield**

`@lawrennd` [inverseprobability.com](http://inverseprobability.com)

What is Machine Learning?
-------------------------

What is machine learning? At its most basic level machine learning is a
combination of

$$ \text{data} + \text{model} \xrightarrow{\text{compute}} \text{prediction}$$

where *data* is our observations. They can be actively or passively
acquired (meta-data). The *model* contains our assumptions, based on
previous experience. THat experience can be other data, it can come from
transfer learning, or it can merely be our beliefs about the
regularities of the universe. In humans our models include our inductive
biases. The *prediction* is an action to be taken or a categorization or
a quality score. The reason that machine learning has become a mainstay
of artificial intelligence is the importance of predictions in
artificial intelligence. The data and the model are combined through
computation.

In practice we normally perform machine learning using two functions. To
combine data with a model we typically make use of:

**a prediction function** a function which is used to make the
predictions. It includes our beliefs about the regularities of the
universe, our assumptions about how the world works, e.g. smoothness,
spatial similarities, temporal similarities.

**an objective function** a function which defines the cost of
misprediction. Typically it includes knowledge about the world’s
generating processes (probabilistic objectives) or the costs we pay for
mispredictions (empiricial risk minimization).

The combination of data and model through the prediction function and
the objectie function leads to a *learning algorithm*. The class of
prediction functions and objective functions we can make use of is
restricted by the algorithms they lead to. If the prediction function or
the objective function are too complex, then it can be difficult to find
an appropriate learning algorithm. Much of the acdemic field of machine
learning is the quest for new learning algorithms that allow us to bring
different types of models and data together.

A useful reference for state of the art in machine learning is the UK
Royal Society Report, [Machine Learning: Power and Promise of Computers
that Learn by
Example](https://royalsociety.org/~/media/policy/projects/machine-learning/publications/machine-learning-report.pdf).

You can also check my blog post on [“What is Machine
Learning?”](http://inverseprobability.com/2017/07/17/what-is-machine-learning)

### Artificial vs Natural Systems

### Natural Systems are Evolved

> Survival of the fittest
>
> [Herbet Spencer](https://en.wikipedia.org/wiki/Herbert_Spencer), 1864

Darwin never said “Survival of the Fittest” he talked about evolution by
natural selection.

Evolution is better described as “non-survival of the non-fit”. You
don’t have to be the fittest to survive, you just need to avoid the
pitfalls of life. This is the first priority.

A mistake we make in our systems design is to equate fitness with the
objective function, and to assume it is known and static. In practice, a
real environment would have an evolving fitness function which would be
unknown at any given time.

Uncertainty in models is handled by Bayesian inference, here we consider
uncertainty arising in loss functions.

Consider a loss function which decomposes across individual
observations, ${y}_{k,j}$, each of which is dependent on some set of
features, ${{\bf {x}}}_k$.

$$
{E}({\mathbf{{y}}}, {{\bf X}}) = \sum_{k}\sum_{j}
L({y}_{k,j}, {{\bf {x}}}_k)
$$ Assume that the loss function depends on the features through some
mapping function, ${f}_j(\cdot)$ which we call the *prediction
function*.

$$
{E}({\mathbf{{y}}}, {{\bf X}}) = \sum_{k}\sum_{j} L({y}_{k,j},
{f}_j({{\bf {x}}}_k))
$$ without loss of generality, we can move the index to the inputs, so
we have ${{\bf {x}}}_i =\left[{{\bf {x}}}\quad j\right]$, and we set
${y}_i = {y}_{k, j}$. So we have

$$
{E}({\mathbf{{y}}}, {{\bf X}}) = \sum_{i} L({y}_i, {f}({{\bf {x}}}_i))
$$ Bayesian inference considers uncertainty in ${f}$, often through
parameterizing it, ${f}({{\bf {x}}}; {\boldsymbol{{\theta}}})$, and
considering a *prior* distribution for the parameters,
$p({\boldsymbol{{\theta}}})$, this in turn implies a distribution over
functions, $p({f})$. Process models, such as Gaussian processes specify
this distribution, known as a process, directly.

Bayesian inference proceeds by specifying a *likelihood* which relates
the data, ${y}$, to the parameters. Here we choose not to do this, but
instead we only consider the *loss* function for our objective. The loss
is the cost we pay for a misclassification.

The *risk function* is the expectation of the loss under the
distribution of the data. Here we are using the framework of *empirical
risk* minimization, because we have a sample based approximation. The
new expectation we are considering is around the loss function itself,
not the uncertainty in the data.

The loss function and the log likelihood may take a mathematically
similar form but they are philosophically very different. The log
likelihood assumes something about the *generating* function of the
data, whereas the loss function assumes something about the cost we pay.
Importantly the loss function in Bayesian inference only normally enters
at the point of decision.

The key idea in Bayesian inference is that the probabilistic inference
can be performed *without* knowing the loss becasue if the model is
correct, then the form of the loss function is irrelevant when
performing inference. In practice, however, the model is *never*
correct.

Some of the maths below looks similar to the maths we can find in
Bayesian methods, in particular variational Bayes, but that is merely a
consequence of the availability of analytical mathematics. There are
only particular ways of developing tractable algorithms, one route
involves linear algebra. However, the similarity of the mathematics
belies a difference in interpretation. It is similar to travelling a
road (e.g. Ermine Street) in a wild landscape. We travel together
because that is where efficient progress is to be made, but in practice
a our destinations (Lincoln, York), may be different.

### Introduce Uncertainty

To introduce uncertainty we consider a weighted version of the loss
function, we introduce positive weights,
$\left\{{s}_i\right\}_{i=1}^{n}$. $$
{E}({\mathbf{{y}}}, {{\bf X}}) = \sum_{i}
{s}_i L({y}_i, {f}({{\bf {x}}}_i))
$$ We now assume that tmake the assumption that these weights are drawn
from a distribution, $q({s})$. Instead of looking to minimize the loss
direction, we look at the expected loss under this distribution.

$$
\begin{align*}
{E}({\mathbf{{y}}}, {{\bf X}}) = & \sum_{i}{\left\langle {s}_i L({y}_i,
{f}({{\bf {x}}}_i)) \right\rangle _{q({s})}}\\
&
=\sum_{i}{\left\langle {s}_i  \right\rangle _{q({s})}}L({y}_i,
{f}({{\bf {x}}}_i))
\end{align*}
$$ We will assume that our process, $q({s})$ can depend on a variety of
inputs such as ${\mathbf{{y}}}$, ${{\bf X}}$ and time, $t$.

### Principle of Maximum Entropy

To maximize uncertainty in $q(w)$ we maximize its entropy. Following
Jaynes formalism of maximum entropy, in the continuous space we do this
with respect to an invariant measure, $$
H({s})= - \int q({s}) \log
\frac{q({s})}{m({s})} \text{d}{s}$$ and since we minimize the loss, we
balance this by adding in this term to form $$
\begin{align*}
{E}= & \beta\sum_{i}{\left\langle {s}_i
 \right\rangle _{q({s})}}L({y}_i, {f}({{\bf {x}}}_i)) -
H({s})\\
&= \beta\sum_{i}{\left\langle {s}_i
 \right\rangle _{q({s})}}L({y}_i, {f}({{\bf {x}}}_i)) +  \int
q({s}) \log \frac{q({s})}{m({s})}
\text{d}{s}\end{align*}
$$ where $\beta$ serves to weight the relative contribution of the
entropy term and the loss term.

We can now minimize this modified loss with respect to the density
$q({s})$, the freeform optimization over this term leads to $$
\begin{align*}
q({s}) \propto & \exp\left(- \beta \sum_{i=1}^{n}{s}_i L({y}_i, {f}({{\bf {x}}}_i)) \right)
m({s})\\
 \propto & \prod_{i=1}^{n}\exp\left(- \beta
{s}_i L({y}_i, {f}({{\bf {x}}}_i)) \right)
m({s})
\end{align*}
$$

### Example

Assume $$
m({s}) = \prod_i
\lambda\exp\left(-\lambda{s}_i\right)
$$ which is the distribution with the maximum entropy for a given mean,
${s}$. Then we have $$
q({s}) = \prod_i q({s}_i)
$$ $$
q({s}_i) \propto
\frac{1}{\lambda+\beta L_i} \exp\left(-(\lambda+\beta L_i) {s}_i\right)
$$ and we can compute $$
{\left\langle {s}_i \right\rangle _{q({s})}} =
\frac{1}{\lambda + \beta L_i}
$$

### Coordinate Ascent

We can optimize with respect to $q({s})$ recovering, $$
q({s}_i) = \frac{1}{\lambda+\beta L_i}
\exp\left(-(\lambda+\beta L_i) {s}_i\right)
$$ allowing us to compute the expectation of ${s}$, $$
{\left\langle {s}_i \right\rangle _{q({s}_i)}} = \frac{1}{\lambda+\beta
L_i}
$$ then, we can maximize our expected loss with respect to ${f}(\cdot)$
$$
\beta \sum_{i=1}^{n}{\left\langle {s}_i \right\rangle _{q({s}_i)}} L({y}_i,
{f}({{\bf {x}}}_i))
$$ If the loss is the *squared loss*, then this is recognised as a
*reweighted least squares algorithm*. However, the loss can be of any
form as long as $q({s})$ defined above exists.

In addition to the above, in our example below, we updated $\beta$ to
normalize the expected loss to be ${n}$ at each iteration, so we have $$
\beta = \frac{{n}}{\sum_{i=1}^{n}{\left\langle {s}_i \right\rangle _{q({s}_i)}} L({y}_i,
{f}({{\bf {x}}}_i))}
$$

``` {.python}
import pods
import matplotlib.pyplot as plt
```

### Olympic Marathon Data

The first thing we will do is load a standard data set for regression
modelling. The data consists of the pace of Olympic Gold Medal Marathon
winners for the Olympics from 1896 to present. First we load in the data
and plot.

``` {.python}
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

<table>
<tr>
<td width="70%">
-   Gold medal times for Olympic Marathon since 1896.

-   Marathons before 1924 didn’t have a standardised distance.

-   Present results using pace per km.

-   In 1904 Marathon was badly organised leading to very slow times.

</td>
<td width="30%">
![image](../slides/diagrams/Stephen_Kiprotich.jpg) <small>Image from
Wikimedia Commons <http://bit.ly/16kMKHQ></small>
</td>
</tr>
</table>
<object class="svgplot" align data="../slides/diagrams/ml/olympic_marathon.svg">
</object>
Things to notice about the data include the outlier in 1904, in this
year, the olympics was in St Louis, USA. Organizational problems and
challenges with dust kicked up by the cars following the race meant that
participants got lost, and only very few participants completed.

More recent years see more consistently quick marathons.

### Example: Linear Regression

``` {.python}
import mlai
import numpy as np
import scipy as sp
```

Create a weighted linear regression class, inheriting from the `mlai.LM`
class.

``` {.python}
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

``` {.python}
num_basis=2 
data_limits=[1890, 2020]
basis = mlai.basis(mlai.polynomial, num_basis, data_limits=data_limits)
model = LML(x, y, basis=basis, lambd=1, beta=1)
model2 = mlai.LM(x, y, basis=basis)
```

``` {.python}
model.fit()
model2.fit()
```

``` {.python}
import matplotlib.pyplot as plt
```

``` {.python}
x_test = np.linspace(data_limits[0], data_limits[1], 130)[:, None]
f_test, f_var = model.predict(x_test)
f2_test, f2_var = model2.predict(x_test)
```

``` {.python}
import teaching_plots as plot
from matplotlib import rc, rcParams
rcParams.update({'font.size': 22})
rc('text', usetex=True)
```

``` {.python}

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

``` {.python}
import pods
pods.notebook.display_plots('olympic-loss-linear-regression{number:0>3}.svg', 
                            directory='../slides/diagrams/ml', number=(0, 1))
```

### Parameter Uncertainty

Classical Bayesian inference is concerned with parameter uncertainty,
which equates to uncertainty in the *prediction function*,
${f}({{\bf {x}}})$. The prediction function is normally an estimate of
the value of ${y}$ or constructs a probability density for ${y}$.

Uncertainty in the prediction function can arise through uncertainty in
our loss function, but also through uncertainty in parameters in the
classical Bayesian sense. The full maximum entropy formalism would now
be $$
{\left\langle \beta {s}_i L({y}_i,
{f}({{\bf {x}}}_i)) \right\rangle _{q({s}, {f})}} + \int
q({s}, {f}) \log \frac{q({s},
{f})}{m({s})m({f})}\text{d}{s}\text{d}{f}$$

$$
q({f}, {s}) \propto
\prod_{i=1}^{n}\exp\left(- \beta {s}_i L({y}_i,
{f}({{\bf {x}}}_i)) \right) m({s})m({f})
$$

### Approximation

-   Generally intractable, so assume: $$
    q({f}, {s}) = q({f})q({s})
    $$

-   Entropy maximization proceeds as before but with $$
    q({s}) \propto
    \prod_{i=1}^{n}\exp\left(- \beta {s}_i {\left\langle L({y}_i,
    {f}({{\bf {x}}}_i)) \right\rangle _{q({f})}} \right) m({s})
    $$ and $$
    q({f}) \propto
    \prod_{i=1}^{n}\exp\left(- \beta {\left\langle {s}_i \right\rangle _{q({s})}} L({y}_i,
    {f}({{\bf {x}}}_i)) \right) m({f})
    $$

-   Can now proceed with iteration between $q({s})$, $q({f})$

``` {.python}
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

``` {.python}
model = BLML(x, y, basis=basis, alpha=1000, lambd=1, beta=1)
model2 = mlai.BLM(x, y, basis=basis, alpha=1000, sigma2=1)
```

``` {.python}
model.fit()
model2.fit()
```

``` {.python}
x_test = np.linspace(data_limits[0], data_limits[1], 130)[:, None]
f_test, f_var = model.predict(x_test)
f2_test, f2_var = model2.predict(x_test)
```

``` {.python}
import gp_tutorial
```

``` {.python}
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

``` {.python}
import pods
pods.notebook.display_plots('olympic-loss-bayes-linear-regression{number:0>3}.svg', 
                            directory='../slides/diagrams/ml', number=(0, 1))
```

### Correlated Scales

Going beyond independence between weights, we now consider $m({v})$ to
be a Gaussian process, and scale by the *square* of ${v}$, ${s}={v}^2$
$$
{v}\sim \mathcal{GP}\left({\mu}({{\bf {x}}}), {{k}}({{\bf {x}}}, {{\bf {x}}}^\prime)\right)
$$

$$
q({v}) \propto
\prod_{i=1}^{n}\exp\left(- \beta {v}_i^2 L({y}_i,
{f}({{\bf {x}}}_i)) \right)
\exp\left(-\frac{1}{2}({\mathbf{v}}-{\boldsymbol{{\mu}}})^\top {\mathbf{K}}^{-1}
({\mathbf{v}}-{\boldsymbol{{\mu}}})\right)
$$ where ${\mathbf{K}}$ is the covariance of the process made up of
elements taken from the covariance function,
${k}({{\bf {x}}}, t, {\mathbf{{y}}}; {{\bf {x}}}^\prime, t^\prime, {\mathbf{{y}}}^\prime)$
so $q({v})$ itself is Gaussian with covariance $$
{\mathbf{C}}= \left(\beta\mathbf{L} + {\mathbf{K}}^{-1}\right)^{-1}
$$ and mean $$
{\mathbf{{m}}}= \beta{\mathbf{C}}\mathbf{L}{\boldsymbol{{\mu}}}$$ where
$\mathbf{L}$ is a matrix containing the loss functions,
$L({y}_i, {f}({{\bf {x}}}_i))$ along its diagonal elements with zeros
elsewhere.

The update is given by $$
{\left\langle {v}_i^2 \right\rangle _{q({v})}} = {m}_i^2 +
{c}_{i, i}.
$$ To compare with before, if the mean of the measure $m({v})$ was zero
and the prior covariance was spherical,
${\mathbf{K}}=\lambda^{-1}{\mathbf{I}}$. Then this would equate to an
update, $$
{\left\langle {v}_i^2 \right\rangle _{q({v})}} = \frac{1}{\lambda + \beta L_i}
$$ which is the same as we had before for the exponential prior over
${s}$.

### Conditioning the Measure

Now that we have defined a process over ${v}$, we could define a region
in which we’re certain that we would like the weights to be high. For
example, if we were looking to have a test point at location
${{\bf {x}}}_\ast$, we could update our measure to be a Gaussian process
that is conditioned on the observation of ${v}_\ast$ set appropriately
at ${x}_\ast$. In this case we have,

$$
{\mathbf{K}}^\prime = {\mathbf{K}}- \frac{{\mathbf{{k}}}_\ast{\mathbf{{k}}}^\top_\ast}{{k}_{*,*}}
$$ and $$
{\boldsymbol{{\mu}}}^\prime = {\boldsymbol{{\mu}}}+ \frac{{\mathbf{{k}}}_\ast}{{k}_{*,*}}
({v}_\ast-{\mu})
$$ where ${k}_\ast$ is the vector computed through the covariance
function between the training data ${{\bf X}}$ and the proposed point
that we are conditioning the scale upon, ${{\bf {x}}}_\ast$ and
${k}_{*,*}$ is the covariance function computed for ${{\bf {x}}}_\ast$.
Now the updated mean and covariance can be used in the maximum entropy
formulation as before. $$
q({v}) \propto \prod_{i=1}^{n}\exp\left(-
\beta {v}_i^2 L({y}_i, {f}({{\bf {x}}}_i)) \right)
\exp\left(-\frac{1}{2}({\mathbf{v}}-{\boldsymbol{{\mu}}}^\prime)^\top
\left.{\mathbf{K}}^\prime\right.^{-1} ({\mathbf{v}}-{\boldsymbol{{\mu}}}^\prime)\right)
$$

We will consider the same data set as above. We first create a Gaussian
process model for the update.

``` {.python}
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

``` {.python}
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

``` {.python}
model = BLMLGP(x, y, 
           basis=basis, 
           kernel=mlai.kernel(mlai.eq_cov, lengthscale=20, variance=1.0),
           mu=0.0,
           beta=1.0, 
           alpha=1000,
           X_star=np.asarray([[2020]]), 
           v_star=np.asarray([[1]]))
```

``` {.python}
model.fit()
```

``` {.python}
f_test, f_var = model.predict(x_test)
```

``` {.python}
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

``` {.python}
import pods
```

``` {.python}
pods.notebook.display_plots('olympic-gp-loss-bayes-linear-regression{number:0>3}.svg', 
                            directory='../slides/diagrams/ml', number=(0, 1))
```

Finally we make an attempt to show the joint uncertainty by first of all
sampling from

``` {.python}
fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
num_samps=10
samps=np.random.multivariate_normal(model.gp_model.f.flatten(), model.gp_model.C, size=100).T**2
ax.plot(x, samps, '-x', markersize=10, linewidth=2)
ax.set_xlim(data_limits[0], data_limits[1])
ax.set_xlabel('year')
_ = ax.set_ylabel('$s_i$')
mlai.write_figure('../slides/diagrams/ml/olympic-gp-loss-samples.svg', transparent=True)
```

<object class="svgplot" align data="../slides/diagrams/ml/olympic-gp-loss-samples.svg">
</object>
``` {.python}
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

``` {.python}
import pods
pods.notebook.display_plots('olympic-gp-loss-bayes-linear-regression-and-samples{number:0>3}.svg', 
                            directory='../slides/diagrams/ml', number=(0, 1))
```

``` {.python}
fig, ax = plt.subplots(figsize=plot.big_figsize)
ax.hist(np.asarray(allsamps), bins=30, density=True)
ax.set_xlabel='pace min/kim'
mlai.write_figure('../slides/diagrams/ml/olympic-gp-loss-histogram-2020.svg', transparent=True)
```

### Histogram from 2020 {#histogram-from-2020 .slide: data-transition="none"}

<object class="svgplot" align data="../slides/diagrams/ml/olympic-gp-loss-histogram-2020.svg">
</object>
### Conclusions

-   Maximum Entropy Framework for uncertainty in
    -   Loss functions
    -   Prediction functions

### Thanks!

-   twitter: @lawrennd
-   blog:
    [http://inverseprobability.com](http://inverseprobability.com/blog.html)
