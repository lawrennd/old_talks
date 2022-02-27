\ifndef{deepGp}
\define{deepGp}

\editme

\subsection{Bottleneck Layers in Deep Neural Networks}

\setupplotcode{import mlai.plot as plot}
\plotcode{plot.deep_nn_bottleneck(diagrams='\writeDiagramsDir/deepgp')}


\slides{
\includediagram{\diagramsDir/deepgp/deep-nn-bottleneck1}{60%}
}

\newslide{Deep Neural Network}

\slides{
\includediagram{\diagramsDir/deepgp/deep-nn-bottleneck2}{60%}
}

\notes{\figure{\includediagram{\diagramsDir/deepgp/deep-nn-bottleneck2}{70%}}{Inserting the bottleneck layers introduces a new set of variables.}{deep-nn-bottleneck}}

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

\newslide{A Cascade of Neural Networks}

$$
\begin{align}
  \latentVector_{1} &= \eigenvectwoMatrix^\top_1 \inputVector\\
  \latentVector_{2} &= \eigenvectwoMatrix^\top_2 \basisFunction\left(\eigenvectorMatrix_1 \latentVector_{1}\right)\\
  \latentVector_{3} &= \eigenvectwoMatrix^\top_3 \basisFunction\left(\eigenvectorMatrix_2 \latentVector_{2}\right)\\
  \dataVector &= \mappingVector_4 ^\top \latentVector_{3}
\end{align}
$$

talk-macros.gpp}eepgp/includes/cascade-of-gps.md}

\endif
