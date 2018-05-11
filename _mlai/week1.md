---
layout: slides
title: Probability and an Introduction to Jupyter, Python and Pandas
author: Neil D. Lawrence
date: 2015/09/29
---

\include{talk-macros.tex}

\notes{Welcome to the Machine Learning and Adaptive
Intelligence course. In this course we will introduce the basic concepts of
machine learning and data science. In particular we will look at tools and
techniques that describe how to model. An integrated part of that is how we
approach data with the computer. We are choosing to do that with the tool you
see in front of you: the Jupyter Notebook.}

\notes{The notebook provides us with a way
of interacting with the data that allows us to give the computer instructions
and explore the nature of a data set. It is *different* to normal coding, but it
is related. In this course you will, through intensive practical sessions and
labs, develop your understanding of the interaction between data and computers.
The first thing we are going to do is ask you to forget a bit about what you
think about normal programming, or 'classical software engineering'. Classical
software engineering demands a large amount of design and testing. In data
analysis, testing remains very important, but the design is often evolving. The
design evolves through a process known as *exploratory data analysis*. You will
learn some of the techniques of exploratory data analysis in this course.}

\notes{A
particular difference between classical software engineering and data analysis
is the way in which programs are run. Classically we spend a deal of time
working with a text editor, writing code. Compilations are done on a regular
basis and aspects of the code are tested (perhaps with unit tests).}

