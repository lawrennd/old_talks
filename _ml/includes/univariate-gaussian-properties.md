\subsection{Two Important Gaussian Properties}

\notes{The Gaussian density has many important properties, but for the moment we'll review two of them.}

\subsection{Sum of Gaussians}

\notes{If we assume that a variable, $\dataScalar_i$, is sampled from a Gaussian density,}
\slides{. . .

\alignleft{Sum of Gaussian variables is also Gaussian.}}

$$\dataScalar_i \sim \gaussianSamp{\meanScalar_i}{\sigma_i^2}$$

\notes{Then we can show that the sum of a set of variables, each drawn independently from such a density is also distributed as Gaussian. The mean of the resulting density is the sum of the means, and the variance is the sum of the variances,}

\slides{. . .

\alignleft{And the sum is distributed as}}

$$\sum_{i=1}^{\numData} \dataScalar_i \sim \gaussianSamp{\sum_{i=1}^\numData \meanScalar_i}{\sum_{i=1}^\numData \sigma_i^2}$$

\notes{Since we are very familiar with the Gaussian density and its properties, it is not immediately apparent how unusual this is. Most random variables, when you add them together, change the family of density they are drawn from. For example, the Gaussian is exceptional in this regard. Indeed, other random variables, if they are independently drawn and summed together tend to a Gaussian density. That is the [*central limit theorem*](https://en.wikipedia.org/wiki/Central_limit_theorem) which is a major justification for the use of a Gaussian density.}
\slides{. . .
	
\smalltext{(*Aside*: As sum increases, sum of non-Gaussian, finite
variance variables is also Gaussian because of [central limit theorem](https://en.wikipedia.org/wiki/Central_limit_theorem).)}}


\subsection{Scaling a Gaussian}

\notes{Less unusual is the *scaling* property of a Gaussian density. If a variable, $\dataScalar$, is sampled from a Gaussian density,}
\slides{. . .

\alignleft{Scaling a Gaussian leads to a Gaussian.}

. . .
}
$$\dataScalar \sim \gaussianSamp{\meanScalar}{\sigma^2}$$
\notes{and we choose to scale that variable by a *deterministic* value, $\mappingScalar$, then the *scaled variable* is distributed as}
\slides{
. . .

\alignleft{And the scaled variable is distributed as}
}
$$\mappingScalar \dataScalar \sim \gaussianSamp{\mappingScalar\meanScalar}{\mappingScalar^2 \sigma^2}.$$
\notes{Unlike the summing properties, where adding two or more random variables independently sampled from a family of densitites typically brings the summed variable *outside* that family, scaling many densities leaves the distribution of that variable in the same *family*  of densities. Indeed, many densities include a *scale* parameter (e.g. the [Gamma density](https://en.wikipedia.org/wiki/Gamma_distribution)) which is purely for this purpose. In the Gaussian the standard deviation, $\dataStd$, is the scale parameter. To see why this makes sense, let's consider,
$$z \sim \gaussianSamp{0}{1},$$
then if we scale by $\dataStd$ so we have, $\dataScalar=\dataStd z$, we can write,
$$\dataScalar =\dataStd z \sim \gaussianSamp{0}{\dataStd^2}$$
} 
