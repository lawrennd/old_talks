\ifndef{differentialPrivacyForGps}
\define{differentialPrivacyForGps}

\editme

\newslide{Differential Privacy, summary}{data-background="\diagramsDir/pres_bg.png"}

* We want to protect a user from a linkage attack...

    ...while still performing inference over the whole group.

* Making a dataset private is more than just erasing names.

@Narayanan:nosilver14;@Ohm:broken10;@BarthJones:governor12

* To achieve a level of privacy one needs to add **randomness** to the
data.

* This is a fundamental feature of differential privacy.

See [The Algorithmic Foundations of Differential
Privacy](https://www.cis.upenn.edu/~aaroth/Papers/privacybook.pdf) by
@Dwork:algorithmic14 for a rigorous introduction to the framework.


\subsection{Differential Privacy for Gaussian Processes}

We have a dataset in which the inputs, $\inputMatrix$, are **public**. The
outputs, $\dataVector$, we want to keep **private**.

\includepng{\diagramsDir/privacy/kung_pseudo_pert}{65%}{negate}

**Data consists of the heights and weights of 287 women from a census of
the !Kung [@Howell:kungsan67]**

\newslide{Vectors and Functions}

@Hall:dpfunctions13 showed that one can ensure that a version of $\mappingFunction$,
function $\tilde{f}$ is $(\varepsilon, \delta)$-differentially
private by adding a scaled sample from a GP prior.

\includeimg{\diagramsDir/privacy/hall1.png}{30%}{negate}

3 pages of maths ahead!

\newslide{Applied to Gaussian Processes}{data-background="\diagramsDir/pres_bg.png"}

* We applied this method to the GP posterior.

* The covariance of the posterior only depends on the inputs, $\inputMatrix$. So we
can compute this without applying DP.

* The mean function, $\mappingFunction_D(\inputVector_*)$, does depend on
$\dataVector$.
    $$\mappingFunction_D(\inputVector_*) = \kernelVector(x_*, \inputMatrix)
\kernelMatrix^{-1} \dataVector$$

* We are interested in finding

    $$|| \mappingFunction_D(\inputVector_*) -
\mappingFunction_{D^\prime}(\inputVector_*) ||_H^2$$

    ...how much the mean function (in RKHS) can change due to a change in
$\dataVector$.


\newslide{Applied to Gaussian Processes}{data-background="\diagramsDir/pres_bg.png"}

* Using the representer theorem, we can write
    $$|| \mappingFunction_D(\inputVector_*) -
	\mappingFunction_{D^\prime}(\inputVector_*) ||_H^2$$
	
    as:

    $$\Big|\Big|\sum_{i=1}^\numData \kernelScalar(\inputVector_*,\inputVector_i)
\left(\alpha_i - \alpha^\prime_i\right)\Big|\Big|_H^2$$

     where $\boldsymbol{\alpha} - \boldsymbol{\alpha}^\prime = \kernelMatrix^{-1}
\left(\dataVector - \dataVector^\prime \right)$


\newslide{}{data-background="\diagramsDir/pres_bg.png" }

* L2 Norm

    $$\Big|\Big|\sum_{i=1}^\numData \kernelScalar(\inputVector_*,\inputVector_i)
\left(\alpha_i - \alpha^\prime_i\right)\Big|\Big|_H^2$$

    where $\boldsymbol{\alpha} - \boldsymbol{\alpha}^\prime = \kernelMatrix^{-1}
\left(\dataVector - \dataVector^\prime \right)$

* We constrain the kernel: $-1\leq \kernelScalar(\cdot,\cdot) \leq 1$ and we only allow one
element of $\dataVector$ and $\dataVector^\prime$ to differ (by at most
$d$).

* So only one column of $\kernelMatrix^{-1}$ will be involved in the change of mean
(which we are summing over).

* The distance above can then be shown to be no greater than
$d\;||\kernelMatrix^{-1}||_\infty$


\newslide{Applied to Gaussian Processes}

This 'works' in that it allows DP predictions...but to avoid too much
noise, the value of $\varepsilon$ is too large (here it is 100)

\includepng{\diagramsDir/privacy/kung_standard_simple}{50%}{negate}

EQ kernel, $\lengthScale = 25$ years, $\Delta=100$cm


\newslide{Inducing Inputs}

Using sparse methods (i.e. inducing inputs) can help reduce the
sensitivity a little. We'll see more on this later.

\includepng{\diagramsDir/privacy/kung_inducing_simple}{70%}{negate}

\endif
