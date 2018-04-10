\setupcode{import teaching_plots as plot}

### The Gaussian Density

-   Perhaps the most common probability density.

$$\begin{align}
p(\dataScalar| \meanScalar, \dataStd^2) & = \frac{1}{\sqrt{2\pi\dataStd^2}}\exp\left(-\frac{(\dataScalar - \meanScalar)^2}{2\dataStd^2}\right)\\& \buildrel\triangle\over = \gaussianDist{\dataScalar}{\meanScalar}{\dataStd^2}
\end{align}$$
 
. . .

-   The Gaussian density.

\code{plot.gaussian_of_height(diagrams='../../slides/diagrams/ml')}

### Gaussian Density

\includesvg{../slides/diagrams/gaussian_of_height.svg}

The Gaussian PDF with ${\mu}=1.7$ and variance ${\sigma}^2=
  0.0225$. Mean shown as cyan line. It could represent the heights of a
population of students.

### Gaussian Density {#gaussian-density}

<large>
$$
\gaussianDist{\dataScalar}{\meanScalar}{\dataStd^2} = \frac{1}{\sqrt{2\pi\dataStd^2}} \exp\left(-\frac{(\dataScalar-\meanScalar)^2}{2\dataStd^2}\right)
$$
$\dataStd^2$ is the variance of the density and $\meanScalar$ is the mean.
</large>


