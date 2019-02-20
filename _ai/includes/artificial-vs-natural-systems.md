\ifndef{naturalVsArtificialSystems}
\define{naturalVsArtificialSystems}
\editme

\subsection{Artificial vs Natural Systems}
\slides{
* Consider natural intelligence, or natural *systems*
* Contrast between an artificial *system* and an natural system.
* The key difference between the two is that artificial systems are *designed* whereas natural systems are *evolved*.
}

\notes{Let’s take a step back from artificial intelligence, and consider natural intelligence. Or even more generally, let’s consider the contrast between an artificial *system* and an natural system. The key difference between the two is that artificial systems are *designed* whereas natural systems are *evolved*.}


\newslide{Natural Systems are Evolved}
\slides{
> Survival of the fittest
> 
> ?
}

\notes{Systems design is a major component of all Engineering disciplines. The details differ, but there is a single common theme: achieve your objective with the minimal use of resources to do the job. That provides efficiency. The engineering designer imagines a solution that requires the minimal set of components to achieve the result. A water pump has one route through the pump. That minimises the number of components needed. Redundancy is introduced only in safety critical systems, such as aircraft control systems. Students of biology, however, will be aware that in nature system-redundancy is everywhere. Redundancy leads to robustness. For an organism to survive in an evolving environment it must first be robust, then it can consider how to be efficient. Indeed, organisms that evolve to be too efficient at a particular task, like those that occupy a niche environment, are particularly vulnerable to extinction.}

