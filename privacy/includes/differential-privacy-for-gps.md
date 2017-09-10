### Differential Privacy, summary {data-background="../slides/diagrams/pres_bg.png"}


* We want to protect a user from a linkage attack...

    ...while still performing inference over the whole group.

* Making a dataset private is more than just erasing names.

* To achieve a level of privacy one needs to add **randomness** to the
data.

* This is a fundamental feature of differential privacy.

See [The Algorithmic Foundations of Differential
Privacy](https://www.cis.upenn.edu/~aaroth/Papers/privacybook.pdf) by
Dwork and Roth for a rigorous introduction to the framework.


### Differential Privacy for Gaussian Processes {data-transition="None"}

We have a dataset in which the inputs, $\mathbf{X}$, are **public**. The
outputs, $\mathbf{y}$, we want to keep **private**.

![Data consists of the heights and weights of 287 women from a census of
the !Kung](../slides/diagrams/kung_pseudo_pert_neg.png){width="65%" style="border:none" align="center"}

**Data consists of the heights and weights of 287 women from a census of
the !Kung**

### Vectors and Functions {data-transition="None"}

Hall et al. (2013) showed that one can ensure that a version of $f$,
function $\tilde{f}$ is $(\varepsilon, \delta)$-differentially
private by adding a scaled sample from a GP prior.

![](../slides/diagrams/hall1_neg.png){width="30%" style="border:none" align="center"}

3 pages of maths ahead!

### Applied to Gaussian Processes  {data-background="../slides/diagrams/pres_bg.png"}

* We applied this method to the GP posterior.

* The covariance of the posterior only depends on the inputs, $X$. So we
can compute this without applying DP.

* The mean function, $f_D(\mathbf{x_*})$, does depend on
$\mathbf{y}$.
    $$f_D(\mathbf{x_*}) = \mathbf{k}(x_*, \mathbf{X})
\mathbf{K}^{-1} \mathbf{y}$$

* We are interested in finding

    $$|| f_D(\mathbf{x_*}) -
f_{D^\prime}(\mathbf{x_*}) ||_H^2$$

    ...how much the mean function (in RKHS) can change due to a change in
$\mathbf{y}$.


### Applied to Gaussian Processes {data-background="../slides/diagrams/pres_bg.png"}

* Using the representer theorem, we can write
    $$|| f_D(\mathbf{x_*}) -
	f_{D^\prime}(\mathbf{x_*}) ||_H^2$$
	
    as:

    $$\Big|\Big|\sum_{i=1}^n k(\mathbf{x_*},\mathbf{x}_i)
\left(\alpha_i - \alpha^\prime_i\right)\Big|\Big|_H^2$$

     where $\boldsymbol{\alpha} - \boldsymbol{\alpha}^\prime = \mathbf{K}^{-1}
\left(\mathbf{y} - \mathbf{y}^\prime \right)$


### {data-background="../slides/diagrams/pres_bg.png" }

* L2 Norm

    $$\Big|\Big|\sum_{i=1}^n k(\mathbf{x_*},\mathbf{x}_i)
\left(\alpha_i - \alpha^\prime_i\right)\Big|\Big|_H^2$$

    where $\boldsymbol{\alpha} - \boldsymbol{\alpha}^\prime = \mathbf{K}^{-1}
\left(\mathbf{y} - \mathbf{y}^\prime \right)$

* We constrain the kernel: $-1\leq k(\cdot,\cdot) \leq 1$ and we only allow one
element of $\mathbf{y}$ and $\mathbf{y}'$ to differ (by at most
$d$).

* So only one column of $\mathbf{K}^{-1}$ will be involved in the change of mean
(which we are summing over).

* The distance above can then be shown to be no greater than
$d\;||\mathbf{K}^{-1}||_\infty$


### Applied to Gaussian Processes {data-transition="None"}

This 'works' in that it allows DP predictions...but to avoid too much
noise, the value of $\varepsilon$ is too large (here it is 100)

![](../slides/diagrams/kung_standard_simple_neg.png){width="50%" style="border:none" align="center"}

EQ kernel, $\ell = 25$ years, $\Delta=100$cm


### Inducing Inputs {data-transition="None"}

Using sparse methods (i.e. inducing inputs) can help reduce the
sensitivity a little. We'll see more on this later.

![](../slides/diagrams/kung_inducing_simple_neg.png){width="70%" style="border:none" align="center"}
