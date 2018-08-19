\newslide{Mathematically}
\slides{
* Composite *multivariate* function
}\notes{Mathematically, a deep Gaussian process can be seen as a composite *multivariate* function,}
  $$
  \mathbf{g}(\inputVector)=\mappingFunctionVector_5(\mappingFunctionVector_4(\mappingFunctionVector_3(\mappingFunctionVector_2(\mappingFunctionVector_1(\inputVector))))).
  $$
\notes{Or if we view it from the probabilistic perspective we can see that a deep Gaussian process is specifying a factorization of the joint density, the standard deep model takes the form of a Markov chain.}

\setupcode{from matplotlib import rc

rc("font", **{'family':'sans-serif','sans-serif':['Helvetica'],'size':30})
rc("text", usetex=True)}

\plotcode{pgm = plot.horizontal_chain(depth=5)
pgm.render().figure.savefig("../slides/diagrams/deepgp/deep-markov.svg", transparent=True)}

\newslide{Equivalent to Markov Chain}
\slides{
* Composite *multivariate* function}
  $$
  p(\dataVector|\inputVector)= p(\dataVector|\mappingFunctionVector_5)p(\mappingFunctionVector_5|\mappingFunctionVector_4)p(\mappingFunctionVector_4|\mappingFunctionVector_3)p(\mappingFunctionVector_3|\mappingFunctionVector_2)p(\mappingFunctionVector_2|\mappingFunctionVector_1)p(\mappingFunctionVector_1|\inputVector)
  $$

\includesvg{../slides/diagrams/deepgp/deep-markov.svg}
\notes{\caption{Probabilistically the deep Gaussian process can be represented as a Markov chain.}}

\setupcode{from matplotlib import rc
rc("font", **{'family':'sans-serif','sans-serif':['Helvetica'], 'size':15})
rc("text", usetex=True)}

\plotcode{pgm = plot.vertical_chain(depth=5)
pgm.render().figure.savefig("../slides/diagrams/deepgp/deep-markov-vertical.svg", transparent=True)}

\newslide{}

\includesvg{../slides/diagrams/deepgp/deep-markov-vertical.svg}

### Why Deep?

\slides{* Gaussian processes give priors over functions.

* Elegant properties:
  * e.g. *Derivatives* of process are also Gaussian distributed (if they exist).

* For particular covariance functions they are ‘universal approximators’, i.e. all functions can have support under the prior.

* Gaussian derivatives might ring alarm bells.

* E.g. a priori they don’t believe in function ‘jumps’.
}
\notes{If the result of composing many functions together is simply another function, then why do we bother? The key point is that we can change the class of functions we are modeling by composing in this manner. A Gaussian process is specifying a prior over functions, and one with a number of elegant properties. For example, the derivative process (if it exists) of a Gaussian process is also Gaussian distributed. That makes it easy to assimilate, for example, derivative observations. But that also might raise some alarm bells. That implies that the *marginal derivative distribution* is also Gaussian distributed. If that's the case, then it means that functions which occasionally exhibit very large derivatives are hard to model with a Gaussian process. For example, a function with jumps in. 

A one off discontinuity is easy to model with a Gaussian process, or even multiple discontinuities. They can be introduced in the mean function, or independence can be forced between two covariance functions that apply in different areas of the input space. But in these cases we will need to specify the number of discontinuities and where they occur. In otherwords we need to *parameterise* the discontinuities. If we do not know the number of discontinuities and don't wish to specify where they occur, i.e. if we want a non-parametric representation of discontinuities, then the standard Gaussian process doesn't help.}

### Stochastic Process Composition

\slides{* From a process perspective: *process composition*.

* A (new?) way of constructing more complex *processes* based on simpler components.
}\notes{The deep Gaussian process leads to *non-Gaussian* models, and non-Gaussian characteristics in the covariance function. In effect, what we are proposing is that we change the properties of the functions we are considering by *composing stochastic processes$. This is an approach to creating new stochastic processes from well known processes.} 

\newslide{}

\includesvg{../slides/diagrams/deepgp/deep-markov-vertical.svg}

\plotcode{pgm = plot.vertical_chain(depth=5, shape=[2, 7])
pgm.add_node(daft.Node('y_2', r'$\mathbf{y}_2$', 1.5, 3.5, observed=True))
pgm.add_edge('f_2', 'y_2')
pgm.render().figure.savefig("../slides/diagrams/deepgp/deep-markov-vertical-side.svg", transparent=True)}

\newslide{}

\notes{Additionally, we are not constrained to the formalism of the chain. For example, we can easily add single nodes emerging from some point in the depth of the chain. This allows us to combine the benefits of the graphical modelling formalism, but with a powerful framework for relating one set of variables to another, that of Gaussian processes}
\includesvg{../slides/diagrams/deepgp/deep-markov-vertical-side.svg}


