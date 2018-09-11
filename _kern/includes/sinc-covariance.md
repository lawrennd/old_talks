\subsection{Sinc Covariance}

\notes{Another approach to developing covariance function exploits Bochner's theorem @Bochner:book59. Bochner's theorem tells us that any positve filter in Fourier space implies has an associated Gaussian process with a stationary covariance function. The covariance function is the *inverse Fourier transform* of the filter applied in Fourier space.

For example, in signal processing, *band limitations* are commonly applied as an assumption. For example, we may believe that no frequency above $w=2$ exists in the signal. This is equivalent to a rectangle function being applied as a the filter in Fourier space. 

The inverse Fourier transform of the rectangle function is the $\text{sinc}(\cdot)$ function. So the sinc is a valid covariance function, and it represents *band limited* signals.

Note that other covariance functions we've introduced can also be interpreted in this way. For example, the exponentiated quadratic covariance function can be Fourier transformed to see what the implied filter in Fourier space is. The Fourier transform of the exponentiated quadratic is an exponentiated quadratic, so the standard EQ-covariance implies a EQ filter in Fourier space.}

\define{\formula}{\kernelScalar(\inputVector, \inputVector^\prime) = \alpha \text{sinc}\left(\pi w r\right)}
\loadcode{sinc_cov}{mlai}

\setupplotcode{import teaching_plots as plot
import mlai
import numpy as np}

\plotcode{kernel = mlai.Kernel(function=sinc_cov,
                     name='Sinc',
                     shortname='sinc',					 
                     formula='\formula',
					 w=2)
					 
plot.covariance_func(kernel, diagrams='../slides/diagrams/kern/')}


\includecovariane{sinc}{\formula}
