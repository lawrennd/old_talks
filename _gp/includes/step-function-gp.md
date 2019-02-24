\ifndef{stepFunctionGp}
\define{stepFunctionGp}
\editme

\include{_ml/includes/step-function-data.md}
\include{_gp/includes/gpy-software.md}

\subsection{Step Function Data GP}

\notes{We can fit a Gaussian process to the step function data using ```GPy``` as follows.}

\code{m_full = GPy.models.GPRegression(x,yhat)
_ = m_full.optimize() # Optimize parameters of covariance function}

\notes{Where ```GPy.models.GPRegression()``` gives us a standard GP regression model with exponentiated quadratic covariance function.}

\notes{The model is optimized using ```m_full.optimize()``` which calls an L-BGFS gradient based solver in python.}

\displaycode{fig, ax=plt.subplots(figsize=plot.big_wide_figsize)
plot.model_output(m_full, scale=scale, offset=offset, ax=ax, fontsize=20, portion=0.5)
ax.set_ylim(ylim)
ax.set_xlim(xlim)

mlai.write_figure(figure=fig,filename='../slides/diagrams/gp/step-function-gp.svg', 
            transparent=True, frameon=True)}
			

\rawfigure{\includediagram{../slides/diagrams/gp/step-function-gp} 
\caption{Gaussian process fit to the step function data. Note the large error bars and the over-smoothing of the discontinuity. Error bars are shown at two standard deviations.}
}

\notes{The resulting fit to the step function data shows some challenges. In particular, the over smoothing at the discontinuity. If we know how many discontinuities there are, we can parameterize them in the step function. But by doing this, we form a semi-parametric model. The parameters indicate how many discontinuities are, and where they are. They can be optimized as part of the model fit. But if new, unforeseen, discontinuities arise when the model is being deployed in practice, these won't be accounted for in the predictions.}

\endif
