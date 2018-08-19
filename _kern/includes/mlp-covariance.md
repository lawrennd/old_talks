### MLP Covariance

\loadcode{%load -s mlp_cov mlai.py}

\setupcode{import teaching_plots as plot
import mlai
import numpy as np}

\plotcode{K, anim=plot.animate_covariance_function(mlai.compute_kernel, 
                                         kernel=mlp_cov, lengthscale=0.2)}

\setupcode{from IPython.core.display import HTML}

\displaycode{HTML(anim.to_jshtml())}

\plotcode{plot.save_animation(anim, 
                    diagrams='../slides/diagrams/kern', 
				    filename='mlp_covariance.html')}
\notes{The multi-layer perceptron (MLP) covariance, also known as the neural network covariance or the arcsin covariance, is derived by considering the infinite limit of a neural network.} 
$$
\kernelScalar(\inputVector, \inputVector^\prime) = \alpha \arcsin\left(\frac{w \inputVector^\top \inputVector^\prime + b}{\sqrt{\left(w \inputVector^\top \inputVector + b + 1\right)\left(w \left.\inputVector^\prime\right.^\top \inputVector^\prime + b + 1\right)}}\right)
$$

\columns{
\includesvg{../slides/diagrams/kern/mlp_covariance.svg}
}{
\includehtml{../slides/diagrams/kern/mlp_covariance.html}{512}{384}
}{50%}{50%}
\notes{\caption{The multi-layer perceptron covariance function. This is derived by considering the infinite limit of a neural network with probit activation functions.}}
