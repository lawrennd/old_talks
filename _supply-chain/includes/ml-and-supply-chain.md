\ifndef{mlAndSupplyChain}
\define{mlAndSupplyChain}

\editme

\subsection{Machine Learning in Supply Chain}

\figure{\includejpg{../slides/diagrams/supply-chain/container-2539942_1920}{70%}}{The container, arguably the largest agent of social change in the last 100 years.}{container-2539942_1920}


\notes{Containerization has had a dramatic effect on global economics, placing many people in the developing world at the end of the supply chain. }

\newslide{Wild Alaskan Cod}
\slides{
\includejpg{../slides/diagrams/supply-chain/wild-alaskan-cod}{30%}
}

\newslide{Wild Alaskan Cod}
\slides{
\includejpg{../slides/diagrams/supply-chain/wild-alaskan-cod-made-in-china}{30%}
}

\notes{
\figure{\columns{\includejpg{../slides/diagrams/supply-chain/wild-alaskan-cod}{90%}}{\includejpg{../slides/diagrams/supply-chain/wild-alaskan-cod-made-in-china}{90%}}{45%}{45%}}{Wild Alaskan Cod, that is a product of China. It is cheaper to ship the deep frozen fish thousands of kilometers for processing than to process locally.}{wild-alaskan-cod}
}

\notes{For example, you can buy Wild Alaskan Cod fished from Alaska, processed in China, sold in North America. This is driven by the low cost of transport for frozen cod vs the higher relative cost of cod processing in the US versus China. Similarly, \href{https://www.telegraph.co.uk/news/uknews/1534286/12000-mile-trip-to-have-seafood-shelled.html}{Scottish prawns are also processed in China for sale in the UK.} }

\newslide{Machine Learning in Supply Chain}
\slides{
* *Supply chain*: Large Automated Decision Making Network
* Amazon's supply chain: Possibly the world's largest 'AI'
* Major Challenge: 
    * We have a *mechanistic* understanding of supply chain.
    * Machine learning is a *data driven* technology.
}
\notes{Supply chain is a large scale automated decision making network. Our aim is to make decisions not only based on our models of customer behavior (as observed through data), but also by accounting for the structure of our fulfilment center, and delivery network.}

\notes{Many of the most important questions in supply chain take the form of counterfactuals. E.g. “What would happen if we opened a manufacturing facility in  Cambridge?” A counter factual is a question that implies a mechanistic understanding of a system. It goes beyond simple smoothness assumptions or translation invariants. It requires a physical, or *mechanistic* understanding of the supply chain network. For this reason the type of models we deploy in supply chain often involve simulations or more mechanistic understanding of the network.}

\notes{In supply chain Machine Learning alone is not enough, we need to bridge between models that contain real mechanisms and models that are entirely data driven.}

\notes{This is challenging, because as we introduce more mechanism to the models we use, it becomes harder to develop efficient algorithms to match those models to data.}

\newslide{Amazon Supply Chain Optimization}

\figure{\includeyoutube{ncwsr1Of6Cw}{100%}{auto}}{The Supply Chain Optimization Team (SCOT) at Amazon is responsible for the automated decision making in (probably) the world's largest AI.}{supply-chain-optimization-team}

\endif
