---
title: Where Next for AI?
venue: CWTech AI Conference
date: 2017-10-02
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: Amazon Cambridge and University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
transition: None
incremental: True
---

\include{_data-science/includes/gartner-hype-cycle-ai-bd-dl.md}

\newslide{What about IoT?}

\include{_ai/includes/gartner-hype-cycle-bd-iot.md}

\newslide{Background: Big Data}

* The pervasiveness of data brings forward particular challenges.
* Emerging themes: Devolving compute onto device. 
* Data preprocessing: Internet of Intelligence.

\include{_ai/includes/embodiment-factors.md}
\include{_data-science/includes/evolved-relationship.md}



\newslide{Effects}

* This phenomenon has already revolutionised biology.
* Large scale data acquisition and distribution.
* What does it mean for IoT

\newslide{Internet of People}

* Fog computing: barrier between cloud and device blurring.
* Stuxnet: Adversarial and Security implications for intelligent systems.
* Complex feedback between algorithm and implementation
  
\newslide{Challenges}

1. Paradoxes of the Data Society
2. Quantifying the Value of Data
3. Privacy, loss of control, marginalisation

\include{_data-science/includes/value-of-data.md}

\newslide{Quantifying the Value of Data}

There's a sea of data, but most of it is undrinkable

\includejpg{\diagramsDir/sea-water-ocean-waves}

We require data-desalination before it can be consumed!


\newslide{Data --- Quotes from NeurIPS 2017 Workshop on ML for Healthcare}

* 90% of our time is spent on validation and integration (Leo Anthony Celi)
* "The Dirty Work We Don't Want to Think About" (Eric Xing)
* "Voodoo to get it decompressed" (Francisco Giminez)
* In health care clinicians collect the data and often control the direction of research through guardianship of data.

\newslide{Value}

* How do we measure value in the data economy?
* How do we encourage data workers: curation and management
    * Incentivization for sharing and production.
    * Quantifying the value in the contribution of *each actor*.


\newslide{Embodiment: Data Readiness Levels}

* Three Bands of Data Readiness:

* Band C - accessibility
* Band B - validity
* Band A - usability


\newslide{Accessibility: Band C}

* Hearsay data.
* Availability, is it actually being recorded?
* privacy or legal constraints on the accessibility of the recorded data, have ethical constraints been alleviated?
* Format: log books, PDF ...
* limitations on access due to topology (e.g. it's distributed across a number of devices)

\newslide{Validity: Band B}

*  faithfulness and representation
* visualisations.
* noise characterisation.
* Missing values.
* Example, was a column or columns accidentally perturbed (e.g. through a sort operation that missed one or more columns)? Or was a [gene name accidentally converted to a date](http://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-5-80)?

\newslide{Usability: Band A}

* The usability of data
* Band A is about data in context.
* Consider appropriateness of a given data set to answer a particular
question or to be subject to a particular analysis.

\newslide{Recursive Effects}

* Band A may also require
    * active collection of new data. 
    * annotation of data by human experts
    * revisiting the collection (and running through the appropriate stages again)

\newslide{Also ...}

* Encourage greater interaction between application domains and data scientists

* Encourage *visualization* of data

* Incentivise the delivery of data.

\newslide{See Also ...}

* Data Joel Tests proposal by Damon Civin (ARM)


\newslide{Privacy, Loss of Control and Marginalization}

* Society is becoming harder to monitor

* Individual is becoming easier to monitor

\newslide{Discrimination}

* Marketing can become more sinister when the target of the marketing is well understood and the (digital) environment of the target is also so well controlled

* Potential for explicit and implicit discrimination on the basis of race, religion, sexuality, health status

* All prohibited under European law, but can pass unawares, or be implicit


\newslide{Marginalization}

* Credit scoring, insurance, medical treatment
* What if certain sectors of society are under-represented in our aanalysis?
* What if Silicon Valley develops everything for us?

\newslide{Digital Revolution and Inequality?}

<img src="\writeDiagramsDir/woman-tends-house-in-village-of-uganda-africa.jpg" width="50%" style="border:none">

\newslide{Amelioration}

* Work to ensure individual retains control of their own data
* We accept privacy in our real lives, need to accept it in our digital
* Control of persona and ability to project

* Need better technological solutions: trust and algorithms.

\include{../_ai/includes/ml-systems-design.md}

\newslide{Conclusion}

* Data science offers a great deal of promise for personalized health
* There are challenges and pitfalls
* It is incumbent on us to avoid them

**Many solutions rely on education and awareness**

* There are particular challenges around the Internet of Intelligence. 

\thanks

\references
