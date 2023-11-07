\ifndef{univariateGaussian}
\define{univariateGaussian}
\editme

\subsection{The Gaussian Density}

\notes{The Gaussian density is perhaps the most commonly used probability density. It is defined by a *mean*, $\meanScalar$, and a *variance*, $\dataStd^2$. The variance is taken to be the square of the *standard deviation*, $\dataStd$.}
\slides{* Perhaps the most common probability density.

. . .

}
  $$\begin{align}
  p(\dataScalar| \meanScalar, \dataStd^2) & = \frac{1}{\sqrt{2\pi\dataStd^2}}\exp\left(-\frac{(\dataScalar - \meanScalar)^2}{2\dataStd^2}\right)\\& \buildrel\triangle\over = \gaussianDist{\dataScalar}{\meanScalar}{\dataStd^2}
  \end{align}$$
 
\setupplotcode{import mlai.plot as plot}
\plotcode{plot.gaussian_of_height(diagrams='\writeDiagramsDir/ml')}

\newslide{Gaussian Density}

\figure{\includediagram{\diagramsDir/ml/gaussian_of_height}{60%}}{The Gaussian PDF with ${\meanScalar}=1.7$ and variance ${\dataStd}^2=0.0225$. Mean shown as \slides{cyan}\notes{red} line. It could represent the heights of a population of students.}{gaussian-of-height}

\newslide{Gaussian Density}
\slides{
\largetext{$$
\gaussianDist{\dataScalar}{\meanScalar}{\dataStd^2} = \frac{1}{\sqrt{2\pi\dataStd^2}} \exp\left(-\frac{(\dataScalar-\meanScalar)^2}{2\dataStd^2}\right)
$$}

. . .

\aligncenter{$\dataStd^2$ is the variance of the density and $\meanScalar$ is the mean.}}


\endif
