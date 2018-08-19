\setupcode{import teaching_plots as plot}
\plotcode{plot.deep_nn(diagrams='../slides/diagrams/deepgp/')}

\slides{
### Deep Neural Network

\includesvg{../slides/diagrams/deepgp/deep-nn1.svg}

### Deep Neural Network

\includesvg{../slides/diagrams/deepgp/deep-nn2.svg}
}
\notesfigure{\includesvg{../slides/diagrams/deepgp/deep-nn2.svg}}
\notes{\caption{A deep neural network. Input nodes are shown at the bottom. Each hidden layer is the result of applying an affine transformation to the previous layer and placing through an activation function.}}

\newslide{Mathematically}

\notes{Mathematically, each layer of a neural network is given through computing the activation function, $\basisFunction(\cdot)$, contingent on the previous layer, or the inputs. In this way the activation functions, are composed to generate more complex interactions than would be possible with any single layer.}
$$
\begin{align}
    \hiddenVector_{1} &= \basisFunction\left(\mappingMatrix_1 \inputVector\right)\\
    \hiddenVector_{2} &=  \basisFunction\left(\mappingMatrix_2\hiddenVector_{1}\right)\\
    \hiddenVector_{3} &= \basisFunction\left(\mappingMatrix_3 \hiddenVector_{2}\right)\\
    \dataVector &= \mappingVector_4 ^\top\hiddenVector_{3}
\end{align}
$$
