---
title: "Intellectual Debt and the Death of the Programmer"
abstract: >
  Technical debt is incurred when complex systems are rapidly deployed without due thought as to how they will be *maintained*. Intellectual debt is incurred when complex systems are rapidly deployed without due thought to how they'll be *explained*.
  
  Both problems are pervasive in the design and deployment of large scale algorithmic decision making engines. 
  
  In this talk we'll review the origin of the problem, and propose a roadmap for obtaining solutions. It's a journey that will require collaboration between industry, academia, third sector, and government. 
reveal: True
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Cambridge
  twitter: lawrennd
  url: http://inverseprobability.com
date: 2020-02-14
venue: Distinguished Lecture Series on Information Engineering 
transition: None
---

I was woken up on Wednesday morning with three news headlines that don't seem connected. But I'd like to connect them today. The connections I'll draw go to the heart of fundamental challenges we'll face with our artificial intelligence solutions. 

The first headline was about the national census, Sir Ian Diamond, the UK's National Statistician, [suggested that the next national census might be our last](https://www.bbc.co.uk/news/uk-51468919).

The second headline was about the OfCom, the UK's national regulator of telecommunications being granted more powers to [more powers to control content on social media](https://www.bbc.co.uk/news/technology-51446665).

The third headline was about the short-selling (you can listen [here](https://www.bbc.co.uk/sounds/play/m000f76k), go to 17 minutes 26 second). Carson Block, a US-based short-selling firm raised questions over asset values. In the interview, Carson referred to the difference between accounting practices that are illegal versus those that misrepresent the financial health of a company. Since the collapse of BHS, Patisserie Valerie and Carillion auditing practices have come under scrutiny.

How are these three items connected? Well, my argument in this talk is that they are each part of wider phenomena which when combined will form a perfect storm for "artificial intelligence" technologies. The Cambridge Analytica scandal and challenges with election manipulation are just the leading edge of this storm. 

To weather the challenges we face, we need far more interaction across academic sub-disciplines, policy and industry. Helping to facilitate that is my main aim in moving to Cambridge, and I'm excited about the opportunities that this University and this city offer for delivering on that vision.

These challenges are multi-faceted, but today I want to focus on the primary challenge which unites these three news headlines. I was struggling for a term for it, until a couple of weeks back when I was sharing a coffee with Bill Thompson. Those that know Bill will understand that he is a Cambridge institution, and a font of wisdom and knowledge on all things technical. I was describing the challenge we face and Bill said: this sounds like Jonathan Zittrain's notion of Intellectual Debt. 

Zittrain gave the Tanner lectures at Clare Hall last month, which I'm very disappointed I missed. Because the challenges he's highlighting are exactly those that my research is designed to address.

So what is intellectual debt?

In computer systems the concept of *technical debt* has been surfaced by authors including @Sculley:debt15. It is an important concept, that I think is somewhat hidden from the academic community, because it is a phenomenon that occurs when a computer software system is deployed. 

In technology, there is the notion of a "minimum viable product" (MVP). Sometimes called "minimum loveable product" (MLP). A minimum viable product is the smallest thing that you need to ship to test your commercial idea. There is a methodology known as the "lean start-up" methodology, where you use the least effort to create your machine learning model is deployed.

The idea is that you should build the quickest thing possible to test your market and see if your idea works. Only when you know your idea is working should you invest more time and personel in the software.

Unfortunately, there is a tension between deploying quickly and deploying a maintainable system. To build an MVP you deploy quickly, but if the system is succesful you take a 'maintenance hit' in the future because you've not invested early in the right maintainable design for your system.

You save on engineer time at the beginning, but you pay it back with high interest when you need a much higher operations load once the system is deployed.

The notion of the Sculley paper is that there are particular challenges for machine learning models around technical debt.

However, when managing systems in production, you soon discover maintenance of a rapidly deployed system is not your ownly problem. 

To deploy large and complex software systems, an engineering approach known as "separation of concerns" is taken. Frederick Brooks's book "The Mythical Man-month" [@Brooks:mythical75], has itself gained almost mythical status in the community. It focuses on what has become known as Brooks's law "adding manpower to a late software project makes it later". 

Adding people (men or women!) to a project delays it because of the communication overhead required to get people up to speed. 

To construct such complex systems an approach known as "separation of concerns" has been developed. The idea is that you architect your system, which consists of a large scale complex task, into a set of simpler tasks. Each of these tasks is separately implemented. This is known as the decomposition of the task.

This is where Jonathan Zittrain's beautifully named term "intellectual debt" rises to the fore. Separation of concerns enables the construction of a complex system. But who is concerned with the overall system?

In the worst case, technical debt manifests as an inability to *maintain* your complex software system. 

Intellectual debt is the inability to *explain* your software system. 

https://upload.sms.csx.cam.ac.uk/media/3152997

It is right their in our approach to software engineering. "Separation of concerns" means no one is concerned about the overall system itself. 

The challenge is two-fold. Firstly, we are building a very complex system, which is difficult for a single individual to understand. But secondly there is no physical manifestation of the system to inspect. Contrast this with the situation of the civil engineer building a bridge. Despite the complexity of the project, with one glance a project manager can see the project status. In manufacturing and supply chain, there is something known as a [gemba walk](https://en.wikipedia.org/wiki/Gemba), where senior staff take to the shop-floor to identify potential challenges. Senior Amazon leaders pride themselves on their gemba walks. Who is performing the software equivalent of a gemba walk?

NEED TO WATCH ZITTRAIN TALK

The general approach to large scale software infrastructure is known as  'service oriented architecture'. In a service oriented architecture each component in the decomposition of the system is assigned to a small team (typically 4-10 people). The concept of 'ownership' is important, the small team may not just design and build the service, but maintain it in production. This is an attempt to hedge against technical debt. Where it has been incurred it is ideally having to be repaid by the team that took out the loan. The team is incentivised to ensure that their service is reliable and performs to particular engineering standards (availability, latency etc). 

So far, I've just been talking about complex software systems. And these challenges certainly exist for those systems. But over time we've evolved cultures and practices around our software that have protected us against some of the worse effects. In particular agile development, pair programming, code review, test-oriented development are all mechanisms that help us quantify the quality of what we are doing and maintain standards. Regardless, in a complex legacy code base the intellectual debt is significant. The main route to dealing with it is to hope you have an old-hand Engineer, let's call her Pam, who's long-standing presence in your organisation gives them a handle on how things are constructed.

Eventually, a characteristic of the legacy system, is that changes cannot be made without running them by Pam first. Initially this isn't policy, but it becomes the de facto approach because leaders learn that if Pam doesn't approve the change then the system fails. Pam becomes a bottleneck for change, overloaded and eventually looses track where the system is. 

This does lead to technical debt, but more perniciously it leads to intellectual debt. Even if your system is functioning, you struggle to explain how and why it is working. 

This situation is not good enough, but it becomes far worse when data is involved. 

With the introduction of machine learning we see three principle effects in these complex systems.

1. Machine learning models are being deployed as regular software, this means their very existence in the complex infrastructure is not being declared. Maybe Pam knows, but she's likely too busy dealing with some other issue.

This is a challenge because the machine learning model has a sell-by date. It is trained and validated on data from a particular time period which reflects a particular snapshot of the population. In practice the statistical population will evolve, and the quality of the model with decay over time. Unless the team placed in particular infrastructure to monitor this performance loss (which they often don't, because they are under pressure to deploy). The time frame over which a model can become stale can be extremely short, because often the very deployment of a model (if done at scale) effects the dynamics of data production rendering the training data non-representative.[^closed-loop]

[^closed-loop]: I'm excited by the [EPSRC Funded Closed Loop Data Science](https://www.gla.ac.uk/schools/computing/research/researchsections/ida-section/closedloop/) project at the University of Glasgow run by Rod Murray-Smith for addressing this. 

2. In the rush to adopt "AI" and make use of machine learning technology, standard software engineering sanity checks are often suspended because people are told that 'machine learning is different'. It is indeed different, it is much worse than standard software in its potential failure modes and extra safeguards need to be put in place.

3. The individual models are sometimes difficult to interpret and there is potential for bias to enter in the modelling or from the data. Performance of these models is normally measured empirically, and is therefore driven by the 'average case'. Exceptional circumstances are often handled extremely badly. 

We are beginning to broach the subject of intellectual debt around the interpretability of individual models. And indeed, there is a field known as Fairness, Accountability and Transparency Machine learning that is looking to address these issues for single models. This is where, unfortunately, the death of the programmer enters.

By "The Death of the Programmer" we are giving a nod to ["The Death of the Author"](https://en.wikipedia.org/wiki/The_Death_of_the_Author), a literary criticism essay which argues that readers must separate a literary work from the author. That the interpretation of a work depends on the impression on the reader, rather than the intention of the author. "The Death of the Programmer" occurs in the service oriented architecture framework, because whatever the intent of the team that built and maintains each individual service, once it is deployed the service can be consumed for whichever purpose. It is beyond the control of the original programmers. This is a challenge because notions of interpretability, bias and fairness rely on context. The context is controlled by the consumer of these services not by the programmers of these services. So however well intentioned the work of ensuring fairness was in an individual model, once it is consumed the authors' best intentions can be sacrificed as the service is repurposed for a role beyond the original programmers' understanding. 

So even if we deploy a component that we consider to be fair and explainable for the role for which it was intended, but since the consumers of the service don't have access to the intent of the programmers, in practice the service will fail to be fair or explainable. 

Zittrain points out the challenge around the lack of interpretability of individual ML models as the origin of intellectual debt. And to an extent I agree, but if we understand the context and purpose of the decision making, I believe this is readily put right by the correct monitoring and retraining regime around the model. A concept I refer to as "progression testing". Indeed, the best teams do this at the moment, and their failure to do it feels more of a matter of technical debt rather than intellectual, because arguably it is a maintenance task rather than an explanation task. After all, we have good statistical tools for interpreting individual models and decisions when we have the context. We can linearise around the operating point, we can perform counterfactual tests on the model. We can build empirical validation sets that explore fairness or accuracy of the model.

So this is where, my understanding of intellectual debt in ML systems departs, I believe from John Zittrain's. The long term challenge is *not* in the individual model. We have excellent statistical tools for validating what any individual model, the long term challenge is the complex interaction between different components in the decomposed system, where the original intent of each component has been forgotten (except perhaps by Pam) and each service has been repurposed.

So, how to address these challenges? With collaborators I've been working towards a solution that contains broadly two parts. The first part is what we refer to as "Data Oriented Architectures". It aims to address the rats nest that is the current interaction between the services in a service oriented architecture. It does this by introducing data oriented programming. The data oriented programming language tracks the movement of data between each service. 

Service oriented programming style is a necessary, but not sufficient approach to data oriented programming. Data oriented programming is not only about the individual services, but how they are connected. Which service is calling which and where the flow of the data through the system occurs. 

If each service has its inputs and outputs declared on a wider ecosystem, then we can programmatically determine which inputs effect which decisions. This programmatic discovery is vital because as systems are built compositionally, the actual inputs that affect a final decision may not be known to any of the software engineers who are maintaining the system (except perhaps Pam). 

At Amazon my team built a *data oriented programming* language which is now available through BSD license. [The language is called Milan](https://tborchertblog.wordpress.com/2020/02/13/28/). Quoting from Tom Borchert's blog on Milan:

>Milan has three components:
>
>    A general purpose stream algebra that encodes relationships between data streams (the Milan Intermediate Language or Milan IL)
>    A Scala library for building programs in that algebra.
>    A compiler that takes programs expressed in Milan IL and produces a Flink application that executes the program.
>
>Component (2) can be extended to support interfaces in additional languages, and component (3) can be extended to support additional runtime targets. Considering just the multiple interfaces and the multiple runtimes, Milan looks a lot like the much more mature Apache Beam. The difference lies in (1), Milan’s general purpose stream algebra.

It is through the general purpose stream algebra that we hope to make significant inroads on the intellectual debt challenge.

The stream algebra defines the relationship between different machine learning components in the wider softare architecture. Composition of multiple services cannot occur without a signature existing within the stream algebra. The Milan IL becomes the key information structure that is required to reason about the wider software system.

This deals with the challenges that arise through the death of the programmer because we can now see the context around each service. This allows us to design the relevant validation checks to ensure that accuracy and fairness are maintained. By recompiling the algebra to focus on a particular decision within the system we can also derive new statistical tests to validate performance. These are the checks that we refer to as progression testing. The loss of programmer control means that we can no longer rely on software tests written at design time, we must have the capability to deploy new (statistical) tests after deployment as the uses to which each service is placed extend to previously unenvisaged domains.

Importantly, Milan does not place onerous constraints on the builders of individual machine learning models. Standard modelling frameworks can be used. The main constraint is that any code that is not visible to the ecosystem does not maintain or store global state. This conditon implies that the parameters of any machine learning model need to also be declared as an input to the model within the Milan IL. 

This now relates to the increased regulatory powers that have been handed to OfCom. Shortly after the 2016 US election Mark Zuckerberg was quoted as saying ["To think it influenced the election in any way is a pretty crazy idea"](https://www.cnet.com/news/facebook-mark-zuckerberg-fake-news-affect-election-techonomy-donald-trump-crazy/). He has since revisited that conclusion. But was it a conspiracy when he suggested that it hadn't happened. A conspiracy we could deal with. The deeper and more real problem is that Zuckerberg's lack of understanding was due to the significant intellectual debt integrated into his vast software ecosystem. It took a further 10 months for [Facebook to acknowledge](https://www.theguardian.com/technology/2017/sep/27/mark-zuckerberg-facebook-2016-election-fake-news) the presence and influence of a coordinated Russian-based influence operation had infiltrated the site.

The key question here is, if Facebook can't understand when their own systems are under attack, then how can OfCom, the UK regulator expect to be able to understand when Facebook's systems are breaking UK law?

The second connection in 

An intermediate language such as Milan's could offer an opening for regulatory oversight. By providing the data architecture from 


has occured, we can simply compile the relevant parts of the stream algebra to inform us what 

This difference is important, because it is this intermediate language, in the form of a stream algebra, that encodes the vital information about how data is flowing through the ecosystem. From this algerbra ...


Emukit
NMC and Muddy Waters

https://www.bbc.co.uk/sounds/play/m000f76k at 17 minutes 26 second

\include{talk-macros.tex}

https://medium.com/berkman-klein-center/from-technical-debt-to-intellectual-debt-in-ai-e05ac56a502c

https://www.cnbc.com/2019/11/11/goldman-sachs-to-reevaluate-apple-card-credit-limits-after-bias-claim.html
\thanks

\references






