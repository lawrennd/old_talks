\ifndef{stackedGp}
\define{stackedGp}
\editme

\subsection{Stacked GP}

\plotcode{plot.stack_gp_sample(kernel=GPy.kern.RBF,
                     diagrams="\writeDiagramsDir/deepgp")}
				
\displaycode{pods.notebook.display_plots('stack-gp-sample-RBF-{sample:0>1}.svg', 
                            directory='\writeDiagramsDir/deepgp', sample=(0,4))}

\slides{
\define{width}{10%}
\startanimation{stack-gp-sample}{0}{4}
\newframe{\includediagram{\diagramsDir/stack-gp-sample-0}{\width}}{stack-gp-sample}
\newframe{\includediagram{\diagramsDir/stack-gp-sample-1}{\width}}{stack-gp-sample}
\newframe{\includediagram{\diagramsDir/stack-gp-sample-2}{\width}}{stack-gp-sample}
\newframe{\includediagram{\diagramsDir/stack-gp-sample-3}{\width}}{stack-gp-sample}
\newframe{\includediagram{\diagramsDir/stack-gp-sample-4}{\width}}{stack-gp-sample}
\endanimation
}
\notes{\figure{\includediagram{\diagramsDir/stack-gp-sample-4}{20%}}{Stacking Gaussian process models leads to non linear mappings at each stage. Here we are mapping from two dimensions to two dimensions in each layer.}{stack-gp-sample}}

\notes{Note that once the box has folded over on itself, it cannot be unfolded. So a feature that is generated near the top of the model cannot be removed further down the model.

This folding over effect happens in low dimensions. In higher dimensions it is less common. 

Observation of this effect at a talk in Cambridge was one of the things that caused David Duvenaud (and collaborators) to consider the behavior of deeper Gaussian process models [@Duvenaud:pathologies14]. 

Such folding over in the latent spaces necessarily forces the density to be non-Gaussian. Indeed, since folding-over is avoided as we increase the dimensionality of the latent spaces, such processes become more Gaussian. If we take the limit of the latent space dimensionality as it tends to infinity, the entire deep Gaussian process returns to a standard Gaussian process, with a covariance function given as a deep kernel (such as those described by @Cho:deep09).

Further analysis of these deep networks has been conducted by @Dunlop:deep2017, who use analysis of the deep network's stationary density (treating it as a Markov chain across layers), to explore the nature of the implied process prior for a deep GP.

Both of these works, however, make constraining assumptions on the form of the Gaussian process prior at each layer (e.g. same covariance at each layer). In practice, the form of this covariance can be learnt and the densities described by the deep GP are more general than those mentioned in either of these papers.
}
\newslide{Analysis of Deep GPs}
\slides{
* *Avoiding pathologies in very deep networks* @Duvenaud:pathologies14 show that the derivative distribution of the process becomes more *heavy tailed* as number of layers increase.

* *How Deep Are Deep Gaussian Processes?* @Dunlop:deep2017 perform a theoretical analysis possible through conditional Gaussian Markov property.
}

\include{_deepgp/includes/deep-pathologies.md}


\endif
