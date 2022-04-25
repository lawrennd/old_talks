---
title: "Understanding Artificial Intelligence"
abstract: |
  Though artificial intelligence is ubiquitous in our homes and
  workplaces, there is widespread misunderstanding of what it really
  is. Join Neil Lawrence, DeepMind Professor of Machine Learning at
  the University of Cambridge, as he encourages us to reframe our view
  of AI.

  Neil will discuss how the artificial systems we have developed
  operate in a fundamentally different way to our own intelligence. He
  will describe how this difference in operational capability leads us
  to misunderstand the influence that decisions made by machine
  intelligence are having on our lives. Without this understanding we
  cannot take back control of those decisions from the machine.
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Cambridge
  twitter: lawrennd
  url: http://inverseprobability.com
date: 2022-06-07
venue: "Bristol Data and AI Showcase"
transition: None
---
 

\notes{\section{Introduction}

\notes{\include{_ai/includes/henry-ford-intro.md}}
\include{_ai/includes/cambridge-personal-history.md}

\newslide

\notes{The key idea I want to communicate next is related to our ability to share our thoughts.}

\include{_ai/includes/the-diving-bell-butterfly.md}

\include{_ai/includes/jean-dominique-bauby.md}

\newslide

\figure{\columns{\aligncenter{\includejpg{\diagramsDir/ai/Jean-Dominique_Bauby}{100%}}}{\aligncenter{\includejpg{\diagramsDir/ClaudeShannon_MFO3807}{70%}}}}{Claude Shannon developed information theory which allows us to quantify how much Bauby can communicate. This allows us to compare how locked in he is to us.}{bauby-shannon}

\include{_ai/includes/embodiment-factors-short.md}

\include{_ai/includes/heider-simmel.md}
\include{_ai/includes/conversation.md}
\include{_ai/includes/conversation-computer.md}

\newslide

\figure{\includediagramclass{\diagramsDir/ai/anne-imagine-ai}{50%}}{Our tendency to anthrox means that even when an intelligence is very different from ours we tend to embody it and represent it as having objectives similar to human.}{anne-imageine-ai}

\newslide

\figure{\includediagramclass{\diagramsDir/ai/anne-imagine-god}{50%}}{Our tendency to anthrox means that even when an intelligence is very different from ours we tend to embody it and represent it as having objectives similar to human.}{anne-imageine-god}

\include{_data-science/includes/evolved-relationship.md}

\newslide

\notes{
\subsection{Fairness in Decision Making}}

\notes{As a more general example, let's consider fairness in decision making. Computers make decisions on the basis of our data, how can we have confidence in those decisions?}

\newslide{}

\figure{\includepng{\diagramsDir/data-science/convention-108-coe}{70%}}{The convention for the protection of individuals with regard to the processing of personal data was opened for signature on 28th January 1981. It was the first legally binding international instrument in the field of data protection.}{convention-108-coe}

\notes{\include{_governance/includes/gdpr-overview.md}}

\notes{The GDPR gives us some indications of the aspects we might consider when judging whether or not a decision is "fair".}

\notes{But when considering fairness, it seems that there's two forms that we might consider.}

\notes{\include{_ai/includes/p-n-fairness.md}}

\newslide

\slides{\figure{\includediagramclass{\diagramsDir/ai/n-p-fairness}{80%}}{We seem to have two different aspects to fairness, which in practice can be in tension.}{n-p-fairness}}

\notes{\include{_ai/includes/reflexive-reflective.md}}

\newslide

$$\text{reflect} \Longleftrightarrow \text{reflex}$$

\newslide

\slides{\aligncenter{The Great AI Fallacy}}

\notes{\include{_ai/includes/the-great-ai-fallacy.md}}

\notes{In large part, these challenges associated with AI are because AI has no understanding of the human condition. But there's also a problem that we don't have an intuitive understanding of AI and how it is working.}

\notes{The marvellous resolution does not apply to machine driven decisions, because we *don't* have an intuitive understanding of what motivates the machine.}

\newslide

\aligncenter{If AI isn't a tool for us, then we are the tool of AI.}

\notes{The consequence is that the AI, driven by it's detailed knowledge of who we are, arising from its access to large quantities of our data, can undermine the delicate balance of our decision-making, and replace our objectives with it's own simplistic ideas of how things should be.}

\notes{So, what are the resolutions for this problem? At Cambridge we are focussed on three different interventions.}

\notes{The first example is empowering those who want to use AI through *education* and tool development. The [Accelerate Programme for Scientific Discovery](https://acceleratescience.github.io/index.html), sponsored by Schmidt Futures, focusses on empowering scientists and other domains across the University with the tools and understanding they need to make use of AI in practice.}

\notes{\include{_accelerate/includes/accelerate-programme.md}}

\newslide{Accelerate Program: Empower the User}

\slides{\figure{\includepng{\diagramsDir/accelerate/accelerate-website}{70%}}{The Accelerate Programme for Scientific Discovery covers research, education and training, engagement. Our aim is to bring about a step change in scientific discovery through AI. <http://acceleratescience.github.io>}{accelerate-website}
}

\newslide


\notes{Other examples of this form of work include our collaboration with [Data Science Africa](http://www.datascienceafrica.org/), which focusses on empowering individuals with solutions for solving challenges that emerge in the African context.}

\newslide{AutoAI: Resolve Intellectual Debt}

\figure{\includepng{\diagramsDir/ai/autoai-project-page}{60%}}{Address challenges in the way that complex software systems involving machine learning components are constructed to deal with the challenge of Intellectual Debt.}{autoai-project-page}

\notes{\include{_ai/includes/turing-ai-fellowship-intro.md}}


\notes{A second intervention is dealing with the complexity of the software systems that underpin modern AI solutions. Even if two individuals, say African masters students, who are technically capable and have an interesting idea, deploy their idea. One challenge they face is the operational load in *maintaining* and *explaining* their software systems. The challenge of *maintaining* is known as intellectual debt [@Sculley:debt15], the problem of *explaining* is known as [intellectual debt](https://medium.com/berkman-klein-center/from-technical-debt-to-intellectual-debt-in-ai-e05ac56a502c).}

\notes{The [AutoAI project](https://mlatcl.github.io/projects/autoai.html), sponsored by an ATI Senior AI Fellowship addresses this challenge.}

\subsection{Data Trusts: Empower People through their Data}

\figure{\includepng{\diagramsDir/governance/data-trusts-initiative-project-page}{60%}}{The Data Trusts Initiative (\href{https://datatrusts.uk/}{http://datatrusts.uk}) hosts blog posts helping build understanding of data trusts and supports research and pilot projects.}{data-trusts-initiative-website}

\notes{The third intervention goes direct to the source of the machine's power. What we are seeing is an emergent *[digital oligarchy](https://www.theguardian.com/media-network/2015/mar/05/digital-oligarchy-algorithms-personal-data)* based on the power that comes with aggregation of data. [Data Trusts](https://www.theguardian.com/media-network/2016/jun/03/data-trusts-privacy-fears-feudalism-democracy) are form of data intermediary designed to reutrn the power associated with this data accumulation to the originators of the data, that is us.}

\notes{\include{_governance/includes/data-trusts.md}}

\include{_ai/includes/ai-at-cam.md}
\include{_ai/includes/reclaiming-control-conclusions.md}
 
\thanks

\references


\comment{Start with some of the explanation of the difference between artificial and human intelligence. (With Pepper and Nao at the front to illustrate anthropomorphism.) 

The embodiment factor – we represent an all-seeing, all-knowing God as a bearded, robed character. We represent AI as the Terminator. But these are completely ‘other’ intelligence and neither is embodied in that way. We do so because of our human tendency to anthropomorphise, but doing that with machines is problematic. If you try and interact in a human way with an artificial intelligence, that’s how you lose control.
Pepper and Nao can communicate as one, and as one with the internet, whereas we are restricted. That goes to the heart of the theme. 
Differences between human and machine decision-making
1 Fairness
Re human decision-making, there’s 2 types of fairness. Performative fairness (procedural fairness) is if we all understand and engage with these rules to do this thing, it will lead to this expected outcome. Normative fairness (substantive fairness) is where we take the individual with all their human experience into account. It’s a quite different intention. And normative fairness can be abused, while performative fairness can simply embed existing unfairness. So no decision should ever be based purely on one form of fairness. 
One requires simplicity because it requires everyone to be engaged and to understand what to do to get a desired outcome. The other requires nuance. There are tensions between the two approaches and these can be resolved if a human is involved in the decision making. But it’s much harder to employ a machine to make that kind of nuanced decision-making because what is it going to take into account when making the decision? We are unable to replace humans with machines to do that. 
Not only the difference between thinking speed (faster in humans) and communication speed (much, much lower in humans), but also the fact that while humans model other humans in their head, adapting their communication to that model when they communicate, computers’ intelligence is based upon large amounts of data. Humans are bad at large data, but good with other humans. Computers are very good with large data, but bad with humans. So when we are interacting with computers it is very important to remember that they are not another human. 
2 Differences in computation and communication capacities
Computers don’t understand us because we are not yet capable of designing things that understand our moods. And humans empathise in order to communicate. Computers don’t. As humans, we anthropomorphise – whether it’s our cats, our dogs, or our cars. We give them all human characteristics in an effort to understand them. Our computers are very different: their computation is being based on very large amounts of data. Our fears around AI are being based on this anthopomorphism. We fear we are creating a better version of us – something with the same motivations as ourselves, only more powerful, because it has additional capabilities. But we are not. 
The real danger is a very different one – it’s that those computers do not anthropomorphise us. They work below our cognitive radar, they make decisions about us without understanding the human condition. Artificial intelligence is artificial in the way a plastic plant is artificial. It has some aspects of real intelligence, but it is constructed in a very different way. There are real dangers with AI as there are with any new technology. But if we are to face those dangers head-on as a society, we need to understand what we are dealing with.
The AI fallacy, that AI will adapt to us. It won’t.
The great AI fallacy is that we are building the first wave of automation that will adapt to us, instead of expecting us to adapt to it. If you look historically, all our automation has required humans to accommodate it: roads now prioritise cars over people, we’ve had to build railways for trains, factories require us to turn up on time to operate machines. One thing that’s common to almost everything that’s written about AI in public, is the idea that because AI is “intelligent”, it is going to be accommodating us in ways other automation hasn’t. I just don’t think that that is true and I see no evidence for it. Indeed, it seems more like everything is still going in the opposite direction. The way that AI is employed, we are having to adapt to it rather than it adapting to us. 
So what do we do about this? We intervene.
Examples of interventions
1) Bring Diana Robinson in here to talk about her work on human-machine interfaces.
Her work is on helping doctors to use machine-derived data in what they’re doing and helping them understand what the machine is doing. Removing uncertainty: i.e. looking at how a machine can represent its uncertainty in a way that a doctor can assimilate it. 
2) The need to view AI as a tool and bring in Sarah Morgan to talk about Accelerate.
If you don’t understand AI as a tool and can’t wield it yourself for it to do things for you, then it is doing things to you, or using your data and if you don’t understand the ways in which that is happening, then that is problematic. 
Because AI is a tool, that’s why we have the Accelerate Programme which is equipping scientists to use machine learning techniques. Sarah Morgan – substantive vs procedural fairness. When computer does give a decision, if you don’t understand basis of decision making, you can’t negotiate with it. Set Sarah up to talk about what she does. (Computer says no.)
We need better understanding and more interventions to prevent existing problems… People deploy systems that operate in ways that are far more complex than they understand. For example, Facebook didn’t understand the extent of interference in the election of Donald Trump, and Mark Zuckerberg said it was a crazy idea that the Russians would influence the election. They then found out several months later that yes, they had influenced the election. 
Illustrations of the use and misuse of data leads us on to consider why we should be much more careful about the use of our personal data and how much of it we give away.
Our views about machines taking over from us reflect our own lack of understanding of what is really going on. The more immediate problem is taking back control of our data, and then further on thinking more about how the machines see us and what we need to do to help that understanding and making sure AI does accommodate us if we understand better to what AI really is. 
Example of intervention around use of data: the Data Trusts Initiative 
The new pilot projects show how some community groups are using a data trust to give their communities/groups more control over their data: Brixham and deprivation being an example. Coastal communities are deprived communities, but deprived in a different way than an inner-city area like Rotherham. So interventions to help them need to be different, the idea of a ‘one size fits all’ intervention doesn’t work. Data from the Brixham community could help inform that intervention, though it raises the question, how can a community have a say as to how that data is being used about them to set up a state-level intervention?
CONCLUSION
We are imagining enemies – but there are ones out there that we really need to be worrying about. Particularly the ones we are not really aware of, like the crimes committed in international waters where it’s far harder to say where responsibility lies. Everyone has heard about Deepwater Horizon, but not Trafigura who dumped oil off the Ivory Coast. At least with Facebook and BP those accidents were a failure of process, not a conscious transgression of law. The long-term problem is that everyone wants to talk about Google and Facebook and DeepMind and they are highly incentivised to align their activities with what the public wants. But there are lots of companies working behind the scenes that we aren’t so conscious of.
Take-home messages
If we are going to be empowered by AI, rather than ruled by it, it’s important that we have more understanding of these things. 

15 minutes for questions – could take some as we go along (gathering them via Slido), or we could leave them for the end. 

}
