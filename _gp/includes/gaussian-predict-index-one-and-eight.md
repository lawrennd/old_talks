\ifndef{gaussianPredictIndexOneAndEight}
\define{gaussianPredictIndexOneAndEight}
\editme

\subsubsection{Joint Density of $f_1$ and $f_8$}

\setupdisplaycode{import notutils as nu
from ipywidgets import IntSlider}
\setupdisplaycode{import notutils as nu}
\displaycode{nu.display_plots('two_point_sample{sample:0>3}.svg', 
                            '\writeDiagramsDir/gp', 
							sample=IntSlider(13, 13, 17, 1))}
							
\notes{\figure{\includediagram{\diagramsDir/gp/two_point_sample013}{80%}}{Sample from the joint Gaussian model, points indexed by 1 and 8 highlighted.}{two-point-sample-13}}

\subsubsection{Prediction of $\mappingFunction_{8}$ from $\mappingFunction_{1}$}

\slides{
\define{width}{80%}
\startanimation{two_point_sample3}{13}{17}
\newframe{\includediagram{\diagramsDir/gp/two_point_sample013}{\width}}{two_point_sample3}
\newframe{\includediagram{\diagramsDir/gp/two_point_sample014}{\width}}{two_point_sample3}
\newframe{\includediagram{\diagramsDir/gp/two_point_sample015}{\width}}{two_point_sample3}
\newframe{\includediagram{\diagramsDir/gp/two_point_sample016}{\width}}{two_point_sample3}
\newframe{\includediagram{\diagramsDir/gp/two_point_sample017}{\width}}{two_point_sample3}
\endanimation
}
\notes{\figure{\includediagram{\diagramsDir/gp/two_point_sample017}{80%}}{The joint Gaussian over $\mappingFunction_1$ and $\mappingFunction_8$ along with the conditional distribution of $\mappingFunction_8$ given $\mappingFunction_1$}{two-point-sample-one-eight}}

\endif
