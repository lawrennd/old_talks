\ifndef{uqSamplingHistoryDoe}
\define{uqSamplingHistoryDoe}

\editme

\subsection{Uncertainty Quantification and Design of Experiments}
\slides{* History of interest, see e.g. @McKay-selecting79
* The review:
    * Random Sampling
    * Stratified Sampling
    * Latin Hypercube Sampling
* As approaches for Monte Carlo estimates
}
\notes{We're introducing you to the optimization and analysis of real-world models through emulation, this domain is part of a broader field known as surrogate modelling.}

\notes{Although we're approaching this from the machine learning perspective, with a computer-scientist's approach, you won't be surprised to find out that this field is not new and there are a diverse range of research communities interested in this domain.}

\notes{We've been focussing on *active* experimental design. In particular, the case where we are sequentially selecting points to run our simulation based on previous results.}

\notes{Here, we pause for a moment and cover approaches to *passive* experimental design. Almost all the emulation examples we've looked at so far need some initial points to 'seed' the emulator. Selecting these is also a task of experimental design, but one we perform without running our simulator.}

\notes{This type of challenge, of where to run the simulation to get the answer you require is an old challenge. One classic paper, @McKay-selecting79, reviews three different methods for designing these inputs. They are *random sampling*, *stratified sampling*, and *Latin hypercube sampling*.}


\newslide{Random Sampling}

\notes{Random sampling is the default approach, this is where across the input domain of interest, we just choose to select samples randomly (perhaps uniformly, or if we believe there's an underlying distribution 


>  Let the input values $\inputVector_1, \dots, \inputVector_\numData$
> be a random sample from $f(\inputVector)$. This method of sampling
> is perhaps the most obvious, and an entire body of statistical
> literature may be used in making inferences regarding the
> distribution of $Y(t)$.


\newslide{Stratified Sampling}

\notes{In statistical surveillance stratified sampling is an approach from statistics where a population is divided into sub-populations before sampling. For example, imagine that we are interested surveillance data for Covid-19 tracking. If we can only afford to track 100 people, we could sample them randomly from across the population. But we might worry that (by chance) we don't get many people from a particular age group. So instead, we could divide the population into sub-groups and sample a fixed number from each group. This ensures we get coverage across all ages, although downstream we might have to do some weighting of the samples when considering the population effect.}

\notes{The same ideas can be deployed in emulation, your input domain can be divided into domains of particular intererest. For example if testing the performance of a component from an F1 car, you might be interested in the performance on the straight, the performance in "fast corners" and the performance in "slow corners". Because slow corners have a very large effect on the final performance, you might take more samples from slow corners relative to the frequency that such corners appear in the actual races.}

> Using stratified sampling, all
> areas of the sample space of $\inputVector$ are represented by
> input values. Let the sample space $S$ of $\inputVector$ be partitioned into $I$ disjoint strata $S_t$. Let $\pi = P(\inputVector \in S_i)$
> represent the size of $S_i$. Obtain a random sample $\inputVector_{ij}$, $j
> = 1, \dots, n$ from $S_i$. Then of course the $n_i$ sum to $\numData$.
> If $I = 1$, we have random sampling over the entire
> sample space.

\newslide{Latin Hypercube Sampling}

\notes{Latin hypercube sampling is a form of stratified sampling. For a Latin square if $M$ samples are requred, then the strata are determined by dividing the area of the inputs into discrete $M$ rows and $M$ columns. Then the samples are taken so that each row and column only contains one total sample. The Latin hypercube is the generalisation of this idea to more than two dimensions.}

> The same reasoning that led to stratified sampling, ensuring that
> all portions of $S$ were sampled, could lead further. If we wish
> to ensure also that each of the input variables $\inputVector_k$ has
> all portions of its distribution represented by input values, we can
> divide the range of each $\inputVector_k$ into $\numData$ strata of
> equal marginal probability $1/\numData$, and sample once from each
> stratum. Let this sample be $\inputVector_{kj}$, $j = 1, \dots,
> \numData$. These form the $\inputVector_k$ component, $k = 1, \dots
> , K$, in $\inputVector_i$, $i = 1, \dots, \numData$. The components
> of the various $\inputVector_k$'s are matched at random. This method
> of selecting input values is an extension of quota sampling
> (Steinberg 1963), and can be viewed as a $K$-dimensional extension of
> Latin square sampling (Raj 1968).

\notes{The paper's rather dated reference to "Output from a Computer Code" does carry forward through this literature, which has continued to be a focus of interest for statisticians. [Tony O'Hagan](http://www.tonyohagan.co.uk/academic/), who was a colleague in Sheffield but is also one of the pioneers of Gaussian process models was developing these methods when I first arrived there [@Kennedy-bayesian01], and continued with a large EPSRC funded project for managing uncertainty in computational models, <http://www.mucm.ac.uk/>. You can see a list of [their technical reports here](http://www.mucm.ac.uk/Pages/Dissemination/TechnicalReports.html).}

\notes{Another important group based in France is the "MASCOT-NUM Research Group", <https://www.gdr-mascotnum.fr/>. These researchers bring together statisticians, applied mathematicians and engineers in solving these problems.}

\endif
