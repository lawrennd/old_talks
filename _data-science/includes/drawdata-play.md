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

\include{_datasets/includes/drawdata-data.md}

\code{drawdata_data = data}

\subsection{Simpson's Paradox}

\notes{We introduced [Simpson's paradox](https://en.wikipedia.org/wiki/Simpson%27s_paradox) briefly in the "Review and Refresh" lab session.}


\codeassignment{Use `drawdata` to construct a data set that exhibits Simpson's paradox.

Here's some pandas functionality you might find useful, 

```
pd.DataFrame.corr?
```

and

```
pd.DataFrame.groupby?
```
}{}{10}

\notes{If you want to play some more, why not try and create your own drawing of a Gorilla that gives plausible correlation values for a BMI dataset? But don't spend five hours on this! If you want to draw the data with lines, you can use `draw_line` from `drawdata` instead of `draw_scatter`.}


\endif
