---
title: "Machine Learning Systems Design"
subtitle: "Making Amazon a Data First Company"
abstract: >
  Machine learning solutions, in particular those based on deep learning methods, form an underpinning of the current revolution in “artificial intelligence” that has dominated popular press headlines and is having a significant influence on the wider tech agenda.
  
  In this talk I will give an overview of where we are now with machine learning solutions, and what challenges we face both in the near and far future. These include practical application of existing algorithms in the face of the need to explain decision making, mechanisms for improving the quality and availability of data, dealing with large unstructured datasets.
ipynb: 2018-09-20-machine-learning-systems-design-data-first.ipynb
reveal: 2018-09-20-machine-learning-systems-design-data-first.slides.html
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: Amazon Cambridge and University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
date: 2018-09-20
venue: Analyticon
transition: None
---

\include{talk-macros.tex}

\notes{Machine learning allows us to extract knowledge from data to
form a prediction.}

$$\text{model} + \text{data} \rightarrow \text{prediction}$$

\notes{A machine learning prediction is made by combining a model with data to
form a prediction. The manner in which this is done gives us the machine
learning algorithm.}

Machine learning models are *mathematical models* which make weak
assumptions about data, e.g. smoothness assumptions. By combining these
assumptions with the data we observe we can interpolate between data
points or, occasionally, extrapolate into the future.

Machine learning is a technology which strongly overlaps with the
methodology of statistics. From a historical/philosophical view point,
machine learning differs from statistics in that the focus in the
machine learning community has been primarily on accuracy of prediction,
whereas the focus in statistics is typically on the interpretability of
a model and/or validating a hypothesis through data collection.}

\notes{The rapid increase in the availability of compute and data has led to
the increased prominence of machine learning. This prominence is
surfacing in two different, but overlapping domains: data science and
artificial intelligence.}

\subsection{Artificial Intelligence and Data Science}

\notes{Artificial intelligence has the objective of endowing computers with
human-like intelligent capabilities. For example, understanding an image
(computer vision) or the contents of some speech (speech recognition),
the meaning of a sentence (natural language processing) or the
translation of a sentence (machine translation).}

\notes{The machine learning approach to artificial intelligence is to collect
and annotate a large data set from humans. The problem is characterized
by input data (e.g. a particular image) and a label (e.g. is there a car
in the image yes/no). The machine learning algorithm fits a mathematical
function (I call this the *prediction function*) to map from the input
image to the label. The parameters of the prediction function are set by
minimizing an error between the function’s predictions and the true
data. This mathematical function that encapsulates this error is known
as the *objective function*.}

\notes{This approach to machine learning is known as *supervised learning*.
Various approaches to supervised learning use different prediction
functions, objective functions or different optimization algorithms to
fit them.}

\notes{For example, *deep learning* makes use of *neural networks* to form the
predictions. A neural network is a particular type of mathematical
function that allows the algorithm designer to introduce invariances
into the function.}

\notes{An invariance is an important way of including prior understanding in a
machine learning model. For example, in an image, a car is still a car
regardless of whether it’s in the upper left or lower right corner of
the image. This is known as translation invariance. A neural network
encodes translation invariance in *convolutional layers*. Convolutional
neural networks are widely used in image recognition tasks.}

\notes{An alternative structure is known as a recurrent neural network (RNN).
RNNs neural networks encode temporal structure. They use auto regressive
connections in their hidden layers, they can be seen as time series
models which have non-linear auto-regressive basis functions. They are
widely used in speech recognition and machine translation.}

\notes{Amazon has deployed machine learning in the Alexa (deep neural networks,
convolutional neural networks for speech recognition), in Amazon Go
(convolutional neural networks for person recognition and pose
detection).}

\notes{The field of data science is related to AI, but philosophically
different. It arises because we are increasingly creating large amounts
of data through *happenstance* rather than active collection. In the
modern era data is laid down by almost all our activities. The objective
of data science is to extract insights from this data.}

\notes{Classically, in the field of statistics, data analysis proceeds by
assuming that the question (or scientific hypothesis) comes before the
data is created. E.g., if I want to determine the effectiveness of a
particular drug I perform a *design* for my data collection. I use
foundational approaches such as randomization to account for
confounders. This made a lot of sense in an era where data had to be
actively collected. The reduction in cost of data collection and storage
now means that many data sets are available which weren’t collected with
a particular question in mind. This is a challenge because bias in the
way data was acquired can corrupt the insights we derive. In SCOT/IPC we
have IPC labs performing classical statistical studies, but the
opportunity is to use data science techniques to better guide our
question selection or even answer a question without the expense of a
full randomized control trial (referred to as A/B testing in modern
internet parlance).}

