``` {#mycode .octave .numberLines startFrom="0"}

  %}
  gpKalmanFilterKroneckerInit
  %{
```

<!--frame start-->
\[allowframebreaks\]

### Simple Kalman Filter

-   We have state vector $\latentMatrix = \left[\latentVector_1
          \dots \latentVector_\latentDim\right] \in \mathbb{R}^{\numTime
          \times \latentDim}$ and if each state evolves independently we
    have $$\begin{aligned}
        p(\latentMatrix) &= \prod_{i=1}^\latentDim p(\latentVector_{:,
          i}) \\
        p(\latentVector_{:, i})&= \gaussianDist{\latentVector_{:,
            i}}{\zerosVector}{\kernelMatrix}.
      \end{aligned}$$

-   We want to obtain outputs through:
    $$\dataVector_{i, :} = \mappingMatrix \latentVector_{i, :}$$

<!--frame end-->
<!--frame start-->
\[allowframebreaks\]

### Stacking and Kronecker Products

-   Represent with a ‘stacked’ system:
    $$p(\latentVector) = \gaussianDist{\latentVector}{\zerosVector}{\eye \otimes \kernelMatrix}$$
    where the stacking is placing each column of $\latentMatrix$ one on
    top of another as $$\latentVector = \begin{bmatrix}
          \latentVector_{:, 1}\\
          \latentVector_{:, 2}\\
          \vdots\\
          \latentVector_{:, \latentDim}
        \end{bmatrix}$$

<!--frame end-->
<!--frame start-->
\[fragile\]

### Kronecker Product

``` {#mycode .octave .numberLines startFrom="0"}

    %}
    gpKalmanFilterKroneckerPlot1
    %{
  
```

\only<1>{\inputdiagram{../../../gp/tex/diagrams/kroneckerProduct}}\only<2>{\inputdiagram{../../../gp/tex/diagrams/kroneckerProductImage}}

<!--frame end-->
<!--frame start-->
\[allowframebreaks\]

### Stacking and Kronecker Products {#stacking-and-kronecker-products}

-   Represent with a ‘stacked’ system:
    $$p(\latentVector) = \gaussianDist{\latentVector}{\zerosVector}{\eye \otimes \kernelMatrix}$$
    where the stacking is placing each column of $\latentMatrix$ one on
    top of another as $$\latentVector = \begin{bmatrix}
          \latentVector_{:, 1}\\
          \latentVector_{:, 2}\\
          \vdots\\
          \latentVector_{:, \latentDim}
        \end{bmatrix}$$

<!--frame end-->
<!--frame start-->
\[fragile\]

### Column Stacking

``` {#mycode .octave .numberLines startFrom="0"}

    %}
    gpKalmanFilterKroneckerPlot2
    %{
  
```

![](../../../gp/tex/diagrams/kronecker_ik.png)

<!--frame end-->
<!--frame start-->
\[fragile\]

``` {#mycode .octave .numberLines startFrom="0"}

    %}
    gpKalmanFilterKroneckerPlot3
    %{
  
```

\
[For this stacking the marginal distribution over *time* is given by the
block diagonals.]{}

<!--frame end-->
<!--frame start-->
### Two Ways of Stacking

Can also stack each row of $\latentMatrix$ to form column vector:
$$\latentVector = \begin{bmatrix}
      \latentVector_{1, :}\\
      \latentVector_{2, :}\\
      \vdots\\
      \latentVector_{\numTime, :}
    \end{bmatrix}$$
$$p(\latentVector) = \gaussianDist{\latentVector}{\zerosVector}{\kernelMatrix \otimes \eye}$$

<!--frame end-->
<!--frame start-->
\[fragile\]

### Row Stacking

``` {#mycode .octave .numberLines startFrom="0"}

    %}
    gpKalmanFilterKroneckerPlot4
    %{
  
```

![](../../../gp/tex/diagrams/kronecker_ki.png)

<!--frame end-->
<!--frame start-->
\[fragile\]

``` {#mycode .octave .numberLines startFrom="0"}

    %}
    gpKalmanFilterKroneckerPlot5
    %{
  
```

\
[For this stacking the marginal distribution over the latent
*dimensions* is given by the block diagonals.]{}

<!--frame end-->
<!--frame start-->
### Observed Process

The observations are related to the latent points by a linear mapping
matrix,
$$\dataVector_{i, :} = \mappingMatrix \latentVector_{i, :} + \noiseVector_{i, :}$$
$$\noiseVector \sim \gaussianSamp{0}{\dataStd^2\eye}$$

<!--frame end-->
<!--frame start-->
\[fragile\]

### Mapping from Latent Process to Observed

``` {#mycode .octave .numberLines startFrom="0"}

    %}
    gpKalmanFilterKroneckerPlot6
    %{
  
```

![](../../../gp/tex/diagrams/kronecker_product_wx.png)

<!--frame end-->
<!--frame start-->
### Output Covariance

This leads to a covariance of the form
$$(\eye \otimes \mappingMatrix) (\kernelMatrix \otimes \eye) (\eye \otimes \mappingMatrix^\top) + \eye\dataStd^2$$
Using
$(\mathbf{A}\otimes\mathbf{B}) (\mathbf{C}\otimes\mathbf{D}) = \mathbf{A}\mathbf{C} \otimes \mathbf{B}\mathbf{D}$
This leads to
$$\kernelMatrix \otimes \mappingMatrix\mappingMatrix^\top + \eye \dataStd^2$$
or
$$\dataVector \sim \gaussianSamp{0}{\mappingMatrix\mappingMatrix^\top \otimes \kernelMatrix + \eye\dataStd^2}$$

<!--frame end-->

