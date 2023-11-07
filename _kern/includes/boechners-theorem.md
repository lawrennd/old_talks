\ifndef{bochnersTheorem}
\define{bochnersTheorem}

\editme

\subsection{Bochners Theoerem}

\slides{Given a positive finite Borel measure $\mu$ on the real line $\mathbb{R}$, the Fourier transform $Q$ of $\mu$ is the continuous function}
  $$
  Q(t) = \int_{\mathbb{R}} e^{-itx} \text{d} \mu(x).
  $$
\slides{$Q$ is continuous since for a fixed $x$, the function $e^{-itx}$ is continuous and periodic.  The function $Q$ is a positive definite function, i.e. the kernel $\kernelScalar(\inputScalar, \inputScalar^\prime)= Q(\inputScalar^\prime - \inputScalar)$ is positive definite.}
  
\slides{Bochner's theorem [@Bochner:book59] says the converse is true, i.e. every positive definite function $Q$ is the Fourier transform of a positive finite Borel measure.  A proof can be sketched as follows [@Stein:interpolation99]}
  
\notes{Imagine we are given data and we wish to generalize from it. Without making further assumptions, we have no more information than the given data set. We can think of this ssomewhat like a weighted sum of Dirac delta functions. The Dirac delta function is defined to be a function with an integral of one, which is zero at all places apart from zero, where it is infinite. Given observations at particular times (or locations) $\inputVector_i$ we can think of our observations as being a function,}
$$
\mappingFunction(\inputVector) = \sum_{i=1}^\numData y_i \delta(\inputVector-\inputVector_i),
$$
\notes{This function is highly discontinuous, imagine if we wished to smooth it by filtering in Fourier space. The Fourier transform of a function is given by,}
$$
F(\boldsymbol{\omega}) = \int_{-\infty}^\infty \mappingFunction(\inputVector) \exp\left(-i2\pi \boldsymbol{\omega}^\top \inputVector\right) \text{d} \inputVector
$$
\notes{and since our function is a series of delta functions the the transform is easy to compute,}
$$
F(\boldsymbol{\omega}) = \sum_{i=1}^\numData y_i\exp\left(-i 2\pi \boldsymbol{\omega}^\top \inputVector_i\right)
$$ 
\notes{which has a real part given by a weighted sum of cosines and a complex part given by a weighted sum of sines.}

\notes{One theorem that gives insight into covariances is Bochner's theorem. Bochner's theorem states that any positive filter in Fourier space gives rise to a valid covariance function. Further, it gives a relationship between the filter and the form of the covariance function. The form of the covariance is given by the [Fourier transform](http://en.wikipedia.org/wiki/Fourier_transform) of the filter, with the argument of the transform being replaced by the distance between the points.}

\notes{Fourier space is a transformed space of the original function to a new basis. The transformation occurs through a convolution with a sine and cosine basis. Given a function of time $\mappingFunction(t)$ the Fourier transform moves it to a weighted linear sum of a sine and cosine basis,}
$$
F(\omega) = \int_{-\infty}^\infty \mappingFunction(t) \left[\cos(2\pi \omega t) - i \sin(2\pi \omega t) \right]\text{d} t
$$
\notes{where is the imaginary basis, $i=\sqrt{-1}$. Through Euler's formula,}
$$
\exp(ix) = \cos x + i\sin x 
$$
we can re-express this form as 
$$
F(\omega) = \int_{-\infty}^\infty \mappingFunction(t) \exp(-i 2\pi\omega)\text{d} t
$$
\notes{which is a standard form for the Fourier transform. Fourier's theorem was that the *inverse* transform can also be expressed in a similar form so we have}
$$
\mappingFunction(t) = \int_{-\infty}^\infty F(\omega) \exp(2\pi\omega)\text{d} \omega.
$$
\notes{Although we've introduced the transform in the context of time Fourier's interest was an analytical theory of heat and the transform can be applied to a multidimensional spatial function, $\mappingFunction(\inputVector)$.}

\includegooglebook{TDQJAAAAIAAJ}{PA525}


\endif
