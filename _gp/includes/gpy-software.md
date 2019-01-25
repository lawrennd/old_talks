\ifndef{gpySoftware}
\define{gpySoftware}
\editme

\subsection{GPy: A Gaussian Process Framework in Python}

\includepng{../slides/diagrams/gp/gpy}{70%}

\slides{\aligncenter{<https://github.com/SheffieldML/GPy>}}

\newslide{GPy: A Gaussian Process Framework in Python}

\slides{
* BSD Licensed software base.
* Wide availability of libraries, 'modern' scripting language.
* Allows us to set projects to undergraduates in Comp Sci that use GPs.
* Available through GitHub
  <https://github.com/SheffieldML/GPy>
* Reproducible Research with Jupyter Notebook.
}
\notes{GPy is a BSD licensed software code base for implementing Gaussian process models in python. This allows GPs to be combined with a wide variety of software libraries. 

The software itself is available on [GitHub](https://github.com/SheffieldML/GPy) and the team welcomes contributions.}

\newslide{Features}

\slides{
* Probabilistic-style programming (specify the model, not the algorithm).
* Non-Gaussian likelihoods.
* Multivariate outputs.
* Dimensionality reduction.
* Approximations for large data sets.
}

\notes{The aim for GPy is to be a probabilistic-style programming language, i.e. you specify the model rather than the algorithm. As well as a large range of covariance functions the software allows for non-Gaussian likelihoods, multivariate outputs, dimensionality reduction and approximations for larger data sets.}

\endif
