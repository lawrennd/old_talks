\ifndef{deepHealthModel}
\define{deepHealthModel}
\editme

\subsection{Deep Health}

\figure{\includediagram{../slides/diagrams/deep-health}{70%}}{The deep health model uses different layers of abstraction in the deep Gaussian process to represent information about diagnostics and treatment to model interelationships between a patients different data modalities.}{deep-health-model}

\notes{From a machine learning perspective, we'd like to be able to interrelate all the different modalities that are informative about the state of the disease. For deep health, the notion is that the state of the disease is appearing at the more abstract levels, as we descend the model, we express relationships between the more abstract concept, that sits within the physician's mind, and the data we can measure.}

\endif
