\subsection{Data}
\slides{
* Hard to overstate its importance.
* Half the equation of $\text{data} + \text{model}$.
* Often utterly neglected.
}
\newslide{Data Neglect}
\slides{
* Arises for two reasons.
    1. Data cleaning is perceived as tedious. 
	2. Data cleaning is complex.
}	
\notes{It is difficult to overstate the importance of data. It is half of the
equation for machine learning, but is often utterly neglected. We can
speculate that there are two reasons for this. Firstly, data cleaning is
perceived as tedious. It doesn’t seem to consist of the same
intellectual challenges that are inherent in constructing complex
mathematical models and implementing them in code. Secondly, data
cleaning is highly complex, it requires a deep understanding of how
machine learning systems operate and good intuitions about the data
itself, the domain from which data is drawn (e.g. Supply Chain) and what
downstream problems might be caused by poor data quality.}

\newslide{Data Cleaning}
\slides{
* Seems difficult to formulate into readily teachable princples.
* Heavily neglected in data science, statistics and ML courses.
* In practice most scientists spend around 80% of time data cleaning.
}

\notes{A consequence of these two reasons, data cleaning seems difficult to
formulate into a readily teachable set of principles. As a result it is
heavily neglected in courses on machine learning and data science.
Despite data being half the equation, most University courses spend
little to no time on its challenges.}

\notes{Anecdotally, talking to data modelling scientists. Most say they spend
80% of their time acquiring and cleaning data. This is precipitating
what I refer to as the “data crisis”. This is an analogy with software.
The “software crisis” was the phenomenon of inability to deliver
software solutions due to increasing complexity of implementation. There
was no single shot solution for the software crisis, it involved better
practice (scrum, test orientated development, sprints, code review),
improved programming paradigms (object orientated, functional) and
better tools (CVS, then SVN, then git).}



\newslide{The Data Crisis}

\include{_data-science/includes/the-data-crisis.md}

\notes{Data is the new software, and the data crisis is already upon us. It is
driven by the cost of cleaning data, the paucity of tools for monitoring
and maintaining our deployments, the provenance of our models (e.g. with
respect to the data they’re trained on).}


\notes{Three principal changes need to occur in response. They are cultural and
infrastructural.}

\subsection{The Data First Paradigm}

\notes{First of all, to excel in data driven decision making we need to move
from a *software first* paradigm to a *data first* paradigm. That means
refocusing on data as the product. Software is the intermediary to
producing the data, and its quality standards must be maintained, but
not at the expense of the data we are producing. Data cleaning and
maintenance need to be prized as highly as software debugging and
maintenance. Instead of *software* as a service, we should refocus
around *data* as a service. This first change is a cultural change in
which our teams think about their outputs in terms of data. Instead of
decomposing our systems around the software components, we need to
decompose them around the data generating and consuming components.[^technical-debt]
Software first is only an intermediate step on the way to be coming
*data first*. It is a necessary, but not a sufficient condition for
efficient machine learning systems design and deployment. We must move
from *software orientated architecture* to a *data orientated
architecture*.

[^technical-debt]: This is related to challenges of machine learning and technical debt [@Sculley:debt15], although we are trying to frame the solution here rather than the problem.}

\subsection{Data Quality}

\notes{Secondly, we need to improve our language around data quality. We cannot
assess the costs of improving data quality unless we generate a language
around what data quality means. Data Readiness Levels[^data-readiness-levels] are an assessment of data quality that is based on the usage to which data is
put.

[^data-readiness-levels]: [Data Readiness Levels](http://inverseprobability.com/2017/01/12/data-readiness-levels) [@Lawrence:drl17] are an attempt to develop a language around data quality that can bridge the gap between technical solutions and decision makers such as managers and project planners. The are inspired by Technology Readiness Levels which attempt to quantify the readiness of technologies for deployment.
}

\include{_data-science/includes/data-readiness-levels.md}

\recommendation{Build a shared understanding of the language of data readiness levels for use in planning documents and costing of data cleaning and the benefits of reusing cleaned data.}

\subsection{Move Beyond Software Engineering to Data Engineering}

\notes{Thirdly, we need to improve our mental model of the separation of data science from applied science. A common trap in our thinking around data is to see data science (and data engineering, data preparation) as a sub-set of the software engineer’s or applied scientist’s skill set. As a result we recruit and deploy the wrong type of resource. Data preparation and question formulation is superficially similar to both because of the need for programming skills, but the day to day problems faced are very different.}
