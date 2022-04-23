---
title: "Post-Digital Transformation, Decision Making and Intellectual Debt"
abstract: |
  Digital transformation has offered the promise of moving from a
  manual decision-making world to a world where decisions can be
  rational, data-driven and automated. The first step to digital
  transformation is mapping the world of atoms (material, customers,
  logistic networks) into the world of bits.

  I’ll discuss how the artificial systems we have developed operate
  in a fundamentally different way to our own intelligence. I’ll
  describe how this difference in operational capability leads us to
  misunderstand the influence the nature of decisions made by machine
  intelligence.

  Developing this understanding is important in integrating human
  decisions with those from the machine. These ideas are designed to
  help with the challenge of 'post digital transformation': doing
  business in a digital world.
date: 2022-04-26
pptx: False
potx: ../_includes/judge-reference.potx
docx: False
pdfnotes: False
ipynb: True
author:
- given: Neil D.
  family: Lawrence
  url: http://inverseprobability.com
  institute: University of Cambridge
  twitter: lawrennd
  gscholar: r3SJcvoAAAAJ
  orcid: 
venue: Cambridge Senior Management Programme, Judge Business School, University of Cambridge
transition: None
---

\section{Introduction}

\slides{\aligncenter{\neilLawrencePicture{20%}}
\aligncenter{Neil Lawrence}
\aligncenter{Professor of Machine Learning}}

\subsection{Pre-Read Material}

\notes{Please watch [this excerpt](https://www.youtube.com/watch?v=ubq3ayuG2EY) from the Lex Friedman podcast, interviewing with the roboticist Rodney Brooks. Please read this [blog post by Jonathan Zittrain on Intellectual Debt](https://medium.com/berkman-klein-center/from-technical-debt-to-intellectual-debt-in-ai-e05ac56a502c).}

\notes{For the facemasks case study read the summary of [this report on facemasks](https://rs-delve.github.io/reports/2020/05/04/face-masks-for-the-general-public.html) and the responses [from scientists to the report](https://www.sciencemediacentre.org/expert-reaction-to-review-of-evidence-on-face-masks-and-face-coverings-by-the-royal-society-delve-initiative/).}


\include{_notebooks/includes/notebook-setup.md}

\include{_data-science/includes/gartner-hype-cycle-ai-bd-dm-dl-ml.md}

\include{_ml/includes/what-is-ml.md}

\include{_ai/includes/ai-vs-data-science-2.md}

\newslide{Exercise: Score Yourself}

\slides{* I am a data science: 
1. follower (no visibility/influence)
2. some visibilty/influence
3. visibility and some influence
4. leader (lead on data and AI developments)}

\slides{\aligncenter{Discussion: to 14:15}}

\section{Embodiment and Intellectual Debt}

\include{_ai/includes/sistine-terminator-images.md}

<!-- Embodiment Factors -->

\include{_ai/includes/embodiment-factors-celsius.md}

\include{_ai/includes/conversation-tedx.md}

<!-- Data Science (why it's happening) -->

\include{_data-science/includes/lies-damned-lies.md}
\include{_ai/includes/heider-simmel.md}
\include{_ai/includes/conversation-computer.md}
\include{_data-science/includes/evolved-relationship.md}

\newslide

\figure{\includediagramclass{\diagramsDir/ai/anne-imagine-ai}{50%}}{Our tendency to anthrox means that even when an intelligence is very different from ours we tend to embody it and represent it as having objectives similar to human.}{anne-imageine-ai}

\newslide

\figure{\includediagramclass{\diagramsDir/ai/anne-imagine-god}{50%}}{Our tendency to anthrox means that even when an intelligence is very different from ours we tend to embody it and represent it as having objectives similar to human.}{anne-imageine-god}

\include{_ai/includes/intellectual-debt-blog-post.md}

\notes{\subsection{Fairness in Decision Making}}

\notes{As a more general example, let's consider fairness in decision making. Computers make decisions on the basis of our data, how can we have confidence in those decisions?}

\newslide{}


\include{_governance/includes/gdpr-overview.md}

\notes{The GDPR gives us some indications of the aspects we might consider when judging whether or not a decision is "fair".}

\notes{But when considering fairness, it seems that there's two forms that we might consider.}

\include{_ai/includes/p-n-fairness.md}

\include{_ai/includes/reflexive-reflective.md}


\include{_data-science/includes/big-data-paradox.md}
\include{_data-science/includes/big-model-paradox.md}
\include{_psychology/includes/selective-attention-bias.md}
\include{_data-science/includes/data-inattention-bias.md}
\include{_policy/includes/diane-coyle-fitzwilliam-lecture.md}

\newslide{Case Study: 15:00}

\newslide{15 Minute Break!}

\include{_policy/includes/face-masks-case-study.md}

\section{Bringing it Back}

\include{_business/includes/dealing-with-intellectual-debt.md}

\newslide{Breakout: What would *you* do in *your* company?}

* Finish 16:30

\include{_business/includes/gorilla-conclusion.md}

\reading

\thanks

\references
