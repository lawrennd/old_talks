\ifndef{simpleKalmanFilter}
\define{simpleKalmanFilter}

\editme

\subsection{Simple Kalman Filter}

-   We have state vector
    $\inputMatrix = \left[\inputVector_1
          \dots \inputVector_\latentDim\right] \in \mathbb{R}^{T \times \latentDim}$
    and if each state evolves independently we have 
$$		
\begin{align*}
  p(\inputMatrix) &= \prod_{i=1}^\latentDim p(\inputVector_{:, i}) \\
     p(\inputVector_{:, i}) &= \gaussianDist{\inputVector_{:, i}}{\zerosVector}{\kernelMatrix}.
\end{align*}
$$

-   We want to obtain outputs through:
    $$
	\dataVector_{i, :} = \mappingMatrix\inputVector_{i, :}
	$$

\subsection{Stacking and Kronecker Products}

-   Represent with a ‘stacked’ system:
$$
p(\inputVector) = \gaussianDist{\inputVector}{\zerosVector}{\eye \otimes \kernelMatrix}
$$
where the stacking is placing each column of $\inputMatrix$ one on top of another as
$$
\inputVector= \begin{bmatrix}
          \inputVector_{:, 1}\\
          \inputVector_{:, 2}\\
          \vdots\\
          \inputVector_{:, \latentDim}
        \end{bmatrix}
$$
		

\subsection{Kronecker Product}

\setupplotcode{import mlai.plot as plot}
\plotcode{plot.kronecker_illustrate(diagrams='\writeDiagramsDir/kern')}

\figure{\includediagram{\diagramsDir/kern/kronecker_illustrate}{80%}}{Illustration of the Kronecker product.}{kronecker-illustrate}


\newslide{Kronecker Product}

\plotcode{plot.kronecker_IK(diagrams='\writeDiagramsDir/kern')}

\figure{\includediagram{\diagramsDir/kern/kronecker_IK}{80%}}{Kronecker product between two matrices.}{kronecker-ik}

\subsection{Stacking and Kronecker Products}

-   Represent with a ‘stacked’ system:
    $$p
	(\inputVector) = \gaussianDist{\inputVector}{\zerosVector}{\eye\otimes \kernelMatrix}
	$$
    where the stacking is placing each column of
    $\inputMatrix$ one on top of another as
    $$
	\inputVector= \begin{bmatrix}
          \inputVector_{:, 1}\\
          \inputVector_{:, 2}\\
          \vdots\\
          \inputVector_{:, \latentDim}
        \end{bmatrix}
		$$
		
\subsection{Column Stacking}

\matlabcode{gpKalmanFilterKroneckerPlot2}

For this stacking the marginal distribution over *time* is given
by the block diagonals.

\setupplotcode{import mlai.plot as plot}
\plotcode{plot.kronecker_IK_highlight(diagrams='\writeDiagramsDir/kern')}

\setupdisplaycode{import notutils as nu}
\displaycode{nu.display_plots('kronecker_IK_highlighted{count:0>3}.svg', 
                 directory='\writeDiagramsDir/kern', count=(1,5))}

\newslide{}

\slides{
\define{width}{80%}
\startanimation{kronecker-IK-highlighted}{0}{5}
\newframe{\includediagram{\diagramsDir/kern/kronecker_IK_highlighted001}{\width}}{kronecker-IK-highlighted}
\newframe{\includediagram{\diagramsDir/kern/kronecker_IK_highlighted002}{\width}}{kronecker-IK-highlighted}
\newframe{\includediagram{\diagramsDir/kern/kronecker_IK_highlighted003}{\width}}{kronecker-IK-highlighted}
\newframe{\includediagram{\diagramsDir/kern/kronecker_IK_highlighted004}{\width}}{kronecker-IK-highlighted}
\newframe{\includediagram{\diagramsDir/kern/kronecker_IK_highlighted005}{\width}}{kronecker-IK-highlighted}
\endanimation
}

