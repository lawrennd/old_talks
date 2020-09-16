\ifndef{olympicMarathonGp}
\define{olympicMarathonGp}
\editme

\include{_ml/includes/olympic-marathon-data.md}
\include{_ml/includes/alan-turing-marathon.md}

\notes{
Our first objective will be to perform a Gaussian process fit to the data, we'll do this using the [GPy software](https://github.com/SheffieldML/GPy).}

\setupcode{import GPy}
\code{m_full = GPy.models.GPRegression(x,yhat)
_ = m_full.optimize() # Optimize parameters of covariance function}

\notes{The first command sets up the model, then ```m_full.optimize()```
optimizes the parameters of the covariance function and the noise level of the model. Once the fit is complete, we'll try creating some test points, and computing the output of the GP model in terms of the mean and standard deviation of the posterior functions between 1870 and 2030. We plot the mean function and the standard deviation at 200 locations. We can obtain the predictions using
```y_mean, y_var = m_full.predict(xt)```
}

\code{xt = np.linspace(1870,2030,200)[:,np.newaxis]
yt_mean, yt_var = m_full.predict(xt)
yt_sd=np.sqrt(yt_var)}

\notes{Now we plot the results using the helper function in ```teaching_plots```.}

\setupdisplaycode{import teaching_plots as plot}

\displaycode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot.model_output(m_full, scale=scale, offset=offset, ax=ax, xlabel='year', ylabel='pace min/km', fontsize=20, portion=0.2)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
mlai.write_figure(figure=fig,
                  filename='\writeDiagramsDir/gp/olympic-marathon-gp.svg', 
                  transparent=True, frameon=True)}

\newslide{Olympic Marathon Data GP}

\figure{\includediagram{\diagramsDir/gp/olympic-marathon-gp}}{Gaussian process fit to the Olympic Marathon data. The error bars are too large, perhaps due to the outlier from 1904.}{olympic-marathon-gp}


\notes{
\subsection{Fit Quality}

In the fit we see that the error bars (coming mainly from the noise variance) are quite large. This is likely due to the outlier point in 1904, ignoring that point we can see that a tighter fit is obtained. To see this make a version of the model, ```m_clean```, where that point is removed. 

\code{x_clean=np.vstack((x[0:2, :], x[3:, :]))
y_clean=np.vstack((y[0:2, :], y[3:, :]))

m_clean = GPy.models.GPRegression(x_clean,y_clean)
_ = m_clean.optimize()}
}

\displaycode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot.model_output(m_clean, scale=scale, offset=offset, ax=ax, xlabel='year', ylabel='pace min/km', fontsize=20, portion=0.2)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
mlai.write_figure(figure=fig,
                  filename='\writeDiagramsDir/gp/olympic-marathon-gp.svg', 
                  transparent=True, frameon=True)}

\endif
