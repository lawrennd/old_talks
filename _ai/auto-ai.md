---
title: "AutoAI"
subtitle: "Putting Systems at the Heart of Machine Learning"
abstract: >
  Deployed artificial intelligence solutions consist of interacting components often trained as the result of *supervised machine learning*. Automatic training of these sub-components is known as AutoML. But the real world challenges of deployment consist of the monitoring of system performance in the real world, in terms of accuracy but also for fairness and bias. 
  
  To make such systems easily maintainable there is a need for automation of the process of monitoring and redeploying models as well as checking the quality of the overall system decomposition. 
  
  In contrast to AutoML, we call this system-wide approach "Auto AI". This is the subject of my Turing Fellowship 
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Cambridge
  twitter: lawrennd
  url: http://inverseprobability.com
blog: 
date: 2019-10-30
venue: 10 Minute Talk, Wednesday Meeting, Department of Computer Science and Technology, University of Cambridge
transition: None
---

\include{talk-macros.tex}

\subsection{Introduction}

\notes{Artificial Intelligence (AI) solutions
are based on machine learning algorithms (ML), but each ML
solution is only capable of solving a restricted task, e.g. a
supervised learning problem. Consequently, any AI that we deploy today
takes the form of an ML System with interacting
components. As these ML systems become larger and more complex,
challenges in interpretation, explanation, accuracy and fairness
arise. This project addresses these issues. The challenges
include [@Lawrence:threeds19]: the *decomposition* of the system, the
*data* availability, and the performance of the system in
*deployment*. Collectively we refer to these challenges as the "Three
Ds of ML Systems Design".}

\include{_ai/includes/turing-ai-fellowship.md}
\include{_ai/includes/ride-allocation-prediction.md}
\include{_ai/includes/the-promise-of-ai.md}
\include{_ml/includes/ml-paradigm-shift.md}

\notes{This gives vulnerabilities that we are exposing to the natural environment. Many security problems that we face today are the result of bugs that mean that code and data are not separate in thee systems we deploy, imagine what will happen when we deploy systems that purposefully short-circuit this protection into uncontrolled environments.}


\include{_ai/includes/ml-system-decomposability.md}
\subsection{Data Oriented Architectures}
\slides{
* Convert data to a *first-class citizen*.
* View system as operations on *data streams*.
* Expose data operations in a programmatic way.
}
\notes{In a streaming architecture we shift from management of services, to management of data streams. Instead of worrying about availability of the services we shift to worrying about the quality of the data those services are producing.}


\subsection{Streaming System}
\slides{
* Move from pull updates to push updates.
* Operate on rows rather than columns.
* Lead to stateless logic: persistence handled by system.
* Example Apache Kafka + Apache Flink
}
\notes{Characteristics of a streaming system include a move from *pull* updates to *push* updates, i.e. the computation is driven by a change in the input data rather than the service calling for input data when it decides to run a computation. Streaming systems operate on 'rows' of the data rather than 'columns'. This is because the full column isn't normally available as it changes over time. As an important design principle, the services themselves are stateless, they take their state from the streaming ecosystem. This ensures the inputs and outputs of given computations are easy to declare. As a result, persistence of the data is also handled by the streaming ecosystem and decisions around data retention or recomputation can be taken at the systems level rather than the component level.}


\subsection{Hypothetical Streams}

\slides{
* Real stream --- share prices
    * derived *hypothetical* stream --- share prices in future.
* Hypothetical constrained by
    * input constraints.
    * decision functional
    * computational requirements (latency)
}


\notes{We'll call the future price a hypothetical stream. 

A hypothetical stream is a desired stream of information which cannot be directly accessed. The lack of direct access may be because the events happen in the future, or there may be some latency between the event and the availability of the data. 

Any hypothetical stream will only be provided as a prediction, ideally with an error bar. 

The nature of the hypothetical Anne needs is dependent on her decision-making process. In Anne's case it will depend over what period she is expecting her returns. In MDOP Anne specifies a hypothetical that is derived from the pricing stream. 

It is not the price stream directly, but Anne looks for *future* predictions from the price stream, perhaps for price in $T$ days' time.

At this stage, this stream is merely typed as a hypothetical.

There are constraints on the hypothetical, they include: the *input* information, the upper limit of latency between input and prediction, and the decision Anne needs to make (how far ahead, what her upside, downside risks are). These three constraints mean that we can only recover an approximation to the hypothetical.}

\subsection{Hypothetical Advantage}

\slides{* Modelling is now required.
* But modelling is declared in the ecosystem.
* If it's manual, warnings can be used 
     * calibration, fairness, dataset shift
* Opens door to auto-adaptable ML.
}

\notes{What is the advantage to defining things in this way? By defining, clearly, the two streams as real and hypothetical variants of each other, we now enable automation of the deployment and any redeployment process. The hypothetical can be *instantiated* against the real, and design criteria can be constantly evaluated triggering retraining when necessary.}

\include{_ai/includes/safe-boda.md}

\include{_ai/includes/ride-allocation-prediction.md}


\notes{Let's consider a ride sharing app, for example the SafeBoda system. 

Anne is on her way home now; she wishes to hail a car using a ride sharing app. 

The app is designed in the following way. On opening her app Anne is notified about drivers in the nearby neighborhood. She is given an estimate of the time a ride may take to come.

Given this information about driver availability, Anne may feel encouraged to enter a destination. Given this destination, a price estimate can be given. This price is conditioned on other riders that may wish to go in the same direction, but the price estimate needs to be made before the user agrees to the ride. 

Business customer service constraints dictate that this price may not change after Anne's order is confirmed. 

In this simple system, several decisions are being made, each of them on the basis of a hypothetical.

When Anne calls for a ride, she is provided with an estimate based on the expected time a ride can be with her. But this estimate is made without knowing where Anne wants to go. There are constraints on drivers imposed by regional boundaries, reaching the end of their shift, or their current passengers mean that this estimate can only be a best guess.

This best guess may well be driven by previous data.
}

\include{_data-science/includes/ride-sharing-soa-doa.md}
\include{_data-science/includes/information-dynamics.md}
\include{_uq/includes/auto-ai.md}

\include{_ai/includes/auto-ai-conclusions.md}



\thanks

\references


