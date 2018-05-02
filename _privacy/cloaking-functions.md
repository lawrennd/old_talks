---
layout: slides
title:  "Cloaking Functions: Differential Privacy with Gaussian Processes"
author: >
  Neil D. Lawrence
  with **Michael T. Smith**, Max Zwiessele and Mauricio Alvarez
abstract: > 
  Processing of personally sensitive information should respect an individual's
  privacy. One promising framework is Differential Privacy (DP). In this talk
  I'll present work led by Michael Smith at the University of Sheffield on the
  use of cloaking functions to make Gaussian process (GP) predictions
  differentially private. Gaussian process models are flexible models with
  particular advantages in handling missing and noisy data. Our hope is that
  advances in DP for GPs will make it easier to 'learn without looking', i.e.
  gain the advantages of prediction from patient data without impinging on
  their privacy.

  Joint work with **Michael T. Smith**, Max Zwiessele and Mauricio Alvarez
date: 2017-08-30
affiliation: Amazon and University of Sheffield
transition: None
---


####  Cloaking Functions: Differential Privacy with Gaussian Processes  
#### 2017-08-30
#### Neil D. Lawrence
#### with **Michael T. Smith**, Max Zwiessele and Mauricio Alvarez
#### Amazon and University of Sheffield
```@lawrennd``` [inverseprobability.com](http://inverseprobability.com)
[Paper on Arxiv](https://arxiv.org/pdf/1606.00720.pdf)
<!--  pandoc -s -S -c talks.css -t revealjs --mathjax="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" -o 2017-08-30-cloaking-functions.slides.html 2017-08-30-cloaking-functions.md
-->

\include{../talk-macros.tex}

\include{_ai/includes/embodiment-factors.md}
\include{_data-science/includes/evolved-relationship.md}
\include{_ai/includes/conversation-technical.md}
\include{_gp/includes/gp-book.md}
\include{_gp/includes/gp-intro-very-short.md}
\include{_privacy/includes/differential-privacy-for-gps.md}
\include{_privacy/includes/differential-privacy-with-cloaking.md}


###  Conclusions {data-background="../slides/diagrams/pres_bg.png"}

* **Summary** We have developed an improved method for performing
differentially private regression.

* **Future work** Multiple outputs, GP classification, DP Optimising
hyperparameters, Making the inputs private.

* **Thanks** Funders: EPSRC; Colleagues: **Michael T. Smith**, Mauricio, Max.

* **Recruiting** Deep Probabilistic Models: 2 year postdoc ([tinyurl.com/shefpostdoc](http://tinyurl.com/shefpostdoc))


###  {.allowframebreaks data-background="../slides/diagrams/pres_bg.png"}

* [**The go-to book on differential privacy, by Dwork and Roth;**\
]{style="margin-left:-50px;"} Dwork, Cynthia, and Aaron Roth. "The
algorithmic foundations of differential privacy." Theoretical Computer
Science 9.3-4 (2013): 211-407.
[link](https://www.cis.upenn.edu/~aaroth/Papers/privacybook.pdf)

* [**Original basis of applying DP to GPs;**\
]{style="margin-left:-50px;"} Hall, Rob, Alessandro Rinaldo, and Larry
Wasserman. "Differential privacy for functions and functional data." The
Journal of Machine Learning Research 14.1 (2013): 703-727.
[link](http://www.stat.cmu.edu/~arinaldo/papers/hall13a.pdf)


* [**Articles about the Massachusetts privacy debate**\
]{style="margin-left:-50px;"} Barth-Jones, Daniel C.
"The 're-identification' of Governor William Weld's medical information: a
critical re-examination of health data identification risks and privacy
protections, then and now." Then and Now (June 4, 2012) (2012).
[link](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2076397)


* Ohm, Paul. "Broken promises of privacy: Responding to the surprising
failure of anonymization." UCLA Law Review 57 (2010): 1701.
[link](https://epic.org/privacy/reidentification/ohm_article.pdf)

* Narayanan, Arvind, and Edward W. Felten. "No silver bullet:
De-identification still doesn’t work." White Paper (2014).
[link](http://randomwalker.info/publications/no-silver-bullet-de-identification.pdf)

* Howell, N. Data from a partial census of the !kung san, dobe. 1967-1969.
<https://public.tableau.com/profile/john.marriott\#!/vizhome/kung-san/Attributes>, 1967.

* **Images used:** BostonGlobe: [Mass
Mutual](https://c.o0bg.com/rf/image_960w/Boston/2011-2020/2015/05/29/BostonGlobe.com/Business/Images/MassMutual_04.jpg),
[Weld](https://c.o0bg.com/rf/image_960w/Boston/2011-2020/2014/10/20/BostonGlobe.com/Metro/Images/Gov.%20Bill%20Weld%201-100425.jpg).
Harvard: [Sweeney](http://www.gov.harvard.edu/files/Sweeney6crop.jpg).
Rich on flickr: [Sheffield
skyline](https://www.flickr.com/photos/rich_b1982/13114665103/in/pool-sheffieldskyline/).




