\ifndef{erichFriedmanPackingGp}
\define{erichFriedmanPackingGp}

\installcode{mlai}
\include{_datasets/includes/erich-friedman-packing-data.md}

\editme

\installcode{GPy}

\subsection{Gaussian Process Fit}

\notes{Our first objective will be to perform a Gaussian process fit to the data, we'll do this using the [GPy software](https://github.com/SheffieldML/GPy).}

\setupcode{import GPy}
\code{m_full = GPy.models.GPRegression(x,y)
_ = m_full.optimize() # Optimize parameters of covariance function}

\notes{The first command sets up the model, then `m_full.optimize()`
optimizes the parameters of the covariance function and the noise level of the model. Once the fit is complete, we'll try creating some test points, and computing the output of the GP model in terms of the mean and standard deviation of the posterior functions between 1870 and 2030. We plot the mean function and the standard deviation at 200 locations. We can obtain the predictions using
`y_mean, y_var = m_full.predict(xt)`
}

\code{xt = np.linspace(0,100,400)[:,np.newaxis]
yt_mean, yt_var = m_full.predict(xt)
yt_sd=np.sqrt(yt_var)}

\notes{Now we plot the results using the helper function in `mlai.plot`.}

\setupdisplaycode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\displaycode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot.model_output(m_full, ax=ax,  xlabel="n", ylabel="s", fontsize=20, portion=0.2)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
mlai.write_figure(figure=fig,
                  filename="erich-friedman-packing-gp.svg", 
                  directory = "\writeDiagramsDir/gp",
                  transparent=True)}

\newslide{Erich Friedman Packing Data GP}

\figure{\includediagram{\diagramsDir/gp/erich-friedman-packing-gp}{80%}}{Gaussian process fit to the Erich Friedman Packing data.}{erich-friedman-packing-gp}



\endif
