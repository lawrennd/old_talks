\ifndef{gplvmTutorialData}
\define{gplvmTutorialData}

\editme

\subsection{Getting Started and Downloading Data}

\setupcode{import numpy as np
import GPy
import string}

\notes{The following code is for plotting and to prepare the bigger models for later useage. If you are interested, you can have a look, but this is not essential.}


\setupplotcode{from matplotlib import pyplot as plt
import mlai.plot as plot
import mlai}

\setupplotcode{colors = ["#3FCC94", "#DD4F23", "#C6D63B", "#D44271", 
          "#E4A42C", "#4F9139", "#6DDA4C", "#85831F", 
          "#B36A29", "#CF4E4A"]}
\helpercode{def plot_model(X, which_dims, labels):
	fig, ax = plt.subplots(figsize=plot.big_figsize)
    X = X[:,which_dims]
    ulabs = []
    for lab in labels:
        if not lab in ulabs:
            ulabs.append(lab)
            pass
        pass
    for i, lab in enumerate(ulabs):
        ax.scatter(*X[labels==lab].T,marker='o',color=colors[i],label=lab)
        pass
    pass}

\notes{For this lab, we'll use a data set containing all handwritten digits from $0 \cdots 9$ handwritten, provided by @deCampos-character09. We will only use some of the digits for the demonstrations in this lab class, but you can edit the code below to select different subsets of the digit data as you wish.}


\code{which = [0,1,2,6,7,9] # which digits to work on
data = pods.datasets.decampos_digits(which_digits=which)
Y = data['Y']
labels = data['str_lbls']}

\notes{You can try to plot some of the digits using `plt.matshow` (the digit images have size `16x16`).}

\endif