\notes{This notion is akin to the idea that only the best will survive, popularly encoded into an notion of evolution by Herbert Spencer's quote.}

\newslide{Natural Systems are Evolved}

> Survival of the fittest
>
> [Herbet Spencer](https://en.wikipedia.org/wiki/Herbert_Spencer), 1864

\notes{Darwin himself never said "Survival of the Fittest" he talked about evolution by natural selection.}


\newslide{Natural Systems are Evolved}

> Non-survival of the non-fit
> 
> 

\notes{Evolution is better described as "non-survival of the non-fit". You don't have to be the fittest to survive, you just need to avoid the pitfalls of life. This is the first priority.}

\notes{So it is with natural vs artificial intelligences. Any natural intelligence that was not robust to changes in its external environment would not survive, and therefore not reproduce. In contrast the artificial intelligences we produce are designed to be efficient at one specific task: control, computation, playing chess. They are *fragile*.}

\newslide{Mistake we Make}
\slides{
* Equate fitness for objective function.
* Assume static environment and known objective. 
}

\notes{A mistake we make in the design of our systems is to equate fitness with the objective function, and to assume it is known and static. In practice, a real environment would have an evolving fitness function which would be unknown at any given time.}

\addblog{On Natural and Artificial Intelligence}{2018/02/06/natural-and-artificial-intelligence}.

\notes{The first criterion of a natural intelligence is *don’t fail*, not because it has a will or intent of its own, but because if it had failed it wouldn’t have stood the test of time. It would no longer exist. In contrast, the mantra for artificial systems is to be more efficient. Our artificial systems are often given a single objective (in machine learning it is encoded in a mathematical function) and they aim to achieve that objective efficiently. These are different characteristics. Even if we wanted to incorporate *don’t fail* in some form, it is difficult to design for. To design for “don’t fail”, you have to consider every which way in which things can go wrong, if you miss one you fail. These cases are sometimes called corner cases. But in a real, uncontrolled environment, almost everything is a corner. It is difficult to imagine everything that can happen. This is why most of our automated systems operate in controlled environments, for example in a factory, or on a set of rails. Deploying automated systems in an uncontrolled environment requires a different approach to systems design. One that accounts for uncertainty in the environment and is robust to unforeseen circumstances. }

\notes{The systems we produce today only work well when their tasks are pigeonholed, bounded in some way. To achieve robust artificial intelligences we need new approaches to both the design of the individual components, and the combination of components within our AI systems. We need to deal with uncertainty and increase robustness. Today, it is easy to make a fool of an artificial intelligent agent, technology needs to address the challenge of the uncertain environment to achieve robust intelligences.}

\notes{However, even if we find technological solutions for these challenges, it may be that the essence of human intelligence remains out of reach. It may be that the most quintessential element of our intelligence is defined by limitations. Limitations that computers have never experienced.}

\ifndef{embodimentFactors}
\notes{Claude Shannon developed the idea of information theory: the mathematics of information. He defined the amount of information we gain when we learn the result of a coin toss as a “bit” of information. A typical computer can communicate with another computer with a billion bits of information per second. Equivalent to a billion coin tosses per second. So how does this compare to us? Well, we can also estimate the amount of information in the English language. Shannon estimated that the average English word contains around 12 bits of information, twelve coin tosses, this means our verbal communication rates are only around the order of tens to hundreds of bits per second. Computers communicate tens of millions of times faster than us, in relative terms we are constrained to a bit of pocket money, while computers are corporate billionaires.}
\endif

\notes{Our intelligence is not an island, it interacts, it infers the goals or intent of others, it predicts our own actions and how we will respond to others. We are social animals, and together we form a communal intelligence that characterises our species. For intelligence to be communal, our ideas to be shared somehow. We need to overcome this bandwidth limitation. The ability to share and collaborate, despite such constrained ability to communicate, characterises us. We must intellectually commune with one another. We cannot communicate all of what we saw, or the details of how we are about to react. Instead, we need a shared understanding. One that allows us to infer each other’s intent through context and a common sense of humanity. This characteristic is so strong that we anthropomorphise any object with which we interact. We apply moods to our cars, our cats, our environment. We seed the weather, volcanoes, trees with intent. Our desire to communicate renders us intellectually animist.}
	
\notes{But our limited bandwidth doesn’t constrain us in our imaginations. Our consciousness, our sense of self, allows us to play out different scenarios. To internally observe how our self interacts with others. To learn from an internal simulation of the wider world. Empathy allows us to understand others’ likely responses without having the full detail of their mental state. We can infer their perspective. Self-awareness also allows us to understand our own likely future responses, to look forward in time, play out a scenario. Our brains contain a sense of self and a sense of others. Because our communication cannot be complete it is both contextual and cultural. When driving a car in the UK a flash of the lights at a junction concedes the right of way and invites another road user to proceed, whereas in Italy, the same flash asserts the right of way and warns another road user to remain.}

\notes{Our main intelligence is our social intelligence, intelligence that is dedicated to overcoming our bandwidth limitation. We are individually complex, but as a society we rely on shared behaviours and oversimplification of our selves to remain coherent. }

\notes{This nugget of our intelligence seems impossible for a computer to recreate directly, because it is a consequence of our evolutionary history. The computer, on the other hand, was born into a world of data, of high bandwidth communication. It was not there through the genesis of our minds and the cognitive compromises we made are lost to time. To be a truly human intelligence you need to have shared that journey with us. }

\notes{Of course, none of this prevents us emulating those aspects of human intelligence that we observe in humans. We can form those emulations based on data. But even if an artificial intelligence can emulate humans to a high degree of accuracy it is a different type of intelligence. It is not constrained in the way human intelligence is. You may ask does it matter? Well, it is certainly important to us in many domains that there’s a human pulling the strings. Even in pure commerce it matters: the narrative story behind a product is often as important as the product itself. Handmade goods attract a price premium over factory made. Or alternatively in entertainment: people pay more to go to a live concert than for streaming music over the internet. People will also pay more to go to see a play in the theatre rather than a movie in the cinema. }

\notes{In many respects I object to the use of the term Artificial Intelligence. It is poorly defined and means different things to different people.  But there is one way in which the term is very accurate. The term artificial is appropriate  in the same way we can describe a plastic plant as an artificial plant. It is often difficult to pick out from afar whether a plant is artificial or not. A plastic plant can fulfil many of the functions of a natural plant, and plastic plants are more convenient. But they can never replace natural plants.}

\notes{In the same way, our natural intelligence is an evolved thing of beauty, a consequence of our limitations. Limitations which don’t apply to artificial intelligences and can only be emulated through artificial means. Our natural intelligence, just like our natural landscapes, should be treasured and can never be fully replaced. }

\endif
