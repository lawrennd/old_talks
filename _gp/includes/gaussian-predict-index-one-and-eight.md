\ifndef{gaussianPredictIndexOneAndEight}
\define{gaussianPredictIndexOneAndEight}
\editme

\setupdisplaycode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('two_point_sample{sample:0>3}.svg', '../slides/diagrams/gp', sample=IntSlider(13, 13, 17, 1))}
							
\notesfigure{\includediagram{../slides/diagrams/gp/two_point_sample013}}

\newslide{Prediction of $\mappingFunction_{8}$ from $\mappingFunction_{1}$}
\slides{
\startanimation{two_point_sample3}{13}{17}
\newframe{\includediagram{../slides/diagrams/gp/two_point_sample013}}{two_point_sample3}
\newframe{\includediagram{../slides/diagrams/gp/two_point_sample014}}{two_point_sample3}
\newframe{\includediagram{../slides/diagrams/gp/two_point_sample015}}{two_point_sample3}
\newframe{\includediagram{../slides/diagrams/gp/two_point_sample016}}{two_point_sample3}
\newframe{\includediagram{../slides/diagrams/gp/two_point_sample017}}{two_point_sample3}
\endanimation
}
\notes{\figure{\includediagram{../slides/diagrams/gp/two_point_sample017}{80%}}{The joint Gaussian over $\mappingFunction_1$ and $\mappingFunction_8$ along with the conditional distribution of $\mappingFunction_8$ given $\mappingFunction_1$}{two-point-sample-one-eight}
\endif
