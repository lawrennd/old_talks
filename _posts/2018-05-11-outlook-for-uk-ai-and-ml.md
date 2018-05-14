---
title: "Outlook for AI and Machine Learning"
abstract: With the recent BEIS Industrial Strategy and the UK Sector deal the UK is turning its attention to how the next generation of artificial intelligence can drive efficiency and innovation in the UK economy. In this talk we review the outlook. 
reveal: 2018-05-11-outlook-for-uk-ai-and-ml.slides.html
published: 2018-05-11
venue: HM Revenue and Customs
layout: talk
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: Amazon Cambridge and University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
published: 2018-05-11
---

$$\newcommand{\numData}{n}
\newcommand{\errorFunction}{E}
\newcommand{\mappingFunction}{f}
\newcommand{\sigmoid}[1]{\sigma\left(#1\right)}
\newcommand{\inputScalar}{x}
\newcommand{\inputVector}{\mathbf{x}}
\newcommand{\inputMatrix}{\mathbf{X}}
\newcommand{\dataScalar}{y}
\newcommand{\dataVector}{\mathbf{y}}
\newcommand{\dataMatrix}{\mathbf{Y}}$$

The aim of this presentation is give a sense of the current situation in machine learning and artificial intelligence as well as some perspective on the immediate outlook for the field.

## The Gartner Hype Cycle

<img class="negate" src="http://inverseprobability.com/talks/slides/diagrams/Gartner_Hype_Cycle.png" width="70%" align="center" style="background:none; border:none; box-shadow:none;">

The [Gartner Hype Cycle](https://en.wikipedia.org/wiki/Hype_cycle) tries to assess where an idea is in terms of maturity and adoption. It splits the evolution of technology into a technological trigger, a peak of expectations followed by a trough of disillusionment and a final ascension into a useful technology. It looks rather like a classical control response to a final set point.

<object class="svgplot" align="" data="http://inverseprobability.com/talks/slides/diagrams/data-science/bd-ds-iot-ml-google-trends003.svg"></object>
<center><i>Google Trends data for different search terms in an attempt to assess their position on the "hype cycle"</i></center>

Google trends gives us insight into how far along various technological terms are on the hype cycle.

## What is Machine Learning?

What is machine learning? At its most basic level machine learning is a combination of

$$ \text{data} + \text{model} \xrightarrow{\text{compute}} \text{prediction}$$

where *data* is our observations. They can be actively or passively
acquired (meta-data). The *model* contains our assumptions, based on
previous experience. THat experience can be other data, it can come
from transfer learning, or it can merely be our beliefs about the
regularities of the universe. In humans our models include our
inductive biases. The *prediction* is an action to be taken or a
categorization or a quality score. The reason that machine learning
has become a mainstay of artificial intelligence is the importance of
predictions in artificial intelligence. The data and the model are combined through computation.

In practice we normally perform machine learning using two functions. To combine data with a model we typically make use of:

**a prediction function** a function which is used to make the predictions. It includes our beliefs about the regularities of the universe, our assumptions about how the world works, e.g. smoothness, spatial similarities, temporal similarities.

**an objective function** a function which defines the cost of misprediction. Typically it includes knowledge about the world's generating processes (probabilistic objectives) or the costs we pay for mispredictions (empiricial risk minimization).

The combination of data and model through the prediction function and the objectie function leads to a *learning algorithm*. The class of prediction functions and objective functions we can make use of is restricted by the algorithms they lead to. If the prediction function or the objective function are too complex, then it can be difficult to find an appropriate learning algorithm. Much of the acdemic field of machine learning is the quest for new learning algorithms that allow us to bring different types of models and data together.

A useful reference for state of the art in machine learning is the UK Royal Society Report, [Machine Learning: Power and Promise of Computers that Learn by Example](https://royalsociety.org/~/media/policy/projects/machine-learning/publications/machine-learning-report.pdf).

You can also check my blog post on ["What is Machine Learning?"](http://inverseprobability.com/2017/07/17/what-is-machine-learning)

## Natural and Artificial Intelligence: Embodiment Factors

<table>
 <tr>
  <td></td>
  <td align="center"><img class="" src="http://inverseprobability.com/talks/slides/diagrams/IBM_Blue_Gene_P_supercomputer.jpg" width="40%" align="center" style="background:none; border:none; box-shadow:none;"></td>
  <td align="center"><img class="" src="http://inverseprobability.com/talks/slides/diagrams/ClaudeShannon_MFO3807.jpg" width="25%" align="center" style="background:none; border:none; box-shadow:none;"></td>
 </tr>
 <tr>
  <td>compute</td>
  <td align="center">$$\approx 10 \text{ gigaflops}$$</td><td align="center">$$\approx 14 \text{ teraflops}$$</td>
 </tr>
 <tr>
  <td>communicate</td>
  <td align="center">$$\approx 1 \text{ gigbit/s}$$</td>
  <td align="center">$$\approx 100 \text{ bit/s}$$</td>
 </tr>
 <tr>
  <td>(compute/communicate)</td>
  <td align="center">$$10$$</td>
  <td align="center">$$\approx 10^{13}$$</td>
 </tr>
</table>

There is a fundamental limit placed on our intelligence based on our ability to communicate. Claude Shannon founded the field of information theory. The clever part of this theory is it allows us to separate our measurement of information from what the information pertains to[^knowledge-representation].

[^knowledge-representation]: the challenge of understanding what it pertains to is known as knowledge representation). 

Shannon measured information in bits. One bit of information is the amount of information I pass to you when I give you the result of a coin toss. Shannon was also interested in the amount of information in the English language. He estimated that on average a word in the English language contains 12 bits of information. 

Given typical speaking rates, that gives us an estimate of our ability to communicate of around 100 bits per second. Computers on the other hand can communicate much more rapidly. Current wired network speeds are around a billion bits per second, ten million times faster. 

When it comes to compute though, our best estimates indicate our computers are slower. A typical modern computer can process make around 2 billion floating point operations per second, each floating point operation involves a 64 bit number. So the computer is processing around 120 billion bits per second. 

It's difficult to get similar estimates for humans, but by some estimates the amount of compute we would require to *simulate* a human brain is equivalent to that in the UK's fastest computer, the MET office machine in Exeter, which in 2018 ranks as the 11th fastest computer in the world. That machine simulates the world's weather each morning, and then simulates the world's climate. It is a 16 petaflop machine. 

So when it comes to our ability to compute we are extraordinary, not compute in our conscious mind, but the underlying neuron firings that underpin both our consciousness, our sbuconsciousness as well as our motor control etc. By analogy I sometimes like to think of us as a Formula One engine. But in terms of our ability to deploy that computation in actual use, to share the results of what we have inferred, we are very limited. So when you imagine the F1 car that represents a psyche, think of an F1 car with bicycle wheels.

In contrast, our computers have less computational power, but they can communicate far more fluidly. They are more like a go-kart, less well powered, but with tires that allow them to deploy that power.

For humans, that means much of our computation should be dedicated to considering *what* we should compute. To do that efficiently we need to model the world around us. The most complex thing in the world around us is other humans. So it is no surprise that we model them. We second guess what their intentions are, and our communication is only necessary when they are departing from how we model them. Naturally, for this to work well, we need to understand those we work closely with. So it is no surprise that social communication, social bonding, forms so much of a part of our use of our limited bandwidth. 

There is a second effect here, our need to anthropomorphise objects around us. Our tendency to model our fellow humans extends to when we interact with other entities in our environment. To our pets as well as inanimate objects around us, such as computers or even our cars. This tendency to overinterpret could be a consequence of our limited ability to communicate. 

For more details see this paper ["Living Together: Mind and Machine Intelligence"](https://arxiv.org/abs/1705.07996), and this [TEDx talk](http://inverseprobability.com/talks/lawrence-tedx17/living-together.html).

## Evolved Relationship with Information

<object class="svgplot" align="" data="http://inverseprobability.com/talks/slides/diagrams/data-science/information-flow003.svg"></object>

The high bandwidth of computers has resulted in a close relationship between the computer and data. Larege amounts of information can flow between the two. The degree to which the computer is mediating our relationship with data means that we should consider it an intermediary. 

Origininally our low bandwith relationship with data was affected by two characteristics. Firstly, our tendency to over-interpret driven by our need to extract as much knowledge from our low bandwidth information channel as possible. Secondly, by our improved understanding of the domain of *mathematical* statistics and how our cognitive biases can mislead us. 

With this new set up there is a potential for assimilating far more information via the computer, but the computer can present this to us in various ways. If it's motives are not aligned with ours then it can misrepresent the information. This needn't be nefarious it can be simply as a result of the computer pursuing a different objective from us. For example, if the computer is aiming to maximize our interaction time that may be a different objective from ours which may be to summarize information in a representative manner in the *shortest* possible lenght of time. 

For example, for me it was  a common experience to pick up my telephone with the intention of checking when my next appointme was, but to soon find myself  distracted by another application on the phone, and end up reading something on the internet. By the time I'd finished reading, I would often have forgotten the reason I picked up my phone in the first place. 

We can benefit enormously from the very large amount of information we can now obtain through this evolved relationship between us and data. Biology has already benefited from large scale data sharing and the improved inferences that can be drawn through summarizing data by computer. That has underpinned the revolution in computational biology. But in our daily lives this phenomenon is affecting us in ways which we haven't envisaged.

Better mediation of this flow actually requires a better understanding of human-computer interaction. This in turn involves understanding our own intelligence better, what its cognitive biases are and how these might mislead us.

For further thoughts see [this Guardian article](https://www.theguardian.com/media-network/2015/jul/23/data-driven-economy-marketing) on marketing in the internet era and [this blog post](http://inverseprobability.com/2015/12/04/what-kind-of-ai) on System Zero. 

### Societal Effects

We have already seen the effects of this changed dynamic in biology and computational biology. Improved sensorics have led to the new domains of transcriptomics, epigenomics, and 'rich phenomics' as well as considerably augmenting our capabilities in genomics. 

Biologists have had to become data-savvy, they require a rich understanding of the available data resources and need to assimilate existing data sets in their hypothesis generation as well as their experimental design. Modern biology has become a far more quantitative science, but the quantitativeness has required new methods developed in the domains of *computational biology* and *bioinformatics*.

There is also great promise for personalized health, but in health the wide data-sharing that has underpinned success in the computational biology community is much harder to cary out. 

We can expect to see these phenomena reflected in wider society. Particularly as we make use of more automated decision making based only on data.

The main phenomenon we see across the board is the shift in dynamic from the direct pathway between human and data, as traditionally mediated by classical statistcs, to a new flow of information via the computer. This change of dynamics gives us the modern and emerging domain of *data science*.

## Human Communication

For human conversation to work, we require an internal model of who we are speaking to. We model each other, and combine our sense of who they are, who they think we are, and what has been said. This is our approach to dealing with the limited bandwidth connection we have. Empathy and understanding of intent. Mental dispositional concepts are used to augment our limited communication bandwidth.

Fritz Heider referred to the important point of a conversation as being that they are happenings that are "*psychologically represented* in each of the participants" (his emphasis) [@Heider:interpersonal58]

### Machine Learning and Narratives

<img class="" src="http://inverseprobability.com/talks/slides/diagrams/Classic_baby_shoes.jpg" width="60%" align="" style="background:none; border:none; box-shadow:none;">

<center><i>For sale: baby shoes, never worn.</i></center>

Consider the six word novel, apocraphally credited to Ernest Hemingway, "For sale: baby shoes, never worn". To understand what that means to a human, you need a great deal of additional context. Context that is not directly accessible to a machine that has not got both the evolved and contextual understanding of our own condition to realize both the implication of the advert and what that implication means emotionally to the previous owner.

[![](https://img.youtube.com/vi/8FIEZXMUM2I/0.jpg)](https://www.youtube.com/watch?v=8FIEZXMUM2I&t=7)

[Fritz Heider](https://en.wikipedia.org/wiki/Fritz_Heider) and [Marianne Simmel](https://en.wikipedia.org/wiki/Marianne_Simmel)'s experiments with animated shapes from 1944 [@Heider:experimental44]. Our interpretation of these objects as showing motives and even emotion is a combination of our desire for narrative, a need for understanding of each other, and our ability to empathise. At one level, these are crudely drawn objects, but in another key way, the animator has communicated a story through simple facets such as their relative motions, their sizes and their actions. We apply our psychological representations to these faceless shapes in an effort to interpret their actions.

> There are three types of lies: lies, damned lies and statistics
>
> Benjamin Disraeli 1804-1881

The quote lies, damned lies and statistics was credited to Benjamin Disraeli by Mark Twain in his autobiography. It characterizes the idea that statistic can be made to prove anything. But Disraeli died in 1881 and Mark Twain died in 1910. The important breakthrough in overcoming our tendency to overinterpet data came with the formalization of the field through the development of *mathematical statistics*.

### *Mathematical* Statistics

<img class="" src="http://inverseprobability.com/talks/slides/diagrams/Portrait_of_Karl_Pearson.jpg" width="30%" align="" style="background:none; border:none; box-shadow:none;">

[Karl Pearson](https://en.wikipedia.org/wiki/Karl_Pearson) (1857-1936), [Ronald Fisher](https://en.wikipedia.org/wiki/Ronald_Fisher) (1890-1962) and others considered the question of what conclusions can truly be drawn from data. Their mathematical studies act as a restraint on our tendency to over-interpret and see patterns where there are none. They introduced concepts such as randomized control trials that form a mainstay of the our decision making today, from government, to clinicians to large scale A/B testing that determines the nature of the web interfaces we interact with on social media and shopping.

Today the statement "There are three types of lies: lies, damned lies and 'big data'" may be more apt. We are revisiting many of the mistakes made in interpreting data from the 19th century. Big data is laid down by happenstance, rather than actively collected with a particular question in mind. That means it needs to be treated with care when conclusions are being drawn. For data science to succede it needs the same form of rigour that Pearson and Fisher brought to statistics, a "mathematical data science" is needed.

### Artificial Intelligence and Data Science

Machine learning technologies have been the driver of two related, but distinct disciplines. The first is *data science*. Data science is an emerging field that arises from the fact that we now collect so much data by happenstance, rather than by *experimental design*. Classical statistics is the science of drawing conclusions from data, and to do so statistical experiments are carefully designed. In the modern era we collect so much data that there's a desire to draw inferences directly from the data.

As well as machine learning, the field of data science draws from statistics, cloud computing, data storage (e.g. streaming data), visualization and data mining.

In contrast, artificial intelligence technologies typically focus on emulating some form of human behaviour, such as understanding an image, or some speech, or translating text from one form to another. The recent advances in artifcial intelligence have come from machine learning providing the automation. But in contrast to data science, in artifcial intelligence the data is normally collected with the specific task in mind. In this sense it has strong relations to classical statistics. 

Classically artificial intelligence worried more about *logic* and *planning* and focussed less on data driven decision making. Modern machine learning owes more to the field of *Cybernetics* [@Wiener:cybernetics48] than artificial intelligence. Related fields include *robotics*, *speech recognition*, *language understanding* and *computer vision*. 

There are strong overlaps between the fields, the wide availability of data by happenstance makes it easier to collect data for designing AI systems. These relations are coming through wide availability of sensing technologies that are interconnected by celluar networks, WiFi and the internet. This phenomenon is sometimes known as the *Internet of Things*, but this feels like a dangerous misnomer. We must never forget that we are interconnecting people, not things. 

### What does Machine Learning do?

Any process of automation allows us to scale what we do by codifying a process in some way that makes it efficient and repeatable. Machine learning automates by emulating human (or other actions) found in data. Machine learning codifies in the form of a mathematical function that is learnt by a computer. If we can create these mathematical functions in ways in which they can interconnect, then we can also build systems.

Machine learning works through codifing a prediction of interest into a mathematical function. For example, we can try and predict the probability that a customer wants to by a jersey given knowledge of their age, and the latitude where they live. The technique known as logistic regression estimates the odds that someone will by a jumper as a linear weighted sum of the features of interest.

$$ \text{odds} = \frac{p(\text{bought})}{p(\text{not bought})} $$
$$ \log \text{odds}  = \beta_0 + \beta_1 \text{age} + \beta_2 \text{latitude}$$

Here $\beta_0$, $\beta_1$ and $\beta_2$ are the parameters of the model. If $\beta_1$ and $\beta_2$  are both positive, then the log-odds that someone will buy a jumper increase with increasing latitude and age, so the further north you are and the older you are the more likely you are to buy a jumper. The parameter $\beta_0$ is an offset parameter, and gives the log-odds of buying a jumper at zero age and on the equator. It is likely to be negative[^logarithms] indicating that the purchase is odds-against. This is actually a classical statistical model, and models like logistic regression are widely used to estimate probabilities from ad-click prediction to risk of disease.

[^logarithm]: The logarithm of a number less than one is negative, for a number greater than one the logarithm is positive. So if odds are greater than evens (odds-on) the log-odds are positive, if the odds are less than evens (odds-against) the log-odds will be negative.

This is called a generalized linear model, we can also think of it as estimating the *probability* of a purchase as a nonlinear function of the features (age, lattitude) and the parameters (the $\beta$ values). The function is known as the *sigmoid* or [logistic function](https://en.wikipedia.org/wiki/Logistic_regression), thus the name *logistic* regression.


$$ p(\text{bought}) =  \sigmoid{\beta_0 + \beta_1 \text{age} + \beta_2 \text{latitude}}$$

In the case where we have *features* to help us predict, we sometimes denote such features as a vector, $\inputVector$, and we then use an inner product between the features and the parameters, $\boldsymbol{\beta}^\top \inputVector = \beta_1 \inputScalar_1 + \beta_2 \inputScalar_2 + \beta_3 \inputScalar_3 ...$, to represent the argument of the sigmoid.

$$ p(\text{bought}) =  \sigmoid{\boldsymbol{\beta}^\top \inputVector}$$

More generally, we aim to predict some aspect of our data, $\dataScalar$, by relating it through a mathematical function, $\mappingFunction(\cdot)$, to the parameters, $\boldsymbol{\beta}$ and the data, $\inputVector$.

$$ \dataScalar =  \mappingFunction\left(\inputVector, \boldsymbol{\beta}\right)$$

We call $\mappingFunction(\cdot)$ the *prediction function*

To obtain the fit to data, we use a separate function called the *objective function* that gives us a mathematical representation of the difference between our predictions and the real data. 

$$\errorFunction(\boldsymbol{\beta}, \dataMatrix, \inputMatrix)$$
A commonly used examples (for example in a regression problem) is least squares,
$$\errorFunction(\boldsymbol{\beta}, \dataMatrix, \inputMatrix) = \sum_{i=1}^\numData \left(\dataScalar_i - \mappingFunction(\inputVector_i, \boldsymbol{\beta})\right)^2.$$

If a linear prediction funciton is combined with the least squares objective function then that gives us a classical *linear regression*, another classical statistical model. Statistics often focusses on linear models because it makes interpretation of the model easier. Interpretation is key in statistics because the aim is normally to validate questions by analysis of data. Machine learning has typically focussed more on the prediction function itself and worried less about the interpretation of parameters, which are normally denoted by $\mathbf{w}$ instead of $\boldsymbol{\beta}$. As a result *non-linear* functions are explored more often as they tend to improve quality of predictions but at the expense of interpretability.

### Deep Learning

* These are interpretable models: vital for disease etc.

* Modern machine learning methods are less interpretable

* Example: face recognition

<small>Outline of the DeepFace architecture. A front-end of a single convolution-pooling-convolution filtering on the rectified input, followed by three locally-connected layers and two fully-connected layers. Color illustrates feature maps produced at each layer. The net includes more than 120 million parameters, where more than 95% come from the local and fully connected.</small>

<img class="" src="http://inverseprobability.com/talks/slides/diagrams/deepface_neg.png" width="100%" align="" style="background:none; border:none; box-shadow:none;">

<p align="right">
<small>Source: DeepFace</small></p>

<img class="" src="http://inverseprobability.com/talks/slides/diagrams/576px-Early_Pinball.jpg" width="50%" align="" style="background:none; border:none; box-shadow:none;">

We can think of what these models are doing as being similar to early pin ball machines. In a neural network, we input a number (or numbers), whereas in pinball, we input a ball. The location of the ball on the left-right axis can be thought of as the number. As the ball falls through the machine, each layer of pins can be thought of as a different layer of neurons. Each layer acts to move the ball from left to right. 

In a pinball machine, when the ball gets to the bottom it might fall into a hole defining a score, in a neural network, that is equivalent to the decision: a classification of the input object. 

An image has more than one number associated with it, so it's like playing pinball in a *hyper-space*.

At initialization, the pins aren't in the right place to bring the ball to the correct decision.

Learning involves moving all the pins to be in the right position, so that the ball falls in the right place. But moving all these pins in hyperspace can be difficult. In a hyper space you have to put a lot of data through the machine for to explore the positions of all the pins. Adversarial learning reflects the fact that a ball can be moved a small distance and lead to a very different result.

Probabilistic methods explore more of the space by considering a range of possible paths for the ball through the machine.

### Uncertainty and Learning

* In this "vanilla" form these machines "don't know when they don't know".

* Doubt is vital in real world decision making. 

* Incorporating this in systems is a long time focus of my technical research.


### Comparison with Human Learning & Embodiment

* The emulation of intelligence does not exhibit all the meta-modelling humans perform.

### Data Science

* Industrial Revolution 4.0?
* *Industrial Revolution* (1760-1840) term coined by Arnold Toynbee,
late 19th century.
* Maybe: But this one is dominated by *data* not *capital*
* That presents *challenges* and *opportunities* 

compare [digital oligarchy](https://www.theguardian.com/media-network/2015/mar/05/digital-oligarchy-algorithms-personal-data) vs [how Africa can benefit from the data revolution](https://www.theguardian.com/media-network/2015/aug/25/africa-benefit-data-science-information)

Disruptive technologies take time to assimilate, and best practices, as well as the pitfalls of new technologies take time to share. Historically, new technologies led to new professions. [Isambard Kingdom Brunel](https://en.wikipedia.org/wiki/Isambard_Kingdom_Brunel) (born 1806) was a leading innovator in civil, mechanical and naval engineering. Each of these has its own professional institutions founded in 1818, 1847, and 1860 respectively.

[Nikola Tesla](https://en.wikipedia.org/wiki/Nikola_Tesla) developed the modern approach to electrical distribution, he was born in 1856 and the American Instiute for Electrical Engineers was founded in 1884, the UK equivalent was founded in 1871. 

[William Schockley Jr](https://en.wikipedia.org/wiki/William_Shockley), born 1910, led the group that developed the transistor, referred to as "the man who brought silicon to Silicon Valley", in 1963 the American Institute for Electical Engineers merged with the Institute of Radio Engineers to form the Institute of Electrical and Electronic Engineers. 

[Watts S. Humphrey](https://en.wikipedia.org/wiki/Watts_Humphrey), born 1927, was known as the "father of software quality", in the 1980s he founded a program aimed at understanding and managing the software process. The British Computer Society was founded in 1956.

Why the need for these professions? Much of it is about codification of best practice and developing trust between the public and practitioners. These fundamental characteristics of the professions are shared with the oldest professions (Medicine, Law) as well as the newest (Information Technology).

So where are we today? My best guess is we are somewhere equivalent to the 1980s for Software Engineering. In terms of professional deployment we have a basic understanding of the equivalent of "programming" but much less understanding of *machine learning systems design* and *data infrastructure*. How the components we ahve developed interoperate together in a reliable and accountable manner. Best practice is still evolving, but perhaps isn't being shared widely enough. 

One problem is that the art of data science is superficially similar to regular software engineering. Although in practice it is rather different. Modern software engineering practice operates to generate code which is well tested as it is written, agile programming techniques provide the appropriate degree of flexibility for the individual programmers alongside sufficient formalization and testing. These techniques have evolved from an overly restrictive formalization that was proposed in the early days of software engineering.

While data science involves programming, it is different in the following way. Most of the work in data science involves understanding the data and the appropriate manipulations to apply to extract knowledge from the data. The eventual number of lines of code that are required to extract that knowledge are often very few, but the amount of thought and attention that needs to be applied to each line is much more than a traditional line of software code. Testing of those lines is also of a different nature, provisions have to be made for evolving data environments. Any development work is often done on a static snapshot of data, but deployment is made in a live environment where the nature of data changes. Quality control involves checking for degradation in performance arising form unanticipated changes in data quality. It may also need to check for regulatory conformity. For example, in the UK the General Data Protection Regulation stipulates standards of explainability and fairness that may need to be monitored. These concerns do not affect traditional software deployments.

Others are also pointing out these challenges, [this post](https://medium.com/@karpathy/software-2-0-a64152b37c35) from Andrej Karpathy (now head of AI at Tesla) covers the notion of "Software 2.0". Google researchers have highlighted the challenges of "Technical Debt" in machine learning [@Sculley:debt15]. Researchers at Berkeley have characterized the systems challenges associated with machine learning [@Stoica:systemsml17].

Data science is not only about technical expertise and analysis of data, we need to also generate a culture of decision making that acknowledges the true challenges in data-driven automated decision making. In particular, a focus on algorithms has neglected the importance of data in driving decisions. The quality of data is paramount in that poor quality data will inevitably lead to poor quality decisions. Anecdotally most data scientists will suggest that 80% of their time is spent on data clean up, and only 20% on actually modelling. 

### The Software Crisis

>The major cause of the software crisis is that the machines have
>become several orders of magnitude more powerful! To put it quite
>bluntly: as long as there were no machines, programming was no problem
>at all; when we had a few weak computers, programming became a mild
>problem, and now we have gigantic computers, programming has become an
>equally gigantic problem.
>
> Edsger Dijkstra (1930-2002), The Humble Programmer

In the late sixties early software programmers made note of the increasing costs of software development and termed the challenges associated with it as the "[Software Crisis](https://en.wikipedia.org/wiki/Software_crisis)". Edsger Dijkstra referred to the crisis in his 1972 Turing Award winner's address.

### The Data Crisis

>The major cause of the data crisis is that machines have become more
>interconnected than ever before. Data access is therefore cheap, but
>data quality is often poor. What we need is cheap high quality
>data. That implies that we develop processes for improving and
>verifying data quality that are efficient.
>
>There would seem to be two ways for improving efficiency. Firstly, we
>should not duplicate work. Secondly, where possible we should automate
>work. 

What I term "The Data Crisis" is the modern equivalent of this problem. The quantity of modern data, and the lack of attention paid to data as it is initially "laid down" and the costs of data cleaning are bringing about a crisis in data-driven decision making. Just as with software, the crisis is most correctly addressed by 'scaling' the manner in which we process our data. Duplication of work occurs because the value of data cleaning is not correctly recognised in management decision making processes. Automation of work is increasingly possible through techniques in "artificial intelligence", but this will also require better management of the data science pipeline so that data about data science (meta-data science) can be correctly assimilated and processed. The Alan Turing institute has a program focussed on this area, [AI for Data Analytics](https://www.turing.ac.uk/research_projects/artificial-intelligence-data-analytics/).

<img class="" src="http://inverseprobability.com/talks/slides/diagrams/Medievalplowingwoodcut.jpg" width="" align="" style="background:none; border:none; box-shadow:none;">

Our current information infrastructure bears a close relation with *feudal systems* of government. In the feudal system a lord had a duty of care over his serfs and vassals, a duty to protect subjects. But in practice there was a power-asymetry. In feudal days protection was against Viking raiders, today, it is against information raiders. However, when there is an information leak, when there is a failure it is too late. Alternatively, our data is publicly shared, in an information commons. Akin to common land of the medieval village. But just as commons were subject to overgrazing and poor management, so it is that much of our data cannot be managed in this way. In particularly personal, sensitive data. 

I explored this idea further in [this Guardian Op-Ed from 2015](https://www.theguardian.com/media-network/2015/nov/16/information-barons-threaten-autonomy-privacy-online).

## Public Use of Data for Public Good

Since machine learning methods are so dependent on data, Understanding public attitudes to the use of their data is key to developing machine learning methods that maintain the trust of the public. Nowhere are the benefits of machine learning more profound, and the potential pitfalls more catastrophic than in the use of machine learning in health data. 

The promise is for methods that take a personalized perspective on our individual health, but health data is some of the most sensitive data available to us. This is recognised both by the public and by regulation. 

With this in mind The Wellcome Trust launched a report on ["Understanding Patient Data"](https://wellcome.ac.uk/news/understanding-patient-data-launches-today) authored by Nicola Perrin, driven by the National Data Guardian's recommendations.

From this report we know that patients trust Universities and hospitals more than the trust commercial entities and insurers. However, there are a number of different ways in which data can be mishandled, it is not only the intent of the data-controllers that effects our data security.

For example, the recent WannaCry virus attack which demonstrated the unpreparedness of much of the NHS IT infrastructure for a virus exhibiting an exploit that was well known to the security community. The key point is that the public trust the *intent* of academics and medical professionals, but actual *capability* could be at variance with the intent. 

<img class="" src="http://inverseprobability.com/talks/slides/diagrams/health/bush-pilot-grant-mcconachie.jpg" width="60%" align="" style="background:none; border:none; box-shadow:none;">

<center><i>Bush Pilot Grant McConachie</i></center>

The situation is somewhat reminiscient of early aviation. This is where we are with our data science capabilities. By analogy, the engine of the plane is our data security infrastructure, the basic required technology to make us safe. The pilot is the health professional performing data analytics. The nature of the job of early pilots and indeed today's *bush pilots* (who fly to remote places) included a need to understand the mechanics of the engine. Just as a health data scientist, today, needs to deal with security of the infrastructure as well as the nature of the analysis.

<img class="" src="http://inverseprobability.com/talks/slides/diagrams/health/British_Airways_at_SFO.jpg" width="50%" align="" style="background:none; border:none; box-shadow:none;">
<center><i>British Airways 747 at SFO</i></center>

I suspect most passengers would find it disconcerting if the pilot of a 747 was seen working on the engine shortly before a flight. As aviation has become more widespread, there is now a separation of responsibilities between pilots and mechanics. Indeed, Rolls Royce maintain ownership of their engines today, and merely lease them to the aircraft company. The responsibility for maintenance of the engine is entirely with Rolls Royce, yet the pilot is responsibility for the safety of the aircraft and its passengers.

We need to develop a modern data-infrastructure for which separates the need for security of infrastructure from the decision making of the data analyst.
 
This separation of responsibility according to expertise needs to be emulated when considering health data infrastructure. This resolves the *intent-capability* dilemma, by ensuring a separation of responsibilities to those that are best placed to address the issues.

### Propagation of Best Practice

We must also be careful to maintain openness in this new genaration of digital solutions for patient care. Matthew Syed's book, "Black Box Thinking" [@Syed:blackbox15], emphasizes the importance of surfacing errors as a route to learning and improved process. Taking aviation as an example, and contrasting it with the culture in medicine, Matthew relates the story of [Martin Bromiley](https://chfg.org/trustees/martin-bromiley/), an airline pilot whose wife died during a routine hospital procedure and his efforts to improve the culture of safety in medicine. The motivation for the book is the difference in culture between aviation and medicine in how errors are acknowledged and dealt with. We must ensure that these high standards of oversight apply to the era of data-driven automated decision making. 

In particular, while there is much to be gained by involving comemrcial companies, if the process by which they are drawing inference about patient condition is hidden (for example, due to commercial confidentiality), this may prevent us from understanding errors in diagnosis or treatment. This would be a retrograde step. It may be that health device certification needs modification or reform for data-driven automated decision making, but we need a spirit of transparency around how these systems are deriving their inferences to ensure best practice.

## Data Trusts

The machine learning solutions we are dependent on to drive automated decision making are dependent on data. But with regard to personal data there are important issues of privacy. Data sharing brings benefits, but also exposes our digital selves. From the use of social media data for targeted advertising to influence us, to the use of genetic data to identify criminals, or natural family members. Control of our virtual selves maps on to control of our actual selves. 

The fuedal system that is implied by current data protection legislation has signficant power asymmetries at its heart, in that the data controller has a duty of care over the data subject, but the data subject may only discover failings in that duty of care when it's too late. Data controllers also may have conflicting motivations, and often their primary motivation is *not* towards the data-subject, but that is a consideration in their wider agenda.

I proposed [Data Trusts](https://www.theguardian.com/media-network/2016/jun/03/data-trusts-privacy-fears-feudalism-democracy) as a solution to this problem. Inspired by *land societies* that formed in the 19th century to bring democratic representation to the growing middle classes. A land society was a mutual organisation where resources were pooled for the common good. 

A Data Trust would be a legal entity where the trustees responsibility was entirely to the members of the trust. So the motivation of the data-controllers is aligned only with the data-subjects. How data is handled would be subject to the terms under which the trust was convened. The success of an individual trust would be contingent on it satisfying its members with appropriate balancing of individual privacy with the benefits of data sharing. 

Formation of Data Trusts became the number one recommendation of the Hall-Presenti report on AI, but the manner in which this is done will have a significant impact on their utility. It feels important to have a diversity of approaches, and yet it feels important that any individual trust would be large enough to be taken seriously in representing the views of its members in wider negotiations.

### Thanks!

* twitter: @lawrennd
* blog: [http://inverseprobability.com](http://inverseprobability.com/blog.html)
* [Mike Jordan's Medium Post](https://medium.com/@mijordan3/artificial-intelligence-the-revolution-hasnt-happened-yet-5e1d5812e1e7)
