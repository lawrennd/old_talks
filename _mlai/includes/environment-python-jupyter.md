### Choice of Language

\notes{In this course we will be using Python for our
programming language. A prerequisite of attending this course is that you have
learnt at least one programming language in the past. It is not our objective to
teach you python. At Level 4 and Masters we expect our students to be able pick
up a language as they go. If you have not experienced python before it may be
worth your while spending some time understanding the language. There are
resources available for you to do this
[here](https://docs.python.org/2/tutorial/) that are based on the standard
console. An introduction to the Jupyter notebook (formerly known as the IPython
notebook) is available [here](http://ipython.org/ipython-
doc/2/notebook/index.html).}

\writeassignment{Who invented python and why? What was the language
designed to do? What is the origin of the name "python"? Is the language a
compiled language? Is it an object orientated language?}{1}{10}

\section{Choice of Environment}

\notes{We are working in the Jupyter notebook (formerly known
as the IPython notebook). It provides an environment for interacting with data
in a natural way which is reproducible. We will be learning how to make use of
the notebook throughout the course. The notebook allows us to combine code with
descriptions, interactive visualizations, plots etc. In fact it allows us to do
many of the things we need for data science. Notebooks can also be easily shared
through the internet for ease of communication of ideas. The box this text is
written in is a *markdown* box. Below we have a *code* box.}

\code{print("This is the Jupyter notebook")
print("It provides a platform for:")
words = ['Open', 'Data', 'Science']
from random import shuffle
for i in range(3):
    shuffle(words)
    print(' '.join(words))}

\notes{Have a play with the code in the above box. Think about the following questions:
what is the difference between `CTRL-enter` and `SHIFT-enter` in running the
code? What does the command `shuffle` do? Can you find out by typing `shuffle?`
in a code box?
Once you've had a play with the code we can load in some data
using the `pandas` library for data analysis.}


