### What is Machine Learning?

\slides{
. . .

$$ \text{data} + \text{model} \rightarrow \text{prediction}$$

. . .

-   $\text{data}$ : observations, could be actively or passively
    acquired (meta-data).

. . .

-   $\text{model}$ : assumptions, based on previous experience (other data!
    transfer learning etc), or beliefs about the regularities of
    the universe. Inductive bias.

. . .

-   $\text{prediction}$ : an action to be taken or a categorization or a
    quality score.

. . .

-   Royal Society Report:
[Machine Learning: Power and Promise of Computers that Learn by Example](https://royalsociety.org/~/media/policy/projects/machine-learning/publications/machine-learning-report.pdf)
}

\notes{First of all, we'll consider the question, what is machine learning? By my definition Machine Learning is a combination of

$$\text{data} + \text{model} \rightarrow \text{prediction}$$

and the reason that machine learning has become a mainstay of artificial intelligence is the importance of predictions in artificial intelligence.
}

### What is Machine Learning?

$$\text{data} + \text{model} \rightarrow \text{prediction}$$

\slides{
. . .

* To combine data with a model need:

. . .

* **a prediction function** $\mappingFunction(\cdot)$ includes our beliefs about the regularities of the universe

. . .

* **an objective function** $\errorFunction(\cdot)$ defines the cost of misprediction.
}

\notes{
In practice we normally perform machine learning using two functions. To combine data with a model we typically make use of:

**a prediction function** a function which is used to make the predictions. It includes our beliefs about the regularities of the universe, our assumptions about how the world works, e.g. smoothness, spatial similarities, temporal similarities.

**an objective function** a function which defines the cost of misprediction. Typically it includes knowledge about the world's generating processes (probabilistic objectives) or the costs we pay for mispredictions (empiricial risk minimization).

A useful reference for state of the art in machine learning is the UK Royal Society Report, [Machine Learning: Power and Promise of Computers that Learn by Example](https://royalsociety.org/~/media/policy/projects/machine-learning/publications/machine-learning-report.pdf).
}
