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

\include{talk-macros.gpp}


\include{_ai/includes/the-great-ai-fallacy.md}

\subsection{The News}

\figure{\includepng{\diagramsDir/ai/2020-02-12-today-programme}{70%}}{Three news items from the Today programme seemed to combine on Wednesday for me.}{today-programme}

\notes{I was woken up on Wednesday morning with three news headlines that don't
seem connected. But I'd like to connect them today. The connections I'll
draw go to the heart of fundamental challenges we'll face with our
artificial intelligence solutions.

The first headline was about the national census, Sir Ian Diamond, the
UK's National Statistician, [suggested that the next national census
might be our last](https://www.bbc.co.uk/news/uk-51468919).

The second headline was about the OfCom, the UK's national regulator of
telecommunications being granted more powers to [more powers to control
content on social
media](https://www.bbc.co.uk/news/technology-51446665).

The third headline was about the short-selling (you can listen
[here](https://www.bbc.co.uk/sounds/play/m000f76k), go to 17 minutes 26
second). Carson Block, a US-based short-selling firm raised questions
over asset values. In the interview, Carson referred to the difference
between accounting practices that are illegal versus those that
misrepresent the financial health of a company. Since the collapse of
BHS, Patisserie Valerie and Carillion auditing practices have come under
scrutiny.

How are these three items connected? Well, my argument in this talk is
that they are each part of wider phenomena which when combined will form
a perfect storm for "artificial intelligence" technologies. My further
claim would be that the Cambridge Analytica scandal and challenges with
election manipulation are just the leading edge of this storm.

To weather the challenges we face, we need far more interaction across
academic sub-disciplines, policy and industry. Helping to facilitate
that is my main aim in moving to Cambridge, and I'm excited about the
opportunities that this University and this city offer for delivering on
that vision.}


\notes{These challenges are multi-faceted, but today I want to focus on the
primary challenge which unites these three news headlines. I was
struggling for a term for it, until a couple of weeks back when I was
sharing a coffee with Bill Thompson. Those that know Bill will
understand that he is a Cambridge institution, and a font of wisdom and
knowledge on all things technical. I was describing the challenge and
Bill said: this sounds like Jonathan Zittrain's notion of Intellectual
Debt.

Zittrain [gave the Tanner lectures at Clare Hall last
month](https://upload.sms.csx.cam.ac.uk/media/3152997), which I'm very
disappointed I missed. Because the challenges he's highlighting are
exactly those that my research is designed to address.

So, what is intellectual debt?}

\include{_ai/includes/intellectual-debt.md}

\subsection{Virtual Gemba Walks}

\notes{The challenge is two-fold. Firstly, we are building a very complex
system, which is difficult for a single individual to understand. But
secondly there is no physical manifestation of the system to inspect.

Contrast this with the situation of the civil engineer building a
bridge. Despite the complexity of the project, with one glance a project
manager can see the project status. In manufacturing and supply chain,
there is something known as a [gemba
walk](https://en.wikipedia.org/wiki/Gemba), where senior staff take to
the shop-floor to identify potential challenges. Senior Amazon leaders
pride themselves on their gemba walks. Who is performing the software
equivalent of a gemba walk?

Such a physical manifestation can be extremely important for
co-ordination across teams because it represents a consistent and
observable object that can be directly observed by all engineers.}

\subsection{Service-oriented Architecture}

\notes{The general approach to large scale software infrastructure is known as
'service-oriented architecture'. In a service-oriented architecture each
component in the decomposition of the system is assigned to a small team
(typically 4-10 people). The concept of 'ownership' is important, the
small team may not just design and build the service but maintain it in
production. This is an attempt to hedge against technical debt. Where it
has been incurred it is ideally having to be repaid by the team that
took out the loan. The team is incentivized to ensure that their service
is reliable and performs to particular engineering standards
(availability, latency etc).}

\subsection{Test-oriented Software}

\notes{So far, I've just been talking about complex software systems. And these
challenges certainly exist for those systems. But over time we've
evolved cultures and practices around our software that have protected
us against some of the worse effects. In particular agile development,
pair programming, code review, test-oriented development are all
mechanisms that help us quantify the quality of what we are doing and
maintain standards. Regardless, in a complex legacy code base the
intellectual debt is significant. The main route to dealing with it is
to hope you have an old-hand Engineer, let's call him Lancelot, whose
long-standing presence in your organisation gives them a handle on how
things are constructed.}

\include{_software/includes/lancelot.md}
\include{_ai/includes/data-and-intellectual-debt.md}

\include{_ml/includes/the-death-of-the-programmer.md}
\include{_ai/includes/fit-systems.md}
\include{_data-science/includes/data-oriented-architectures-short.md}
\include{_data-science/includes/milan.md}

\section{News}

\subsection{OfCom}

\notes{This now relates to the increased regulatory powers that have been
handed to OfCom. Shortly after the 2016 US election Mark Zuckerberg was
quoted as saying ["To think it influenced the election in any way is a
pretty crazy
idea"](https://www.cnet.com/news/facebook-mark-zuckerberg-fake-news-affect-election-techonomy-donald-trump-crazy/).
He has since revisited that conclusion. But was it a conspiracy when he
suggested that it hadn't happened? A conspiracy we could deal with. The
deeper and more real problem is that Zuckerberg's lack of understanding
was due to the significant *intellectual debt* integrated into his vast
software ecosystem. It took a further 10 months for [Facebook to
acknowledge](https://www.theguardian.com/technology/2017/sep/27/mark-zuckerberg-facebook-2016-election-fake-news)
the presence and influence of a coordinated Russian-based influence
operation had infiltrated the site.

The key question here is, if Facebook can't understand when their own
systems are under attack, then how can OfCom, the UK regulator expect to
be able to understand when Facebook's systems are breaking UK law?

The Milan IL may well provide the answer. If we can standardize around a
limited number of formalisms for expressing the data flow in an algebra,
then we can automate the deployment of systems that validate the
conformance of the decision-making system to standards dictated by
OfCom. This could even be done in an automated algorithmic way without
revealing proprietary knowledge of the underlying infrastructure.}

\subsection{The Census and the Big Data Paradox}

\notes{What's this got to do with the census? As far as I understood the story,
Sir Ian was suggesting that the next census might be the last, because
in future we could obtain all the information we need through other
data.

I find this worrying, because intellectual debt has manifested across
society. In a phenomenon I've previously called the "Big Data Paradox"
which, simply put, that as we measure more about society we understand
less.

Examples include our inability to predict elections and referenda
through polls and the challenges of developing personalized medicines to
deal with particular diseases.

There's a common phrase "Can't see the wood for the trees", meaning that
we don't see the overall structure of the forest due to our obsession
with an individual tree. Classical statistics has historically allowed
us to characterize the forest. It allows us to see beyond the trees and
see the entire wood. Classical statistics is underpinned by the
randomized control trial, but unfortunately a correctly designed trial
can be expensive. Data science has emerged as a field focussed on what I
call *happenstance* data. Data which was not collected for the purpose
to which it is being used. A particular problem is that the provenance
of that data is not understood, including any biases. Whoever collected
the data was not a statistician, if anything they are more likely to be
a programmer. But we see the same phenomenon emerging in that the
individual is losing control of the purpose to which the data is being
put.

This is separation of concerns occurring, potentially, across entities,
individuals even societies. Our only ability to sanity-check ourselves
is to run the equivalent of progression tests. And without a model of
the data provenance, such as is partially provided by the Milan IL, the
only way we can do this is with a large-scale end-to-end A/B test.

Within companies that have sufficient customer or product bases that
remains the gold standard by which release is judged, because despite
the lack of understanding of the individual components of the system, a
randomized trial of the entire pipeline can often be undertaken. What
Sir Ian is suggesting is tantamount to removing our capability to run
such a validation test across our society.

The advent of AI is not going to eliminate our need to do statistical
studies, it will increase it. Famously, Xerox PARC considered the advent
of the computer as the dawn of the paperless office, because documents
could be stored electronically. In reality, the invention of the
computer has caused more paper than ever to be used in our offices.

In a similar way, we can expect a much-increased demand for statistical
validation of our decision making. We should not be looking to eliminate
such studies, because a rigorous statistical control is our only
protection against the Big Data Paradox which in reality is the
society-wide manifestation of Intellectual Debt.}

\subsection{Accounting}

\notes{Against this background is a depressing warning from the professional
auditors. Accounting was perhaps the first profession to take data
quality seriously. Principally because there is a direct equivalence
between data and money. What Carson Block was suggesting in his today
program interview was that the challenge in accounting was not breaking
of the law but bending of the law in ways that misrepresented the
underlying health of a company.

This situation appears to have emerged through a too-cosy relationship
between the large auditing firms and their clients, driven by the common
practice of large auditors also providing lucrative consulting services.

Most companies have been persuaded (often by the consulting arms of
these accounting firms) that they need to digitally transform, to move
their entire decision making and data process into large warehouses.
However, without the underpinning data-oriented architectures these
firms are borrowing from their intellectual futures by doing so. The
post-digital transformation challenges will take the form of paying back
that intellectual debt. The accounting scandals provide us with the
starkest reminders. If we cannot trust a vital profession to properly
explain what is occurring in some of our largest firms and how it
effects their financial health, in a domain where the data quality is
high, how do we expect to build systems that properly explain the nature
of automated data decision making systems that will take place in these
companies.}

\section{Conclusion}
\slides{
* AI Fallacy incorrectly suggests machines will adapt to us.
* Reality is a greater need for explanation of decision making.
* Roadmap to address this challenge involves:
  * The Milan IL Algebra
  * Meta modelling with e.g. Emukit
  }

\notes{The great AI fallacy suggests that the new wave of automation is the
first generation of automation where machines will adapt to us, rather
than us adapting to them. The reality is stark, without significant
changes to our best practices around designing and deploying these
systems, not only will they not accommodate our needs properly, but they
will be unable to explain the complex decisions they are being made.
Rather than being enslaved by super-intelligence, we are heading for a
world where we are enslaved by super-ignorance.

We proposed a roadmap to addressing these problems that begins with the
notion of data-oriented architectures and ends with the use of meta
modelling for deploying the necessary progression tests.}

\thanks







