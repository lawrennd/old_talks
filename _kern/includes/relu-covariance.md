\helpercode{%load -s relu_cov mlai.py}
\setupcode{import teaching_plots as plot
import mlai
import numpy as np}
\code{K, anim=plot.animate_covariance_function(mlai.compute_kernel, 
                                         kernel=relu_cov, lengthscale=0.2)}

\setupcode{from IPython.core.display import HTML}

\displaycode{HTML(anim.to_jshtml())}

\plotcode{plot.save_animation(anim, 
                    diagrams='../slides/diagrams/kern', 
				    filename='relu_covariance.html')}


### RELU Covariance

$$\kernelScalar(\inputVector, \inputVector^\prime) = 
\alpha \arcsin\left(\frac{w \inputVector^\top \inputVector^\prime + b}
{\sqrt{\left(w \inputVector^\top \inputVector + b + 1\right)
\left(w \left.\inputVector^\prime\right.^\top \inputVector^\prime + b + 1\right)}}\right)$$

\columns{
\includesvg{../slides/diagrams/kern/relu_covariance.svg}
}{
\includehtml{../slides/diagrams/kern/relu_covariance.html}{512}{384}
}{50%}{50%}

