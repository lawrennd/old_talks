\ifndef{linearMultifidelity}
\define{linearMultifidelity}

\editme

\subsection{Linear multi-fidelity model}

\notes{The linear multi-fidelity model proposed in
@Kennedy-predicting00 is widely viewed as a reference point for all
such models.  In this model, the high-fidelity (true) function is
modeled as a scaled sum of the low-fidelity function plus an error
term:}
$$
\mappingFunction_{\text{high}}(x) = \mappingFunction_{\text{err}}(x) + \rho \,\mappingFunction_{\text{low}}(x)
$$
\notes{In this equation, $\mappingFunction_{\text{low}}(x)$ is taken to be a Gaussian process modeling the outputs of the lower fidelity function, while $\rho$ is a scaling factor indicating the magnitude of the correlation to the high-fidelity data.
Setting this to 0 implies that there is no correlation between observations at different fidelities.
Meanwhile, $\mappingFunction_{\text{err}}(x)$ denotes yet another Gaussian process which models the bias term for the high-fidelity data.
Note that $\mappingFunction_{\text{err}}(x)$ and $\mappingFunction_{\text{low}}(x)$ are assumed to be independent processes which are only related by the equation given above.}

\notes{**Note**: While we shall limit our explanation to the case of two fidelities, this set-up can easily be generalized to cater for $T$ fidelities as follows:}
$$
\mappingFunction_{t}(x) = \mappingFunction_{t}(x) + \rho_{t-1} \,\mappingFunction_{t-1}(x), \quad t=1,\dots, T
$$
\notes{If the training points are sorted such that the low and high-fidelity points are grouped together:}
$$
\begin{pmatrix}
\inputMatrix_{\text{low}} \\
\inputMatrix_{\text{high}}
\end{pmatrix}
$$
\notes{we can express the model as a single Gaussian process having the following prior.}
$$
\begin{bmatrix}
\mappingFunction_{\text{low}}\left(h\right)\\
\mappingFunction_{\text{high}}\left(h\right)
\end{bmatrix}
\sim
GP
\begin{pmatrix}
\begin{bmatrix}
0 \\ 0
\end{bmatrix},
\begin{bmatrix}
\kernelScalar_{\text{low}} & \rho \kernelScalar_{\text{low}} \\
\rho \kernelScalar_{\text{low}} & \rho^2 \kernelScalar_{\text{low}} + \kernelScalar_{\text{err}}
\end{bmatrix}
\end{pmatrix}
$$

\subsubsection{Linear multi-fidelity modeling in Emukit}

\notes{As a first example of how the linear multi-fidelity model
implemented in `Emukit`
`emukit.multi_fidelity.models.GPyLinearMultiFidelityModel` can be
used, we shall consider the two-fidelity Forrester function.  This
benchmark is frequently used to illustrate the capabilities of
multi-fidelity models.}

\setupcode{import numpy as np}

\setupplotcode{import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)}

\code{np.random.seed(20)}

\setupcode{import GPy
import emukit.multi_fidelity
import emukit.test_functions
from emukit.model_wrappers.gpy_model_wrappers import GPyMultiOutputWrapper
from emukit.multi_fidelity.models import GPyLinearMultiFidelityModel}

\notes{Generate samples from the Forrester function}

\code{high_fidelity = emukit.test_functions.forrester.forrester
low_fidelity = emukit.test_functions.forrester.forrester_low

x_plot = np.linspace(0, 1, 200)[:, np.newaxis]
y_plot_l = low_fidelity(x_plot)
y_plot_h = high_fidelity(x_plot)

x_train_l = np.atleast_2d(np.random.rand(12)).T
x_train_h = np.atleast_2d(np.random.permutation(x_train_l)[:6])
y_train_l = low_fidelity(x_train_l)
y_train_h = high_fidelity(x_train_h)}

\notes{The inputs to the models are expected to take the form of
ndarrays where the last column indicates the fidelity of the observed
points.}

\notes{Although only the input points, $X$, are augmented with the
fidelity level, the observed outputs $Y$ must also be converted to
array form.}

