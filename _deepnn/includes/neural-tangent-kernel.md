\ifndef{neuralTangentKernel}
\define{neuralTangentKernel}

\editme

\subsection{Neural Tangent Kernel}

\slides{* Consider very wide neural networks.
* Consider particular initialisation.
* Deep neural network is regularising with a particular *kernel*.
* This is known as the neural tangent kernel [@Jacot-ntk18].
}

\notes{Another approach to analysis exploits the fact that optimization is occurring in a very high dimensional parameter space. By considering initializations that involve small random weights (known as the NTK initialization) and noting that small updates in the learning mean that the model doesn't move far from this initialization [@Jacot-ntk18].}

\notes{For very wide neural networks, when these conditions are fulfilled, the network can be approximately represented by a *kernel* known as the neural tangent kernel. A kernel is a regularizer that operates in *function space* rather than *feature space*.}

\endif
