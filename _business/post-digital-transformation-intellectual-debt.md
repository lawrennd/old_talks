---
title: "Post-Digital Transformation: Intellectual Debt"
abstract: "Digital transformation has offered the promise of moving from a manual decision-making world to a world where decisions can be rational, data-driven and automated. The first step to digital transformation is mapping the world of atoms (material, customers, logistic networks) into the world of bits. But the real challenges may start once this is complete. In this talk we introduce the notion of 'post digital transformation': the challenges of doing business in a digital world."
date: 2021-05-17
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


\include{talk-macros.gpp}

\section{Introduction}

\slides{\aligncenter{\neilLawrencePicture{20%}}
\aligncenter{Neil Lawrence}
\aligncenter{Professor of Machine Learning}}

\include{_notebooks/includes/notebook-setup.md}

\include{_data-science/includes/gartner-hype-cycle-ai-bd-dm-dl-ml.md}

\include{_ml/includes/what-is-ml.md}

\include{_ai/includes/ai-vs-data-science-2.md}

\newslide{Exercise: Score Yourself (in chat)}

\slides{* I am a data science: 
1. follower (no visibility/influence)
2. some visibilty/influence
3. visibility and some influence
4. leader (lead on data and AI developments)}

\slides{\aligncenter{Discussion: to 9:30}}



\section{Intellectual Debt}

\figure{\includepng{\diagramsDir/ai/2020-02-12-intellectual-debt}{70%}}{Jonathan Zittrain's term to describe the challenges of explanation that come with AI is Intellectual Debt.}{intellectual-debt}

<!-- Embodiment Factors-->

\include{_ai/includes/embodiment-factors-celsius.md}

\include{_data-science/includes/evolved-relationship.md}
\include{_ai/includes/conversation-tedx.md}

<!-- Data Science (why it's happening) -->

\include{_data-science/includes/lies-damned-lies.md}
\include{_ai/includes/heider-simmel.md}

\include{_ai/includes/conversation-computer.md}

\include{_data-science/includes/big-data-paradox.md}
\include{_data-science/includes/big-model-paradox.md}
\include{_psychology/includes/selective-attention-bias.md}
\include{_data-science/includes/data-inattention-bias.md}
\include{_policy/includes/diane-coyle-fitzwilliam-lecture.md}

\newslide{Case Study: 10:30}

\newslide{15 Minute Break!}

\include{_policy/includes/face-masks-case-study.md}

\section{Bringing it Back}


\subsection{What we did Amazon}

\notes{Corporate culture turns out to be an important component of how you can react to digital transformation. Amazon is a company that likes to take a data driven approach. It has a corporate culture that is set up around data-driven decision making. In particular *customer obsession* and other *leadership principles* help build a cohesive approach to how data is assimilated.}

\notes{Amazon has [14 leadership principles](https://www.amazon.jobs/en/principles) in total, but two I found to be particularly useful are called *right a lot* and *dive deep*.}

\subsubsection{Are Right a Lot}

> Leaders are right a lot. They have strong judgment and good instincts. They seek diverse perspectives and work to disconfirm their beliefs.

\notes{I chose "right a lot" because of the the final sentence. Many people find this leadership princple odd because how can you be 'right a lot'. Well, I think it's less about being right, but more about how you interact with those around you. Seeking *diverse perspectives* and working to *disconfirm your beliefs*. One of my favourite aspects of Amazon was how new ideas are presented. They are presented in the form of a document that is discussed. There is a particular writing style where claims in the document need to be backed up with evidence, often in the form of data. Importantly, when these documents are produced, they are read in silence at the beginning of the meeting. When everyone has finished reading, the *most junior person* speaks first. Senior leaders speak last. This is one approach to ensuring that a diverse range of perspectives are heard. It is this sort of respect that needs to be brought to complex decisions around data.}

\subsubsection{Dive Deep}

> Leaders operate at all levels, stay connected to the details, audit frequently, and are skeptical when metrics and anecdote differ. No task is beneath them.

\notes{I chose "dive deep" because of the last phrase of the second sentence. Amazon is suggesting that leaders "are skeptical when metrics and anecdote differ". This phrase is vitally important, data inattention bias means that there's a tendency to 'miss the gorilla'. The gorilla is often your own business instinct and/or domain expertise *or* that of others. If the data you are seeing contradicts the anecdotes you are hearing, this is a clue that something may be wrong. Your data skepticism should be on *high alert*. This leadership principle is teaching us how to mediate between 'seeing the forest' and 'seeing the tree'. It warns us to look for inconsistencies between what we're hearing about the individual tree and teh wider forest.}

\notes{Understanding your own corporate culture, and what levers you have at your disposal, is a key component of bringing the right approach to data driven decision making.}

\newslide{Thoughtsday}

\slides{* Dealing with highly *operational* decision making.}

\notes{These challenges can be particularly difficult if your organisation is dominated by *operational concerns*. If rapid decision making is required, the Gorilla may be missed. And this may be mostly OK, for example, in Amazon's supply chain there are weekly business reviews that are looking at the international state of the supply chain. If there are problems, they often need quick actions to rectify them. When quick actions are required, 'command and control' tends to predominate over more collaorative decision making that we hope allows us to see the Gorilla. Unfortunately, it can be hard, even as senior leaders, to switch between this type of operational decision making, and the more inclusive decision making we need around complex data scenarios. One possibility is to reserve a day for meetings that are dealing with the more complex decision making. In Amazon later in the week was more appropriate for this type of meeting. So making, e.g. Thursday into a more thoughtful day (Thoughtsday if you will?) you can potentially switch modes of thinking and take a longer term view on a given day in the week.}

\subsection{What we did in DELVE}

\include{_delve/includes/delve-timeline.md}

\notes{Any policy question can be framed in a number of different
ways - what are the health outcomes; what is the impact on NHS
capacity; how are different groups affected; what is the economic
impact – and each has different types of evidence associated with
it. Complex and uncertain challenges require efforts to draw insights
together from across disciplines.}

\include{_policy/includes/data-as-a-convener.md}

\notes{For more on the experience of giving advice to government during a pandemic see [this talk](http://inverseprobability.com/talks/notes/science-evidence-and-government-reflections-on-the-covid-19-experience.html).}

\newslide{Breakout: What would *you* do in *your* company?}

* Finish 12:30





\subsection{Conclusion}

See the Gorilla *don't* be the Gorilla. 
\figure{\includejpg{\diagramsDir/business/gorilla-punch-mouth}{50%}}{A famous quote from Mike Tyson before his fight with Evander Holyfield: "Everyone has a plan untill they get punched in the mouth". Don't let the gorilla punch you in the mouth. See the gorilla, but don't be the gorilla. Photo credit: <https://www.catersnews.com/stories/animals/go-ape-unlucky-photographer-gets-punched-by-lairy-gorilla-drunk-from-eating-bamboo-shoots/>}{gorilla-punch-mouth}



\reading

\thanks

\refernces
