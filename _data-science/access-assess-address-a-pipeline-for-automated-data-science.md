---
title: "Access, Assess and Address: A Pipeline for (Automated?) Data Science"
abstract: |
  Data Science is an emerging discipline that is being promoted as a universal panacea for the world’s desire to make better informed decisions based on the wealth of data that is available in our modern interconnected society. In practice data science projects often find it difficult to deliver. In this talk we will review efforts to drive data informed in real world examples, e.g., the UK’s early Covid19 pandemic response. We will introduce a framework for categorising the stages and challenges of the data science pipeline and relate it to the challenges we see when giving data driven answers to real world questions. We will speculate on where automation may be able to help but emphasise that automation in this landscape is challenging when so many issues remain for getting humans to do the job well.
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Cambridge
  twitter: lawrennd
  url: http://inverseprobability.com
blog: 
date: 2021-09-17
venue: "ECML Workshop on Automating Data Science"
transition: None
---


\include{_data-science/includes/lies-damned-lies.md}

\newslide{DELVE}

\figure{\includepng{\diagramsDir/delve/rs-delve-announcement}{70%}}{The Royal Society announces the DELVE group to tackle the COVID-19 crisis. <https://royalsociety.org/news/2020/04/royal-society-convenes-data-analytics-group-to-tackle-COVID-19/>.}{delve-announcement}


\notes{\include{_delve/includes/delve-overview.md}}

\subsection{What is Machine Learning?}

$$ \text{data} + \text{model} \stackrel{\text{compute}}{\rightarrow} \text{prediction}$$


\include{_data-science/includes/big-data-paradox.md}
\include{_data-science/includes/big-model-paradox.md}
\include{_policy/includes/diane-coyle-fitzwilliam-lecture.md}

\include{_policy/includes/data-as-a-convener.md}

\section{Delve}

\include{_delve/includes/delve-report-list.md}

\notes{There is lots of hope for the role data science and AI could play, but we’re still a way off from being AI-ready. Further attention is needed on some of the foundational issues around data use – access, skills, culture – before we can begin to talk in earnest about deploying AI. [link here to data readiness]}

\include{_delve/includes/delve-data-report.md}

\notes{\include{_delve/includes/data-report-recommendations.md}}

\notes{Delivering a rapid response requires the ability to quickly convene teams from across disciplines (and often institutions) around a key question. To facilitate this, we also used ideas from \addblog{open data science}{2014/07/01/open-data-science} to facilitate communication and understanding.}

\include{_data-science/includes/access-assess-address.md}

\subsection{Conclusions}

\slides{* Bandwidth constraints of humans
* Big Data Paradox
* Big Model Paradox
* Access, Assess, Address
}


\notes{The particular circumstances of the Covid-19 pandemic have highlighted the challenges of integrating scientific ideas to answer policy questions. In this talk, we've given a formal introduction to the problem, the difficulty of communicating between individuals (particularly from different domains) and reviewed the ideas and solutions we used in the Delve initiative.}

\notes{Recommendations from the DELVE Data report suggest that more effort needs to be placed into working in this manner in normal circumstances, so that when an emergency occurs we are better prepared to deal with the questions we face.}

\notes{Stepping back from these recommendations, we've introduced the "Access, Assess, Address" three stage framework for the data science process. Access is about getting hold of the data, bringing it into the digital machines. Assess is about reusable work we can do on the data before we pose a question about the data. For example, data schema, characterising the missing values, looking for corrupted entries, ensuring that the number of data hasn't saturated the excel row limit or that a gene name hasn't been converted to a date. Finally, the *address* stage is about addressing the statistical question or machine learning prediction we require from the data.

When it comes to the automation process, we can see three areas where we need progress. Access to data itself often requires manual intervention. Even downloading a CSV file may require a password. Building eacosystems of data exchange is vital for automating this step. For assessment we already have work from e.g. the AIDA team at the Alan Turing Institute, automated type detection, the automatic statistician @@Valera-automatic17;@Lloyd-automatic14
then finally we have AutoML.}

\thanks

\references
