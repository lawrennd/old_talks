\subsection{Decomposition}
\slides{
* ML is not Magical Pixie Dust.
* It cannot be sprinkled thoughtlessly.
* We cannot simply *automate all decisions through data*
}
\newslide{Decomposition}
\slides{
We are constrained by:

1. Our *data*.
2. The *models*.
}

\notes{Machine learning is not magical pixie dust, we cannot simply automate all decisions through data. We are constrained by our data (see below) and the models we use.[^tribal]  Machine learning models are relatively simple function mappings that include characteristics such as smoothness. With some famous exceptions, e.g. speech and image data, inputs are constrained in the form of vectors and the model consists of a mathematically well behaved function. This means that some careful thought has to be put in to the right sub-process to automate with machine learning. This is the challenge of *decomposition* of the machine learning system.

[^tribal]: We can also become constrained by our tribal thinking, just as each of the other groups can.
}
\newslide{Decomposition of Task}
\slides{
* Careful thought needs to be put into sub-processes of task.
* Any repetitive task is a candidate for automation.
}
\notes{Any repetitive task is a candidate for automation, but many of the repetitive tasks we perform as humans are more complex than any individual algorithm can replace. The selection of which task to automate becomes critical and has downstream effects on our overall system design.}

\subsection{Pigeonholing}

\div{\includeimg{../slides/diagrams/TooManyPigeons.jpg}{60%}}{}{text-align:center}
\notes{\caption{The machine learning systems decomposition process calls for separating a complex task into decomposable separate entities. A process we can think of as *[pigeonholing](https://en.wikipedia.org/wiki/Pigeonholing)*.}}

\notes{Some aspects to take into account are}

\newslide{Pigeonholing}
\slides{
1. Can we decompose decision we need to repetitive sub-tasks where inputs and outputs are well defined?
2. Are those repetitive sub-tasks well represent by a mathematical mapping?
}
\notes{Some aspects to take into account are

1.  Can we refine the decision we need to a set of repetitive tasks
    where input information and output decision/value is well defined?
2.  Can we represent each sub-task we’ve defined with a mathematical
    mapping?
}
\notes{The representation necessary for the second aspect may involve massaging
of the problem: feature selection or adaptation. It may also involve
filtering out exception cases (perhaps through a pre-classification).}

\notes{All else being equal, we’d like to keep our models simple and
interpretable. If we can convert a complex mapping to a linear mapping
through clever selection of sub-tasks and features this is a big win.}

\notes{For example, Facebook have *feature engineers*, individuals whose main
role is to design features they think might be useful for one of their
tasks (e.g. newsfeed ranking, or ad matching). Facebook have a
training/testing pipeline called
[FBLearner](https://www.facebook.com/Engineering/posts/fblearner-flow-is-a-machine-learning-platform-capable-of-easily-reusing-algorith/10154077833317200/).
Facebook have predefined the sub-tasks they are interested in, and they
are tightly connected to their business model.

It is easier for Facebook to do this because their business model is
heavily focused on user interaction. A challenge for companies that have
a more diversified portfolio of activities driving their business is the
identification of the most appropriate sub-task. A potential solution to
feature and model selection is known as *AutoML* [@Feurer:automl15]. Or we
can think of it as using Machine Learning to assist Machine Learning.
It’s also called meta-learning. Learning about learning. The input to
the ML algorithm is a machine learning task, the output is a proposed
model to solve the task.}

\newslide{A Trap}
\slides{
* Over emphasis on the *type* of model we're deploying.
* Under emphasis on the appropriateness of the task decomposition.
}
\notes{One trap that is easy to fall in is too much emphasis on the type of model we have deployed rather than the appropriateness of the task decomposition we
have chosen.}

\recommendation{Conditioned on task decomposition, we should
automate the process of model improvement. Model updates should not be
discussed in management meetings, they should be deployed and updated as
a matter of course. Further details below on model deployment, but model
updating needs to be considered at design time. This is the domain of
AutoML.}

\newslide{Chicken and Egg}

\div{\includeimg{../slides/diagrams/ai/chicken-and-egg.jpg}}{}{text-align:center}
\notes{\caption{The answer to the question which comes first, the chicken or the egg is simple, they co-evolve [@Popper:conjectures63]. Similarly, when we place components together in a complex machine learning system, they will tend to co-evolve and compensate for one another.}}

\newslide{Co-evolution}
\slides{
* Absolute decomposition is impossible. 
* If we deploy a weak component in one place, downstream system will compensate.
* Systems *co-evolve* ... there is no *simple* solution
* Trade off between *performance* and *decomposability*.
    * Need to monitor deployment
}
\notes{To form modern decision making systems, many components are interlinked.  We decompose our complex decision making into individual tasks, but the performance of each component is dependent on those upstream of it.}

\notes{This naturally leads to co-evolution of systems, upstream errors can be
compensated by downstream corrections.}

\notes{To embrace this characteristic, end-to-end training could be considered. Why produce the best forecast by metrics when we can just produce the best forecast for our systems? End to end training can lead to improvements in performance, but it would also damage our systems decomposability and its interpretability, and perhaps its adaptability.}

\notes{The less human interpretable our systems are, the harder they are to adapt to different circumstances or diagnose when there's a challenge.  The trade-off between interpretability and performance is a constant tension which we should always retain in our minds when performing our system design.}

