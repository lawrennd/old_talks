\ifndef{gpIntroVeryShort}
\define{gpIntroVeryShort}
\editme

\notes{\subsection{Bayesian Inference by Rejection Sampling}

One view of Bayesian inference is to assume we are given a mechanism for generating samples, where we assume that mechanism is representing an accurate view on the way we believe the world works. 

This mechanism is known as our *prior* belief. 

We combine our prior belief with our observations of the real world by discarding all those prior samples that are inconsistent with our observations. The *likelihood* defines mathematically what we mean by inconsistent with the observations. The higher the noise level in the likelihood, the looser the notion of consistent.

The samples that remain are samples from the *posterior*. 

This approach to Bayesian inference is closely related to two sampling techniques known as *rejection sampling* and *importance sampling*. It is realized in practice in an approach known as *approximate Bayesian computation* (ABC) or likelihood-free inference. 

In practice, the algorithm is often too slow to be practical, because most samples will be inconsistent with the observations and as a result the mechanism must be operated many times to obtain a few posterior samples. 

However, in the Gaussian process case, when the likelihood also assumes Gaussian noise, we can operate this mechanism mathematically, and obtain the posterior density *analytically*. This is the benefit of Gaussian processes.}


\notes{First, we will load in two python functions for computing the covariance function.}

\loadplotcode{Kernel}{mlai}
\plotcode{# %load -n mlai.Kernel
class Kernel():
    """Covariance function
    :param function: covariance function
    :type function: function
    :param name: name of covariance function
    :type name: string
    :param shortname: abbreviated name of covariance function
    :type shortname: string
    :param formula: latex formula of covariance function
    :type formula: string
    :param function: covariance function
    :type function: function
    :param \**kwargs:
        See below

    :Keyword Arguments:
        * """

    def __init__(self, function, name=None, shortname=None, formula=None, **kwargs):        
        self.function=function
        self.formula = formula
        self.name = name
        self.shortname = shortname
        self.parameters=kwargs
        
    def K(self, X, X2=None):
        """Compute the full covariance function given a kernel function for two data points."""
        if X2 is None:
            X2 = X
        K = np.zeros((X.shape[0], X2.shape[0]))
        for i in np.arange(X.shape[0]):
            for j in np.arange(X2.shape[0]):
                K[i, j] = self.function(X[i, :], X2[j, :], **self.parameters)

        return K

    def diag(self, X):
        """Compute the diagonal of the covariance function"""
        diagK = np.zeros((X.shape[0], 1))
        for i in range(X.shape[0]):            
            diagK[i] = self.function(X[i, :], X[i, :], **self.parameters)
        return diagK

    def _repr_html_(self):
        raise NotImplementedError}

\loadplotcode{eq_cov}{mlai}

\plotcode{# %load -n mlai.eq_cov
def eq_cov(x, x_prime, variance=1., lengthscale=1.):
    """Exponentiated quadratic covariance function."""
    diffx = x - x_prime
    return variance*np.exp(-0.5*np.dot(diffx, diffx)/lengthscale**2)}

\plotcode{kernel = Kernel(function=eq_cov,
                     name='Exponentiated Quadratic',
                     shortname='eq',					 
					 lengthscale=0.25)}

\notes{Next, we sample from a multivariate normal density (a multivariate Gaussian), using the covariance function as the covariance matrix.}

\setupplotcode{import numpy as np
np.random.seed(10)
import mlai.plot}
\plotcode{plot.rejection_samples(kernel=kernel, 
    diagrams='\writeDiagramsDir/gp')}


\setupdisplaycode{import notutils as nu
from ipywidgets import IntSlider}
\displaycode{nu.display_plots('gp_rejection_sample{sample:0>3}.png', 
                 directory='\writeDiagramsDir/gp', 
                 sample=IntSlider(1,1,5,1))}
\slides{
\newslide{}

\includepng{\diagramsDir/gp/gp_rejection_sample001}{100%}{negate}

\speakernotes{Here we're showing 20 samples taken from the prior over functions defined by our covarariance}

\newslide{}

\includepng{\diagramsDir/gp/gp_rejection_sample002}{100%}{negate}

\speakernotes{We can sample many such functions, in this slide there are now 1000 in total. This is a sample from our prior over functions.}


\newslide{}

\includepng{\diagramsDir/gp/gp_rejection_sample003}{100%}{negate}

\speakernotes{Now we observe data. Here there are three data points. Conceptually in Bayesian inference we discard all samples that are distant from the data.}

\newslide{}

\includepng{\diagramsDir/gp/gp_rejection_sample004}{100%}{negate}

\speakernotes{Throwing away such samples we are left with our posterior. This is the collection of samples from the prior that are consistent with the data.}

\newslide{} 

\includepng{\diagramsDir/gp/gp_rejection_sample005}{100%}{negate}

\speakernotes{The elegance of the Gaussian process is that this result can be computed analytically using linear algebra.}
}
\notes{\figure{\includepng{\diagramsDir/gp/gp_rejection_sample003}{100%}
\includepng{\diagramsDir/gp/gp_rejection_sample004}{100%}
\includepng{\diagramsDir/gp/gp_rejection_sample005}{100%}}{One view of Bayesian inference is we have a machine for generating samples (the *prior*), and we discard all samples inconsistent with our data, leaving the samples of interest (the *posterior*). This is a rejection sampling view of Bayesian inference. The Gaussian process allows us to do this analytically by multiplying the *prior* by the *likelihood*.}{gp-rejection-samples}}

\endif
