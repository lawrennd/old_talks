### Mathematically {data-transition="None"}

-   Composite *multivariate* function
    $$\mathbf{g}(\inputVector)=\mappingFunctionVector_5(\mappingFunctionVector_4(\mappingFunctionVector_3(\mappingFunctionVector_2(\mappingFunctionVector_1(\inputVector)))))$$


\plotcode{rc("font", **{'family':'sans-serif','sans-serif':['Helvetica'],'size':30})
rc("text", usetex=True)
pgm = plot.horizontal_chain(depth=5)
pgm.render().figure.savefig("../slides/diagrams/deepgp/deep-markov.svg", transparent=True)}

### Equivalent to Markov Chain {data-transition="None"}

-   Composite *multivariate* function

$$p(\dataVector|\inputVector)= p(\dataVector|\mappingFunctionVector_5)p(\mappingFunctionVector_5|\mappingFunctionVector_4)p(\mappingFunctionVector_4|\mappingFunctionVector_3)p(\mappingFunctionVector_3|\mappingFunctionVector_2)p(\mappingFunctionVector_2|\mappingFunctionVector_1)p(\mappingFunctionVector_1|\inputVector)$$

\includesvg{../slides/diagrams/deepgp/deep-markov.svg}

\plotcode{from matplotlib import rc
rc("font", **{'family':'sans-serif','sans-serif':['Helvetica'], 'size':15})
rc("text", usetex=True)
pgm = plot.vertical_chain(depth=5)
pgm.render().figure.savefig("../slides/diagrams/deepgp/deep-markov-vertical.svg", transparent=True)}

### {data-transition="None"}

\includesvg{../slides/diagrams/deepgp/deep-markov-vertical.svg}

### Why Deep? {data-transition="None"}

-   Gaussian processes give priors over functions.

-   Elegant properties:
    -   e.g. *Derivatives* of process are also Gaussian distributed (if
        they exist).

-   For particular covariance functions they are ‘universal
    approximators’, i.e. all functions can have support under the prior.

-   Gaussian derivatives might ring alarm bells.

-   E.g. a priori they don’t believe in function ‘jumps’.

### Process Composition {data-transition="none"}


-   From a process perspective: *process composition*.

-   A (new?) way of constructing more complex *processes* based on
    simpler components.


### {data-transition="None"}

\includesvg{../slides/diagrams/deepgp/deep-markov-vertical.svg}

\plotcode{
pgm = plot.vertical_chain(depth=5, shape=[2, 7])
pgm.add_node(daft.Node('y_2', r'$\mathbf{y}_2$', 1.5, 3.5, observed=True))
pgm.add_edge('f_2', 'y_2')
pgm.render().figure.savefig("../slides/diagrams/deepgp/deep-markov-vertical-side.svg", transparent=True)}

### {data-transition="None"}

\includesvg{../slides/diagrams/deepgp/deep-markov-vertical-side.svg}


