\editme

\setupplotcode{import numpy as np
np.random.seed(4949)}

\subsection{Sampling a Function}
\slides{
**Multi-variate Gaussians**

* We will consider a Gaussian with a particular structure of covariance matrix.
* Generate a single sample from this 25 dimensional Gaussian density,}\notes{We will consider a Gaussian distribution with a particular structure of covariance matrix. We will generate *one* sample from a 25-dimensional Gaussian density.} 
$$
\mappingFunctionVector=\left[\mappingFunction_{1},\mappingFunction_{2}\dots \mappingFunction_{25}\right].
$$
\slides{* We will plot these points against their index.}\notes{in the figure below we plot these data on the $y$-axis against their *indices* on the $x$-axis.}

\loadcode{Kernel}{mlai}
\loadcode{polynomial_cov}{mlai}
\loadcode{exponentiated_quadratic}{mlai}

\setupplotcode{import teaching_plots as plot
from mlai import Kernel, exponentiated_quadratic}
\plotcode{kernel=Kernel(function=exponentiated_quadratic, lengthscale=0.5)
plot.two_point_sample(kernel.K, diagrams='../slides/diagrams/gp')}

\setupdisplaycode{import pods
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
\notes{\caption{A 25 dimensional correlated random variable (values ploted against index)}}

\include{_gp/includes/gaussian-predict-index-one-and-two.md}

\subsection{Uluru}

\includeimg{../slides/diagrams/gp/799px-Uluru_Panorama.jpg}{}{}{center}
\notes{When viewing these contour plots, I sometimes find it helpful to think of Uluru, the prominent rock formation in Australia. The rock rises above the surface of the plane, just like a probability density rising above the zero line. The rock is three dimensional, but when we view Uluru from the classical position, we are looking at one side of it. This is equivalent to viewing the marginal density. 

The joint density can be viewed from above, using contours. The conditional density is equivalent to *slicing* the rock. Uluru is a holy rock, so this has to be an imaginary slice. Imagine we cut down a vertical plane orthogonal to our view point (e.g. coming across our view point). This would give a profile of the rock, which when renormalized, would give us the conditional distribution, the value of conditioning would be the location of the slice in the direction we are facing.}

\subsection{Prediction with Correlated Gaussians}
\slides{
* Prediction of $\mappingFunction_2$ from $\mappingFunction_1$ requires *conditional density*.}\notes{Of course in practice, rather than manipulating mountains physically, the advantage of the Gaussian density is that we can perform these manipulations mathematically. 

Prediction of $\mappingFunction_2$ given $\mappingFunction_1$ requires the *conditional density*, $p(\mappingFunction_2|\mappingFunction_1)$.}\slides{
* Conditional density is *also* Gaussian.}\notes{Another remarkable property of the Gaussian density is that this conditional distribution is *also* guaranteed to be a Gaussian density. It has the form,}
    $$
    p(\mappingFunction_2|\mappingFunction_1) = \gaussianDist{\mappingFunction_2}{\frac{\kernelScalar_{1, 2}}{\kernelScalar_{1, 1}}\mappingFunction_1}{ \kernelScalar_{2, 2} - \frac{\kernelScalar_{1,2}^2}{\kernelScalar_{1,1}}}
    $$\slides{
    where covariance of joint density is given by}\notes{where we have assumed that the covariance of the original joint density was given by}
    $$
    \kernelMatrix = \begin{bmatrix} \kernelScalar_{1, 1} & \kernelScalar_{1, 2}\\ \kernelScalar_{2, 1} & \kernelScalar_{2, 2}.\end{bmatrix}
    $$

\notes{Using these formulae we can determine the conditional density for any of the elements of our vector $\mappingFunctionVector$. For example, the variable $\mappingFunction_8$ is less correlated with $\mappingFunction_1$ than $\mappingFunction_2$. If we consider this variable we see the conditional density is more diffuse.}

\include{_gp/includes/gaussian-predict-index-one-and-eight.md}
