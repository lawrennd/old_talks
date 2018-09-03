\editme

\subsection{Where Did This Covariance Matrix Come From?}
$$
k(\inputVector, \inputVector^\prime) = \alpha \exp\left(-\frac{\left\Vert \inputVector - \inputVector^\prime\right\Vert^2_2}{2\lengthScale^2}\right)$$
\slides{
\columns{* Covariance matrix is built using the *inputs* to the function, $\inputVector$.

* For the example above it was based on Euclidean distance.

* The covariance function is also know as a kernel.
}{\includesvg{../slides/diagrams/kern/eq_covariance.svg}}{50%}{50%}
}

\newslide{Computing Covariance}

\setupplotcode{import numpy as np
from mlai import exponentiated_quadratic, Kernel
import teaching_plots as plot}

\plotcode{formula = r"$k(x_i, x_j)=\alpha\exp\left(-\frac{\left|\left|x_i-x_j\right|\right|^{2}}{2\ell^{2}}\right)$"
kernel = Kernel(exponentiated_quadratic, lengthscale=2.0, variance=1.0)
plot.computing_covariance(kernel=kernel, x=np.asarray([[-3.],[1.2], [1.4]]), 
                          formula=formula,
						  stub='eq_three')}


\setupdisplaycode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('computing_eq_three_covariance{sample:0>3}.svg', 
                            directory='../slides/diagrams/kern', 
							sample=IntSlider(0, 0, 16, 1))}

\slides{
\startslides{computing_eq_three_covariance}{0}{16}
\includesvg{../slides/diagrams/kern/computing_eq_three_covariance000.svg}{}{computing_eq_three_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_three_covariance001.svg}{}{computing_eq_three_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_three_covariance002.svg}{}{computing_eq_three_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_three_covariance003.svg}{}{computing_eq_three_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_three_covariance004.svg}{}{computing_eq_three_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_three_covariance005.svg}{}{computing_eq_three_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_three_covariance006.svg}{}{computing_eq_three_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_three_covariance007.svg}{}{computing_eq_three_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_three_covariance008.svg}{}{computing_eq_three_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_three_covariance009.svg}{}{computing_eq_three_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_three_covariance010.svg}{}{computing_eq_three_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_three_covariance011.svg}{}{computing_eq_three_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_three_covariance012.svg}{}{computing_eq_three_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_three_covariance013.svg}{}{computing_eq_three_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_three_covariance014.svg}{}{computing_eq_three_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_three_covariance015.svg}{}{computing_eq_three_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_three_covariance016.svg}{}{computing_eq_three_covariance}
}

\notesfigure{\includesvg{../slides/diagrams/kern/computing_eq_three_covariance016.svg}{}
\includesvg{../slides/diagrams/kern/computing_eq_three_covariance016.svg}{}}\notes{\caption{Entrywise fill in of the covariance matrix from the covariance function.}}


\newslide{Computing Covariance}

\setupplotcode{import numpy as np
from mlai import exponentiated_quadratic, Kernel
import teaching_plots as plot}

\plotcode{formula = r"$k(x_i, x_j)=\alpha\exp\left(-\frac{\left|\left|x_i-x_j\right|\right|^{2}}{2\ell^{2}}\right)$"
kernel = Kernel(exponentiated_quadratic, lengthscale=2.0, variance=1.0)
plot.computing_covariance(kernel=kernel, x=np.asarray([[-3.],[1.2], [1.4], [2.0]]), 
                          formula=formula,
						  stub='eq_four')}


\setupdisplaycode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('computing_eq_four_covariance{sample:0>3}.svg', 
                            directory='../slides/diagrams/kern', 
							sample=IntSlider(0, 0, 27, 1))}

