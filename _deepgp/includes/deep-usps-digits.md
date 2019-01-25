\ifndef{deepUspsDigits}
\define{deepUspsDigits}
\editme

\credit{Zhenwen Dai and Neil D. Lawrence}

\notes{We now look at the deep Gaussian processes' capacity to perform unsupervised learning.

We will look at a sub-sample of the MNIST digit data set.}

\include{_deepgp/includes/pydeepgp-include.md}

\notes{First load in the MNIST data set from scikit learn. This can take a little while because it's large to download.}

\setupcode{from sklearn.datasets import fetch_mldata}
\code{mnist = fetch_mldata('MNIST original')}

\notes{Sub-sample the dataset to make the training faster.}

\setupcode{import numpy as np}
\code{np.random.seed(0)
digits = [0,1,2,3,4]
N_per_digit = 100
Y = []
labels = []
for d in digits:
    imgs = mnist['data'][mnist['target']==d]
    Y.append(imgs[np.random.permutation(imgs.shape[0])][:N_per_digit])
    labels.append(np.ones(N_per_digit)*d)
Y = np.vstack(Y).astype(np.float64)
labels = np.hstack(labels)
Y /= 255.}

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
from matplotlib import rc
import teaching_plots as plot
import mlai}
\displaycode{rc("font", **{'family':'sans-serif','sans-serif':['Helvetica'],'size':20})
fig, ax = plt.subplots(figsize=plot.big_figsize)
for d in digits:
    ax.plot(m.layer_1.X.mean[labels==d,0],m.layer_1.X.mean[labels==d,1],'.',label=str(d))
_ = plt.legend()
mlai.write_figure(figure=fig, filename="../slides/diagrams/deepgp/usps-digits-latent.svg", transparent=True)}

\newslide{}

\includediagram{../slides/diagrams/usps-digits-latent}

\notes{
\subsection{Visualize the latent space of the intermediate layer}

We can also visualize dimensions of the intermediate layer. First the lengthscale of those dimensions is given by
}
\code{m.obslayer.kern.lengthscale}

\setupdisplaycode{import matplotlib.pyplot as plt
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
        mlai.write_figure(figure=fig, filename="../slides/diagrams/deepgp/usps-digits-hidden-" + str(dims[0]) + '-' + str(dims[1]) + '.svg', transparent=True)}
		
\newslide{}

\includediagram{../slides/diagrams/usps-digits-hidden-1-0}

\newslide{}

\includediagram{../slides/diagrams/usps-digits-hidden-2-0}

\newslide{}

\includediagram{../slides/diagrams/usps-digits-hidden-3-0}

\newslide{}

\includediagram{../slides/diagrams/usps-digits-hidden-4-0}

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
mlai.write_figure(figure=fig, filename="../slides/diagrams/deepgp/digit-samples-deep-gp.svg", transparent=True)}

\newslide{}

\includediagram{../slides/diagrams/digit-samples-deep-gp}

\endif
