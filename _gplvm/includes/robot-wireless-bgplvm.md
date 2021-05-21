\ifndef{robotWirelessBgplvm}
\define{robotWirelessBgplvm}

\editme

\include{_datasets/includes/robot-wireless-data.md}

\subsection{Bayesian GP-LVM fit to the Robot Wireless Data}


\setupbcode{import GPy}

\notes{Set up a Bayesian GP-LVM with four latent dimensions.}

\code{model = GPy.models.BayesianGPLVM(data['Y'], 4, num_inducing=25)}

\notes{Optimize the model.}

\code{model.optimize(messages=True, max_f_eval=10000)}

\setupplotcode{from matplotlib import pyplot as plt
import mlai.plot as plot
import mlai.mlai as ma}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_figsize)
model.plot_latent(ax=ax)
ma.write_figure(filename='\writeDiagramsDir/gplvm/robot-wireless-bgplvm.svg', 
            transparent=True, frameon=True)}


\endif
