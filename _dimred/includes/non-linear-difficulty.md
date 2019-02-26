\ifndef{nonLinearDifficulty}
\define{nonLinearDifficulty}

\editme

\subsection{Difficulty for Probabilistic Approaches}

\setupplotcode{import teaching_plots as plot}

\plotcode{plot.non_linear_difficulty_plot_3(diagrams='../../slides/diagrams/dimred/')}


\notes{The challenge for composition of probabilistic models is that you need to propagate a probability densities through non linear mappings. This allows you to create broader classes of probability density. Unfortunately it renders the resulting densities *intractable*.}\slides{
* Propagate a probability distribution through a non-linear mapping.

* Normalisation of distribution becomes intractable.
}

\figure{\includediagram{../slides/diagrams/dimred/nonlinear-mapping-3d-plot}{center}{80%}}{A two dimensional grid mapped into three dimensions to form a two dimensional manifold.}{nonlinear-mapping-3d-plot}

\plotcode{plot.non_linear_difficulty_plot_2(diagrams='../../slides/diagrams/dimred/')}

\newslide{Difficulty for Probabilistic Approaches}

\slides{
* Propagate a probability distribution through a non-linear mapping.

* Normalisation of distribution becomes intractable.
}

\figure{\includediagram{../slides/diagrams/dimred/nonlinear-mapping-2d-plot}{center}{80%}}{A one dimensional line mapped into two dimensions by two separate independent functions. Each point can be mapped exactly through the mappings.}{non-linear-mapping-2d-plot}

\plotcode{plot.non_linear_difficulty_plot_1(diagrams='../../slides/diagrams/dimred')}

\newslide{Difficulty for Probabilistic Approaches}

\slides{
* Propagate a probability distribution through a non-linear mapping.

* Normalisation of distribution becomes intractable.
}

\figure{\includediagram{../slides/diagrams/dimred/gaussian-through-nonlinear}{80%}}{A Gaussian density over the input of a non linear function leads to a very non Gaussian output. Here the output is multimodal.}{gaussian-through-nonlinear}


\endif
