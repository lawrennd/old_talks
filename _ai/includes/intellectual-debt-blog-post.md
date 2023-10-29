\ifndef{intellectualDebtBlogPost}
\define{intellectualDebtBlogPost}

\editme

\subsection{Intellectual Debt}

\figure{\includepng{\diagramsDir/ai/2020-02-12-intellectual-debt}{70%}}{Jonathan Zittrain's term to describe the challenges of explanation that come with AI is Intellectual Debt.}{intellectual-debt}

\notes{In the context of machine learning and complex systems, Jonathan Zittrain has coined the term ["Intellectual Debt"](https://medium.com/berkman-klein-center/from-technical-debt-to-intellectual-debt-in-ai-e05ac56a502c) to describe the challenge of understanding what you've created. In [the ML@CL group we've been foucssing on developing the notion of a *data-oriented architecture*](https://mlatcl.github.io/projects/data-oriented-architectures-for-ai-based-systems.html) to deal with intellectual debt [@Cabrera-realworld23].}

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
validation sets that explore fairness or accuracy of the model.}

\endif
