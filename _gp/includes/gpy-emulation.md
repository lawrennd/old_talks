\ifndef{gpyEmulation}
\define{gpyEmulation}

\editme

talk-macros.gpp}oftware/includes/gpy-install.md}

\subsection{GPy and Emulation}


\notes{Let $\inputVector$ be a random variable defined over the real numbers, $\Re$, and $\mappingFunction(\cdot)$ be a function mapping between the real numbers $\Re \rightarrow \Re$. 

The problem of *uncertainty propagation* is the study of the distribution of the random variable $\mappingFunction(\inputVector)$.

We're going to address this problem using emulation and GPy. We will see in this section the advantage of using a model when only a few observations of $f$ are available. 

Firstly, we'll make use of a test function known as the Branin test function.}
$$
\mappingFunction(\inputVector) = a(\inputScalar_2 - b\inputScalar_1^2 + c\inputScalar_1 - r)^2 + s(1-t \cos(\inputScalar_1)) + s
$$
\notes{where we are setting $a=1$, $b=5.1/(4\pi^2)$, $c=5/\pi$, $r=6$, $s=10$ and $t=1/(8\pi)$.}

\setupcode{import numpy as np}

\code{def branin(X):
    y = ((X[:,1]-5.1/(4*np.pi**2)*X[:,0]**2+5*X[:,0]/np.pi-6)**2 
	    + 10*(1-1/(8*np.pi))*np.cos(X[:,0])+10)
    return(y)}

\notes{We'll define a grid of twenty-five observations  over [−5, 10] × [0, 15] and a set of 25 observations.}

\code{# Training set defined as a 5*5 grid:
xg1 = np.linspace(-5,10,5)
xg2 = np.linspace(0,15,5)
X = np.zeros((xg1.size * xg2.size,2))
for i,x1 in enumerate(xg1):
    for j,x2 in enumerate(xg2):
        X[i+xg1.size*j,:] = [x1,x2]

Y = branin(X)[:,np.newaxis]}

\notes{The task here will be to consider the distribution of $\mappingFunction(U)$, where $U$ is a random variable with uniform distribution over the input space of $\mappingFunction$. We focus on the computaiton of two quantities, the expectation of $\mappingFunction(U)$, $\expSamp{\mappingFunction(U)}$, and the probability that the value is greater than 200.}

\subsection{Computation of $\expSamp{\mappingFunction(U)}$}

\slides{* Compute the expectation of the Branin function.
* Sample at 25 points on a grid.
* Compute the mean (Reiemann sum approximation).}

\notes{The expectation of $\mappingFunction (U )$ is given by $\int_\inputVector \mappingFunction ( \inputVector)\text{d}\inputVector$. A basic approach to approximate this
integral is to compute the mean of the 25 observations: `np.mean(Y)`. Since the points
are distributed on a grid, this can be seen as the approximation of the integral by a
rough Riemann sum.}

\code{print('Estimate of the expectation is given by: {mean}'.format(mean=Y.mean()))}

\notes{The result can be compared with the actual mean of the Branin
function which is 54.31.}

\newslide{Emulate and do MC Samples}

Alternatively, we can fit a GP model and compute the integral of the best predictor
by Monte Carlo sampling.

\notes{Firstly, we create the covariance function. Here we're going to use an exponentiated quadratic, but we'll augment it with the 'bias' covariance function. This covariance function represents a single fixed bias that is added to the overall covariance. It allows us to deal with non-zero-mean emulations.}

\setupcode{import GPy}

\code{# Create an exponentiated quadratic plus bias covariance function
kern_eq = GPy.kern.RBF(input_dim=2, ARD = True)
kern_bias = GPy.kern.Bias(input_dim=2)
kern = kern_eq + kern_bias}

\notes{Now we construct the Gaussian process regression model in GPy.}
\code{# Build a GP model
model = GPy.models.GPRegression(X,Y,kern)}

\notes{In the sinusoid example above, we learnt the variance of the process. But in this example, we are fitting an emulator to a function we know is noise-free. However, we don't fix the noise value to precisely zero, as this can lead to some numerical errors. Instead, we fix the variance of the Gaussian noise to a very small value.}

\code{# fix the noise variance
model.likelihood.variance.fix(1e-5)}

\notes{Now we fit the model. Note, that the initial values for the length scale are not appropriate. So first set the length scale of the model needs to be reset.}

\code{kern.rbf.lengthscale = np.asarray([3, 3])}

\notes{It's a common error in Gaussian process fitting to initialize the length scale too small or too big. The challenge is that the error surface is normally multimodal, and the final solution can be very sensitive to this initialization. If the length scale is initialized too small, the solution can converge on an place where the signal isn't extracted by the covariance function. If the length scale is initialized too large, then the variations of the function are often missing. Here the length scale is set for each dimension of inputs as 3. Now that's done, we can optimize the model.}


\code{# Randomize the model and optimize
model.optimize(messages=True)}

\setupplotcode{import matplotlib.pyplot as plt}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
model.plot(ax=ax)

mlai.write_figure('branin-gp-optimized-fit.svg', directory='\writeDiagramsDir/gp')}

\newslide{Branin Function Fit}

\figure{\includediagram{\diagramsDir/gp/branin-gp-optimized-fit}{80%}}{A Gaussian process fit to the Branin test function, used to assess the mean of the function by emulation.}{branin-gp-optimized-fit}

\notes{Finally, we can compute the mean of the model predictions using very many Monte Carlo samples.

Note, that in this example, because we're using a test function, we could simply have done the Monte Carlo estimation directly on the Branin function. However, imagine instead that we were trying to understand the results of a complex computational fluid dynamics simulation, where each run of the simulation (which is equivalent to our test function) took many hours. In that case the advantage of the emulator is clear.}

\code{# Compute the mean of model prediction on 1e5 Monte Carlo samples
Xp = np.random.uniform(size=(int(1e5),2))
Xp[:,0] = Xp[:,0]*15-5
Xp[:,1] = Xp[:,1]*15
mu, var = model.predict(Xp)
print('The estimate of the mean of the Branin function is {mean}'.format(mean=np.mean(mu)))}

\notes{\codeassignment{Now think about how to make use of the variance estimation from the Gaussian process to obtain error bars around your estimate.}

\codeassignment{You've seen how the Monte Carlo estimates work with the Gaussian process. Now make your estimate of the probability that the Branin function is greater than 200 with the uniform random inputs.}}

talk-macros.gpp}q/includes/uq-sampling-history-doe.md}

\endif
