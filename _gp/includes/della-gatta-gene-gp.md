\ifndef{dellaGattaGeneGp}
\define{dellaGattaGeneGp}
\editme

\notes{\subsection{Gene Expression Example}}

\notes{We now consider an example in gene expression. Gene expression is the measurement of mRNA levels expressed in cells. These mRNA levels show which genes are 'switched on' and producing data. In the example we will use a Gaussian process to determine whether a given gene is active, or we are merely observing a noise response.}

\include{_datasets/includes/della-gatta-gene-data.md}

\newslide{Gene Expression Example}

* Want to detect if a gene is expressed or not, fit a GP to each gene @Kalaitzis:simple11.

\newslide{}

\centerdiv{\freddieKalaitzisPicture{15%}}

\figure{\includepng{\diagramsDir/health/1471-2105-12-180_1}{80%}}{The example is taken from the paper "A Simple Approach to Ranking Differentially Expressed Gene Expression Time Courses through Gaussian Process Regression." @Kalaitzis:simple11.}{a-simple-approach-to-ranking}

\aligncenter{<http://www.biomedcentral.com/1471-2105/12/180>}

\newslide{}

\notes{
Our first objective will be to perform a Gaussian process fit to the data, we'll do this using the [GPy software](https://github.com/SheffieldML/GPy).}

\setupcode{import GPy}
\code{m_full = GPy.models.GPRegression(x,yhat)
m_full.kern.lengthscale=50
_ = m_full.optimize() # Optimize parameters of covariance function}

\notes{Initialize the length scale parameter (which here actually represents a *time scale* of the covariance function) to a reasonable value. Default would be 1, but here we set it to 50 minutes, given points are arriving across zero to 250 minutes.}

\code{xt = np.linspace(-20,260,200)[:,np.newaxis]
yt_mean, yt_var = m_full.predict(xt)
yt_sd=np.sqrt(yt_var)}

\notes{Now we plot the results using the helper function in `mlai.plot`.}

\setupdisplaycode{import mlai.plot}

\displaycode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot.model_output(m_full, scale=scale, offset=offset, ax=ax, xlabel='time/min', ylabel='expression', fontsize=20, portion=0.2)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
ax.set_title('log likelihood: {ll:.3}'.format(ll=m_full.log_likelihood()), fontsize=20)
mlai.write_figure(figure=fig,
                  filename='\writeDiagramsDir/gp/della-gatta-gene-gp.svg', 
                  transparent=True, frameon=True)}

\newslide{TP53 Gene Data GP}

\figure{\includediagram{\diagramsDir/gp/della-gatta-gene-gp}{80%}}{Result of the fit of the Gaussian process model with the time scale parameter initialized to 50 minutes.}{della-gatta-gene-gp}

\notes{Now we try a model initialized with a longer length scale.}

\code{m_full2 = GPy.models.GPRegression(x,yhat)
m_full2.kern.lengthscale=2000
_ = m_full2.optimize() # Optimize parameters of covariance function}

\setupdisplaycode{import mlai.plot}

\displaycode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot.model_output(m_full2, scale=scale, offset=offset, ax=ax, xlabel='time/min', ylabel='expression', fontsize=20, portion=0.2)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
ax.set_title('log likelihood: {ll:.3}'.format(ll=m_full2.log_likelihood()), fontsize=20)
mlai.write_figure(figure=fig,
                  filename='\writeDiagramsDir/gp/della-gatta-gene-gp2.svg', 
                  transparent=True, frameon=True)}

\newslide{TP53 Gene Data GP}

\figure{\includediagram{\diagramsDir/gp/della-gatta-gene-gp2}{80%}}{Result of the fit of the Gaussian process model with the time scale parameter initialized to 2000 minutes.}{della-gatta-gene-gp2}

\notes{Now we try a model initialized with a lower noise.}

\code{m_full3 = GPy.models.GPRegression(x,yhat)
m_full3.kern.lengthscale=20
m_full3.likelihood.variance=0.001
_ = m_full3.optimize() # Optimize parameters of covariance function}

\setupdisplaycode{import mlai.plot}

\displaycode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
plot.model_output(m_full3, scale=scale, offset=offset, ax=ax, xlabel='time/min', ylabel='expression', fontsize=20, portion=0.2)
ax.set_xlim(xlim)
ax.set_ylim(ylim)
ax.set_title('log likelihood: {ll:.3}'.format(ll=m_full3.log_likelihood()), fontsize=20)
mlai.write_figure(figure=fig,
                  filename='\writeDiagramsDir/gp/della-gatta-gene-gp3.svg', 
                  transparent=True, frameon=True)}

\newslide{TP53 Gene Data GP}

\figure{\includediagram{\diagramsDir/gp/della-gatta-gene-gp3}{80%}}{Result of the fit of the Gaussian process model with the noise initialized low (standard deviation 0.1) and the time scale parameter initialized to 20 minutes.}{della-gatta-gene-gp3}


\setupplotcode{import mlai.plot}

\plotcode{plot.multiple_optima(diagrams='\writeDiagramsDir/gp')}

\newslide{Multiple Optima}

\figure{\includediagram{\diagramsDir/gp/multiple-optima000}{50%}}{}{gp-multiple-optima000}

<!--\newslide{Multiple Optima}

\includediagram{\diagramsDir/gp/multiple-optima001}-->

\endif
