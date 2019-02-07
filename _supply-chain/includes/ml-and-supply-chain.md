\ifndef{mlAndSupplyChain}
\define{mlAndSupplyChain}
\editme



\subsection{Machine Learning in Supply Chain}

\figure{
\includejpg{../slides/diagrams/supply-chain/container-2539942_1920}{70%}
\notes{\caption{The container, arguably the largest agent of social change in the last 100 years.}}
}

Containerization has had a dramatic effect on global economics, placing many people in the developing world at the end of the supply chain. 

\newslide{Wild Alaskan Cod}
\slides{
\includejpg{../slides/diagrams/supply-chain/wild-alaskan-cod}{30%}
}

\newslide{Wild Alaskan Cod}
\slides{
\includejpg{../slides/diagrams/supply-chain/wild-alaskan-cod-made-in-china}{30%}
}

\notes{
\figure{
\column{\includejpg{../slides/diagrams/supply-chain/wild-alaskan-cod}{90%}}{\includejpg{../slides/diagrams/supply-chain/wild-alaskan-cod-made-in-china}{90%}}{45%}{45%}
\caption{Wild Alaskan Cod, that is a product of China. It is cheaper to ship the deep frozen fish thousands of kilometers for processing than to process locally.}
}
}


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

\endif
