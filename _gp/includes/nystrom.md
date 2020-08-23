\ifndef{nystrom}
\define{nystrom}
\editme
\newslide{Nystr\"om Method}

\includeimg{\diagramsDir/cov_approx.png}{90%}{negate}
\caption{Figure originally from presentation by Ed Snelson at NIPS}
\notes{The Nystr\"om approximation takes the form,}
$$
\Kff \approx \Qff = \Kfu \Kuu^{-1}\Kuf
$$
\notes{The idea is that instead of inverting $\Kff$, we make a low rank (or Nyström) approximation, and invert $\Kuu$ instead.

In the original Nystr\"om method the columns to incorporate are sampled from the complete set of columns (without replacement). In a kernel matrix each of these columns corresponds to a data point. In the Nystr\"om method these points are sometimes called *landmark* points.}


\endif


