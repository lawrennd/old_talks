\ifndef{rollsRoyceAnalogy}
\define{rollsRoyceAnalogy}
\editme

\section{Public Use of Data for Public Good}

\notes{Since machine learning methods are so dependent on data, Understanding public attitudes to the use of their data is key to developing machine learning methods that maintain the trust of the public. Nowhere are the benefits of machine learning more profound, and the potential pitfalls more catastrophic than in the use of machine learning in health data. 

The promise is for methods that take a personalized perspective on our individual health, but health data is some of the most sensitive data available to us. This is recognised both by the public and by regulation. 

With this in mind The Wellcome Trust launched a report on ["Understanding Patient Data"](https://wellcome.ac.uk/news/understanding-patient-data-launches-today) authored by Nicola Perrin, driven by the National Data Guardian's recommendations.}


\newslide{Understanding Patient Data}

\figure{\includepng{../slides/diagrams/health/understanding-patient-data}{80%}}{The Wellcome Trust \href{https://wellcome.ac.uk/news/understanding-patient-data-launches-today}{surveyed patients} to determine their attitudes to the sharing of their data.}{wellcome-trust}


\notes{From this report we know that patients trust Universities and hospitals more than the trust commercial entities and insurers. However, there are a number of different ways in which data can be mishandled, it is not only the intent of the data-controllers that effects our data security.}

\newslide{WannaCry}
\slides{
\href{https://www.telegraph.co.uk/news/2017/05/12/nhs-hit-major-cyber-attack-hackers-demanding-ransom/}{\includepng{../slides/diagrams/health/wannacry}{80%}}
}
\notes{For example, the recent WannaCry virus attack which demonstrated the unpreparedness of much of the NHS IT infrastructure for a virus exhibiting an exploit that was well known to the security community. The key point is that the public trust the *intent* of academics and medical professionals, but actual *capability* could be at variance with the intent.} 

\newslide{Bush Pilot Model}

\figure{\includejpg{../slides/diagrams/health/bush-pilot-grant-mcconachie}{60%}}{Bush Pilot Grant McConachie. A Bush Pilot is expected to fly the plane, but also to be able to repair it in difficult and isolated conditions.}{bush-pilot-grant-mcconachie}


\notes{The situation is somewhat reminiscient of early aviation. This is where we are with our data science capabilities. By analogy, the engine of the plane is our data security infrastructure, the basic required technology to make us safe. The pilot is the health professional performing data analytics. The nature of the job of early pilots and indeed today's *bush pilots* (who fly to remote places) included a need to understand the mechanics of the engine. Just as a health data scientist, today, needs to deal with security of the infrastructure as well as the nature of the analysis.}

\newslide{}

\slides{
* The difference between *capability* and *intent*.
}

\newslide{}

\figure{\includejpg{../slides/diagrams/health/British_Airways_at_SFO}{70%}}{British Airways 747 at SFO. Today airlines lease their engines from Rolls Royce who take care of maintenance independently from the pilot.}{british-airways-at-sfo}

\notes{I suspect most passengers would find it disconcerting if the pilot of a 747 was seen working on the engine shortly before a flight. As aviation has become more widespread, there is now a separation of responsibilities between pilots and mechanics. For example, Rolls Royce goes so far as to maintain ownership of their engines, and lease them to the airline. The responsibility for maintenance of the engine is entirely with Rolls Royce, yet the pilot is responsibility for the safety of the aircraft and its passengers.

 We need to develop a modern data-infrastructure for which separates the need for security of infrastructure from the decision making of the data analyst.
 
This separation of responsibility according to expertise needs to be emulated when considering health data infrastructure. This resolves the *intent-capability* dilemma, by ensuring a separation of responsibilities to those that are best placed to address the issues.}

\endif
