\ifndef{fitSystems}
\define{fitSystems}

\editme

\subsection{FIT Models to FIT Systems}

\slides{* Focus in machine learning has been on FAcT learning.
* Fairness, accountability and Transparency in individual models.
* But individual models aren't the problem. 
* Fariness, interpetability and transparency required for whole system.}

\notes{Zittrain points out the challenge around the lack of interpretability
of individual ML models as the origin of intellectual debt. In machine
learning I refer to work in this area as fairness, interpretability
and transparency or FIT models. To an extent I agree with Zittrain,
but if we understand the context and purpose of the decision making, I
believe this is readily put right by the correct monitoring and
retraining regime around the model. A concept I refer to as
"progression testing". Indeed, the best teams do this at the moment,
and their failure to do it feels more of a matter of technical debt
rather than intellectual, because arguably it is a maintenance task
rather than an explanation task. After all, we have good statistical
tools for interpreting individual models and decisions when we have
the context. We can linearise around the operating point, we can
perform counterfactual tests on the model. We can build empirical
validation sets that explore fairness or accuracy of the model.

So, this is where, my understanding of intellectual debt in ML systems
departs, I believe from John Zittrain's. The long-term challenge is
*not* in the individual model. We have excellent statistical tools for
validating what any individual model, the long-term challenge is the
complex interaction between different components in the decomposed
system, where the original intent of each component has been forgotten
(except perhaps by Lancelot) and each service has been repurposed. We need to move from FIT models to FIT systems.

How to address these challenges? With collaborators I've been working
towards a solution that contains broadly two parts. The first part is
what we refer to as "Data-Oriented Architectures". The second part is "meta modelling", machine learning techniques that help us model the models. }


\endif
