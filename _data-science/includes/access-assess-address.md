\ifndef{accessAssessAddress}
\define{accessAssessAddress}


\editme

\subsection{The Fynesse Framework}

\slides{* Access
* Assess
* Address}
\notes{Here we present a new framework for thinking about data science. The Fynesse framework splits the activities of the data scientist into three aspects, each aspect is repressented by a one of three words that highlight different activities that occur within a data science project: we call them access, assess and address.}

\notes{Before going deeper into the framework, we will contextualise by looking at some other formalisations of the data analysis pipeline.}

\newslide{CRISP-DM}

\figure{\includepng{\diagramsDir/data-science/1022px-CRISP-DM_Process_Diagram}{50%}}{The CRISP Data Mining Process diagram: it stands for cross industry standard process for data mining. The process was defined in 2000 (@Chapman-step00), well before the modern service oriented architecture approach to software engineering emerged.}{crisp-dm-diagram}

\notes{There are formal processes designed for, e.g., data mining, but they are not always appropriate for operational science or continuous deployment. One is the CRISP-DM @Chapman-step00 process, which does a nice job of capturing the cyclic nature of these processes, but fails to capture the need to build resources that answer questions in real time that occurs in operational science and continuous deployment.}

\define{\terms}{'data mining', 'data science'}
\define{\initials}{dm-ds}

talk-macros.gpp}ata-science/includes/gartner-hype-cycle-base.md}

\notes{We note that the term *data mining* is falling somewhat out of favour, and the CRISP-DM data mining process also feels somewhat dated. In particular software engineering has moved on a great deal since it was defined, with modern software engineering more focussed on service oriented architectures. Software design has a pervasive effect on our ability to do data science.}

\notes{When thinking about the data science process it is important to consider the *software architectures* that are used in large scale decision making systems, and understand what it is that they are bring to help solve these problems.}

\notes{A more modern view from the O'Reilly book *Doing Data Science* frames the problem as shown in Figure \ref{data-science-process-oneil}.}

\newslide{}

>More generally, a data scientist is someone who knows how to extract meaning from and interpret data, which requires both tools and methods from statistics and machine learning, as well as being human. She spends a lot of time in the process of collecting, cleaning, and munging data, because data is never clean. This process requires persistence, statistics, and software engineering skills--—skills that are also necessary for understanding biases in the data, and for debugging logging output from code.
>
> Cathy O'Neil and Rachel Strutt from @ONeil-doing13

\newslide{}

\figure{\includepng{\diagramsDir/data-science/dnds_0202}{70%}}{Another perspective on the data science process, this one from @ONeil-doing13.}{data-science-process-oneil}

talk-macros.gpp}ata-science/includes/experiment-analyze-design.md}

\notes{One challenge for data science and data science processes is that they do not always accommodate the real-time and evolving nature of data science advice as required, for example in pandemic response or in managing an international supply chain.}

\newslide{}

\figure{\includeyoutube{-QjJLgRni-M}{600}{450}}{Data science processes do not always accommodate the real-time and evolving nature of data science advice as required, for example, for policy advice as described in this presentation.}{policy-science-convening-power-of-data}

talk-macros.gpp}ata-science/includes/ride-sharing-soa-doa.md}

\newslide{Inspiration}

\slides{* Operational data science with:
  * Data Science Africa
  * Amazon (particularly in supply chain)
  * The Royal Society DELVE Group (pandemic advice)}
  
