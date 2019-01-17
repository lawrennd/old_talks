\ifndef{mlCombiningDataAndSystemsDesignChallenge}
\define{mlCombiningDataAndSystemsDesignChallenge}
\editme

\notes{\subsection{Combining Data and Systems Design}}

\newslide{Data Science as Debugging}
\slides{
* Analogies: For Software Engineers [describe data science as *debugging*](http://inverseprobability.com/2017/03/14/data-science-as-debugging).
}

\notes{One analogy I find helpful for understanding the depth of change we need
is the following. Imagine as an engineer, you find a USB stick on the
ground. And for some reason you *know* that on that USB stick is a
particular API call that will enable you to make a significant positive
difference on a business problem. However, you also know on that USB
stick there is potentially malicious code. The most secure thing to do
would be to *not* introduce this code into your production system. But
what if your manager told you to do so, how would you go about
incorporating this code base?}

\notes{The answer is *very* carefully. You would have to engage in a process
more akin to debugging than regular software engineering. As you
understood the code base, for your work to be reproducible, you should
be documenting it, not just what you discovered, but how you discovered
it. In the end, you typically find a single API call that is the one
that most benefits your system. But more thought has been placed into
this line of code than any line of code you have written before.}

\notes{Even then, when your API code is introduced into your production system,
it needs to be deployed in an environment that monitors it. We cannot
rely on an individual’s decision making to ensure the quality of all our
systems. We need to create an environment that includes quality
controls, checks and bounds, tests, all designed to ensure that
assumptions made about this foreign code base are remaining valid.}

\notes{This situation is akin to what we are doing when we incorporate data in
our production systems. When we are consuming data from others, we
cannot assume that it has been produced in alignment with our goals for
our own systems. Worst case, it may have been adversarialy produced. A
further challenge is that data is dynamic. So, in effect, the code on
the USB stick is evolving over time.}

\recommendation{Anecdotally, resolving a machine learning challenge requires 80% of the
resource to be focused on the data and perhaps 20% to be focused on the
model. But many companies are too keen to employ machine learning
engineers who focus on the models, not the data. We should change our hiring priorities and training. Universities cannot provide the understanding of how to data-wrangle. Companies must fill this gap.}

\newslide{}

\figure{
\includejpg{../slides/diagrams/data-science/water-bridge-hill-transport-arch-calm-544448-pxhere.com}{80%}
\notes{\caption{A reservoir of data has more value if the data is consumbable. The data crisis can only be addressed if we focus on outputs rather than inputs.}}
}

\newslide{}

\figure{
\includejpg{../slides/diagrams/data-science/1024px-Lake_District_picture}{80%}
\notes{\caption{For a data first architecture we need to clean our data at source,
rather than individually cleaning data for each task. This involves a
shift of focus from our inputs to our outputs. We should provide data
streams that are consumable by many teams without purification.}}
}

\recommendation{We need to share best practice around data deployment across our teams. We should make best use of our processes where applicable, but we need to develop them to become *data first* organizations. Data needs to be cleaned at *output* not at *input*.}

\endif
