\subsection{Brownian Covariance}

\loadcode{brownian_cov}{mlai}

\setupplotcode{import teaching_plots as plot
import mlai
import matplotlib.pyplot as plt
import numpy as np
import os}
\plotcode{t=np.linspace(0, 2, 200)[:, np.newaxis]
kernel = mlai.Kernel(function=mlai.brownian_cov)
K, anim=plot.animate_covariance_function(kernel.K, t)}

\plotcode{fig, ax = plt.subplots(figsize=plot.one_figsize)
t=np.linspace(0, 1, 20)[:, np.newaxis]
plot.matrix(kernel.K(t), ax=ax, type='image', bracket_style='boxes', colormap='gray')
plot.clear_axes(ax)
ax.set_xlabel('$t$')
ax.set_ylabel('$t^\prime$')
mlai.write_figure(os.path.join('../slides/diagrams/kern', 'brownian_covariance.svg'), 
                  transparent=True)
}

\setupplotcode{from IPython.core.display import HTML}

\displaycode{HTML(anim.to_jshtml())}

\plotcode{plot.save_animation(anim, 
                    diagrams='../slides/diagrams/kern', 
				    filename='brownian_covariance.html')}

\notes{Brownian motion is also a Gaussian process. It follows a Gaussian random walk, with diffusion occuring at each time point driven by a Gaussian input. This implies it is both Markov and Gaussian. The covariane function for Brownian motion has the form}
$$
\kernelScalar(t, t^\prime) = \alpha \min(t, t^\prime)
$$

<!--\columns{
\includesvg{../slides/diagrams/kern/brownian_covariance.svg}
}{
\includehtml{../slides/diagrams/kern/brownian_covariance.html}{512}{384}
}{50%}{50%}
\notes{\caption{The covariance of Brownian motion, and some samples from the covariance showing the functional form.}}-->
\columns{\includesvgclass{../slides/diagrams/kern/brownian_covariance.svg}}{\includeimg{../slides/diagrams/kern/brownian_covariance.gif}{100%}{negate}{center}}{45%}{45%}

