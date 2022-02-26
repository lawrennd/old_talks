\ifndef{overdeterminedSystem}
\define{overdeterminedSystem}

\editme

\subsection{Overdetermined System}

\notes{The challenge with a linear model is that it has two unknowns, $m$, and $c$. Observing data allows us to write down a system of simultaneous linear equations. So, for example if we observe two data points, the first with the input value, $\inputScalar_1 = 1$ and the output value, $\dataScalar_1 =3$ and a second data point, $\inputScalar = 3$, $\dataScalar=1$, then we can write two simultaneous linear equations of the form. 

point 1: $\inputScalar = 1$, $\dataScalar=3$
$$
3 = m + c
$$
point 2: $\inputScalar = 3$, $\dataScalar=1$
$$
1 = 3m + c
$$

The solution to these two simultaneous equations can be represented graphically as}

\notes{\figure{\includediagram{\diagramsDir/ml/over_determined_system003}{40%}}{The solution of two linear equations represented as the fit of a straight line through two data}{over-determined-system-3}}

\notes{
The challenge comes when a third data point is observed, and it doesn't fit on the straight line. 

point 3: $\inputScalar = 2$, $\dataScalar=2.5$
$$
2.5 = 2m + c
$$
}

\notes{\figure{\includediagram{\diagramsDir/ml/over_determined_system004}{40%}}{A third observation of data is inconsistent with the solution dictated by the first two observations}{over-determined-system-4}}

\notes{Now there are three candidate lines, each consistent with our data.}

\notes{\figure{\includediagram{\diagramsDir/ml/over_determined_system007}{40%}}{Three solutions to the problem, each consistent with two points of the three observations}{over-determined-system-7}}

\notes{This is known as an *overdetermined* system because there are more data than we need to determine our parameters. The problem arises because the model is a simplification of the real world, and the data we observe is therefore inconsistent with our model.}


\newslide{}

\setupplotcode{import mlai.plot}
\plotcode{plot.over_determined_system(diagrams='\writeDiagramsDir/ml')}

\setupdisplaycode{from ipywidgets import IntSlider
import notutils as nu}
\displaycode{nu.display_plots('over_determined_system{samp:0>3}.svg',
                  directory='\writeDiagramsDir/ml', 
                  samp=IntSlider(1,1,7,1))}

\slides{
\define{\width}{40%}
\startanimation{over_determined_system}{1}{8}
\newframe{\includediagram{\diagramsDir/ml/over_determined_system001}{\width}}{over_determined_system}
\newframe{\includediagram{\diagramsDir/ml/over_determined_system002}{\width}}{over_determined_system}
\newframe{\includediagram{\diagramsDir/ml/over_determined_system003}{\width}}{over_determined_system}
\newframe{\includediagram{\diagramsDir/ml/over_determined_system004}{\width}}{over_determined_system}
\newframe{\includediagram{\diagramsDir/ml/over_determined_system005}{\width}}{over_determined_system}
\newframe{\includediagram{\diagramsDir/ml/over_determined_system006}{\width}}{over_determined_system}
\newframe{\includediagram{\diagramsDir/ml/over_determined_system007}{\width}}{over_determined_system}
\endanimation
}


\newslide{$\dataScalar = m\inputScalar + c$}
\slides{

. . . 

point 1: $\inputScalar = 1$, $\dataScalar=3$
$$
3 = m + c
$$

. . .

point 2: $\inputScalar = 3$, $\dataScalar=1$
$$
1 = 3m + c
$$

. . . 

point 3: $\inputScalar = 2$, $\dataScalar=2.5$
$$
2.5 = 2m + c
$$}

\endif
