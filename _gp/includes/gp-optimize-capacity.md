\ifndef{gpOptimizeCapacity}
\define{gpOptimizeCapacity}

\editme

\subsection{Capacity Control through the Determinant}

The parameters are *inside* the covariance function (matrix).
\normalsize
$$\kernelScalar_{i, j} = \kernelScalar(\inputVals_i, \inputVals_j; \parameterVector)$$


\newslide{Eigendecomposition of Covariance}

[\Large
$$\kernelMatrix = \rotationMatrix \eigenvalueMatrix^2 \rotationMatrix^\top$$]{}


\columns{\includepng{\diagramsDir/gp/gp-optimize-eigen}{100%}{negate}}{$\eigenvalueMatrix$ represents distance on axes.
$\rotationMatrix$ gives rotation.}{50%}{50%}


\newslide{Eigendecomposition of Covariance}

* $\eigenvalueMatrix$ is *diagonal*, $\rotationMatrix^\top\rotationMatrix = \eye$. 
* Useful representation since $\det{\kernelMatrix} = \det{\eigenvalueMatrix^2} = \det{\eigenvalueMatrix}^2$.

\newslide{Capacity control: $\color{\blueColor}{\log \det{\kernelMatrix}}$}


\setupplotcode{import matplotlib.pyplot as plt
import numpy as np
import mlai
import mlai.plot as plot}


\plotcode{plot.covariance_capacity(rotate_angle=np.pi/4, lambda1 = 0.5, lambda2 = 0.3, diagrams = '\writeDiagramsDir/gp/')}

\setupdisplaycode{import notutils as nu
from ipywidgets import IntSlider}
\displaycode{nu.display_plots('gp-optimise-determinant{sample:0>3}.svg', 
                                          directory='\writeDiagramsDir/gp', 
			                  sample=IntSlider(0, 0, 9, 1))}

\slides{\define{width}{80%}
\startanimation{gp-optimise-determinant}{0}{10}
\newframe{\includediagram{\diagramsDir/gp/gp-optimise-determinant000}{\width}}{gp-optimise-determinant}
\newframe{\includediagram{\diagramsDir/gp/gp-optimise-determinant001}{\width}}{gp-optimise-determinant}
\newframe{\includediagram{\diagramsDir/gp/gp-optimise-determinant002}{\width}}{gp-optimise-determinant}
\newframe{\includediagram{\diagramsDir/gp/gp-optimise-determinant003}{\width}}{gp-optimise-determinant}
\newframe{\includediagram{\diagramsDir/gp/gp-optimise-determinant004}{\width}}{gp-optimise-determinant}
\newframe{\includediagram{\diagramsDir/gp/gp-optimise-determinant005}{\width}}{gp-optimise-determinant}
\newframe{\includediagram{\diagramsDir/gp/gp-optimise-determinant006}{\width}}{gp-optimise-determinant}
\newframe{\includediagram{\diagramsDir/gp/gp-optimise-determinant007}{\width}}{gp-optimise-determinant}
\newframe{\includediagram{\diagramsDir/gp/gp-optimise-determinant008}{\width}}{gp-optimise-determinant}
\newframe{\includediagram{\diagramsDir/gp/gp-optimise-determinant009}{\width}}{gp-optimise-determinant}
\endanimation}

\notes{\figure{\includediagram{\diagramsDir/gp/gp-optimise-determinant009}{80%}}{The determinant of the covariance is dependent only on the eigenvalues. It represents the 'footprint' of the Gaussian.}{gp-optimise-determinant-figure}}

\endif
