\ifndef{matern32Covariance}
\define{matern32Covariance}
\editme

\subsection{Matern 3/2 Covariance}

\define{\formula}{\kernelScalar(\inputVector, \inputVector^\prime) = \alpha \left(1+\frac{\sqrt{3}\ltwoNorm{\inputVector-\inputVector^\prime}}{\lengthScale}\right)\exp\left(-\frac{\sqrt{3}\ltwoNorm{\inputVector-\inputVector^\prime}}{\lengthScale}\right)}

\loadplotcode{Kernel}{mlai}
\loadplotcode{matern32_cov}{mlai}

\plotcode{kernel = Kernel(function=matern32_cov,
                     name='Matern 3/2',
                     shortname='matern32',					 
                     formula='\formula',
					 lengthscale=0.2)}

\setupplotcode{import teaching_plots as plot}
\plotcode{plot.covariance_func(kernel=kernel, diagrams='\writeDiagramsDir/kern/')}

\notes{The Mat\'ern 3/2 [@Stein:interpolation99] covariance is which is once differentiable, it arises from applying a Student-$t$ based filter in Fourier space with three degrees of freedom. 

The covariance takes the following form,
$$
\formula
$$
where $\ell$ is the *length scale* or *time scale* of the process and $\alpha$ represents the overall process variance.}

\includecovariance{matern32}{\formula}{The exponentiated quadratic covariance function.}


\endif
