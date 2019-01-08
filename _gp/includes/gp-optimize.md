\define{\blueColor}{yellow}
\define{\redColor}{cyan}
\define{\magentaColor}{green}
\code{gpoptimizeInit}

\newslide{Learning Covariance Parameters}

Can we determine covariance parameters from the data?

\newslide{}

$$\gaussianDist{\dataVector}{\mathbf{0}}{\kernelMatrix}=\frac{1}{(2\pi)^\frac{\numData}{2}{\det{\kernelMatrix}^{\frac{1}{2}}}}{\exp\left(-\frac{\dataVector^{\top}\kernelMatrix^{-1}\dataVector}{2}\right)}$$

\newslide{}
$$\begin{aligned}
    \gaussianDist{\dataVector}{\mathbf{0}}{\kernelMatrix}=\frac{1}{(2\pi)^\frac{\numData}{2}{\color{\blueColor} \det{\kernelMatrix}^{\frac{1}{2}}}}{\color{\redColor}\exp\left(-\frac{\dataVector^{\top}\kernelMatrix^{-1}\dataVector}{2}\right)}
    \end{aligned}$$ 

\newslide{}

$$\begin{aligned}
    \log \gaussianDist{\dataVector}{\mathbf{0}}{\kernelMatrix}=&{\color{\blueColor}-\frac{1}{2}\log\det{\kernelMatrix}}{\color{\redColor}-\frac{\dataVector^{\top}\kernelMatrix^{-1}\dataVector}{2}} \\ &-\frac{\numData}{2}\log2\pi
    \end{aligned}$$ \onslide<4>
$$\errorFunction(\parameterVector) = {\color{\blueColor} \frac{1}{2}\log\det{\kernelMatrix}} + {\color{\redColor} \frac{\dataVector^{\top}\kernelMatrix^{-1}\dataVector}{2}}$$

\newslide{}

The parameters are *inside* the covariance function (matrix).
\normalsize
$$\kernelScalar_{i, j} = \kernelScalar(\inputVals_i, \inputVals_j; \parameterVector)$$


\newslide{Eigendecomposition of Covariance}

[\Large
$$\kernelMatrix = \rotationMatrix \eigenvalueMatrix^2 \rotationMatrix^\top$$]{}

\code{gpoptimizePlot1}

\columns{\includepng{../slides/diagrams/gp/gp-optimize-eigen}{100%}{negate}}{$\eigenvalueMatrix$ represents distance on axes.
$\rotationMatrix$ gives rotation.}{50%}{50%}


\newslide{Eigendecomposition of Covariance}

$\eigenvalueMatrix$ is *diagonal*, $\rotationMatrix^\top\rotationMatrix = \eye$. 
Useful representation since $\det{\kernelMatrix} = \det{\eigenvalueMatrix^2} = \det{\eigenvalueMatrix}^2$.

\newslide{Capacity control: ${\color{\blueColor} \log \det{\kernelMatrix}}$}

\code{gpoptimizePlot2}


\only<1>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseDeterminant1}}\only<2>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseDeterminant2}}\only<3>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseDeterminant3}}\only<4>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseDeterminant4}}\only<5>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseDeterminant5}}\only<6>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseDeterminant6}}\only<7>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseDeterminant7}}\only<8>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseDeterminant8}}\only<9>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseDeterminant9}}\only<10>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseDeterminant10}}

\newslide{Data Fit: ${\color{\redColor} \frac{\dataVector^\top\kernelMatrix^{-1}\dataVector}{2}}$}

\code{gpoptimizePlot3}

\only<1>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseQuadratic1}}\only<2>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseQuadratic2}}\only<3>{\inputdiagram{../../../gp/tex/diagrams/gpOptimiseQuadratic3}}

\newslide{Learning Covariance Parameters}

Can we determine length scales and noise levels from the data?

\code{gpoptimizePlot4}

\only<1>{\inputdiagram{../../../gp/tex/diagrams/gpOptimise1}\hfill}\only<1>{\inputdiagram{../../../gp/tex/diagrams/gpOptimise2}}\only<2>{\inputdiagram{../../../gp/tex/diagrams/gpOptimise3}\hfill}\only<2>{\inputdiagram{../../../gp/tex/diagrams/gpOptimise4}}\only<3>{\inputdiagram{../../../gp/tex/diagrams/gpOptimise5}\hfill}\only<3>{\inputdiagram{../../../gp/tex/diagrams/gpOptimise6}}\only<4>{\inputdiagram{../../../gp/tex/diagrams/gpOptimise7}\hfill}\only<4>{\inputdiagram{../../../gp/tex/diagrams/gpOptimise8}}\only<5>{\inputdiagram{../../../gp/tex/diagrams/gpOptimise9}\hfill}\only<5>{\inputdiagram{../../../gp/tex/diagrams/gpOptimise10}}\only<6>{\inputdiagram{../../../gp/tex/diagrams/gpOptimise11}\hfill}\only<6>{\inputdiagram{../../../gp/tex/diagrams/gpOptimise12}}\only<7>{\inputdiagram{../../../gp/tex/diagrams/gpOptimise13}\hfill}\only<7>{\inputdiagram{../../../gp/tex/diagrams/gpOptimise14}}\only<8>{\inputdiagram{../../../gp/tex/diagrams/gpOptimise15}\hfill}\only<8>{\inputdiagram{../../../gp/tex/diagrams/gpOptimise16}}\only<9>{\inputdiagram{../../../gp/tex/diagrams/gpOptimise17}\hfill}\only<9>{\inputdiagram{../../../gp/tex/diagrams/gpOptimise18}}

$$\errorFunction(\parameterVector) = {\color{\blueColor}\frac{1}{2}\log\det{\kernelMatrix}}+{\color{\redColor}\frac{\dataVector^{\top}\kernelMatrix^{-1}\dataVector}{2}}$$

