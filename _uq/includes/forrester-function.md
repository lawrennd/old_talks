\ifndef{forresterFunction}
\define{forresterFunction}

\editme

\subsection{Forrester Function}

\include{_uq/includes/alex-forrester.md}

\notes{We're going to introduce the experimental design acquisiton functions by looking at the Forrester function [@Forrester-engineering08]}

\setupcode{import numpy as np

from emukit.test_functions import forrester_function
#from emukit.core.loop.user_function import UserFunctionWrapper
#from emukit.core import ContinuousParameter, ParameterSpace
}


\code{target_function, space = forrester_function()}

\code{x_plot = np.linspace(space.parameters[0].min, space.parameters[0].max, 301)[:, None]
y_plot = target_function(x_plot)}

\setupplot{import matplotlib.pyplot as plt}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.plot(x_plot, y_plot, 'k', label='target Function', linewidth=2)

ax.legend(loc=2)
ax.set_xlabel('$x$')
ax.set_ylabel('$f(x)$')
ax.grid(True)
ax.set_xlim(0, 1)

mlai.write_figure(filename='forrester-function.svg', directory='\writeDiagramsDir/uq')}

\figure{\includediagram{\diagramsDir/uq/forrester-function}{80%}}{The Forrester function [@Forrester-engineering08].}{forrester-function}

\endif
