\setupplotcode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('two_point_sample{sample:0>3}.svg', '../slides/diagrams/gp', sample=IntSlider(13, 13, 17, 1))}
							
\notesfigure{\includesvg{../slides/diagrams/gp/two_point_sample013.svg}}

\newslide{Prediction of $\mappingFunction_{8}$ from $\mappingFunction_{1}$}
\slides{
\startslides{two_point_sample3}{13}{17}

\includesvg{../slides/diagrams/gp/two_point_sample013.svg}{}{two_point_sample3}
\includesvg{../slides/diagrams/gp/two_point_sample014.svg}{}{two_point_sample3}
\includesvg{../slides/diagrams/gp/two_point_sample015.svg}{}{two_point_sample3}
\includesvg{../slides/diagrams/gp/two_point_sample016.svg}{}{two_point_sample3}
\includesvg{../slides/diagrams/gp/two_point_sample017.svg}{}{two_point_sample3}
}
\notesfigure{\includesvg{../slides/diagrams/gp/two_point_sample017.svg}}
\caption{A 25 dimensional correlated random variable (values ploted against index)}



