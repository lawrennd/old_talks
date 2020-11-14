\ifndef{ouCovariance}
\define{ouCovariance}
\editme

\subsection{Exponential Covariance}

\define{\formula}{\kernelScalar(\inputVector, \inputVector^\prime) = \alpha \exp\left(-\frac{\ltwoNorm{\inputVector-\inputVector^\prime}}{\lengthScale}\right)}

\loadplotcode{Kernel}{mlai}
\loadplotcode{eq_cov}{mlai}

\plotcode{kernel = Kernel(function=ou_cov,
                     name='Ornstein Uhlenbeck',
                     shortname='ou',					 
                     formula='\formula',
					 lengthscale=0.2)}

\setupplotcode{import teaching_plots as plot}
\plotcode{plot.covariance_func(kernel=kernel, diagrams='\writeDiagramsDir/kern/')}

\notes{The expontential covariance, in one dimension this is also known as the Ornstein Uhlenbeck covariance, and in multiple dimensions it's also the Mater 1/2 covaraince. It has an interpretation as a stochastic differential equation with a linear drift term (equivalent to a quadratic potential). The drift keeps the covariance stationary (unlike the Brownian motion covariance). It also has an interpretation as a Cauchy filter in Fourier space [@Stein:interpolation99] (from Bochner's theorem). 

The covariance takes the following form,
$$
\formula
$$
where $\ell$ is the *length scale* or *time scale* of the process and $\alpha$ represents the overall process variance.}

\includecovariance{ou}{\formula}{The exponential covariance function.}


\endif
