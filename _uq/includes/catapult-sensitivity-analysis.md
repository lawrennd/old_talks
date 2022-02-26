\ifndef{catapultSensitivityAnalysis}
\define{catapultSensitivityAnalysis}


\editme


\include{_uq/includes/catapult-simulation.md}

\notes{Before we perform sensitivity analysis, we need to build an emulator of the catapulter, which we do using our experimental design process.}

\include{_uq/includes/catapult-experimental-design.md}

\subsection{Sensitivity Analysis of a Catapult Simulation}

\notes{The final step is to compute the coefficients using the class `ModelBasedMonteCarloSensitivity` which directly calls the model and uses its predictive mean to compute the Monte Carlo estimates of the Sobol indices. We plot the estimates of the Sobol indices computed using a Gaussian process model trained on the observations we've acquired.}

\code{num_mc = 10000
senstivity = MonteCarloSensitivity(model = model_emukit, input_domain = space)
main_effects_gp, total_effects_gp, _ = senstivity.compute_effects(num_monte_carlo_points = num_mc)}

\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot
import mlai}

\setupplotcode{import pandas as pd}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)

main_effects_gp_plot = {ivar: main_effects_gp[ivar][0] for ivar in main_effects_gp}

d = {'GP Monte Carlo':main_effects_gp_plot}

pd.DataFrame(d).plot(kind='bar', ax=ax)
plt.ylabel('% of explained output variance')

mlai.write_figure(filename='first-order-sobol-indices-gp-catapult.svg', directory='./uq')}


\figure{\includediagram{\diagramsDir/uq/first-order-sobol-indices-gp-catapult}{80%}}{First Order sobol indices as estimated by GP-emulator based Monte Carlo on the catapult.}{first-order-sobol-indices-gp-catapult}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)

total_effects_gp_plot = {ivar: total_effects_gp[ivar][0] for ivar in total_effects_gp}

d = {'GP Monte Carlo':total_effects_gp_plot}

pd.DataFrame(d).plot(kind='bar', ax=ax)
ax.set_ylabel('% of explained output variance')

mlai.write_figure(filename='total-effects-sobol-indices-gp-catapult.svg', directory='\writeDiagramsDir/uq')}

\newslide{}

\figure{\includediagram{\diagramsDir/uq/total-effects-sobol-indices-gp-catapult}{80%}}{Total effects as estimated by GP based Monte Carlo on the catapult.}{total-effects-sobol-indices-gp-catapult}


\endif
