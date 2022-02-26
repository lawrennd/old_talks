\ifndef{computingRbfCovariance}
\define{computingRbfCovariance}

\editme

\subsection{Where Did This Covariance Matrix Come From?}
$$
k(\inputVector, \inputVector^\prime) = \alpha \exp\left(-\frac{\left\Vert \inputVector - \inputVector^\prime\right\Vert^2_2}{2\lengthScale^2}\right)$$
\slides{
\columns{* Covariance matrix is built using the *inputs* to the function, $\inputVector$.

* For the example above it was based on Euclidean distance.

* The covariance function is also know as a kernel.
}{\includediagram{\diagramsDir/kern/eq_covariance}}{50%}{50%}
}

\newslide{Computing Covariance}

\setupplotcode{import numpy as np
from mlai import exponentiated_quadratic, Kernel
import mlai.plot}

\plotcode{formula = r"$k(x_i, x_j)=\alpha\exp\left(-\frac{\left|\left|x_i-x_j\right|\right|^{2}}{2\ell^{2}}\right)$"
kernel = Kernel(exponentiated_quadratic, lengthscale=2.0, variance=1.0)
plot.computing_covariance(kernel=kernel, x=np.asarray([[-3.],[1.2], [1.4]]), 
                          formula=formula,
						  stub='eq_three')}


\setupdisplaycode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('computing_eq_three_covariance{sample:0>3}.svg', 
                            directory='\writeDiagramsDir/kern', 
							sample=IntSlider(0, 0, 16, 1))}

\slides{
\define{width}{80%}
\startanimation{computing_eq_three_covariance}{0}{16}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_three_covariance000}{\width}}{computing_eq_three_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_three_covariance001}{\width}}{computing_eq_three_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_three_covariance002}{\width}}{computing_eq_three_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_three_covariance003}{\width}}{computing_eq_three_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_three_covariance004}{\width}}{computing_eq_three_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_three_covariance005}{\width}}{computing_eq_three_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_three_covariance006}{\width}}{computing_eq_three_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_three_covariance007}{\width}}{computing_eq_three_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_three_covariance008}{\width}}{computing_eq_three_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_three_covariance009}{\width}}{computing_eq_three_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_three_covariance010}{\width}}{computing_eq_three_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_three_covariance011}{\width}}{computing_eq_three_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_three_covariance012}{\width}}{computing_eq_three_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_three_covariance013}{\width}}{computing_eq_three_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_three_covariance014}{\width}}{computing_eq_three_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_three_covariance015}{\width}}{computing_eq_three_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_three_covariance016}{\width}}{computing_eq_three_covariance}
\endanimation
}

\notes{\figure{\includediagram{\diagramsDir/kern/computing_eq_three_covariance016}{80%}}{Entrywise fill in of the covariance matrix from the covariance function.}{computing-eq-three-covariance2}}


\newslide{Computing Covariance}

\setupplotcode{import numpy as np
from mlai import exponentiated_quadratic, Kernel
import mlai.plot}

\plotcode{formula = r"$k(x_i, x_j)=\alpha\exp\left(-\frac{\left|\left|x_i-x_j\right|\right|^{2}}{2\ell^{2}}\right)$"
kernel = Kernel(exponentiated_quadratic, lengthscale=2.0, variance=1.0)
plot.computing_covariance(kernel=kernel, x=np.asarray([[-3.],[1.2], [1.4], [2.0]]), 
                          formula=formula,
						  stub='eq_four')}


\setupdisplaycode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('computing_eq_four_covariance{sample:0>3}.svg', 
                            directory='\writeDiagramsDir/kern', 
							sample=IntSlider(0, 0, 27, 1))}

