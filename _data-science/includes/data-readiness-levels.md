\section{Data Readiness Levels}

\newslide{Data Readiness Levels}
\slides{
[\includeimg{../slides/diagrams/data-science/data-readiness-levels.png}](https://arxiv.org/pdf/1705.02245.pdf)

[Data Readiness Levels](http://inverseprobability.com/2017/01/12/data-readiness-levels) [@Lawrence:drl17]
}

\notes{[Data Readiness Levels](http://inverseprobability.com/2017/01/12/data-readiness-levels) [@Lawrence:drl17] are an attempt to develop a language around data quality that can bridge the gap between technical solutions and decision makers such as managers and project planners. The are inspired by Technology Readiness Levels which attempt to quantify the readiness of technologies for deployment.}

\newslide{Three Grades of Data Readiness:}

\notes{Data-readiness describes, at its coarsest level,  three separate stages of data graduation.}

* Grade C - accessibility

* Grade B - validity

* Grade A - usability

\subsection{Accessibility: Grade C}

\notes{The first grade refers to the accessibility of data. Most data science practitioners will be used to working with data-providers who, perhaps having had little experience of data-science before, state that they "have the data". More often than not, they have not verified this. A convenient term for this is "Hearsay Data", someone has *heard* that they have the data so they *say* they have it. This is the lowest grade of data readiness. 

Progressing through Grade C involves ensuring that this data is accessible. Not just in terms of digital accessiblity, but also for regulatory, ethical and intellectual property reasons.}

\slides{* *Hearsay* data.
* Availability, is it actually being recorded?
* privacy or legal constraints on the accessibility of the recorded data, have ethical constraints been alleviated?
* Format: log books, PDF ...
* limitations on access due to topology (e.g. it's distributed across a number of devices)
* At the end of Grade C data is ready to be loaded into analysis software (R, SPSS, Matlab, Python, Mathematica)}

\subsection{Validity: Grade B}

\notes{Data transits from Grade C to Grade B once we can begin digital analysis on the computer. Once the challenges of access to the data have been resolved, we can make the data available either via API, or for direct loading into analysis software (such as Python, R, Matlab, Mathematica or SPSS). Once this has occured the data is at B4 level. Grade B involves the *validity* of the data. Does the data really represent what it purports to? There are challenges such as missing values, outliers, record duplication. Each of these needs to be investigated. 

Grade B and C are important as if the work done in these grades is documented well, it can be reused in other projects. Reuse of this labour is key to reducing the costs of data-driven automated decision making. There is a strong overlap between the work required in this grade and the statistical field of [*exploratory data analysis*](https://en.wikipedia.org/wiki/Exploratory_data_analysis) [@Tukey:exploratory77].}
\slides{
* faithfulness and representation
* visualisations.
* exploratory data analysis
* noise characterisation.
}
\newslide{Grade B Checks}
\slides{
* Missing values.
* Schema alignment, record linkage, data fusion
* Example:
    * Was a column or columns accidentally perturbed (e.g. through a sort operation that missed one or more columns)? Or was a [gene name accidentally converted to a date](http://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-5-80)?
}

\notes{The need for Grade B emerges due to the fundamental change in the availability of data. Classically, the scientific question came first, and the data came later. This is still the approach in a randomized control trial, e.g. in A/B testing or clinical trials for drugs. Today data is being laid down by happenstance, and the question we wish to ask about the data often comes after the data has been created. The Grade B of data readiness ensures thought can be put into data quality *before* the question is defined. It is this work that is reusable across multiple teams. It is these processes that the team which is *standing up* the data must deliver.}


\newslide{Grade B Transition}
\slides{
* At the end of Grade B, ready to define a *task*, or *question*
* Compare with classical statistics:
    * *Classically*: question is first data comes later.
	* *Today*: data is first question comes later.
}

\newslide{Data First}
\slides{
In a *data first* company teams own their data quality issues at least as far as grade B1.
}

\subsection{Usability: Grade A}
\slides{
* The *usability* of data
    * Grade A is about data in context.
* Consider appropriateness of a given data set to answer a particular question or to be subject to a particular analysis.
}

\notes{Once the validity of the data is determined, the data set can be considered for use in a particular task. This stage of data readiness is more akin to what machine learning scientists are used to doing in Universities. Bringing an algorithm to bear on a well understood data set. 

In Grade A we are concerned about the utility of the data given a particular task. Grade A may involve additional data collection (experimental design in statistics) to ensure that the task is fulfilled.

This is the stage where the data and the model are brought together, so expertise in learning algorithms and their application is key. Further ethical considerations, such as the fairness of the resulting predictions are required at this stage. At the end of this stage a prototype model is ready for deployment.

Deployment and maintenance of machine learning models in production is another important issue which Data Readiness Levels are only a part of the solution for.}


\subsection{Recursive Effects}
\slides{
* Grade A may also require:
    * data integration
    * active collection of new data.
    * rebalancing of data to ensure fairness
	* annotation of data by human experts 
	* revisiting the collection (and running through the appropriate stages again)
}

\newslide{A1 Data}
\slides{
* A1 data is ready to make available for *challenges* or *AutoML* platforms.
}

\newslide{Contribute!}
\slides{

\aligncenter{<http://data-readiness.org>}}

\notes{To find out more, or to contribute ideas go to <http://data-readiness.org>}

\newslide{Also ...}
\slides{
* Encourage greater interaction between application domains and data scientists
* Encourage *visualization* of data
}

\notes{Throughout the data preparation pipeline, it is important to have close interaction between data scientists and application domain experts. Decisions on data preparation taken outside the context of application have dangerous downstream consequences. This provides an additional burden on the data scientist as they are required for each project, but it should also be seen as a learning and familiarization exercise for the domain expert. Long term, just as biologists have found it necessary to assimilate the skills of the bioinformatician to be effective in their science, most domains will also require a familiarity with the nature of data driven decision making and its application. Working closely with data-scientists on data preparation is one way to begin this sharing of best practice.

The processes involved in Grade C and B are often badly taught in courses on data science. Perhaps not due to a lack of interest in the areas, but maybe more due to a lack of access to real world examples where data quality is poor. 

These stages of data science are also ridden with ambiguity. In the long term they could do with more formalization, and automation, but best practice needs to be understood by a wider community before that can happen.}

