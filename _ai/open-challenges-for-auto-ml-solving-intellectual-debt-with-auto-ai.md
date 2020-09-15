---
title: "Open Challenges for Automated Machine Learning: Solving Intellectual Debt with AutoAI"
abstract: Machine learning models are deployed as part of wider systems where outputs of one model are consumed by other models. This composite structure for machine learning systems is the dominant approach for deploying artificial intelligence. Such deployed systems can be complex to understand, they bring with them intellectual debt. In this talk we'll argue that the next frontier for automated machine learning is to move to automation of the systems design, going from AutoML to AutoAI.
layout: talk
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

\slides{\section{AI via ML Systems}

\include{_ai/includes/alexa-system.md}
\include{_ai/includes/prime-air-system.md}
\include{_uq/includes/emulation.md}
\include{_ai/includes/supply-chain-system.md}
\include{_ai/includes/aws-soa.md}


\section{Intellectual Debt}

\subsection{Separation of Concerns}

\centerdiv{\circleHead{\diagramsDir/people/dave-clark.png}{Dave Clark}{15%}{https://www.linkedin.com/in/dave-clark-3a82684/}\circleHead{\diagramsDir/people/nevena-lalic.png}{Nevena Lalic}{15%}{https://www.linkedin.com/in/nevena-lalic-65561b53/}}


\include{_ai/includes/dsa-systems.md}
\section{AutoAI}


\include{_uq/includes/deep-emulation.md}



<!-- \include{_data-science/includes/milan.md} -->
<!-- \include{_uq/includes/emukit-software.md} -->

\newslide{Conclusion}

* For deployed ML, worrying about a single ML component isn't good enough.
* Real world systems involve interaction of components
* Leads to intellectual debt
* Need for sophisticated emulation techniques for making deployment scalable.
}

\thanks

