\ifndef{twoDGaussianIndependentSample}
\define{twoDGaussianIndependentSample}
\editme

\newslide{Sampling Two Dimensional Variables}

\setupplotcode{import mlai.plot}
\plotcode{plot.independent_height_weight(num_samps=8, 
                               diagrams='\writeDiagramsDir/ml')}
							   
							
\setupdisplaycode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('independent_height_weight{fig:0>3}.svg', 
                            directory='\writeDiagramsDir/ml', 
							fig=IntSlider(0, 0, 7, 1))}

\slides{
\define{width}{70%}
\startanimation{independent_height_weight}{0}{7}
\newframe{\includediagram{\diagramsDir/ml/independent_height_weight000}{\width}}{independent_height_weight}
\newframe{\includediagram{\diagramsDir/ml/independent_height_weight001}{\width}}{independent_height_weight}
\newframe{\includediagram{\diagramsDir/ml/independent_height_weight002}{\width}}{independent_height_weight}
\newframe{\includediagram{\diagramsDir/ml/independent_height_weight003}{\width}}{independent_height_weight}
\newframe{\includediagram{\diagramsDir/ml/independent_height_weight004}{\width}}{independent_height_weight}
\newframe{\includediagram{\diagramsDir/ml/independent_height_weight005}{\width}}{independent_height_weight}
\newframe{\includediagram{\diagramsDir/ml/independent_height_weight006}{\width}}{independent_height_weight}
\newframe{\includediagram{\diagramsDir/ml/independent_height_weight007}{\width}}{independent_height_weight}
\endanimation
}
\notes{\figure{\includediagram{\diagramsDir/ml/independent_height_weight007}{70%}}{Samples from independent Gaussian variables that might represent heights and weights.}{independent-height-weight-7}}

\endif
