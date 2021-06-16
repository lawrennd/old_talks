\ifndef{neuripsExperimentRandomCommittee}
\define{neuripsExperimetnRandomCommittee}

\editme

\subsection{A Random Committee @ 25%}

\notes{The first context we can place around the numbers is what would have happened at the 'Random Conference' where we simply accept a quarter of papers at random. In this NIPS the expected numbers of accepts would then have been:}

<table>
  <tr>
  <td colspan="2"></td><td colspan="2">Committee 1</td>
  </tr>
  <tr>
  <td colspan="2"></td><td>Accept</td><td>Reject</td>
  </tr>
  <tr>
    <td rowspan="2">Committee 2</td><td>Accept</td><td>10.4 (1 in 16)</td><td>31.1 (3 in 16)</td>
  </tr>
  <tr>
    <td>Reject</td><td>31.1 (3 in 16) </td><td>93.4 (9 in 16)</td>
  </tr>
  </table>

\newslide{NeurIPS Experiment Results}

\slides{
<table>
  <tr>
  <td colspan="2"></td><td colspan="2">Committee 1</td>
  </tr>
  <tr>
  <td colspan="2"></td><td>Accept</td><td>Reject</td>
  </tr>
  <tr>
    <td rowspan="2">Committee 2</td><td>Accept</td><td>22</td><td>22</td>
  </tr>
  <tr>
    <td>Reject</td><td>21</td><td>101</td>
  </tr>
</table>}


\newslide{A Random Committee @ 25%}

\slides{
<table>
  <tr>
  <td colspan="2"></td><td colspan="2">Committee 1</td>
  </tr>
  <tr>
  <td colspan="2"></td><td>Accept</td><td>Reject</td>
  </tr>
  <tr>
    <td rowspan="2">Committee 2</td><td>Accept</td><td>10</td><td>31</td>
  </tr>
  <tr>
    <td>Reject</td><td>31</td><td>93</td>
  </tr>
</table>}



