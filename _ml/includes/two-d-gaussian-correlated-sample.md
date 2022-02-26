\ifndef{twoDGaussianCorrelatedSample}
\define{twoDGaussianCorrelatedSample}
\editme

\subsection{Sampling Two Dimensional Variables}

\setupplotcode{import mlai.plot}
\plotcode{plot.correlated_height_weight(num_samps=8, 
                              diagrams='\writeDiagramsDir/ml')}

\setupdisplaycode{import pods
from ipywidgets import IntSlider}
\displaycode{
pods.notebook.display_plots('correlated_height_weight{fig:0>3}.svg', 
                            directory='\writeDiagramsDir/ml', 
							fig=IntSlider(0, 0, 7, 1))}


\slides{
\define{weight}{70%}
\startanimation{correlated_height_weight}{0}{7}
\newframe{\includediagram{\diagramsDir/ml/correlated_height_weight000}{\width}}{correlated_height_weight}
\newframe{\includediagram{\diagramsDir/ml/correlated_height_weight001}{\width}}{correlated_height_weight}
\newframe{\includediagram{\diagramsDir/ml/correlated_height_weight002}{\width}}{correlated_height_weight}
\newframe{\includediagram{\diagramsDir/ml/correlated_height_weight003}{\width}}{correlated_height_weight}
\newframe{\includediagram{\diagramsDir/ml/correlated_height_weight004}{\width}}{correlated_height_weight}
\newframe{\includediagram{\diagramsDir/ml/correlated_height_weight005}{\width}}{correlated_height_weight}
\newframe{\includediagram{\diagramsDir/ml/correlated_height_weight006}{\width}}{correlated_height_weight}
\newframe{\includediagram{\diagramsDir/ml/correlated_height_weight007}{\width}}{correlated_height_weight}
\endanimation
}

\notes{\figure{\includediagram{\diagramsDir/ml/correlated_height_weight007}{70%}}{Samples from *correlated* Gaussian variables that might represent heights and weights.}{correlated-height-weight-7}}

\endif
