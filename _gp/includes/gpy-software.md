\ifndef{gpySoftware}
\define{gpySoftware}
\editme

\subsection{GPy: A Gaussian Process Framework in Python}

\notes{Gaussian processes are a flexible tool for non-parametric analysis with uncertainty. The GPy software was started in Sheffield to provide a easy to use interface to GPs. One which allowed the user to focus on the modelling rather than the mathematics.}

\figure{\includepng{\diagramsDir/gp/gpy}{70%}}{GPy is a BSD licensed software code base for implementing Gaussian process models in Python. It is designed for teaching and modelling. We welcome contributions which can be made through the Github repository <https://github.com/SheffieldML/GPy>}{gpy-software}

\slides{\aligncenter{<https://github.com/SheffieldML/GPy>}}

\newslide{GPy: A Gaussian Process Framework in Python}

\slides{
* BSD Licensed software base.
* Wide availability of libraries, 'modern' scripting language.
* Allows us to set projects to undergraduates in Comp Sci that use GPs.
* Available through GitHub
  <https://github.com/SheffieldML/GPy>
* Reproducible Research with Jupyter Notebook.
}
\notes{GPy is a BSD licensed software code base for implementing Gaussian process models in python. This allows GPs to be combined with a wide variety of software libraries. 

The software itself is available on [GitHub](https://github.com/SheffieldML/GPy) and the team welcomes contributions.}

\newslide{Features}

\slides{
* Probabilistic-style programming (specify the model, not the algorithm).
* Non-Gaussian likelihoods.
* Multivariate outputs.
* Dimensionality reduction.
* Approximations for large data sets.
}

\notes{The aim for GPy is to be a probabilistic-style programming language, i.e. you specify the model rather than the algorithm. As well as a large range of covariance functions the software allows for non-Gaussian likelihoods, multivariate outputs, dimensionality reduction and approximations for larger data sets.}

\notes{The documentation for GPy can be found [here](https://gpy.readthedocs.io/en/latest/).}

\installcode{GPy}

\downloadcode{mlai}
\downloadcode{teaching_plots}
\downloadcode{gp_tutorial}

\setupcode{import numpy as np
import GPy}

\setupplotcode{from matplotlib import pyplot as plt}

\notes{To give a feel for the sofware we'll start by creating an exponentiated quadratic covariance function,
$$
\kernelScalar(\inputVector, \inputVector^\prime) = \alpha \exp\left(-\frac{\ltwoNorm{\inputVector - \inputVector^\prime}^2}{2\ell^2}\right),
$$
where the length scale is $\ell$ and the variance is $\alpha$.

To set this up in GPy we create a kernel in the following manner.}

\code{input_dim=1
alpha = 1.0
lengthscale = 2.0
kern = GPy.kern.RBF(input_dim=input_dim, variance=alpha, lengthscale=lengthscale)}

\notes{That builds a kernel object for us. The kernel can be displayed.}

\code{display(kern)}

\notes{Or because it's one dimensional, you can also plot the kernel as a function of its inputs (while the other is fixed).}

\setupplotcode{import teaching_plots as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
kern.plot(ax=ax)
mlai.write_figure('gpy-eq-covariance.svg', directory='\writeDiagramsDir/kern')}

\figure{\includediagram{\diagramsDir/kern/gpy-eq-covariance}{50%}}{The exponentiated quadratic covariance function as plotted by the `GPy.kern.plot` command.}{gpy-eq-covariance}

\notes{You can set the lengthscale of the covariance to different values and plot the result.}

\code{kern = GPy.kern.RBF(input_dim=input_dim)     # By default, the parameters are set to 1.
lengthscales = np.asarray([0.2,0.5,1.,2.,4.])}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)

for lengthscale in lengthscales:
    kern.lengthscale=lengthscale
    kern.plot(ax=ax)

ax.legend(lengthscales)
mlai.write_figure('gpy-eq-covariance-lengthscales.svg', directory='\writeDiagramsDir/kern')}

\notes{\subsection{Covariance Functions in GPy}}

\notes{Many covariance functions are already implemented in GPy. Instead of rbf, try constructing and plotting the following  covariance functions: `exponential`, `Matern32`, `Matern52`, `Brownian`, `linear`, `bias`,
`rbfcos`, `periodic_Matern32`, etc. Some of these covariance functions, such as `rbfcos`, are not
parametrized by a variance and a lengthscale. Furthermore, not all kernels are stationary (i.e., they can’t all be written as $k ( x, y) = f ( x − y)$, see for example the Brownian
covariance function). For plotting  so it may be interesting to change the value of the fixed input.}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)

brownian_kern = GPy.kern.Brownian(input_dim=1)
inputs = np.array([2., 4.])
for x in inputs:
    brownian_kern.plot(x,plot_limits=[0,5], ax=ax)
ax.legend(inputs)
ax.set_ylim(-0.1,5.1)

mlai.write_figure('gpy-brownian-covariance-lengthscales.svg', directory='\writeDiagramsDir/kern')}

\subsection{Combining Covariance Functions in GPy}

\notes{In GPy you can easily combine covariance functions you have created using the sum and product operators, `+` and `*`. So, for example, if we wish to combine an exponentiated quadratic covariance with a Matern 5/2 then we can write}

\code{kern1 = GPy.kern.RBF(1, variance=1., lengthscale=2.)
kern2 = GPy.kern.Matern52(1, variance=2., lengthscale=4.)
kern = kern1 + kern2
display(kern)}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)

kern.plot(ax=ax)

mlai.write_figure('gpy-eq-plus-matern52-covariance.svg', directory='\writeDiagramsDir/kern')}

\figure{\includediagram{\diagramsDir/kern/gpy-eq-plus-matern52-covariance}{80%}}{A combination of the exponentiated quadratic covariance plus the Matern $5/2$ covariance.}{gpy-eq-plus-matern52-covariance}

\notes{Or if we wanted to multiply them we can write}

\code{kern1 = GPy.kern.RBF(1, variance=1., lengthscale=2.)
kern2 = GPy.kern.Matern52(1, variance=2., lengthscale=4.)
kern = kern1 * kern2
display(kern)}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)

kern.plot(ax=ax)

mlai.write_figure('gpy-eq-times-matern52-covariance.svg', directory='\writeDiagramsDir/kern')}

