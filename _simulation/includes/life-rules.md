\ifndef{lifeRules}
\define{lifeRules}

\editme

\notes{\subsection{Life Rules}}

\notes{John Conway's game of life is a cellular automaton where the cells obey three very simple rules. The cells live on a rectangular grid, so that each cell has 8 possible neighbors.}

\newslide{Loneliness}

\figure{\columns{\threeColumns{\aligncenter{\includediagramclass{\diagramsDir/simulation/life-rules-1-0}{100%}}}{\aligncenter{*loneliness*}\aligncenter{\includediagram{\diagramsDir/util/right-arrow}{60%}}}{\aligncenter{\includediagramclass{\diagramsDir/simulation/life-rules-1-1}{100%}}}{30%}{39%}{30%}}{\aligncenter{\includejpg{\diagramsDir/maths/John-Conway}{100%}{}{right}}}{70%}{30%}}{'Death' through loneliness in Conway's game of life. If a cell is surrounded by less than three cells, it 'dies' through loneliness.}{life-rules-loneliness}

\notes{The game proceeds in turns, and at each location in the grid is either alive or dead. Each turn, a cell counts its neighbors. If there are two or fewer neighbors, the cell 'dies' of 'loneliness'.}

\newslide{Crowding}

\figure{\columns{\threeColumns{\aligncenter{\includediagramclass{\diagramsDir/simulation/life-rules-2-0}{100%}}}{\aligncenter{*overcrowding*}\aligncenter{\includediagram{\diagramsDir/util/right-arrow}{60%}}}{\aligncenter{\includediagramclass{\diagramsDir/simulation/life-rules-2-1}{100%}}}{30%}{39%}{30%}}{\aligncenter{\includejpg{\diagramsDir/maths/John-Conway}{100%}{}{right}}}{70%}{30%}}{'Death' through overpopulation in Conway's game of life. If a cell is surrounded by more than three cells, it 'dies' through loneliness.}{life-rules-crowding}

\notes{If there are four or more neighbors, the cell 'dies' from 'overcrowding'. If there are three neighbors, the cell persists, or if it is currently dead, a new cell is born.}

\newslide{Birth}

\figure{\columns{\threeColumns{\aligncenter{\includediagramclass{\diagramsDir/simulation/life-rules-3-0}{100%}}}{\aligncenter{*birth*}\aligncenter{\includediagram{\diagramsDir/util/right-arrow}{60%}}}{\aligncenter{\includediagramclass{\diagramsDir/simulation/life-rules-3-1}{100%}}}{30%}{39%}{30%}}{\aligncenter{\includejpg{\diagramsDir/maths/John-Conway}{100%}{}{right}}}{70%}{30%}}{Birth in Conway's life. Any position surounded by precisely three live cells will give birth to a new cell at the next turn.}{life-rules-crowding}

\notes{And that's it. Those are the simple 'physical laws' for Conway's game.}

\endif

