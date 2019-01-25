\ifndef{twoDGaussianIndependentSample}
\define{twoDGaussianIndependentSample}
\editme

\newslide{Sampling Two Dimensional Variables}

\setupplotcode{import teaching_plots as plot}
\plotcode{plot.independent_height_weight(num_samps=8, 
                               diagrams='../slides/diagrams/ml')}
							   
							
\setupdisplaycode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('independent_height_weight{fig:0>3}.svg', 
                            directory='../slides/diagrams/ml', 
							fig=IntSlider(0, 0, 7, 1))}

\slides{
\startanimation{independent_height_weight}{0}{7}
\newframe{\includediagram{../slides/diagrams/ml/independent_height_weight000}}{independent_height_weight}
\newframe{\includediagram{../slides/diagrams/ml/independent_height_weight001}}{independent_height_weight}
\newframe{\includediagram{../slides/diagrams/ml/independent_height_weight002}}{independent_height_weight}
\newframe{\includediagram{../slides/diagrams/ml/independent_height_weight003}}{independent_height_weight}
\newframe{\includediagram{../slides/diagrams/ml/independent_height_weight004}}{independent_height_weight}
\newframe{\includediagram{../slides/diagrams/ml/independent_height_weight005}}{independent_height_weight}
\newframe{\includediagram{../slides/diagrams/ml/independent_height_weight006}}{independent_height_weight}
\newframe{\includediagram{../slides/diagrams/ml/independent_height_weight007}}{independent_height_weight}
\endanimation
}
\notesfigure{\includediagram{../slides/diagrams/ml/independent_height_weight007}{}}\notes{\caption{Samples from independent Gaussian variables that might represent heights and weights.}}

\endif
