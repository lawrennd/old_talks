\ifndef{gpyTutorial}
\define{gpyTutorial}

\editme

\subsection{GPy Tutorial}

\centerdiv{\jamesHensmanPicture{15%}\nicolasDurrandePicture{15%}}

\notes{This GPy tutorial is based on material we share in the Gaussian process summer school for teaching these models <https://gpss.cc>. It contains material from various members and former members of the Sheffield machine learning group, but particular mention should be made of [Nicolas Durrande](https://sites.google.com/site/nicolasdurrandehomepage/) and [James Hensman](https://jameshensman.github.io/), see <http://gpss.cc/gpss17/labs/GPSS_Lab1_2017.ipynb>.}

\installcode{GPy}

\downloadcode{mlai}
\downloadcode{teaching_plots}
\downloadcode{gp_tutorial}

\setupcode{import numpy as np
import GPy}

\setupplotcode{from matplotlib import pyplot as plt}
\newslide{Covariance Functions}

\notes{To give a feel for the software we'll start by creating an exponentiated quadratic covariance function,}
$$
\kernelScalar(\inputVector, \inputVector^\prime) = \alpha \exp\left(-\frac{\ltwoNorm{\inputVector - \inputVector^\prime}^2}{2\ell^2}\right),
$$
\notes{where the length scale is $\ell$ and the variance is $\alpha$.

To set this up in GPy we create a kernel in the following manner.}

\code{input_dim=1
alpha = 1.0
lengthscale = 2.0
kern = GPy.kern.RBF(input_dim=input_dim, variance=alpha, lengthscale=lengthscale)}

\slides{```{.python}
input_dim=1
alpha = 1.0
lengthscale = 2.0
kern = GPy.kern.RBF(input_dim=input_dim, 
                    variance=alpha, 
					lengthscale=lengthscale)
```}

\notes{That builds a kernel object for us. The kernel can be displayed.}

\code{display(kern)}

\notes{Or because it's one dimensional, you can also plot the kernel as a function of its inputs (while the other is fixed).}

\setupplotcode{import teaching_plots as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
kern.plot(ax=ax)
mlai.write_figure('gpy-eq-covariance.svg', directory='\writeDiagramsDir/kern')}


\notes{\figure{\includediagram{\diagramsDir/kern/gpy-eq-covariance}{80%}}{The exponentiated quadratic covariance function as plotted by the `GPy.kern.plot` command.}{gpy-eq-covariance}}

\notes{You can set the lengthscale of the covariance to different values and plot the result.}

\code{kern = GPy.kern.RBF(input_dim=input_dim)     # By default, the parameters are set to 1.
lengthscales = np.asarray([0.2,0.5,1.,2.,4.])}

\newslide{Kernel Output}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)

for lengthscale in lengthscales:
    kern.lengthscale=lengthscale
    kern.plot(ax=ax)

ax.legend(lengthscales)
mlai.write_figure('gpy-eq-covariance-lengthscales.svg', directory='\writeDiagramsDir/kern')}

\figure{\includediagram{\diagramsDir/kern/gpy-eq-covariance-lengthscales}{80%}}{The exponentiated quadratic covariance function plotted for different length scales by `GPy.kern.plot` command.}{gpy-eq-covariance}

\subsection{Covariance Functions in GPy}
\slides{* Includes a range of covariance functions
    * E.g. Matern family, Brownian motion, periodic, linear etc.
	* Can [define new covariances](https://gpy.readthedocs.io/en/latest/tuto_creating_new_kernels.html)}

\notes{Many covariance functions are already implemented in GPy. Instead of rbf, try constructing and plotting the following  covariance functions: `exponential`, `Matern32`, `Matern52`, `Brownian`, `linear`, `bias`, `rbfcos`, `periodic_Matern32`, etc. Some of these covariance functions, such as `rbfcos`, are not parametrized by a variance and a lengthscale. Furthermore, not all kernels are stationary (i.e., they can’t all be written as $\kernelScalar(\inputVector, \inputVector^\prime) = f(\inputVector-\inputVector^\prime)$, see for example the Brownian covariance function). For plotting  so it may be interesting to change the value of the fixed input.}

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

\slides{```{.python}
kern1 = GPy.kern.RBF(1, variance=1., lengthscale=2.)
kern2 = GPy.kern.Matern52(1, variance=2., lengthscale=4.)
kern = kern1 + kern2
```}

\code{kern1 = GPy.kern.RBF(1, variance=1., lengthscale=2.)
kern2 = GPy.kern.Matern52(1, variance=2., lengthscale=4.)
kern = kern1 + kern2
display(kern)}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)

kern.plot(ax=ax)

mlai.write_figure('gpy-eq-plus-matern52-covariance.svg', directory='\writeDiagramsDir/kern')}

\newslide{}

\figure{\includediagram{\diagramsDir/kern/gpy-eq-plus-matern52-covariance}{80%}}{A combination of the exponentiated quadratic covariance plus the Matern $5/2$ covariance.}{gpy-eq-plus-matern52-covariance}

\newslide{Multiplication}

\notes{Or if we wanted to multiply them we can write}

\slides{```{.python}
kern1 = GPy.kern.RBF(1, variance=1., lengthscale=2.)
kern2 = GPy.kern.Matern52(1, variance=2., lengthscale=4.)
kern = kern1 * kern2
display(kern)
```}

\code{kern1 = GPy.kern.RBF(1, variance=1., lengthscale=2.)
kern2 = GPy.kern.Matern52(1, variance=2., lengthscale=4.)
kern = kern1 * kern2
display(kern)}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)

