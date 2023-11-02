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

\notes{This type of challenge, of where to run the simulation to get the answer you require is an old challenge. One classic paper, @McKay-selecting79, reviews three different methods for designing these inputs. They are *random sampling*, *stratified sampling* and *Latin hypercube sampling*.}


\newslide{Random Sampling}


>  Let the input values $\inputVector_1, \dots, \inputVector_\numData$
> be a random sample from $f(\inputVector)$. This method of sampling
> is perhaps the most obvious, and an entire body of statistical
> literature may be used in making inferences regarding the
> distribution of $Y(t)$.


\newslide{Stratified Sampling}

> Using stratified sampling, all
> areas of the sample space of $\inputVector$ are represented by
> input values. Let the sample space $S$ of $\inputVector$ be partitioned into $I$ disjoint strata $S_t$. Let $\pi = P(\inputVector \in S_i)$
> represent the size of $S_i$. Obtain a random sample $\inputVector_{ij}$, $j
> = 1, \dots, n$ from $S_i$. Then of course the $n_i$ sum to $\numData$.
> If $I = 1$, we have random sampling over the entire
> sample space.

\newslide{Latin Hypercube Sampling}

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

\notes{The paper's rather dated reference to "Output from a Computer Code" does carry forward through this literature, which has continued to be a focus of interest for statisticians. [Tony O'Hagan](http://www.tonyohagan.co.uk/academic/), who was a colleague in Sheffield but is also one of the pioneers of Gaussian process models was developing these methods when I first arrived there [@Kennedy-bayesian01], and continued with a large EPSRC funded project for managing uncertainty in computational models, <http://www.mucm.ac.uk/>. You can see a list of [their technical reports here](http://www.mucm.ac.uk/Pages/Dissemination/TechnicalReports.html).

Another important group based in France is the "MASCOT-NUM Research Group", <https://www.gdr-mascotnum.fr/>. These researchers bring together statisticians, applied mathematicians and engineers in solving these problems.}

\endif