\notes{For example, a dataset consisting of 3 low-fidelity points and
2 high-fidelity points would be represented as follows, where the
input is three-dimensional while the output is one-dimensional:}
$$
\inputMatrix = \begin{pmatrix}
\inputScalar_{\text{low};0}^0 & \inputScalar_{\text{low};0}^1 & \inputScalar_{\text{low};0}^2 & 0\\
\inputScalar_{\text{low};1}^0 & \inputScalar_{\text{low};1}^1 & \inputScalar_{\text{low};1}^2 & 0\\
\inputScalar_{\text{low};2}^0 & \inputScalar_{\text{low};2}^1 & \inputScalar_{\text{low};2}^2 & 0\\
\inputScalar_{\text{high};0}^0 & \inputScalar_{\text{high};0}^1 & \inputScalar_{\text{high};0}^2 & 1\\
\inputScalar_{\text{high};1}^0 & \inputScalar_{\text{high};1}^1 & \inputScalar_{\text{high};1}^2 & 1
\end{pmatrix}\quad
\dataMatrix = \begin{pmatrix}
\dataScalar_{\text{low};0}\\
\dataScalar_{\text{low};1}\\
\dataScalar_{\text{low};2}\\
\dataScalar_{\text{high};0}\\
\dataScalar_{\text{high};1}
\end{pmatrix}
$$
\notes{A similar procedure must be carried out for obtaining
predictions at new test points, whereby the fidelity indicated in the
column then indicates the fidelity at which the function must be
predicted for a designated point.}

\notes{For convenience of use, we provide helper methods for easily
converting between a list of arrays (ordered from the lowest to the
highest fidelity) and the required ndarray representation. This is
found in `emukit.multi_fidelity.convert_lists_to_array`.}

\notes{Convert lists of arrays to ndarrays augmented with fidelity indicators.}

\setupcode{from emukit.multi_fidelity.convert_lists_to_array import convert_x_list_to_array, convert_xy_lists_to_arrays}

\code{X_train, Y_train = convert_xy_lists_to_arrays([x_train_l, x_train_h], 
                                                    [y_train_l, y_train_h])}

\notes{Plot the original functions.}

\setupplotcode{import matplotlib.pyplot as plt
import teaching_plots as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)

ax.plot(x_plot, y_plot_l, 'b', linewidth=3)
ax.plot(x_plot, y_plot_h, 'r', linewidth=3)
ax.scatter(x_train_l, y_train_l, color='b', s=40)
ax.scatter(x_train_h, y_train_h, color='r', s=40)
ax.set_ylabel('$f(x)$')
ax.set_xlabel('$x$')
ax.legend(['Low fidelity', 'High fidelity'])

mlai.write_figure('high-and-low-fidelity-forrester.svg', directory='\writeDiagramsDir/uq')}

\figure{\includediagram{\diagramsDir/uq/high-and-low-fidelity-forrester}{80%}}{High and low fidelity Forrester functions.}{high-and-low-fidelity-forrester}


\notes{Observe that in the example above we restrict our observations
to 12 from the lower fidelity function and only 6 from the high
fidelity function.  As we shall demonstrate further below, fitting a
standard GP model to the few high fidelity observations is unlikely to
result in an acceptable fit, which is why we shall instead consider
the linear multi-fidelity model presented in this section.}

\notes{Below we fit a linear multi-fidelity model to the available low
and high fidelity observations. Given the smoothness of the functions,
we opt to use an exponentiated quadratic kernel for both the bias and correlation
components of the model.}

\notes{**Note**: The model implementation defaults to a `MixedNoise`
noise likelihood whereby there is independent Gaussian noise for each
fidelity.}

\notes{This can be modified upfront using the 'likelihood' parameter
in the model constructor, or by updating them directly after the model
has been created.  In the example below, we choose to fix the noise to
'0' for both fidelities in order to reflect that the observations are
exact.}

\notes{Construct a linear multi-fidelity model.}

