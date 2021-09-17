\ifndef{accessAssessAddress}
\define{accessAssessAddress}


\editme

\subsection{The Four Esses Framework}

\slides{* Access
* Assess
* Address}
\notes{Here we present a framework for thinking about data science that has three words that are meant to highlight three distinct types of data science activity that occur within a data science project: we call them access, assess and address.}

\newslide{CRISP-DM}

\figure{\includepng{\diagramsDir/data-science/1022px-CRISP-DM_Process_Diagram}{50%}}{The CRISP Data Mining Process diagram.}{crisp-dm-diagram}

\notes{There are formal processes designed for, e.g., data mining, but they are not always appropriate for operational science or continuous deployment. One is the CRISP-DM @Chapman-step00 process, which does a nice job of capturing the cyclic nature of these processes, but fails to capture the need to build resources that answer questions in real time that occurs in operational science and continuous deployment.}

\notes{A more modern view from the O'Reilly book *Doing Data Science* frames the problem as shown in Figure \ref{Oneil-doing14}}

\figure{\includepng{\diagramsDir/data-science/data-science-process}}{Another perspective on the data science process, this one from @

\newslide{}

\figure{\includeyoutube{-QjJLgRni-M}{600}{450}}{Data science processes do not always accommodate the real-time and evolving nature of data science advice as required, for example, for policy advice as described in this presentation.}{policy-science-convening-power-of-data}

\notes{The "Access, Assess, Address" paradigm is inspired by experience in operational data science both in the Amazon supply chain and in dealing with the UK pCovid-19 pandemic.}

\newslide{}

\figure{\includeyoutube{5PdHgR6zz1o}{600}{450}}{The challenges of operational data science are closer to the challenges of deploying software and machine learning solutions than a classical analysis. The AutoAI project at Cambridge is focussed on maintaining and explaining AI solutions.} 

\notes{Arguably the challenges for automated data science and deploying complex machine learning solutions are similar. The AutoAI project at Cambridge is focussed on maintaining and explaining machine learning systems. The assumption is that such systems are generally made up of interacting components that make decisions in a composite manner. They have interfaces to the real world where that data is collected, but they also generate data within themselelves. The challenge of collecting data is sometimes less the challenge of pacing the streets and more the challenge of extracting it from existing systems.}

\subsection{Access}

\notes{In the Access, Assess, Address paradigm, the first challenge is accessing the data. Depending on domain, the skills needed to address this challenge will vary greatly. For example, [Michael T. Smith](https://www.sheffield.ac.uk/dcs/people/academic/michael-smith) was leading a project in collaboration with the Kampala police force to collate accident data.}

\include{_data-science/includes/crash-map-kampala.md}


\subsection{Assess}

\include{_data-science/includes/joyce-nabende-text-mining-case-study.md}

@Nazabal-engineering20

\subsection{Schema Detection}

@Valera-automatic17
@Lloyd-automatic14
\subsection{AI for Data Analytics}

\includeyoutube{wFfeyGmNOAI}{600}{450}


\subsection{AutoML}

\includeyoutube{5A4xbv5nd8c}{600}{450}

\endif
