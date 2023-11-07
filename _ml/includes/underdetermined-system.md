\ifndef{underdeterminedSystem}
\define{underdeterminedSystem}
\editme

\section{Underdetermined System}

\setupplotcode{import mlai.plot as plot}
\plotcode{plot.under_determined_system(diagrams='\writeDiagramsDir/ml')}

\notes{What about the situation where you have more parameters than data in your simultaneous equation? This is known as an *underdetermined* system. In fact, this set up is in some sense *easier* to solve, because we don't need to think about introducing a slack variable (although it might make a lot of sense from a *modelling* perspective to do so).

The way Laplace proposed resolving an  overdetermined system, was to introduce slack variables, $\noiseScalar_i$, which needed to be estimated for each point. The slack variable represented the difference between our actual prediction and the true observation. This is known as the *residual*. By introducing the slack variable, we now have an additional $n$ variables to estimate, one for each data point, $\{\noiseScalar_i\}$. This turns the overdetermined system into an underdetermined system. Introduction of $n$ variables, plus the original $m$ and $c$ gives us $\numData+2$ parameters to be estimated from $n$ observations, which makes the system *underdetermined*. However, we then made a probabilistic assumption about the slack variables, we assumed that the slack variables were distributed according to a probability density. And for the moment we have been assuming that density was the Gaussian, 
$$\noiseScalar_i \sim \gaussianSamp{0}{\dataStd^2},$$ 
with zero mean and variance $\dataStd^2$. }

\notes{The follow up question is whether we can do the same thing with the parameters. If we have two parameters and only one unknown, can we place a probability distribution over the parameters as we did with the slack variables? The answer is yes.}


\newslide{Underdetermined System}
\slides{
* What about two unknowns and *one* observation?
  $$\dataScalar_1 =  m\inputScalar_1 + c$$

. . .

Can compute $m$ given $c$. 
$$m = \frac{\dataScalar_1 - c}{\inputScalar}$$
}

\subsection{Underdetermined System}

\setupdisplaycode{import notutils as nu
from ipywidgets import IntSlider}
\displaycode{nu.display_plots('under_determined_system{samp:0>3}.svg', 
                 directory='\writeDiagramsDir/ml', samp=IntSlider(0, 0, 9, 1))}

\slides{
\define{width}{40%}
\startanimation{under_determined_system}{0}{9}
\newframe{\includediagram{\diagramsDir/ml/under_determined_system000}{\width}}{under_determined_system}
\newframe{\includediagram{\diagramsDir/ml/under_determined_system001}{\width}}{under_determined_system}
\newframe{\includediagram{\diagramsDir/ml/under_determined_system002}{\width}}{under_determined_system}
\newframe{\includediagram{\diagramsDir/ml/under_determined_system003}{\width}}{under_determined_system}
\newframe{\includediagram{\diagramsDir/ml/under_determined_system004}{\width}}{under_determined_system}
\newframe{\includediagram{\diagramsDir/ml/under_determined_system005}{\width}}{under_determined_system}
\newframe{\includediagram{\diagramsDir/ml/under_determined_system006}{\width}}{under_determined_system}
\newframe{\includediagram{\diagramsDir/ml/under_determined_system007}{\width}}{under_determined_system}
\newframe{\includediagram{\diagramsDir/ml/under_determined_system008}{\width}}{under_determined_system}
\newframe{\includediagram{\diagramsDir/ml/under_determined_system009}{\width}}{under_determined_system}
\endanimation
}

\notes{\figure{\includediagram{\diagramsDir/ml/under_determined_system009}{40%}}{An underdetermined system can be fit by considering uncertainty. Multiple solutions are consistent with one specified point.}{under-determined-system-9}}

\endif
