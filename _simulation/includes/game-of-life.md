\ifndef{gameOfLife}
\define{gameOfLife}

\editme

Inspired by <https://gist.github.com/jiffyclub/3778422#file-game_of_life-ipynb>


\figure{\includegif{\diagramsDir/simulation/Glider}{50%}}{The glider is an oscillator that moves diagonally after creation. From the simple rules of Life it's not obvious that such an object does exist, until you do the necessary computation.}{glider-gif}


\figure{\includegif{\diagramsDir/simulation/Gosperglidergun}{80%}}{The Gosper glider gun is a configuration that creates gliders. A new glider is released after every 30 turns.}{gosper-glider-gun}

\notes{These patterns had to be discovered, in the same way that a scientist might discover a disease, or an explorer a new land. For example, the Gosper glider gun was [discovered by Bill Gosper in 1970](https://conwaylife.com/wiki/Bill_Gosper).}

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
	
\endif
