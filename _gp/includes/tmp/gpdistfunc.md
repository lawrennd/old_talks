\ifdefined\blackBackground\global\long\def\redColor{cyan}
\global\long\def\magentaColor{green} \global\long\def\blueColor{yellow}
\else\global\long\def\redColor{red}
\global\long\def\magentaColor{magenta} \global\long\def\blueColor{blue}
\fi

``` {#mycode .octave .numberLines startFrom="0"}

  %}
  gpdistfuncInit
  %{
```

<!--frame start-->
### Sampling a Function

[**Multi-variate Gaussians**]{}

-   We will consider a Gaussian with a particular structure of
    covariance matrix.

-   Generate a single sample from this 25 dimensional Gaussian
    distribution,
    ${\mathbf{{f}}}=\left[{f}_{1},{f}_{2}\dots {f}_{25}\right]$.

-   We will plot these points against their index.

<!--frame end-->
<!--frame start-->
\[fragile\]

### Gaussian Distribution Sample

``` {#mycode .octave .numberLines startFrom="0"}

            gpdistfuncSample
          
```

\subfigure[A 25 dimensional correlated random variable (values ploted against index)]{\only<1>{\inputdiagram{../../../gp/tex/diagrams/gpSampleValue}}\only<2->{\inputdiagram{../../../gp/tex/diagrams/gpSampleValue12}}}\hfill\only<1-7>{\subfigure[colormap showing correlations between dimensions.]{\only<1-2>{\inputdiagram{../../../gp/tex/diagrams/gpSampleCovariance}}\only<3>{\inputdiagram{../../../gp/tex/diagrams/gpSampleCovariance12a}}\only<4>{\inputdiagram{../../../gp/tex/diagrams/gpSampleCovariance12b}}\only<5>{\inputdiagram{../../../gp/tex/diagrams/gpSampleCovariance12c}}\only<6>{\inputdiagram{../../../gp/tex/diagrams/gpSampleCovariance12d}}\only<7>{\inputdiagram{../../../gp/tex/diagrams/gpSampleCovariance12e}}}}\only<8>{\subfigure[correlation between ${f}_1$ and ${f}_2$.]{\inputdiagram{../../../gp/tex/diagrams/gpSampleCovariance12f}}}

<!--frame end-->

