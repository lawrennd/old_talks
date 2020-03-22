\ifndef{deepTheory}
\define{deepTheory}
\editme
\include{_deepgp/includes/process-composition.md}
\include{_dimred/includes/non-linear-difficulty.md}
\include{_gplvm/includes/variational-bayes-gplvm-long.md}

\newslide{See also ...}
\slides{
* MAP approach [@Lawrence:hgplvm07].
* Hamiltonian Monte Carlo approach [@Havasi:deepgp18].
* Expectation Propagation approach [@Bui:deep16].
}
\notes{Variational approximations aren't the only approach to approximate inference. The original work on deep Gaussian processes made use of MAP approximations [@Lawrence:hgplvm07], which couldn't propagate the uncertainty through the model at the data points but sustain uncertainty elsewhere. Since the variational approximation was proposed researchers have also considered sampling approaches [@Havasi:deepgp18] and expectation propagation [@Bui:deep16].}

\newslide{Neural Networks}

\figure{\includepng{\diagramsDir/deepgp/neural-network-uncertainty}{90%}}{Even the latest work on Bayesian neural networks has severe problems handling uncertainty. In this example, [@Izmailov:subspace19], methods even fail to interpolate through the data correctly or provide well calibrated error bars in regions where data is observed.}{neural-network-uncertainty}
\slides{\alignright{@Izmailov:subspace19}}


\include{_deepgp/includes/stack-gp-intro.md}
\include{_deepgp/includes/stacked-pca.md}
\include{_deepgp/includes/stacked-gp.md}
\endif
