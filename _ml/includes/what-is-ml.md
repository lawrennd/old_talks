\section{What is Machine Learning?}

\newslide{What is Machine Learning?}
\slides{
. . .

$$ \text{data} + \text{model} \xrightarrow{\text{compute}} \text{prediction}$$

. . .

-   **data** : observations, could be actively or passively
    acquired (meta-data).

. . .

-   **model** : assumptions, based on previous experience (other data!
    transfer learning etc), or beliefs about the regularities of
    the universe. Inductive bias.

. . .

-   **prediction** : an action to be taken or a categorization or a
    quality score.

. . .

-   Royal Society Report:
[Machine Learning: Power and Promise of Computers that Learn by Example](https://royalsociety.org/~/media/policy/projects/machine-learning/publications/machine-learning-report.pdf)
}

\notes{What is machine learning? At its most basic level machine learning is a combination of

$$\text{data} + \text{model} \xrightarrow{\text{compute}} \text{prediction}$$

where *data* is our observations. They can be actively or passively
acquired (meta-data). The *model* contains our assumptions, based on
previous experience. That experience can be other data, it can come
from transfer learning, or it can merely be our beliefs about the
regularities of the universe. In humans our models include our
inductive biases. The *prediction* is an action to be taken or a
categorization or a quality score. The reason that machine learning
has become a mainstay of artificial intelligence is the importance of
predictions in artificial intelligence. The data and the model are combined through computation.}

\newslide{What is Machine Learning?}
\slides{
$$\text{data} + \text{model} \xrightarrow{\text{compute}} \text{prediction}$$

> - To combine data with a model need:
      + **a prediction function** $\mappingFunction(\cdot)$ includes our beliefs about the regularities of the universe
      + **an objective function** $\errorFunction(\cdot)$ defines the cost of misprediction.
}

\notes{In practice we normally perform machine learning using two functions. To combine data with a model we typically make use of:

**a prediction function** a function which is used to make the predictions. It includes our beliefs about the regularities of the universe, our assumptions about how the world works, e.g. smoothness, spatial similarities, temporal similarities.

**an objective function** a function which defines the cost of misprediction. Typically it includes knowledge about the world's generating processes (probabilistic objectives) or the costs we pay for mispredictions (empiricial risk minimization).

The combination of data and model through the prediction function and the objectie function leads to a *learning algorithm*. The class of prediction functions and objective functions we can make use of is restricted by the algorithms they lead to. If the prediction function or the objective function are too complex, then it can be difficult to find an appropriate learning algorithm. Much of the acdemic field of machine learning is the quest for new learning algorithms that allow us to bring different types of models and data together.

A useful reference for state of the art in machine learning is the UK Royal Society Report, [Machine Learning: Power and Promise of Computers that Learn by Example](https://royalsociety.org/~/media/policy/projects/machine-learning/publications/machine-learning-report.pdf).

You can also check my blog post on ["What is Machine Learning?"](http://inverseprobability.com/2017/07/17/what-is-machine-learning)}
