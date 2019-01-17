---
title: "Data Science and Digital Systems"
subtitle: "The Three Ds of ML Systems Design"
abstract: >
  Machine learning solutions, in particular those based on deep
  learning methods, form an underpinning of the current revolution in
  “artificial intelligence” that has dominated popular press headlines
  and is having a significant influence on the wider tech agenda.
  
  In this talk I will give an overview of where we are now with
  machine learning solutions, and what challenges we face both in the
  near and far future. These include practical application of existing
  algorithms in the face of the need to explain decision making,
  mechanisms for improving the quality and availability of data,
  dealing with large unstructured datasets.
reveal: 2019-02-19-data-science-and-digital-systems.slides.html
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: Amazon Cambridge and University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
geometry: ['a4paper', 'margin=1in']
date: 2019-02-19
venue: Stu Hunter Resesearch Conference, Milan
transition: None
---

\include{talk-macros.tex}

\section{Introduction}

\include{_data-science/includes/gartner-hype-cycle-ai-bd-dm-dl-ml.md}

\include{_ai/includes/centrifugal-governor.md}

\section{Machine Learning, Artificial Intelligence and Data Science}

\include{_ml/includes/what-is-ml-2.md}
\include{_ai/includes/ai-vs-data-science-2.md}

\section{Human Intelligence}

\include{_ai/includes/embodiment-factors.md}
\include{_data-science/includes/evolved-relationship.md}

\subsection{A Definition of Intelligence}

\notes{The word intelligence is heavily overloaded, it means different things to different people. My own definition for intelligence is as follows [@Lawrence:embodiment17]. Intelligence is the use of information to achieve a goal with less resource. Here information is often in the form of data, resource is often energy (or strictly speaking free energy). 

This implies a more intelligent decision is one that either used less information and the same amount of resource or less resource for the same information, or any interpolation between.}

\include{_ml/includes/what-does-machine-learning-do.md}

\subsection{Deep Learning}

\slides{
* These are interpretable models: vital for disease etc.

* Modern machine learning methods are less interpretable

* Example: face recognition
}
\notes{Classical statistical models and simple machine learning models have a great deal in common. The main difference between the fields is philosophical. Machine learning practitioners are typically more concerned with the quality of prediciton (e.g. measured by ROC curve) while statisticians tend to focus more on the interpretability of the model and the validity of any decisions drawn from that interpretation. For example, a statistical model may be used to validate whether a large scale intervention (such as the mass provision of mosquito nets) has had a long term effect on disease (such as malaria). In this case one of the covariates is likely to be the provision level of nets in a particular region. The response variable would be the rate of malaria disease in the region. The parmaeter, $\beta_1$ associated with that covariate will demonstrate a positive or negative effect which would be validated in answering the question. The focus in statistics would be less on the accuracy of the response variable and more on the validity of the interpretation of the effect variable, $\beta_1$. 

A machine learning practitioner on the other hand would typically denote the parameter $\weightScalar_1$, instead of $\beta_1$ and would only be interested in the output of the prediction function, $\mappingFunction(\cdot)$ rather than the parameter itself.}

\include{_ml/includes/deep-learning-overview.md}

\section{Data Science and Professionalisation}

\include{_data-science/includes/a-time-for-professionalisation.md}

<!--
include{_data-science/includes/the-data-crisis.md} 

newslide{Rest of this Talk: Two Areas of Focus}

* Reusability of Data
* Deployment of Machine Learning Systems

newslide{Rest of this Talk: Two Areas of Focus}

* <s>Reusability of Data</s>
* Deployment of Machine Learning Systems

include{_data-science/includes/data-readiness-levels.md}

\newslide{Artificial Intelligence}

* Challenges in deploying AI.
* Currently this is in the form of "machine learning systems"

\newslide{Internet of People}

* Fog computing: barrier between cloud and device blurring.
    * Computing on the Edge
* Complex feedback between algorithm and implementation
  
\newslide{Deploying ML in Real World: Machine Learning Systems Design}

* Major new challenge for systems designers.
* Internet of Intelligence but currently:
	* AI systems are *fragile*

\include{_ml/includes/what-is-ml-2.md}
\include{_ai/includes/ai-vs-data-science-2.md}
-->

\section{The Physical World: Where Bits meet Atoms}

\notes{Before I joined Amazon I was invited to speak at their annual Machine Learning Conference. It has over two thousand attendees. I met the VP in charge of Amazon Special Projects, Babak Parviz. He said to me, the important thing about Amazon is that it's a "bits and atoms" company, meaning it moves both stuff (atoms) and information (bits). This quote resonated with me because it maps well on to my own definition of intelligence. Moving stuff requires resource. Moving, or processing, of information to move stuff more efficiently requires intelligence. 

That notion is the most fundamental notion for how the modern information infrastructure can help society. At Amazon the place where bits meet atoms is the *supply chain*. The movement of goods from manufacturer to customer, the supply chain.}

\include{_supply-chain/includes/ml-and-supply-chain.md}
\include{_ml/includes/or-control-econometrics-statistics-ml.md}

\todo{THE DANGER OF LOST TECHNOLOGIES THE PROGRAMMER CAN DEPLOY QUICKLY}

\section{The Three Ds of ML Systems Design}

\include{_ml/includes/the-3ds-of-ml-systems-design.md}

\include{_ml/includes/ml-outlook.md}

\section{Conclusion}

\newslide{Conclusion}

\slides{
* Technologically *evolving* environment.
* ML is a key component of decision making.
* Data is the key component of ML.
* ML is *critically* dependent on data.
* Challenges in *problem Decomposition*, *Data curation* and *model Deployment* 
}
\notes{We operate in a technologically evolving environment.  Machine learning is becoming a key coponent in our decision making capabilities, our intelligence and strategic command. However, technology drove changes in battlefield strategy. From the stalemate of the first world war to the tank-dominated Blitzkrieg of the second, to the asymmetric warfare of the present. Our technology, tactics and strategies are also constantly evolving. Machine learning is part of that evolution solution, but the main challenge is not to become so fixated on the tactics of today that we miss the evolution of strategy that the technology is suggesting.}

\newslide{Thanks!}

\slides{
* twitter: \@lawrennd
* blog: [http://inverseprobability.com](http://inverseprobability.com/blog.html)
* podcast: <http://thetalkingmachines.com>
* [Natural vs Artifical Intelligence](http://inverseprobability.com/2018/02/06/natural-and-artificial-intelligence)
* [Mike Jordan's Medium Post](https://medium.com/@mijordan3/artificial-intelligence-the-revolution-hasnt-happened-yet-5e1d5812e1e7)
}

\references





