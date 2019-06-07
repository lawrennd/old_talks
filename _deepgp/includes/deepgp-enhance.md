\ifndef{deepGpEnhanced}
\define{deepGpEnhanced}
\editme

\notes{The deep Gaussian process code we are using is research code by Andreas Damianou. 

To extend the research code we introduce some approaches to initialization and optimization that we'll use in examples. These approaches can be found in the ```deepgp_tutorial.py``` file.}

\notes{Deep Gaussian process models also can require some thought in the initialization. Here we choose to start by setting the noise variance to be one percent of the data variance.}

\loadcode{initialize}{deepgp_tutorial}

\notes{Secondly, we introduce a staged optimization approach.}

\notes{Optimization requires moving variational parameters in the hidden layer representing the mean and variance of the expected values in that layer. Since all those values can be scaled up, and this only results in a downscaling in the output of the first GP, and a downscaling of the input length scale to the second GP. It makes sense to first of all fix the scales of the covariance function in each of the GPs.

Sometimes, deep Gaussian processes can find a local minima which involves increasing the noise level of one or more of the GPs. This often occurs because it allows a minimum in the KL divergence term in the lower bound on the likelihood. To avoid this minimum we habitually train with the likelihood variance (the noise on the output of the GP) fixed to some lower value for some iterations.


Next an optimization of the kernel function parameters at each layer is performed, but with the variance of the likelihood fixed. Again, this is to prevent the model minimizing the Kullback-Leibler divergence between the approximate posterior and the prior *before* achieving a good data-fit. 

Finally, all parameters of the model are optimized together.}

\loadcode{staged_optimize}{deepgp_tutorial}

\notes{The next code is for visualizing the intermediate layers of the deep model. This visualization is only appropriate for models with intermediate layers containing a single latent variable.}

\loadcode{visualize}{deepgp_tutorial}

\notes{The pinball visualization is to bring the pinball-analogy to life in the model. It shows how a ball would fall through the model to end up in the right pbosition. This visualization is only appropriate for models with intermediate layers containing a single latent variable.}

\loadcode{visualize_pinball}{deepgp_tutorial}

\notes{The ```posterior_sample``` code allows us to see the output sample locations for a given input. This is useful for visualizing the non-Gaussian nature of the output density.}

\loadcode{posterior_sample}{deepgp_tutorial}

\notes{Finally, we bind these methods to the DeepGP object for ease of calling.}

\helpercode{deepgp.DeepGP.initialize=initialize
deepgp.DeepGP.staged_optimize=staged_optimize
deepgp.DeepGP.posterior_sample = posterior_sample
deepgp.DeepGP.visualize=visualize
deepgp.DeepGP.visualize_pinball=visualize_pinball}

\endif