\notes{The Fynesse paradigm is inspired by experience in operational data science working with [Data Science Africa](http://www.datascienceafrica.org), deploying in the Amazon supply chain and in the UK Covid-19 pandemic response.}

\newslide{}

\figure{\includeyoutube{5PdHgR6zz1o}{600}{450}}{The challenges of operational data science are closer to the challenges of deploying software and machine learning solutions than a classical analysis. The AutoAI project at Cambridge is focussed on maintaining and explaining AI solutions.} 

\notes{Arguably the challenges for automated data science and deploying complex machine learning solutions are similar. The AutoAI project at Cambridge is focussed on maintaining and explaining machine learning systems. The assumption is that such systems are generally made up of interacting components that make decisions in a composite manner. They have interfaces to the real world where that data is collected, but they also generate data within themselelves. The challenge of collecting data is sometimes less the challenge of pacing the streets and more the challenge of extracting it from existing systems.}

\subsection{The Fynesse Framework}

\slides{* Three *aspects*
  * Access - before data is available electronically
  * Assess - work that can be done *without* the question
  * Address - giving answers to question at hand}

\notes{The Fynesse paradigm considers three *aspects* to data analysis: Access, Assess, Address. In this way it builds on many two stage processes that consider *data collection* and *data wrangling* to be two separate stages. There are two key differences to the Fynesse process. Firstly, the attempt to separate data wrangling tasks into (a) those that can be done *without* knowing the downstream task (Assess) and (b) those that can only be done *with* knowing the downstream task (Address). Naturally, this won't turn out to be a clean separation. But the ethos is to ensure that any reusable tasks that is done in the process of data wrgangling is labelled as such and pushed back into the data ecosystem. Secondly, our use of the term *aspects* instead of stages acknowledges the fact that although there is a natural ordering to the aspects, we find that in practice the data scientist is often moving quicly across the different aspects, so that the mind set of "stages" can be unhelpful}


\subsection{Access}
\slides{* Work to make data electronically accessible.
* Legal work
* Ethical work
* Extraction of data form where it's held
  * mobile phones, within software ecosystem, physical log books
* Associated with data readiness level C.}

\notes{The first aspect we'll consider is *accessing* the data. Depending on domain, the skills needed to address this challenge will vary greatly. For example, [Michael T. Smith](https://www.sheffield.ac.uk/dcs/people/academic/michael-smith) was leading a project in collaboration with the Kampala police force to collate accident data.}

\notes{The *access* aspect is associated with data readiness level C (@Lawrence-drl17).}

\newslide{Access Case Study: Crash Map Kampala}

\slides{
\centerdiv{\jimmyKinyonyiPicture{15%}\michaelSmithPicture{15%}}
\figure{\includepng{\diagramsDir/data-science/crash-map-kampala}{60%}}{Crash Map Kampala was an initiative by Michael T. Smith and Bagonza Jimmy Owa Kinyonyi to map the location, date and severity of vehicle accidents across the city of Kampala. Original storage location for the data was in police log books.}{crash-map-kampala}}

talk-macros.gpp}ata-science/includes/crash-map-kampala.md}

\newslide{Access Automation}

\slides{* Digital Transformation
* Post-Digital Transformation}

\notes{It seems a great challenge to automate all the different aspects of the process of data access, but this challenge is underway already through the process of what is commonly called *digital transformation*. The process of digital transformation takes data away from physical log books and into digital devices. But that transformation process itself comes with challenges. For example, the Kampala police force is not currently equipped to store this data in purely digital form. It would require not only devices (which many officers *will* have access to) but a system of backup and storage that is beyond the capabilities of many organisations.}

\notes{Legal complications around data are still a major barrier though. In the EU and the US database schema and indices are subject to copyright law. Companies making data available often require license fees. As many data sources are combined, the composite effect of the different license agreements often makes the legal challenges insurmountable. This was a common challenge in the pandemic, where academics who were capable of dealing with complex data predictions were excluded from data access due to challenges around licensing. A nice counter example was the work led by Nuria Oliver in Spain who after a call to arms in a national newspaper (@Oliver-valor20) was able to bring the ecosystem together around mobility data.}

\notes{However, even when organisation is fully digital, and license issues are overcome, there are issues around how the data is managed stored, accessed. The discoverability of the data and the recording of its provenance are too often neglected in the process of digtial transformation. Further, once an organisation has gone through digital transformation, they begin making predictions around the data. These predictions are data themselves, and their presence in the data ecosystem needs recording. Automating this portion requires structured thinking around our data ecosystems.}

\subsection{Assess}

\slides{* Only things you can do *without* knowing the "question".
  * This ensures *assess* is reusable across tasks.
* Driven by happenstance data.
* Associated with data readiness level B}

\notes{Data that is accessible can be imported (via APIs or database calls or reading a CSV) into the machine and work can be done understanding the nature of the data. The important thing to say about the assess aspect is that it only includes things you can do *without* the question in mind. This runs counter to many ideas about how we do data analytics. The history of statistics was that we think of the question *before* we collect data. But that was because data was expensive, and it needed to be excplicitly collected. The same mantra is true today of *surveillance data*. But the new challenge is around *happenstance data*, data that is cheaply available but may be of poor quality. The nature of the data needs to be understood before its integrated into analysis. Unfortunately, because the work is conflated with other aspects, decisions are sometimes made during assessment (for example approaches to imputing missing values) which may be useful in one context, but are useless in others. So the aim in *assess* is to only do work that is repeatable, and make that work available to others who may also want to use the data.}

\notes{The assess aspect renders the Fynesse framework quite different form other data science frameworks that split the process into data *wrangling* and data *modelling*. It acknowledges that there is a component to both wrangling and modelling that is specific to the task (this occurs in the *address* aspect) and a component that is useful across tasks (the *assess* aspect). This is important in the wider system because any reusable work can be shared. By keeping this uppermost in the mind through the *assess* aspect, then the wider data ecosystem benefits.}

\notes{The *assess* aspect is associated with data readiness level B (@Lawrence-drl17).}

\newslide{Case Study: Text Mining for Covid Misinformation}

\slides{\centerdiv{\joyceNabendePicture{15%}}
\figure{\includepng{\diagramsDir/data-science/joyce-nabende-uganda-social-media-killing}{60%}}{Misinformation through media has been a challenge for as long as we've been communicating. Social media misinformation is a particular challenge due to the number of possible sources, the scale and speed with which it can propagate. Slide from Joyce Nabende's presentation.}{uganda-social-medial-killing}}

talk-macros.gpp}ata-science/includes/joyce-nabende-text-mining-case-study.md}

