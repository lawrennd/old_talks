\setupcode{import numpy as np
import teaching_plots as plot}

\code{%load -s compute_kernel mlai.py}

\code{%load -s eq_cov mlai.py}

\plotcode{np.random.seed(10)
plot.rejection_samples(compute_kernel, kernel=eq_cov, 
                       lengthscale=0.25, diagrams='../slides/diagrams/gp')}

\displaycode{import pods
pods.notebook.display_plots('gp_rejection_samples{sample:0>3}.svg', 
                            '../slides/diagrams/gp', sample=(1,5))}
\slides{
###  {data-transition="none"}

\includesvg{../slides/diagrams/gp/gp_rejection_sample001.svg}

###  {data-transition="none"}

\includesvg{../slides/diagrams/gp/gp_rejection_sample002.svg}

###  {data-transition="none"}

\includesvg{../slides/diagrams/gp/gp_rejection_sample003.svg}

###  {data-transition="none"}

\includesvg{../slides/diagrams/gp/gp_rejection_sample004.svg}

###  {data-transition="none"}

\includesvg{../slides/diagrams/gp/gp-rejection-sample005.svg}
}

