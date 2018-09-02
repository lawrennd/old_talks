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
\startslides{independent_height_weight}{0}{7}
\includesvg{../slides/diagrams/ml/independent_height_weight000.svg}{}{independent_height_weight}
\includesvg{../slides/diagrams/ml/independent_height_weight001.svg}{}{independent_height_weight}
\includesvg{../slides/diagrams/ml/independent_height_weight002.svg}{}{independent_height_weight}
\includesvg{../slides/diagrams/ml/independent_height_weight003.svg}{}{independent_height_weight}
\includesvg{../slides/diagrams/ml/independent_height_weight004.svg}{}{independent_height_weight}
\includesvg{../slides/diagrams/ml/independent_height_weight005.svg}{}{independent_height_weight}
\includesvg{../slides/diagrams/ml/independent_height_weight006.svg}{}{independent_height_weight}
\includesvg{../slides/diagrams/ml/independent_height_weight007.svg}{}{independent_height_weight}
}
\notesfigure{\includesvg{../slides/diagrams/ml/independent_height_weight007.svg}{}}\notes{\caption{Samples from independent Gaussian variables that might represent heights and weights.}}
