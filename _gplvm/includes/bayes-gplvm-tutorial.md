\ifndef{bayesGplvmTutorial}
\define{bayesGplvmTutorial}

talk-macros.gpp}plvm/includes/gplvm-tutorial-data.md}

\editme

\subsection{Bayesian GPLVM}

\notes{In GP-LVM we use a point estimate of the distribution of the input $\latentMatrix$. This estimate is derived through maximum likelihood or through a maximum a posteriori (MAP) approach. Ideally, we would like to also estimate a distribution over the input $\latentMatrix$. In the Bayesian GPLVM we approximate the true distribution $p(\latentMatrix|\dataMatrix)$ by a variational approximation $q(\latentMatrix)$ and integrate $\latentMatrix$ out [@Titsias:bayesGPLVM10].}

\notes{Approximating the posterior in this way allows us to optimize a lower bound on the marginal likelihood. Handling the uncertainty in a principled way allows the model to make an assessment of whether a particular latent dimension is required, or the variation is better explained by noise. This allows the algorithm to switch off latent dimensions. The switching off can take some time though, so below in Section 6 we provide a pre-learnt module, but to complete section 6 you'll need to be working in the IPython console instead of the notebook.}

\notes{For the moment we'll run a short experiment applying the Bayesian GP-LVM with an exponentiated quadratic covariance function.}


\code{
# Model optimization
input_dim = 5 # How many latent dimensions to use
kern = GPy.kern.RBF(input_dim,ARD=True) # ARD kernel
m = GPy.models.BayesianGPLVM(Yn, input_dim=input_dim, kernel=kern, num_inducing=25)

# initialize noise as 1% of variance in data
#m.likelihood.variance = m.Y.var()/100.
m.optimize(messages=1)}

\plotcode{# Plotting the model
plot_model(m.X.mean, m.rbf.lengthscale.argsort()[:2], labels.flatten())
pb.legend()
m.kern.plot_ARD()
# Saving the model:
m.pickle('digit_bgplvm_rbf.pickle')}


\notes{Because we are now also considering the uncertainty in the model, this optimization can take some time. However, you are free to interrupt the optimization at any point selecting `Kernel->Interupt` from the notepad menu. This will leave you with the model, `m` in the current state and you can plot and look into the model parameters. }

\writeAssignment{How does the Bayesian GP-LVM compare with the standard model?}


\subsection{Preoptimized Model}

\notes{A good way of working with latent variable models is to interact with the latent dimensions, generating data. This is a little bit tricky in the notebook, so below in section 6 we provide code for setting up an interactive demo in the standard IPython shell. If you are working on your own machine you can try this now. Otherwise continue with section 5.}

\subsection{Multiview Learning: Manifold Relevance Determination}

\notes{In Manifold Relevance Determination we try to find one latent space, common for $K$ observed output sets (modalities) $\{\dataMatrix_{k}\}_{k=1}^{K}$. Each modality is associated with a separate set of ARD parameters so that it switches off different parts of the whole latent space and, therefore, $\latentMatrix$ is softly segmented into parts that are private to some, or shared for all modalities. Can you explain what happens in the following example?}

\notes{Again, you can stop the optimizer at any point and explore the result obtained with the so far training:}


\code{m = GPy.examples.dimensionality_reduction.mrd_simulation(optimize = False, plot=False)
m.optimize(messages = True, max_iters=3e3, optimizer = 'bfgs')}

\plotcode{_ = m.X.plot()
m.plot_scales()}


\writeAssignment{The simulated data set is a sinusoid and a double frequency sinusoid function as input signals.

a) Which signal is shared across the three datasets? 
b) Which are private? 
c) Are there signals shared only between two of the three datasets?}{}{30}


\subsection{Interactive Demo: For Use Outside the Notepad}

\notes{The module below loads a pre-optimized Bayesian GPLVM model (like the one you just trained) and allows you to interact with the latent space. 
Three interactive figures pop up: the latent space, the ARD scales and a sample in the output space (corresponding to the current selected latent point of the other figure). 
You can sample with the mouse from the latent space and obtain samples in the output space. 
You can select different latent dimensions to vary by clicking on the corresponding scales with the left and right mouse buttons.
This will also cause the latent space to be projected on the selected latent dimensions in the other figure.}


\setupcode{import urllib2, os, sys}

\code{model_path =  'digit_bgplvm_demo.pickle' # local name for model file
status = ""

re = 0
if len(sys.argv) == 2:
    re = 1

if re or not os.path.exists(model_path): # only download the model new, if it was not already
    url = 'http://staffwww.dcs.sheffield.ac.uk/people/M.Zwiessele/gpss/lab3/digit_bgplvm_demo.pickle'
    with open(model_path, 'wb') as f:
        u = urllib2.urlopen(url)
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        print "Downloading: %s" % (model_path)

        file_size_dl = 0
        block_sz = 8192
        while True:
            buff = u.read(block_sz)
            if not buff:
                break
            file_size_dl += len(buff)
            f.write(buff)
            sys.stdout.write(" "*(len(status)) + "\r")
            status = r"{:7.3f}/{:.3f}MB [{: >7.2%}]".format(file_size_dl/(1.*1e6), file_size/(1.*1e6), float(file_size_dl)/file_size)
            sys.stdout.write(status)
            sys.stdout.flush()
        sys.stdout.write(" "*(len(status)) + "\r")
        print status
else:
    print("Already cached, to reload run with 'reload' as the only argument")}

\code{import cPickle as pickle
with open('./digit_bgplvm_demo.pickle', 'rb') as f:
    m = pickle.load(f)}

\notes{Prepare for plotting of this model. If you run on a webserver the interactive plotting will not work. Thus, you can skip to the next codeblock and run it on your own machine, later.}


\plotcode{fig = pb.figure('Latent Space & Scales', figsize=(16,6))
ax_latent = fig.add_subplot(121)
ax_scales = fig.add_subplot(122)

fig_out = pb.figure('Output', figsize=(1,1))
ax_image  = fig_out.add_subplot(111)
fig_out.tight_layout(pad=0)

data_show = GPy.plotting.matplot_dep.visualize.image_show(m.Y[0:1, :], dimensions=(16, 16), transpose=0, invert=0, scale=False, axes=ax_image)
lvm_visualizer = GPy.plotting.matplot_dep.visualize.lvm_dimselect(m.X.mean.copy(), m, data_show, ax_latent, ax_scales, labels=labels.flatten())}

\subsubsection{Observations}

\notes{Confirm the following observations by interacting with the demo:}

* We tend to obtain more "strange" outputs when sampling from latent space areas away from the training inputs.
* When sampling from the two dominant latent dimensions (the ones corresponding to large scales) we differentiate between all digits. Also note that projecting the latent space into the two dominant dimensions better separates the classes.
* When sampling from less dominant latent dimensions the outputs vary in a more subtle way.

\notes{You can also run the dimensionality reduction example}


\code{GPy.examples.dimensionality_reduction.bgplvm_simulation()}


\subsubsection{Questions}

* Can you see a difference in the ARD parameters to the non Bayesian GPLVM?
* How does the Bayesian GPLVM allow the ARD parameters of the RBF kernel magnify the two first dimensions?
* Is Bayesian GPLVM better in differentiating between different kinds of digits?
* Why does the starting noise variance have to be lower then the variance of the observed values?
* How come we use the lowest variance when using a linear kernel, but the highest lengtscale when using an RBF kernel?

\endif
