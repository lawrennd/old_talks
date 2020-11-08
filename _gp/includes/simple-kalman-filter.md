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
		
\setupplotcode{import teaching_plots as plot}

\plotcode{plot.kronecker_illustrate(diagrams='\writeDiagramsDir/kern')}

\subsection{Kronecker Product}

\includediagram{\diagramsDir/kern/kronecker_illustrate}

\plotcode{plot.kronecker_IK(diagrams='\writeDiagramsDir/kern')}

\newslide{Kronecker Product}

\includediagram{\diagramsDir/kern/kronecker_IK}

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

gpKalmanFilterKroneckerPlot2

For this stacking the marginal distribution over *time* is given
by the block diagonals.


\setupplotcode{import teaching_plots as plot}
\plotcode{plot.kronecker_IK_highlight(diagrams='\writeDiagramsDir/kern')}

\setupdisplaycode{import pods}
\displaycode{pods.notebook.display_plots('kronecker_IK_highlighted{count:0>3}.svg', 
                            diagrams='\writeDiagramsDir/kern', count=(1,5))}

\newslide{}

\slides{
\startanimation
\includediagram{\diagramsDir/kern/kronecker_IK_highlighted001}
\includediagram{\diagramsDir/kern/kronecker_IK_highlighted002}
\includediagram{\diagramsDir/kern/kronecker_IK_highlighted003}
\includediagram{\diagramsDir/kern/kronecker_IK_highlighted004}
\includediagram{\diagramsDir/kern/kronecker_IK_highlighted005}
\endanimation
}

\notes{\figure{\includediagram{\diagramsDir/kern/kronecker_IK_highlighted005}{60%}}{}{kronecker-ik-highlighted}}


\subsection{Two Ways of Stacking

Can also stack each row of $\inputMatrix$ to form
column vector: $$\inputVector= \begin{bmatrix}
      \inputVector_{1, :}\\
      \inputVector_{2, :}\\
      \vdots\\
      \inputVector_{T, :}
    \end{bmatrix}$$
$$p(\inputVector) = \gaussianDist{\inputVector}{\zerosVector}{\kernelMatrix\otimes \eye}$$

\subsection{Row Stacking

gpKalmanFilterKroneckerPlot3

\
For this stacking the marginal distribution over the latent
*dimensions* is given by the block diagonals.

\plotcode{plot.kronecker_IK_highlight(reverse=True, diagrams='\writeDiagramsDir/kern')}

\displaycode{pods.notebook.display_plots('kronecker_KI_highlighted{count:0>3}.svg', '\writeDiagramsDir/kern', count=(1,5))}

\plotcode{plot.kronecker_IK(reverse=True, diagrams='\writeDiagramsDir/kern')}

\newslide{}

\startanimation
\includediagram{\diagramsDir/kern/kronecker_KI_highlighted001}
\includediagram{\diagramsDir/kern/kronecker_KI_highlighted002}
\includediagram{\diagramsDir/kern/kronecker_KI_highlighted003}
\includediagram{\diagramsDir/kern/kronecker_KI_highlighted004}
\includediagram{\diagramsDir/kern/kronecker_KI_highlighted005}
\endanimation

\figure{\includediagram{\diagramsDir/kern/kronecker_KI_highlighted005}{60%}}{}{kronecker-ki-highlighted}


\subsection{Mapping from Latent Process to Observed}

\includediagram{\diagramsDir/kern/kronecker_KI}

gpKalmanFilterKroneckerPlot4


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

\setupplotcode{import teaching_plots as plot}
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
