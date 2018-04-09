### Two Dimensional Gaussian

-   Consider height, $h/m$ and weight, $w/kg$.

-   Could sample height from a distribution:
    $$p(h) \sim \gaussianSamp{1.7}{0.0225}$$

-   And similarly weight: $$p(\mappingScalar) \sim \gaussianSamp{75}{36}$$

\plotcode{plot.height_weight(diagrams='../../slides/diagrams/ml')}

\slides{
### Height and Weight Models {data-transition="none"}

\includesvg{../slides/diagrams/ml/height_weight_gaussian.svg}

Gaussian distributions for height and weight.
}
\include{../../_ml/includes/two-d-gaussian-independent-sample.md}

### Independence Assumption

-   This assumes height and weight are independent.
    $$p(h, w) = p(h)p(w)$$

-   In reality they are dependent (body mass index) $= \frac{w}{h^2}$.

\include{../../_ml/includes/two-d-gaussian-correlated-sample.md}

\include{../../_ml/includes/two-d-gaussian-maths.md}
