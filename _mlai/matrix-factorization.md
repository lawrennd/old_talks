---
week: 2
title: "Objective Functions: A Simple Example with Matrix Factorisation"
abstract: |
  In this session we introduce the notion of objective functions and show how they can be used in a simple recommender system based on *matrix factorisation*.
youtube: Gq6bjcm8AqQ
---

\include{_mlai/includes/mlai-notebook-setup.md}

\newslide{Objective Function}
\slides{
- Last week we motivated the importance of probability.
- This week we motivate the idea of the 'objective function'.}

\slides{
\include{_ml/includes/perceptron.md}
\include{_ml/includes/linear-regression-iterative.md}
}


\newslide{Lab Class}

\slides{
- You will take the ideas you have learnt.
- You will apply them in the domain of *matrix factorisation*.
- Matrix factorization presents a different error function.
}

\addreading{@Rogers:book11}{Section 1.1.3} for loss functions.

\reading

\notes{In \refnotes{the introduction}{intro-probability} we saw how
we could load in a data set to pandas and use it for some simple data
processing. We computed variaous probabilities on the data and I encouraged you
to think about what sort of probabilities you need for prediction. This week we
are going to take a slightly different tack.}

\notes{Broadly speaking there are two dominating approaches to machine learning problems. We started to consider the first approach last week: constructing models based on defining the relationship between variables using probabilities. This week we will consider the second approach: which involves defining an *objective function* and optimizing it. What do we mean by an objective function? An objective function could be an *error function* a *cost function* or a *benefit* function. In evolutionary computing they are called *fitness* functions. But the idea is always the same. We write down a mathematical equation which is then optimized to do the learning. The equation should be a function of the *data* and our model *parameters*. We have a choice when optimizing, either minimize or maximize. To avoid confusion, in the optimization field, we always choose to minimize the function. If we have function that we would like to maximize, we simply choose to minimize the negative of that function.}

\notes{So for this lab session, we are going to ignore probabilities, but don't worry, they will return!}

\notes{This week we are going to try and build a simple movie recommender system using an objective function. To do this, the first thing I'd like you to do is to install some software we've written for sharing information across google documents.}

\include{_software/includes/pods-software.md}

\include{_ml/includes/movie-body-count-data.md}

\writeassignment{Data ethics. If you find data available on the
internet, can you simply use it without consequence? If you are given data by a
fellow researcher can you publish that data on line?}{1}{10}

\include{_ml/includes/recommender-systems.md}
\include{_ml/includes/recommender-data.md}
\include{_ml/includes/matrix-factorization.md}


\thanks

\reading

\exercises

\references