\subsection{Automating Assess}

\slides{* Automated scheme detection
* Automated data type detection (@Valera-automatic17)
* The automatic statistician (@Lloyd-automatic14)
* AI for Data Analytics (@Nazabal-engineering20)
* Joyce's case study gives us also POS tagging for new languages.}

\notes{There are lots of interesting projects around automating the assessment of the data, for example one can consider automation of schema and data type detection (@Valera-automatic17) or the AI for Data Analytics Project (see @Nazabal-engineering20 for an overview of issues and case studies and the video in Figure \ref{ai-for-data-analytics} for details on the project). We may even view projects like the automatic statistician as automating of assessment (@Lloyd-automatic14), although arguably one could suggest that the choice of data set used in those projects itself is reflective of the *question* or *context*. This highlights the difficulty in separating the aspects. The key quesiton to ask in any given context is whether the augmentation you are performing for the data set is going to be helpful or a hindrance to those that may wish to reuse your data.}

\newslide{AI for Data Analytics}

\figure{\includeyoutube{wFfeyGmNOAI}{600}{450}}{The AI for Data Analytics project is an attempt to automate some of the challenges of automated data assessment.}{ai-for-data-analytics}

\subsection{Address}

\slides{* Address the question.
* Now we bring the context in.
* Could require:
  * Confirmatory data analysis
  * An ML prediction model
  * Visualisation through a dashboard
  * An Excel spreadsheet
* Associated with data readiness level A.}

\notes{The final aspect of the process is to *address* the question. We'll spend the least time on this aspect here, because it's the one that is most widely formally taught and the one that most researchers are familiar with. In statistics, this might involve some confirmatory data analysis. In machine learning it may involve designing a predictive model. In many domains it will involve figuring out how best to visualise the data to present it to those who need to make the decisions. That could involve a dashboard, a plot or even summarisation in an Excel spreadsheet.}

\notes{The *address* aspect is associated with data readiness level A (@Lawrence-drl17).}


\subsection{Automating Address}

\slides{* Auto ML
* Automatic Statistician
* Automatic Visualization}

\notes{Perhaps the most widespread approach to automating the address aspect is known as AutoML (see video in Figure \ref{frank-hutter-automl}). This is an automatic approach to creating ML prediction models. The automatic statistician we mentioned in assess also has some of these goals in mind for automating confirmatory data analysis. But there are clearly other aspects we may wish to automate, particularly around visualization.}

\newslide{AutoML}

\figure{\includeyoutube{5A4xbv5nd8c}{600}{450}}{Here Frank Hutter gives a tutorial on AutoML, one of the approaches to automating address.}{frank-hutter-automl}

\endif
