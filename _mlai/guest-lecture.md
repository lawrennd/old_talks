---
layout: lectures
title: "Naive Days"
subtitle: "Challenges Before the AI Revolution Arrives"
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Cambridge
  twitter: lawrennd
  url: http://inverseprobability.com
venue: University of Sheffield
date: 2019-12-02
abstract: >
transition: None
---

\include{../talk-macros.tex}

\include{_data-science/includes/lies-damned-lies.md}
\include{_ml/includes/ml-to-deep-learning.md}
\include{_ml/includes/what-is-ml-end-to-end.md}
\include{_ai/includes/amazon-delivery-drone.md}
\include{_supply-chain/includes/ml-and-supply-chain.md}
\include{_supply-chain/includes/supply-chain-motto.md}
\include{_supply-chain/includes/supply-chain.md}
\include{_ai/includes/safe-boda.md}
\include{_data-science/includes/data-science-africa.md}
\include{_health/includes/malaria-gp.md}
\include{_ml/includes/ml-deployment-challenge.md}

\subsection{Conclusions}

\notes{The real challenges of machine learning are not in the models that we create but in the data and decision making ecosystems we intend to deploy. We can never do without fundamentals, but when you move from the academic into the applied be careful not to ignore the importance of good software engineering and data infrastructure. 

As well as the ideas we've mentioned today, other areas of importance are data quality (see e.g. @Lawrence:drl17) and data rights (see Guardian article on \addguardian{Data Trusts}{https://www.theguardian.com/media-network/2016/jun/03/data-trusts-privacy-fears-feudalism-democracy} and @Delacroix:trusts19).

Physically engineered systems (such as the Amazon drone) can be easier to work on and deploy because you control the entire information pipeline. When integrating new models in a continuous deployment environment separation of concerns can mean that no single individual is concerned for the whole system.}

\slides{* Challenge is in data and model ecosystem.
* Also problems of 
    * data quality (see e.g. @Lawrence:drl17) and 
	* data sharing (article on \addguardian{Data Trusts}{https://www.theguardian.com/media-network/2016/jun/03/data-trusts-privacy-fears-feudalism-democracy} and @Delacroix:trusts19)
* Physical systems can be easier to deploy becaue they're contained.
}

\thanks

\references
