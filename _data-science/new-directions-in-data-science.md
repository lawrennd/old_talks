---
title: New Directions in Data Science
author:
- given: Neil D.
  family: Lawrence
  twitter: lawrennd
  url: http://inverseprobability.com
abstract: |
  Data science presents new opportunities for Africa but also new
  challenges. In this talk we will focus on three separate challenges
  for data science: 1. Paradoxes of the Data Society, 2. Quantifying
  the Value of Data, 3. Privacy, loss of control,
  marginalization. Each of these challenges has particular
  implications for data science in the developing world. By addressing
  these challenges now we can ensure that the pitfalls of the data
  driven society are overcome allowing to reap the benefits.
venue: Data Science in Africa Workshop
location: Pulse Lab, Kampala, Uganda
date: 2016-07-01
---

\notes{This post is thoughts for a talk given at the UN Global Pulse lab in Kampala as part of the second [Data Science in Africa Workshop](http://www.datascienceafrica.org) at the [UN Global Pulse Lab in Kampala, Uganda](http://www.unglobalpulse.org/kampala). It covers challenges in data science.

Data is a pervasive phenomenon. It affects all aspects of our activities. This diffusiveness is both a challenge and an opportunity. A challenge, because our expertise is spread thinly: like raisins in a fruitcake, or nuggets in a gold mine. It is an opportunity, because if we can resolve the challenges of difussion we can foster a multi-faceted benefits across the entire University.

## What Got Us Here

The old world of data was formulated around the relationship between human and data. Data was expensive to collect, and the focus was on minimising subjectivity through randomised trials and hypothesis testing.

<img src="http://inverseprobability.com/talks/slides/diagrams/data-science/information-flow.svg" width="30%">

*The trinity of human, data and computer, and highlights the modern phenomenon. The communication channel between computer and data now has an extremely high bandwidth. The channel between human and computer and the channel between data and human is narrow.*

Historically, the interaction between human and data was necessarily restricted by our capability to absorb its implications and the laborious tasks of collection, collation and validation. The bandwidth of communication between human and computer was limited (perhaps at best hundreds of bits per second).

This status quo has been significantly affected by the coming of the digital age and the development of fast computers with extremely high communication bandwidth. In particular, today, our computing power is widely distributed and communication occurs at Gigabits per second. Data is now often collected through happenstance. Its collation can be automated. The cost per bit has dropped dramatically, but the care with which it is collected has significantly decreased.

Traditional data analyses focused on the interaction between data and human. Sometimes, these data may have been processed by computer, but often through human driven data entry.

Today, massively interconnected processing power combined with widely deployed sensorics has led to manyfold increases in the channel between data and computer. This leads to two effects:

* automated decision making within the computer based only on the data. 
* a requirement to better understand our own subjective biases to ensure that the human to computer interface formulates the correct conclusions from the data.

This process has already revolutionised biology, leading to computational biology and a closer interaction between computational, mathematical and wet lab scientists. Now we are seeing new challenges in health and computational social sciences. The area has been widely touted as 'big data' in the media and the sensorics side has been referred to as the 'internet of things'. In some academic fields overuse of these terms has already caused them to be viewed with some trepidation. However, the phenomena to which the refer are very real. With this in mind we choose the term 'data science' to refer to the wider domain of studying these effects and developing new methodologies and practices for dealing with them. 

The main shift in dynamic we'd like to highlight is from the direct pathway between human and data (the traditional domain of statistics) to the indirect pathway between human and data via the computer scientist. This change of dynamics gives us the modern and emerging domain of data science.

## Challenges

The field of data science is rapidly evolving. Different practitioners from different domains have their own perspectives. In this post we identify three broad challenges that are emerging. Challenges which have not been addressed in the traditional sub-domains of data science. The challenges have social implications but require technological advance for their solutions.

### Paradoxes of the Data Society

The first challenge we'd like to highlight is the unusual paradoxes of the data society. It is too early to determine whether these paradoxes are fundmental or transient. Evidence for them is still somewhat anecdotal, but they seem worthy of further attention.

#### The Paradox of Measurement

The first paradox is the paradox of measurement in the data society. We are now able to quantify to a greater and greater degree the actions of individuals in society, and this might lead us to believe that social science, politics, economics are becoming quantifiable. We are able to get a far richer characterization of the world around us. Paradoxically it seems that as we measure more, we understand less.

How could this be possible? It may be that the greater preponderance of data is making society itself more complex. Therefore traditional approaches to measurement (e.g. polling by random sub sampling) are becoming harder, for example due to more complex batch effects, a greater stratification of society where it is more difficult to weigh the various sub-populations correctly.

The end result is that we have a Curate's egg of a society: it is only 'measured in parts'. Whether by examination of social media or through polling we no longer obtain the overall picture that can be necessary to obtain the depth of understanding we require.

[One example of this phenomenon](http://www.theguardian.com/politics/2015/nov/13/new-research-general-election-polls-inaccurate) is the 2015 UK election which polls had as a tie and yet in practice was won by the Conservative party with a seven point advantage. A post-election poll which was truly randomized suggested that this lead was measurable, but pre-election polls are conducted on line and via phone. These approaches can under represent certain sectors. The challenge is that the truly randomized poll is expensive and time consuming. In practice on line and phone polls are usually weighted to reflect the fact that they are not truly randomized, but in a rapidly evolving society the correct weights may move faster than they can be tracked. 

Another example is clinical trials. Once again they are the preserve of randomized studies to verify the efficacy of the drug. But now, rather than population becoming more stratified, it is the more personalized nature of the drugs we wish to test. A targeted drug which has efficacy in a sub-population may be harder to test due to difficulty in recruiting the sub-population, the benefit of the drug is also for a smaller sub-group, so expense of drug trials increases.

There are other less clear cut manifestations of this phenomenon. We seem to rely increasingly on social media as a news source, or as a indicator of opinion on a particular subject. But it is beholden to the whims of a vocal minority. 

Similar to the way we required more paper when we first developed the computer, the solution is more *classical* statistics. We need to do more work to verify the tentative conclusions we produce so that we know that our new methodologies are effective.

#### Filter Bubbles and Echo Chambers

A related effect is own own ability to judge the wider society in our countries and across the world. It is now possible to be connected with friends and relatives across the globe, and one might hope that would lead to greater understanding between people. Paradoxically, it may be the case that the opposite is occurring, that we understand each other less well.

This argument, sometimes summarised as the 'filter bubble' or the 'echo chamber' is based on the idea that our information sources are now curated, either by ourselves or by algorithms working to maximise our interaction. Twitter feeds, for example, contain comments from only those people you follow. Facebook's newsfeed is ordered to increase your interaction with the site. 

In our diagram above, if humans have a limited bandwidth through which to consume their data, and that bandwidth is saturated with filtered content, e.g. ideas which they agree with, then it might be the case that we become more entrenched in our opinions than we were before. We don't see ideas that challenge our opinions. 

This is not a purely new phenomenon, in the past people's perspectives were certainly influenced by the community in which they lived, but the scale on which this can now occur is much larger than it has been before.

### Quantifying the Value of Data

Most of the data we generate is not directly usable. To make it usable we first need to identify it, then curate it and finally make it accessible. Historically this work was done because data was actively collected and the collection of data was such a burden in itself that its curation was less of an additional overhead. Now we find that there's a sea of data, but most of it is undrinkable. We require data-desalination before it can be consumed. 

<img src="http://inverseprobability.com/talks/slides/diagrams/sea-water-ocean-waves.jpg" width="50%">

* How do we measure value in the data economy?
* How do we encourage data workers: curation and management.
  * Incentivization
  * Quantifying the value in their contribution.

This relates also to the questions of measurment above. Direct work on data generates an enormous amount of 'value' in the data economy. Yet, the credit allocation for this work is not properly accounted for. There are many organizations where the curation of data is treated almost as a dirty after thought, you might be shown simmulations of cities of questionable value (in the real world) but highlighting work at the data-face is rare. Until this work is properly quantified the true worth of an organisation will not be understood. This may be because such work is difficult to 'embody'.

By embodiment here we mean the delivery of something tangible to (perhaps) a decision maker who has an interest in the data. Data is diffusive and pervasive by its nature. This means for non-experts its potential is sometimes difficult to realize. Similarly, for data experts who are non-domain experts there are challenges in understanding what aspect of the domain requires implementation.[^embodiment] 

[^embodiment]:The importance of embodiment is reflected in a mini-industry of simulation that seems to pervade complex systems. But often simulation without motivation. For example, it seems impressive to build a large scale simulation of a city like Sheffield and it seems like such a simulation should be useful for decision makers. In practice though, most decision makers focus (at any given time) on a particular aspect of the city and a full complex simulation is not required. Such simulations do, however, impress non-domain experts.

Another important action is to encourage greater interaction between application domains and data scientists. Embedding of data scientists within application teams and greater education of domain experts in the possibilities and limitations of the data. This is particularly important in data science education: when projects are proposed they should be undertaken through close interaction with the application domain, for example through project placements. 

Visualization of data seems very important as an intermediary between the data scientist and the application domain. A visualization acts in such a way so as to embody the data set and generate questions around it. Getting into the habit of visualizing data also forces the data generators to perform some basic quality control. Critical analysis of visualized data should be widely taught, it doesn't require such strong technical understanding as full analysis, but acts as an important quality control on the data set close to where it is collected.

A final possibility would be the adoption of 'data readiness levels' for describing the nature of data collected and its potential usability. Data readiness levels would mirror 'technology readiness levels' which assess the deployability of technology in application. Technology is a similarly diffuse idea to 'data'. Readiness levels ensure that reports and/or discussions have some way of accounting for deployability in discussions even for non-experts.

Better quantifying the value of data also has important implications for incetivisation markets which encourage users to provide data in exchange for incentives. The extent to which this economy will become separate from the standard economy of monetary exchange for services is also unclear. And as it does separate, it compounds the problem of measurement highlighted above.

### Privacy, Loss of Control and Marginalization

While society is perhaps becoming harder to monitor, the individual is becoming easier. Our behavior can now be tracked to a far greater extent than ever before in our history. What would have been considered surveillance in our past is now standard practice. 

We are to a great extent compounding this problem, for example social media monitoring for 'hate speech' as an early warning system of potential inter-tribal tensions could easily evolve into monitoring social media for 'political dissent'.

Even less nefarious purposes, such as marketing, become more sinister when the target of the marketing is well understood and the (digital) environment of the target is also so well controlled.

As computers collect more data about us they will characterize us better and, given a particular scenario, they are likely to be able to predict our own actions better than we can predict them ourselves. If a system external to ourselves can predict our actions better than us, does this have implications for our free will?

### Marginalization and Discrimination

This also has the potential for powerful discrimination against the disadvantaged. When automated decision making is taking place, then there is the possibility for significant discrimination on the basis of race, religion, sexuality, health status. This is all prohibited under European law, but it can pass unawares, it can be implicit in our processes. 

Applications such as credit scoring, insurance, medical treatment will all suffer if particular sections of society are under-represented in data sets collected for those applications. Predictions made would be less accurate. This has particular consequences for developing economies if these applications are developed mainly in developed economies (or even more specifically in Silicon Valley).

To ameliorate the downsides of these outcomes we should be working to ensure that the individual retains control of their own data. This is the concept of privacy. We accept, in our real lives, the principle that we should be able to express ourselves differently according to the nature of our social relationship. I share more with my doctor than my students. This control of self needs to be replicated in the digital world. Technologies like differential privacy are the key here.

With regards to discrimination, we need to increase awareness of the pitfalls among researchers and ensure that technological solutions are being delivered not merely for the set of #FirstWorldProblems but for the wider set of challenges that the greater part of the world's population is facing. That involves increasing the capability to meet those challenges within the populations that are facing them.

## Conclusion

Data science offers a great deal of promise in resolving our challenges in health, wealth and well being, but it is also associated with a set of potential pitfalls. As data scientists it is particularly incumbent upon us to avoid these pitfalls and ensure that our community takes steps to resolve challenges as rapidly and equitably as possible. The nature of data is changing and will continue to change our societies. We need to work to ensure that those changes are carried out in a manner that narrows inequality and preserves the individual freedoms we have come to expect. }

\slides{\newslide{Background}

* Data is Pervasive phenomenon that affects all aspects of our activities
* Data diffusiveness is both a challenge and an opportunity

\section{Evolved Relationship}

<img src="./diagrams/data-science-information-flow.png" width="60%">

\section{Societal Effects}

* Automated decision making within the computer based only on the data
* A requirement to better understand our own subjective biases to ensure that the human to computer interface formulates the correct conclusions from the data

\section{Societal Effects}

* This process has already revolutionised biology

* Shift in dynamic from the direct pathway between human and data to indirect pathway between human and data via the computer

* This change of dynamics gives us the modern and emerging domain of data science

\section{Challenges}

1. Paradoxes of the Data Society

2. Quantifying the Value of Data

3. Privacy, loss of control, marginalization

\section{Measurement}

* Able to quantify to a greater and greater degree the actions of individuals

* But less able to characterize society

* As we measure more, we understand less

\section{What?}

* Perhaps  greater preponderance of data is making society itself more complex

* Therefore traditional approaches to measurement are failing

* Curate's egg of a society: it is only 'measured in parts'

\section{Examples}

* 2015 UK election polls

* Clinical trial and personalized medicine

* Social media memes

* Filter bubbles and echo chambers

\section{Solutions}

* More classical statistics!

* A better characterization of human needs and flaws

\section{Quantifying the Value of Data}

There's a sea of data, but most of it is undrinkable

<img src="./diagrams/sea-water-ocean-waves.jpg" width="50%">

We require data-desalination before it can be consumed!

\section{Value}

* How do we measure value in the data economy?
* How do we encourage data workers: curation and management
  * Incentivization
  * Quantifying the value in their contribution

\section{Credit Allocation}

* Direct work on data generates an enormous amount of 'value' in the data economy but this is unaccounted in the economy

* Hard because data is difficult to 'embody'

\section{Solutions}

* Encourage greater interaction between application domains and data scientists

* Encourage visualization of data

* Adoption of 'data readiness levels'

* Implications for incentivization schemes

\subsection{Privacy, Loss of Control and Marginalization}

* Society is becoming harder to monitor

* Individual is becoming easier to monitor

\subsection{Hate Speech or Political Dissent?}

* social media monitoring for 'hate speech' can be easily turned to political dissent monitoring

\section{Marketing}

* can become more sinister when the target of the marketing is well understood and the (digital) environment of the target is also so well controlled


\section{Free Will}

*  What does it mean if a computer can predict our individual behavior better than we ourselves can?

\section{Discrimination}

* Potential for explicit and implicit discrimination on the basis of race, religion, sexuality, health status

* All prohibited under European law, but can pass unawares, or be implicit

\section{Marginalization}

* Credit scoring, insurance, medical treatment
* What if certain sectors of society are under-represented in our aanalysis?
* What if Silicon Valley develops everything for us?

\section{Amelioration}

* Work to ensure individual retains control of their own data
* We accept privacy in our real lives, need to accept it in our digital
* Control of persona and ability to project

\section{Awareness}

* Need to increase awareness of the pitfalls among researchers
* Need to ensure that technological solutions are being delivered not merely for few (#FirstWorldProblems)
* Address a wider set of challenges that the greater part of the world's population is facing

\section{Conclusion}

* Data science offers a great deal of promise
* There are challenges and pitfalls
* It is incumbent on us to avoid them}

\thanks

\references
