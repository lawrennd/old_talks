<!--frame start-->
### Multivariate Regression Likelihood

-   Noise corrupted data point
    $${y}_i = {\mathbf{{w}}}^\top {{\bf {x}}}_{i, :} + {\epsilon}_i$$
    \pause

-   Multivariate regression likelihood:
    $$p({\mathbf{{y}}}| {{\bf \MakeUppercase{{x}}}}, {\mathbf{{w}}}) = \frac{1}{\left(2\pi {\sigma}^2\right)^{{n}/2}} \exp\left(-\frac{1}{2{\sigma}^2}\sum_{i=1}^{n}\left({y}_i - {\mathbf{{w}}}^\top {{\bf {x}}}_{i, :}\right)^2\right)$$
    \pause

-   Now use a multivariate Gaussian prior:
    $$p({\mathbf{{w}}}) = \frac{1}{\left(2\pi \alpha\right)^\frac{{p}}{2}} \exp \left(-\frac{1}{2\alpha} {\mathbf{{w}}}^\top {\mathbf{{w}}}\right)$$

<!--frame end-->

