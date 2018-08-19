### Brownian Covariance

\loadcode{%load -s brownian_cov mlai.py}

\setupcode{import teaching_plots as plot
import mlai
import numpy as np}
\code{t=np.linspace(0, 2, 200)[:, np.newaxis]
K, anim=plot.animate_covariance_function(mlai.compute_kernel, 
                                         t, 
                                         kernel=brownian_cov)}

\setupcode{from IPython.core.display import HTML}

\displaycode{HTML(anim.to_jshtml())}

\plotcode{plot.save_animation(anim, 
                    diagrams='../slides/diagrams/kern', 
				    filename='brownian_covariance.html')}

\notes{Brownian motion is also a Gaussian process. It follows a Gaussian random walk, with diffusion occuring at each time point driven by a Gaussian input. This implies it is both Markov and Gaussian. The covariane function for Brownian motion has the form}
$$
\kernelScalar(t, t^\prime) = \alpha \min(t, t^\prime)
$$
\columns{
\includesvg{../slides/diagrams/kern/brownian_covariance.svg}
}{
\includehtml{../slides/diagrams/kern/brownian_covariance.html}{512}{384}
}{50%}{50%}
\notes{\caption{The covariance of Brownian motion, and some samples from the covariance showing the functional form.}}
