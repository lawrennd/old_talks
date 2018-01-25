
### The Maths {.slide: data-transition="none"}

$$ \dataMatrix = \begin{bmatrix}
\dataScalar_{1, 1} & \dataScalar_{1, 2} &\dots & \dataScalar_{1,p}\\
\dataScalar_{2, 1} & \dataScalar_{2, 2} &\dots & \dataScalar_{2,p}\\
\vdots & \vdots &\dots & \vdots\\
\dataScalar_{n, 1} & \dataScalar_{n, 2} &\dots & \dataScalar_{n,p}
\end{bmatrix} \in \Re^{n\times p}
$$

### The Maths {.slide: data-transition="none"}

$$ \dataMatrix = \begin{bmatrix}
\dataVector^\top_{1, :} \\
\dataVector^\top_{2, :} \\
\vdots \\
\dataVector^\top_{n, :}
\end{bmatrix} \in \Re^{n\times p}
$$

### The Maths {.slide: data-transition="none"}

$$ \dataMatrix = \begin{bmatrix}
\dataVector_{:, 1} &
\dataVector_{:, 2} &
\dots &
\dataVector_{:, p}
\end{bmatrix} \in \Re^{n\times p}
$$


<!-- This is the nature of modern streaming data, what has been called big data, although in the UK it looks like that term will gain a more diffuse meaning now that the government has associated a putative 189 billion pounds of funding to it. But the characteristic of massive missing data is particularly obvious when we look at clinical domains. EMIS, a Yorkshire based provider of software to General Practitioners, has 39 million patient records. When we consider clinical measurements, we need to build models that not only take into account all current clinical tests, but all tests that will be invented in the future. This leads to the idea of massive missing data. The classical statistical table of data is merely the special case where someone has filled in a block of information.  -->

