\ifndef{gaussLeastSquares}
\define{gaussLeastSquares}

\editme

\subsection{Sum of Squares and Probability}

\notes{In the overdetermined system we introduced a new set of slack variables, $\{\noiseScalar_i\}_{i=1}^\numData$, on top of our parameters $m$ and $c$. We dealt with the variables by placing a probability distribution over them. This gives rise to the likelihood and for the case of Gaussian distributed variables, it gives rise to the sum of squares error. It was Gauss who first made this connection in his volume on *Theoria Motus Corprum Coelestium* [@Gauss:theoria09] (written in Latin)}

\figure{\includegooglebook{ORUOAAAAQAAJ}{PA213}}{Gauss's book *Theoria Motus Corprum Coelestium* [@Gauss:theoria09] motivates the use of least squares through a probabilistic forumation.}{gauss-theoria-ls}

\notes{The relevant section roughly translates as}

>... It is clear, that for the product $\Omega = h^\mu \pi^{-\frac{1}{2}\mu} e^{-hh(vv + v^\prime v^\prime + v^{\prime\prime} v^{\prime\prime} + \dots)}$ to be maximised the sum $vv + v ^\prime v^\prime + v^{\prime\prime} v^{\prime\prime} + \text{etc}.$ ought to be minimized. *Therefore, the most probable values of the unknown quantities $p , q, r , s \text{etc}.$, should be that in which the sum of the squares of the differences between the functions $V, V^\prime, V^{\prime\prime} \text{etc}$, and the observed values is minimized*, for all observations of the same degree of precision is presumed.

\notes{It's on the strength of this paragraph that the density is known as the Gaussian, despite the fact that four pages later Gauss credits the necessary integral for the density to Laplace, and it was also Laplace that did a lot of the original work on dealing with these errors through probability. [Stephen Stigler's book on the measurement of uncertainty before 1900](http://www.hup.harvard.edu/catalog.php?isbn=9780674403413) [@Stigler:table99] has a nice chapter on this.}

\notes{
\figure{\includegooglebook{ORUOAAAAQAAJ}{PA217}}{Gauss credits Laplace with the invention of the Gaussian density here.}{gauss-laplace-gaussian}

where the crediting to the Laplace is about halfway through the last paragraph. This book was published in 1809, four years after \refnotes{Legendre presented least squares}{linear-regression} in an appendix to one of his chapters on the orbit of comets. Gauss goes on to make a claim for priority on the method on page 221 (towards the end of the first paragraph ...).

\figure{\includegooglebook{ORUOAAAAQAAJ}{PA221}}{Gauss places his claim for priority on least squares over Legendre who published first. Gauss claims he used least squares for his prediction of the location of Ceres.}{gauss-least-squares-priority}
}


\endif
