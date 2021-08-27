\ifndef{lifeGliderLoaferConway}
\define{lifeGliderLoaferConway}

\editme

\notes{The game leads to patterns emerging, some of these patterns are static, but some oscillate in place, with varying periods. Others oscillate, but when they complete their cycle they've translated to a new location, in other words they move. In Life the former are known as [oscillators](https://conwaylife.com/wiki/Oscillator) and the latter as [spaceships](https://conwaylife.com/wiki/Spaceship).}

\notes{\subsection{Loafers and Gliders}}

\notes{John Horton Conway, as the creator of the game of life, could be seen somehow as the god of this small universe. He created the rules. The rules are so simple that in many senses he, and we, are all-knowing in this space. But despite our knowledge, this world can still 'surprise' us. From the simple rules, emergent patterns of behaviour arise. These include static patterns that don't change from one turn to the next. They also include, oscillators, that pulse between different forms across different periods of time. A particular form of oscillator is known as a 'spaceship', this is one that moves across the board as the game evolves. One of the simplest and earliest spaceships to be discovered is known as the glider.}

\newslide{Glider}

\figure{\columns{\aligncenter{*Glider (1969)*}\aligncenter{\includegif{\diagramsDir/simulation/Glider}{80%}{}{left}}}{\includejpg{\diagramsDir/maths/John-Conway}{80%}{}{right}}{45%}{45%}}{*Left* A Glider pattern discovered 1969 by Richard K. Guy. *Right*. John Horton Conway, creator of *Life* (1937-2020). The glider is an oscillator that moves diagonally after creation. From the simple rules of Life it's not obvious that such an object does exist, until you do the necessary computation.}{glider-loafer-conway}

\notes{The glider was 'discovered' in 1969 by Richard K. Guy. What do we mean by discovered in this context? Well, as soon as the game of life is defined, objects such as the glider do somehow exist, but the many configurations of the game mean that it takes some time for us to see one and know it exists. This means, that despite being the creator, Conway, and despite the rules of the game being simple, and despite the rules being deterministic, we are not 'omniscient' in any simplistic sense. It requires computation to 'discover' what can exist in this universe once it's been defined.} 


\newslide{}
\notes{}

\figure{\includegif{\diagramsDir/simulation/Gosperglidergun}{80%}}{The Gosper glider gun is a configuration that creates gliders. A new glider is released after every 30 turns.}{gosper-glider-gun}

\notes{These patterns had to be discovered, in the same way that a scientist might discover a disease, or an explorer a new land. For example, the Gosper glider gun was [discovered by Bill Gosper in 1970](https://conwaylife.com/wiki/Bill_Gosper). It is a pattern that creates a new glider every 30 turns of the game.}


\newslide{Loafer}

\notes{Despite widespread interest in Life, some of its patterns were only very recently discovered like the Loafer, discovered in 2013 by Josh Ball. So despite the game having existed for over forty years, and the rules of the game being simple, there are emergent behaviours that are unknown.}

\newslide{}

\figure{\columns{\aligncenter{*Loafer (2013)*}\aligncenter{\includegif{\diagramsDir/simulation/Loafer}{80%}{}{left}}}{\includejpg{\diagramsDir/maths/John-Conway}{80%}{}{right}}{45%}{45%}}{*Left* A Loafer pattern discovered by Josh Ball in 2013. *Right*. John Horton Conway, creator of *Life* (1937-2020).}{the-loafer-spaceship}

\endif
