\subsection{Pigeonholing}

\includeimg{../slides/diagrams/TooManyPigeons.jpg}{60%}

\notes{To deal with the complexity of systems design, a common approach is to break complex systems down into a series of tasks. An approach we can think of as "pigeonholing". Classically, a sub-task could perhaps be thought of as a particular stage in machining (automating a factory) or a sub-routine call in computing. Machine learning allows any complex sub-task, that was difficult to decompose by classical methods, to be reconstituted by acquiring data. In particular, when we think of emulating a human, we can ask many humans to perform the sub-task many times and fit machine learning models to reconstruct the performance, or to *emulate* the human in the performance of the task. For example, the decomposition of a complex process such as driving a car into apparently obvious sub-tasks (following the road, identifyin pedestrians, etc).}

\newslide{Robust}

\slides{
* Need to move beyond pigeonholing tasks.
* Need new approaches to both the design of the individual components, and the combination of components within our AI systems.
}

\notes{But this is not robust approach to systems design. The definition of sub-tasks can lead to a single point of failure, where if a sub-task fails, the system fails.}
