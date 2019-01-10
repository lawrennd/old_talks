\ifndef{stackedPca}
\define{stackedPca}
\editme

\setupplotcode{import teaching_plots as plot}
\plotcode{plot.stack_gp_sample(kernel=GPy.kern.Linear,
                     diagrams="../../slides/diagrams/deepgp")}

\setupdisplaycode{import pods}
\displaycode{pods.notebook.display_plots('stack-gp-sample-Linear-{sample:0>1}.svg', 
                            directory='../../slides/diagrams/deepgp', sample=(0,4))}

\subsection{Stacked PCA}
\slides{
\startanimation{stack-pca-sample}{0}{4}
\newframe{\includesvg{../slides/diagrams/stack-pca-sample-0.svg}}{stack-pca-sample}
\newframe{\includesvg{../slides/diagrams/stack-pca-sample-1.svg}}{stack-pca-sample}
\newframe{\includesvg{../slides/diagrams/stack-pca-sample-2.svg}}{stack-pca-sample}
\newframe{\includesvg{../slides/diagrams/stack-pca-sample-3.svg}}{stack-pca-sample}
\newframe{\includesvg{../slides/diagrams/stack-pca-sample-4.svg}}{stack-pca-sample}
\endanimation
}

\notesfigure{\includesvg{../slides/diagrams/stack-pca-sample-4.svg}}
\notes{\caption{Composition of linear functions just leads to a new linear function.}}

\notes{Stacking a series of linear functions simply leads to a new linear function. The use of multiple linear function merely changes the covariance of the resulting Gaussian. If
$$
\latentMatrix \sim \gaussianSamp{\zerosVector}{\eye}
$$
and the $i$th hidden layer is a multivariate linear transformation defined by $\weightMatrix_i$,
$$
\dataMatrix = \latentMatrix\weightMatrix_1 \weightMatrix_2 \dots \weightMatrix_\numLayers
$$
then the rules of multivariate Gaussians tell us that
$$
\dataMatrix \sim \gaussianSamp{\zerosVector}{\weightMatrix_\numLayers \dots \weightMatrix_1 \weightMatrix^\top_1 \dots \weightMatrix^\top_\numLayers}.
$$
So the model can be replaced by one where we set $\vMatrix = \weightMatrix_\numLayers \dots \weightMatrix_2 \weightMatrix_1$. So is such a model trivial? The answer is that it depends. There are two cases in which such a model remaisn interesting. Firstly, if we make intermediate observations stemming from the chain. So, for example, if we decide that,
$$
\latentMatrix_i = \weightMatrix_i \latentMatrix_{i-1}
$$
and set $\latentMatrix_{0} = \inputMatrix \sim \gaussianSamp{\zerosVector}{\eye}$, then the matrices $\weightMatrix$ inter-relate a series of jointly Gaussian observations in an interesting way, stacking the full data matrix to give
$$
\latentMatrix = \begin{bmatrix}
\latentMatrix_0 \\
\latentMatrix_1 \\
\vdots \\
\latentMatrix_\numLayers
\end{bmatrix}
$$
we can obtain
$$\latentMatrix \sim \gaussianSamp{\zerosVector}{\begin{bmatrix}
\eye & \weightMatrix^\top_1 & \weightMatrix_1^\top\weightMatrix_2^\top & \dots & \vMatrix^\top \\
\weightMatrix_1 & \weightMatrix_1 \weightMatrix_1^\top & \weightMatrix_1 \weightMatrix_1^\top \weightMatrix_2^\top & \dots & \weightMatrix_1 \vMatrix^\top \\
\weightMatrix_2 \weightMatrix_1 & \weightMatrix_2 \weightMatrix_1 \weightMatrix_1^\top & \weightMatrix_2 \weightMatrix_1 \weightMatrix_1^\top \weightMatrix_2^\top & \dots & \weightMatrix_2 \weightMatrix_1 \vMatrix^\top \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
\vMatrix & \vMatrix   \weightMatrix_1^\top  & \vMatrix \weightMatrix_1^\top \weightMatrix_2^\top& \dots & \vMatrix\vMatrix^\top
\end{bmatrix}}$$
which is a highly structured Gaussian covariance with hierarchical dependencies between the variables $\latentMatrix_i$. 
}



\endif
