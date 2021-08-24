\ifndef{gpyEmulation}
\define{gpyEmulation}

\editme

\subsection{GPy and Emulation}


\notes{Let $\inputVector$ be a random variable defined over the real numbers, $\Re$, and $\mappingFunction(\cdot)$ be a function mapping between the real numbers $\Re \rightarrow \Re$. 

The problem of *uncertainty propagation* is the study of the distribution of the random variable $\mappingFunction(\inputVector)$.

We're going to address this problem using emulation and GPy. We will see in this section the advantage of using a model when only a few observations of $f$ are available. 

Firstly, we'll make use of a test function known as the Branin test function.}
$$
\mappingFunction(\inputVector) = a(\inputScalar_2 - b\inputScalar_1^2 + c\inputScalar_1 - r)^2 + s(1-t \cos(\inputScalar_1)) + s
$$
\notes{where we are setting $a=1$, $b=5.1/(4\pi^2)$, $c=5/\pi$, $r=6$, $s=10$ and $t=1/(8\pi)$.}

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
mu, var = m.predict(Xp)
print('The estimate of the mean of the Branin function is {mean}'.format(mean=np.mean(mu)))}

\notes{\codeassignment{Now think about how to make use of the variance estimation from the Gaussian process to obtain error bars around your estimate.}

\codeassignment{You've seen how the Monte Carlo estimates work with the Gaussian process. Now make your estimate of the probability that the Branin function is greater than 200 with the uniform random inputs.}}

\subsection{Uncertainty Quantification}
\slides{* History of interest, see e.g. @McKay-selecting79
* The review:
    * Random Sampling
    * Stratified Sampling
    * Latin Hypercube Sampling
* As approaches for Monte Carlo estimates
}
\notes{We're introducing you to the optimization and analysis of real-world models through emulation, this domain is part of a broader field known as surrogate modelling. 

Although we're approaching this from the machine learning perspective, with a computer-scientist's approach, you won't be surprised to find out that this field is not new and there are a range of research groups interested in this domain.}

\notes{This type of challenge, of where to run the simulation to get the answer you require is an old challenge. One classic paper, @McKay-selecting79, reviews three different methods for designing these inputs. They are *random sampling*, *stratified sampling* and *Latin hypercube sampling*.}

\newslide{Random Sampling}

>  Let the input values $\inputVector_1, \dots, \inputVector_\numData$
> be a random sample from $f(\inputVector)$. This method of sampling
> is perhaps the most obvious, and an entire body of statistical
> literature may be used in making inferences regarding the
> distribution of $Y(t)$.

\newslide{Stratified Sampling}

> Using stratified sampling, all
> areas of the sample space of $\inputVector$ are represented by
> input values. Let the sample space $S$ of $\inputVector$ be partitioned into $I$ disjoint strata $S_t$. Let $\pi = P(\inputVector \in S_i)$
> represent the size of $S_i$. Obtain a random sample $\inputVector_{ij}$, $j
> = 1, \dots, n$ from $S_i$. Then of course the $n_i$ sum to $\numData$.
> If $I = 1$, we have random sampling over the entire
> sample space.

\newslide{Latin Hypercube Sampling}

> The same reasoning that led to stratified sampling, ensuring that
> all portions of $S$ were sampled, could lead further. If we wish
> to ensure also that each of the input variables $\inputVector_k$ has
> all portions of its distribution represented by input values, we can
> divide the range of each $\inputVector_k$ into $\numData$ strata of
> equal marginal probability $1/\numData$, and sample once from each
> stratum. Let this sample be $\inputVector_{kj}$, $j = 1, \dots,
> \numData$. These form the $\inputVector_k$ component, $k = 1, \dots
> , K$, in $\inputVector_i$, $i = 1, \dots, \numData$. The components
> of the various $\inputVector_k$'s are matched at random. This method
> of selecting input values is an extension of quota sampling
> (Steinberg 1963), and can be viewed as a $K$-dimensional extension of
> Latin square sampling (Raj 1968).

\notes{The paper's rather dated reference to "Output from a Computer Code" does carry forward through this literature, which has continued to be a focus of interest for statisticians. [Tony O'Hagan](http://www.tonyohagan.co.uk/academic/), who was a colleague in Sheffield but is also one of the pioneers of Gaussian process models was developing these methods when I first arrived there [@Kennedy-bayesian01], and continued with a large EPSRC funded project for managing uncertainty in computational models, <http://www.mucm.ac.uk/>. You can see a list of [their technical reports here](http://www.mucm.ac.uk/Pages/Dissemination/TechnicalReports.html).

Another important group based in France is the "MASCOT-NUM Research Group", <https://www.gdr-mascotnum.fr/>. These researchers bring together statisticians, applied mathematicians and engineers in solving these problems.}

