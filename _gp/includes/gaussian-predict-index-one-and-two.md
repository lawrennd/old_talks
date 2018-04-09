\code{%load -s compute_kernel mlai.py}

\code{%load -s polynomial_cov mlai.py}

\code{%load -s exponentiated_quadratic mlai.py}

\plotcode{plot.two_point_sample(compute_kernel, kernel=exponentiated_quadratic, 
                      lengthscale=0.5, diagrams='../slides/diagrams/gp')}

\plotcode{pods.notebook.display_plots('two_point_sample{sample:0>3}.svg', 
                            '../slides/diagrams/gp', sample=(0,13))}
							
\slides{
### Gaussian Distribution Sample {data-transition="none"}

\includesvg{../slides/diagrams/gp/two_point_sample000.svg}

A 25 dimensional correlated random variable (values ploted against index)

### Gaussian Distribution Sample {data-transition="none"}

\includesvg{../slides/diagrams/gp/two_point_sample001.svg}

A 25 dimensional correlated random variable (values ploted against index)

### Gaussian Distribution Sample {data-transition="none"}

\includesvg{../slides/diagrams/gp/two_point_sample002.svg}

A 25 dimensional correlated random variable (values ploted against index)

### Gaussian Distribution Sample {data-transition="none"}

\includesvg{../slides/diagrams/gp/two_point_sample003.svg}

A 25 dimensional correlated random variable (values ploted against index)

### Gaussian Distribution Sample {data-transition="none"}

\includesvg{../slides/diagrams/gp/two_point_sample004.svg}

A 25 dimensional correlated random variable (values ploted against index)

### Gaussian Distribution Sample {data-transition="none"}

\includesvg{../slides/diagrams/gp/two_point_sample005.svg}

A 25 dimensional correlated random variable (values ploted against index)

### Gaussian Distribution Sample {data-transition="none"}

\includesvg{../slides/diagrams/gp/two_point_sample006.svg}

A 25 dimensional correlated random variable (values ploted against index)

### Gaussian Distribution Sample {data-transition="none"}

\includesvg{../slides/diagrams/gp/two_point_sample007.svg}

A 25 dimensional correlated random variable (values ploted against index)

### Gaussian Distribution Sample {data-transition="none"}

\includesvg{../slides/diagrams/gp/two_point_sample008.svg}

A 25 dimensional correlated random variable (values ploted against index)

### Prediction of $\mappingFunction_{2}$ from $\mappingFunction_{1}$ {data-transition="none"}

\includesvg{../slides/diagrams/gp/two_point_sample009.svg}

A 25 dimensional correlated random variable (values ploted against index)

### Prediction of $\mappingFunction_{2}$ from $\mappingFunction_{1}$ {data-transition="none"}

\includesvg{../slides/diagrams/gp/two_point_sample010.svg}

A 25 dimensional correlated random variable (values ploted against index)

### Prediction of $\mappingFunction_{2}$ from $\mappingFunction_{1}$ {data-transition="none"}

\includesvg{../slides/diagrams/gp/two_point_sample011.svg}

A 25 dimensional correlated random variable (values ploted against index)

### Prediction of $\mappingFunction_{2}$ from $\mappingFunction_{1}$ {data-transition="none"}

\includesvg{../slides/diagrams/gp/two_point_sample012.svg}

A 25 dimensional correlated random variable (values ploted against index)

}