\code{kernels = [GPy.kern.RBF(1), GPy.kern.RBF(1)]
lin_mf_kernel = emukit.multi_fidelity.kernels.LinearMultiFidelityKernel(kernels)
gpy_lin_mf_model = GPyLinearMultiFidelityModel(X_train, Y_train, lin_mf_kernel, n_fidelities=2)
gpy_lin_mf_model.mixed_noise.Gaussian_noise.fix(0)
gpy_lin_mf_model.mixed_noise.Gaussian_noise_1.fix(0)}

\notes{Wrap the model using the given `GPyMultiOutputWrapper`}

\code{lin_mf_model = GPyMultiOutputWrapper(gpy_lin_mf_model, 2, n_optimization_restarts=5)}

\notes{Fit the model}
  
\code{lin_mf_model.optimize()}

\notes{Convert x_plot to its ndarray representation.}

\code{X_plot = convert_x_list_to_array([x_plot, x_plot])
X_plot_l = X_plot[:len(x_plot)]
X_plot_h = X_plot[len(x_plot):]}

\notes{Compute mean predictions and associated variance.}

\code{lf_mean_lin_mf_model, lf_var_lin_mf_model = lin_mf_model.predict(X_plot_l)
lf_std_lin_mf_model = np.sqrt(lf_var_lin_mf_model)
hf_mean_lin_mf_model, hf_var_lin_mf_model = lin_mf_model.predict(X_plot_h)
hf_std_lin_mf_model = np.sqrt(hf_var_lin_mf_model)}

\notes{Plot the posterior mean and variance.}

\setupplotcode{import matplotlib.pyplot as plt
import teaching_plots as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.fill_between(x_plot.flatten(), (lf_mean_lin_mf_model - 1.96*lf_std_lin_mf_model).flatten(), 
                 (lf_mean_lin_mf_model + 1.96*lf_std_lin_mf_model).flatten(), facecolor='g', alpha=0.3)
ax.fill_between(x_plot.flatten(), (hf_mean_lin_mf_model - 1.96*hf_std_lin_mf_model).flatten(), 
                 (hf_mean_lin_mf_model + 1.96*hf_std_lin_mf_model).flatten(), facecolor='y', alpha=0.3)

ax.plot(x_plot, y_plot_l, 'b', linewidth=3)
ax.plot(x_plot, y_plot_h, 'r', linewidth=3)
ax.plot(x_plot, lf_mean_lin_mf_model, '--', color='g', linewidth=3)
ax.plot(x_plot, hf_mean_lin_mf_model, '--', color='y', linewidth=3)
ax.scatter(x_train_l, y_train_l, color='b', s=40)
ax.scatter(x_train_h, y_train_h, color='r', s=40)
ax.set_ylabel('$f(x)$')
ax.set_xlabel('$x$')
ax.legend(['Low Fidelity', 'High Fidelity', 'Predicted Low Fidelity', 'Predicted High Fidelity'])

mlai.write_figure('linear-multi-fidelity-model.svg', directory='\writeDiagramsDir/uq')}

\figure{\includediagram{\diagramsDir/uq/linear-multi-fidelity-model}{80%}}{Linear multi-fidelity model fit to low and high fidelity Forrester function}{linear-multi-fidelity-model}

\notes{The above plot demonstrates how the multi-fidelity model learns
the relationship between the low and high-fidelity observations in
order to model both of the corresponding functions.}

\notes{In this example, the posterior mean almost fits the true
function exactly, while the associated uncertainty returned by the
model is also appropriately small given the good fit.}

\subsubsection{Comparison to standard GP}

\notes{In the absence of such a multi-fidelity model, a regular
Gaussian process would have been fit exclusively to the high fidelity
data.}

\notes{As illustrated in the figure below, the resulting Gaussian
process posterior yields a much worse fit to the data than that
obtained by the multi-fidelity model. The uncertainty estimates are
also poorly calibrated.}

\notes{Create standard GP model using only high-fidelity data.}

