\ifndef{typesOfUncertainty}
\define{typesOfUncertainty}
\editme

\notes{
\subsection{A Philosophical Dispute: Probabilistic Treatment of Parameters?}

From a philosophical perspective placing a probability distribution over the *parameters* is known as the *Bayesian* approach. This is because Thomas Bayes, in a [1763 essay](http://en.wikipedia.org/wiki/An_Essay_towards_solving_a_Problem_in_the_Doctrine_of_Chances) published at the Royal Society introduced the [Bernoulli distribution](http://en.wikipedia.org/wiki/Bernoulli_distribution) with a probabilistic interpretation for the *parameters*. Later statisticians such as [Ronald Fisher](http://en.wikipedia.org/wiki/Ronald_Fisher) objected to the use of probability distributions for *parameters*, and so in an effort to discredit the approach the referred to it as Bayesian. However, the earliest practioners of modelling, such as Laplace applied the approach as the most natural thing to do for dealing with unknowns (whether they were parameters or variables). Unfortunately, this dispute led to a split in the modelling community that still has echoes today. It is known as the Bayesian vs Frequentist controversy. From my own perspective, I think that it is a false dichotomy, and that the two approaches are actually complementary. My own focus research focus is on *modelling* and in that context, the use of probability is vital. For frequenstist statisticians, such as Fisher, the emphasis was on the value of the evidence in the data for a particular hypothesis. This is known as hypothesis testing. The two approaches can be unified because one of the most important approaches to hypothesis testing is to [compute the ratio of the likelihoods](http://en.wikipedia.org/wiki/Likelihood-ratio_test), and the result of applying a probability distribution to the parameters is merely to arrive at a different form of the likelihood.}

\subsection{The Bayesian Controversy: Philosophical Underpinnings}

A segment from the lecture in 2012 on philsophical underpinnings.

\figure{\includeyoutube{AvlnFnvFw_0}{600}{450}{1215}{1900}}{The philosophical underpinnings of uncertainty, as discussed in 2012 MLAI lecture.}{philosophical-underpinnings-uncertainty}

\newslide{Noise Models}

\slides{
* We aren’t modeling entire system.
* Noise model gives mismatch between model and data.
* Gaussian model justified by appeal to central limit theorem.
* Other models also possible (Student-$t$ for heavy tails).
* Maximum likelihood with Gaussian noise leads to *least squares*.
}

\newslide{Different Types of Uncertainty}

\slides{
* The first type of uncertainty we are assuming is *aleatoric* uncertainty.
* The second type of uncertainty we are assuming is *epistemic* uncertainty.
}

\newslide{Aleatoric Uncertainty}

\slides{
* This is uncertainty we couldn’t know even if we wanted to. e.g. the result of a football match before it’s played.
* Where a sheet of paper might land on the floor.
}

\newslide{Epistemic Uncertainty}

\slides{
* This is uncertainty we could in principal know the answer too. We just haven’t observed enough yet, e.g. the result of a football match *after* it’s played.
* What colour socks your lecturer is wearing.
}
\endif
