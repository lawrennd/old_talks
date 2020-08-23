\ifndef{stepFunctionData}
\define{stepFunctionData}
\editme

\notes{\subsection{Step Function}

Next we consider a simple step function data set.}

\code{num_low=25
num_high=25
gap = -.1
noise=0.0001
x = np.vstack((np.linspace(-1, -gap/2.0, num_low)[:, np.newaxis],
              np.linspace(gap/2.0, 1, num_high)[:, np.newaxis]))
y = np.vstack((np.zeros((num_low, 1)), np.ones((num_high,1))))
scale = np.sqrt(y.var())
offset = y.mean()
yhat = (y-offset)/scale}

\displaycode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
_ = ax.plot(x, y, 'r.',markersize=10)
_ = ax.set_xlabel('$x$', fontsize=20)
_ = ax.set_ylabel('$y$', fontsize=20)
xlim = (-2, 2)
ylim = (-0.6, 1.6)
ax.set_ylim(ylim)
ax.set_xlim(xlim)
mlai.write_figure(figure=fig, filename='../\diagramsDir/datasets/step-function.svg', 
            transparent=True, frameon=True)}
			
\subsection{Step Function Data}

\figure{\includediagram{\diagramsDir/datasets/step-function}{80%}}{Simulation study of step function data artificially generated. Here there is a small overlap between the two lines.}{step-function-data}

\endif
