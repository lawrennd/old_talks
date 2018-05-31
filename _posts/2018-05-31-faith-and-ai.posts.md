---
bibliography:
- '../other.bib'
- '../lawrence.bib'
- '../zbooks.bib'
csl: '../elsevier-harvard.csl'
date: '2018-05-31'
layout: talk
published: '2018-05-31'
reveal: '2018-05-31-faith-and-ai.slides.html'
---

## What is Machine Learning?

What is machine learning? At its most basic level machine learning is a
combination of

$$ \text{data} + \text{model} \xrightarrow{\text{compute}} \text{prediction}$$

where *data* is our observations. They can be actively or passively
acquired (meta-data). The *model* contains our assumptions, based on
previous experience. THat experience can be other data, it can come from
transfer learning, or it can merely be our beliefs about the
regularities of the universe. In humans our models include our inductive
biases. The *prediction* is an action to be taken or a categorization or
a quality score. The reason that machine learning has become a mainstay
of artificial intelligence is the importance of predictions in
artificial intelligence. The data and the model are combined through
computation.

In practice we normally perform machine learning using two functions. To
combine data with a model we typically make use of:

**a prediction function** a function which is used to make the
predictions. It includes our beliefs about the regularities of the
universe, our assumptions about how the world works, e.g. smoothness,
spatial similarities, temporal similarities.

**an objective function** a function which defines the cost of
misprediction. Typically it includes knowledge about the world’s
generating processes (probabilistic objectives) or the costs we pay for
mispredictions (empiricial risk minimization).

The combination of data and model through the prediction function and
the objectie function leads to a *learning algorithm*. The class of
prediction functions and objective functions we can make use of is
restricted by the algorithms they lead to. If the prediction function or
the objective function are too complex, then it can be difficult to find
an appropriate learning algorithm. Much of the acdemic field of machine
learning is the quest for new learning algorithms that allow us to bring
different types of models and data together.

