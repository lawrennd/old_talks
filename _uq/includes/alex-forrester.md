\ifndef{alexForrester}
\define{alexForrester}

\editme

\subsection{Alex Forrester}

\centerdiv{\circleHead{\diagramsDir/people/alex-forrester.jpg}{Alex Forrester}{15%}{https://www.southampton.ac.uk/engineering/research/groups/performance-sports/staff-profiles/alexander-forrester.page}}

\notes{We're going to make use of the Forrester function in our example below, a function developed as a demonstrator by [Alex Forrester](https://www.southampton.ac.uk/engineering/research/groups/performance-sports/staff-profiles/alexander-forrester.page). Alex is a design engineer who makes extensive use of surrogate modelling in Engineering design. 

You can see Alex talking about the use of Gaussian process surrogates [in this online video lecture](http://videolectures.net/mla09_forrester_sbcmoo/).}

\figure{\includeyoutube{2ngc2aw9xYs}{600}{450}}{A kinematic simulation of the human body doing breaststroke that Alex uses as part of his work in optimization of human motion during sports.}{kinematic-human-simulation}

\newslide{The Forrester Function}

\notes{The Forrester function [@Forrester-engineering08] is commonly used as a demonstrator function in surrogate modelling. It has the form}
$$
f(x) = (6x-2)^2\sin(12 x-4).
$$

\setupcode{import numpy as np}

\code{x = np.linspace(0, 1, 100)
f = (6*x-2)**2 * np.sin(12*x-4)}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.plot(x, f, 'r-', linewidth=2)
ax.set_xlabel('$x$')
ax.set_ylabel('$f(x)$')
ax.set_xlim(-0.01, 1)
ax.set_ylim([-20, 20])

mlai.write_figure('forrester-function.svg', directory='\writeDiagramsDir/uq')}

\figure{\includediagram{\diagramsDir/uq/forrester-function}{80%}}{The Forrester function is commonly used as an exemplar function for surrogate modelling and emulation. It has the form $f(x) = (6x-2)^2\sin(12 x-4)$}{forrester-function}

\endif
