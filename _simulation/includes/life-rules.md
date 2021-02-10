\ifndef{lifeRules}
\define{lifeRules}

\editme


\notes{\subsection{Life Rules}}

\newslide{}

\figure{\columns{\threeColumns{\aligncenter{\includediagramclass{\diagramsDir/simulation/life-rules-1-0}{100%}}}{}{\aligncenter{\includediagramclass{\diagramsDir/simulation/life-rules-1-1}{100%}}}{33%}{33%}{33%}}{\aligncenter{\includejpg{\diagramsDir/maths/John-Conway}{100%}{}{right}}}{70%}{30%}}{'Death' through loneliness in Conway's game of life. If a cell is surrounded by less than three cells, it 'dies' through loneliness.}{life-rules-loneliness}

\newslide{}

\figure{\columns{\threeColumns{\aligncenter{\includediagramclass{\diagramsDir/simulation/life-rules-2-0}{60%}}}{}{\aligncenter{\includediagramclass{\diagramsDir/simulation/life-rules-2-1}{60%}}}{33%}{33%}{33%}}{\aligncenter{\includejpg{\diagramsDir/maths/John-Conway}{100%}{}{right}}}{70%}{30%}}{'Death' through overpopulation in Conway's game of life. If a cell is surrounded by more than three cells, it 'dies' through loneliness.}{life-rules-crowding}

\newslide{}

\figure{\columns{\threeColumns{\aligncenter{\includediagramclass{\diagramsDir/simulation/life-rules-3-0}{60%}}}{}{\aligncenter{\includediagramclass{\diagramsDir/simulation/life-rules-3-1}{60%}}}{33%}{33%}{33%}}{\aligncenter{\includejpg{\diagramsDir/maths/John-Conway}{100%}{}{right}}}{70%}{30%}}{'Death' through overpopulation in Conway's game of life. If a cell is surrounded by more than three cells, it 'dies' through loneliness.}{life-rules-crowding}

\notes{Conway's game of life has three simple rules.

* **Survival** Every cell surrounded by two or three other cells survives for the next turn.
* **Death** Each cell surrounded by four or more cells dies from overpopulation. Likewise, every cell next to one or no cells at all dies from isolation.
* **Birth** Each square adjacent to exactly three cells gives birth to a new cell.
}

\endif

