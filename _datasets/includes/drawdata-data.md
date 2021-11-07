\ifndef{drawdataData}
\define{drawdataData}

\editme

\subsection{Drawdata Data}

\notes{The `drawdata` package is made available by [Vincent D. Warmerdam](https://github.com/koaning) for drawing datasets within the Jupyter notebook. You can find it on [Github here](https://github.com/koaning/drawdata). See also [this page](https://calmcode.io/labs/drawdata.html).}

\installcode{drawdata}

\setupcode{from drawdata import draw_scatter}

\notes{Now you can draw scatter data to your heart's content. You can select one of the groups and draw a region which will be filled roughly with random dots.}

\code{draw_scatter()}

\notes{You can then copy to the clipboard and convert to a `DataFrame` as follows.}

\setupcode{import pandas as pd}

\code{data = pd.read_clipboard(sep=",")}

\endif


