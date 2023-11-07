\ifndef{mocapPpca}
\define{mocapPpca}

\editme


\subsection{Examples: Motion Capture Data}

For our first example we'll consider some motion capture data of a
man breaking into a run. [Motion capture data](http://en.wikipedia.org/wiki/Motion_capture) involves capturing a 3-d point cloud to represent a character, often by an underlying skeleton. For this data set, from Ohio State University, we have 54 frame of motion capture, each frame containing 102 values, which are the 3-d locations of 34 different points from the subject's skeleton.

\setupcode{import pods}
\code{data = pods.datasets.osu_run1()
Y = data['Y']}

Once the data is loaded in we can examine the first two principal components as
follows,

\code{q = 2
U, ell, sigma2 = ppca(Y, q)
mu_x, C_x = posterior(Y, U, ell, sigma2)}

\setupcode{import matplotlib.pyplot as plt}
\code{plt.plot(mu_x[:, 0], mu_x[:, 1], 'rx-')}

Here because the data is a time course, we have connected points that are
neighbouring in time. This highlights the form of the run, which involves 3
paces. This projects in our low dimensional space to 3 loops. We can examin how
much residual variance there is in the system by looking at `sigma2`.

\code{print(sigma2)}

\endif
