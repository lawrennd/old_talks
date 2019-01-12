\ifndef{whatIsMl}
\define{whatIsMl}
\editme
\section{What is Machine Learning?}

\include{_ml/includes/data-plus-model.md}

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
\endif
