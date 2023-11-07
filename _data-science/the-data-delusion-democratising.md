---
layout: slides
title: The Data Delusion
subtitle: Challenges for Democratising Deep Learning
abstract: >
  The widespread success of deep learning in a variety of domains is
  being hailed as a new revolution in artificial intelligence. It has
  taken 20 years to go from defeating Kasparov at Chess to Lee Sedol
  at Go. But what have the real advances been across this time? The
  fundamental change has been in terms of data availability and
  compute availability. The underlying technology has not changed much
  in the last 20 years. So what does that mean for areas like medicine
  and health? Significant challenges remain, improving the data
  efficiency of these algorithms and retaining the balance between
  individual privacy and predictive power of the models. In this talk
  we will review these challenges and propose some ways forward. 
  
  Bio: Neil Lawrence is a Professor of Machine Learning and
  Computational Biology at the University of Sheffield. His main
  research interest is machine learning through probabilistic
  models. He focuses on both the algorithmic side of these models and
  their application.  He has a particular focus on applications in
  personalized health and applications in the developing world. He is
  well known for his work with Gaussian processes, and has proposed
  Gaussian process variants of many of the succesful deep learning
  architectures. He is highly active in the machine learning
  community, most recently Program Chairing the NIPS conference in
  2014 and General Chairing (alongside Corinna Cortes) in 2015.
extras:
- link: https://arxiv.org/abs/1705.07996
  label: Paper on Mind and Machine Intelligence
pptx: True
reveal: False
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: Amazon Cambridge and University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
date: 2016-09-22
venue: Rework Deep Learning Summit, London, UK
transition: None
---

\include{talk-macros.tex}

\define{\newslide{text}}{---}
\newslide{}

\div{\includediagram{\diagramsDir/data-science/hilbert-info-growth}}{}{text-align:center}

\include{_data-science/includes/newcomen-engine.md}

\newslide{}

\div{\includediagram{\diagramsDir/data-science/uk_tin_coal_railways001}}{}{text-align:center}

\newslide{}

\div{\includediagram{\diagramsDir/data-science/uk_tin_coal_railways002}}{}{text-align:center}

\newslide{}

\div{\includediagram{\diagramsDir/data-science/uk_tin_coal_railways003}}{}{text-align:center}

\newslide{}

\include{_health/includes/doctor-and-patient.md}

\newslide{}

\div{\includeimg{\diagramsDir/Watt7783.png}{}{negate}}{}{height:600px;text-align:center}
@Uglow:lunar02


\newslide{}

\div{\includeimg{\diagramsDir/SteamEngine_Boulton&Watt_1784.png}{}{negate}}{}{height:600px;text-align:center}

\include{_ml/includes/deep-learning-overview.md}

\newslide{}
 
<!--<span class="fragment fade-in">-->
\div{\includediagram{\diagramsDir/data-science/user-centric-data}}{}{text-align:center}
<!--</span>-->


\include{_health/includes/deep-health-model.md}

\newslide{}

\div{\includediagram{\diagramsDir/data-science/uk_tin_coal_railways004}}{}{text-align:center}

\newslide{}

\div{\includediagram{\diagramsDir/data-science/uk_tin_coal_railways005}}{}{text-align:center}

\define{\newslide{text}}{### \text}

\newslide{Thank you!}

<center>Neil Lawrence</center>
<center>[http://inverseprobability.com](http://inverseprobability.com/blog.html)</center>
<center>\@lawrennd</center>

\newslide{References}