\slides{
\define{width}{80%}
\startanimation{computing_eq_four_covariance}{0}{27}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_four_covariance000}{\width}}{computing_eq_four_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_four_covariance001}{\width}}{computing_eq_four_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_four_covariance002}{\width}}{computing_eq_four_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_four_covariance003}{\width}}{computing_eq_four_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_four_covariance004}{\width}}{computing_eq_four_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_four_covariance005}{\width}}{computing_eq_four_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_four_covariance006}{\width}}{computing_eq_four_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_four_covariance007}{\width}}{computing_eq_four_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_four_covariance008}{\width}}{computing_eq_four_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_four_covariance009}{\width}}{computing_eq_four_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_four_covariance010}{\width}}{computing_eq_four_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_four_covariance011}{\width}}{computing_eq_four_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_four_covariance012}{\width}}{computing_eq_four_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_four_covariance013}{\width}}{computing_eq_four_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_four_covariance014}{\width}}{computing_eq_four_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_four_covariance015}{\width}}{computing_eq_four_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_four_covariance016}{\width}}{computing_eq_four_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_four_covariance017}{\width}}{computing_eq_four_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_four_covariance018}{\width}}{computing_eq_four_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_four_covariance019}{\width}}{computing_eq_four_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_four_covariance020}{\width}}{computing_eq_four_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_four_covariance021}{\width}}{computing_eq_four_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_four_covariance022}{\width}}{computing_eq_four_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_four_covariance023}{\width}}{computing_eq_four_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_four_covariance024}{\width}}{computing_eq_four_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_four_covariance025}{\width}}{computing_eq_four_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_four_covariance026}{\width}}{computing_eq_four_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_four_covariance027}{\width}}{computing_eq_four_covariance}
\endanimation
}

\figure{\includediagram{\diagramsDir/kern/computing_eq_four_covariance027}{80%}}{Entrywise fill in of the covariance matrix from the covariance function.}{computing-eq-four-covariance2}

\newslide{Computing Covariance}

\setupplotcode{import numpy as np
from mlai import exponentiated_quadratic, Kernel
import mlai.plot}

\plotcode{formula = r"$k(x_i, x_j)=\alpha\exp\left(-\frac{\left|\left|x_i-x_j\right|\right|^{2}}{2\ell^{2}}\right)$"
kernel = Kernel(exponentiated_quadratic, lengthscale=5.0, variance=2.0)
plot.computing_covariance(kernel=kernel, x=np.asarray([[-3.],[1.2], [1.4]]), 
                          formula=formula,
						  stub='eq_three_2')}


\setupdisplaycode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('computing_eq_three_2_covariance{sample:0>3}.svg', 
                            directory='\writeDiagramsDir/kern', 
							sample=IntSlider(0, 0, 16, 1))}

\slides{
\define{width}{80%}
\startanimation{computing_eq_three_2_covariance}{0}{16}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_three_2_covariance000}{\width}}{computing_eq_three_2_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_three_2_covariance001}{\width}}{computing_eq_three_2_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_three_2_covariance002}{\width}}{computing_eq_three_2_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_three_2_covariance003}{\width}}{computing_eq_three_2_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_three_2_covariance004}{\width}}{computing_eq_three_2_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_three_2_covariance005}{\width}}{computing_eq_three_2_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_three_2_covariance006}{\width}}{computing_eq_three_2_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_three_2_covariance007}{\width}}{computing_eq_three_2_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_three_2_covariance008}{\width}}{computing_eq_three_2_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_three_2_covariance009}{\width}}{computing_eq_three_2_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_three_2_covariance010}{\width}}{computing_eq_three_2_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_three_2_covariance011}{\width}}{computing_eq_three_2_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_three_2_covariance012}{\width}}{computing_eq_three_2_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_three_2_covariance013}{\width}}{computing_eq_three_2_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_three_2_covariance014}{\width}}{computing_eq_three_2_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_three_2_covariance015}{\width}}{computing_eq_three_2_covariance}
\newframe{\includediagram{\diagramsDir/kern/computing_eq_three_2_covariance016}{\width}}{computing_eq_three_2_covariance}
\endanimation
}

\figure{\includediagram{\diagramsDir/kern/computing_eq_three_2_covariance016}{80%}}{Entrywise fill in of the covariance matrix from the covariance function.}{computing-eq-three-2-covariance2}

\endif
