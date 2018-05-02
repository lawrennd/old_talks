### Cloaking {data-transition="None"}

* So far we've made the whole posterior mean function private...

    ...what if we just concentrate on making particular predictions private?


### Effect of perturbation {data-transition="None"}

* Standard approach: sample the noise is from the GP's
**prior**.

* Not necessarily the most 'efficient' covariance to use.

### Cloaking {#cloaking-1 data-transition="None"}

\includesvg{../slides/diagrams/privacy/dp-firstpoint000.svg}

*Left*: Function change. *Right*: test point change

### Cloaking {#cloaking-1 data-transition="None"}

\includesvg{../slides/diagrams/privacy/dp-firstpoint002.svg}

*Left*: Function change. *Right*: test point change

### Cloaking {#cloaking-1 data-transition="None"}

\includesvg{../slides/diagrams/privacy/dp-secondpoint000.svg}

*Left*: Function change. *Right*: test point change

### Cloaking {#cloaking-1 data-transition="None"}

\includesvg{../slides/diagrams/privacy/dp-secondpoint002.svg}

*Left*: Function change. *Right*: test point change

### Cloaking {#cloaking-1 data-transition="None"}

\includesvg{../slides/diagrams/privacy/dp-with-ellipse001.svg}

*Left*: Function change. *Right*: test point change

### Cloaking {#cloaking-1 data-transition="None"}

\includesvg{../slides/diagrams/privacy/dp-with-ellipse002.svg}

*Left*: Function change. *Right*: test point change

### DP Vectors  {data-background="../slides/diagrams/pres_bg.png"}

* Hall et al. (2013) also presented a bound on vectors.

* Find a bound ($\Delta$) on the scale of the output change, in term of
its Mahalanobis distance (wrt the added noise covariance).

    $$\sup_{D \sim {D^\prime}} ||\mathbf{M}^{-1/2} (\dataVector_* - \dataVector_{*}^\prime)||_2 \leq \Delta$$

* We use this to scale the noise we add:

    $$\frac{\text{c}(\delta)\Delta}{\varepsilon} \mathcal{N}_d(0,\mathbf{M})$$

    We get to pick $\mathbf{M}$


### Cloaking  {data-background="../slides/diagrams/pres_bg.png"}

* Intuitively we want to construct $\mathbf{M}$ so that it has greatest
covariance in those directions most affected by changes in training
points, so that it will be most able to mask those changes.

* The change in posterior mean predictions is,

     $$\dataVector_* - \dataVector^\prime_* = \kernelMatrix_{*f} \kernelMatrix^{-1} (\dataVector-\dataVector^\prime)$$

* Effect of perturbing each training point on each test point is
represented in the cloaking matrix,

    $$\mathbf{C} = \kernelMatrix_{*f} \kernelMatrix^{-1}$$


### Cloaking  {data-background="../slides/diagrams/pres_bg.png"}

* We assume we are protecting only one training input's change, by at most
$d$.

* So $\dataVector-\dataVector^\prime$ will be all zeros except for one
element, $i$.\

* So the change in test points will be (at most)

    $$\dataVector_*^\prime - \dataVector_* = d \mathbf{C}_{:i}$$

* We're able to write the earlier bound as,

    $$d^2 \sup_{i} \mathbf{c}_i^\top \mathbf{M}^{-1} \mathbf{c}_i \leq\Delta$$

    where $\mathbf{c}_i \triangleq \mathbf{C}_{:i}$


### Cloaking  {data-background="../slides/diagrams/pres_bg.png"}

* Dealing with $d$ elsewhere and setting $\Delta = 1$ (thus $0 \leq
\mathbf{c}_i^\top \mathbf{M}^{-1} \mathbf{c}_i \leq 1$) and minimise
$\log |\mathbf{M}|$ (minimises the partial entropy).

* Using Lagrange multipliers and gradient descent, we find

    $$\mathbf{M} = \sum_i{\lambda_i \mathbf{c}_i \mathbf{c}_i^\top}$$

### Cloaking: Results {data-transition="None"}

The noise added by this method is now practical.

\includeimg{../slides/diagrams/kung_cloaking_simple.png}{100%}{negate}

EQ kernel, $l = 25$ years, $\Delta=100$cm, $\varepsilon=1$

### Cloaking: Results {data-background="../slides/diagrams/pres_bg.png"}

It also has some interesting features;

-   Less noise where data is concentrated
-   Least noise far from any data
-   Most noise just outside data

### Cloaking: Results  {data-transition="None"}

\includeimg{../slides/diagrams/kung_cloaking_simple.png}{100%}{negate}


### House Prices Around London  {data-transition="None"}

\includeimg{../slides/diagrams/houseprices_bigcirc_15km_0_labels.png}{60%}{negate}

### Citibike {#citibike data-transition="None"}

* Tested on 4D citibike dataset (predicting journey durations from
start/finish station locations).

* The method appears to achieve lower noise than binning alternatives (for
reasonable $\varepsilon$).

### Citibike {data-transition="None"}

\includeimg{../slides/diagrams/privacy/newtable2.png}{80%}{negate} lengthscale in degrees, values
above, journey duration (in seconds)

### Cloaking and Inducing Inputs {#cloaking-and-inducing-inputs}

* Outliers poorly predicted.

* Too much noise around data 'edges'.

* Use inducing inputs to reduce the sensitivity to these outliers.

### Cloaking (no) Inducing Inputs {#cloaking-no-inducing-inputs  data-transition="None"}

\includeing{../slides/diagrams/privacy/cloaking-no-inducing.png}{100%}{negate}

### Cloaking and Inducing Inputs {#cloaking-and-inducing-inputs-1
   data-transition="None"}

\includeimg{../slides/diagrams/privacy/cloaking-inducing.png}{80%}{negate}

### Results {#results}

* For 1D !Kung, RMSE improved from $15.0 \pm 2.0 \text{cm}$ to $11.1 \pm 0.8 \text{cm}$

    Use Age and Weight to predict Height

* For 2D !Kung, RMSE improved from $22.8 \pm 1.9 \text{cm}$ to $8.8 \pm 0.6 \text{cm}$

    Note that the uncertainty across cross-validation runs smaller. 2D version benefits from data's 1D manifold.

### Cloaking (no) Inducing Inputs {#cloaking-no-inducing-inputs-1 data-transition="none"}

\includeimg{../slides/diagrams/privacy/housing-no-inducing.png}{80%}{negate}

### Cloaking and Inducing Inputs {#cloaking-and-inducing-inputs-2 data-transition="none"}

\includeimg{../slides/diagrams/privacy/housing-inducing.png}{80%}{negate}
