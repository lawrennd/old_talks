\ifndef{dataAndIntellectualDebt}
\define{dataAndIntellectualDebt}

\editme

\subsection{Adding Data}

\notes{This does lead to technical debt, but more perniciously it leads to
intellectual debt. Even if your system is functioning, you struggle to
explain how and why it is working.

This situation is not good enough, but it becomes far worse when data is
involved.

With the introduction of machine learning we see three principle effects
in these complex systems.

1.  Machine learning models are being deployed as regular software; this
    means their very existence in the complex infrastructure is not
    being declared. Maybe Lancelot knows, but he's likely too busy dealing
    with some other issue.

    This is a challenge because the machine learning model has a
    sell-by date. It is trained and validated on data from a
    particular time period which reflects a particular snapshot of the
    population. In practice the statistical population will evolve,
    and the quality of the model with decay over time. Unless the team
    placed in particular infrastructure to monitor this performance
    loss (which they often don't, because they are under pressure to
    deploy). The time frame over which a model can become stale can be
    extremely short, because often the very deployment of a model (if
    done at scale) effects the dynamics of data production rendering
    the training data non-representative.[^1]

2.  In the rush to adopt "AI" and make use of machine learning
    technology, standard software engineering sanity checks are often
    suspended because people are told that 'machine learning is
    different'. It is indeed different; it is much worse than standard
    software in its potential failure modes and extra safeguards need to
    be put in place.

3.  The individual models are sometimes difficult to interpret and there
    is potential for bias to enter in the modelling or from the data.
    Performance of these models is normally measured empirically and is
    therefore driven by the 'average case'. Exceptional circumstances
    are often handled extremely badly.

[^1]: I'm excited by the [EPSRC Funded Closed Loop Data
    Science](https://www.gla.ac.uk/schools/computing/research/researchsections/ida-section/closedloop/)
    project at the University of Glasgow run by Rod Murray-Smith for
    addressing this.


We are beginning to broach the subject of intellectual debt around the
interpretability of individual models. And indeed, there is a field
known as Fairness, Accountability and Transparency Machine learning that
is looking to address these issues for single models. This is where,
unfortunately, the death of the programmer enters.}

\endif
