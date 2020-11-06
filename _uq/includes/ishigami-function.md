\ifndef{ishigamiFunction}
\define{ishigamiFunction}

\editme

\subsubsection{Ishigami Function}


\notes{The Ishigami function [@Ishigami-importance90] is a well-known example for uncertainty and sensitivity analysis methods because of its strong nonlinearity and peculiar dependence on $\inputScalar_3$. More details of this function can be found in [@Sobol-variance99].}

\notes{Mathematically, the form of the Ishigami function is}
$$
\mappingFunctionTwo(\textbf{x}) = \sin(\inputScalar_1) + a \sin^2(\inputScalar_2) + b \inputScalar_3^4 \sin(\inputScalar_1). 
$$
\notes{We will set the parameters to be $a = 5$ and $b=0.1$ . The input variables are sampled randomly $\inputScalar_i \sim \uniformSamp{-\pi}{\pi}$.}

\notes{Next we create the function object and visualize its shape marginally for each one of its three inputs.}

\notes{Load the Ishigami function}

\setupcode{from emukit.test_functions.sensitivity import Ishigami}

\code{ishigami = Ishigami(a=5, b=0.1)
target_function = ishigami.fidelity1}

\notes{That gives us the target function, next we define the input space for the simulator.}

\setupcode{import numpy as np
from emukit.core import ContinuousParameter, ParameterSpace}

\code{variable_domain = (-np.pi,np.pi)
		   
space = ParameterSpace(
          [ContinuousParameter('x1', *variable_domain), 
           ContinuousParameter('x2', *variable_domain),
           ContinuousParameter('x3', *variable_domain)])}

\notes{Before moving to any further analysis, we first plot the non-zero components $\mappingFunctionTwo(\inputVector)$. These components are 
$$
\begin{align*}
\mappingFunctionTwo_1(\inputScalar_1) & = \sin(\inputScalar_1) \\
\mappingFunctionTwo_2(\inputScalar_1) & = a \sin^2 (\inputScalar_2) \\
\mappingFunctionTwo_{13}(\inputScalar_1,\inputScalar_3) & = b \inputScalar_3^4 \sin(\inputScalar_1) 
\end{align*}
$$}

\code{x_grid = np.linspace(*variable_domain,100)
target_simulator = ishigami.fidelity1
f1 = ishigami.f1(x_grid)
f2 = ishigami.f2(x_grid)
F13 = ishigami.f13(np.array([x_grid,x_grid]).T)[:,np.newaxis]}

\setupplotcode{from mpl_toolkits.mplot3d import Axes3D}

\plotcode{fig, axs = plt.subplots(2, 2, figsize=plot.big_wide_figsize)
gs = axs[1, 1].get_gridspec()
for ax in axs[1, 0:]:
    ax.remove()

ax2 = fig.add_subplot(gs[1, 0:], projection='3d')

axs[0,0].plot(x_grid, f1,'-r')
axs[0,0].set_xlabel('$x_1$')
axs[0,0].set_ylabel('$f_1$')

axs[0,1].plot(x_grid,f2,'-r')
axs[0,1].set_xlabel('$x_2$')
axs[0,1].set_ylabel('$f_2$')

X, Y = np.meshgrid(x_grid, x_grid)
surf = ax2.plot_surface(X, Y, F13, cmap=cm.coolwarm, linewidth=0, antialiased=False)

ax2.set_xlabel('$x_1$')
ax2.set_ylabel('$x_3$')
ax2.set_zlabel('$f_{13}$')

mlai.write_figure(filename='non-zero-sobol-ishigami.svg', directory='\writeDiagramsDir/uq')}

\figure{\includediagram{\diagramsDir/uq/non-zero-sobol-ishigami}{80%}}{The non-zero components of the Ishigami function.}{non-zero-sobol-ishigami}

\endif
