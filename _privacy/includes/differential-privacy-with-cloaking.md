\ifndef{differentialPrivacyWithCloaking}
\define{differentialPrivacyWithCloaking}

\editme

\subsection{Cloaking}

* So far we've made the whole posterior mean function private...

    ...what if we just concentrate on making particular predictions private?


\newslide{Effect of perturbation}

* Standard approach: sample the noise is from the GP's
**prior**.

* Not necessarily the most 'efficient' covariance to use.

\newslide{Cloaking}

\includediagram{\diagramsDir/privacy/dp-firstpoint000}{80%}

*Left*: Function change. *Right*: test point change

\newslide{Cloaking}

\includediagram{\diagramsDir/privacy/dp-firstpoint002}{80%}

*Left*: Function change. *Right*: test point change

\newslide{Cloaking}

\includediagram{\diagramsDir/privacy/dp-secondpoint000}{80%}

*Left*: Function change. *Right*: test point change

\newslide{Cloaking}

\includediagram{\diagramsDir/privacy/dp-secondpoint002}{80%}

*Left*: Function change. *Right*: test point change

\newslide{Cloaking}

\includediagram{\diagramsDir/privacy/dp-with-ellipse001}{80%}

*Left*: Function change. *Right*: test point change

\newslide{Cloaking}

\includediagram{\diagramsDir/privacy/dp-with-ellipse002}{80%}

*Left*: Function change. *Right*: test point change

\newslide{DP Vectors}{data-background="\writeDiagramsDir/pres_bg.png"}

* Hall et al. (2013) also presented a bound on vectors.

* Find a bound ($\Delta$) on the scale of the output change, in term of
its Mahalanobis distance (wrt the added noise covariance).

    $$\sup_{D \sim {D^\prime}} ||\mathbf{M}^{-1/2} (\dataVector_* - \dataVector_{*}^\prime)||_2 \leq \Delta$$

* We use this to scale the noise we add:

    $$\frac{\text{c}(\delta)\Delta}{\varepsilon} \mathcal{N}_d(0,\mathbf{M})$$

    We get to pick $\mathbf{M}$


\newslide{Cloaking}{data-background="\writeDiagramsDir/pres_bg.png"}

* Intuitively we want to construct $\mathbf{M}$ so that it has greatest
covariance in those directions most affected by changes in training
points, so that it will be most able to mask those changes.

* The change in posterior mean predictions is,

  $$\dataVector_* - \dataVector^\prime_* = \kernelMatrix_{*f} \kernelMatrix^{-1} (\dataVector-\dataVector^\prime)$$

* Effect of perturbing each training point on each test point is
represented in the cloaking matrix,

  $$\mathbf{C} = \kernelMatrix_{*f} \kernelMatrix^{-1}$$


\newslide{Cloaking}{data-background="\writeDiagramsDir/pres_bg.png"}

* We assume we are protecting only one training input's change, by at most
$d$.

* So $\dataVector-\dataVector^\prime$ will be all zeros except for one
element, $i$.\

* So the change in test points will be (at most)

  $$\dataVector_*^\prime - \dataVector_* = d \mathbf{C}_{:i}$$

* We're able to write the earlier bound as,

  $$d^2 \sup_{i} \mathbf{c}_i^\top \mathbf{M}^{-1} \mathbf{c}_i \leq\Delta$$

  where $\mathbf{c}_i \triangleq \mathbf{C}_{:i}$


\newslide{Cloaking}{data-background="\writeDiagramsDir/pres_bg.png"}

* Dealing with $d$ elsewhere and setting $\Delta = 1$ (thus $0 \leq
\mathbf{c}_i^\top \mathbf{M}^{-1} \mathbf{c}_i \leq 1$) and minimise
$\log |\mathbf{M}|$ (minimises the partial entropy).

* Using Lagrange multipliers and gradient descent, we find
  $$
  \mathbf{M} = \sum_i{\lambda_i \mathbf{c}_i \mathbf{c}_i^\top}
  $$

\newslide{Cloaking: Results}

The noise added by this method is now practical.

\figure{\includepng{\diagramsDir/privacy/kung_cloaking_simple}{100%}{negate}}{}{kung-cloaking-simple}

EQ kernel, $l = 25$ years, $\Delta=100$cm, $\varepsilon=1$

\newslide{Cloaking: Results}{data-background="\writeDiagramsDir/pres_bg.png"}

It also has some interesting features;

-   Less noise where data is concentrated
-   Least noise far from any data
-   Most noise just outside data

\newslide{Cloaking: Results}

\figure{\includepng{\diagramsDir/privacy/kung_cloaking_simple}{100%}{negate}}{Simple cloaking function.}{kung-cloaking-simple}


\newslide{House Prices Around London}

\figure{\includepng{\diagramsDir/privacy/houseprices_bigcirc_15km_0_labels}{60%}{negate}}{Simple cloaking function on house price data.}{house-prices-cloaking}

\newslide{Citibike}

* Tested on 4D citibike dataset (predicting journey durations from
start/finish station locations).

* The method appears to achieve lower noise than binning alternatives (for
reasonable $\varepsilon$).

\newslide{Citibike}

\figure{\includepng{\diagramsDir/privacy/newtable2}{80%}{negate}}{Citibike data. Lengthscale in degrees, values above, journey duration (in seconds).}{citibike-data} 

\slides{lengthscale in degrees, values above, journey duration (in seconds)}

\newslide{Cloaking and Inducing Inputs}

* Outliers poorly predicted.

* Too much noise around data 'edges'.

* Use inducing inputs to reduce the sensitivity to these outliers.

\newslide{Cloaking (no) Inducing Inputs}

\figure{\includepng{\diagramsDir/privacy/cloaking-no-inducing}{100%}{negate}}{Cloaking function with no inducing inputs.}{cloaking-no-inducing}

\newslide{Cloaking and Inducing Inputs}

\figure{\includepng{\diagramsDir/privacy/cloaking-inducing}{80%}{negate}}{Cloaking function with inducing inputs.}{cloaking-inducing}

\newslide{Results}

* For 1D !Kung, RMSE improved from $15.0 \pm 2.0 \text{cm}$ to $11.1 \pm 0.8 \text{cm}$

    Use Age and Weight to predict Height

* For 2D !Kung, RMSE improved from $22.8 \pm 1.9 \text{cm}$ to $8.8 \pm 0.6 \text{cm}$

    Note that the uncertainty across cross-validation runs smaller. 2D version benefits from data's 1D manifold.

\newslide{Cloaking (no) Inducing Inputs}

\figure{\includepng{\diagramsDir/privacy/housing-no-inducing}{80%}{negate}}{Cloaking functions on the housing data with no inducing inputs.}{cloaking-housing-no-inducing}

\newslide{Cloaking and Inducing Inputs}

\figure{\includepng{\diagramsDir/privacy/housing-inducing}{80%}{negate}}{Cloaking functions on the housing data with inducing inputs.}{cloaking-housing-inducing}

\endif
