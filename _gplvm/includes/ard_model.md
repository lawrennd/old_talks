<!--frame start-->
### Priors for Latent Space

\begin{flushright}
    \textbf{\cite{Titsias:bayesGPLVM10}}
  \end{flushright}
-   Variational marginalization of $\latentMatrix$ allows us to learn
    parameters of $p(\latentMatrix)$.

-   Standard GP-LVM where $\latentMatrix$ learnt by MAP, this is not
    possible [\scriptsize[see e.g. @Wang:gpdm08]]{}.

-   First example: learn the dimensionality of latent space.

<!--frame end-->
\include{../gplvm/includes/graphical_gplvm.md}
\include{../gplvm/includes/ard_description.md}
