\subsection{Brownian Covariance}

\loadcode{brownian_cov}{mlai}

\setupplotcode{import teaching_plots as plot
import mlai
import numpy as np}

\plotcode{t=np.linspace(0, 2, 200)[:, np.newaxis]
kernel = mlai.Kernel(function=brownian_cov,
                     name='Brownian',
                     formula='\kernelScalar(t, t^\prime)=\alpha \min(t, t^\prime)',
                     shortname='brownian')
plot.covariance_func(kernel, t, diagrams='../slides/diagrams/kern/')}

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

