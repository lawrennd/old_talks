\ifndef{olympicMarathonBootstrapPolynomial}
\define{olympicMarathonBootstrapPolynomial}

talk-macros.gpp}l/includes/olympic-marathon-polynomial.md}

\editme

\subsection{Bootstrap and Olympic Marathon Data}

\notes{First we define a function to bootstrap resample our dataset.}

\setupcode{import numpy as np}

\code{def bootstrap(X, y):
    "Return a bootstrap sample from a data set."
    n = X.shape[0]
    ind = np.random.choice(n, n, replace=True) # Sample randomly with replacement.
    return X[ind, :], y[ind, :]}


\code{num_bootstraps = 10}

\code{def bootstrap_fit(Phi, y, size):
    W = np.zeros((Phi.shape[1], size))
    for i in range(size):
	    Phi_hat, y_hat = bootstrap(Phi, y)
    	W[:, i:i+1] = basis_fit(Phi_hat, y_hat)
	return W}

\subsection{Linear Fit}

\slides{$$\mappingFunction(x, \mappingVector) = \mappingScalar_0 + \mappingScalar_1 \inputScalar$$}

\code{poly_args = {'num_basis':2, # two basis functions (1 and x)
             'data_limits':xlim}
Phi = polynomial(x, **poly_args)
W_hat = bootstrap_fit(Phi, y, num_bootstraps)}

\notes{Now we make some predictions for the fit.}

\code{x_pred = np.linspace(xlim[0], xlim[1], 400)[:, np.newaxis]
Phi_pred = polynomial(x_pred, **poly_args)
f_pred = Phi_pred@W_hat}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
_ = ax.plot(x, y, 'r.',markersize=10)
ax.set_xlabel('year', fontsize=20)
ax.set_ylabel('pace min/km', fontsize=20)
ax.set_xlim(xlim)
ax.set_ylim(ylim)

_ = ax.plot(x_pred, f_pred, 'b-', linewidth=2)

mlai.write_figure(filename='olympic-marathon-bootstrap-polynomial-2.svg', 
				  directory='\writeDiagramsDir/ml')}

\figure{\includediagram{\diagramsDir/ml/olympic-marathon-bootstrap-polynomial-2}{80%}}{Fit of a 1 degree polynomial (a linear model) to the olympic marathon data.}{olympic-marathon-bootstrap-polynomial-2}


\subsection{Cubic Fit}

\slides{$$\mappingFunction(x, \mappingVector) = \mappingScalar_0 + \mappingScalar_1 \inputScalar + \mappingScalar_2 \inputScalar^2 + \mappingScalar_{3} \inputScalar^3$$}

\code{poly_args = {'num_basis':4, # four basis: 1, x, x^2, x^3
             'data_limits':xlim}
Phi = polynomial(x, **poly_args)
W_hat = bootstrap_fit(Phi, y, num_bootstraps)}


\code{Phi_pred = polynomial(x_pred, **poly_args)
f_pred = Phi_pred@W_hat}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
_ = ax.plot(x, y, 'r.',markersize=10)
ax.set_xlabel('year', fontsize=20)
ax.set_ylabel('pace min/km', fontsize=20)
ax.set_xlim(xlim)
ax.set_ylim(ylim)

_ = ax.plot(x_pred, f_pred, 'b-', linewidth=2)

mlai.write_figure(filename='olympic-marathon-bootstrap-polynomial-4.svg', 
				  directory='\writeDiagramsDir/ml')}

\figure{\includediagram{\diagramsDir/ml/olympic-marathon-bootstrap-polynomial-4}{80%}}{Fit of a 3 degree polynomial (a cubic model) to the olympic marathon data.}{olympic-marathon-bootstrap-polynomial-4}

\subsection{9th Degree Polynomial Fit}

\slides{$$\mappingFunction(x, \mappingVector) = \mappingScalar_0 + \mappingScalar_1 \inputScalar + \mappingScalar_2 \inputScalar^2 + \dots + \mappingScalar_{9} \inputScalar^{9}$$}

\notes{Now we'll try a 9th degree polynomial fit to the data.}

\code{poly_args = {'num_basis':10, # basis up to x^9
             'data_limits':xlim}
Phi = polynomial(x, **poly_args)
W_hat = bootstrap_fit(Phi, y, num_bootstraps)}


\code{Phi_pred = polynomial(x_pred, **poly_args)
f_pred = Phi_pred@W_hat}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
_ = ax.plot(x, y, 'r.',markersize=10)
ax.set_xlabel('year', fontsize=20)
ax.set_ylabel('pace min/km', fontsize=20)
ax.set_xlim(xlim)
ax.set_ylim(ylim)

_ = ax.plot(x_pred, f_pred, 'b-', linewidth=2)

mlai.write_figure(filename='olympic-marathon-bootstrap-polynomial-10.svg', 
				  directory='\writeDiagramsDir/ml')}

\figure{\includediagram{\diagramsDir/ml/olympic-marathon-bootstrap-polynomial-10}{80%}}{Fit of a 9 degree polynomial to the olympic marathon data.}{olympic-marathon-bootstrap-polynomial-10}


\subsection{16th Degree Polynomial Fit}

\slides{$$\mappingFunction(x, \mappingVector) = \mappingScalar_0 + \mappingScalar_1 \inputScalar + \mappingScalar_2 \inputScalar^2 + \dots + \mappingScalar_{16} \inputScalar^{16}$$}

\notes{Now we'll try a 16th degree polynomial fit to the data.}

\code{poly_args = {'num_basis':17, # basis up to x^16
             'data_limits':xlim}
Phi = polynomial(x, **poly_args)
W_hat = bootstrap_fit(Phi, y, num_bootstraps)}


\code{Phi_pred = polynomial(x_pred, **poly_args)
f_pred = Phi_pred@W_hat}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
_ = ax.plot(x, y, 'r.',markersize=10)
ax.set_xlabel('year', fontsize=20)
ax.set_ylabel('pace min/km', fontsize=20)
ax.set_xlim(xlim)
ax.set_ylim(ylim)

_ = ax.plot(x_pred, f_pred, 'b-', linewidth=2)

mlai.write_figure(filename='olympic-marathon-bootstrap-polynomial-17.svg', 
				  directory='\writeDiagramsDir/ml')}

\figure{\includediagram{\diagramsDir/ml/olympic-marathon-bootstrap-polynomial-17}{80%}}{Fit of a 16 degree polynomial to the olympic marathon data.}{olympic-marathon-bootstrap-polynomial-17}




                            
\endif
