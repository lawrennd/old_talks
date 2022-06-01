---
title: "The AI Paradigm Shift: Machine Learning, Automated Decision Making and Modern Society"
abstract: |
  The term Artificial Intelligence means different things to different people, but we can distil some commonality across different expectations of the term. It seems that the word intelligence drives us to believe that this new approach to automation will be the first to adapt to us as humans rather than requiring us to adapt to it. This promise presents challenges, because machine learning technologies that underpin the revolution in artificial intelligence are not capable of adapting to humans as we are to each other. In this talk we introduce the challenges and overview the research directions we are taking to uncover the solutions.
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Cambridge
  twitter: lawrennd
  url: http://inverseprobability.com
blog: 
date: 2022-06-14
venue: "Four Seasons, Park Lane, London"
transition: None
---

\comment{The AI Fallacy ... followed by material on how to fix it.

Likely to be informed by ideas that arise in AI@Cam}

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

\aligncenter{\dianaRobinsonPicture{30%}}

\notes{In the group [Diana Robinson]() has been focussing on how we can communicate the machine's understanding of *uncertainty* to clinicians, within the context blood plasma infusions and surgical operations.}

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

\aligncenter{\sarahMorganPicture{30%}}

\notes{Sarah Morgan is one of our fellows, she'll tell us about how she makes use of the machine's capabilities in improving understanding and diagnostics of schizophrenia.}

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