\code{kernel = GPy.kern.RBF(1)
high_gp_model = GPy.models.GPRegression(x_train_h, y_train_h, kernel)
high_gp_model.Gaussian_noise.fix(0)}

\notes{Fit the GP model.}

\code{high_gp_model.optimize_restarts(5)}

\notes{Compute mean predictions and associated variance.}

\code{hf_mean_high_gp_model, hf_var_high_gp_model  = high_gp_model.predict(x_plot)
hf_std_hf_gp_model = np.sqrt(hf_var_high_gp_model)}

\notes{Plot the posterior mean and variance for the high-fidelity GP
model.}

\setupplotcode{import matplotlib.pyplot as plt
import teaching_plots as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)

ax.fill_between(x_plot.flatten(), (hf_mean_lin_mf_model - 1.96*hf_std_lin_mf_model).flatten(), 
                 (hf_mean_lin_mf_model + 1.96*hf_std_lin_mf_model).flatten(), facecolor='y', alpha=0.3)
ax.fill_between(x_plot.flatten(), (hf_mean_high_gp_model - 1.96*hf_std_hf_gp_model).flatten(), 
                 (hf_mean_high_gp_model + 1.96*hf_std_hf_gp_model).flatten(), facecolor='k', alpha=0.1)

ax.plot(x_plot, y_plot_h, color='r', linewidth=3)
ax.plot(x_plot, hf_mean_lin_mf_model, '--', color='y', linewidth=3)
ax.plot(x_plot, hf_mean_high_gp_model, 'k--', linewidth=3)
ax.scatter(x_train_h, y_train_h, color='r')
ax.set_xlabel('$x$')
ax.set_ylabel('$f(x)$')
ax.legend(['True Function', 'Linear Multi-fidelity GP', 'High fidelity GP'])

mlai.write_figure('linear-multi-fidelity-high-fidelity-gp.svg', directory='\writeDiagramsDir/uq')}

\figure{\includediagram{\diagramsDir/uq/linear-multi-fidelity-high-fidelity-gp}{80%}}{Comparison of linear multi-fidelity model and high fidelity GP}{linear-multi-fidelity-high-fidelity-gp}

\subsection{Nonlinear multi-fidelity model}

\notes{Although the model described above works well when the mapping
between the low and high-fidelity functions is linear, several issues
may be encountered when this is not the case.}

\notes{Consider the following example, where the low and high fidelity
functions are defined as follows:}
$$
\mappingFunction_{\text{low}}(\inputScalar) = \sin(8\pi \inputScalar)
$$

$$
\mappingFunction_{\text{high}}(\inputScalar) = \left(\inputScalar - \sqrt{2}\right) \, \mappingFunction_{\text{low}}^2
$$

\notes{Generate data for nonlinear example.}

\code{high_fidelity = emukit.test_functions.non_linear_sin.nonlinear_sin_high
low_fidelity = emukit.test_functions.non_linear_sin.nonlinear_sin_low}

\code{x_plot = np.linspace(0, 1, 200)[:, np.newaxis]
y_plot_l = low_fidelity(x_plot)
y_plot_h = high_fidelity(x_plot)

n_low_fidelity_points = 50
n_high_fidelity_points = 14

x_train_l = np.linspace(0, 1, n_low_fidelity_points)[:, np.newaxis]
y_train_l = low_fidelity(x_train_l)

x_train_h = x_train_l[::4, :]
y_train_h = high_fidelity(x_train_h)}

\notes{Convert lists of arrays to ND-arrays augmented with fidelity indicators}

\code{X_train, Y_train = convert_xy_lists_to_arrays([x_train_l, x_train_h], [y_train_l, y_train_h])}

\setupplotcode{import matplotlib.pyplot as plt
import teaching_plots as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)

ax.plot(x_plot, y_plot_l, 'b', linewidth=3)
ax.plot(x_plot, y_plot_h, 'r', linewidth=3)
ax.scatter(x_train_l, y_train_l, color='b', s=40)
ax.scatter(x_train_h, y_train_h, color='r', s=40)
ax.set_xlabel('$x$')
ax.set_ylabel('$f(x)$')
ax.set_xlim([0, 1])
ax.legend(['Low fidelity', 'High fidelity'])

