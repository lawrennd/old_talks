\ifndef{emukitNonlinearMultifidelity}
\define{emukitNonlinearMultifidelity}

\editme

\subsubsection{Nonlinear Multi-fidelity model}

\notes{In view of the deficiencies of the linear multi-fidelity model,
a nonlinear multi-fidelity model is proposed in @Pedikaris:nonlinear17
to better capture these correlations.  This nonlinear model
is constructed as follows:}
$$ 
\mappingFunction_{\text{high}}(x) = \rho( \, \mappingFunction_{\text{low}}(x)) + \delta(x) 
$$
\notes{Replacing the linear scaling factor with a non-deterministic
function results in a model which can thus capture the nonlinear
relationship between the fidelities.}

\notes{This model is implemented in Emukit as `emukit.multi_fidelity.models.NonLinearModel`.}

\notes{It is defined in a sequential manner where a Gaussian process
model is trained for every set of fidelity data available. Once again,
we manually fix the noise parameter for each model to 0. The
parameters of the two Gaussian processes are then optimized
sequentially, starting from the low-fidelity.}

\notes{Create nonlinear model.}

\setupcode{from emukit.multi_fidelity.models.non_linear_multi_fidelity_model import make_non_linear_kernels, NonLinearMultiFidelityModel}

\code{base_kernel = GPy.kern.RBF
kernels = make_non_linear_kernels(base_kernel, 2, X_train.shape[1] - 1)
nonlin_mf_model = NonLinearMultiFidelityModel(X_train, Y_train, n_fidelities=2, kernels=kernels, 
                                              verbose=True, optimization_restarts=5)
for m in nonlin_mf_model.models:
    m.Gaussian_noise.variance.fix(0)}
    
\code{nonlin_mf_model.optimize()}

\notes{Now we compute the mean and variance predictions}

\code{hf_mean_nonlin_mf_model, hf_var_nonlin_mf_model = nonlin_mf_model.predict(X_plot_high)
hf_std_nonlin_mf_model = np.sqrt(hf_var_nonlin_mf_model)

lf_mean_nonlin_mf_model, lf_var_nonlin_mf_model = nonlin_mf_model.predict(X_plot_low)
lf_std_nonlin_mf_model = np.sqrt(lf_var_nonlin_mf_model)}


\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.fill_between(x_plot.flatten(), (lf_mean_nonlin_mf_model - 1.96*lf_std_nonlin_mf_model).flatten(), 
                 (lf_mean_nonlin_mf_model + 1.96*lf_std_nonlin_mf_model).flatten(), color='g', alpha=0.3)
ax.fill_between(x_plot.flatten(), (hf_mean_nonlin_mf_model - 1.96*hf_std_nonlin_mf_model).flatten(), 
                 (hf_mean_nonlin_mf_model + 1.96*hf_std_nonlin_mf_model).flatten(), color='y', alpha=0.3)
ax.plot(x_plot, y_plot_l, 'b', linewidth=3)
ax.plot(x_plot, y_plot_h, 'r', linewidth=3)
ax.plot(x_plot, lf_mean_nonlin_mf_model, '--', color='g', linewidth=3)
ax.plot(x_plot, hf_mean_nonlin_mf_model, '--', color='y', linewidth=3)
ax.scatter(x_train_h, y_train_h, color='r')
ax.set_xlabel('$x$')
ax.set_ylabel('$f(x)$')
ax.set_xlim(0, 1)
ax.legend(['Low Fidelity', 'High Fidelity', 'Predicted Low Fidelity', 'Predicted High Fidelity'])

mlai.write_figure('nonlinear-multi-fidelity-model-fit.svg', directory='\writeDiagramsDir/uq')}

\newslide{}

\figure{\includediagram{\diagramsDir/uq/nonlinear-multi-fidelity-model-fit}{80%}}{Nonlinear multi-fidelity model fit to low and high-fidelity functions.}

\notes{Fitting the nonlinear fidelity model to the available data very
closely fits the high-fidelity function while also fitting the
low-fidelity function exactly.  This is a vast improvement over the
results obtained using the linear model.  We can also confirm that the
model is properly capturing the correlation between the low and
high-fidelity observations by plotting the mapping learned by the
model to the true mapping shown earlier.}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.plot(y_plot_l, y_plot_h, '-', color=colors['purple'], linewidth=3)
ax.plot(lf_mean_nonlin_mf_model, hf_mean_nonlin_mf_model, 'k--', linewidth=3)
ax.set_ylabel('$HF(x)$')
ax.set_xlabel('$LF(x)$')
ax.legend(['True HF-LF Correlation', 'Learned HF-LF Correlation'], loc='lower center')

mlai.write_figure('mapping-low-fidelity-to-high-fidelity.svg', directory='\writeDiagramsDir/uq')}

\newslide{}

\figure{\includediagram{\diagramsDir/uq/mapping-low-fidelity-to-high-fidelity}{80%}}{Mapping from low fidelity to high fidelity}{mapping-low-fidelity-to-high-fidelity}

\subsection{Deep Gaussian Processes}

\centerdiv{\andreasDamianouPicture{15%}}
\notes{These non-linear multi-fidelity models are an example of composing Gaussian processes together. This type of non-linear relationship leads to what we refer to as a Deep Gaussian process [@Damianou:deepgp13;@Lawrence:hgplvm07] which Andreas Damianou worked on for his PhD thesis [@Damianou:thesis2015].}

\notes{These ideas lead to the notion of 'deep emulation', where a number of emulators are chained together to represent a system.}

\endif
