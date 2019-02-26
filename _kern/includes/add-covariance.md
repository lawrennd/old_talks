\ifndef{addCovariance}
\define{addCovariance}
\editme

\subsection{Additive Covariance}

\define{\formula}{\kernelScalar_f(\inputVector, \inputVector^\prime) = \kernelScalar_g(\inputVector, \inputVector^\prime) + \kernelScalar_h(\inputVector, \inputVector^\prime)}

\loadplotcode{Kernel}{mlai}

\loadplotcode{linear_cov}{mlai}

\loadplotcode{eq_cov}{mlai}

\loadplotcode{add_cov}{mlai}

\plotcode{kernel = Kernel(function=add_cov,
                     name='Additive',
                     shortname='add',                     
                     formula='\formula', 
                     kerns=[linear_cov, eq_cov], 
                     kern_args=[{'variance': 25}, {'lengthscale' : 0.2}])}

\setupplotcode{import teaching_plots as plot}
\plotcode{plot.covariance_func(kernel=kernel, diagrams='../slides/diagrams/kern/')}

\notes{An additive covariance function is derived from considering the result of summing two Gaussian processes together. If the first Gaussian process is $g(\cdot)$, governed by covariance $\kernelScalar_g(\cdot, \cdot)$ and the second process is $h(\cdot)$, governed by covariance $\kernelScalar_h(\cdot, \cdot)$ then the combined process $f(\cdot) = g(\cdot) + h(\cdot)$ is govererned by a covariance function,
$$
\formula
$$
}

\includecovariance{add}{\formula}{An additive covariance function formed by combining two exponentiated quadratic covariance functions.}

\endif
