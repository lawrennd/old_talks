\editme

\notes{\subsection{Bayesian Inference by Rejection Sampling}

One view of Bayesian inference is to assume we are given a mechanism for generating samples, where we assume that mechanism is representing on accurate view on the way we believe the world works. 

This mechanism is known as our *prior* belief. 

We combine our prior belief with our observations of the real world by discarding all those samples that are inconsistent with our prior. The *likelihood* defines mathematically what we mean by inconsistent with the prior. The higher the noise level in the likelihood, the looser the notion of consistent.

The samples that remain are considered to be samples from the *posterior*. 

This approach to Bayesian inference is closely related to two sampling techniques known as *rejection sampling* and *importance sampling*. It is realized in practice in an approach known as *approximate Bayesian computation* (ABC) or likelihood-free inference. 

In practice, the algorithm is often too slow to be practical, because most samples will be inconsistent with the data and as a result the mechanism has to be operated many times to obtain a few posterior samples. 

However, in the Gaussian process case, when the likelihood also assumes Gaussian noise, we can operate this mechanims mathematically, and obtain the posterior density *analytically*. This is the benefit of Gaussian processes.}

\setupcode{import numpy as np}
\loadcode{compute_kernel}{mlai}
\loadcode{exponentiated_quadratic}{mlai}


\setupplotcode{import numpy as np
np.random.seed(10)
import teaching_plots as plot
from mlai import Kernel}
\plotcode{kernel = Kernel(function=exponentiated_quadratic, lengthscale=0.25)
plot.rejection_samples(kernel.K,
                       lengthscale=0.25, 
					   diagrams='../slides/diagrams/gp')}


\setupdisplaycode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('gp_rejection_sample{sample:0>3}.svg', 
                            directory='../slides/diagrams/gp', 
							sample=IntSlider(1,1,5,1))}
\slides{
###  {data-transition="none"}

\includesvg{../slides/diagrams/gp/gp_rejection_sample001.svg}

###  {data-transition="none"}

\includesvg{../slides/diagrams/gp/gp_rejection_sample002.svg}

###  {data-transition="none"}

\includesvg{../slides/diagrams/gp/gp_rejection_sample003.svg}

###  {data-transition="none"}

\includesvg{../slides/diagrams/gp/gp_rejection_sample004.svg}

###  {data-transition="none"}
x
\includesvg{../slides/diagrams/gp/gp_rejection_sample005.svg}
}
\notesfigure{\includesvg{../slides/diagrams/gp/gp_rejection_sample003.svg}
\includesvg{../slides/diagrams/gp/gp_rejection_sample004.svg}
\includesvg{../slides/diagrams/gp/gp_rejection_sample005.svg}}
\notes{\caption{One view of Bayesian inference is we have a machine for generating samples (the *prior*), and we discard all samples inconsistent with our data, leaving the samples of interest (the *posterior*). The Gaussian process allows us to do this analytically.}}
