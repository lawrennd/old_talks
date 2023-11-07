\ifndef{autoAiOverview}
\define{autoAiOverview}

\editme

\subsection{Auto AI}

\slides{* Auto ML is great but not sufficient
* Interacting components in an ML system
* Identify problems, and automatically deploy solutions
}

\notes{Supervised machine learning models are data-driven statistical functional
estimators. Each ML model is trained to perform a task. Machine learning
systems are created when these models are integrated as interacting
components in a more complex system that carries out a larger scale
task, e.g. an autonomous drone delivery system.

Artificial Intelligence can also be seen as *algorithmic
decision-making*. ML systems are *data driven* algorithmic
decision-makers. Designing decision-making engines requires us to
firstly decompose the system into its component parts. The
decompositions are driven by (1) system performance requirements (2)
the suite of ML algorithms at our disposal (3) the data
availability. Performance requirements could be computational speed,
accuracy, interpretability, and 'fairness'. The current generation of ML
Systems is often based around *supervised learning* and human
annotated data. But in the future, we may expect more use of
*reinforcement learning* and automated knowledge discovery using
*unsupervised learning*.

The classical systems approach assumes decomposability of
components. In ML, upstream components (e.g. a pedestrian detector in
an autonomous vehicle) make decisions that require revisiting once a
fuller picture is realized at a downstream stage (e.g. vehicle path
planning). The relative weaknesses and strengths of the different
component parts need to be assessed when resolving conflicts.

In long-term planning, e.g. logistics and supply chain, a plan
may be computed multiple times under different constraints as data
evolves. In logistics, an initial plan for delivery may be computed
when an item is viewed on a webpage. Webpage waiting-time constraints
dominate the solution we choose. However, when an order is placed the
time constraint may be relaxed and an accuracy constraint or a cost
constraint may now dominate.

Such sub-systems will make inconsistent decisions, but we
should monitor and control the extent of the inconsistency.

One solution to aid with both the lack of decomposability of the
components and the inconsistency between components is *end-to-end*
learning of the system. End-to-end learning is when we use ML
techniques to fit parameters across the entire decision pipeline. We
exploit gradient descent and automated differentiation software to
achieve this. However, components in the system may themselves be
running a *simulation* (e.g. a transport delivery-time simulation) or
*optimization* (e.g. a linear program) as a subroutine. This limits
the universality of automatic differentiation. Another alternative is
to replace the entire system with a single ML model, such as in Deep
Reinforcement Learning. However, this can severely limit the
interpretability of the resulting system.

We envisage AutoAI as allowing us to take advantage of end-to-end
learning without sacrificing the interpretability of the underlying
system. Instead of optimizing each component individually, we
introduce *Bayesian system optimization* (BSO). We will make use of
the end-to-end learning signals and attribute them to the system
sub-components through the construction of an interconnected network
of *surrogate models*, known as emulators, each of which is associated
with an individual component from the underlying ML-system. Instead of
optimizing each component individually (e.g. by classical Bayesian
optimization) in BSO we account for upstream and downstream
interactions in the optimization, leveraging our end-to-end knowledge
without damaging the interpretability of the underlying system.}

\endif
