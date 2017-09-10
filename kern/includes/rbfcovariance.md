``` {#mycode .octave .numberLines startFrom="0"}

  %}
  rbfcovarianceInit
  %{
```

frame start

\[fragile\]

### Covariance Functions

#### Where did this covariance matrix come from?

**Exponentiated Quadratic Kernel Function (RBF, Squared Exponential,
Gaussian)**

$$\kernelScalar\left(\inputVals,\inputVals^{\prime}\right)=\alpha\exp\left(-\frac{\ltwoNorm{\inputVals-\inputVals^{\prime}}^{2}}{2\lengthScale^{2}}\right)$$

columns start

\[c\]

{column width=5cm}

-   Covariance matrix is built using the *inputs* to the function
    $\inputVals$.

-   For the example above it was based on Euclidean distance.

-   The covariance function is also know as a kernel.

{column width=5cm}

``` {#mycode .octave .numberLines startFrom="0"}

      %}
      rbfcovarianceSample
      %{
    
```

{only slideno=&lt;1&gt;}{\\inputdiagram{../../../kern/tex/diagrams/rbfKernelImage}}{only slideno=&lt;2&gt;}{\\begin{animateinline}\[autoplay,loop\]{10}\\PandocStartInclude{../../../kern/tex/diagrams/rbfSampleIncludeText.tex}
\\inputdiagram{../../../kern/tex/diagrams/rbfSample1}\\newframe\\inputdiagram{../../../kern/tex/diagrams/rbfSample2}\\newframe\\inputdiagram{../../../kern/tex/diagrams/rbfSample3}\\newframe\\inputdiagram{../../../kern/tex/diagrams/rbfSample4}\\newframe\\inputdiagram{../../../kern/tex/diagrams/rbfSample5}\\newframe\\inputdiagram{../../../kern/tex/diagrams/rbfSample6}\\newframe\\inputdiagram{../../../kern/tex/diagrams/rbfSample7}\\newframe\\inputdiagram{../../../kern/tex/diagrams/rbfSample8}\\newframe\\inputdiagram{../../../kern/tex/diagrams/rbfSample9}\\newframe\\inputdiagram{../../../kern/tex/diagrams/rbfSample10}\\newframe\\inputdiagram{../../../kern/tex/diagrams/rbfSample11}\\newframe\\inputdiagram{../../../kern/tex/diagrams/rbfSample12}\\newframe\\inputdiagram{../../../kern/tex/diagrams/rbfSample13}\\newframe\\inputdiagram{../../../kern/tex/diagrams/rbfSample14}\\newframe\\inputdiagram{../../../kern/tex/diagrams/rbfSample15}\\newframe\\inputdiagram{../../../kern/tex/diagrams/rbfSample16}\\newframe\\inputdiagram{../../../kern/tex/diagrams/rbfSample17}\\newframe\\inputdiagram{../../../kern/tex/diagrams/rbfSample18}\\newframe\\inputdiagram{../../../kern/tex/diagrams/rbfSample19}\\newframe\\inputdiagram{../../../kern/tex/diagrams/rbfSample20}\\newframe\\inputdiagram{../../../kern/tex/diagrams/rbfSample21}\\newframe\\inputdiagram{../../../kern/tex/diagrams/rbfSample22}\\newframe\\inputdiagram{../../../kern/tex/diagrams/rbfSample23}\\newframe\\inputdiagram{../../../kern/tex/diagrams/rbfSample24}\\newframe\\inputdiagram{../../../kern/tex/diagrams/rbfSample25}\\newframe\\inputdiagram{../../../kern/tex/diagrams/rbfSample26}\\newframe\\inputdiagram{../../../kern/tex/diagrams/rbfSample27}\\newframe\\inputdiagram{../../../kern/tex/diagrams/rbfSample28}\\newframe\\inputdiagram{../../../kern/tex/diagrams/rbfSample29}\\newframe\\inputdiagram{../../../kern/tex/diagrams/rbfSample30}

\\PandocEndInclude{input}{35}{185}\\end{animateinline}}

columns end

frame end
