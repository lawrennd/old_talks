\ifndef{olympicSprintGp}
\define{olypmicSprintGp}

talk-macros.gpp}atasets/includes/olympic-sprint-data.md}

\editme

\subsection{Gaussian Process Fit}

\notes{We will perform a multi-output Gaussian process fit to the data, we'll do this using the [GPy software](https://github.com/SheffieldML/GPy).}

\installcode{GPy}

\notes{We will look at modelling the data using coregionalization approaches described in this morning's lecture. We introduced these approaches through the Kronecker product. To indicate we want to construct a covariance function of this type in GPy we've overloaded the `**` operator. Stricly speaking this operator means to the power of (like `^` in MATLAB). But for covariance functions we've used it to indicate a tensor product. The linear models of coregionalization we introduced in the lecture were all based on combining a matrix with a standard covariance function. We can think of the matrix as a particular type of covariance function, whose elements are referenced using the event indices. I.e. $k(0, 0)$ references the first row and column of the coregionalization matrix. $k(1, 0)$ references the second row and first column of the coregionalization matrix. Under this set up, we want to build a covariance where the first column from the features (the years) is passed to a covariance function, and the second column from the features (the event number) is passed to the coregionalisation matrix. Let's start by trying a intrinsic coregionalisation model (sometimes known as multitask Gaussian processes). Let's start by checking the help for the `Coregionalize` covariance.}

\setupcode{import GPy}

\code{GPy.kern.Coregionalize?}

\notes{The coregionalize matrix, $\mathbf{B}$, is itself is constructed from two other matrices, $\mathbf{B} = \mathbf{W}\mathbf{W}^\top + \text{diag}(\boldsymbol{\kappa})$. This allows us to specify a low rank form for the coregionalization matrix. However, for our first example we want to specify that the matrix $\mathbf{B}$ is not constrained to have a low rank form.}


\code{kern = GPy.kern.RBF(1, lengthscale=80)**GPy.kern.Coregionalize(1,output_dim=6, rank=5)}

\notes{Note here that the rank we specify is that of the $\mathbf{W}\mathbf{W}^\top$ part. When this part is combined with the diagonal matrix from $\mathbf{\kappa}$ the matrix $\mathbf{B}$ is totally general. This covariance function can now be used in a standard Gaussian process regression model. Let's build the model and optimize it.}


\code{model = GPy.models.GPRegression(X, y, kern)
model.optimize()}

\notes{We can plot the results using the ability to 'fix inputs' in the `model.plot()` function. We can specify that column 1 should be fixed to event number 2 by passing `fixed_inputs = [(1, 2)]` to the model. To plot the results for all events on the same figure we also specify `fignum=1` in the loop as below. }


\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
for i in range(6):
    model.plot(ax = ax, fixed_inputs=[(1, i)])
ax.set_xlabel('years')
ax.set_ylabel('time/s')

mlai.write_figure('olympic-sprint-gp.svg',
                 directory='\writeDiagramsDir/gp')}

\newslide{Olympic Marathon Data GP}

\figure{\includediagram{\diagramsDir/gp/olympic-sprint-gp}}{Gaussian process fit to the Olympic Sprint data.}{olympic-sprint-gp}

\notes{There is a lot we can do with this model. First of all, each of the races is a different length, so the series have a different mean. We can include another coregionalization term to deal with the mean. Below we do this and reduce the rank of the coregionalization matrix to 1.}

\code{kern1 = GPy.kern.RBF(1, lengthscale=80)**GPy.kern.Coregionalize(1, output_dim=6, rank=1)
kern2 = GPy.kern.Bias(1)**GPy.kern.Coregionalize(1,output_dim=6, rank=1)
kern = kern1 + kern2}

\code{model = GPy.models.GPRegression(X, y, kern)
model.optimize()}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
for i in range(6):
    model.plot(ax=ax, fignum=1,fixed_inputs=[(1, i)])
ax.set_xlabel('years')
ax.set_ylabel('time/s')

mlai.write_figure('olympic-sprint-lmc-gp.svg',
                 directory='\writeDiagramsDir/gp')}

\newslide{Olympic Marathon Data LMC GP}

\figure{\includediagram{\diagramsDir/gp/olympic-sprint-lmc-gp}}{Gaussian process fit to the Olympic Sprint data.}{olympic-sprint-lmc-gp}


\notes{This is a simple form of the linear model of coregionalization. Note how confident the model is about what the women's 400 m performance would have been. You might feel that the model is being over confident in this region. Perhaps we are forcing too much sharing of information between the sprints. We could return to the intrinsic coregionalization model and force the two base covariance functions to share the same coregionalization matrix.}


\code{kern1 = GPy.kern.RBF(1, lengthscale=80) + GPy.kern.Bias(1)
kern2 = GPy.kern.Coregionalize(1, output_dim=6, rank=5)
kern = kern1**kern2}

\code{model = GPy.models.GPRegression(X, y, kern)
model.optimize()}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
for i in range(6):
    model.plot(fignum=1,fixed_inputs=[(1, i)])
ax.set_xlabel('years')
ax.set_ylabel('time/s')

mlai.write_figure('olympic-sprint-icm-gp.svg',
                  directory='\writeDiagramsDir/gp')}

\newslide{Olympic Marathon Data ICM GP}

\figure{\includediagram{\diagramsDir/gp/olympic-sprint-icm-gp}}{Gaussian process fit to the Olympic Sprint data.}{olympic-sprint-icm-gp}


\codeAssignment{Can you fix the issue with over confidence in this model? Some things you might try include (a) adding additional covariance functions to handle shorter lengthscale effects. (b) Changing the rank of the coregionalization matrix. (c) Adding a coregionalized noise model using `GPy.kern.white()`.}{}{10}

\notes{Predictions in the multioutput case can be very effected by our covariance function *design*. This reflects the themes we saw on the first day where the importance of covariance function choice was emphasized at design time.}


\endif
