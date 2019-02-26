\ifndef{bdaForecasting}
\define{bdaForecasting}
\editme

\notes{\subsection{Analysis of US Birth Rates}}
\newslide{}

\figure{\includepng{../slides/diagrams/ml/bialik-fridaythe13th-1}{70%}}{This is a retrospective analysis of US births by Aki Vehtari. The challenges of forecasting. Even with seasonal and weekly effects removed there are significant effects on holidays, weekends, etc.}{bialik-friday-the-13th}

\notes{There's a nice analysis of US birth rates by Gaussian processes with additive covariances in @Gelman:bayesian13. A combination of covariance functions are used to take account of weekly and yearly trends. The analysis is summarized on the cover of the book.}

\newslide{Gelman Book}

\figure{\columns{\includepng{../slides/diagrams/ml/bda_cover_1}{80%}}{\includepng{../slides/diagrams/ml/bda_cover}{80%}}{50%}{50%}}{Two different editions of Bayesian Data Analysis [@Gelman:bayesian13].}{bayesian-data-analysis}

\slides{\alignright{@Gelman:bayesian13}}

\endif
