\ifndef{gameOfLife}
\define{gameOfLife}

\editme


\subsection{Game of Life}

\notes{[John Horton Conway](https://en.wikipedia.org/wiki/John_Horton_Conway) was a mathematician who developed a game known as the Game of Life. He unfortunately died in April 2020, but since he invented the game he was in effect 'god' for this game. But as we will see, just inventing the rules doesn't give you omniscience in the game.}

\notes{The Game of Life is played on a grid of squares, or pixels. Each pixel is either on or off. The game has no players, but a set of simple rules that are followed at each turn the rules are.}

* **Survival** Every pixel surrounded by two or three other pixels survives for the next turn.
* **Death** Each pixel surrounded by four or more pixels dies from overpopulation. Likewise, every pixel next to one or no pixels at all dies from isolation.
* **Birth** Each square adjacent to exactly three pixels gives birth to a new pixel.

\notes{And that's it. Those are the simple 'physical laws' for Conway's game.}

\notes{The game leads to patterns emerging, some of these patterns are static, but some oscilate, with varying periods. Others oscilalate, but when they complete their cycle they've translated to a new location, in other words they move. In Life the former are known as [oscillators](https://conwaylife.com/wiki/Oscillator) and the latter as [spaceships](https://conwaylife.com/wiki/Spaceship).}

\newslide{}

\figure{\includegif{\diagramsDir/simulation/Glider}{50%}}{The glider is an oscillator that moves diagonally after creation. From the simple rules of Life it's not obvious that such an object does exist, until you do the necessary computation.}{glider-gif}

\newslide{}
\notes{}

\figure{\includegif{\diagramsDir/simulation/Gosperglidergun}{80%}}{The Gosper glider gun is a configuration that creates gliders. A new glider is released after every 30 turns.}{gosper-glider-gun}

\notes{These patterns had to be discovered, in the same way that a scientist might discover a disease, or an explorer a new land. For example, the Gosper glider gun was [discovered by Bill Gosper in 1970](https://conwaylife.com/wiki/Bill_Gosper).}

\notes{Despite widespread interest in Life, some of its patterns were only very recently discovered like the Loafer, discovered in 2013 by Josh Ball.}

\notes{}

\newslide{}

\figure{\includegif{\diagramsDir/simulation/Loafer}{60%}}{The Loafer, discovered by Josh Ball in 2013 is named for its slow movement.}{the-loafer-spaceship}

\notes{Once these patterns are discovered, they are combined (or engineered) to create new Life patterns that do some remarkable things. For example there's a life pattern that runs a Turing machine, or more remarkably there's a Life pattern that runs Life itself.}

\newslide{}

\figure{\includegif{\diagramsDir/simulation/life-in-life}{80%}}{The Game of Life running in Life. The video is drawing out recursively showing pixels that are being formed by filling cells with moving spaceships. Each individual pixel in this game of life is made up of $2048 \times 2048$ pixels called an [OTCA metapixel](https://www.conwaylife.com/wiki/OTCA_metapixel).}{life-in-life}

\notes{To find out more about the Game of Life you can watch this video by Alan Zucconi or read his [associated blog post](https://www.alanzucconi.com/2020/10/13/conways-game-of-life/).}

\newslide{}

\figure{\includeyoutube{Kk2MH9O4pXY}{800}{600}}{An introduction to the Game of Life by Alan Zucconi.}{intro-to-life}



<!--
\notes{Inspired by <https://gist.github.com/jiffyclub/3778422#file-game_of_life-ipynb>}
\setupcode{import numpy as np
from scipy.signal import convolve}

\code{# used for counting the number of living neighbors each cell has
FILTER = np.array([[1, 1, 1],
                   [1, 100, 1],
                   [1, 1, 1]], dtype=np.uint8)}


\code{def evolve(length, generations):
    """
    Run the Game of Life. Starting state is random.

    Parameters
    ----------
    length : int
        Universe will be `length` units per side.
    generations : int
        Number of generations to run simulation.

    """
    current = np.random.randint(2, size=(length, length))
    next = np.empty_like(current)
    current[length//2, 1:(length-1)] = 1
    show_board(current)
    for _ in range(generations):
        advance(current, next)
        current, next = next, current
        show_board(current)}

\code{def advance(current, next):
    """
    Calculate the next iteration of the Game of Life.

    Parameters
    ----------
    current : 2D array
        Current state of universe.
    next : 2D array
        This array will be modified in place so that it contains the
        next step. Must be the same size as `current`.

    """
    assert current.shape[0] == current.shape[1], \
           'Expected square universe'
    next[:] = 0
    count = convolve(current, FILTER, mode='same')
    next[(count == 3) | (count == 102) | (count == 103)] = 1}
-->	
\endif
