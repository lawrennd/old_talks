---
title: "Open Challenges for Automated Machine Learning: Solving Intellectual Debt with AutoAI"
abstract: Machine learning models are deployed as part of wider systems where outputs of one model are consumed by other models. This composite structure for machine learning systems is the dominant approach for deploying artificial intelligence. Such deployed systems can be complex to understand, they bring with them intellectual debt. In this talk we'll argue that the next frontier for automated machine learning is to move to automation of the systems design, going from AutoML to AutoAI.
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Cambridge
  twitter: lawrennd
  url: http://inverseprobability.com
date: 2020-07-18
venue: ICML Workshop on Automated Machine Learning
transition: None
---

\include{../talk-macros.gpp}

\section{AI via ML Systems}

\subsection{Alexa}

\centerdiv{\tomTaylorPicture{15%}\joeWalowskiPicture{15%}\rohitPrasad{15%}}
\includeyoutube{VQVZ2hvNVfo}{600}{450}

\subsection{Alexa}

\centerdiv{\tomTaylorPicture{15%}\joeWalowskiPicture{15%}\rohitPrasad{15%}}
\figure{\includediagram{\diagramsDir/software/alexa-schematic}{40%}}{Simple schmeatic of a intelligent agent set of components.}{alexa-schematic}

\subsection{Speech to Text}

\centerdiv{\catherineBreslinPicture{15%}}

\subsection{Cloud Service: Knowledge Base}

\centerdiv{\davidHardcastlePicture{15%}\arpitMittalPicture{15%}\christosChristodoulopoulosPicture{15%}}

\subsection{Text to Speech}

\centerdiv{\andyBreenPicture{15%}\robertoBarraChicotePicture{15%}}

\subsection{Prime Air}

\centerdiv{\gurKimchiPicture{15%}\paulViolaPicture{15%}\davidMoroPicture{15%}}

\includeyoutube{3HJtmx5f1Fc}{600}{450} 

\include{_uq/includes/emulation.md}


\subsection{Supply Chain Optimization}

\centerdiv{\llewMasonPicture{15%}\deveshMishraPicture{15%}}

\figure{\includeyoutube{ncwsr1Of6Cw}{600}{450}}{Promotional video for the Amazon supply chain optimization team.}{scot-promo-video}

\subsection{Supply Chain Optimization}

\centerdiv{\llewMasonPicture{15%}\deveshMishraPicture{15%}}

\figure{\includediagram{\diagramsDir/software/buying-schematic}{40%}}{A schematic of a typical buying system for supply chain.}{buying-schematic}


\subsection{Forecasting}

\centerdiv{\jennyFreshwaterPicture{15%}\pingXuPicture{15%}\deanFosterPicture{15%}}

\subsection{Inventory and Buying}

\centerdiv{\deepakBhatiaPicture{15%}\piyushSaraogiPicture{15%}\ramanIyerPicture{15%}\salalHumairPicture{15%}\narayanVenkatasubramanyanPicture{15%}}

\subsection{Service Oriented Architecture}

\centerdiv{\charlieBellPicture{15%}\peterVosshallPicture{15%}}

\figure{\includediagram{\diagramsDir/ai/ml-system-monolith-purchasing}{60%}}{A potential path of models in a machine learning system.}{ml-system-monolith}

\subsection{Service Oriented Architecture}

\centerdiv{\charlieBellPicture{15%}\peterVosshallPicture{15%}}

\figure{\includediagram{\diagramsDir/ai/ml-system-downstream-purchasing000}{60%}}{A potential path of models in a machine learning system.}{ml-system-downstream-purchasing}


\section{Intellectual Debt}

\subsection{Separation of Concerns}

\centerdiv{\daveClarkPicture{15%}\nevenaLalicPicture{15%}}


\section{Data Science Africa}

\include{_data-science/includes/crop-monitoring.md}
\include{_data-science/includes/biosurveillance.md}
\include{_data-science/includes/community-radio.md}
\include{_data-science/includes/kudu-project.md}
\include{_data-science/includes/safe-boda.md}


\section{AutoAI}


\include{_uq/includes/deep-emulation.md}



<!-- \include{_data-science/includes/milan.md} -->
<!-- \include{_uq/includes/emukit-software.md} -->

\newslide{Conclusion}

* For deployed ML, worrying about a single ML component isn't good enough.
* Real world systems involve interaction of components
* Leads to intellectual debt
* Need for sophisticated emulation techniques for making deployment scalable.

\thanks