\subsection{Machine Learning in SCOT/IPC}

\notes{SCOT/IPC is a large scale automated decision making network. Our aim is
to make decisions not only based on our models of customer behavior (as
observed through data), but also by accounting for the structure of our
fulfilment center, and delivery network.}

\notes{Many of the most important questions in SCOT/IPC take the form of
counterfactuals. E.g. “What would happen if we opened a fulfilment
center in Cambridge?” A counter factual is a question that implies a
mechanistic understanding of our systems. It goes beyond simple
smoothness assumptions or translation invariants. It requires a
physical, or *mechanistic* understanding of our network. For this reason
the type of models we deploy in SCOT/IPC often involve simulations or
more mechanistic understanding of our network.}

\notes{In SCOT/IPC Machine Learning alone is not enough, we need to bridge
between models that contain real mechanisms and models that are entirely
data driven.}

\notes{This is challenging, because as we introduce more mechanism to our
models, it becomes harder to develop efficient algorithms to match those
models to data.}

\notes{Some examples of machine learning models being deployed across SCOT/IPC
I've seen emerging this week are}


\notes{
-   Long term short term memory (LSTM) neural networks were mentioned in
    the S&OP three year plan for launch in Q3 2019 for improved accuracy
    in *FBA planning*. An LSTM is a type of recurrent neural network
    that incorporates a 'long term memory', allowing long range
    interactions to be stored in the model.}

-   The *Mariana* model for neural network forecasting is based on a
    neural network with multiple hidden layers that directly predicts
    quantiles of future forecasts. This supersedes previous models
    (Delphi) based on Gaussian process ideas.
}

\subsection{Operations Research, Control, Econometrics, Statistics and Machine Learning}

\notes{Different academic fields are born in different eras, driven by
different motivations and arrive at different solutions.}

\notes{The separation between these fields can almost become tribal, and from
one perspective this can be very helpful. Each tribe can agree on a
common language, a common set of goals and a shared understanding of the
approach they’ve chose for those goals. This ensures that best practice
can be developed and shared and as a result quality standards rise.}

\notes{This is the nature of our *professions*. Medics, lawyers, engineers and
accountants all have a system of shared best practice that they deploy
efficiently in the resolution of a roughly standardized set of problems
where they deploy (broken leg, defending a libel trial, bridging a
river, ensuring finances are correct).}

\notes{Control, statistics, economics, operations research are all established
professions. Techniques are established, often at undergraduate level,
and graduation to the profession is regulated by professional bodies.
This system works well as long as the problems we are easily categorized
and mapped onto the existing set of known problems.}

\notes{However, at another level our separate professions of OR, statistics and
control engineering are just different views on the same problem. Just
as any tribe of humans need to eat and sleep, so do these professions
depend on data, modelling, optimization and decision-making.}

\notes{At SCOT/IPC we are doing something that has never been done before,
optimizing and evolving the world’s largest decision making network. The
ambition of Amazon to scale and automate in a *data driven* manner means
that a tribal approach to problem solving can hinder our progress. Any
tribe of hunter gatherers would struggle to understand the operation of
a modern city. Similarly, SCOT/IPC needs to develop cross-functional
skill sets to address the modern problems we face, not the problems that
were formulated in the past.}

\notes{Many of the challenges we face are at the interface between our tribal
expertize. We have particular cost functions we are trying to minimize
(an expertise of OR) but we have large scale feedbacks in our system (an
expertise of control). We also want our systems to be adaptive to
changing circumstances, to perform the best action given the data
available (an expertise of machine learning and statistics).}

\notes{Taking the tribal analogy further, we could imagine each of our
professions as a separate tribe of hunter-gathers, each with particular
expertise (e.g. fishing, deer hunting, trapping). Each of these tribes
has their own approach to eating to survive, just as each of our
localized professions has its own approach to modelling. But in this
analogy, Amazon is not a wilderness, it is an emerging metropolis. Our
new task is to feed our population through a budding network of
supermarkets. While we may be sourcing our food in the same way, this
requires new types of thinking that don't belong in the pure domain of
any of our existing tribes.}

\notes{For our biggest challenges, focusing on the differences between these
fields is unhelpful, we should consider their strengths and how they
overlap. Fundamentally all these fields are focused on taking the right
action given the information available to us. They need to work in
*synergy* for us to make progress.}

