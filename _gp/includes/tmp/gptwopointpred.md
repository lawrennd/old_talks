\ifdefined\blackBackground\global\long\def\redColor{cyan}
\global\long\def\greenColor{magenta} \global\long\def\blueColor{yellow}
\global\long\def\magentaColor{green} \else\global\long\def\redColor{red}
\global\long\def\greenColor{green} \global\long\def\blueColor{blue}
\global\long\def\magentaColor{magenta} \fi

``` {#mycode .octave .numberLines startFrom="0"}

  %}
  gptwopointpredInit
  %{
```

<!--frame start-->
\[fragile\]

### Prediction of ${f}_{2}$ from ${f}_{1}$

``` {#mycode .octave .numberLines startFrom="0"}

        gptwopointpredPlot
      
```

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------
      \only<1>{\inputdiagram{../../../gp/tex/diagrams/gptwopointpred1_2_1}}\only<2>{\inputdiagram{../../../gp/tex/diagrams/gptwopointpred1_2_2}}\only<3>{\inputdiagram{../../../gp/tex/diagrams/gptwopointpred1_2_3}}\only<4>{\inputdiagram{../../../gp/tex/diagrams/gptwopointpred1_2_4}}   ![](../../../gp/tex/diagrams/gp_sample_covariance12f.png)
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------

-   The single contour of the Gaussian density represents the
    [\color{\blueColor} joint distribution, $p({f}_1, {f}_2)$]{}. \pause

-   We observe that
    [\color{\greenColor}$\PandocStartInclude{../../../gp/tex/diagrams/inputValueF1.tex}{f}_1=-0.313\PandocEndInclude{input}{41}{91}$]{}.
    \pause

-   Conditional density: [\color{\redColor}
    $p({f}_2|\PandocStartInclude{../../../gp/tex/diagrams/inputValueF1.tex}{f}_1=-0.313\PandocEndInclude{input}{42}{116})$]{}.

<!--frame end-->
<!--frame start-->
### Prediction with Correlated Gaussians

-   Prediction of ${f}_2$ from ${f}_1$ requires *conditional density*.

-   Conditional density is *also* Gaussian.
    $$p({f}_2|{f}_1) = {\mathcal{N}\left({f}_2|\frac{{k}_{1, 2}}{{k}_{1, 1}}{f}_1,{k}_{2, 2} - \frac{{k}_{1,2}^2}{{k}_{1,1}}\right)}$$
    where covariance of joint density is given by
    $${\mathbf{\MakeUppercase{{k}}}}= \begin{bmatrix} {k}_{1, 1} & {k}_{1, 2}\\ {k}_{2, 1} & {k}_{2, 2}\end{bmatrix}$$

<!--frame end-->
<!--frame start-->
### Prediction of ${f}_{5}$ from ${f}_{1}$

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------
      \only<1>{\inputdiagram{../../../gp/tex/diagrams/gptwopointpred1_5_1}}\only<2>{\inputdiagram{../../../gp/tex/diagrams/gptwopointpred1_5_2}}\only<3>{\inputdiagram{../../../gp/tex/diagrams/gptwopointpred1_5_3}}\only<4>{\inputdiagram{../../../gp/tex/diagrams/gptwopointpred1_5_4}}   ![](../../../gp/tex/diagrams/gp_sample_covariance15f.png)
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------

-   The single contour of the Gaussian density represents the
    [\color{\blueColor} joint distribution, $p({f}_1, {f}_5)$]{}. \pause

-   We observe that
    [\color{\greenColor}$\PandocStartInclude{../../../gp/tex/diagrams/inputValueF1.tex}{f}_1=-0.313\PandocEndInclude{input}{77}{91}$]{}.
    \pause

-   Conditional density: [\color{\redColor}
    $p({f}_5|\PandocStartInclude{../../../gp/tex/diagrams/inputValueF1.tex}{f}_1=-0.313\PandocEndInclude{input}{78}{116})$]{}.

<!--frame end-->
<!--frame start-->
### Prediction with Correlated Gaussians {#prediction-with-correlated-gaussians}

-   Prediction of ${\mathbf{{f}}}_*$ from ${\mathbf{{f}}}$ requires
    multivariate *conditional density*.

-   Multivariate conditional density is *also* Gaussian. \large

    <!--overprint start-->
    \onslide<1>
    $$p({\mathbf{{f}}}_*|{\mathbf{{f}}}) = {\mathcal{N}\left({\mathbf{{f}}}_*|{\mathbf{\MakeUppercase{{k}}}}_{*,{\mathbf{{f}}}}{\mathbf{\MakeUppercase{{k}}}}_{{\mathbf{{f}}},{\mathbf{{f}}}}^{-1}{\mathbf{{f}}},{\mathbf{\MakeUppercase{{k}}}}_{*,*}-{\mathbf{\MakeUppercase{{k}}}}_{*,{\mathbf{{f}}}} {\mathbf{\MakeUppercase{{k}}}}_{{\mathbf{{f}}},{\mathbf{{f}}}}^{-1}{\mathbf{\MakeUppercase{{k}}}}_{{\mathbf{{f}}},*}\right)}$$
    \onslide<2>
    $$p({\mathbf{{f}}}_*|{\mathbf{{f}}}) = {\mathcal{N}\left({\mathbf{{f}}}_*|{\boldsymbol{{\mu}}},\boldsymbol{\Sigma}\right)}$$
    $${\boldsymbol{{\mu}}}= {\mathbf{\MakeUppercase{{k}}}}_{*,{\mathbf{{f}}}}{\mathbf{\MakeUppercase{{k}}}}_{{\mathbf{{f}}},{\mathbf{{f}}}}^{-1}{\mathbf{{f}}}$$
    $$\boldsymbol{\Sigma} = {\mathbf{\MakeUppercase{{k}}}}_{*,*}-{\mathbf{\MakeUppercase{{k}}}}_{*,{\mathbf{{f}}}} {\mathbf{\MakeUppercase{{k}}}}_{{\mathbf{{f}}},{\mathbf{{f}}}}^{-1}{\mathbf{\MakeUppercase{{k}}}}_{{\mathbf{{f}}},*}$$

    <!--overprint end-->
    \normalsize

-   Here covariance of joint density is given by
    $${\mathbf{\MakeUppercase{{k}}}}= \begin{bmatrix} {\mathbf{\MakeUppercase{{k}}}}_{{\mathbf{{f}}}, {\mathbf{{f}}}} & {\mathbf{\MakeUppercase{{k}}}}_{*, {\mathbf{{f}}}}\\ {\mathbf{\MakeUppercase{{k}}}}_{{\mathbf{{f}}}, *} & {\mathbf{\MakeUppercase{{k}}}}_{*, *}\end{bmatrix}$$

<!--frame end-->

