\helpercode{%load -s polynomial_cov mlai.py}

\code{plot.covariance_func(x, compute_kernel, 
                     formula = r'$$k(\inputVector, \inputVector^\prime) = \alpha(w \inputVector^\top \inputVector^\prime + b)^d$$', 
                     shortname='poly', 
                     longname='Polynomial', 
					 kernel=polynomial_cov,
                     degree=4., 
					 diagrams='../../slides/diagrams/kern')}


### Polynomial Covariance

$$k(\mathbf{x}, \mathbf{x}^\prime) = \alpha(w \mathbf{x}^\top
\mathbf{x}^\prime + b)^d$$

<table><tr><td>
\includesvg{../slides/diagrams/kern/poly_covariance.svg}
</td>
<td>
\includeimg{../slides/diagrams/kern/poly_covariance.gif}{50%}
</td>
</tr>
</table>


