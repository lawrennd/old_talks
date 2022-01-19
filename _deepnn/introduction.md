---
layout: lecture
title: Introduction
week: 1
session: 1
author:
- given: Neil D.
  family: Lawrence
  institution: University of Cambridge
  url: http://inverseprobability.com
abstract: >
  This lecture will give the background to what this course is about, and how it fits in to other material you can find on deep neural network models. It explains deep neural networks are, how they fit into the wider context of the field and why they are successful.
talkscam:
venue: LT1, William Gates Building
youtube: 9pjIhoeXlnI
reveal: True
ipynb: True
date: 2022-01-20
time: "14:00"
start: "14:00"
end: "15:00"
---

\include{_deepnn/includes/overview-2021.md}
\include{_ml/includes/what-is-ml.md}

\subsection{Ingredients}

\notes{The three key ingredients of machine learning are a model, data and compute. Note, that this necessarily implies that an *algorithm* exists to combine the model with the data and that algorithm is what consumes the compute.}

\notes{So how do these ingredients pan out in our recipe for deep learning? To better understand this, we're going to add more historical context and go back go 1997 when, here in Cambridge, there was a six-month programme at the Isaac Newton Institute run on Machine Learning, Neural Networks and Generalisation.}

\include{_ml/includes/cybernetics-ratio-club.md}
\include{_ml/includes/connectionist-revival.md}

<!--include{_ml/includes/what-does-machine-learning-do.md}-->

\include{_ml/includes/neil-newton-institute.md}

\newslide{}

\figure{\includegif{\diagramsDir/ml/le-net-5}{60%}}{Gif animation of LeNet-5 in action.}{le-net-5}

\newslide{}

\figure{\includegif{\diagramsDir/ml/le-net-translate}{60%}}{Gif animation of LeNet-5 in action. Here the translation invariance of the network is being tested.}{le-net-5}

\newslide{}

\figure{\includegif{\diagramsDir/ml/le-net-scale}{60%}}{Gif animation of LeNet-5 in action, here the scale invariance of the network is being tested.}{le-net-5}

\notes{But at the same meeting Vladmir Vapnik was there as was Bernhard Scholkopf. Corinna Cortes, Bernard Boser, Isabelle Guyon and Vladmir Vapnik were all instrumental in developing the Support Vector Machine.}

\newslide{}

\figure{\threeColumns{\includejpg{\diagramsDir/ml/corinna-cortes}{100%}{}{left}}{\includejpg{\diagramsDir/ml/isabelle-guyon}{100%}{}{center}}{\includejpg{\diagramsDir/ml/vladmir-vapnik}{100%}{}{right}}{30%}{30%}{30%}}{Corinna Cortes, Isabelle Guyon and Vladmir Vapnik. Three of the key people behind the support vector machine [@Boser-optimal92,@Cortes:svnet95]. All were based at Bell Labs in the 1990s.}{cortes-guyon-vapnik}

\notes{Also attending the summer school at the Newton Institute was Bernhard Schölkopf. He had shown that, on the same USPS digits data set, the support vector machine was able to achieve an error of 4.2% [@Scholkopf:comparing97]. It was also mathematically more elegant than the neural network approaches. Even on larger data sets, by incorporating the translation invariance [@Scholkopf:incorporating96], the support vector machine was able to achieve similar error rates to convolutional neural networks.}


\newslide{}

> This work points out the necessity of having flexible "network design" software tools that ease the design of complex, specialized network architectures
>
> From conclusions of @LeCun:zip89

\newslide{}

\figure{\columns{\includepng{\diagramsDir/ml/olga-russakovsky}{100%}{}{left}}{\includepng{\diagramsDir/ml/fei-fei-li}{100%}{}{right}}{50%}{50%}}{Olga Russakovsky, Fei Fei Li. Olga and Fei Fei led the creation of the ImageNet database that enabled convolutional neural networks to show their true potential. The data base contains millions of images.}{russakovsky-li}

\subsection{The Third Wave}

* Data (many data, many classes)
* Compute (GPUs)
* Stochastic Gradient Descent
* Software (autograd)

\subsection{Domains of Use}

* Perception and Representation
  1. Speech
  2. Vision
  3. Language

\subsection{Experience}

* Bringing it together:
  * Unsupervised pre-training
  * Initialisation and RELU
  * A Zoo of methods and models

\subsecion{New}

* Why do they generalize well?

\subsection{Conclusion}

* Understand the principles behind:
  * Generalization
  * Optimization
  * Implementation (hardware)

* Differen NN Architectures


\reading

\thanks

\references
