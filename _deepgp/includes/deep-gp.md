\setupcode{import teaching_plots as plot}
\plotcode{plot.deep_nn_bottleneck(diagrams='../slides/diagrams/deepgp')}

\slides{
### Deep Neural Network

\includesvg{../slides/diagrams/deepgp/deep-nn-bottleneck1.svg}

### Deep Neural Network

\includesvg{../slides/diagrams/deepgp/deep-nn-bottleneck2.svg}
}

\notesfigure{\includesvg{../slides/diagrams/deepgp/deep-nn-bottleneck2.svg}}

\newslide{Mathematically}
\notes{Including the low rank decomposition of $\mappingMatrix$ in the neural network, we obtain a new mathematical form. Effectively, we are adding additional *latent* layers, $\latentVector$, in between each of the existing hidden layers. In a neural network these are sometimes known as *bottleneck* layers.} The network can now be written mathematically as
$$
\begin{align}
  \latentVector_{1} &= \eigenvectwoMatrix^\top_1 \inputVector\\
  \hiddenVector_{1} &= \basisFunction\left(\eigenvectorMatrix_1 \latentVector_{1}\right)\\
  \latentVector_{2} &= \eigenvectwoMatrix^\top_2 \hiddenVector_{1}\\
  \hiddenVector_{2} &= \basisFunction\left(\eigenvectorMatrix_2 \latentVector_{2}\right)\\
  \latentVector_{3} &= \eigenvectwoMatrix^\top_3 \hiddenVector_{2}\\
  \hiddenVector_{3} &= \basisFunction\left(\eigenvectorMatrix_3 \latentVector_{3}\right)\\
  \dataVector &= \mappingVector_4^\top\hiddenVector_{3}.
\end{align}
$$

### A Cascade of Neural Networks

$$
\begin{align}
  \latentVector_{1} &= \eigenvectwoMatrix^\top_1 \inputVector\\
  \latentVector_{2} &= \eigenvectwoMatrix^\top_2 \basisFunction\left(\eigenvectorMatrix_1 \latentVector_{1}\right)\\
  \latentVector_{3} &= \eigenvectwoMatrix^\top_3 \basisFunction\left(\eigenvectorMatrix_2 \latentVector_{2}\right)\\
  \dataVector &= \mappingVector_4 ^\top \latentVector_{3}
\end{align}
$$

### Cascade of Gaussian Processes

* Replace each neural network with a Gaussian process
$$
\begin{align}
  \latentVector_{1} &= \mappingFunctionVector_1\left(\inputVector\right)\\
  \latentVector_{2} &= \mappingFunctionVector_2\left(\latentVector_{1}\right)\\
  \latentVector_{3} &= \mappingFunctionVector_3\left(\latentVector_{2}\right)\\
  \dataVector &= \mappingFunctionVector_4\left(\latentVector_{3}\right)
\end{align}
$$

* Equivalent to prior over parameters, take width of each layer to infinity.
