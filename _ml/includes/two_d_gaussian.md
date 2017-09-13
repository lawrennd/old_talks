### Two Dimensional Gaussian

-   Consider height, $h/m$ and weight, $w/kg$.

-   Could sample height from a distribution:
    $$p(h) \sim {\mathcal{N}\left(1.7,0.0225\right)}$$

-   And similarly weight: $$p(w) \sim {\mathcal{N}\left(75,36\right)}$$

### Height and Weight Models {data-transition="none"}

<object class="svgplot"
data="../_ml/diagrams/height_weight_gaussian.svg">
</object>

Gaussian distributions for height and weight.

\include{../../_ml/includes/two_d_gaussian_independent_sample.md}

### Independence Assumption

-   This assumes height and weight are independent.
    $$p(h, w) = p(h)p(w)$$

-   In reality they are dependent (body mass index) $= \frac{w}{h^2}$.

\include{../../_ml/includes/two_d_gaussian_correlated_sample.md}

\include{../../_ml/includes/two_d_gaussian_maths.md}