kern.plot(ax=ax)

mlai.write_figure('gpy-eq-times-matern52-covariance.svg', directory='\writeDiagramsDir/kern')}

\newslide{}

\notes{\figure{\includediagram{\diagramsDir/kern/gpy-eq-times-matern52-covariance}{80%}}{A combination of the exponentiated quadratic covariance multiplied by the Matern $5/2$ covariance.}{gpy-eq-times-matern52-covariance}}

\notes{You can learn about how to implement [new kernel objects in GPy here](https://gpy.readthedocs.io/en/latest/tuto_creating_new_kernels.html).}

\figure{\includeyoutube{-sY8zW3Om1Y}{600}{450}}{Designing the covariance function for your Gaussian process is a key place in which you introduce your understanding of the data problem. To learn more about the design of covariance functions, see this talk from Nicolas Durrande at GPSS in 2016.}{nicolas-durrande-on-kernel-design}

\subsection{A Gaussian Process Regression Model}

\notes{We will now combine the Gaussian process prior with some data to form a GP regression model with GPy. We will generate data from the function }
$$
\mappingFunction( \inputScalar ) = − \cos(\pi \inputScalar ) + \sin(4\pi \inputScalar )
$$ 
\notes{over the domain $[0, 1]$, adding some noise to gives }
$$
\dataScalar(\inputScalar) = \mappingFunction(\inputScalar) + \noiseScalar,
$$ 
\notes{with the noise being Gaussian distributed, $\noiseScalar \sim \gaussianSamp{0}{0.01}$.}

\newslide{Noisy Sine}

\code{X = np.linspace(0.05,0.95,10)[:,np.newaxis]
Y = -np.cos(np.pi*X) + np.sin(4*np.pi*X) + np.random.normal(loc=0.0, scale=0.1, size=(10,1))}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.plot(X,Y,'kx',mew=1.5, linewidth=2)

mlai.write_figure('noisy-sine.svg', directory='\writeDiagramsDir/gp')}

\figure{\includediagram{\diagramsDir/gp/noisy-sine}{80%}}{Data from the noisy sine wave for fitting with a GPy model.}{noisy-sine}

\notes{A GP regression model based on an exponentiated quadratic covariance function can be defined by first defining a covariance function.}

\slides{```{.python}
kern = GPy.kern.RBF(input_dim=1, variance=1., lengthscale=1.)
model = GPy.models.GPRegression(X,Y,kern)
```}

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

\newslide{GP Fit to Noisy Sine}

\figure{\includediagram{\diagramsDir/gp/noisy-sine-gp-fit}{80%}}{A Gaussian process fit to the noisy sine data. Here the parameters of the process and the covariance function haven't yet been optimized.}{noisy-sine-gp-fit}

\notes{You can also look directly at the predictions for the model using.}

\code{Xstar = np.linspace(0, 10, 100)[:, np.newaxis]
Ystar, Vstar = model.predict(Xstar)}

\notes{Which gives you the mean (`Ystar`), the variance (`Vstar`)  at the locations given by `Xstar`.}


\subsection{Covariance Function Parameter Estimation}

\notes{As we have seen during the lectures, the parameters values can be estimated by maximizing the likelihood of the observations. Since we don’t want any of the variances to become negative during the optimization, we can constrain all parameters to be positive before running the optimization.}

\code{model.constrain_positive()}

\notes{The warnings are because the parameters are already constrained by default, the software is warning us that they are being reconstrained.

Now we can optimize the model using the `model.optimize()` method. Here we switch messages on, which allows us to see the progression of the optimization.}

\slides{
```{.python}
model.optimize(messages=True)
```}

\code{model.optimize(messages=True)}

\notes{By default, the optimization is using a limited memory BFGS optimizer [@Byrd:lbfgsb95].

Once again, we can display the model, now to see how the parameters have changed.}

\code{display(model)}

\notes{The length scale is much smaller, as well as the noise level. The variance of the exponentiated quadratic has also reduced.}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
model.plot(ax=ax)

mlai.write_figure('noisy-sine-gp-optimized-fit.svg', directory='\writeDiagramsDir/gp')}

\figure{\includediagram{\diagramsDir/gp/noisy-sine-gp-optimized-fit}{80%}}{A Gaussian process fit to the noisy sine data with parameters optimized.}{noisy-sine-gp-optimized-fit}

\endif
