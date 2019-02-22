\ifndef{pigeonholing}
\define{pigeonholing}
\editme
\subsection{Pigeonholing}

\figure{
\includejpg{../slides/diagrams/TooManyPigeons}{60%}
\notes{\caption{Decompartmentalization of the model into parts can be seen as pigeonholing the separate tasks that are required.}}
}
\notes{To deal with the complexity of systems design, a common approach is to break complex systems down into a series of tasks. An approach we can think of as "pigeonholing". Classically, a sub-task could be thought of as a particular stage in machining (by analogy to productionlines in factories) or a sub-routine call in computing. Machine learning allows any complex sub-task, that was difficult to decompose by classical methods, to be reconstituted by acquiring data. In particular, when we think of emulating a human, we can ask many humans to perform the sub-task many times and fit machine learning models to reconstruct the performance, or to *emulate* the human in the performance of the task. For example, the decomposition of a complex process such as driving a car into apparently obvious sub-tasks (following the road, identifying pedestrians, etc).}

\notes{The practitioner's approach to deploying artificial intelligence systems is to build up systems of machine learning components. To build a machine learning system, we decompose the task into parts, each of which we can emulate with ML methods. These parts are typically independently constructed and verified. For example, in a driverless car we can decompose the tasks into components such as "pedestrian detection" and "road line detection". Each of these components can be constructed with, for example, a classification algorithm. Nowadays, people will often deploy a deep neural network, but for many tasks a random forest algorithm may be sufficient. We can then superimpose a logic on top. For example, "Follow the road line unless you detect a pedestrian in the road".} 

\notes{This allows for verification of car performance, as long as we can verify the individual components. However, it also implies that the AI systems we deploy are *fragile*.

Our intelligent systems are composed by "pigeonholing" each indvidual task, then substituting with a machine learning model.}

\newslide{Robust}

\slides{
* Need to move beyond pigeonholing tasks.
* Need new approaches to both the design of the individual components, and the combination of components within our AI systems.
}

\notes{But this is not a robust approach to systems design. The definition of sub-tasks can lead to a single point of failure, where if any sub-task fails, the entire system fails.}

\endif
