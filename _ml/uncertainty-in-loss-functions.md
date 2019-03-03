---
title: "Uncertainty in Loss Functions"
abstract: "Bayesian formalisms deal with uncertainty in parameters, frequentist formalisms deal with the *risk* of a data set, uncertainty in the data sample. In this talk, we consider uncertainty in the *loss function*. Uncertainty in the loss function. We introduce uncertainty through linear weightings of terms in the loss function and show how a distribution over the loss can be maintained through the *maximum entropy principle*. This allows us minimize the expected loss under our maximum entropy distribution of the loss function. We recover weighted least squares and a LOESS-like regression from the formalism."
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: Amazon Cambridge and University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
date: 2018-05-29
venue: IWCV 2018, Modena, Italy
geometry: ["a4paper", "margin=2cm"]
papersize: a4paper
transition: None
---

\include{talk-macros.tex}

\editme
\section{Introduction}

\include{_ml/includes/what-is-ml.md}
\include{_ai/includes/artificial-vs-natural-systems.md}

\notes{Uncertainty in models is handled by Bayesian inference, here we
consider uncertainty arising in loss functions.

Consider a loss function which
decomposes across individual observations, $\dataScalar_{k,j}$, each of which is
dependent on some set of features, $\inputVector_k$.}
\slides{### Classical Loss Function}
$$
\errorFunction(\dataVector, \inputMatrix) = \sum_{k}\sum_{j}
L(\dataScalar_{k,j}, \inputVector_k)
$$
\notes{Assume that the loss function depends
on the features through some mapping function, $\mappingFunction_j(\cdot)$ which
we call the *prediction function*.}
\slides{* Dependent on a prediction function}
$$
\errorFunction(\dataVector, \inputMatrix) = \sum_{k}\sum_{j} L(\dataScalar_{k,j},
\mappingFunction_j(\inputVector_k))
$$
\notes{without loss of generality, we can move
the index to the inputs, so we have $\inputVector_i =\left[\inputVector \quad
j\right]$, and we set $\dataScalar_i = \dataScalar_{k, j}$. So we have}
\slides{### Absorb $j$ into $\inputVector$}
$$
\errorFunction(\dataVector, \inputMatrix) = \sum_{i} L(\dataScalar_i, \mappingFunction(\inputVector_i))
$$
\notes{Bayesian inference considers uncertainty in $\mappingFunction$, often through parameterizing it, $\mappingFunction(\inputVector; \parameterVector)$, and considering a *prior* distribution for the parameters, $p(\parameterVector)$, this in turn implies a distribution over functions, $p(\mappingFunction)$.  Process models, such as Gaussian processes specify this distribution, known as a process, directly.

Bayesian inference proceeds by specifying a *likelihood* which relates the data, $\dataScalar$, to the parameters. Here we choose not to do this, but instead we only consider the *loss* function for our objective. The loss is the cost we pay for a misclassification.

The *risk function* is the expectation of the loss under the distribution of the data. Here we are using the framework of *empirical risk* minimization, because we have a sample based approximation. The new expectation we are considering is around the loss function itself, not the uncertainty in the data.

The loss function and the log likelihood may take a mathematically similar form but they are philosophically very different. The log likelihood assumes something about the *generating* function of the data, whereas the loss function assumes something about the cost we pay. Importantly the loss function in Bayesian inference only normally enters at the point of decision.

The key idea in Bayesian inference is that the probabilistic inference can be performed *without* knowing the loss becasue if the model is correct, then the form of the loss function is irrelevant when performing inference. In practice, however, for real data sets the model is almost never correct.

Some of the maths below looks similar to the maths we can find in Bayesian methods, in particular variational Bayes, but that is merely a consequence of the availability of analytical mathematics. There are only particular ways of developing tractable algorithms, one route involves linear algebra. However, the similarity of the mathematics belies a difference in interpretation. It is similar to travelling a road (e.g. Ermine Street) in a wild landscape. We travel together because that is where efficient progress is to be made, but in practice a our destinations (Lincoln, York), may be different.}

\subsection{Introduce Uncertainty}

\notes{To introduce uncertainty we consider a weighted version of the loss function, we introduce positive weights,}\slides{* Introduce} $\left\{ \scaleScalar_i\right\}_{i=1}^\numData$.
$$
\errorFunction(\dataVector, \inputMatrix) = \sum_{i}
\scaleScalar_i L(\dataScalar_i, \mappingFunction(\inputVector_i))
$$
\notes{We now assume that tmake the assumption that these weights are drawn from a distribution, $q(\scaleScalar)$. Instead of looking to minimize the loss direction, we look at the expected loss under this distribution.}
\slides{* Assume $\scaleScalar \sim q(\scaleScalar)$}
$$
\begin{align*}
\errorFunction(\dataVector, \inputMatrix) = & \sum_{i}\expectationDist{\scaleScalar_i L(\dataScalar_i, \mappingFunction(\inputVector_i))}{q(\scaleScalar)} \\
& =\sum_{i}\expectationDist{\scaleScalar_i }{q(\scaleScalar)}L(\dataScalar_i, \mappingFunction(\inputVector_i))
\end{align*}
$$
\notes{We will assume that our process, $q(\scaleScalar)$ can depend on a variety of inputs such as $\dataVector$, $\inputMatrix$ and time, $t$.}

\subsection{Principle of Maximum Entropy}

\notes{To maximize uncertainty in $q(\scaleScalar)$ we maximize its entropy. Following Jaynes formalism of maximum entropy, in the continuous space we do this with respect to an invariant measure,}\slides{* Maximum entropy principle}
$$
H(\scaleScalar)= - \int q(\scaleScalar) \log \frac{q(\scaleScalar)}{m(\scaleScalar)} \text{d}\scaleScalar
$$
\notes{and since we minimize the loss, we balance this by adding in this term to form}\slides{* Minimize loss minus Entropy}
$$
\begin{align*}
\errorFunction = & \beta\sum_{i}\expectationDist{\scaleScalar_i }{q(\scaleScalar)}L(\dataScalar_i, \mappingFunction(\inputVector_i)) - H(\scaleScalar)\\
&= \beta\sum_{i}\expectationDist{\scaleScalar_i }{q(\scaleScalar)}L(\dataScalar_i, \mappingFunction(\inputVector_i)) +  \int q(\scaleScalar) \log \frac{q(\scaleScalar)}{m(\scaleScalar)}\text{d}\scaleScalar
\end{align*}
$$
\notes{where $\beta$ serves to weight the relative
contribution of the entropy term and the loss term.}

\slides{### Freeform Minimization wrt $q(\scaleScalar)$}

\notes{We can now minimize this modified loss with respect to the density $q(\scaleScalar)$, the freeform optimization over this term leads to}
$$
\begin{align*}
q(\scaleScalar) \propto & \exp\left(- \beta \sum_{i=1}^\numData \scaleScalar_i L(\dataScalar_i, \mappingFunction(\inputVector_i)) \right) m(\scaleScalar)\\
 \propto & \prod_{i=1}^\numData \exp\left(- \beta \scaleScalar_i L(\dataScalar_i, \mappingFunction(\inputVector_i)) \right) m(\scaleScalar)
\end{align*}
$$

### Example

\slides{* }Assume 
$$
m(\scaleScalar) = \prod_i \lambda\exp\left(-\lambda\scaleScalar_i\right)
$$
\notes{which is the distribution with the maximum entropy for a given mean, $\scaleScalar$.}
\slides{*} Then we have
$$ 
q(\scaleScalar) = \prod_i q(\scaleScalar_i)
$$
$$
q(\scaleScalar_i) \propto \frac{1}{\lambda+\beta L_i} \exp\left(-(\lambda+\beta L_i) \scaleScalar_i\right)
$$
\notes{and we can compute}\slides{* And}
$$
\expectationDist{\scaleScalar_i}{q(\scaleScalar)} =
\frac{1}{\lambda + \beta L_i}
$$

### Coordinate Descent

\notes{We can minimize with respect to $q(\scaleScalar)$ recovering,}\slides{* Optimize wrt $q(\cdot)$}
$$
q(\scaleScalar_i) = \frac{1}{\lambda+\beta L_i} \exp\left(-(\lambda+\beta L_i) \scaleScalar_i\right)
$$t
\slides{* Update expectation}\notes{allowing us to compute the expectation of $\scaleScalar$,}
$$
\expectationDist{\scaleScalar_i}{q(\scaleScalar_i)} = \frac{1}{\lambda+\beta
L_i}
$$
\slides{* Minimize expected loss}\notes{then, we can minimize our expected loss with respect to $\mappingFunction(\cdot)$}
$$
\beta \sum_{i=1}^\numData \expectationDist{\scaleScalar_i}{q(\scaleScalar_i)} L(\dataScalar_i, \mappingFunction(\inputVector_i))
$$
\notes{If the loss is the *squared loss*, then this is recognised as a *reweighted least squares algorithm*. However, the loss can be of any form as long as $q(\scaleScalar)$ defined above exists.}

\notes{In addition to the above, in our example below, we updated $\beta$ to normalize the expected loss to be $\numData$ at each iteration, so we
have
$$
\beta = \frac{\numData}{\sum_{i=1}^\numData \expectationDist{\scaleScalar_i}{q(\scaleScalar_i)} L(\dataScalar_i, \mappingFunction(\inputVector_i))}
$$}

\include{_ml/includes/olympic-marathon-data.md}

\subsection{Example: Linear Regression}

\setupcode{import mlai
import numpy as np
import scipy as sp}

\notes{Create a weighted linear regression class, inheriting from the ```mlai.LM```
class.}

\code{class LML(mlai.LM):
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
        return (self.losses*self.s).sum()}


\notes{Set up a linear model (polynomial with two basis functions).}

\code{num_basis=2 
data_limits=[1890, 2020]
basis = mlai.basis(mlai.polynomial, num_basis, data_limits=data_limits)
model = LML(x, y, basis=basis, lambd=1, beta=1)
model2 = mlai.LM(x, y, basis=basis)}

\code{model.fit()
model2.fit()}

\code{import matplotlib.pyplot as plt}

\code{x_test = np.linspace(data_limits[0], data_limits[1], 130)[:, None]
f_test, f_var = model.predict(x_test)
f2_test, f2_var = model2.predict(x_test)}

\code{import teaching_plots as plot
from matplotlib import rc, rcParams
rcParams.update({'font.size': 22})
rc('text', usetex=True)}

\code{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
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
mlai.write_figure('../slides/diagrams/ml/olympic-loss-linear-regression001.svg', transparent=True)}

\code{import pods
pods.notebook.display_plots('olympic-loss-linear-regression{number:0>3}.svg', 
                            directory='../slides/diagrams/ml', number=(0, 1))}

\newslide{Linear Regression on Olympic Data}

\slides{
\figure{\includediagram{../slides/diagrams/ml/olympic-loss-linear-regression000}{80%}}{}{olympic-loss-linear-regression-0}

\newslide{Linear Regression on Olympic Data}
}
\figure{\includediagram{../slides/diagrams/ml/olympic-loss-linear-regression001}{80%}}{Linear regression for the standard quadratic loss in *red* and the probabilistically weighted loss in *blue*.}{olympic-loss-linear-regression-1}

\subsection{Parameter Uncertainty}

\slides{* In Bayesian inference we consider parameter uncertainty}
\notes{Classical Bayesian inference is concerned with
parameter uncertainty, which equates to uncertainty in the *prediction
function*, $\mappingFunction(\inputVector)$. The prediction function is normally
an estimate of the value of $\dataScalar$ or constructs a probability density
for $\dataScalar$. 

Uncertainty in the prediction function can arise through
uncertainty in our loss function, but also through uncertainty in parameters in
the classical Bayesian sense. The full maximum entropy formalism would now be}
$$
\expectationDist{\beta \scaleScalar_i L(\dataScalar_i,
\mappingFunction(\inputVector_i))}{q(\scaleScalar, \mappingFunction)} + \int
q(\scaleScalar, \mappingFunction) \log \frac{q(\scaleScalar,
\mappingFunction)}{m(\scaleScalar)m(\mappingFunction)}\text{d}\scaleScalar
\text{d}\mappingFunction
$$
\slides{* Implying}
$$
q(\mappingFunction, \scaleScalar) \propto
\prod_{i=1}^\numData \exp\left(- \beta \scaleScalar_i L(\dataScalar_i,
\mappingFunction(\inputVector_i)) \right) m(\scaleScalar)m(\mappingFunction)
$$

\subsection{Approximation}

* Generally intractable, so assume:
$$
q(\mappingFunction, \scaleScalar) = q(\mappingFunction)q(\scaleScalar)
$$

\newslide{Approximation II}

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

\newslide{Approximation III}

* Can now proceed with iteration between $q(\scaleScalar)$, $q(\mappingFunction)$

\code{class BLML(mlai.BLM):
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
        

 }

\code{model = BLML(x, y, basis=basis, alpha=1000, lambd=1, beta=1)
model2 = mlai.BLM(x, y, basis=basis, alpha=1000, sigma2=1)}

\code{model.fit()
model2.fit()}

\code{x_test = np.linspace(data_limits[0], data_limits[1], 130)[:, None]
f_test, f_var = model.predict(x_test)
f2_test, f2_var = model2.predict(x_test)}

\code{import gp_tutorial}

\code{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
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
}

\code{import pods
pods.notebook.display_plots('olympic-loss-bayes-linear-regression{number:0>3}.svg', 
                            directory='../slides/diagrams/ml', number=(0, 1))}


\newslide{Probabilistic Linear Regression on Olympic Data}

\figure{\includediagram{../slides/diagrams/ml/olympic-loss-bayes-linear-regression000}{80%}}{Probabilistic linear regression for the standard quadratic loss in *red* and the probabilistically weighted loss in *blue*.}{olympic-loss-bayes-linear-regression-0}

\newslide{Probabilistic Linear Regression on Olympic Data}

\figure{\includediagram{../slides/diagrams/ml/olympic-loss-bayes-linear-regression001}{80%}}{Probabilistic linear regression for the standard quadratic loss in *red* and the probabilistically weighted loss in *blue*.}{olympic-loss-bayes-linear-regression-1}

\subsection{Correlated Scales}

\notes{Going beyond independence between weights, we now consider
$m(\vScalar)$ to be a Gaussian process, and scale by the *square* of $\vScalar$,
$\scaleScalar=\vScalar^2$}\slides{* Assume the measure is a GP}
$$
\vScalar \sim \mathcal{GP}\left(\meanScalar(\inputVector), \kernel(\inputVector, \inputVector^\prime)\right)
$$
\slides{* Assume $\scaleScalar = \vScalar^2$}

\newslide{Correlated Scales II}
\slides{
* Implies
$$
q(\vScalar) \propto
\prod_{i=1}^\numData \exp\left(- \beta \vScalar_i^2 L(\dataScalar_i,
\mappingFunction(\inputVector_i)) \right)\mathcal{GP}\left(\meanScalar(\inputVector), \kernel(\inputVector, \inputVector^\prime)\right)
$$}
\notes{$$
q(\vScalar) \propto
\prod_{i=1}^\numData \exp\left(- \beta \vScalar_i^2 L(\dataScalar_i,
\mappingFunction(\inputVector_i)) \right)
\exp\left(-\frac{1}{2}(\vVector-\meanVector)^\top \kernelMatrix^{-1}
(\vVector-\meanVector)\right)
$$
where $\kernelMatrix$ is the covariance of the
process made up of elements taken from the covariance function,
$\kernelScalar(\inputVector, t, \dataVector; \inputVector^\prime, t^\prime,
\dataVector^\prime)$ so $q(\vScalar)$ itself is Gaussian with covariance}\slides{* Gives $q(\vScalar)$ as Gaussian with covariance:}
$$
\covarianceMatrix = \left(\beta\mathbf{L} + \kernelMatrix^{-1}\right)^{-1}
$$
and mean
$$
\meanTwoVector = \beta\covarianceMatrix\mathbf{L}\meanVector
$$
\notes{where $\mathbf{L}$ is a matrix containing the loss functions, $L(\dataScalar_i,
\mappingFunction(\inputVector_i))$ along its diagonal elements with zeros
elsewhere.}

\newslide{Expectation Update}
\slides{
* }The update is given by 
$$
\expectationDist{\vScalar_i^2}{q(\vScalar)} = \meanTwoScalar_i^2 +
\covarianceScalar_{i, i}.
$$
\slides{* If measure covariance spherical and mean zero}\notes{To compare with before, if the mean of the measure $m(\vScalar)$  was zero and the prior covariance was spherical, $\kernelMatrix=\lambda^{-1}\eye$. Then this would equate to an update,}
$$
\expectationDist{\vScalar_i^2}{q(\vScalar)} = \frac{1}{\lambda + \beta L_i}
$$
which is the same as we had before for the exponential prior over
$\scaleScalar$.

\subsection{Conditioning the Measure}

\notes{Now that we have defined a process over $\vScalar$, we could define a region in which we're certain that we would like the weights to be high. For example, if we were looking to have a test point at location $\inputVector_\ast$, we could update our measure to be a Gaussian process that is conditioned on the observation of $\vScalar_\ast$ set appropriately at $\inputScalar_\ast$. In this case we have,}
\slides{* Condition measure to be high weight in *test* region}
$$
\kernelMatrix^\prime = \kernelMatrix - \frac{\kernelVector_\ast\kernelVector^\top_\ast}{\kernelScalar_{*,*}}
$$
and 
$$
\meanVector^\prime = \meanVector + \frac{\kernelVector_\ast}{\kernelScalar_{*,*}}
(\vScalar_\ast-\meanScalar)
$$
\notes{where $\kernelScalar_\ast$ is the vector computed
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
$$}
\slides{* As covariance becomes small, this becomes *LOESS regression*}

\notes{We will consider the same data set as above. We first create a
Gaussian process model for the update.}

\code{class GPL(mlai.GP):
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
                raise ValueError("v_star should not be None when X_star is None")}

\code{class BLMLGP(BLML):
    def __init__(self, X, y, basis=None, kernel=None, beta=1.0, mu=0.0, alpha=1.0, X_star=None, v_star=None):
        BLML.__init__(self, X, y, basis=basis, alpha=alpha, beta=beta, lambd=None)
        self.gp_model=GPL(self.X, self.losses, kernel=kernel, beta=beta, mu=mu, X_star=X_star, v_star=v_star)
    def update_s(self):
        """Update the weights"""
        self.gp_model.C = sp.linalg.inv(sp.linalg.inv(self.gp_model.K+np.eye(self.X.shape[0])*1e-6) + self.beta*np.diag(self.losses.flatten()))
        self.gp_model.diagC = np.diag(self.gp_model.C)[:, np.newaxis]
        self.gp_model.f = self.gp_model.beta*np.dot(np.dot(self.gp_model.C,np.diag(self.losses.flatten())),self.gp_model.mu) +self.gp_model.mu
        
        #f, v = self.gp_model.K self.gp_model.predict(self.X)
        self.s = self.gp_model.f*self.gp_model.f + self.gp_model.diagC # + 1.0/(self.losses*self.gp_model.beta)}

\code{model = BLMLGP(x, y, 
           basis=basis, 
           kernel=mlai.kernel(mlai.eq_cov, lengthscale=20, variance=1.0),
           mu=0.0,
           beta=1.0, 
           alpha=1000,
           X_star=np.asarray([[2020]]), 
           v_star=np.asarray([[1]]))}

\code{model.fit()}

\code{f_test, f_var = model.predict(x_test)}

\code{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
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
mlai.write_figure('../slides/diagrams/ml/olympic-gp-loss-bayes-linear-regression001.svg', transparent=True)}

\setupcode{import pods}
\code{pods.notebook.display_plots('olympic-gp-loss-bayes-linear-regression{number:0>3}.svg', 
                            directory='../slides/diagrams/ml', number=(0, 1))}


\newslide{Olympic Data: GP Measure}

\slides{\figure{\includediagram{../slides/diagrams/ml/olympic-gp-loss-bayes-linear-regression000}{80%}}{}{olympic-gp-loss-bayes-linear-0}
}
\newslide{Olympic Data: GP Measure}

\figure{\includediagram{../slides/diagrams/ml/olympic-gp-loss-bayes-linear-regression001}{80%}}{Probabilistic linear regression for the standard quadratic loss in *red* and the probabilistically weighted loss with a Gaussian process measure in *blue*.}{olympic-gp-loss-bayes-linear-regression-1}


\newslide{Joint Uncertainty}

\notes{Finally, we make an attempt to show the joint uncertainty
by first of all sampling from the loss function weights density, $q(\scaleScalar)$.}

\code{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
num_samps=10
samps=np.random.multivariate_normal(model.gp_model.f.flatten(), model.gp_model.C, size=100).T**2
ax.plot(x, samps, '-x', markersize=10, linewidth=2)
ax.set_xlim(data_limits[0], data_limits[1])
ax.set_xlabel('year')
_ = ax.set_ylabel('$s_i$')
mlai.write_figure('../slides/diagrams/ml/olympic-gp-loss-samples.svg', transparent=True)}

\figure{\includediagram{../slides/diagrams/ml/olympic-gp-loss-samples}{80%}}{Samples of loss weightings from the density $q(\scaleSamples)$.}}{olympic-gp-loss-samples}

\code{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
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
mlai.write_figure('../slides/diagrams/ml/olympic-gp-loss-bayes-linear-regression-and-samples001.svg', transparent=True)}

\code{import pods
pods.notebook.display_plots('olympic-gp-loss-bayes-linear-regression-and-samples{number:0>3}.svg', 
                            directory='../slides/diagrams/ml', number=(0, 1))}

\newslide{Joint Samples from Regression}
\slides{
\figure{\includediagram{../slides/diagrams/ml/olympic-gp-loss-bayes-linear-regression-and-samples000}{80%}}{Samples from the joint density of loss weightings and regression weights.}{olympic-gp-loss-bayes-linear-regression-and-samples-0
}

\newslide{Joint Samples from Regression}

\figure{\includediagram{../slides/diagrams/ml/olympic-gp-loss-bayes-linear-regression-and-samples001}{80%}}{Samples from the joint density of loss weightings and regression weights show the full distribution of function predictions.}{olympic-gp-loss-bayes-linear-regression-and-samples-1}


\code{fig, ax = plt.subplots(figsize=plot.big_figsize)
ax.hist(np.asarray(allsamps), bins=30, density=True)
ax.set_xlabel='pace min/kim'
mlai.write_figure('../slides/diagrams/ml/olympic-gp-loss-histogram-2020.svg', transparent=True)}

\newslide{Histogram from 2020}

\figure{\includediagram{../slides/diagrams/ml/olympic-gp-loss-histogram-2020}{80%}}{Histogram of samples from the year 2020, where the weight of the loss function was pinned to ensure that the model focussed its predictions on this region for test data.}{olympic-gp-loss-histogram-2020}

\subsection{Conclusions}

* Maximum Entropy Framework for uncertainty in 
    * Loss functions
    * Prediction functions

\thanks

\references
