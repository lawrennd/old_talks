---
title: "Machine Learning and Emergency Medicine"
extras:
- link: https://arxiv.org/abs/1705.07996
  label: Paper on Mind and Machine Intelligence
layout: slides
author:
- given: Neil D.
  family: Lawrence
  url: http://inverseprobability.com
  institute: Amazon Cambridge and University of Sheffield
  twitter: lawrennd
  gscholar: r3SJcvoAAAAJ
  orchid: 0000-0001-9258-1030
date: 2020-01-09
venue: TERM
layout: talk
geometry: ["a4paper", "margin=2cm"]
papersize: a4paper
transition: None
categories:
- notes
---

\include{talk-macros.tex}

\section{My Background}

\notes{I'd like to start this talk by emphasizing that I don't know anything about emergency medicine, except what I picked up by cycling with a friend who works in A&E in Rotherham. 

So as far as I'm aware, all emergency medicine doctors are extremely good cyclists. 

What I do know about is deployments of machine learning, how they succeed, how they fail. Both from a manager's perspective, a domain expert's perspective and a user's perspective. For our context, let's map these people onto the senior administrator, the doctors and nurses and the patients.}

\section{Artificial Intelligence}

\notes{Let's start with the term artificial intelligence. It's an extremely emotive term because intelligence is something precious to us. It implies that the machine is encroaching on territory which we formerly thought of as our own.}

\section{Anthrox}

\notes{The emotive nature of the term is  not the only problem, the second problem with the term is anthrox. In the word anthrox the X stands for pomorphisation. So the full word is normally anthropomorphisation.

We are bandwidth limited, so when interacting with other intelligent agents, we make assumptions that they think and operate like us. That is the tendency to anthrox. The problem is pernicious because it's difficult to say, so we tend not to call it out in case our tongue trips us up. That's why we'll call it anthtrox. When communicating with humans, anthrox is a short cut to gaining a form of information coherence of what your objectives are. You can use contextual analogies to align activities. You don't need to send detailed and explicit instructions. You can rely on your team of professionals to work towards one goal, making the patient safe and comfortable. All of this is implicit in the humans around you. It cannot be taken forgranted in the computer.}

\define{\stubname}{anne-bob-conversation}
\include{_ai/includes/anne-bob-talk.md}

\notes{If you must anthrox AI, then please think of it as an extremely literal and willful friend, who ignores social cues. Is the last to remain at the party, will blurt out the most inappropriate conclusions regardless of the social context. Has an encyclopedic knowledge about things that sound irrelevant to you. 

The truth is that the current generation of artificial intelligence solutions are almost entirely based on machine learning, and machine learning is simply a combination of compute and statistics. So it will help you a great deal if whenever you see the term AI, you mentally replace it with computers and statistics. That will give you a more realistic understanding of its capabilities.}


\define{\stubname}{anne-computer-conversation}
\include{_ai/includes/anne-bob-talk.md}