\notes{\figure{\includediagram{\diagramsDir/kern/kronecker_IK_highlighted005}{60%}}{The marginal distribution for the first three variables (highlighted) is givne by $\kernelMatrix$ when the form of stacking is $\eye \otimes \kernelMatrix$. This is the 'column stacking' case.}{kronecker-ik-highlighted}}


\subsection{Two Ways of Stacking}

Can also stack each row of $\inputMatrix$ to form
column vector: $$\inputVector= \begin{bmatrix}
      \inputVector_{1, :}\\
      \inputVector_{2, :}\\
      \vdots\\
      \inputVector_{T, :}
    \end{bmatrix}$$
$$p(\inputVector) = \gaussianDist{\inputVector}{\zerosVector}{\kernelMatrix\otimes \eye}$$

\subsection{Row Stacking}

\matlabcode{gpKalmanFilterKroneckerPlot3}

For this stacking the marginal distribution over the latent
*dimensions* is given by the block diagonals.

\plotcode{plot.kronecker_IK_highlight(reverse=True, diagrams='\writeDiagramsDir/kern')}
\setupdisplaycode{import notutils as nu}

\displaycode{nu.display_plots('kronecker_KI_highlighted{count:0>3}.svg', directory='\writeDiagramsDir/kern', count=(1,5))}

\plotcode{plot.kronecker_IK(reverse=True, diagrams='\writeDiagramsDir/kern')}

\newslide{}

\slides{
\define{width}{80%}
\startanimation{kronecker-ki-highlighted}{1}{5}
\newframe{\includediagram{\diagramsDir/kern/kronecker_KI_highlighted001}{\width}}{kronecker-ki-highlighted}
\newframe{\includediagram{\diagramsDir/kern/kronecker_KI_highlighted002}{\width}}{kronecker-ki-highlighted}
\newframe{\includediagram{\diagramsDir/kern/kronecker_KI_highlighted003}{\width}}{kronecker-ki-highlighted}
\newframe{\includediagram{\diagramsDir/kern/kronecker_KI_highlighted004}{\width}}{kronecker-ki-highlighted}
\newframe{\includediagram{\diagramsDir/kern/kronecker_KI_highlighted005}{\width}}{kronecker-ki-highlighted}
\endanimation
}

\notes{\figure{\includediagram{\diagramsDir/kern/kronecker_KI_highlighted002}{60%}}{The marginal distribution for the first three variables (highlighted) is independent when the form of stacking is $\kernelMatrix \otimes \eye$. This is the 'row stacking' case.}{kronecker-ki-highlighted}}


\subsection{Mapping from Latent Process to Observed}

\figure{\includediagram{\diagramsDir/kern/kronecker_KI}{60%}}{Mapping from latent process to observed}{kronecker-ki}

\matlabcode{gpKalmanFilterKroneckerPlot4}

\subsection{Observed Process}

The observations are related to the latent points by a linear mapping
matrix,
$$
\dataVector_{i, :} = \mappingMatrix\inputVector_{i, :} + \noiseVector_{i, :}
$$
$$
\noiseVector \sim \gaussianSamp{\zerosVector}{\dataStd^2\eye}
$$

\newslide{}

\setupplotcode{import mlai.plot as plot}
\plotcode{plot.kronecker_WX(diagrams='\writeDiagramsDir/kern')}

\figure{\includediagram{\diagramsDir/kern/kronecker_WX}{60%}}{}{kronecker-wx}

\subsection{Output Covariance}

This leads to a covariance of the form
$$
(\eye\otimes \mappingMatrix) (\kernelMatrix \otimes \eye) (\eye \otimes \mappingMatrix^\top) + \eye\dataStd^2
$$
Using
$(\mathbf{A}\otimes\mathbf{B}) (\mathbf{C}\otimes\mathbf{D}) = \mathbf{A}\mathbf{C} \otimes \mathbf{B}\mathbf{D}$
This leads to
$$
\kernelMatrix\otimes {\mappingMatrix}{\mappingMatrix}^\top + \eye\dataStd^2
$$
or
$$
\dataVector\sim \gaussianSamp{\zerosVector}{\mappingMatrix\mappingMatrix^\top \otimes \kernelMatrix + \eye\dataStd^2}
$$

\endif
