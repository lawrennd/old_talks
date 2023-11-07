\ifndef{logisticRegressionGoingFurther}
\define{logisticRegressionGoingFurther}

\editme

\subsection{Going Further: Optimization}

Other optimization techniques for generalized linear models include [Newton's method](http://en.wikipedia.org/wiki/Newton%27s_method), it requires you to compute the Hessian, or second derivative of the objective function.

Methods that are based on gradients only include [L-BFGS](http://en.wikipedia.org/wiki/Limited-memory_BFGS) and [conjugate gradients](http://en.wikipedia.org/wiki/Conjugate_gradient_method). Can you find these in python? Are they suitable for very large data sets?
}

\subsection{Other GLMs}

\slides{
* Logistic regression is part of a family known as *generalized linear models*
* They all take the form 
  $$g^{-1}(\mappingFunction_i(x)) = \mappingVector^\top \basisVector(\inputVector_i)$$
* Other examples include *Poisson regression*.}

\notes{We've introduced the formalism for generalized linear models. Have a think about how you might model count data using the [Poisson distribution](http://en.wikipedia.org/wiki/Poisson_distribution) and a log link function for the rate, $\lambda(\inputVector)$. If you want a data set you can try the `pods.datasets.google_trends()` for some count data.}


\include{_ml/includes/poisson-regression.md}

\endif
