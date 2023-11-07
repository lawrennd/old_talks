\subsection{Selecting Number and Location of Basis}
\slides{
* Need to choose
  1. location of centers
  2. number of basis functions
  Restrict analysis to 1-D input, $\inputScalar$.
* Consider uniform spacing over a region:
}\notes{In practice for a basis function model we need to choose both
1. the location of the basis functions
2. the number of basis functions

One very clever of finessing this problem is to choose to have *infinite* basis functions and place them *everywhere*. To show how this is possible, we will consider a one dimensional system, $\inputScalar$, which should give the intuition of how to do this. However, these ideas also extend to multidimensional systems as shown in, for example, @Williams:infinite96 and @Neal:thesis94. 

We consider a one dimensional set up with exponentiated quadratic basis functions, 
$$
\basisFunction_k(\inputScalar_i) = \exp\left(\frac{\ltwoNorm{\inputScalar_i - \locationScalar_k}^2}{2\rbfWidth^2}\right)
$$}
\newslide{Uniform Basis Functions}
\slides{
* Set each center location to}\notes{To place these basis functions, we first define the basis function centers in terms of a starting point on the left of our input, $a$, and a finishing point, $b$. The gap between basis is given by $\Delta\locationScalar$. The location of each basis is then given by}
  $$\locationScalar_k = a+\Delta\locationScalar\cdot (k-1).$$
\slides{
* Specify the basis functions in terms of their indices,}\notes{The covariance function can then be given as
$$
\kernelScalar\left(\inputScalar_i,\inputScalar_j\right) = \sum_{k=1}^\numBasisFunc \basisFunction_k(\inputScalar_i)\basisFunction_k(\inputScalar_j)
$$}
  $$\begin{aligned}
    \kernelScalar\left(\inputScalar_i,\inputScalar_j\right) = &\alpha^\prime\Delta\locationScalar \sum_{k=1}^{\numBasisFunc} \exp\Bigg(
      -\frac{\inputScalar_i^2 + \inputScalar_j^2}{2\rbfWidth^2}\\ 
   & - \frac{2\left(a+\Delta\locationScalar\cdot (k-1)\right)
       \left(\inputScalar_i+\inputScalar_j\right) + 2\left(a+\Delta\locationScalar \cdot (k-1)\right)^2}{2\rbfWidth^2} \Bigg)
  \end{aligned}$$
\slides{
where we’ve scaled variance of process by $\Delta\locationScalar$.
}\notes{where we've also scaled the variance of the process by $\Delta\locationScalar$.}

\newslide{Infinite Basis Functions}
\slides{
* Take}\notes{A consequence of our definition is that the first and last basis function locations are given by}
  $$
  \locationScalar_1=a \ \text{and}\  \locationScalar_\numBasisFunc=b \ \text{so}\ b= a+ \Delta\locationScalar\cdot(\numBasisFunc-1)
  $$
\slides{
* This implies}\notes{This implies that the distance between $b$ and $a$ is given by}
  $$
  b-a = \Delta\locationScalar (\numBasisFunc -1)
  $$ 
  \slides{and therefore}\notes{and since the basis functions are separated by $\Delta\locationScalar$ the number of basis functions is given by}
  $$
  \numBasisFunc = \frac{b-a}{\Delta \locationScalar} + 1
  $$
\slides{
* Take limit as }\notes{The next step is to take the limit as} $\Delta\locationScalar\rightarrow 0$ so $\numBasisFunc \rightarrow \infty$ where we have used $a + k\cdot\Delta\locationScalar\rightarrow \locationScalar$.


\newslide{Result}
\slides{
* Performing the integration leads to}\notes{Performing the integration gives}
  $$\begin{aligned}
    \kernelScalar(\inputScalar_i,&\inputScalar_j) = \alpha^\prime \sqrt{\pi\rbfWidth^2}
    \exp\left( -\frac{\left(\inputScalar_i-\inputScalar_j\right)^2}{4\rbfWidth^2}\right)\\ &\times
    \frac{1}{2}\left[\text{erf}\left(\frac{\left(b - \frac{1}{2}\left(\inputScalar_i +
    \inputScalar_j\right)\right)}{\rbfWidth} \right)-
    \text{erf}\left(\frac{\left(a - \frac{1}{2}\left(\inputScalar_i +
       \inputScalar_j\right)\right)}{\rbfWidth} \right)\right],
    \end{aligned}$$\slides{
* Now take limit as}\notes{Now we take the limit as} $a\rightarrow -\infty$ and $b\rightarrow \infty$
  $$\kernelScalar\left(\inputScalar_i,\inputScalar_j\right) = \alpha\exp\left(
    -\frac{\left(\inputScalar_i-\inputScalar_j\right)^2}{4\rbfWidth^2}\right).$$
  where $\alpha=\alpha^\prime \sqrt{\pi\rbfWidth^2}$.


\newslide{Infinite Feature Space}
\slides{
* An RBF model with infinite basis functions is a Gaussian process.
* The covariance function is given by the  covariance function.}\notes{In conclusion, an RBF model with infinite basis functions is a Gaussian process with the exponentiated quadratic covariance function}
  $$\kernelScalar\left(\inputScalar_i,\inputScalar_j\right) = \alpha \exp\left(
          -\frac{\left(\inputScalar_i-\inputScalar_j\right)^2}{4\rbfWidth^2}\right).$$

\newslide{Infinite Feature Space}
\slides{
* An RBF model with infinite basis functions is a Gaussian process.
* The covariance function is the exponentiated quadratic (squared exponential).
* **Note:** The functional form for the covariance function and basis functions are similar.
  * this is a special case,
  * in general they are very different
}
\notes{Note that while the functional form of the basis function and the covariance function are similar, in general if we repeated this analysis for other basis functions the covariance function will have a very different form. For example the error function, $\text{erf}(\cdot)$, results in an $\asin(\cdot)$ form. See @Williams:infinite96 for more details.}
