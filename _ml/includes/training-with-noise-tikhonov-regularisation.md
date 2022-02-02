\ifndef{trainingWithNoiseTikhonovRegularisation}
\define{trainingWithNoiseTikhonovRegularisation}

\editme

\subsection{Training with Noise}

\notes{In practice, and across the last two waves of neural networks, other techniques for regularization have been used which can be seen as perturbing the neural network in some way. For example, in dropout [@Srivastava-dropout14], different basis functions are eliminated from the gradient computation at each gradient update.}

\notes{Many of these perturbations have some form of regularizing effect. The exact nature of the effect is not always easy to characterize, but in some cases, we can assess how these manipulations effect the model. For example, @Bishop:noise95 analyzed training with 'noisy inputs' and showed conditions under which it's equivalent to Tikhonov regularization.}

\notes{But in general, these approaches can have different interpretations and they've also been related to ensemble learning (e.g. related to *bagging* or Bayesian approaches).}

\slides{* Other regularisation approaches such as *dropout* [@Srivastava-dropout14]
* Often perturbing the neural network structure or inputs.
* Can have elegant interpretations (see e.g. @Bishop:noise95)
* Also interpreted as *ensemble* or *Bayesian* methods.
}


\endif