\notes{A particular bias that is important is [automation bias](https://en.wikipedia.org/wiki/Automation_bias)}

\notes{I was skimming a recent nature paper about these techniques in medicine, a paper that used machine learning to classify potentially cancerous images. Throuhout the paper they refer to an 'AI system'. Whether it is conscious or not, the paper plays on our tendency to anthrox. It makes the work feel like it's doing something magical, that it relates to our intelligence. This is a particularly dangerous trap for a medical professional to fall into.}

\notes{Managers see AI as a way of improving processes and giving them more control over decision making in their organisation. People are hard to control, computers are easy to control.

Domain experts have an understanding of context of decisions, and an intuition about what the right decision might be. But they can be blind to unusual situations and overly convinced by their own expertise. 

Users are placing trust in the decision making process. They want to believe in the outcome, and like to think that it considers there personal circumstances and that it is fair in some way.}

\include{_ai/includes/newcomen-steam-engine.md}

\notes{The promise of artificial intelligence is that it is the first generation of automation that will adapt to us rather than us adapting to it. What do I mean by that? The challenges of automation are not new. In the 18th century, automation of the physical labour of pumping mines clear of water was a priority, and the steam engine was invented and evolved for that task. The challenge is that the engine is not flexible, it is designed to do one job repetitively. It is like a small baby. It needs feeding, it needs cleaning, and it has regular emissions. It has no concept of time or convenience of those that maintain it. 

Although the computer is more advanced than the steam engine in many respects, it is still utterly dependent on its human operators. For the information it gets in the form of data (the input coal) to the actions it takes in response (the operation of the mine pump). It doesn't have a contextual awareness of side effects of those decisions because they don't fall within its cognitive landscape. Just like the steam engine, it doesn't wear nappies, so any unaccounted for side effects of feeding it with data are felt by the environment.}

\newslide{}

\figure{\includejpg{../slides/diagrams/ai/person-cute-portrait-young-small-child-684477-pxhere.com}{70%}}{Machines are as helpless and unaware as small children, and less cute. Just like a small child they require us to maintain and service them.}{young-baby-image}


\include{_health/includes/doctor-and-patient.md}

\newslide{}

\figure{\includejpg{../slides/diagrams/ai/Giant_Baby_One}{70%}}{When we deploy at scale the damage done by deploying a naive machine can feel exactly like the damage done by deploying a maliscious machine.}{giant-baby-image}


\notes{The machine is also relentless, as long as it is fed, it can complete actions tirelessly, day or night.}

\notes{Having said that, it's remarkable what we're doing today with computers and statistics. And the drive for this is really the quantity of data available. In particular we have significant advances in what we might think of as tasks that traditionally needed human perception to solve. For example, object detection in images. We can now train computers to identify and highlight objects that a decade ago were only identifiable by humans.

How have we achieved this?}

\include{_ml/includes/deep-learning-overview.md}

\notes{Similar comments could be made for machine learning systems that are recognising speech (e.g. in voice assistances such as Siri, Alexa and Google Assistant). And for automated language translation. However, these systems are critically dependent on our data, on data that has been labelled by humans. They are emulating our perceptual set up through having observed lare amounts of data.}

\notes{On average we may be able to show that these machines outperform us, but this also can bring problems. It turns out to be important not just whether we are wrong, but how we are wrong.}


\include{_ai/includes/watt-steam-engine.md}

\include{_ml/includes/bias-variance-plots.md}

\notes{One of the very real problems we face at the moment is we have an ecosystem of people and companies that are delivering solutions that are not driven by the 'pain points' of our health service, not driven by getting the fundamentals right. Not driven by solutions that would make a difference for patients, doctors, nurses and administrators but driven by headlines. These are companies that are not making money from these solutions, but are engaged in a wider battle for mindshare. To give the impression that AI systems are delivering magical solutions.}

\notes{It's an intrinsic part of their agenda because in the near term this is the fastest route to large scale investment. Capturing the imagination of the public, investors, vice-presidents and CEOs is a far surer route to a billion dollar check than actually trying to build and deploy a product in such a complex ecosystem as the healthcare market.}

\notes{But we shouldn't bemoan this too much. This stage is likely inevitable, but it is unsustainable. The key question is, how do we take advantage of the excitement to deliver sustainable change that benefits all doctors?}

\notes{Many of the particular answers to this are personal, but here's a couple of ideas I think might help. Firstly, it's a learning opportunity. First, you should assimilate the skepticism, but once you've understood the very real reasons why there won't be overnight success, then you should indulge your curiousity, and allow the child in you to emerge. There are fascinating technologies emerging, and the current excitement means there will be more opportunities to learn about these technologies and inspire you to think about how they might make your life easier. But then you need to take off the rose-tinted spectacles and examine how such technologies might be making a difference in your particular A&E. How does this neural network change the life of the metal worker from Rotherham with a steel splint in her eye? Because if that question isn't being asked, then the applicability of the technology is not being considered. The benefit may of course be indirect, but if it is not eventually felt by patients in some way then the utility is questionable.}

\notes{Secondly, to deploy any of these systems you will find that the main barriers are in your existing processes. A classic mistake is to believe that you can bring in an advanced machine learning technique and deploy it within your hospital environment, when the reality is that the machine will face all the challenges you face and more. In particular, given that the machine is making decisions on the basis of data that you provide, how does it get access to that data? How do you ensure that the data is of sufficient quality and consistency for the machine to make a high quality decision? How do you ensure that patient privacy is respected in the processing of that data, and that the decision isn't biased to favour a particular group? As you face the reality of the deployment you're considering you'll find that the real challenges are the very poor quality of existing processes. Improving those processes will improve outcome even if you do not integrate and deploy an AI system. Making your department 'AI ready' is far more work than building the machine learning model.}

\notes{An excellent way of considering these two challenges can be done today, without major AI expertise. If you have an idea for how AI can help you in your job, here's my suggestion. Go back to your department and mock-it-up. Whatever decision the AI is going to take can be first taken by a human. Decide what information that human will have available. Choose something where the human is going to make a decision quickly on the basis of only the information they have in front of them. The decision should be one that can take less than a second. Now install that human in your decision making pipeline. How is that decision going to be presented to patients, nurses and doctors? What does the interface look like? Remember, you don't get to ask the decision maker to contextualise it, you need to be able to take the decision at face value and integrate it into your existing processes.}

\notes{I suspect there are very few areas where this can be usefully done in an exising A&E department. Why aren't there more? Because currently most of the processes rely on human flexibility and ability to contextualise. They are poorly documented, and in many cases deliberately obscured in an effort to protect individual domains. The very excercise of understanding why these decisions are difficult to make can be helpful in improving processes in any organisation, and I suspect A&E departments in hospitals are no different.}

\notes{It's equivalent to turning up in a 16th century farm with an internal combustion engine. At that time in the UK^[farm] 58% of the labour force worked in agriculture, today 1.2% of the labour force are in agriculture. But the only people who are empowered to make this change are the domain experts. The people in this room.

[farm]: https://ourworldindata.org/employment-in-agriculture

}

\include{_health/includes/black-box-thinking.md}
\include{_ai/includes/rebel-ideas.md}


\thanks

\references
