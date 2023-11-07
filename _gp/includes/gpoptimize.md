\ifdefined\blackBackground\global\long\def\redColor{cyan}
\global\long\def\magentaColor{green} \global\long\def\blueColor{yellow}
\else\global\long\def\redColor{red}
\global\long\def\magentaColor{magenta} \global\long\def\blueColor{blue}
\fi

``` {#mycode .octave .numberLines startFrom="0"}

  %}
  gpoptimizeInit
%{
```

frame start

### Learning Covariance Parameters

#### Can we determine covariance parameters from the data?

\LARGE

overprint start

\onslide<1>
$$\gaussianDist{\dataVector}{\mathbf{0}}{\kernelMatrix}=\frac{1}{(2\pi)^\frac{\numData}{2}{\det{\kernelMatrix}^{\frac{1}{2}}}}{\exp\left(-\frac{\dataVector^{\top}\kernelMatrix^{-1}\dataVector}{2}\right)}$$
\onslide<2> $$\begin{aligned}
    \gaussianDist{\dataVector}{\mathbf{0}}{\kernelMatrix}=\frac{1}{(2\pi)^\frac{\numData}{2}{\color{\blueColor} \det{\kernelMatrix}^{\frac{1}{2}}}}{\color{\redColor}\exp\left(-\frac{\dataVector^{\top}\kernelMatrix^{-1}\dataVector}{2}\right)}
    \end{aligned}$$ \onslide<3> $$\begin{aligned}
    \log \gaussianDist{\dataVector}{\mathbf{0}}{\kernelMatrix}=&{\color{\blueColor}-\frac{1}{2}\log\det{\kernelMatrix}}{\color{\redColor}-\frac{\dataVector^{\top}\kernelMatrix^{-1}\dataVector}{2}} \\ &-\frac{\numData}{2}\log2\pi
    \end{aligned}$$ \onslide<4>
$$\errorFunction(\parameterVector) = {\color{\blueColor} \frac{1}{2}\log\det{\kernelMatrix}} + {\color{\redColor} \frac{\dataVector^{\top}\kernelMatrix^{-1}\dataVector}{2}}$$

overprint end

The parameters are *inside* the covariance function (matrix).
\normalsize
$$\kernelScalar_{i, j} = \kernelScalar(\inputVals_i, \inputVals_j; \parameterVector)$$

frame end

frame start

\[fragile\]

### Eigendecomposition of Covariance

A useful decomposition for understanding the objective function.

[\Large
$$\kernelMatrix = \rotationMatrix \eigenvalueMatrix^2 \rotationMatrix^\top$$]{}

``` {#mycode .octave .numberLines startFrom="0"}

      %}
      gpoptimizePlot1
      %{
    
```

columns start

\[c\] {column width=6cm}
![](../../../gp/tex/diagrams/gp_optimise_eigen.png) {column width=6cm}
Diagonal of $\eigenvalueMatrix$ represents distance along axes.\
$\rotationMatrix$ gives a rotation of these axes.

columns end

\Large where $\eigenvalueMatrix$ is a *diagonal* matrix and
$\rotationMatrix^\top\rotationMatrix = \eye$. \vspace{0.25cm}

Useful representation since
$\det{\kernelMatrix} = \det{\eigenvalueMatrix^2} = \det{\eigenvalueMatrix}^2$.

frame end

frame start

\[fragile\]

### Capacity control: ${\color{\blueColor} \log \det{\kernelMatrix}}$

``` {#mycode .octave .numberLines startFrom="0"}

    %}
    gpoptimizePlot2
    %{
  
```

\only<1>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseDeterminant1}}\only<2>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseDeterminant2}}\only<3>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseDeterminant3}}\only<4>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseDeterminant4}}\only<5>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseDeterminant5}}\only<6>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseDeterminant6}}\only<7>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseDeterminant7}}\only<8>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseDeterminant8}}\only<9>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseDeterminant9}}\only<10>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseDeterminant10}}

frame end

frame start

\[fragile\]

### Data Fit: ${\color{\redColor} \frac{\dataVector^\top\kernelMatrix^{-1}\dataVector}{2}}$

``` {#mycode .octave .numberLines startFrom="0"}

    %}
    gpoptimizePlot3
    %{
  
```

\only<1>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseQuadratic1}}\only<2>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseQuadratic2}}\only<3>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseQuadratic3}}

frame end

frame start

\[fragile\]

### Learning Covariance Parameters {#learning-covariance-parameters}

#### Can we determine length scales and noise levels from the data?

``` {#mycode .octave .numberLines startFrom="0"}

    %}
    gpoptimizePlot4
    %{
  
```

\only<1>{\inputdiagram{../../../gp/tex/diagrams/gpOptimise1}\hfill}\only<1>{\inputdiagram{../../../gp/tex/diagrams/gpOptimise2}}\only<2>{\inputdiagram{../../../gp/tex/diagrams/gpOptimise3}\hfill}\only<2>{\inputdiagram{../../../gp/tex/diagrams/gpOptimise4}}\only<3>{\inputdiagram{../../../gp/tex/diagrams/gpOptimise5}\hfill}\only<3>{\inputdiagram{../../../gp/tex/diagrams/gpOptimise6}}\only<4>{\inputdiagram{../../../gp/tex/diagrams/gpOptimise7}\hfill}\only<4>{\inputdiagram{../../../gp/tex/diagrams/gpOptimise8}}\only<5>{\inputdiagram{../../../gp/tex/diagrams/gpOptimise9}\hfill}\only<5>{\inputdiagram{../../../gp/tex/diagrams/gpOptimise10}}\only<6>{\inputdiagram{../../../gp/tex/diagrams/gpOptimise11}\hfill}\only<6>{\inputdiagram{../../../gp/tex/diagrams/gpOptimise12}}\only<7>{\inputdiagram{../../../gp/tex/diagrams/gpOptimise13}\hfill}\only<7>{\inputdiagram{../../../gp/tex/diagrams/gpOptimise14}}\only<8>{\inputdiagram{../../../gp/tex/diagrams/gpOptimise15}\hfill}\only<8>{\inputdiagram{../../../gp/tex/diagrams/gpOptimise16}}\only<9>{\inputdiagram{../../../gp/tex/diagrams/gpOptimise17}\hfill}\only<9>{\inputdiagram{../../../gp/tex/diagrams/gpOptimise18}}

$$\errorFunction(\parameterVector) = {\color{\blueColor}\frac{1}{2}\log\det{\kernelMatrix}}+{\color{\redColor}\frac{\dataVector^{\top}\kernelMatrix^{-1}\dataVector}{2}}$$

frame end

[../../../gp/tex/talks/gp\_gene\_expression\_optimize\_example](../../../gp/tex/talks/gp_gene_expression_optimize_example.md)
