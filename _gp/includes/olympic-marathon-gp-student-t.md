\ifndef{olympicMarathonGpStudentt}
\define{olympicMarathonGpStudentt}

\include{_gp/includes/olympic-marathon-gp.md}

\editme

\subsection{Robust Regression: A Running Example}

\notes{We already considered the olympic marathon data. In 1904 we
noted there was an outlier example. Today we'll see if we can deal
with that outlier by considering a non-Gaussian likelihood. Noise
sampled from a Student-$t$ density is heavier tailed than that sampled
from a Gaussian. However, it cannot be trivially assimilated into the
Gaussian process. Below we use the *Laplace approximation* to
incorporate this noise model.}

\code{GPy.likelihoods.StudentT?}


\code{# make a student t likelihood with standard parameters
t_distribution = GPy.likelihoods.StudentT(deg_free=3, sigma2=2)
laplace = GPy.inference.latent_function_inference.Laplace()

kern = GPy.kern.RBF(1, lengthscale=5) + GPy.kern.Bias(1)
model = GPy.core.GP(x, y, kernel=kern, inference_method=laplace, likelihood=t_distribution)
model.constrain_positive('t_noise')

model.optimize(messages=True)
display(model)}


\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
model.plot(ax=ax)

mlai.write_figure('olympic-marathon-gp-student-t.svg', directory='\writeDiagramsDir/gp')}

\newslide{}

\figure{\includediagram{\diagramsDir/gp/olympic-marathon-gp-student-t}{80%}}{Fit to the Olympic marathon data using the Student-$t$ likelihood and the Laplace approximation.}{olympic-marathon-gp-student-t}

\codeAssignment{Compare this model with the regression model using a Gaussian likelihood. What difference do you notice in the predictions? Which model do you think is better?}{}{10}


\endif
