\ifndef{deepNeuralNetworksAsPointEstimates}
\define{deepNeuralNetworksAsPointEstimates}

\editme

\subsection{Deep NNs as Point Estimates for Deep GPs}

\centerdiv{\vincentDutordoirPicture{15%}}
\slides{@Dutordoir-deepnns21}
\figure{\includepng{\diagramsDir/deepgp/deep-nns-as-point-estimates}{60%}}{Deep Neural Networks as Point Estimates for Deep Gaussian Processes by @Dutordoir-deepnns21 shows how deep neural networks can represent the mean function of an approximate deep GP.}{deep-nns-as-point-estimates}

\notes{A very promising idea was recently presented by @Dutordoir-deepnns21. They note that the ReLU activiation functions we use in the neural network can be seen as the consequence of a basis function defined on a circle (or a hypersphere in higher dimensions) being projected onto the real line (or hyperplane) as show in Figure \ref{relu-mapping-spherical}. This allows them to construct a covariance function on the hypersphere that is *stationary*.}

\subsection{ReLU as a Spherical Basis}

\figure{\includediagram{\diagramsDir/deepgp/relu-mapping-spherical}{70%}}{The rectified linear unit can be seen as a basis function that lives on a spherical domain being projected onto the real line.}{relu-mapping-spherical}{relu-mapping-spherical}

\newslide{Soft Plus as a Stationary Spherical}

\figure{\includediagram{\diagramsDir/deepgp/soft-plus-mapping-spherical}{70%}}{The soft ReLU can also be seen as a basis function that lives on a spherical domain being projected onto the real line.}{soft-plus-mapping-spherical}{soft-plus-mapping-spherical}

\subsection{Spherical Harmonics}

\figure{\includepng{\diagramsDir/deepgp/spherical-harmonics}{60%}}{The method exploits interdomain inducing variables, reinterpreting the ReLU covariance function as a stationary covariance on the spherical domain that has been projected to the real line.}{spherical-harmonics}

\notes{Applying variational inference techniques to the resulting model (see e.g. @Hensman:bigdata13,@Hensman:nested14) and making use of interdomain variational approximations (@Lazaro:spectrum10,@Alvarez:efficient10,@Hensman-variational18) causes the *mean function* approximation of the Gaussian process to have the same form as a fully connected deep neural network. This inspires the idea to use a trained neural network to initialise the deep Gaussian process.}


\subsection{Predictions on Banana Data}

\figure{\includediagram{\diagramsDir/deepgp/deep-nn-point-banana-data}{60%}}{The banana data is an artificially sampled data set with two classes (from @Raetsch:soft01).}{deep-nn-point-banana-data}

\newslide{Predictions on Banana Data}

\figure{\includediagram{\diagramsDir/deepgp/deep-nn-point-banana-deep-nn}{60%}}{One layer deep GP fit showing the neural network point estimate (from @Dutordoir-deepnns21).}{deep-nn-point-banana-deep-nn}

\newslide{Predictions on Banana Data}

\figure{\includediagram{\diagramsDir/deepgp/deep-nn-point-banana-deep-gp}{60%}}{One layer deep GP fit showing the activated deep Gaussian process fit (from @Dutordoir-deepnns21).}{deep-nn-point-banana-deep-gp}

\notes{The results of doing this on the banana data (Figure \ref{deep-nn-point-banana-data} @Raetsch:soft01) can be seen with the neural network solution in Figure \ref{deep-nn-point-banana-nn} and the neural network activated deep GP solution given in Figure \ref{deep-nn-point-banana-deep-gp}.}

\endif
