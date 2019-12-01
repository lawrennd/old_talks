\ifndef{artificialVsNaturalSystemsShort}
\define{artificialVsNaturalSystemsShort}
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

\notes{So it is with natural vs artificial intelligences. Any natural intelligence that was not robust to changes in its external environment would not survive, and therefore not reproduce. In contrast the artificial intelligences we produce are designed to be efficient at one specific task: control, computation, playing chess. They are *fragile*. 

The first rule of a natural system is not be intelligent, it is "don't be stupid".}

\newslide{Mistake we Make}
\slides{
* Equate fitness for objective function.
* Assume static environment and known objective. 
}

\notes{A mistake we make in the design of our systems is to equate fitness with the objective function, and to assume it is known and static. In practice, a real environment would have an evolving fitness function which would be unknown at any given time.}

\notes{You can also read this }\addblog{Natural and Artificial Intelligence}{2018/02/06/natural-and-artificial-intelligence}\notes{.} 

\notes{The first criterion of a natural intelligence is *don’t fail*, not because it has a will or intent of its own, but because if it had failed it wouldn’t have stood the test of time. It would no longer exist. In contrast, the mantra for artificial systems is to be more efficient. Our artificial systems are often given a single objective (in machine learning it is encoded in a mathematical function) and they aim to achieve that objective efficiently. These are different characteristics. Even if we wanted to incorporate *don’t fail* in some form, it is difficult to design for. To design for “don’t fail”, you have to consider every which way in which things can go wrong, if you miss one you fail. These cases are sometimes called corner cases. But in a real, uncontrolled environment, almost everything is a corner. It is difficult to imagine everything that can happen. This is why most of our automated systems operate in controlled environments, for example in a factory, or on a set of rails. Deploying automated systems in an uncontrolled environment requires a different approach to systems design. One that accounts for uncertainty in the environment and is robust to unforeseen circumstances.}

\endif
