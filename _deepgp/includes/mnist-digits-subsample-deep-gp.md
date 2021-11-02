\ifndef{mnistDigitsSubsampleDeepGp}
\define{mnistDigitsSubsampleDeepGp}

\include{_ml/includes/mnist-digits-subsample-data.md}

\editme

\subsection{Fitting a Deep GP to a the MNIST Digits Subsample}

\centerdiv{\zhenwenDaiPicture{15%}\andreasDamianouPicture{15%}}

\notes{We now look at the deep Gaussian processes' capacity to perform unsupervised learning.}

\include{_deepgp/includes/pydeepgp-include.md}

\notes{
\subsection{Fit a Deep GP}

We're going to fit a Deep Gaussian process model to the MNIST data with two hidden layers. Each of the two Gaussian processes (one from the first hidden layer to the second, one from the second hidden layer to the data) has an exponentiated quadratic covariance.
}
\setupcode{import deepgp
import GPy}

\code{num_latent = 2
num_hidden_2 = 5
m = deepgp.DeepGP([Y.shape[1],num_hidden_2,num_latent],
                  Y,
                  kernels=[GPy.kern.RBF(num_hidden_2,ARD=True), 
                           GPy.kern.RBF(num_latent,ARD=False)], 
                  num_inducing=50, back_constraint=False, 
                  encoder_dims=[[200],[200]])}
				  
\notes{
\subsection{Initialization}

Just like deep neural networks, there are some tricks to intitializing these models. The tricks we use here include some early training of the model with model parameters constrained. This gives the variational inducing parameters some scope to tighten the bound for the case where the noise variance is small and the variances of the Gaussian processes are around 1. 
}

\code{m.obslayer.likelihood.variance[:] = Y.var()*0.01
for layer in m.layers:
    layer.kern.variance.fix(warning=False)
    layer.likelihood.variance.fix(warning=False)}
	
\notes{We now we optimize for a hundred iterations with the constrained model.}

\code{m.optimize(messages=False,max_iters=100)}

\notes{Now we remove the fixed constraint on the kernel variance parameters, but keep the noise output constrained, and run for a further 100 iterations. }

\code{for layer in m.layers:
    layer.kern.variance.constrain_positive(warning=False)
m.optimize(messages=False,max_iters=100)}

\notes{Finally we unconstrain the layer likelihoods and allow the full model to be trained for 1000 iterations.}

\code{for layer in m.layers:
    layer.likelihood.variance.constrain_positive(warning=False)
m.optimize(messages=True,max_iters=10000)}

\notes{
\subsection{Visualize the latent space of the top layer}

Now the model is trained, let's plot the mean of the posterior distributions in the top latent layer of the model. }

\setupdisplaycode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\setupdisplaycode{from matplotlib import rc}

\displaycode{rc("font", **{'family':'sans-serif','sans-serif':['Helvetica'],'size':20})
fig, ax = plt.subplots(figsize=plot.big_figsize)
for d in digits:
    ax.plot(m.layer_1.X.mean[labels==d,0],m.layer_1.X.mean[labels==d,1],'.',label=str(d))
_ = plt.legend()
mlai.write_figure(figure=fig, filename="\writeDiagramsDir/deepgp/mnist-digits-subsample-latent.svg", transparent=True)}

\newslide{}

\figure{\includediagram{\diagramsDir/deepgp/mnist-digits-subsample-latent}{60%}}{Latent space for the deep Gaussian process learned through unsupervised learning and fitted to a subset of the MNIST digits subsample.}{mnist-digits-subsample-latent}

\notes{
\subsection{Visualize the latent space of the intermediate layer}

We can also visualize dimensions of the intermediate layer. First the lengthscale of those dimensions is given by
}
\code{m.obslayer.kern.lengthscale}

\setupdisplaycode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\displaycode{fig, ax = plt.subplots(figsize=plot.big_figsize)
for i in range(5):
    for j in range(i):
        dims=[i, j]
        ax.cla()
        for d in digits:
            ax.plot(m.obslayer.X.mean[labels==d,dims[0]],
                 m.obslayer.X.mean[labels==d,dims[1]],
                 '.', label=str(d))
        plt.legend()
        plt.xlabel('dimension ' + str(dims[0]))
        plt.ylabel('dimension ' + str(dims[1]))
        mlai.write_figure(figure=fig, filename="\writeDiagramsDir/deepgp/mnist-digits-subsample-hidden-" + str(dims[0]) + '-' + str(dims[1]) + '.svg', transparent=True)}
		
\newslide{}

\figure{\includediagram{\diagramsDir/deepgp/mnist-digits-subsample-hidden-1-0}{60%}}{Visualisation of the intermediate layer, plot of dimension 1 vs dimension 0.}{mnist-digits-subsample-hidden-1-0}

\newslide{}

\figure{\includediagram{\diagramsDir/deepgp/mnist-digits-subsample-hidden-2-0}{60%}}{Visualisation of the intermediate layer, plot of dimension 1 vs dimension 0.}{mnist-digits-subsample-hidden-1-0}

\newslide{}

\figure{\includediagram{\diagramsDir/deepgp/mnist-digits-subsample-hidden-3-0}{60%}}{Visualisation of the intermediate layer, plot of dimension 1 vs dimension 0.}{mnist-digits-subsample-hidden-1-0}

\newslide{}

\figure{\includediagram{\diagramsDir/deepgp/mnist-digits-subsample-hidden-4-0}{60%}}{Visualisation of the intermediate layer, plot of dimension 1 vs dimension 0.}{mnist-digits-subsample-hidden-1-0}

\notes{
\subsection{Generate From Model}

Now we can take a look at a sample from the model, by drawing a Gaussian random sample in the latent space and propagating it through the model.}

\code{
rows = 10
cols = 20
t=np.linspace(-1, 1, rows*cols)[:, None]
kern = GPy.kern.RBF(1,lengthscale=0.05)
cov = kern.K(t, t)
x = np.random.multivariate_normal(np.zeros(rows*cols), cov, num_latent).T
}

\setupdisplaycode{import matplotlib.pyplot as plt
import mlai.plot as plot
import mlai}

\displaycode{yt = m.predict(x)
fig, axs = plt.subplots(rows,cols,figsize=(10,6))
for i in range(rows):
    for j in range(cols):
        #v = np.random.normal(loc=yt[0][i*cols+j, :], scale=np.sqrt(yt[1][i*cols+j, :]))
        v = yt[0][i*cols+j, :]
        axs[i,j].imshow(v.reshape(28,28), 
                        cmap='gray', interpolation='none',
                        aspect='equal')
        axs[i,j].set_axis_off()
mlai.write_figure(figure=fig, filename="\writeDiagramsDir/deepgp/digit-samples-deep-gp.svg", transparent=True)}

\newslide{}

\figure{\includediagram{\diagramsDir/deepgp/digit-samples-deep-gp}{80%}}{These digits are produced by taking a tour of the two dimensional latent space (as described by a Gaussian process sample) and mapping the tour into the data space. We visualize the mean of the mapping in the images.}{digit-samples-deep-gp}

\endif