\notes{By way of example, triggered by the July IPC MBR on Peak Management
(with Jenny Freshwater), the Cambridge team met with the Topline
forecasting team on Wednesday. Our aim was to obtain better
methodological understanding. We didn't make much progress on that side
in our first meeting, but we did notice that almost the entire team was
made up of economists. Topline may well be best handled by econometric
models, because they incorporate some 'mechanistic' understanding of the
economic drivers of growth (e.g. how growth in Prime has a downstream
effect on overall growth). However, it is also a comfortable mode of
operation for teams to be made up of only one tribe. We need to make
sure that our horizons aren't narrowed by forming such specialist teams.}

\notes{**Recommendation**: We should be aware of the limitations of a single
tribal view of any of our problem sets. Where our modelling is dominated
by one perspective (e.g. economics, OR, control, ML) we should ensure
cross fertilization of ideas occurs through scientific review and team
rotation mechanisms that embed our scientists (for a short period) in
different teams across the organization.}

\subsection{Challenges for Machine Learning in General}

\notes{We can characterize the challenges for integrating machine learning
within our systems as the three Ds. Design, Data and Deployment.}

\notes{The first two components *design* and *data* are interlinked, but we
will first outline the design challenge. Below we will mainly focus on
*supervised learning* because this is arguably the technology that is
best understood within machine learning.}

\subsection{Design}

\notes{Machine learning is not magical pixie dust, we cannot simply automate
all decisions through data. We are constrained by our data (see below)
and the models we use.[^1] Machine learning models are relatively simple
function mappings that include characteristics such as smoothness. With
some famous exceptions, e.g. speech and image data, inputs are
constrained in the form of vectors and the model consists of a
mathematically well behaved function. This means that some careful
thought has to be put in to the right sub-process to automate with
machine learning.

[^1]: We can also become constrained by our tribal thinking, just as
    each of the other groups can.
}

\notes{Any repetitive task is a candidate for automation, but many of the
repetitive tasks we perform as humans are more complex than any
individual algorithm can replace. The selection of which task to
automate becomes critical and has downstream effects on our overall
system design.}

\notes{Some aspects to take into account are}

\notes{1.  Can we refine the decision we need to a set of repetitive tasks
    where input information and output decision/value is well defined?}

\notes{2.  Can we represent the sub-task we’ve defined with a mathematical
    mapping?}

\notes{The design for the second task may involve massaging of the problem:
feature selection or adaptation. It may also involve filtering out
exception cases (perhaps through a pre-classification).}

\notes{All else being equal, we’d like to keep our models simple and
interpretable. If we can convert a complex mapping to a linear mapping
through clever selection sub-task and features this is a big win.}

\notes{For example, Facebook have *feature engineers*, individuals whose main
role is to design features they think might be useful for one of their
tasks (e.g. newsfeed ranking, or ad matching). Facebook have a
training/testing pipeline that allows for efficient evaluation of the
utility of any new proposed feature across a range of pre-selected and
extendable machine learning models (random forests, linear regression
etc). Facebook have predefined the sub-tasks they are interested in, and
they are tightly connected to their business model. A challenge for
companies that have a more diversified portfolio of activities is the
identification of the most appropriate sub-task. A potential solution to
feature and model selection is known as *auto ML*. Or we can think of it
as using Machine Learning to assist Machine Learning. It’s also called
meta-learning. Learning about learning. The input to the ML algorithm is
a machine learning task, the output is a proposed model to solve the
task.}

\notes{One observation form SCOT/IPC (and Amazon in general) is that relative
to Facebook there is too much emphasis on the type of model we have
deployed rather than the appropriateness of the task decomposition we
have chosen.}

\notes{**Recommendation**: Conditioned on task decomposition, we should
automate the process of model improvement. If each model update is being
discussed in an MBR this is a significant drain on LT time. See also
below section on model deployment.}

\notes{To form modern decision making systems, many components are interlinked.
We decompose our complex decision making into individual tasks, but the
performance of each component is dependent on those upstream of it.}

\notes{This naturally leads to co-evolution of systems, upstream errors can be
compensated by downstream corrections. An example of this in SCOT/IPC is
the improvement in forecasting brought about in Mariana (by Mariana
metrics) *not* being translated to performance in the lab. Analysis of
the problem isn't yet complete, but one hypothesis is that this due to
compensatory behavior being incorporated into IPC Simulation due to the
poor quality of the previous forecast (at the P90 level the old
forecast, Delphi, was badly calibrated).}

\notes{To embrace this characteristic, end-to-end training is considered. Why
produce the best forecast by metrics when we can just produce the best
forecast for our systems? End to end training can lead to improvements
in performance, but it would also damage our systems decomposability and
its interpretability, and perhaps its adaptability.}

\notes{The less human interpretable our systems are, the harder they are to
adapt to different circumstances or diagnose when there's a challenge.
The trade-off between interpretability and performance is a constant
tension which we should always retain in our minds when performing our
system design.

\subsection{Data}

\notes{It is difficult to overstate the importance of data. It is half of the
equation for machine learning, but is often utterly neglected. I
speculate that there are two reasons for this. Firstly, data cleaning is
tedious. It doesn’t seem to consist of the same intellectual challenges
that are inherent in constructing complex mathematical models and
implementing them in code. Secondly, data cleaning is highly complex, it
requires a deep understanding of how machine learning systems operate
and good intuitions about the data itself, the domain from which data is
drawn (e.g. Supply Chain) and what downstream problems might be caused
by poor data quality.}

\notes{A consequence these two reasons, data cleaning seems difficult to
formulate into a readily teachable set of principles. As a result it is
heavily neglected in courses on machine learning and data science.
Despite data being half the equation, most University courses spend
little to no time on its challenges.}

\notes{Anecdotally, talking to our applied and research scientists. Most say
they spend 80% of their time acquiring and cleaning data. This is
precipitating what I refer to as the “data crisis”. This is an analogy
with software. The “software crisis” was the phenomenon of inability to
deliver software solutions due to increasing complexity of
implementation. There was no single shot solution for the software
crisis, it involved better practice (scrum, test orientated development,
sprints, code review), improved programming paradigms (object
orientated, functional) and better tools (CVS, then SVN, then git).}

\notes{Data is the new software, and the data crisis is already upon us. It is
driven by the cost of cleaning data, the paucity of tools for monitoring
and maintaining our deployments, the provenance of our models (e.g. with
respect to the data they’re trained on).}

\notes{Three principal changes need to occur in response. They are cultural and
infrastructural.}

\notes{First of all, to excel in data driven decision making we need to view
ourselves as a *data first* company, rather than a *software first*
company. That means refocusing on data as the product. Software is the
intermediary to producing the data, and its quality standards must be
maintained, but not at the expense of the data we are producing. Data
cleaning and maintenance need to be prized as highly as software
debugging and maintenance. Instead of *software* as a service, we should
refocus around *data* as a service. This first change is a cultural
change in which our teams think about their outputs. Instead of
decomposing our systems around the software components, we need to
decompose them around the data generating and consuming components.[^2]

[^2]: This is related to machine learning and technical debt, although
    we are framing the solution here rather than the problem.
}

\notes{Secondly, we need to improve our language around data quality. We cannot
assess the costs of improving data quality unless we generate a language
around what data quality means. Data Readiness Levels are an assessment
of data quality that is based on the usage to which data is put.}

\notes{Thirdly, we need to improve our mental model of the separation of data
science from applied science. A common trap in our thinking around data
is to see data science (and data engineering, data preparation) as a
sub-set of the software engineer’s or applied scientist’s skill set. As
a result we recruit and deploy the wrong type of resource. Data
preparation and question formulation is superficially similar to both
because of the need for programming skills, but the day to day problems
faced are very different.}

\notes{**Recommendations** Build a shared understanding of the language of data
readiness levels (see Appendix A) for use in OP1 documents and costing
of data cleaning and the benefits of reusing cleaned data.

\subsection{Combining Data and Systems Design}

\notes{One analogy I find helpful for understanding the depth of change we need
is the following. Imagine as an engineer, you find a USB stick on the
ground. And for some reason you *know* that on that USB stick is a
particular API call that will enable you to make a significant positive
difference on an Amazon business problem. However, you also know on that
USB stick there is potentially malicious code. The most secure thing to
do would be to *not* introduce this code into your production system.
But what if your manager told you to do so, how would you go about
incorporating this code base?}

\notes{The answer is *very* carefully. You would have to engage in a process
more akin to debugging than regular software engineering. As you
understood the code base, for your work to be reproducible, you should
be documenting it, not just what you discovered, but how you discovered
it. In the end, you typically find a single API call that is the one
that most benefits your system. But more thought has been placed into
this line of code than any line of code you have written before.}

\notes{Even then, when your API code is introduced into your production system,
it needs to be deployed in an environment that monitors it. We cannot
rely on an individual’s decision making to ensure the quality of all our
systems. We need to create an environment that includes quality
controls, checks and bounds, tests, all designed to ensure that
assumptions made about this foreign code base are remaining valid.}

\notes{This situation is akin to what we are doing when we incorporate data in
our production systems. When we are consuming data from others, we
cannot assume that it has been produced in alignment with our goals for
our own systems. Worst case, it may have been adversarialy produced. A
further challenge is that data is dynamic. So, in effect, the code on
the USB stick is evolving over time.}

\notes{Anecdotally, resolving a machine learning challenge requires 80% of the
resource to be focused on the data and perhaps 20% to be focused on the
model. But across Amazon our ratio of data scientists to applied
scientists is the other way around.}

\notes{This challenge came up during IPB MBR (three times more data scientist
time required than expected). Was called out in the three year vision
for S&OP "We need to close the gap to automation through faster ability
to build, test and deploy standard models that work for all regions ..."}

\notes{**Recommendation** We need to share best practice around data deployment
across our teams. We should make best use of our processes where
applicable, but we need to develop them to become a *data first*
organization. Data needs to be cleaned at *output* not at *input*.

\subsection{Deployment}

\notes{Once the design is complete, the model code needs to be deployed.}

\notes{To extend our USB stick analogy further, how would we deploy that code
if we thought it was likely to evolve in production? This is what data
does. We cannot assume that the conditions under which we trained our
model will be retained as we move forward, indeed the only constant we
have is change.}

\notes{This means that when any data dependent model is deployed into
production, it requires *continuous monitoring* to ensure the
assumptions of design have not been invalidated. Software changes are
qualified through testing, in particular a regression test ensures that
existing functionality is not broken by change. Since data is
continually evolving, machine learning systems require continual
regression testing: oversight by systems that ensure their existing
functionality has not been broken as the world evolves around them.
Unfortunately, neither in Amazon, nor across the wider world of
software, have standards around ML model deployment yet been developed.
The modern world of continuous deployment does rely on testing, but it
does not recognize the continuous evolution of the world around us.}

\notes{There is a parallel here between machine learning models and the
computational models we use for our simulations. If the world has
changed around our decision making ecosystem, how are we alerted to
those changes?}

\notes{**Recommendation**: We establish best practice around model deployment.
We need to shift our culture from standing up a software service, to
standing up a *data service*. Data as a Service would involve continual
monitoring of our deployed models in production. This would be regulated
by 'hypervisor' systems[^3] that understand the context in which models
are deployed and recognize when circumstance has changed and models need
retraining or restructuring.

[^3]: Emulation is one approach to forming such a hypervisor, because we
    can build emulators that operate at the meta level, not on the
    systems directly, but how they interact. Or emulators that monitor a
    simulation to ensure performance does not change dramatically.
    However, they are not the only approach. Using real time dashboards,
    anomaly detection and classical statistics are also applicable in
    this domain.
}

\notes{**Recommendation**: We should consider a major re-architecting of the
systems around our services. In particular we should scope the use of a
*streaming architecture* (such as Apache Kafka) that ensures data
persistence and enables asynchronous operation of our systems.[^4] This
would enable the provision of QC streams, and real time dash boards as
well as hypervisors.

[^4]: This is the objective of the MLZero project that Cambridge has
    been exploring. We have a reference architecture, and are also
    considering how such a system could/should be extended for
    incorporation of simulation models.}

\subsection{Outlook for Machine Learning}

\notes{Machine learning has risen to prominence in Amazon as an approach to
*scaling* our activities. SCOT/IPC is probably the world’s largest
*automated decision making* system. For Amazon to continue to scale in
the manner we have over the last two decades, we need to make more use
of computer-based automation. Machine learning is allowing us to
automate processes that were out of reach before.}

\subsection{Conclusion}

\notes{Amazon operates in a technologically evolving environment. In operations
we are fighting daily battles to reach the highest standards for our
customers. SCOT/IPC is the key decision making body for our
organization, our intelligence and strategic command. However,
technology drove changes in battlefield strategy. From the stalemate of
the first world war to the tank-dominated Blitzkrieg of the second, to
the asymmetric warfare of the present. Our technology, tactics and
strategies are also constantly evolving. Machine learning is part of
that evolution solution, but the main challenge is not to become so
fixated on the tactics of today that we miss the evolution of strategy
that the technology is suggesting.}






