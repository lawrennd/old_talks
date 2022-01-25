\ifndef{olympicMarathonPolynomial}
\define{olympicMarathonPolynomial}

\include{_datasets/includes/olympic-marathon-data.md}

\editme

\subsection{Polynomial Fits to Olympic Marthon Data}

\slides{* Fit linear model with polynomial basis to marathon data.
* Try different numbers of basis functions (different degress of polynomial).
* Check the quality of fit.}
\setupcode{import numpy as np}

\notes{Define the polynomial basis function.}

\loadcode{polynomial}{mlai}

\code{def polynomial(x, num_basis=4, data_limits=[-1., 1.]):
    "Polynomial basis"
    centre = data_limits[0]/2. + data_limits[1]/2.
    span = data_limits[1] - data_limits[0]
    z = np.asarray(x, dtype=float) - centre
    z = 2*z/span   # scale the inputs to be within -1, 1 where polynomials are well behaved
    Phi = np.zeros((x.shape[0], num_basis))
    for i in range(num_basis):
        Phi[:, i:i+1] = z**i
    return Phi}

\notes{Now we include the solution for the linear regression through QR-decomposition.}

\code{def basis_fit(Phi, y):
    "Use QR decomposition to fit the basis."""
	Q, R = np.linalg.qr(Phi)
	return sp.linalg.solve_triangular(R, Q.T@y) 
}

\subsection{Linear Fit}

\slides{$$\mappingFunction(x, \mappingVector) = \mappingScalar_0 + \mappingScalar_1\inputScalar$$}

\code{poly_args = {'num_basis':2, # two basis functions (1 and x)
             'data_limits':xlim}
Phi = polynomial(x, **poly_args)
w = basis_fit(Phi, y)}

\notes{Now we make some predictions for the fit.}

\code{x_pred = np.linspace(xlim[0], xlim[1], 400)[:, np.newaxis]
Phi_pred = polynomial(x_pred, **poly_args)
f_pred = Phi_pred@w}

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

mlai.write_figure(filename='olympic-marathon-polynomial-2.svg', 
				  directory='\writeDiagramsDir/ml')}

\figure{\includediagram{\diagramsDir/ml/olympic-marathon-polynomial-2}{80%}}{Fit of a 1 degree polynomial (a linear model) to the olympic marathon data.}{olympic-marathon-polynomial-2}


\subsection{Cubic Fit}

\slides{$$\mappingFunction(x, \mappingVector) = \mappingScalar_0 + \mappingScalar_1 \inputScalar + \mappingScalar_2 \inputScalar^2 + \mappingScalar_3 \inputScalar^3$$}

\code{poly_args = {'num_basis':4, # four basis: 1, x, x^2, x^3
             'data_limits':xlim}
Phi = polynomial(x, **poly_args)
w = basis_fit(Phi, y)}


\code{Phi_pred = polynomial(x_pred, **poly_args)
f_pred = Phi_pred@w}

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

mlai.write_figure(filename='olympic-marathon-polynomial-4.svg', 
				  directory='\writeDiagramsDir/ml')}

\figure{\includediagram{\diagramsDir/ml/olympic-marathon-polynomial-4}{80%}}{Fit of a 3 degree polynomial (a cubic model) to the olympic marathon data.}{olympic-marathon-polynomial-4}

\subsection{9th Degree Polynomial Fit}

\slides{$$\mappingFunction(x, \mappingVector) = \mappingScalar_0 + \mappingScalar_1 \inputScalar + \mappingScalar_2 \inputScalar^2 + \dots + \mappingScalar_9 \inputScalar^9$$}

\notes{Now we'll try a 9th degree polynomial fit to the data.}

\code{poly_args = {'num_basis':10, # basis up to x^9
             'data_limits':xlim}
Phi = polynomial(x, **poly_args)
w = basis_fit(Phi, y)}


\code{Phi_pred = polynomial(x_pred, **poly_args)
f_pred = Phi_pred@w}

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

mlai.write_figure(filename='olympic-marathon-polynomial-10.svg', 
				  directory='\writeDiagramsDir/ml')}

\figure{\includediagram{\diagramsDir/ml/olympic-marathon-polynomial-10}{80%}}{Fit of a 9 degree polynomial to the olympic marathon data.}{olympic-marathon-polynomial-10}
\subsection{16th Degree Polynomial Fit}

\slides{$$\mappingFunction(x, \mappingVector) = \mappingScalar_0 + \mappingScalar_1 \inputScalar + \mappingScalar_2 \inputScalar^2 + \dots + \mappingScalar_{16} \inputScalar^{16}$$}

\notes{Now we'll try a 16th degree polynomial fit to the data.}

\code{poly_args = {'num_basis':17, # basis up to x^16
             'data_limits':xlim}
Phi = polynomial(x, **poly_args)
w = basis_fit(Phi, y)}


\code{Phi_pred = polynomial(x_pred, **poly_args)
f_pred = Phi_pred@w}

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

mlai.write_figure(filename='olympic-marathon-polynomial-17.svg', 
				  directory='\writeDiagramsDir/ml')}

\figure{\includediagram{\diagramsDir/ml/olympic-marathon-polynomial-17}{80%}}{Fit of a 16 degree polynomial to the olympic marathon data.}{olympic-marathon-polynomial-17}

\subsection{26th Degree Polynomial Fit}

\slides{$$\mappingFunction(x, \mappingVector) = \mappingScalar_0 + \mappingScalar_1 \inputScalar + \mappingScalar_2 \inputScalar^2 + \dots + \mappingScalar_{26} \inputScalar^{26}$$}

\notes{Now we'll try a 26th degree polynomial fit to the data.}

\code{poly_args = {'num_basis':27, # basis up to x^26
             'data_limits':xlim}
Phi = polynomial(x, **poly_args)
w = basis_fit(Phi, y)}


\code{Phi_pred = polynomial(x_pred, **poly_args)
f_pred = Phi_pred@w}

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

mlai.write_figure(filename='olympic-marathon-polynomial-27.svg', 
				  directory='\writeDiagramsDir/ml')}

\figure{\includediagram{\diagramsDir/ml/olympic-marathon-polynomial-27}{80%}}{Fit of a 26 degree polynomial to the olympic marathon data.}{olympic-marathon-polynomial-27}



\endif
