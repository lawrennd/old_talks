<!--frame start-->
### Independent Gaussians

<!--overprint start-->
\onslide<1> $$p(w, h) = p(w)p(h)$$ \onslide<2>
$$p(w, h) = \frac{1}{\sqrt{2\pi {\sigma}_1^2}\sqrt{2\pi{\sigma}_2^2}} \exp\left(-\frac{1}{2}\left(\frac{(w-{\mu}_1)^2}{{\sigma}_1^2} + \frac{(h-{\mu}_2)^2}{{\sigma}_2^2}\right)\right)$$
\onslide<3> \small
$$p(w, h) = \frac{1}{\sqrt{2\pi{\sigma}_1^22\pi{\sigma}_2^2}} \exp\left(-\frac{1}{2}\left(\begin{bmatrix}w \\ h\end{bmatrix} - \begin{bmatrix}{\mu}_1 \\ {\mu}_2\end{bmatrix}\right)^\top\begin{bmatrix}{\sigma}_1^2& 0\\0&{\sigma}_2^2\end{bmatrix}^{-1}\left(\begin{bmatrix}w \\ h\end{bmatrix} - \begin{bmatrix}{\mu}_1 \\ {\mu}_2\end{bmatrix}\right)\right)$$
\onslide<4>
$$p({\mathbf{{y}}}) = \frac{1}{{\left|2\pi \mathbf{D}\right|}^{\frac{1}{2}}} \exp\left(-\frac{1}{2}({\mathbf{{y}}}- {\boldsymbol{{\mu}}})^\top\mathbf{D}^{-1}({\mathbf{{y}}}- {\boldsymbol{{\mu}}})\right)$$

<!--overprint end-->
<!--frame end-->
<!--frame start-->
### Correlated Gaussian

Form correlated from original by rotating the data space using matrix
${\mathbf{\MakeUppercase{{r}}}}$.

<!--overprint start-->
\onslide<1>
$$p({\mathbf{{y}}}) = \frac{1}{{\left|2\pi\mathbf{D}\right|}^{\frac{1}{2}}} \exp\left(-\frac{1}{2}({\mathbf{{y}}}- {\boldsymbol{{\mu}}})^\top\mathbf{D}^{-1}({\mathbf{{y}}}- {\boldsymbol{{\mu}}})\right)$$
\onslide<2>
$$p({\mathbf{{y}}}) = \frac{1}{{\left|2\pi\mathbf{D}\right|}^{\frac{1}{2}}} \exp\left(-\frac{1}{2}({\mathbf{\MakeUppercase{{r}}}}^\top{\mathbf{{y}}}- {\mathbf{\MakeUppercase{{r}}}}^\top{\boldsymbol{{\mu}}})^\top\mathbf{D}^{-1}({\mathbf{\MakeUppercase{{r}}}}^\top{\mathbf{{y}}}- {\mathbf{\MakeUppercase{{r}}}}^\top{\boldsymbol{{\mu}}})\right)$$
\onslide<3>
$$p({\mathbf{{y}}}) = \frac{1}{{\left|2\pi\mathbf{D}\right|}^{\frac{1}{2}}} \exp\left(-\frac{1}{2}({\mathbf{{y}}}- {\boldsymbol{{\mu}}})^\top{\mathbf{\MakeUppercase{{r}}}}\mathbf{D}^{-1}{\mathbf{\MakeUppercase{{r}}}}^\top({\mathbf{{y}}}- {\boldsymbol{{\mu}}})\right)$$
this gives a covariance matrix:
$${\mathbf{\MakeUppercase{{c}}}}^{-1} = {\mathbf{\MakeUppercase{{r}}}}\mathbf{D}^{-1} {\mathbf{\MakeUppercase{{r}}}}^\top$$
\onslide<4>
$$p({\mathbf{{y}}}) = \frac{1}{{\left|2\pi{\mathbf{\MakeUppercase{{c}}}}\right|}^{\frac{1}{2}}} \exp\left(-\frac{1}{2}({\mathbf{{y}}}- {\boldsymbol{{\mu}}})^\top{\mathbf{\MakeUppercase{{c}}}}^{-1} ({\mathbf{{y}}}- {\boldsymbol{{\mu}}})\right)$$
this gives a covariance matrix:
$${\mathbf{\MakeUppercase{{c}}}}= {\mathbf{\MakeUppercase{{r}}}}\mathbf{D} {\mathbf{\MakeUppercase{{r}}}}^\top$$

<!--overprint end-->
<!--frame end-->

