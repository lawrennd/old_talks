---
layout: lecture
title: Probability and an Introduction to Jupyter, Python and Pandas
abstract: |
  In this first session we will introduce *machine learning*, review *probability* and begin familiarization with the Jupyter notebook, python and pandas.
date: 2015-09-29
ipynb: True
week: 1
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Sheffield
  twitter: lawrennd
  url: http://inverseprobability.com
venue: University of Sheffield
postdir: ../../../mlatcl/mlai/_lectures/
slidedir: ../../../mlatcl/mlai/slides/
notedir: ../../../mlatcl/mlai/_notes/
notebookdir: ../../../mlatcl/mlai/_notebooks/
youtube: M67rG3cZoVg
transition: None
---

\include{talk-macros.tex}

\include{_mlai/includes/welcome.md}
\include{_mlai/includes/assumed-knowledge.md}
\include{_mlai/includes/environment-python-jupyter.md}

\writeassignment{What is jupyter and why was it invented? Give some
examples of functionality it gives over standard python. What is the jupyter
project? Name two languages involved in the Jupyter project other than python.}{3}{10}

\include{_ml/includes/what-is-ml.md}
\include{_ml/includes/overdetermined-inaugural.md}
\include{_ml/includes/nigerian-nmis-data.md}
\include{_ml/includes/probability-intro.md}

\subsection{Assignment Questions}

\notes{The questions in the above lab sheet need to be
answered and handed in before 09:00 on 7th October 2014 (i.e. before next
lecture). The hand should be done via file upload through
[MOLE](http://vle.shef.ac.uk).}

<!--\subsection{More Fun on the Python Data Farm}

\notes{If you want to explore more of the things
you can do with movies and python you might be interested in the `imdbpy` python
library.}

\notes{You can try installing it using `pip` as follows.}

\installcode{IMDbPY}

\notes{If this doesn't work on your machine, try following instructions on
(http://imdbpy.sourceforge.net/)}

\notes{Once you've installed `imdbpy` you can test it
works with the following script, which should list movies with the word 'python'
in their title. To run the code in the following box, simply click the box and
press `SHIFT-enter` or `CTRL-enter`. Then you can try running the code below.}

\code{from imdb import IMDb
ia = IMDb()

for movie in ia.search_movie('python'):
    print(movie)}-->

\includeyoutube{GX8VLYUYScM}{800}{600}

\newslide{Reading}

-   See probability review at end of slides for reminders.

\addreading{@Rogers:book11}{Section 2.2 (pg 41–53)}
\addreading{@Rogers:book11}{Section 2.4 (pg 55–58)}
\addreading{@Rogers:book11}{Section 2.5.1 (pg 58–60)}
\addreading{@Rogers:book11}{Section 2.5.3 (pg 61–62)}

- For other material in  read:

\addreading{@Bishop:book06}{Probability densities: Section 1.2.1 (Pages 17–19)}
\addreading{@Bishop:book06}{Expectations and Covariances: Section 1.2.2 (Pages 19–20)}

\addreading{@Bishop:book06}{The Gaussian density: Section 1.2.4 (Pages 24–28) (don’t worry about material on bias)}
\addreading{@Bishop:book06}{For material on information theory and KL divergence try Section 1.6 & 1.6.1 (pg 48 onwards)}

- If you are unfamiliar with probabilities you should complete the
    following exercises:

\addexercise{@Bishop:book06}{Exercise 1.7}
\addexercise{@Bishop:book06}{Exercise 1.8}
\addexercise{@Bishop:book06}{Exercise 1.9}

\reading

\exercises

\thanks

\references


