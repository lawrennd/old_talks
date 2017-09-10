``` {#mycode .octave .numberLines startFrom="0"}

  %}
  rbfbasiscovarianceInit
  %{
```

frame start

\[fragile\]

### Covariance Functions

**RBF Basis Functions**

$$\kernelScalar\left(\inputVals,\inputVals^{\prime}\right)=\alpha\basisVector(\inputVals)^\top \basisVector(\inputVals^\prime)$$

columns start

\[c\]

{column width=5cm}
$$\basisFunction_k(\inputScalar) = \exp\left(-\frac{\ltwoNorm{\inputScalar-\meanScalar_k}^{2}}{\lengthScale^{2}}\right)$$
$$\meanVector = \begin{bmatrix} -1 \\ 0 \\ 1\end{bmatrix}$$
{column width=5cm}

``` {#mycode .octave .numberLines startFrom="0"}

      %}
      rbfbasiscovarianceSample
      %{
    
```

{only slideno=&lt;1&gt;}{\\inputdiagram{../../../kern/tex/diagrams/rbfbasisCovarianceImage}}{only slideno=&lt;2&gt;}{\\inputdiagram{../../../kern/tex/diagrams/rbfbasisCovarianceSamples}}

columns end

frame end
