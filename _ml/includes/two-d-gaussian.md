\subsection{Two Dimensional Gaussian}
\slides{
* Consider height, $h/m$ and weight, $w/kg$.
* Could sample height from a distribution:}\notes{Consider the distribution of height (in meters) of an adult male human population. We will approximate the marginal density of heights as a Gaussian density with mean given by $1.7\text{m}$ and a standard deviation of $0.15\text{m}$, implying a variance of $\dataStd^2=0.0225$,} 
  $$
  p(h) \sim \gaussianSamp{1.7}{0.0225}.
  $$
\slides{* And similarly weight: }\notes{Similarly, we assume that weights of the population are distributed a Gaussian density with a mean of $75 \text{kg}$ and a standard deviation of $6 kg$ (implying a variance of 36),}
  $$
  p(w) \sim \gaussianSamp{75}{36}.
  $$


\newslide{Height and Weight Models}
\plotcode{import teaching_plots as plot}
\plotcode{plot.height_weight(diagrams='../slides/diagrams/ml')}

\includesvg{../slides/diagrams/ml/height_weight_gaussian.svg}

\caption{Gaussian distributions for height and weight.}


\subsection{Independence Assumption}
\slides{
* We assume height and weight are independent.}
\notes{First of all, we make an independence assumption, we assume that height and weight are independent. The definition of probabilistic independence is that the joint density, $p(w, h)$, factorizes into its marginal densities,}
  $$
  p(w, h) = p(w)p(h).
  $$
\notes{Given this assumption we can sample from the joint distribution by independently sampling weights and heights.}

\include{_ml/includes/two-d-gaussian-independent-sample.md}

\newslide{Body Mass Index}
\slides{
* In reality they are dependent (body mass index) $= \frac{w}{h^2}$.}\notes{In reality height and weight are *not* independent. Taller people tend on average to be heavier, and heavier people are likely to be taller. This is reflected by the *body mass index*. A ratio suggested by one of the fathers of statistics, Adolphe Quetelet. Quetelet was interested in the notion of the *average man* and collected various statistics about people. He defined the BMI to be,
$$
\text{BMI} = \frac{w}{h^2}
$$}\slides{
* To deal with this dependence we introduce *correlated* multivariate Gaussians.}\notes{To deal with this dependence we now introduce the notion of *correlation* to the multivariate Gaussian density.}

\include{_ml/includes/two-d-gaussian-correlated-sample.md}

\include{_ml/includes/two-d-gaussian-maths.md}
