\ifndef{maunaLoaGp}
\define{maunaLoaGp}

\include{_datasets/includes/mauna-loa-data.md}

\editme

\subsection{Gaussian Process Fit}

\notes{The data set was used as a demonstration of model selection for Gaussian processes in @Rasmussen:book06 (Chapter 5).}

\addreading{@Rasmussen:book06}{Chapter 5}

\notes{Here we reconstruct that analysis in GPy. Our first objective will be to perform a Gaussian process fit to the data, we'll do this using the [GPy software](https://github.com/SheffieldML/GPy).}

\setupcode{import GPy}
\code{kernel1 = GPy.kern.RBF(1, lengthscale=40, variance=300)
kernel2 = GPy.kern.PeriodicMatern52(1, variance=4, period=1, lengthscale=0.2)
kernel3 = GPy.kern.RatQuad(1, lengthscale=5, variance=10, power=1)
kernel4 = GPy.kern.RBF(1, lengthscale=0.2, variance=1)
kernel5 = GPy.kern.Bias(1, variance=100)
kernel = kernel1 + kernel2 + kernel3 + kernel4 + kernel5
model = GPy.models.GPRegression(x,yhat, kernel=kernel)
model.optimize(messages=True) # Optimize parameters of covariance function}

\notes{The first command sets up the model, then ```model.optimize()```
optimizes the parameters of the covariance function and the noise level of the model. Once the fit is complete, we'll try creating some test points, and computing the output of the GP model in terms of the mean and standard deviation of the posterior functions between 1870 and 2030. We plot the mean function and the standard deviation at 200 locations. We can obtain the predictions using
```y_mean, y_var = model.predict(xt)```
}

\code{xt = np.linspace(xlim[0],xlim[1],300)[:,np.newaxis]
yt_mean, yt_var = model.predict(xt)
yt_sd=np.sqrt(yt_var)}

\notes{Now we plot the results using the helper function in ```mlai.plot```.}

\setupdisplaycode{import mlai.plot as plot}

\displaycode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.plot(xt, yt_mean*scale+offset, 'C0', linewidth=3)
ax.plot(x, y, 'r.')
ax.fill_between(xt[:, 0],
                 yt_mean[:, 0]*scale + offset + scale*np.sqrt(yt_var)[:, 0],
                 yt_mean[:, 0]*scale + offset - scale*np.sqrt(yt_var)[:, 0], color='C0', alpha=0.6)

ax.set_xlim(xlim)
ax.set_ylim(ylim)
mlai.write_figure(filename='mauna-loa-gp.svg', 
                  directory = '\writeDiagramsDir/gp')}

\newslide{Mauna Loa Data GP}

\figure{\includediagram{\diagramsDir/gp/mauna-loa-gp}{80%}}{Gaussian process fit to the Mauna Loa Observatory data on CO2 concentrations.}{mauna-loa-gp}

\endif
