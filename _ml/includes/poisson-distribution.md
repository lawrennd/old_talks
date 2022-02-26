\ifndef{poissonDistribution}
\define{poissonDistribution}

\editme

\subsection{Poisson Distribution}

\slides{
* Poisson distribution is used for 'count data'. For non-negative integers, $y$, 
  $$P(y) = \frac{\lambda^y}{y!}\exp(-y)$$
* Here $\lambda$ is a *rate* parameter that can be thought of as the number of arrivals per unit time.
* Poisson distributions can be used for disease count data. E.g. number of incidence of malaria in a district.
}

\setupplotcode{import mlai.plot}

\plotcode{plot.poisson('\writeDiagramsDir/ml/')}

\newslide{Poisson Distribution}

\figure{\includediagram{\diagramsDir/ml/poisson}{80%}}{The Poisson distribution.}{the-poisson-distribution}

\endif
