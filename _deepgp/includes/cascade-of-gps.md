\ifndef{cascadeOfGps}
\define{cascadeOfGps}

\editme

\subsection{Cascade of Gaussian Processes}

\notes{Now if we replace each of these neural networks with a Gaussian process. This is equivalent to taking the limit as the width of each layer goes to infinity, while appropriately scaling down the outputs.}
\slides{* Replace each neural network with a Gaussian process}
$$
\begin{align}
  \latentVector_{1} &= \mappingFunctionVector_1\left(\inputVector\right)\\
  \latentVector_{2} &= \mappingFunctionVector_2\left(\latentVector_{1}\right)\\
  \latentVector_{3} &= \mappingFunctionVector_3\left(\latentVector_{2}\right)\\
  \dataVector &= \mappingFunctionVector_4\left(\latentVector_{3}\right)
\end{align}
$$

\slides{* Equivalent to prior over parameters, take width of each layer to infinity.}

\endif
