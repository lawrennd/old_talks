\subsection{MLP Covariance}

\loadcode{mlp_cov}{mlai}

\setupplotcode{import teaching_plots as plot
import mlai
import numpy as np}

\plotcode{kernel = mlai.Kernel(function=mlp_cov,
                     name='Multilayer Perceptron',
                     shortname='mlp',					 
                     formula='\kernelScalar(\inputVector, \inputVector^\prime) = \alpha \arcsin\left(\frac{w \inputVector^\top \inputVector^\prime + b}{\sqrt{\left(w \inputVector^\top \inputVector + b + 1\right)\left(w \left.\inputVector^\prime\right.^\top \inputVector^\prime + b + 1\right)}}\right)',
					 w=1, b=0.5)
					 
plot.covariance_func(kernel, diagrams='../slides/diagrams/')}


\notes{The multi-layer perceptron (MLP) covariance, also known as the neural network covariance or the arcsin covariance, is derived by considering the infinite limit of a neural network.} 
$$
\kernelScalar(\inputVector, \inputVector^\prime) = \alpha \arcsin\left(\frac{w \inputVector^\top \inputVector^\prime + b}{\sqrt{\left(w \inputVector^\top \inputVector + b + 1\right)\left(w \left.\inputVector^\prime\right.^\top \inputVector^\prime + b + 1\right)}}\right)
$$

<!--\columns{
\includesvg{../slides/diagrams/kern/mlp_covariance.svg}
}{
\includehtml{../slides/diagrams/kern/mlp_covariance.html}{512}{384}
}{50%}{50%}
\notes{\caption{The multi-layer perceptron covariance function. This is derived by considering the infinite limit of a neural network with probit activation functions.}}-->

\columns{\includesvgclass{../slides/diagrams/kern/mlp_covariance.svg}}{\includeimg{../slides/diagrams/kern/mlp_covariance.gif}{100%}{negate}{center}}{45%}{45%}