\slides{
\startslides{computing_eq_four_covariance}{0}{27}
\includesvg{../slides/diagrams/kern/computing_eq_four_covariance000.svg}{}{computing_eq_four_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_four_covariance001.svg}{}{computing_eq_four_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_four_covariance002.svg}{}{computing_eq_four_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_four_covariance003.svg}{}{computing_eq_four_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_four_covariance004.svg}{}{computing_eq_four_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_four_covariance005.svg}{}{computing_eq_four_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_four_covariance006.svg}{}{computing_eq_four_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_four_covariance007.svg}{}{computing_eq_four_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_four_covariance008.svg}{}{computing_eq_four_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_four_covariance009.svg}{}{computing_eq_four_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_four_covariance010.svg}{}{computing_eq_four_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_four_covariance011.svg}{}{computing_eq_four_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_four_covariance012.svg}{}{computing_eq_four_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_four_covariance013.svg}{}{computing_eq_four_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_four_covariance014.svg}{}{computing_eq_four_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_four_covariance015.svg}{}{computing_eq_four_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_four_covariance016.svg}{}{computing_eq_four_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_four_covariance017.svg}{}{computing_eq_four_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_four_covariance018.svg}{}{computing_eq_four_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_four_covariance019.svg}{}{computing_eq_four_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_four_covariance020.svg}{}{computing_eq_four_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_four_covariance021.svg}{}{computing_eq_four_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_four_covariance022.svg}{}{computing_eq_four_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_four_covariance023.svg}{}{computing_eq_four_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_four_covariance024.svg}{}{computing_eq_four_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_four_covariance025.svg}{}{computing_eq_four_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_four_covariance026.svg}{}{computing_eq_four_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_four_covariance027.svg}{}{computing_eq_four_covariance}
}

\notesfigure{\includesvg{../slides/diagrams/kern/computing_eq_four_covariance027.svg}{}
\includesvg{../slides/diagrams/kern/computing_eq_four_covariance027.svg}{}}\notes{\caption{Entrywise fill in of the covariance matrix from the covariance function.}}

\newslide{Computing Covariance}

\setupplotcode{import numpy as np
from mlai import exponentiated_quadratic, Kernel
import teaching_plots as plot}

\plotcode{formula = r"$k(x_i, x_j)=\alpha\exp\left(-\frac{\left|\left|x_i-x_j\right|\right|^{2}}{2\ell^{2}}\right)$"
kernel = Kernel(exponentiated_quadratic, lengthscale=5.0, variance=2.0)
plot.computing_covariance(kernel=kernel, x=np.asarray([[-3.],[1.2], [1.4]]), 
                          formula=formula,
						  stub='eq_three_2')}


\setupdisplaycode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('computing_eq_three_2_covariance{sample:0>3}.svg', 
                            directory='../slides/diagrams/kern', 
							sample=IntSlider(0, 0, 16, 1))}

\slides{
\startslides{computing_eq_three_2_covariance}{0}{16}
\includesvg{../slides/diagrams/kern/computing_eq_three_2_covariance000.svg}{}{computing_eq_three_2_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_three_2_covariance001.svg}{}{computing_eq_three_2_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_three_2_covariance002.svg}{}{computing_eq_three_2_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_three_2_covariance003.svg}{}{computing_eq_three_2_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_three_2_covariance004.svg}{}{computing_eq_three_2_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_three_2_covariance005.svg}{}{computing_eq_three_2_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_three_2_covariance006.svg}{}{computing_eq_three_2_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_three_2_covariance007.svg}{}{computing_eq_three_2_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_three_2_covariance008.svg}{}{computing_eq_three_2_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_three_2_covariance009.svg}{}{computing_eq_three_2_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_three_2_covariance010.svg}{}{computing_eq_three_2_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_three_2_covariance011.svg}{}{computing_eq_three_2_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_three_2_covariance012.svg}{}{computing_eq_three_2_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_three_2_covariance013.svg}{}{computing_eq_three_2_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_three_2_covariance014.svg}{}{computing_eq_three_2_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_three_2_covariance015.svg}{}{computing_eq_three_2_covariance}
\includesvg{../slides/diagrams/kern/computing_eq_three_2_covariance016.svg}{}{computing_eq_three_2_covariance}
}

\notesfigure{\includesvg{../slides/diagrams/kern/computing_eq_three_2_covariance016.svg}{}
\includesvg{../slides/diagrams/kern/computing_eq_three_2_covariance016.svg}{}}\notes{\caption{Entrywise fill in of the covariance matrix from the covariance function.}}
