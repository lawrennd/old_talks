\ifndef{singlecellBayesGplvm}
\define{singlecellBayesGplvm}

\include{_datasets/includes/singlecell-data.md}

\editme

\subsection{Bayesian GP-LVM}

\notes{Here we show the new code that uses the Bayesian GP-LVM to fit the data. This means we can automatically determine the dimensionality of the model whilst fitting a non-linear dimensionality reduction. The approximations we use also mean that it is faster than the original GP-LVM.}


\setupcode{import GPy}
\code{kernel=GPy.kern.RBF(5,ARD=1)+GPy.kern.Bias(5)
model = GPy.models.BayesianGPLVM(Y.values, 5, num_inducing=15, kernel=kernel)
model.optimize(messages=True)}

\setupplotcode{import matplotlib.pyplot as plt
import teaching_plots as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_figsize)
model.plot_latent(ax=ax, labels=data['labels'], marker='<>^vsd')

mlai.write_figure('singlecell-bayes-gplvm.svg', directory='\writeDiagramsDir/gplvm')}

\figure{\includediagram{\diagramsDir/gplvm/singlecell-bayes-gplvm}{60%}}{Visualisation of the @Guo:fate10 blastocyst development data with the Bayesian GP-LVM.}{singlecell-bayes-gplvm}

\newslide{}

\setupplotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
model.kern.plot_ARD(ax=ax)

mlai.write_figure('singlecell-bayes-gplvm-ard.svg', directory='\writeDiagramsDir/gplvm')}

\figure{\includediagram{\diagramsDir/gplvm/singlecell-bayes-gplvm-ard}{80%}}{The ARD parameters of the Bayesian GP-LVM for the @Guo:fate10 blastocyst development data.}{singlecell-bayes-gplvm-ard}

\notes{This gives a really nice result. Broadly speaking two latent dimensions dominate the representation. When we visualize using these two dimensions we can see the entire cell phylogeny laid out nicely in the two dimensions.}


\endif
