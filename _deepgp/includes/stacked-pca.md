\ifndef{stackedPca}
\define{stackedPca}
\editme

\subsection{Stacked PCA}

\setupplotcode{import mlai.plot as plot}
\plotcode{plot.stack_gp_sample(kernel=GPy.kern.Linear,
                     diagrams="\writeDiagramsDir/deepgp")}

\setupdisplaycode{import notutils as nu}
\setupdisplaycode{import notutils as nu}
\displaycode{nu.display_plots('stack-gp-sample-Linear-{sample:0>1}.svg', 
                            directory='\writeDiagramsDir/deepgp', sample=(0,4))}


\slides{
\define{\width}{10%}
\startanimation{stack-pca-sample}{0}{4}
\newframe{\includediagram{\diagramsDir/stack-pca-sample-0}{\width}}{stack-pca-sample}
\newframe{\includediagram{\diagramsDir/stack-pca-sample-1}{\width}}{stack-pca-sample}
\newframe{\includediagram{\diagramsDir/stack-pca-sample-2}{\width}}{stack-pca-sample}
\newframe{\includediagram{\diagramsDir/stack-pca-sample-3}{\width}}{stack-pca-sample}
\newframe{\includediagram{\diagramsDir/stack-pca-sample-4}{\width}}{stack-pca-sample}
\endanimation
}

\notes{\figure{\includediagram{\diagramsDir/stack-pca-sample-4}{20%}}{Composition of linear functions just leads to a new linear function. Here you see the result of multiple affine transformations applied to a square in two dimensions.}{stack-pca-sample}}

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
