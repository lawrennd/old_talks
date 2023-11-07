\ifndef{drawdataData}
\define{drawdataData}

\editme

\subsection{Drawdata Data}

\notes{The `drawdata` package is made available by [Vincent D. Warmerdam](https://github.com/koaning) for drawing datasets within the Jupyter notebook. You can find it on [Github here](https://github.com/koaning/drawdata). See also [this page](https://calmcode.io/labs/drawdata.html).}

\installcode{drawdata}

\setupcode{from drawdata import draw_scatter}

\notes{Now you can draw scatter data to your heart's content. You can select one of the groups and draw a region which will be filled roughly with random dots.}

\code{draw_scatter()}

\subsubsection{On a Local Machine}

\notes{If you are running this on a local machine then copy the data to the clipboard by pressing `copy csv` and convert to a `DataFrame` as follows.}

\setupcode{import pandas as pd}

\code{data = pd.read_clipboard(sep=",")}

\subsubsection{On Google Colab}

\notes{Otherwise, on Google Colab you can download the file to your local machine, it will save as `data.csv`. Then you can upload that data into Colab as follows.}

\setupcode{import io
from google.colab import files}

\code{uploaded = files.upload()
data = pd.read_csv(io.StringIO(uploaded["data.csv"].decode("utf-8")))}

\endif


