<!--frame start-->
### Computational Savings

\raggedright{\small\citep{Smola:sparsegp00,Csato:sparse00,Csato:sparse02,Csato:thesis02,Seeger:fast03}}

![image](../../../gp/tex/diagrams/cov_approx){width="90.00000%"}

$$\Kff \approx \Qff = \Kfu \Kuu^{-1}\Kuf$$

Instead of inverting $\Kff$, we make a low rank (or Nyström)
approximation, and invert $\Kuu$ instead.

\vfill  {\footnotesize\hfill Figure originally from presentation by Ed Snelson at NIPS}

<!--frame end-->

