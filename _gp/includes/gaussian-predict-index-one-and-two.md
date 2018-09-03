\editme

\setupdisplaycode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('two_point_sample{sample:0>3}.svg', '../slides/diagrams/gp', sample=IntSlider(9, 9, 12, 1))}

\newslide{Prediction of $\mappingFunction_{2}$ from $\mappingFunction_{1}$}

\slides{
\startslides{two_point_sample2}{9}{12}
\includesvg{../slides/diagrams/gp/two_point_sample009.svg}{}{two_point_sample2}
\includesvg{../slides/diagrams/gp/two_point_sample010.svg}{}{two_point_sample2}
\includesvg{../slides/diagrams/gp/two_point_sample011.svg}{}{two_point_sample2}
\includesvg{../slides/diagrams/gp/two_point_sample012.svg}{}{two_point_sample2}
}

\notesfigure{\includesvg{../slides/diagrams/gp/two_point_sample012.svg}{}}
\notes{\caption{The joint Gaussian over $\mappingFunction_1$ and $\mappingFunction_2$ along with the conditional distribution of $\mappingFunction_2$ given $\mappingFunction_1$}}