\figure{\includediagram{\diagramsDir/kern/gpy-eq-times-matern52-covariance}{80%}}{A combination of the exponentiated quadratic covariance multiplied by the Matern $5/2$ covariance.}{gpy-eq-times-matern52-covariance}

\notes{You can learn about how to implement [new kernel objects in GPy here](https://gpy.readthedocs.io/en/latest/tuto_creating_new_kernels.html).}

\subsection{A Gaussian Process Regression Model}

\notes{We will now combine the Gaussian process prior with some data to form a GP regression model with GPy. We will generate data from the function 
$$
\mappingFunction( \inputScalar ) = − \cos(\pi \inputScalar ) + \sin(4\pi \inputScalar )$ over $[0, 1],
$$
adding some noise to give 
$$
\dataScalar(\inputScalar) = \mappingFunction(\inputScalar) + \noiseScalar,
$$ 
with the noise being Gaussian distributed, $\noiseScalar \sim \gaussianSamp{0}{0.01}$.}

\code{X = np.linspace(0.05,0.95,10)[:,np.newaxis]
Y = -np.cos(np.pi*X) + np.sin(4*np.pi*X) + np.random.normal(loc=0.0, scale=0.1, size=(10,1))}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.plot(X,Y,'kx',mew=1.5, linewidth=2)

mlai.write_figure('noisy-sine.svg', directory='\writeDiagramsDir/gp')}

\notes{\figure{\includediagram{\diagramsDir/gp/noisy-sine}{80%}}{Data from the noisy sine wave for fitting with a GPy model.}{noisy-sine}}

\notes{A GP regression model based on an exponentiated quadratic covariance function can be defined by first defining a covariance function.}

\code{kern = GPy.kern.RBF(input_dim=1, variance=1., lengthscale=1.)}

\notes{And then combining it with the data to form a Gaussian process model.}

\code{model = GPy.models.GPRegression(X,Y,kern)}

\notes{Just as for the covariance function object, we can find out about the model using the command `display(model)`.}

\code{display(model)}

\notes{Note that by default the model includes some observation noise
with variance 1. We can see the posterior mean prediction and visualize the marginal posterior variances using `model.plot()`.}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
model.plot(ax=ax)

mlai.write_figure('noisy-sine-gp-fit.svg', directory='\writeDiagramsDir/gp')}

\notes{\figure{\includediagram{\diagramsDir/gp/noisy-sine-gp-fit}{80%}}{A Gaussian process fit to the noisy sine data. Here the parameters of the process and the covariance function haven't yet been optimized.}{noisy-sine-gp-fit}}

\notes{You can also look directly at the predictions for the model using.}

\code{Xstar = np.linspace(0, 10, 100)[:, np.newaxis]
Ystar, Vstar = model.predict(Xstar)}

\notes{Which gives you the mean (`Ystar`), the variance (`Vstar`)  at the locations given by `Xstar`.}


\subsection{Covariance Function Parameter Estimation}

\notes{As we have seen during the lectures, the parameters values can be estimated by maximizing the likelihood of the observations. Since we don’t want one of the variance to become negative during the optimization, we can constrain all parameters to be positive before running the optimisation.}

\code{model.constrain_positive()}

\notes{The warnings are because the parameters are already constrained by default, the software is warning us that they are being reconstrained.

Now we can optimize the model using the `model.optimize()` method. Here we switch messages on, which allows us to see the progession of the optimization.}

\code{model.optimize(messages=True)}

\notes{By default the optimization is using a limited memory BFGS optimizer [@Byrd:lbfgsb95].

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
model.plot(ax=ax)

mlai.write_figure('noisy-sine-gp-optimized-fit.svg', directory='\writeDiagramsDir/gp')}

\notes{\figure{\includediagram{\diagramsDir/gp/noisy-sine-gp-optimized-fit}{80%}}{A Gaussian process fit to the noisy sine data with parameters optimized.}{noisy-sine-gp-optimized-fit}}


\endif
