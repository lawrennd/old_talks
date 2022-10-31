---
title: "Practical 1"
practical: 1
featured_image: assets/images/practical-one.png
abstract: 
layout: practical
author:
- family: Ek 
  given: Carl Henrik
  institute: University of Cambridge
  url: http://carlhenrik.com
postsdir: ../../../mlatcl/mlphysical/_practicals/
date: 2022-10-27
transition: None
reveal: false
ipynb: true
---


\section{Sequential Decision Making}

\notes{This notebook will form part of your individual submission for the course. The notebook will roughly mimick the parts that are in the PDF worksheet. Your task is to complete the code that is missing in the parts below and answer the questions that we ask. The aim is not for you to solve the worksheet but rather for you to show your understanding of the material in the course, instead of re-running and aiming to get "perfect" results run things, make sure it is correct and then try to explain your results with a few sentences.}

\notes{First we need to implement the surrogate model, we will use a Gaussian process surrogate.}

\setupcode{import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.spatial.distance import cdist}

\code{def f(X, noise=0.0):
    return -(-np.sin(3*X) - X**2 + 0.7*X + noise*np.random.randn(*X.shape))

def squared_exponential_computer(x1,x2,theta):
    # compute the squared exponential covariance function
    return K

def gpposterior(x_star,X,Y,lengthScale,sigma):
    # return the posterior estimate of the GP
    return mu, varSigma

theta = np.zeros((2, ))
theta[0] = 0.3  # lengthscale
theta[1] = 1.0; # variance}

\notes{When we have the surrogate model up and running we need to implement the acquisition function.}

\code{def expected_improvement(f_star, mu, varSigma):
    # return the value of the acquisition function at each
    
    return alpha}
	
	
\notes{Once you have the above code up and running you should be able to reproduce the results that are in Figure 1 in the worksheet. Now lets try to run some additional experiments. First lets evaluate the effect of the initial start locations. Create a plot where on the x-axis have the number of times you have evaluated the true function and on the y-axis have the current minima, run the optimisation loop several times and plot the mean and two standard deviations for the minimal value at each iteration.}

\codeassignment{implement a loop that tries a set of random-restarts}{}{10}
\code{np.random.seed(42)
for j in range(0, n_starts):
    for k in range(0, n_evals):
	    # Your code here
}

{Explain why the plots looks this way? Does it make a difference how many initial points you start with?}

While the function have a local minima so it presents some challenges for optimisation it is still quite easy to find the minima. Let us try make the function a bit more challenging by adding a bit of noise to the function. 

\codeassignment{Implement an additional loop around the previous two loops which alters the amount of noise added.}

\code{# implement a loop that tries different noise-levels
np.random.seed(42)
for i in range(0, 10):
    y = f(x, noise[i])
    for j in range(0, n_starts):
        for k in range(0, n_evals):
	        # Your code here
}

\writeassignment{Explain the results by contrasting to the previous none-noisy evaluation. How does the "best" run compare to the "best" run in the previous example?}{}{}

\notes{As you have probably noticed the kernel-hyperparmeters have a huge effect on the results. This is a desirable effect as this is where we encode our knowledge of the function. We will now do one experiment where we will alter the lengthscale value and see how it effects the results.}

\subsection{Extra}

\notes{For a final extra experiment try to fit the kernel parameters inside the inner-loop. The way to do this is to maximise the marginal likelihood of the surrogate model using gradient descent. You can alter the numpy code that we have implemented to jax instead and which will allow you to use auto-differetiation to compute gradients. Now you can implement a simple gradient descent}

\setupcode{from jax import grad
import jax.numpy as jnp}

\code{def squared_exponential(x1, x2, theta):
    # theta[0] - variance
    # theta[1] - lengthscale
    if x2 == None:
        return theta[0]*jnp.exp(-cdist(x1, x1, metric='sqeuclidean')/theta[1]**2)
    else:
        return theta[0]*jnp.exp(-cdist(x1, x2, metric='sqeuclidean')/theta[1]**2)

def logmarginal_likelihood(x, y, theta):
    # implement the log-marginal likelihood of a GP
    
dLdtheta = grad(logmarginal_likelihood, argnums=2)
for i in range(1000):
    
    theta -= dLdtheta(w) * 0.01}

\writtenassignment{Explain the results that you get above. Do you think this is a good strategy?}{}{}

\section{Submission}

\notes{You can submit the notebook on Moodle. Name your notebook using your CRSid as `crsid_practical-one.ipynb` before submitting to Moodle.}


\notes{The deadline for the submission is Friday the 4th of November at 23:59.}
