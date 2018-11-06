\notes{Anecdotally, talking to data modelling scientists. Most say they spend
80% of their time acquiring and cleaning data. This is precipitating
what I refer to as the “data crisis”. This is an analogy with software.
The “software crisis” was the phenomenon of inability to deliver
software solutions due to increasing complexity of implementation. There
was no single shot solution for the software crisis, it involved better
practice (scrum, test orientated development, sprints, code review),
improved programming paradigms (object orientated, functional) and
better tools (CVS, then SVN, then git).}

\notes{However, these challenges aren't new, they are merely taking a different
form. From the computer's perspective software *is* data. The first wave
of the data crisis was known as the *software crisis*.
}

\subsection{The Software Crisis}

\slidesmall{

>The major cause of the software crisis is that the machines have
>become several orders of magnitude more powerful! To put it quite
>bluntly: as long as there were no machines, programming was no problem
>at all; when we had a few weak computers, programming became a mild
>problem, and now we have gigantic computers, programming has become an
>equally gigantic problem.
>
> Edsger Dijkstra (1930-2002), The Humble Programmer

}

\notes{In the late sixties early software programmers made note of the
increasing costs of software development and termed the challenges
associated with it as the "[Software
Crisis](https://en.wikipedia.org/wiki/Software_crisis)". Edsger Dijkstra
referred to the crisis in his 1972 Turing Award winner's address.}

\subsection{The Data Crisis}

\slidesmall{

>The major cause of the data crisis is that machines have become more
>interconnected than ever before. Data access is therefore cheap, but
>data quality is often poor. What we need is cheap high quality
>data. That implies that we develop processes for improving and
>verifying data quality that are efficient.
>
>There would seem to be two ways for improving efficiency. Firstly, we
>should not duplicate work. Secondly, where possible we should automate
>work. 
\slides{>
> Me}
}
\notes{What I term "The Data Crisis" is the modern equivalent of this problem.
The quantity of modern data, and the lack of attention paid to data as
it is initially "laid down" and the costs of data cleaning are bringing
about a crisis in data-driven decision making. This crisis is at the
core of the challenge of *technical debt* in machine learning [@Sculley:debt15].}

\notes{Just as with software, the crisis is most correctly addressed by
'scaling' the manner in which we process our data. Duplication of work
occurs because the value of data cleaning is not correctly recognised in
management decision making processes. Automation of work is increasingly
possible through techniques in "artificial intelligence", but this will
also require better management of the data science pipeline so that data
about data science (meta-data science) can be correctly assimilated and
processed. The Alan Turing institute has a program focussed on this
area, [AI for Data Analytics](https://www.turing.ac.uk/research_projects/artificial-intelligence-data-analytics/).}