<!-- To deal with massively missing data we need to think about the *Kolmogorov consistency* of a process. Let me introduce Kolmogorov consistency by way of an example heard from Tony O'Hagan, but one that he credits originally to Michael Goldstein. Imagine you are on jury duty. You are asked to adjudicate on the guilt or innocence of Lord Safebury, and you are going to base your judgement on a model that is weighing all the evidence. You are just about to pronounce your decision when a maid comes running in and shouts "He didn't do it! He didn't do it!". The maid wasn't on the witness list and isn't accounted for in your model. How does this effect your inference? The pragmatists answer might be: not at all, because the maid wasn't in the model. But in the interests of justice we might want to include this information in our inference process. If, as a result of the maid's entry, we now think it is less likely that Lord Safebury committed the crime, then necessarily every time that the (unannounced) maid doesn't enter the room we have to assume that it is more likely that Safebury commited the crime (to ensure that the conditional probability of guilt given the maid's evidence normalizes. But we didn't know about the maid, so how can we account for this? Further, how can we account for all possible other surprise evidence, from the announced butlers, gardners, chauffeurs and footmen? Kolmogorov consistency (@Kolmogorov:grundbegriffe33) says that the net effect of marginalizing for all these potential bits of new information is null. It is a particular property of the model. Making it (only slightly) more formal, we can consider Kolmogorov consistency as a marginalization property of the model. We take the $n$ dimensional vector, $\dataVector$, to be an (indexed) vector of all our instantiated observations of the world that we have *at the current time*. Then we take the $n^*$ dimensional vector, $\dataVector^*$ to be the observations of the world that we are *yet to see*. --> 

### The Maths {.slide: data-transition="none"}

$$p(\dataMatrix|\paramVector) = \prod_{i=1}^n p(\dataVector_{i, :}|\paramVector)$$


### The Maths {.slide: data-transition="none"}

$$p(\dataMatrix|\paramVector) = \prod_{i=1}^n p(\dataVector_{i, :}|\paramVector)$$

$$\log p(\dataMatrix|\paramVector) = \sum_{i=1}^n \log p(\dataVector_{i, :}|\paramVector)$$

### Consistency

* Typically $\paramVector \in \Re^{\mathcal{O}(p)}$

* Consistency reliant on large sample approximation of KL divergence

$$ \text{KL}(P(\dataMatrix)|| p(\dataMatrix|\paramVector))$$

* Minimization is equivalent to maximization of likelihood.

* A foundation stone of classical statistics.

### Large $p$

* For large $p$ the parameters are badly determined.

* Large $p$ small $n$ problem.

* Easily dealt with through definition.

### The Maths {.slide: data-transition="none"}

$$p(\dataMatrix|\paramVector) = \prod_{j=1}^p p(\dataVector_{:, j}|\paramVector)$$

$$\log p(\dataMatrix|\paramVector) = \sum_{j=1}^p \log p(\dataVector_{:, j}|\paramVector)$$

### Breadth vs Depth

* Modern Measurement deals with *depth* (many subjects)
    ... or *breadth* lots of detail about subject.
	
* But what about 
    * $p\approx n$?
    * Stratification of populations: batch effects etc.

* Multi-task learning (Natasha Jaques)

### Does $p$ Even Exist?

* Massively missing data.

* Classical bias towards tables.

* Streaming data.

$$ \dataMatrix = \begin{bmatrix}
\dataScalar_{1, 1} & \dataScalar_{1, 2} &\dots & \dataScalar_{1,p}\\
\dataScalar_{2, 1} & \dataScalar_{2, 2} &\dots & \dataScalar_{2,p}\\
\vdots & \vdots &\dots & \vdots\\
\dataScalar_{n, 1} & \dataScalar_{n, 2} &\dots & \dataScalar_{n,p}
\end{bmatrix} \in \Re^{n\times p}
$$

### General index on $\dataScalar$

$$\dataScalar_\inputVector$$

where $\inputVector$ might include time, spatial location ...

Streaming data. Joint model of past, $\dataVector$ and future $\dataVector_*$

$$p(\dataVector, \dataVector_*)$$

Prediction through: 

$$p(\dataVector_*|\dataVector)$$


### Kolmogorov Consistency --- Exchangeability 

* From the sum rule of probability we have
\begin{align*}
p(\dataVector|n^*) = \int p(\dataVector, \dataVector^*) \text{d}\dataVector^*
\end{align*}
$n^*$ is length of $\dataVector^*$.

* Consistent if $p(\dataVector|n^*) = p(\dataVector)$

* Prediction then given by product rule
\begin{align*}
p(\dataVector^*|\dataVector) = \frac{p(\dataVector, \dataVector^*)}{p(\dataVector)}
\end{align*}

### $p(\dataVector^*|\dataVector)$

<!-- where the dependence of the marginal distribution for $\dataVector$ aries from the fact that we are forming an $n^*$ dimensional integral over $\dataVector^*$. If our distribution is Kolmogorov consistent, then we know that the distribution over $\dataVector$ is *independent* of the value of $n^*$. So in other words $p(\dataVector|n*)=p(\dataVector)$. So Kolmogorov consistency says that the form of $p(\dataVector)$ remains the same *regardless* of the number of observations of the world that are yet to come.  -->

### Parametric Models

* Kolmogorov consistency trivial in parametric model.
\begin{align*}
p(\dataVector, \dataVector^*) = \int \prod_{i=1}^n p(\dataScalar_{i} | \paramVector)\prod_{i=1}^{n^*}p(y^*_i|\paramVector) p(\paramVector) \text{d}\paramVector
\end{align*}

* Marginalizing
\begin{align*}
p(\dataVector) = \int \prod_{i=1}^n p(\dataScalar_{i} | \paramVector)\prod_{i=1}^{n^*} \int p(y^*_i|\paramVector) \text{d}y^*_i p(\paramVector) \text{d}\paramVector
\end{align*}


### Parametric Bottleneck

* Bayesian methods suggest a prior over $\paramVector$ and use posterior, $p(\paramVector|\dataVector)$ for making predictions.
\begin{align*}
p(\dataVector^*|\dataVector) = \int \prod_i p(\dataScalar_i^* | \paramVector) p(\paramVector|\dataVector)\text{d}\paramVector 
\end{align*}

* Design time problem: *parametric bottleneck*. 
$$p(\paramVector | \dataVector)$$

* Streaming data could turn out to be more complex than we imagine.

### Finite Storage

* Despite our large interconnected brains, we only have finite storage. 

* Similar for digital computers. So we need to assume that we can only store a finite number of things about the data $\dataVector$. 

* This pushes us back towards *parametric* models. 

