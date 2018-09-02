\loadcode{Kernel}{mlai}
\loadcode{polynomial_cov}{mlai}
\loadcode{exponentiated_quadratic}{mlai}

\setupplotcode{import teaching_plots as plot
from mlai import Kernel, exponentiated_quadratic}
\plotcode{kernel=Kernel(function=exponentiated_quadratic, lengthscale=0.5)
plot.two_point_sample(kernel.K, diagrams='../slides/diagrams/gp')}

\setupplotcode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('two_point_sample{sample:0>3}.svg', '../slides/diagrams/gp', sample=IntSlider(0, 0, 8, 1))}

							
\newslide{Gaussian Distribution Sample}
\slides{
\startslides{two_point_sample}{0}{8}
\includesvg{../slides/diagrams/gp/two_point_sample000.svg}{}{two_point_sample}
\includesvg{../slides/diagrams/gp/two_point_sample001.svg}{}{two_point_sample}
\includesvg{../slides/diagrams/gp/two_point_sample002.svg}{}{two_point_sample}
\includesvg{../slides/diagrams/gp/two_point_sample003.svg}{}{two_point_sample}
\includesvg{../slides/diagrams/gp/two_point_sample004.svg}{}{two_point_sample}
\includesvg{../slides/diagrams/gp/two_point_sample005.svg}{}{two_point_sample}
\includesvg{../slides/diagrams/gp/two_point_sample006.svg}{}{two_point_sample}
\includesvg{../slides/diagrams/gp/two_point_sample007.svg}{}{two_point_sample}
\includesvg{../slides/diagrams/gp/two_point_sample008.svg}{}{two_point_sample}
}
\notesfigure{\includesvg{../slides/diagrams/gp/two_point_sample008.svg}{}}
\caption{A 25 dimensional correlated random variable (values ploted against index)}

\setupplotcode{import pods
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
\caption{A 25 dimensional correlated random variable (values ploted against index)}