\notes{And for this set up we would expect *inconsistency* of 3 in 8 (37.5%) *accept precision* of 1 in 4 (25%) and a *reject precision* of 3 in 4 (75%) and a *agreed accept rate* of 1 in 10 (10%). The actual committee made improvements on these numbers, in particular the accept precision was markedly better with 50%: twice as many consistent accept decisions were made than would be expected if the process had been performed at random and only around two thirds as many inconsistent decisions were made as would have been expected if decisions were made at random. However, we should treat all these figures with some skepticism until we've performed some estimate of the uncertainty associated with them.}

\notes{
\subsection{Stats for Random Committee}

* For random committee we expect:
  * *inconsistency* of 3 in 8 (37.5%) 
  * *accept precision* of 1 in 4 (25%) 
  * *reject precision* of 3 in 4 (75%) and a 
  * *agreed accept rate* of 1 in 10 (10%). 

Actual committee's accept precision markedly better with 50% accept precision.

\subsection{Uncertainty: Accept Rate}

\notes{To get a handle on the uncertainty around these numbers we'll start by making use of the (binomial distribution)[http://en.wikipedia.org/wiki/Binomial_distribution]. First, let's explore the fact that for the overall conference the accept rate was around 23%, but for the duplication committees the accept rate was around 25%. If we assume decisions are made according to a binomial distribution, then is the accept rate for the duplicated papers too high?}

\notes{Note that for all our accept probability statistics we used as a denominator the number of papers that were initially sent for review, rather than the number where a final decision was made by the program committee. These numbers are different because some papers are withdrawn before the program committee makes its decision. Most commonly this occurs after authors have seen their preliminary reviews: for NIPS 2014 we provided preliminary reviews that included paper scores. So for the official accept probability we use the 170 as denominator. The accept probabilities were therefore 43 out of 170 papers (25.3%) for Committee 1 and 44 out of 170 (25.8%) for Committee 2. This compares with the overall conference accept rate for papers outside the duplication process of 349 out of 1508 (23.1%).}

\notes{If the true underlying probability of an accept were actually 0.23 independent of the paper, then the probability of generating accepts for any subset of the papers would be given by a binomial distribution. Combining across the two committees for the duplicated papers, we see that 87 papers in total were recommended for accept out of a total of 340 trials. out of 166 trials would be given by a binomial distribution as depicted below.}

\setupcode{import numpy as np
from scipy.stats import binom
from IPython.display import HTML}

\setupplotcode{import matplotlib.pyplot as plt
import cmtutils.plot as plot
import mlai as ma}

\plotcode{rv = binom(340, 0.23)
x = np.arange(60, 120)
fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
ax.bar(x, rv.pmf(x))
display(HTML('<h3>Number of Accepted Papers for p = 0.23</h3>'))
ax.axvline(87,linewidth=4, color='red')
ma.write_figure(filename="uncertainty-accept-rate.svg", directory="\writeDiagramsDir/neurips")}

\figure{\includediagram{\diagramsDir/neurips/uncertainty-accept-rate}{70%}}{Number of accepted papers for $p=0.23$.}{uncertainty-accept-rate}

\notes{From the plot, we can see that whilst the accept rate was slightly higher for duplicated papers it doesn't seem that we can say that it was statistically significant that it was higher, it falls well within the probability mass of the Binomial.}

\notes{Note that Area Chairs knew which papers were duplicates, whereas reviewers did not. Whilst we stipulated that duplicate papers should not be any given special treatment, we cannot discount the possibility that Area Chairs may have given slightly preferential treatment to duplicate papers.}

\subsection{Uncertainty: Accept Precision}

\notes{For the accept precision, if we assume that accept decisions were drawn according to a binomial, then the distribution for consistent accepts is also binomial. Our best estimate of its parameter is 22/166 = 0.13 (13%). If we had a binomial distribution with these parameters, then the distribution of consistent accepts would be as follows.}

* How reliable is the consistent accept score?

\plotcode{rv = binom(166, 0.13)
x = np.arange(10, 30)
fig, ax = plt.subplots(figsize=(10,5))
ax.bar(x, rv.pmf(x))
display(HTML('<h3>Number of Consistent Accepts given p=0.13</h3>'))
ax.axvline(22,linewidth=4, color='red') 
ma.write_figure(filename="uncertainty-accept-precision.svg", directory="\writeDiagramsDir/neurips")}

\figure{\includediagram{\diagramsDir/neurips/uncertainty-accept-rate}{70%}}{Number of consistent accepts given $p=0.13$.}{uncertainty-accept-precision}

\notes{We see immediately that there is a lot of uncertainty around this number, for the scale of the experiment as we have it. This suggests a more complex analysis is required to extract our estimates with uncertainty.}

\subsection{Bayesian Analysis}

\notes{Before we start the analysis, it's important to make some statements about the aims of our modelling here. We will make some simplifying modelling assumptions for the sake of a model that is understandable. In particular, we are looking to get a handle on the uncertainty associated with some of the probabilities associated with the NIPS experiment. [Some preliminary analyses have already been conducted on blogs](http://inverseprobability.com/2015/01/16/blogs-on-the-nips-experiment/). Those analyses don't have access to information like paper scores etc. For that reason we also leave out such information in this preliminary analysis. We will focus only on the summary results from the experiment: how many papers were consistently accepted, consistently rejected or had inconsistent decisions. For the moment we disregard the information we have about paper scores.
}

\notes{In our analysis there are three possible outcomes for each paper: consistent accept, inconsistent decision and consistent reject. So we need to perform the analysis with the [multinomial distribution](http://en.wikipedia.org/wiki/Multinomial_distribution). The multinomial is parameterized by the probabilities of the different outcomes. These are our parameters of interest, we would like to estimate these probabilities alongside their uncertainties. To make a Bayesian analysis we place a prior density over these probabilities, then we update the prior with the observed data, that gives us a posterior density, giving us an uncertainty associated with these probabilities.}

\slides{* Multinomial distribution three outcomes.
* Uniform Dirichlet prior.
  * (doesn't account for implausability of 'active inconsistency')}

\notes{### Prior Density

Choice of prior for the multinomial is typically straightforward, the [Dirichlet density](http://en.wikipedia.org/wiki/Dirichlet_distribution) is [conjugate](http://en.wikipedia.org/wiki/Conjugate_prior) and has the additional advantage that its parameters can be set to ensure it is *uninformative*, i.e. uniform across the domain of the prior. Combination of a multinomial likelihood and a Dirichelt prior is not new, and in this domain if we were to consider the mean the posterior density only, then the approach is known as [Laplace smoothing](http://en.wikipedia.org/wiki/Additive_smoothing). 

For our model we are assuming for our prior that the probabilities are drawn from a Dirichlet as follows,
$$
p \sim \text{Dir}(\alpha_1, \alpha_2, \alpha_3),
$$
with $\alpha_1=\alpha_2=\alpha_3=1$. The Dirichlet density is conjugate to the [multinomial distribution](http://en.wikipedia.org/wiki/Multinomial_distribution), and we associate three different outcomes with the multinomial. For each of the 166 papers we expect to have a consistent accept (outcome 1), an inconsistent decision (outcome 2) or a consistent reject (outcome 3). If the counts four outcome 1, 2 and 3 are represented by $k_1$, $k_2$ and $k_3$ and the associated probabilities are given by $p_1$, $p_2$ and $p_3$ then our model is, 
\begin{align*}
\mathbf{p}|\boldsymbol{\alpha} \sim \text{Dir}(\boldsymbol{\alpha}) \\
\mathbf{k}|\mathbf{p} \sim \text{mult}(\mathbf{p}).
\end{align*}
Due to the conjugacy the posterior is tractable and easily computed as a Dirichlet (see e.g. [Gelman et al](http://www.stat.columbia.edu/~gelman/book/)), where the parameters of the Dirichlet are given by the original vector from the Dirichlet prior plus the counts associated with each outcome. 
$$
\mathbf{p}|\mathbf{k}, \boldsymbol{\alpha} \sim \text{Dir}(\boldsymbol{\alpha} + \mathbf{k})
$$
The mean probability for each outcome is then given by,
$$
\bar{p}_i = \frac{\alpha_i+k_i}{\sum_{j=1}^3(\alpha_j + k_j)}.
$$
and the variance is
$$
\mathrm{Var}[p_i] = \frac{(\alpha_i+k_i) (\alpha_0-\alpha_i + n + k_i)}{(\alpha_0+n)^2 (\alpha_0+n+1)},
$$
where $n$ is the number of trials (166 in our case) and $\alpha_0 = \sum_{i=1}^3\alpha_i$. This allows us to compute the expected value of the probabilities and their variances under the posterior as follows.}

\code{def posterior_mean_var(k, alpha):
    """Compute the mean and variance of the Dirichlet posterior."""
    alpha_0 = alpha.sum()
    n = k.sum()
    m = (k + alpha)
    m /= m.sum()
    v = (alpha+k)*(alpha_0 - alpha + n + k)/((alpha_0+n)**2*(alpha_0+n+1))
    return m, v

k = np.asarray([22, 43, 101])
alpha = np.ones((3,))
m, v = posterior_mean_var(k, alpha)
outcome = ['consistent accept', 'inconsistent decision', 'consistent reject']
for i in range(3):
    display(HTML("<h4>Probability of " + outcome[i] +' ' + str(m[i]) +  "+/-" + str(2*np.sqrt(v[i])) + "</h4>"))}

\notes{So we have a probability of consistent accept as $0.136 \pm 0.06$, the probability of inconsistent decision as $0.260 \pm 0.09$ and probability of consistent reject as $0.60 \pm 0.15$. Recall that if we'd selected papers at random (with accept rate of 1 in 4) then these values would have been 1 in 16 (0.0625), 3 in 8 (0.375) and 9 in 16 (0.5625). 

The other values we are interested in are the accept precision, reject precision and the agreed accept rate. Computing the probability density for these statistics is complex, because it involves [Ratio Distributions](http://en.wikipedia.org/wiki/Ratio_distribution). However, we can use Monte Carlo to estimate the expected accept precision, reject precision and agreed accept rate as well as their variances. We can use these results to give us error bars and histograms of these statistics.}

\code{def sample_precisions(k, alpha, num_samps):
    """Helper function to sample from the posterior distibution of accept, 
    reject and inconsistent probabilities and compute other statistics of interest 
    from the samples."""

    k = np.random.dirichlet(k+alpha, size=num_samps)
    # Factors of 2 appear because inconsistent decisions 
    # are being accounted for across both committees.
    ap = 2*k[:, 0]/(2*k[:, 0]+k[:, 1])
    rp = 2*k[:, 2]/(k[:, 1]+2*k[:, 2])
    aa = k[:, 0]/(k[:, 0]+k[:, 2])
    return ap, rp, aa

ap, rp, aa = sample_precisions(k, alpha, 10000)
print(ap.mean(), '+/-', 2*np.sqrt(ap.var()))
print(rp.mean(), '+/-', 2*np.sqrt(rp.var()))
print(aa.mean(), '+/-', 2*np.sqrt(aa.var()))}

\notes{Giving an accept precision of $0.51 \pm 0.13$, a reject precision of $0.82 \pm 0.05$ and an agreed accept rate of $0.18 \pm 0.07$. Note that the 'random conference' values of 1 in 4 for accept precision and 3 in 4 for reject decisions are outside the two standard deviation error bars. If it is preferred medians and percentiles could also be computed from the samples above, but as we will see when we histogram the results the densities look broadly symmetric, so this is unlikely to have much effect.

\subsubsection{Histogram of Monte Carlo Results}

Just to ensure that the error bars are reflective of the underlying densities we histogram the Monte Carlo results for accept precision, reject precision and agreed accept below. Shown on each histogram is a line representing the result we would get for the 'random committee'.}

\plotcode{fig, ax = plt.subplots(1, 3, figsize=(15, 5))
_ = ax[0].hist(ap, 20)
_ = ax[0].set_title('Accept Precision')
ax[0].axvline(0.25, linewidth=4, color="r")
_ = ax[1].hist(rp, 20)
_ = ax[1].set_title('Reject Precision')
ax[1].axvline(0.75, linewidth=4, color="r")
_ = ax[2].hist(aa, 20)
_ = ax[2].set_title('Agreed Accept Rate')
_ = ax[2].axvline(0.10, linewidth=4, color="r")
ma.write_figure(filename="random-committee-outcomes-vs-true.svg", directory="\writeDiagramsDir/neurips")}

\figure{\includediagram{\diagramsDir/neurips/random-committee-outcomes-vs-true}{90%}}{Different statistics for the random committee oucomes versus the observed committee outcomes.}{random-committee-outcomes}

\notes{\subsubsection{Model Choice and Prior Values}

In the analysis above we've minimized the modeling choices: we made use of a Bayesian analysis to capture the uncertainty in counts that can be arising from statistical sampling error. To this end we chose an uninformative prior over these probabilities. However, one might argue that the prior should reflect something more about the underlying experimental structure: for example we *know* that if the committees made their decisions independently it is unlikely that we'd obtain an inconsistency figure much greater than 37.5% because that would require committees to explicitly collude to make inconsistent decisions: the random conference is the worst case. Due to the accept rate, we also expect a larger number of reject decisions than reject. This also isn't captured in our prior. Such questions actually move us into the realms of modeling the process, rather then performing a sensitivity analysis. However, if we wish to model the decision process as a whole we have a lot more information available, and we should make use of it. The analysis above is intended to exploit our randomized experiment to explore how inconsistent we expect two committees to be. It focusses on that single question, it doesn't attempt to give answers on what the reasons for that inconsistency are and how it may be reduced. The additional maths was needed only to give a sense of the uncertainty in the figures. That uncertainty arises due to the limited number of papers in the experiment.}

}
\endif
