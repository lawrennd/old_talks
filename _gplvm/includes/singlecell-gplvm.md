\ifndef{singlecellGplvm}
\define{singlecellGplvm}

\include{_datasets/includes/singlecell-data.md}

\editme

\subsection{GP-LVM on the Data}

\centerdiv{\maxZwiesselePicture{15%}\oliverSteglePicture{15%}}

\notes{Work done as a collaboration between Max Zwiessele, Oliver Stegle and Neil D. Lawrence.}

\notes{Then, we follow @Buettner:resolving12 in applying the GP-LVM to the data. There is a slight pathology in the result, one which they fixed by using priors that were dependent on the developmental stage. We then show how the Bayesian GP-LVM doesn't exhibit those pathologies and gives a nice results that seems to show the lineage of the cells.}

\notes{They used modified prior to ensure that small differences between cells at the same differential stage were preserved. Here we apply a standard GP-LVM (no modified prior) to the data.}


\setupcode{import GPy}

\code{kernel = GPy.kern.RBF(2)+GPy.kern.Bias(2)
model = GPy.models.GPLVM(Y.values, 2, kernel=kernel)
model.optimize(messages=True)}


\setupplotcode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_figsize)
model.plot_latent(ax=ax, labels=data['labels'], marker='<>^vsd')

mlai.write_figure('singlecell-gplvm.svg', directory='\writeDiagramsDir/gplvm')}

\figure{\includediagram{\diagramsDir/gplvm/singlecell-gplvm}{60%}}{Visualisation of the @Guo:fate10 blastocyst development data with the GP-LVM.}{singlecell-gplvm}

\newslide{}

\setupplotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
model.kern.plot_ARD(ax=ax)

mlai.write_figure('singlecell-gplvm-ard.svg', directory='\writeDiagramsDir/gplvm')}

\figure{\includediagram{\diagramsDir/gplvm/singlecell-gplvm-ard}{80%}}{The ARD parameters of the GP-LVM for the @Guo:fate10 blastocyst development data.}{singlecell-gplvm-ard}



\endif