A useful reference for state of the art in machine learning is the UK
Royal Society Report, [Machine Learning: Power and Promise of Computers
that Learn by
Example](https://royalsociety.org/~/media/policy/projects/machine-learning/publications/machine-learning-report.pdf).

You can also check my blog post on [“What is Machine
Learning?”](http://inverseprobability.com/2017/07/17/what-is-machine-learning)

### Artificial Intelligence and Data Science

Machine learning technologies have been the driver of two related, but
distinct disciplines. The first is *data science*. Data science is an
emerging field that arises from the fact that we now collect so much
data by happenstance, rather than by *experimental design*. Classical
statistics is the science of drawing conclusions from data, and to do so
statistical experiments are carefully designed. In the modern era we
collect so much data that there’s a desire to draw inferences directly
from the data.

As well as machine learning, the field of data science draws from
statistics, cloud computing, data storage (e.g. streaming data),
visualization and data mining.

In contrast, artificial intelligence technologies typically focus on
emulating some form of human behaviour, such as understanding an image,
or some speech, or translating text from one form to another. The recent
advances in artifcial intelligence have come from machine learning
providing the automation. But in contrast to data science, in artifcial
intelligence the data is normally collected with the specific task in
mind. In this sense it has strong relations to classical statistics.

Classically artificial intelligence worried more about *logic* and
*planning* and focussed less on data driven decision making. Modern
machine learning owes more to the field of *Cybernetics*
[@Wiener:cybernetics48] than artificial intelligence. Related fields
include *robotics*, *speech recognition*, *language understanding* and
*computer vision*.

There are strong overlaps between the fields, the wide availability of
data by happenstance makes it easier to collect data for designing AI
systems. These relations are coming through wide availability of sensing
technologies that are interconnected by celluar networks, WiFi and the
internet. This phenomenon is sometimes known as the *Internet of
Things*, but this feels like a dangerous misnomer. We must never forget
that we are interconnecting people, not things.

### What does Machine Learning do?

Any process of automation allows us to scale what we do by codifying a
process in some way that makes it efficient and repeatable. Machine
learning automates by emulating human (or other actions) found in data.
Machine learning codifies in the form of a mathematical function that is
learnt by a computer. If we can create these mathematical functions in
ways in which they can interconnect, then we can also build systems.

Machine learning works through codifing a prediction of interest into a
mathematical function. For example, we can try and predict the
probability that a customer wants to by a jersey given knowledge of
their age, and the latitude where they live. The technique known as
logistic regression estimates the odds that someone will by a jumper as
a linear weighted sum of the features of interest.

$$ \text{odds} = \frac{p(\text{bought})}{p(\text{not bought})} $$
$$ \log \text{odds}  = \beta_0 + \beta_1 \text{age} + \beta_2 \text{latitude}$$

Here $\beta_0$, $\beta_1$ and $\beta_2$ are the parameters of the model.
If $\beta_1$ and $\beta_2$ are both positive, then the log-odds that
someone will buy a jumper increase with increasing latitude and age, so
the further north you are and the older you are the more likely you are
to buy a jumper. The parameter $\beta_0$ is an offset parameter, and
gives the log-odds of buying a jumper at zero age and on the equator. It
is likely to be negative\[\^logarithms\] indicating that the purchase is
odds-against. This is actually a classical statistical model, and models
like logistic regression are widely used to estimate probabilities from
ad-click prediction to risk of disease.

This is called a generalized linear model, we can also think of it as
estimating the *probability* of a purchase as a nonlinear function of
the features (age, lattitude) and the parameters (the $\beta$ values).
The function is known as the *sigmoid* or [logistic
function](https://en.wikipedia.org/wiki/Logistic_regression), thus the
name *logistic* regression.

$$ p(\text{bought}) =  {\sigma\left(\beta_0 + \beta_1 \text{age} + \beta_2 \text{latitude}\right)}$$

In the case where we have *features* to help us predict, we sometimes
denote such features as a vector, ${{\bf {x}}}$, and we then use an
inner product between the features and the parameters,
$\boldsymbol{\beta}^\top {{\bf {x}}}= \beta_1 {x}_1 + \beta_2 {x}_2 + \beta_3 {x}_3 ...$,
to represent the argument of the sigmoid.

$$ p(\text{bought}) =  {\sigma\left(\boldsymbol{\beta}^\top {{\bf {x}}}\right)}$$

More generally, we aim to predict some aspect of our data, ${y}$, by
relating it through a mathematical function, ${f}(\cdot)$, to the
parameters, $\boldsymbol{\beta}$ and the data, ${{\bf {x}}}$.

$$ {y}=  {f}\left({{\bf {x}}}, \boldsymbol{\beta}\right)$$

We call ${f}(\cdot)$ the *prediction function*

To obtain the fit to data, we use a separate function called the
*objective function* that gives us a mathematical representation of the
difference between our predictions and the real data.

$${E}(\boldsymbol{\beta}, {\mathbf{Y}}, {{\bf X}})$$ A commonly used
examples (for example in a regression problem) is least squares,
$${E}(\boldsymbol{\beta}, {\mathbf{Y}}, {{\bf X}}) = \sum_{i=1}^{n}\left({y}_i - {f}({{\bf {x}}}_i, \boldsymbol{\beta})\right)^2.$$

If a linear prediction funciton is combined with the least squares
objective function then that gives us a classical *linear regression*,
another classical statistical model. Statistics often focusses on linear
models because it makes interpretation of the model easier.
Interpretation is key in statistics because the aim is normally to
validate questions by analysis of data. Machine learning has typically
focussed more on the prediction function itself and worried less about
the interpretation of parameters, which are normally denoted by
$\mathbf{w}$ instead of $\boldsymbol{\beta}$. As a result *non-linear*
functions are explored more often as they tend to improve quality of
predictions but at the expense of interpretability.

### 

<small>Outline of the DeepFace architecture. A front-end of a single
convolution-pooling-convolution filtering on the rectified input,
followed by three locally-connected layers and two fully-connected
layers. Color illustrates feature maps produced at each layer. The net
includes more than 120 million parameters, where more than 95% come from
the local and fully connected.</small>

<img class="" src="../slides/diagrams/deepface_neg.png" width="100%" align="" style="background:none; border:none; box-shadow:none;">

<p align="right">
<small>Source: DeepFace</small>
</p>
### 

<img class="" src="../slides/diagrams/576px-Early_Pinball.jpg" width="50%" align="" style="background:none; border:none; box-shadow:none;">

We can think of what these models are doing as being similar to early
pin ball machines. In a neural network, we input a number (or numbers),
whereas in pinball, we input a ball. The location of the ball on the
left-right axis can be thought of as the number. As the ball falls
through the machine, each layer of pins can be thought of as a different
layer of neurons. Each layer acts to move the ball from left to right.

In a pinball machine, when the ball gets to the bottom it might fall
into a hole defining a score, in a neural network, that is equivalent to
the decision: a classification of the input object.

An image has more than one number associated with it, so it’s like
playing pinball in a *hyper-space*.

At initialization, the pins aren’t in the right place to bring the ball
to the correct decision.

Learning involves moving all the pins to be in the right position, so
that the ball falls in the right place. But moving all these pins in
hyperspace can be difficult. In a hyper space you have to put a lot of
data through the machine for to explore the positions of all the pins.
Adversarial learning reflects the fact that a ball can be moved a small
distance and lead to a very different result.

Probabilistic methods explore more of the space by considering a range
of possible paths for the ball through the machine.

## Artificial vs Natural Systems

### Natural Systems are Evolved

> Survival of the fittest
>
> [Herbet Spencer](https://en.wikipedia.org/wiki/Herbert_Spencer), 1864

Darwin never said “Survival of the Fittest” he talked about evolution by
natural selection.

Evolution is better described as “non-survival of the non-fit”. You
don’t have to be the fittest to survive, you just need to avoid the
pitfalls of life. This is the first priority.

A mistake we make in our systems design is to equate fitness with the
objective function, and to assume it is known and static. In practice, a
real environment would have an evolving fitness function which would be
unknown at any given time.

## Machine Learning System Design

The way we are deploying artificial intelligence systems in practice is
to build up systems of machine learning components. To build a machine
learning system, we decompose the task into parts, each of which we can
emulate with ML methods. These parts are typically independently
constructed and verified. For example, in a driverless car we can
decompose the tasks into components such as “pedestrian detection” and
“road line detection”. Each of these components can be constructed with,
for example, an independent classifier. We can then superimpose a logic
on top. For example, “Follow the road line unless you detect a
pedestrian in the road”.

This allows for verification of car performance, as long as we can
verify the individual components. However, it also implies that the AI
systems we deploy are *fragile*.

Our intelligent systems are composed by “pigeonholing” each indvidual
task, then substituting with a machine learning model.

### Rapid Reimplementation

This is also the classical approach to automation, but in traditional
automation we also ensure the *environment* in which the system operates
becomes controlled. For example, trains run on railway lines, fast cars
run on motorways, goods are manufactured in a controlled factory
environment.

The difference with modern automated decision making systems is our
intention is to deploy them in the *uncontrolled* environment that makes
up our own world.

This exposes us to either unforseen circumstances or adversarial action.
And yet it is unclear our our intelligent systems are capable of
adapting to this.

We become exposed to mischief and adversaries. Adversaries intentially
may wish to take over the artificial intelligence system, and mischief
is the constant practice of many in our society. Simply watching a 10
year old interact with a voice agent such as Alexa or Siri shows that
they are delighted when the can make the the “intelligent” agent seem
foolish.

<img class="rotateimg90" src="../slides/diagrams/2017-10-12 16.47.34.jpg" width="40%" align="center" style="background:none; border:none; box-shadow:none;">
<center>
*Watt’s Governor as held by “Science” on Holborn Viaduct*
</center>
<img class="center" src="../slides/diagrams/SteamEngine_Boulton&Watt_1784_neg.png" width="50%" align="" style="background:none; border:none; box-shadow:none;">
<center>
*Watt’s Steam Engine which made Steam Power Efficient and Practical*
</center>
One of the first automated decision making systems was Watt’s governor,
as held by “Science” on Holborns viaduct. Watt’s governor was a key
component in his steam engine. It senses increases in speed in the
engine and closed the steam valve to prevent the engine overspeeding and
destroying itself. Until the invention of this device, it was a human
job to do this.

The formal study of governors and other feedback control devices was
then began by [James Clerk
Maxwell](https://en.wikipedia.org/wiki/James_Clerk_Maxwell), the
Scottish physicist. This field became the foundation of our modern
techniques of artificial intelligence through Norbert Wiener’s book
*Cybernetics* [@Wiener:cybernetics48]. Cybernetics is Greek for
governor, a word that in itself simply means helmsman in English.

The recent WannaCry virus that had a wide impact on our health services
ecosystem was exploiting a security flaw in Windows systems that was
first exploited by a virus called Stuxnet.

Stuxnet was a virus designed to infect the Iranian nuclear program’s
Uranium enrichment centrifuges. A centrifuge is prevented from overspeed
by a controller, just like Watt’s governor. Only now it is implemented
in control logic, in this case on a Siemens PLC controller.

Stuxnet infected these controllers and took over the response signal in
the centrifuge, fooling the system into thinking that no overspeed was
occuring. As a result, the centrifuges destroyed themselves through
spinning too fast.

This is equivalent to detaching Watt’s governor from the steam engine.
Such sabotage would be easily recognized by a steam engine operator. The
challenge for the operators of the Iranian Uranium centrifuges was that
the sabotage was occurring inside the electronics.

That is the effect of an adversary on an intelligent system, but even
without adveraries, the mischief of a 10 year old can confuse our AIs.

[![](https://img.youtube.com/vi/1y2UKz47gew/0.jpg)](https://www.youtube.com/watch?v=1y2UKz47gew&t=)

Asking Siri “What is a trillion to the power of a thousand minus one?”
leads to a 30 minute response consisting of only 9s. I found this out
because my nine year old grabbed my phone and did it. The only way to
stop Siri was to force closure. This is an interesting example of a
system feature that’s *not* a bug, in fact it requires clever processing
from Wolfram Alpha. But it’s an unexpected result from the system
performing correctly.

This challenge of facing a circumstance that was unenvisaged in design
but has consequences in deployment becomes far larger when the
environment is uncontrolled. Or in the extreme case, where actions of
the intelligent system effect the wider environment and change it.

These unforseen circumstances are likely to lead to need for much more
efficient turn-around and update for our intelligent systems. Whether we
are correcting for security flaws (which *are* bugs) or unenvisaged
circumstantial challenges: an issue I’m referring to as *peppercorns*.
Rapid deployment of system updates is required. For example, Apple have
“fixed” the problem of Siri returning long numbers.

The challenge is particularly acute because of the *scale* at which we
can deploy AI solutions. This means when something does go wrong, it may
be going wrong in billions of households simultaneously.

See also [this blog on the differences between natural and artificial
intelligence](http://inverseprobability.com/2018/02/06/natural-and-artificial-intelligence)
and this paper [on the need for diversity in decision
making](http://inverseprobability.com/2017/11/15/decision-making).

## Natural and Artificial Intelligence: Embodiment Factors

<table>
<tr>
<td>
</td>
<td align="center">
<img class="" src="../slides/diagrams/IBM_Blue_Gene_P_supercomputer.jpg" width="40%" align="center" style="background:none; border:none; box-shadow:none;">
</td>
<td align="center">
<img class="" src="../slides/diagrams/ClaudeShannon_MFO3807.jpg" width="25%" align="center" style="background:none; border:none; box-shadow:none;">
</td>
</tr>
<tr>
<td>
compute
</td>
<td align="center">
$$\approx 100 \text{ gigaflops}$$
</td>
<td align="center">
$$\approx 16 \text{ petaflops}$$
</td>
</tr>
<tr>
<td>
communicate
</td>
<td align="center">
$$1 \text{ gigbit/s}$$
</td>
<td align="center">
$$100 \text{ bit/s}$$
</td>
</tr>
<tr>
<td>
(compute/communicate)
</td>
<td align="center">
$$10^{4}$$
</td>
<td align="center">
$$10^{14}$$
</td>
</tr>
</table>
There is a fundamental limit placed on our intelligence based on our
ability to communicate. Claude Shannon founded the field of information
theory. The clever part of this theory is it allows us to separate our
measurement of information from what the information pertains to[^1].

Shannon measured information in bits. One bit of information is the
amount of information I pass to you when I give you the result of a coin
toss. Shannon was also interested in the amount of information in the
English language. He estimated that on average a word in the English
language contains 12 bits of information.

Given typical speaking rates, that gives us an estimate of our ability
to communicate of around 100 bits per second [@Reed-information98].
Computers on the other hand can communicate much more rapidly. Current
wired network speeds are around a billion bits per second, ten million
times faster.

When it comes to compute though, our best estimates indicate our
computers are slower. A typical modern computer can process make around
100 billion floating point operations per second, each floating point
operation involves a 64 bit number. So the computer is processing around
6,400 billion bits per second.

It’s difficult to get similar estimates for humans, but by some
estimates the amount of compute we would require to *simulate* a human
brain is equivalent to that in the UK’s fastest computer
[@Ananthanarayanan-cat09], the MET office machine in Exeter, which in
2018 ranks as the 11th fastest computer in the world. That machine
simulates the world’s weather each morning, and then simulates the
world’s climate. It is a 16 petaflop machine, processing around 1,000
*trillion* bits per second.

So when it comes to our ability to compute we are extraordinary, not
compute in our conscious mind, but the underlying neuron firings that
underpin both our consciousness, our sbuconsciousness as well as our
motor control etc. By analogy I sometimes like to think of us as a
Formula One engine. But in terms of our ability to deploy that
computation in actual use, to share the results of what we have
inferred, we are very limited. So when you imagine the F1 car that
represents a psyche, think of an F1 car with bicycle wheels.

<img class="" src="../slides/diagrams/640px-Marcel_Renault_1903.jpg" width="70%" align="center" style="background:none; border:none; box-shadow:none;">

In contrast, our computers have less computational power, but they can
communicate far more fluidly. They are more like a go-kart, less well
powered, but with tires that allow them to deploy that power.

<img class="" src="../slides/diagrams/Caleb_McDuff_WIX_Silence_Racing_livery.jpg" width="70%" align="center" style="background:none; border:none; box-shadow:none;">

For humans, that means much of our computation should be dedicated to
considering *what* we should compute. To do that efficiently we need to
model the world around us. The most complex thing in the world around us
is other humans. So it is no surprise that we model them. We second
guess what their intentions are, and our communication is only necessary
when they are departing from how we model them. Naturally, for this to
work well, we need to understand those we work closely with. So it is no
surprise that social communication, social bonding, forms so much of a
part of our use of our limited bandwidth.

There is a second effect here, our need to anthropomorphise objects
around us. Our tendency to model our fellow humans extends to when we
interact with other entities in our environment. To our pets as well as
inanimate objects around us, such as computers or even our cars. This
tendency to overinterpret could be a consequence of our limited ability
to communicate.

For more details see this paper [“Living Together: Mind and Machine
Intelligence”](https://arxiv.org/abs/1705.07996), and this [TEDx
talk](http://inverseprobability.com/talks/lawrence-tedx17/living-together.html).

## Evolved Relationship with Information

<object class="svgplot" align data="../slides/diagrams/data-science/information-flow003.svg">
</object>
The high bandwidth of computers has resulted in a close relationship
between the computer and data. Large amounts of information can flow
between the two. The degree to which the computer is mediating our
relationship with data means that we should consider it an intermediary.

Origininally our low bandwith relationship with data was affected by two
characteristics. Firstly, our tendency to over-interpret driven by our
need to extract as much knowledge from our low bandwidth information
channel as possible. Secondly, by our improved understanding of the
domain of *mathematical* statistics and how our cognitive biases can
mislead us.

With this new set up there is a potential for assimilating far more
information via the computer, but the computer can present this to us in
various ways. If it’s motives are not aligned with ours then it can
misrepresent the information. This needn’t be nefarious it can be simply
as a result of the computer pursuing a different objective from us. For
example, if the computer is aiming to maximize our interaction time that
may be a different objective from ours which may be to summarize
information in a representative manner in the *shortest* possible length
of time.

For example, for me it was a common experience to pick up my telephone
with the intention of checking when my next appointment was, but to soon
find myself distracted by another application on the phone, and end up
reading something on the internet. By the time I’d finished reading, I
would often have forgotten the reason I picked up my phone in the first
place.

We can benefit enormously from the very large amount of information we
can now obtain through this evolved relationship between us and data.
Biology has already benefited from large scale data sharing and the
improved inferences that can be drawn through summarizing data by
computer. That has underpinned the revolution in computational biology.
But in our daily lives this phenomenon is affecting us in ways which we
haven’t envisaged.

Better mediation of this flow actually requires a better understanding
of human-computer interaction. This in turn involves understanding our
own intelligence better, what its cognitive biases are and how these
might mislead us.

For further thoughts see [this Guardian
article](https://www.theguardian.com/media-network/2015/jul/23/data-driven-economy-marketing)
on marketing in the internet era and [this blog
post](http://inverseprobability.com/2015/12/04/what-kind-of-ai) on
System Zero.

### Societal Effects

We have already seen the effects of this changed dynamic in biology and
computational biology. Improved sensorics have led to the new domains of
transcriptomics, epigenomics, and ‘rich phenomics’ as well as
considerably augmenting our capabilities in genomics.

Biologists have had to become data-savvy, they require a rich
understanding of the available data resources and need to assimilate
existing data sets in their hypothesis generation as well as their
experimental design. Modern biology has become a far more quantitative
science, but the quantitativeness has required new methods developed in
the domains of *computational biology* and *bioinformatics*.

There is also great promise for personalized health, but in health the
wide data-sharing that has underpinned success in the computational
biology community is much harder to cary out.

We can expect to see these phenomena reflected in wider society.
Particularly as we make use of more automated decision making based only
on data.

The main phenomenon we see across the board is the shift in dynamic from
the direct pathway between human and data, as traditionally mediated by
classical statistcs, to a new flow of information via the computer. This
change of dynamics gives us the modern and emerging domain of *data
science*.

## Human Communication

For human conversation to work, we require an internal model of who we
are speaking to. We model each other, and combine our sense of who they
are, who they think we are, and what has been said. This is our approach
to dealing with the limited bandwidth connection we have. Empathy and
understanding of intent. Mental dispositional concepts are used to
augment our limited communication bandwidth.

Fritz Heider referred to the important point of a conversation as being
that they are happenings that are “*psychologically represented* in each
of the participants” (his emphasis) [@Heider:interpersonal58]

### Machine Learning and Narratives

<img class="" src="../slides/diagrams/Classic_baby_shoes.jpg" width="60%" align="center" style="background:none; border:none; box-shadow:none;">

<center>
*For sale: baby shoes, never worn.*
</center>
Consider the six word novel, apocraphally credited to Ernest Hemingway,
“For sale: baby shoes, never worn”. To understand what that means to a
human, you need a great deal of additional context. Context that is not
directly accessible to a machine that has not got both the evolved and
contextual understanding of our own condition to realize both the
implication of the advert and what that implication means emotionally to
the previous owner.

[![](https://img.youtube.com/vi/8FIEZXMUM2I/0.jpg)](https://www.youtube.com/watch?v=8FIEZXMUM2I&t=7)

[Fritz Heider](https://en.wikipedia.org/wiki/Fritz_Heider) and [Marianne
Simmel](https://en.wikipedia.org/wiki/Marianne_Simmel)’s experiments
with animated shapes from 1944 [@Heider:experimental44]. Our
interpretation of these objects as showing motives and even emotion is a
combination of our desire for narrative, a need for understanding of
each other, and our ability to empathise. At one level, these are
crudely drawn objects, but in another key way, the animator has
communicated a story through simple facets such as their relative
motions, their sizes and their actions. We apply our psychological
representations to these faceless shapes in an effort to interpret their
actions.

Lies and Damned Lies

> There are three types of lies: lies, damned lies and statistics
>
> Benjamin Disraeli 1804-1881

The quote lies, damned lies and statistics was credited to Benjamin
Disraeli by Mark Twain in his autobiography. It characterizes the idea
that statistic can be made to prove anything. But Disraeli died in 1881
and Mark Twain died in 1910. The important breakthrough in overcoming
our tendency to overinterpet data came with the formalization of the
field through the development of *mathematical statistics*.

### *Mathematical* Statistics

<img class="" src="../slides/diagrams/Portrait_of_Karl_Pearson.jpg" width="30%" align="center" style="background:none; border:none; box-shadow:none;">

[Karl Pearson](https://en.wikipedia.org/wiki/Karl_Pearson) (1857-1936),
[Ronald Fisher](https://en.wikipedia.org/wiki/Ronald_Fisher) (1890-1962)
and others considered the question of what conclusions can truly be
drawn from data. Their mathematical studies act as a restraint on our
tendency to over-interpret and see patterns where there are none. They
introduced concepts such as randomized control trials that form a
mainstay of the our decision making today, from government, to
clinicians to large scale A/B testing that determines the nature of the
web interfaces we interact with on social media and shopping.

Today the statement “There are three types of lies: lies, damned lies
and ‘big data’” may be more apt. We are revisiting many of the mistakes
made in interpreting data from the 19th century. Big data is laid down
by happenstance, rather than actively collected with a particular
question in mind. That means it needs to be treated with care when
conclusions are being drawn. For data science to succede it needs the
same form of rigour that Pearson and Fisher brought to statistics, a
“mathematical data science” is needed.

### Challenges in Data Science

### Faith and AI

1.  Artificial Intelligence as Cartoon Religion
2.  Artificial Intelligence and Introspection
3.  A Systemic Catch 22

### AI as Cartoon Religion

The first parallels one can find between artificial intelligence and
religion come in somewhat of a cartoon doomsday scenario form. The
publically hyped fears of superintelligence and singularity can equally
be placed within the framework of the simpler questions that religion
can try to answer. The parallels are

1.  Superintelligence as god
2.  Demi-god status achievable through trans-humanism
3.  Immortality through uploading the connectome
4.  The day of judgement as the “singularity”

The notion of a ultra-intelligence is similar to the notion of an
interventionist god, with omniscience both in the present and in the
future. This notion was described by Pierre Simon Laplace.

<img class="" src="../slides/diagrams/ml/Pierre-Simon_Laplace.png" width="30%" align="center" style="background:none; border:none; box-shadow:none;">

<img class="" src="../slides/diagrams/laplacesDeterminismFrench.png" width="80%" align="center" style="background:none; border:none; box-shadow:none;">}

Famously, Laplace considered the idea of a deterministic Universe, one
in which all the “”. He speculates on an “intelligence” that can submit
this vast data to analysis and propsoses that such an entity would be
able to predict the future.

> Given for one instant an intelligence which could comprehend all the
> forces by which nature is animated and the respective situation of the
> beings who compose it—an intelligence sufficiently vast to submit
> these data to analysis—it would embrace in the same formulate the
> movements of the greatest bodies of the universe and those of the
> lightest atom; for it, nothing would be uncertain and the future, as
> the past, would be present in its eyes.

Unfortunately, most analyses of his ideas stop at that point, whereas
his real point is that such a notion is somewhat ridiculous. Just three
pages later in the “Philosophical Essay on Probabilities”
[@Laplace:essai14], Laplace goes on to observe:

> The curve described by a simple molecule of air or vapor is regulated
> in a manner just as certain as the planetary orbits; the only
> difference between them is that which comes from our ignorance.
>
> Probability is relative, in part to this ignorance, in part to our
> knowledge.

In other words, we can never utilize the idealistic deterministc
Universe due to our ignorance about the world.

### Thanks!

-   twitter: @lawrennd
-   blog:
    [http://inverseprobability.com](http://inverseprobability.com/blog.html)

[^1]: the challenge of understanding what information pertains to is
    known as knowledge representation.
