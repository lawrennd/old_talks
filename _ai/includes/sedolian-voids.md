\ifndef{sedolianVoids}
\define{sedolianVoids}

\editme

\subsection{AlphaGo}
\notes{In January 2016, the UK company DeepMind's machine learning system AlphaGo won a challenge match in which it beat the world champion Go player, Lee Se-Deol.}


\figure{\includejpg{\diagramsDir/ai/nature-go}{50%}}{AlphaGo's win made the front cover of the journal Nature.}{nature-go}

\notes{Go is a board game that is known to be over 2,500 years old. It is considered challenging for computer systems becaue of its branching factor: the number of possible moves that can be made at a given board postion. The branching factor of Chess is around 35. The branching factor of Go is around 250. This makes Go less susceptible to exhaustive search techniques which were a foundation of DeepBlue, the chess machine that was able to win against Gary Kasparov in 1997. As a result, many commentators predicted that Go was out of the reach of contemporary AI systems, with some predicting that beating the world champion wouldn't occur until 2025.}

\figure{\includeyoutube{WXuK6gekU1Y}{600}{450}}{The AlphaGo documentary tells the story of the tournament between Lee Se-dol and AlphaGo.}{alpha-go-documentary}

\notes{While exhaustive search was beyond the reach of computer systems, they combined stochastic search of the game tree with neural networks. But when training those neural networks vast quantities of data and game play were used. I wrote more about this at the time in the Guardian article "\addguardian{Google AI versus the Go grandmaster}{2016/jan/28/google-ai-go-grandmaster-real-winner-deepmind}".}

\newslide{Sedolian Void}


\notes{However, despite the many millions of matches that AlphaGo had played, Lee Sedol
managed to find a board position that was distinct from anything AlphaGo
had seen before. Within the high dimensional pinball machine that made
up AlphaGo's decision making systems, Lee Sedol found a niche, an
Achillean chink in AlphaGo's armour. He found a path through the neural
network where no data had every been before. He found a location in
feature space "where there be dragons". A space where the model had not seen data before and one where it became confused.} 

\figure{\columns{\includepng{\diagramsDir/ai/lee-se-dol-alpha-go-game-4-move-78}{60%}}{\includejpg{\diagramsDir/ai/lee-se-dol}{60%}}{49%}{49%}}{Move 78 of [Game 4](https://en.wikipedia.org/wiki/AlphaGo_versus_Lee_Sedol#Game_4) was critical in allowing Lee Se-dol to win the match. Described by [Gu Li](https://en.wikipedia.org/wiki/Gu_Li_(Go_player)) as a 'divine move'.}{lee-se-dol-move-78}

\notes{This is a remarkable achievement, a human, with far less experience than the machine of the game, was able to outplay by placing the machine in an unfamiliar situation. In honour of this achievements, I like to call these voids in the machines understanding "Sedolian voids".}

\subsection{Uber ATG}

\notes{Unfortunately, such Sedolian voids are not constrained to game playing machines. On March 18th 2018, just two years after AlphaGo's victory, the Uber ATG self-driving vehicle killed a pedestrian in Tuscson Arizona. The neural networks that were trained on pedestrian detection did not detect Elaine because she was pushing a bicycle, laden with her bags, across the highway.[^uber-atg-crash] This situation represented a Sedolian void for the neural network, and it failed to stop the car.

[^uber-atg-crash]: The NTSB Report on the accident can be found online here: <https://www.ntsb.gov/investigations/Pages/HWY18FH010.aspx>.}



\figure{\includeyoutube{iWGhXof45zI}{600}{450}}{A vehicle operated by Uber ATG was involved in a fatal crash when it killed pedestrian Elaine Herzberg, 49.}{uber-atg-elaine}

\notes{Characterising the regions where this is happening for these models remains an outstanding challenge.}

\endif
