\ifndef{gaussianPredictIndexOneAndTwo}
\define{gaussianPredictIndexOneAndTwo}
\editme

\subsubsection{Sampling a Function from a Gaussian}

\setupdisplaycode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('two_point_sample{sample:0>3}.svg', 
                            '\writeDiagramsDir/gp', 
							sample=IntSlider(0, 0, 8, 1))}

\slides{
\define{width}{80%}
\startanimation{two-point-sample}{9}{12}
\newframe{\includediagram{\diagramsDir/gp/two_point_sample000}{\width}}{two-point-sample}
\newframe{\includediagram{\diagramsDir/gp/two_point_sample001}{\width}}{two-point-sample}
\newframe{\includediagram{\diagramsDir/gp/two_point_sample002}{\width}}{two-point-sample}
\newframe{\includediagram{\diagramsDir/gp/two_point_sample003}{\width}}{two-point-sample}
\newframe{\includediagram{\diagramsDir/gp/two_point_sample004}{\width}}{two-point-sample}
\newframe{\includediagram{\diagramsDir/gp/two_point_sample005}{\width}}{two-point-sample}
\newframe{\includediagram{\diagramsDir/gp/two_point_sample006}{\width}}{two-point-sample}
\newframe{\includediagram{\diagramsDir/gp/two_point_sample007}{\width}}{two-point-sample}
\newframe{\includediagram{\diagramsDir/gp/two_point_sample008}{\width}}{two-point-sample}
\endanimation
}

\notes{\figure{\includediagram{\diagramsDir/gp/two_point_sample001}{80%}}{The joint Gaussian over $\mappingFunction_1$ and $\mappingFunction_2$ along with the conditional distribution of $\mappingFunction_2$ given $\mappingFunction_1$}{two-point-sample-one-two}}


\subsubsection{Joint Density of $f_1$ and $f_2$}

\setupdisplaycode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('two_point_sample{sample:0>3}.svg', 
                            '\writeDiagramsDir/gp', 
							sample=IntSlider(9, 9, 12, 1))}

\newslide{Prediction of $\mappingFunction_{2}$ from $\mappingFunction_{1}$}

\slides{
\define{width}{80%}
\startanimation{two_point_sample2}{9}{12}
\newframe{\includediagram{\diagramsDir/gp/two_point_sample009}{\width}}{two_point_sample2}
\newframe{\includediagram{\diagramsDir/gp/two_point_sample010}{\width}}{two_point_sample2}
\newframe{\includediagram{\diagramsDir/gp/two_point_sample011}{\width}}{two_point_sample2}
\newframe{\includediagram{\diagramsDir/gp/two_point_sample012}{\width}}{two_point_sample2}
\endanimation
}

\notes{\figure{\includediagram{\diagramsDir/gp/two_point_sample012}{80%}}{The joint Gaussian over $\mappingFunction_1$ and $\mappingFunction_2$ along with the conditional distribution of $\mappingFunction_2$ given $\mappingFunction_1$}{two-point-sample-one-two}}

\endif
