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
date: 2020-03-09
venue: BBC Lectures on ML
transition: None
---

talk-macros.gpp}lk-macros.gpp}


talk-macros.gpp}i/includes/the-great-ai-fallacy.md}

\subsection{The News}

\figure{\includepng{\diagramsDir/ai/2020-02-12-today-programme}{70%}}{Three news items from the Today programme seemed to combine on Wednesday for me.}{today-programme}

\section{Intellectual Debt}

\figure{\includepng{\diagramsDir/ai/2020-02-12-intellectual-debt}{70%}}{Jonathan Zittrain's term to describe the challenges of explanation that come with AI is Intellectual Debt.}{intellectual-debt}


\newslide{Technical Debt}

\subsection{Lean Startup Methodology}

\includes{_software/includes/mythical-man-month.md}

\figure{\includejpg{\diagramsDir/ai/Mythical_man-month_(book_cover)}{40%}}{The Mythical Man-month [@Brooks:mythical75] is a 1975 book focussed on the challenges of software project coordination.}{intellectual-debt}

\subsection{Separation of Concerns}

\newslide{Intellectual Debt}

-   Technical debt is the inability to *maintain* your complex software
    system.

-   Intellectual debt is the inability to *explain* your software
    system.


\subsection{Virtual Gemba Walks}

\subsection{Service-oriented Architecture}


\subsection{Test-oriented Software}


\subsection{Adding Data}

1.  ML Models deployed as 'regular software'
2.  Sanity checks are being suspended
3.  Models are driven by "average case"

\subsection{The Death of the Programmer}

\figure{\includejpg{\diagramsDir/ai/lemortedarthur}{40%}}{Malory's book "Le Morte d'Arthur. A guide to team building in the age of chivalry.}{arthur-book}

\subsection{Lancelot}

\figure{\includepng{\diagramsDir/ai/Lancelot_fighting_the_dragons_of_the_Val_without_return}{60%}}{Lancelot quashing another software issue. Lancelot was Arthur's most trusted knight. In the software ecosystem the Lancelot figure is an old-hand software engineer who comes closest to having the full system overview. }{lancelot-software}



\subsection{FIT Models to FIT Systems}


\subsection{Data-oriented Architectures}

\subsection{Milan}
\slides{
1.  A general-purpose stream algebra that encodes relationships between
      data streams (the Milan Intermediate Language or Milan IL)

2.  A Scala library for building programs in that algebra.

3.  A compiler that takes programs expressed in Milan IL and produces a
     Flink application that executes the program.
}


\subsection{Context}


\subsection{Stateless Services}


\subsection{Meta Modelling}

\figure{\includepng{\diagramsDir/uq/emukit-software-page}{80%}}{The Emukit software is a set of software tools for emulation and surrogate modeling. <https://amzn.github.io/emukit/>}{emukit-software-page}


\section{News}

\subsection{OfCom}

\subsection{The Census and the Big Data Paradox}


\subsection{Accounting}

\section{Conclusion}
\slides{
* AI Fallacy incorrectly suggests machines will adapt to us.
* Reality is a greater need for explanation of decision making.
* Roadmap to address this challenge involves:
  * The Milan IL Algebra
  * Meta modelling with e.g. Emukit
  }


\thanks







