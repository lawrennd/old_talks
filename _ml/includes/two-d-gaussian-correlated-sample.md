\ifndef{twoDGaussianCorrelatedSample}
\define{twoDGaussianCorrelatedSample}
\editme
\subsection{Sampling Two Dimensional Variables}

\plotcode{import teaching_plots as plot}
\plotcode{plot.correlated_height_weight(num_samps=8, 
                              diagrams='../slides/diagrams/ml')}

\setupdisplaycode{import pods
from ipywidgets import IntSlider}
\displaycode{
pods.notebook.display_plots('correlated_height_weight{fig:0>3}.svg', 
                            directory='../slides/diagrams/ml', 
							fig=IntSlider(0, 0, 7, 1))}


\slides{
\startanimation{correlated_height_weight}{0}{7}
\newframe{\includediagram{../slides/diagrams/ml/correlated_height_weight000}}{correlated_height_weight}
\newframe{\includediagram{../slides/diagrams/ml/correlated_height_weight001}}{correlated_height_weight}
\newframe{\includediagram{../slides/diagrams/ml/correlated_height_weight002}}{correlated_height_weight}
\newframe{\includediagram{../slides/diagrams/ml/correlated_height_weight003}}{correlated_height_weight}
\newframe{\includediagram{../slides/diagrams/ml/correlated_height_weight004}}{correlated_height_weight}
\newframe{\includediagram{../slides/diagrams/ml/correlated_height_weight005}}{correlated_height_weight}
\newframe{\includediagram{../slides/diagrams/ml/correlated_height_weight006}}{correlated_height_weight}
\newframe{\includediagram{../slides/diagrams/ml/correlated_height_weight007}}{correlated_height_weight}
\endanimation
}
\notesfigure{\includediagram{../slides/diagrams/ml/correlated_height_weight007}{}}\notes{\caption{Samples from *correlated* Gaussian variables that might represent heights and weights.}}
\endif
