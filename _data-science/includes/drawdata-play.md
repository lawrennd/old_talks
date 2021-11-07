\ifndef{dataDrawPlay}
\define{dataDrawPlay}

\editme

\subsection{Playing with Data Draw}

\notes{This section is inspired by [a blog post by Tony Hirst](https://blog.ouseful.info/)[^hot-tip] who talks about the importance of *play*.

[^hot-tip]: Many of the most interesting blog posts are hard to find on Google because it's become dominate by sites that are well optimized for search engines. Even when useful, I find the click-bait titles of the posts that surface on sites like towardsdatascience off-putting: "Four ways of Plotting Data you Must Know About" or "Eight Things Every Data Scientist Sould Know" or "Do you remember this ggplot command? You won't believe what it looks like today!" or "Five Other Cambridge Data Scientists are Currently Using this Trick to Understand their Data". OK ... I made the last two up. Well I made them all up, but I've not seen ones like the last two ... but I have seen snippets of useful information masquerading under the other titles on medium/towardsdatascience, but the overall posts are usually quite vacuous.}


\notes{
> One of the most powerful learning techniques I know that works for me is play, the freedom to explore an idea or concept or principle in an open-ended, personally directed way, trying things out, test them, making up “what if?” scenarios, and so on.
>
> Playing takes time of course, and the way we construst courses means that we donlt give students time to play, preferring to overload them with lots of stuff read, presumably on the basis that stuff = value.
>
> If I were to produce a 5 hour chunk of learning material that was little more three or four pages of text, defining various bits of playful activity, I suspect that questions would be asked on the basis that 5 hours of teaching should include lots more words… I also suspect that the majority of students would not know how to play consructively within the prescribed bounds for that length of time.
>
> Tony Hirst @Hirst-supporting21}


\notes{OK, we'll try and keep this session below five hours, but Tony's instinct is quite correct here. You will learn more from playing with data than in any formal session. So let's give it a try in the way Tony suggests.}

\include{_datasets/include/drawdata-data.md}

\code{drawdata_data = data}

\notes{We introduced Simposon's paradox briefly in the "Review and Refresh" lab session.}


\setupplotcode{import matplotlib.pyplot as plt
import mlai
import mlai.plot as plot}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_figsize)
im = ax.matshow(drawdata_data.corr())
ax.set_xticks([0.5, 1.5, 2.5, 3.5])
ax.set_xticklabels(drawdata_data.columns, fontsize=14, rotation=45)
ax.set_yticks([0, 1, 2, 3])
ax.set_yticklabels(drawdata_data.columns, fontsize=14)

fig.colorbar(im, ax=ax)

mlai.write_figure(filename="drawdata-correlation-matrix.svg", directory="\writeDiagramsDir/data-science")}

\figure{\includediagram{\diagramsDir/data-science/drawdata-correlation-matrix}{50%}}{Correlation matrix derived from drawing a data set with `drawdata`.}


\codassignment{Use `drawdata` to construct a data set that exhibits Simpson's paradox.}{}{10}

\notes{If you want to play some more, why not try and create your own drawing of a Gorilla that gives plausible correlation values for a BMI dataset? But don't spend five hours on this ;-)!}


\endif
