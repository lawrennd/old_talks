\ifndef{dellaGattaGeneGp}
\include{_ml/includes/della-gatta-gene-data.md}

\newslide{Gene Expression Example}

* Want to detect if a gene is expressed or not, fit a GP to each gene @Kalaitzis:simple11.

\newslide{}

\includepng{../slides/diagrams/health/1471-2105-12-180_1}
\aligncenter{<http://www.biomedcentral.com/1471-2105/12/180>}

\newslide{}

\notes{
Our first objective will be to perform a Gaussian process fit to the data, we'll do this using the [GPy software](https://github.com/SheffieldML/GPy).}

\setupcode{import GPy}
\code{m_full = GPy.models.GPRegression(x,yhat)
m_full.kern.lengthscale=50
_ = m_full.optimize() # Optimize parameters of covariance function}

\notes{Initialize the length scale parameter (which here actually represents a *time scale* of the covariance function to a reasonable value. Default would be 1, but here we set it to 50 minutes, given points are arriving across zero to 250 minutes.}

\code{xt = np.linspace(-20,260,200)[:,np.newaxis]
yt_mean, yt_var = m_full.predict(xt)
yt_sd=np.sqrt(yt_var)}

\notes{Now we plot the results using the helper function in ```teaching_plots```.}

\setupdisplaycode{import teaching_plots as plot}

\displaycode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot.model_output(m_full, scale=scale, offset=offset, ax=ax, xlabel='time/min', ylabel='expression', fontsize=20, portion=0.2)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
ax.set_title('log likelihood: {ll:.3}'.format(ll=m_full.log_likelihood()), fontsize=20)
mlai.write_figure(figure=fig,
                  filename='../slides/diagrams/gp/della-gatta-gene-gp.svg', 
                  transparent=True, frameon=True)}

\newslide{TP53 Gene Data GP}

\includesvg{../slides/diagrams/gp/della-gatta-gene-gp.svg}

\notes{Now we try a model initialized with a longer length scale.}

\code{m_full2 = GPy.models.GPRegression(x,yhat)
m_full2.kern.lengthscale=2000
_ = m_full2.optimize() # Optimize parameters of covariance function}

\setupdisplaycode{import teaching_plots as plot}

\displaycode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot.model_output(m_full2, scale=scale, offset=offset, ax=ax, xlabel='time/min', ylabel='expression', fontsize=20, portion=0.2)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
ax.set_title('log likelihood: {ll:.3}'.format(ll=m_full2.log_likelihood()), fontsize=20)
mlai.write_figure(figure=fig,
                  filename='../slides/diagrams/gp/della-gatta-gene-gp2.svg', 
                  transparent=True, frameon=True)}

\newslide{TP53 Gene Data GP}

\includesvg{../slides/diagrams/gp/della-gatta-gene-gp2.svg}

\notes{Now we try a model initialized with a lower noise.}

\code{m_full3 = GPy.models.GPRegression(x,yhat)
m_full3.kern.lengthscale=20
m_full3.likelihood.variance=0.001
_ = m_full3.optimize() # Optimize parameters of covariance function}

\setupdisplaycode{import teaching_plots as plot}

\displaycode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot.model_output(m_full3, scale=scale, offset=offset, ax=ax, xlabel='time/min', ylabel='expression', fontsize=20, portion=0.2)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
ax.set_title('log likelihood: {ll:.3}'.format(ll=m_full3.log_likelihood()), fontsize=20)
mlai.write_figure(figure=fig,
                  filename='../slides/diagrams/gp/della-gatta-gene-gp3.svg', 
                  transparent=True, frameon=True)}

\newslide{TP53 Gene Data GP}

\includesvg{../slides/diagrams/gp/della-gatta-gene-gp3.svg}


\setupplotcode{import teaching_plots as plot}

\plotcode{plot.multiple_optima(diagrams='../slides/diagrams/gp')}

\newslide{Multiple Optima}

\includesvg{../slides/diagrams/gp/multiple-optima000.svg}

<!--\newslide{Multiple Optima}

\includesvg{../slides/diagrams/gp/multiple-optima001.svg}-->

\define{dellaGattaGeneGp}
\endif