\notes{Data
analysis is more like coding in a debugger. In a debugger (particularly a visual
debugger) you interact with the data stored in the memory of the computer to try
and understand what is happening in the computer, you need to understand exactly
what your bug is: you often have a fixed idea of what the program is trying to
do, you are just struggling to find out why it isn't doing it.}

\notes{Naturally,
debugging is an important part of data analysis also, but in some sense it can
be seen as its entire premise. You load in a data set into a computer that you
don't understand, your entire objective is to understand the data. This is best
done by interogating the data to visualise it or summarize it, just like in a
power visual debugger. However, for data science the requirements for
visualization and summarization are far greater than in a regular program. When
the data is well understood, the actual number of lines of your program may well
be very few (particularly if you disregard commands that load in the data and
commands which plot your results). If a powerful data science library is
available, you may be able to summarize your code with just two or three lines,
but the amount of intellectual energy that is expended on writing those three
lines is far greater than in standard code.}

In the first lecture we will think
a little about 'how we got here' in terms of computer science. In the lecture
itself, this will be done by taking a subjective perspective, that of my own
'data autobiography'.

\section{Assumed Knowledge}

### Linear Algebra, Probability and Differential Calculus

We will be assuming that you have good background in maths. In particular we
will be making use of linear algrebra (matrix operations including inverse,
inner products, determinant etc), probability (sum rule of probability, product
rule of probability), and the calculus of differentiation (and integration!). A
new concept for the course is multivariate differentiation and integration. This
combines linear algebra and differential calculus. These techniques are vital in
understanding probability distributions over high dimensional distributions.

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

\section{Movie Body Count Example}

\notes{There is a crisis in the movie industry, deaths are
occuring on a massive scale. In every feature film the body count is tolling up.
But what is the cause of all these deaths? Let's try and investigate.}

\notes{For our
first example of data science, we take inspiration from work by [researchers at
NJIT](http://www.theswarmlab.com/r-vs-python-round-2/). They researchers were
comparing the qualities of Python with R (my brief thoughts on the subject are
available in a Google+ post here:
https://plus.google.com/116220678599902155344/posts/5iKyqcrNN68). They put
together a data base of results from the  the "Internet Movie Database" and the
[Movie Body Count](http://www.moviebodycounts.com/) website which will allow us
to do some preliminary investigation.}

\notes{We will make use of data that has already been 'scraped' from the [Movie Body
Count](http://www.moviebodycounts.com/) website. Code and the data is available
at [a github repository](https://github.com/sjmgarnier/R-vs-
Python/tree/master/Deadliest%20movies%20scrape/code). Git is a version control
system and github is a website that hosts code that can be accessed through git.
By sharing the code publicly through github, the authors are licensing the code
publicly and allowing you to access and edit it. As well as accessing the code
via github you can also [download the zip
file](https://github.com/sjmgarnier/R-vs-Python/archive/master.zip). But let's
do that in python}

\code{import pods
pods.util.download_url('https://github.com/sjmgarnier/R-vs-Python/archive/master.zip')
}

\notes{Once the data is downloaded we can unzip it into the same directory where we are running the lab class.}

\code{import zipfile
zip = zipfile.ZipFile('./master.zip', 'r')
for name in zip.namelist():
    zip.extract(name, '.')}

\code{import pandas as pd # import the pandas library into a namespace called pd
film_deaths = pd.read_csv('./R-vs-Python-master/Deadliest movies scrape/code/film-death-counts-Python.csv')}

\notes{Once it is loaded in the data can be summarized using the `describe` method in pandas.}

\code{film_deaths.describe()}

\notes{In jupyter and jupyter notebook it is possible to see a list of all possible
functions and attributes by typing the name of the object followed by .<Tab> for
example in the above case if we type film_deaths.<Tab> it show the columns
available (these are attributes in pandas dataframes) such as Body_Count, and
also functions, such as .describe().}

\notes{For functions we can also see the
documentation about the function by following the name with a question mark.
This will open a box with documentation at the bottom which can be closed with
the x button.}

\code{film_deaths.describe?}

\notes{The film deaths data is stored in an object known as a 'data frame'. Data frames
come from the statistical family of programming languages based on `S`, the most
widely used of which is
[`R`](http://en.wikipedia.org/wiki/R_(programming_language)). The data frame
gives us a convenient object for manipulating data. The describe method
summarizes which columns there are in the data frame and gives us counts, means,
standard deviations and percentiles for the values in those columns. To access a
column directly we can write}

\code{print(film_deaths['Year'])
#print(film_deaths['Body_Count'])}

\notes{This shows the number of deaths per film across the years. We can plot the data as follows.}

\code{# this ensures the plot appears in the web browser
%matplotlib inline 
import matplotlib.pyplot as plt # this imports the plotting library in python

plt.plot(film_deaths['Year'], film_deaths['Body_Count'], 'rx')}

\notes{You may be curious what the arguments we give to plt.plot are for, now is the perfect time to look at the documentation}

\code{plt.plot?}

\notes{We immediately note that some films have a lot of deaths, which prevent us seeing the detail of the main body of films. First lets identify the films with the most deaths.}

\code{film_deaths[film_deaths['Body_Count']>200]}

\notes{Here we are using the command `film_deaths['Kill_Count']>200` to index the films in the pandas data frame which have over 200 deaths. To sort them in order we can also use the `sort` command. The result of this command on its own is a data series of `True` and `False` values. However, when it is passed to the
`film_deaths` data frame it returns a new data frame which contains only those
values for which the data series is `True`. We can also sort the result. To sort
the result by the values in the `Kill_Count` column in *descending* order we use
the following command.}

\code{film_deaths[film_deaths['Body_Count']>200].sort(columns='Body_Count', ascending=False)}

\notes{We now see that the 'Lord of the Rings' is a large outlier with a very large number of kills. We can try and determine how much of an outlier by histograming the data.}

### Plotting the Data

\code{film_deaths['Body_Count'].hist(bins=20) # histogram the data with 20 bins.
plt.title('Histogram of Film Kill Count')}

\writeassignment{Read on the internet about the following python
libraries: `numpy`, `matplotlib`, `scipy` and `pandas`. What functionality does
each provide python. What is the `pylab` library and how does it relate to the
other libraries?}{2}{10}

\notes{We could try and remove these outliers, but another approach would be plot the logarithm of the counts against the year.}

\code{plt.plot(film_deaths['Year'], film_deaths['Body_Count'], 'rx')
ax = plt.gca() # obtain a handle to the current axis
ax.set_yscale('log') # use a logarithmic death scale
# give the plot some titles and labels
plt.title('Film Deaths against Year')
plt.ylabel('deaths')
plt.xlabel('year')}

\notes{Note a few things. We are interacting with our data. In particular, we are
replotting the data according to what we have learned so far. We are using the
progamming language as a *scripting* language to give the computer one command
or another, and then the next command we enter is dependent on the result of the
previous. This is a very different paradigm to classical software engineering.
In classical software engineering we normally write many lines of code (entire
object classes or functions) before compiling the code and running it. Our
approach is more similar to the approach we take whilst debugging. Historically,
researchers interacted with data using a *console*. A command line window which
allowed command entry. The notebook format we are using is slightly different.
Each of the code entry boxes acts like a separate console window. We can move up
and down the notebook and run each part in a different order. The *state* of the
program is always as we left it after running the previous part.}

\writeassignment{What is jupyter and why was it invented? Give some
examples of functionality it gives over standard python. What is the jupyter
project? Name two languages involved in the Jupyter project other than python.}{3}{10}

\section{Probabilities}

\notes{We are now going to do some simple review of probabilities and
use this review to explore some aspects of our data.}

\notes{A probability distribution
expresses uncertainty about the outcome of an event. We often encode this
uncertainty in a variable. So if we are considering the outcome of an event,
$Y$, to be a coin toss, then we might consider $Y=1$ to be heads and $Y=0$ to be
tails. We represent the probability of a given outcome with the notation:
$$
P(Y=1) = 0.5
$$
The first rule of probability is that the probability must
normalize. The sum of the probability of all events must equal 1. So if the
probability of heads ($Y=1$) is 0.5, then the probability of tails (the only
other possible outcome) is given by
$$
P(Y=0) = 1-P(Y=1) = 0.5
$$}

\notes{Probabilities
are often defined as the limit of the ratio between the number of positive
outcomes (e.g. *heads*) given the number of trials. If the number of positive
outcomes for event $y$ is denoted by $n$ and the number of trials is denoted by
$N$ then this gives the ratio 
$$
P(Y=y) = \lim_{N\rightarrow
\infty}\frac{n_y}{N}.
$$
In practice we never get to observe an event infinite
times, so rather than considering this we often use the following estimate
$$
P(Y=y) \approx \frac{n_y}{N}.
$$
Let's use this rule to compute the approximate
probability that a film from the movie body count website has over 40 deaths.}

\code{deaths = (film_deaths.Body_Count>40).sum()  # number of positive outcomes (in sum True counts as 1, False counts as 0)
total_films = film_deaths.Body_Count.count()

prob_death = float(deaths)/float(total_films)
print("Probability of deaths being greather than 40 is:", prob_death)}

\writeassignment{We now have an estimate of the probability a film has
greater than 40 deaths. The estimate seems quite high. What could be wrong with
the estimate? Do you think any film you go to in the cinema has this probability
of having greater than 40 deaths?

Why did we have to use `float` around our
counts of deaths and total films? What would the answer have been if we hadn't
used the `float` command? If we were using Python 3 would we have this problem?}{4}{20}

\section{Conditioning}

\notes{When predicting whether a coin turns up head or tails, we might
think that this event is *independent* of the year or time of day. If we include
an observation such as time, then in a probability this is known as
*condtioning*. We use this notation, $P(Y=y|T=t)$, to condition the outcome on a
second variable (in this case time). Or, often, for a shorthand we use $P(y|t)$
to represent this distribution (the $Y=$ and $T=$ being implicit). Because we
don't believe a coin toss depends on time then we might write that 
$$
P(y|t) =
p(y).
$$
However, we might believe that the number of deaths is dependent on the
year. For this we can try estimating $P(Y>40 | T=2000)$ and compare the result,
for example to $P(Y>40|2002)$ using our empirical estimate of the probability.}

\code{for year in [2000, 2002]:
    deaths = (film_deaths.Body_Count[film_deaths.Year==year]>40).sum()
    total_films = (film_deaths.Year==year).sum()

    prob_death = float(deaths)/float(total_films)
    print("Probability of deaths being greather than 40 in year", year, "is:", prob_death)}

\codeassignment{Compute the probability for the number of deaths
being over 40 for each year we have in our `film_deaths` data frame. Store the
result in a `numpy` array and plot the probabilities against the years using the
`plot` command from `matplotlib`. Do you think the estimate we have created of
$P(y|t)$ is a good estimate? Write your code and your written answers in the box
below.}{5}{20}

#### Question 5 Answer Text

\notes{Write your answer to the question in this box.}

#### Notes for Question 5

\notes{Make sure the plot is included in *this* notebook
file (the `IPython` magic command `%matplotlib inline` we ran above will do that
for you, it only needs to be run once per file).}

### Rules of Probability

\notes{We've now introduced conditioning and independence to
the notion of probability and computed some conditional probabilities on a
practical example The scatter plot of deaths vs year that we created above can
be seen as a *joint* probability distribution. We represent a joint probability
using the notation $P(Y=y, T=t)$ or $P(y, t)$ for short. Computing a joint
probability is equivalent to answering the simultaneous questions, what's the
probability that the number of deaths was over 40 and the year was 2002? Or any
other question that may occur to us. Again we can easily use pandas to ask such
questions.}

\code{year = 2000
deaths = (film_deaths.Body_Count[film_deaths.Year==year]>40).sum()
total_films = film_deaths.Body_Count.count() # this is total number of films
prob_death = float(deaths)/float(total_films)
print("Probability of deaths being greather than 40 and year being", year, "is:", prob_death)}

### The Product Rule

\notes{This number is the joint probability, $P(Y, T)$ which is
much *smaller* than the conditional probability. The number can never be bigger
than the conditional probabililty because it is computed using the *product
rule*.
$$
p(Y=y, T=t) = p(Y=y|T=t)p(T=t)
$$
and $$p(T=t)$$ is a probability
distribution, which is equal or less than 1, ensuring the joint distribution is
typically smaller than the conditional distribution.}

\notes{The product rule is a
*fundamental* rule of probability, and you must remember it! It gives the
relationship between the two questions: 1) What's the probability that a film
was made in 2002 and has over 40 deaths? and 2) What's the probability that a
film has over 40 deaths given that it was made in 2002?}

\notes{In our shorter notation
we can write the product rule as
$$
p(y, t) = p(y|t)p(t)
$$
We can see the
relation working in practice for our data above by computing the different
values for $t=2000$.}

\code{p_t = float((film_deaths.Year==2002).sum())/float(film_deaths.Body_Count.count())
p_y_given_t = float((film_deaths.Body_Count[film_deaths.Year==2002]>40).sum())/float((film_deaths.Year==2002).sum())
p_y_and_t = float((film_deaths.Body_Count[film_deaths.Year==2002]>40).sum())/float(film_deaths.Body_Count.count())

print("P(t) is", p_t)
print("P(y|t) is", p_y_given_t)
print("P(y,t) is", p_y_and_t)}

### The Sum Rule

\notes{The other *fundamental rule* of probability is the *sum rule*
this tells us how to get a *marginal* distribution from the joint distribution.
Simply put it says that we need to sum across the value we'd like to remove.
$$
P(Y=y) = \sum_{t} P(Y=y, T=t)
$$
Or in our shortened notation
$$
P(y) = \sum_{t}
P(y, t)
$$}

\codeassignment{Write code that computes $P(y)$ by adding $P(y, t)$
for all values of $t$.}{6}{10}

\section{Bayes' Rule}

\notes{Bayes rule is a very simple rule, it's hardly worth the name of
a rule at all. It follows directly from the product rule of probability. Because
$P(y, t) = P(y|t)P(t)$ and by symmetry $P(y,t)=P(t,y)=P(t|y)P(y)$ then by
equating these two equations and dividing through by $P(y)$ we have
$$
P(t|y) =
\frac{P(y|t)P(t)}{P(y)}
$$
which is known as Bayes' rule (or Bayes's rule, it
depends how you choose to pronounce it). It's not difficult to derive, and its
importance is more to do with the semantic operation that it enables. Each of
these probability distributions represents the answer to a question we have
about the world. Bayes rule (via the product rule) tells us how to *invert* the
probability.}

## Probabilities for Extracting Information from Data

\notes{What use is all this
probability in data science? Let's think about how we might use the
probabilities to do some decision making. Let's load up a little more
information about the movies.}

\code{movies = pd.read_csv('./R-vs-Python-master/Deadliest movies scrape/code/film-death-counts-Python.csv')
movies.columns}

\writeassignment{Now we see we have several additional features
including the quality rating (`IMDB_Rating`). Let's assume we want to predict
the rating given the other information in the data base. How would we go about
doing it? 

Using what you've learnt about joint, conditional and marginal
probabilities, as well as the sum and product rule, how would you formulate the
question you want to answer in terms of probabilities? Should you be using a
joint or a conditional distribution? If it's conditional, what should the
distribution be over, and what should it be conditioned on?}{7}{20}

## Assignment Questions

\notes{The questions in the above lab sheet need to be
answered and handed in before 09:00 on 7th October 2014 (i.e. before next
lecture). The hand should be done via file upload through
[MOLE](http://vle.shef.ac.uk).}

## More Fun on the Python Data Farm

\notes{If you want to explore more of the things
you can do with movies and python you might be interested in the `imdbpy` python
library.}

\notes{You can try installing it using `pip` as follows.}

\code{!pip install IMDbPY}

\notes{If this doesn't work on your machine, try following instructions on
(http://imdbpy.sourceforge.net/)}

\notes{Once you've installed `imdbpy` you can test it
works with the following script, which should list movies with the word 'python'
in their title. To run the code in the following box, simply click the box and
press `SHIFT-enter` or `CTRL-enter`. Then you can try running the code below.}

\code{from imdb import IMDb
ia = IMDb()

for movie in ia.search_movie('python'):
    print(movie) }

\includeyoutube{GX8VLYUYScM}
