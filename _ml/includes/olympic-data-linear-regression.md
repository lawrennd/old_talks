\ifndef{olympicDataLinearRegression}
\define{olympicDataLinearRegression}

\editme

\section{Linear Algebra}

\notes{Linear algebra provides a very similar role, when we introduce [linear algebra](http://en.wikipedia.org/wiki/Linear_algebra), it is because we are faced with a large number of addition and multiplication operations. These operations need to be done together and would be very tedious to write down as a group. So the first reason we reach for linear algebra is for a more compact representation of our mathematical formulae.}

\notes{
\subsection{Running Example: Olympic Marathons}

Now we will load in the Olympic marathon data. This is data of the olympic marath times for the men's marathon from the first olympics in 1896 up until the London 2012 olympics.}

\setupcode{import pods}
\code{data = pods.datasets.olympic_marathon_men()
x = data['X']
y = data['Y']}

\notes{You can see what these values are by typing:}

\code{print(x)
print(y)}

\notes{Note that they are not `pandas` data frames for this example, they are just arrays of dimensionality $\numData\times 1$, where $\numData$ is the number of data.}

\notes{The aim of this lab is to have you coding linear regression in python. We will do it in two ways, once using iterative updates (coordinate ascent) and then using linear algebra. The linear algebra approach will not only work much better, it is easy to extend to multiple input linear regression and *non-linear* regression using basis functions.}

\notes{
\subsection{Plotting the Data}

You can make a plot of $\dataScalar$ vs $\inputScalar$ with the following command:}

\setupcode{%matplotlib inline 
import matplotlib.pyplot as plt}

\code{plt.plot(x, y, 'rx')
plt.xlabel('year')
plt.ylabel('pace in min/km')}

\notes{
\subsection{Maximum Likelihood: Iterative Solution}

Now we will take the maximum likelihood approach we derived in the lecture to fit a line, $\dataScalar_i=m\inputScalar_i + c$, to the data you've plotted. We are trying to minimize the error function:
$$
\errorFunction(m, c) =  \sum_{i=1}^\numData(\dataScalar_i-m\inputScalar_i-c)^2
$$
with respect to $m$, $c$ and $\sigma^2$. We can start with an initial guess for $m$,}

\code{m = -0.4
c = 80}

\notes{Then we use the maximum likelihood update to find an estimate for the offset, $c$.}

\endif
