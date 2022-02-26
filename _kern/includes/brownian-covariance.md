\ifndef{brownianCovariance}
\define{brownianCovariance}
\editme

\subsection{Brownian Covariance}

\define{\formula}{\kernelScalar(t, t^\prime)=\alpha \min(t, t^\prime)}

\loadcode{brownian_cov}{mlai}

\setupplotcode{import mlai.plot as plot
import mlai
import numpy as np}

\plotcode{t=np.linspace(0, 2, 200)[:, np.newaxis]
kernel = mlai.Kernel(function=brownian_cov,
                     name='Brownian',
                     formula='\formula',
                     shortname='brownian')
plot.covariance_func(kernel, t, diagrams='\writeDiagramsDir/kern/')}

\notes{Brownian motion is also a Gaussian process. It follows a Gaussian random walk, with diffusion occuring at each time point driven by a Gaussian input. This implies it is both Markov and Gaussian. The covariance function for Brownian motion has the form
$$
\formula
$$}

\includecovariance{brownian}{\formula}{Brownian motion covariance function.}


\endif
