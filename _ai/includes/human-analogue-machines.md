\ifndef{humanAnalogueMachines}
\define{humanAnalogueMachines}

\editme

\include{_simulation/includes/the-moniac.md}
\include{_ai/includes/donald-mackay-brain.md}

\subsection{Human Analogue Machine}

\notes{The machine learning systems we have built today that can reconstruct human text, or human classification of images, necessarily must have some aspects to them that are analagous to our understanding. As MacKay suggests the brain is neither a digital or an analogue computer, and the same can be said of the modern neural network systems that are being tagged as "artificial intelligence".}

\notes{I believe a better term for them is "human-analogue machines", because what we have built is not a system that can make intelligent decisions from first principles (a rational approach) but one that observes how humans have made decisions through our data and reconstructs that process. Machine learning is more empiricist than rational, but now we n empirical approach that distils our evolved intelligence.}

\figure{\includepng{\diagramsDir/ai/human-analogue-machine}{60%}}{The human analogue machine creates a feature space which is analagous to that we use to reason, one way of doing this is to have a machine attempt to compress all human generated text in an auto-regressive manner.}{human-analogue-machine}

\slides{* A human-analogue machine is a machine that has created a feature space that is analagous to the "feature space" our brain uses to reason.

* The latest generation of LLMs are exhibiting this charateristic, giving them ability to converse.}

\reading{@Lawrence-atomic24}{Chapter 11}

\newslide{Counterfeit People}

\notes{The perils of developing this capability include counterfeit people, a notion that the philosopher [Daniel Dennett has described in *The Atlantic*](https://www.theatlantic.com/technology/archive/2023/05/problem-counterfeit-people/674075/). This is where computers can represent themselves as human and fool people into doing things on that basis.}

\slides{* Perils of this include *counterfeit people*.
* Daniel Dennett has described the challenges these bring in [an article in The Atlantic](https://www.theatlantic.com/technology/archive/2023/05/problem-counterfeit-people/674075/).}

\newslide{Psychological Representation of the Machine}

\slides{* But if correctly done, the machine can be appropriately "psychologically represented"

* This might allow us to deal with the challenge of *intellectual debt* where we create machines we cannot explain.}

\notes{\include{_ai/includes/intellectual-debt-blog-post.md}}

\notes{But if we can avoid the pitfalls of counterfeit people, this also offers us an opportunity to *psychologically represent* [@Heider:interpersonal58] the machine in a manner where humans can communicate without special training. This in turn offers the opportunity to overcome the challenge of *intellectual debt*.}

\notes{Despite the lack of interpretability of machine learning models, they allow us access to what the machine is doing in a way that bypasses many of the traditional techniques developed in statistics. But understanding this new route for access is a major new challenge.}

\newslide{}

\figure{\includediagram{\diagramsDir/data-science/new-flow-of-information004}{70%}}{The trinity of human, data, and computer, and highlights the modern phenomenon. The communication channel between computer and data now has an extremely high bandwidth. The channel between human and computer and the channel between data and human is narrow. New direction of information flow, information is reaching us mediated by the computer. The focus on classical statistics reflected the importance of the direct communication between human and data. The modern challenges of data science emerge when that relationship is being mediated by the machine.}{new-flow-of-information-4}

\newslide{}

\figure{\includediagram{\diagramsDir/data-science/new-flow-of-information-ham}{70%}}{The HAM now sits between us and the traditional digital computer.}{new-flow-of-information-ham}


\include{_ai/includes/human-computers-interacting.md}


\endif
