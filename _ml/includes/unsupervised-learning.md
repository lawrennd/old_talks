\ifndef{unsupervisedLearning}
\define{unsupervisedLearning}

\editme

\section{Unsupervised Learning}

\newslide{Unsupervised Learning}
\slides{
* When you have data, $\inputVector$, but no labels $\dataVector$.
* Extract *structure* from data.
* Type of structure you are interested dependent on the broader context of the task.}
\notes{In unsupervised learning you have data, $\inputVector$, but no labels $\dataScalar$. The aim in unsupervised learning is to extract structure from data. The type of structure you are interested in is dependent on the broader context of the task. In supervised learning that context is very much driven by the labels. Supervised learning algorithms try and focus on the aspects of the data which are relevant to predicting the labels. But in unsupervised learning there are no labels.} 

\subsection{Context}
\slides{
* Supervised learning:  context is very much driven by the labels.
* Humans easily sort objects  e.g. animals and vehicles
* For large data sets or data we are not used to (high dimensional data) would like to automate.
    * E.g., an e-commerce company algorithm for sorting products into groups.}
\notes{
Humans can easily sort a number of objects into objects that share similar characteristics. We easily categorize animals or vehicles. But if the data is very large this is too slow. Even for smaller data, it may be that it is presented in a form that is unintelligible for humans. We are good at dealing with high dimensional data when it's presented in images, but if it's presented as a series of numbers, we find it hard to interpret. In unsupervised learning we want the computer to do the sorting for us. For example, an e-commerce company might need an algorithm that can go through its entire list of products and automatically sort them into groups such that similar products are located together.}

\subsection{Discrete vs Continuous}
\slides{
* Supervised learning is broadly divided into classification and regression
* Unsupervised learning can be split too:

1. methods that cluster the data
2. methods that represent the data as (lower dimensional) continuous values.}
\notes{Supervised learning is broadly divided into classification: i.e. wake word classification in the Amazon Echo, and regression, e.g. shelf life prediction for perishable goods.  Similarly, unsupervised learning can be broadly split into methods that cluster the data (i.e. provide a discrete label) and methods that represent the data as a continuous value.}


\include{_ml/includes/clustering.md}
\include{_ml/includes/dimensionality-reduction.md}

\endif
