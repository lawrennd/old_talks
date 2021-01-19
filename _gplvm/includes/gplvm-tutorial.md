\ifndef{gplvmTutorial}
\define{gplvmTutorial}

\include{_gplvm/includes/gplvm-tutorial-data.md}

\editme

\subsection{Principal Component Analysis}

\notes{Principal component analysis (PCA) finds a rotation of the observed outputs, such that the rotated principal component (PC) space maximizes the variance of the data observed, sorted from most to least important (most to least variable in the corresponding PC).}

\notes{In order to apply PCA in an easy way, we have included a PCA module in pca.py. You can import the module by 
import <path.to.pca> (without the ending .py!). 
To run PCA on the digits we have to reshape (Hint: np.reshape ) digits . }

* What is the right shape $\numData \times \dataDim$ to use?

\notes{We will call the reshaped observed outputs $\dataMatrix$ in the following.}


\code{Yn = Y#Y-Y.mean()}

\notes{Now let's run PCA on the reshaped dataset $\dataMatrix$:}


\code{from GPy.util import pca
p = pca.pca(Y) # create PCA class with digits dataset}

\notes{The resulting plot will show the lower dimensional representation of the digits in 2 dimensions.}


\plotcode{
p.plot_fracs(20) # plot first 20 eigenvalue fractions
p.plot_2d(Y,labels=labels.flatten(), colors=colors)
pb.legend()}


\subsection{Gaussian Process Latent Variable Model}

\notes{The Gaussian Process Latent Variable Model (GP-LVM) [@Lawrence:pnpca05] embeds PCA into a Gaussian process framework, where the latent inputs $\latentMatrix$ are learnt as hyperparameters and the mapping variables $\mathbf{W}$ are integrated out. The advantage of this interpretation is it allows PCA to be generalized in a non linear way by replacing the resulting *linear* covariance witha  non linear covariance. But first, let's see how GPLVM is equivalent to PCA using an automatic relevance determination (ARD, see e.g. @Bishop:book06) linear kernel:}


\code{input_dim = 4 # How many latent dimensions to use
kernel = GPy.kern.Linear(input_dim, ARD=True) # ARD kernel
m = GPy.models.GPLVM(Yn, input_dim=input_dim, kernel=kernel)

m.optimize(messages=1, max_iters=1000) # optimize for 1000 iterations}

\plotcode{m.kern.plot_ARD()
plot_model(m.X, m.linear.variances.argsort()[-2:], labels.flatten())
pb.legend()}

\notes{As you can see the solution with a linear kernel is the same as the PCA solution with the exception of rotational changes and axis flips.}

\notes{For the sake of time, the solution you see was only running for 1000 iterations, thus it might not be converged fully yet. The GP-LVM proceeds by iterative optimization of the *inputs* to the covariance. As we saw in the lecture earlier, for the linear covariance, these latent points can be optimized with an eigenvalue problem, but generally, for non-linear covariance functions, we are obliged to use gradient based optimization.}

\writeAssignment{How do your linear solutions differ between PCA and GPLVM with a linear kernel? Look at the plots and also try and consider how the linear ARD parameters compare to the eigenvalues of the principal components.}

\codeAssignment{The next step is to use a non-linear mapping between inputs $\latentMatrix$ and ouputs $\dataMatrix$ by selecting the exponentiated quadratic (`GPy.kern.rbf`) covariance function.}

\writeAssignment{How does the nonlinear model differe from the linear model? Are there digits that the GPLVM with an exponentiated quadratic covariance can separate, which PCA is not able to?}

\codeAssignment{Try modifying the covariance function and running the model again. For example you could try a combination of the linear and exponentiated quadratic covariance function or the Matern 5/2. If you run into stability problems try initializing the covariance function parameters differently.}


\include{_gplvm/includes/cmu-mocap-gplvm.md}

\endif
