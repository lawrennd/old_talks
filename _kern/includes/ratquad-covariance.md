\ifndef{ratquadCovariance}
\define{ratquadCovariance}
\editme

\subsection{Rational Quadratic Covariance}

\define{\formula}{\kernelScalar(\inputVector, \inputVector^\prime) = \alpha \left(1+\frac{\ltwoNorm{\inputVector-\inputVector^\prime}^2}{2 a \lengthScale^2}\right)^{-a}}

\loadplotcode{Kernel}{mlai}
\loadplotcode{ratquad_cov}{mlai}

\plotcode{kernel = Kernel(function=ratquad_cov,
                     name='Rational Quadratic',
                     shortname='ratquad',					 
                     formula='\formula',
					 lengthscale=0.2,
					 alpha=1)}

\setupplotcode{import teaching_plots as plot}
\plotcode{plot.covariance_func(kernel=kernel, diagrams='\writeDiagramsDir/kern/')}

\notes{The rational quadratic covariance function is derived by a continuous mixture of exponentiated quadratic covariance funcitons, where the lengthscale is given by an inverse gamma distribution. The resulting covariance is infinitely smooth (in terms of differentiability) but has a family of length scales present. As $a$ gets larger, the exponentiated quadratic covariance funciton is recovered.}

\notes{The covariance takes the following form,
$$
\formula
$$
where $\ell$ is the *length scale* or *time scale* of the process and $\alpha$ represents the overall process variance and $a$ represents shape parameter of the inverse Gamma used to create the scale mixture.}

\includecovariance{ratquad}{\formula}{The rational quadratic covariance function.}


\endif
