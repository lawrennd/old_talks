\ifndef{pcaOtherDataSets}
\define{pcaOtherDataSets}

\editme

\subsection{Other Data Sets to Explore}

Below there are a few other data sets from `pods` you might want to explore with PCA. Both of them have $p$>$n$ so you need to consider how to do the larger eigenvalue probleme efficiently without large demands on computer memory.

The data is actually quite high dimensional, and solving the eigenvalue problem in the high dimensional space can take some time. At this point we turn to a neat trick, you don't have to solve the full eigenvalue problem in the $\dataDim\times \dataDim$ covariance, you can choose instead to solve the related eigenvalue problem in the $\numData \times \numData$ space, and in this case $\numData=200$ which is much smaller than $\dataDim$.

The original eigenvalue problem has the form
$$
\dataMatrix^\top\dataMatrix \mathbf{U} = \mathbf{U}\boldsymbol{\Lambda}
$$
But if we premultiply by $\dataMatrix$ then we can solve,
$$
\dataMatrix\dataMatrix^\top\dataMatrix \mathbf{U} = \dataMatrix\mathbf{U}\boldsymbol{\Lambda}
$$
but it turns out that we can write
$$
\mathbf{U}^\prime = \dataMatrix \mathbf{U} \Lambda^{\frac{1}{2}}
$$
where $\mathbf{U}^\prime$ is an orthorormal matrix because
$$
\left.\mathbf{U}^\prime\right.^\top\mathbf{U}^\prime = \Lambda^{-\frac{1}{2}}\mathbf{U}\dataMatrix^\top\dataMatrix \mathbf{U} \Lambda^{-\frac{1}{2}}
$$
and since $\mathbf{U}$ diagonalises $\dataMatrix^\top\dataMatrix$, 
$$
\mathbf{U}\dataMatrix^\top\dataMatrix \mathbf{U} = \Lambda
$$
then 
$$
\left.\mathbf{U}^\prime\right.^\top\mathbf{U}^\prime = \eye
$$

talk-macros.gpp}imred/includes/olivetti-eigenfaces.md}
talk-macros.gpp}imred/includes/spellman-eigengenes.md}

\endif
