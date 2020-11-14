\ifndef{matern52Covariance}
\define{matern52Covariance}
\editme

\subsection{Matérn 5/2 Covariance}

\define{\formula}{\kernelScalar(\inputVector, \inputVector^\prime) = \alpha \left(1+\frac{\sqrt{5}\ltwoNorm{\inputVector-\inputVector^\prime}}{\lengthScale} + \frac{5\ltwoNorm{\inputVector-\inputVector^\prime}^2}{3\lengthScale^2}\right)\exp\left(-\frac{\sqrt{5}\ltwoNorm{\inputVector-\inputVector^\prime}}{\lengthScale}\right)}

\loadplotcode{Kernel}{mlai}
\loadplotcode{matern52_cov}{mlai}

\plotcode{kernel = Kernel(function=matern52_cov,
                     name='Matérn 5/2',
                     shortname='matern52',					 
                     formula='\formula',
					 lengthscale=0.2)}

\setupplotcode{import teaching_plots as plot}
\plotcode{plot.covariance_func(kernel=kernel, diagrams='\writeDiagramsDir/kern/')}

\notes{The Matérn 5/2 [@Stein:interpolation99] covariance is which is once differentiable, it arises from applying a Student-$t$ based filter in Fourier space with five degrees of freedom. 

The covariance takes the following form,
$$
\formula
$$
where $\ell$ is the *length scale* or *time scale* of the process and $\alpha$ represents the overall process variance.}

\includecovariance{matern52}{\formula}{The exponentiated quadratic covariance function.}


\endif