mlai.write_figure('high-and-low-fidelity-functions.svg', directory='\writeDiagramsDir/uq')}

\figure{\includediagram{\diagramsDir/uq/high-and-low-fidelity-functions}{80%}}{High and low fidelity functions}{high-and-low-fidelity-functions}

\notes{In this case, the mapping between the two functions is
nonlinear, as can be observed by plotting the high fidelity
observations as a function of the lower fidelity observations.}

\setupplotcode{import matplotlib.pyplot as plt
import teaching_plots as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.set_ylabel('HF(x)')
ax.set_xlabel('LF(x)')
ax.plot(y_plot_l, y_plot_h, color=colors['purple'], linewidth=3)
ax.legend(['HF-LF Correlation'], loc='lower center')

mlai.write_figure('mapping-low-to-high-fidelity.svg', directory='\writeDiagrams/uq')}

\figure{\includediagram{\diagramsDir/uq/mapping-low-to-high-fidelity}{80}}{Mapping from low fidelity to high fidelity.}{mapping-low-to-high-fidelity}

\subsubsection{Failure of linear multi-fidelity model}

\notes{Below we fit the linear multi-fidelity model to this new problem and plot the results.}

\notes{Construct a linear multi-fidelity model.}

\code{kernels = [GPy.kern.RBF(1), GPy.kern.RBF(1)]
lin_mf_kernel = emukit.multi_fidelity.kernels.LinearMultiFidelityKernel(kernels)
gpy_lin_mf_model = GPyLinearMultiFidelityModel(X_train, Y_train, lin_mf_kernel, n_fidelities=2)
gpy_lin_mf_model.mixed_noise.Gaussian_noise.fix(0)
gpy_lin_mf_model.mixed_noise.Gaussian_noise_1.fix(0)

lin_mf_model = model = GPyMultiOutputWrapper(gpy_lin_mf_model, 2, n_optimization_restarts=5)}

\notes{Fit the model}
  
\code{lin_mf_model.optimize()}


\notes{Convert test points to appropriate representation}

\code{X_plot = convert_x_list_to_array([x_plot, x_plot])
X_plot_low = X_plot[:200]
X_plot_high = X_plot[200:]}

\notes{Compute mean and variance predictions}

\code{hf_mean_lin_mf_model, hf_var_lin_mf_model = lin_mf_model.predict(X_plot_high)
hf_std_lin_mf_model = np.sqrt(hf_var_lin_mf_model)}


\notes{Compare linear and nonlinear model fits}

\setupplotcode{import matplotlib.pyplot as plt
import teaching_plots as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.plot(x_plot, y_plot_h, 'r', linewidth=3)
ax.plot(x_plot, hf_mean_lin_mf_model, '--', color='y', linewidth=3)
ax.scatter(x_train_h, y_train_h, color='r')
ax.fill_between(x_plot.flatten(), (hf_mean_lin_mf_model - 1.96*hf_std_lin_mf_model).flatten(), 
                 (hf_mean_lin_mf_model + 1.96*hf_std_lin_mf_model).flatten(), color='y', alpha=0.3)
ax.set_xlim(0, 1)
ax.set_xlabel('$x$')
ax.set_ylabel('$f(x)$')
ax.legend(['True Function', 'Linear multi-fidelity GP'], loc='lower right')
mlai.write_figure('linear-multi-fidelity-model-fit.svg', diagrams='\writeDiagramsDir/uq/')}

\figure{\includediagram{\diagramsDir/uq/linear-multi-fidelity-model-fit}{80%}}{Linear multi-fidelity model fit to high fidelity function}{linear-multi-fidelity-model-fit}

\notes{As expected, the linear multi-fidelity model was unable to
capture the nonlinear relationship between the low and high-fidelity
data.  Consequently, the resulting fit of the true function is also
poor.}

\endif
