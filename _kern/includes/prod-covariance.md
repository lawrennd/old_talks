\ifndef{prodCovariance}
\define{prodCovariance}

\editme

\subsection{Product Covariance}

\define{\formula}{\kernelScalar_f(\inputVector, \inputVector^\prime) = \kernelScalar_g(\inputVector, \inputVector^\prime) \kernelScalar_h(\inputVector, \inputVector^\prime)}

\loadplotcode{Kernel}{mlai}

\loadplotcode{linear_cov}{mlai}

\loadplotcode{eq_cov}{mlai}

\loadplotcode{prod_cov}{mlai}

\plotcode{kernel = Kernel(function=prod_cov,
                     name='Product',
                     shortname='prod',                     
                     formula='\formula', 
                     kerns=[linear_cov, eq_cov], 
                     kern_args=[{'variance': 25}, {'lengthscale' : 0.2}])}

\setupplotcode{import mlai.plot}
\plotcode{plot.covariance_func(kernel=kernel, diagrams='\writeDiagramsDir/kern/')}

\notes{An product covariance function is derived from considering the result of multiplying two stochastic processes together. If the first stochastic process is $g(\cdot)$, governed by covariance $\kernelScalar_g(\cdot, \cdot)$ and the second process is $h(\cdot)$, governed by covariance $\kernelScalar_h(\cdot, \cdot)$ then the combined process $f(\cdot) = g(\cdot)  h(\cdot)$ is governed by a covariance function,
$$
\formula
$$
Note that if $g(\cdot)$ and $h(\cdot)$ are Gaussian processes then $f(\cdot)$ will not in general be a Gaussian process. So the base processes are (presumably) some (unspecified) non-Gaussian processes.
}

\includecovariance{prod}{\formula}{An product covariance function formed by combining a linear and an exponentiated quadratic covariance functions.}

\endif
