\section{Public Use of Data for Public Good}

\notes{Since machine learning methods are so dependent on data, Understanding public attitudes to the use of their data is key to developing machine learning methods that maintain the trust of the public. Nowhere are the benefits of machine learning more profound, and the potential pitfalls more catastrophic than in the use of machine learning in health data. 

The promise is for methods that take a personalized perspective on our individual health, but health data is some of the most sensitive data available to us. This is recognised both by the public and by regulation. 

With this in mind The Wellcome Trust launched a report on ["Understanding Patient Data"](https://wellcome.ac.uk/news/understanding-patient-data-launches-today) authored by Nicola Perrin, driven by the National Data Guardian's recommendations.}



\slides{### Understanding Patient Data

[\includeimg{../slides/diagrams/health/understanding-patient-data.png}](https://wellcome.ac.uk/news/understanding-patient-data-launches-today)}

\notes{From this report we know that patients trust Universities and hospitals more than the trust commercial entities and insurers. However, there are a number of different ways in which data can be mishandled, it is not only the intent of the data-controllers that effects our data security.}

\slides{### WannaCry 

[\includeimg{../slides/diagrams/health/wannacry.png}](https://www.telegraph.co.uk/news/2017/05/12/nhs-hit-major-cyber-attack-hackers-demanding-ransom/)}

\notes{For example, the recent WannaCry virus attack which demonstrated the unpreparedness of much of the NHS IT infrastructure for a virus exhibiting an exploit that was well known to the security community. The key point is that the public trust the *intent* of academics and medical professionals, but actual *capability* could be at variance with the intent.} 

\slides{### Bush Pilot Model}

\includeimg{../slides/diagrams/health/bush-pilot-grant-mcconachie.jpg}{60%}

\aligncenter{*Bush Pilot Grant McConachie*}

\notes{The situation is somewhat reminiscient of early aviation. This is where we are with our data science capabilities. By analogy, the engine of the plane is our data security infrastructure, the basic required technology to make us safe. The pilot is the health professional performing data analytics. The nature of the job of early pilots and indeed today's *bush pilots* (who fly to remote places) included a need to understand the mechanics of the engine. Just as a health data scientist, today, needs to deal with security of the infrastructure as well as the nature of the analysis.}

\slides{###

* The difference between *capability* and *intent*.

###
}

\includeimg{../slides/diagrams/health/British_Airways_at_SFO.jpg}{50%}
\aligncenter{*British Airways 747 at SFO*}

\notes{I suspect most passengers would find it disconcerting if the pilot of a 747 was seen working on the engine shortly before a flight. As aviation has become more widespread, there is now a separation of responsibilities between pilots and mechanics. Indeed, Rolls Royce maintain ownership of their engines today, and merely lease them to the aircraft company. The responsibility for maintenance of the engine is entirely with Rolls Royce, yet the pilot is responsibility for the safety of the aircraft and its passengers.

 We need to develop a modern data-infrastructure for which separates the need for security of infrastructure from the decision making of the data analyst.
 
This separation of responsibility according to expertise needs to be emulated when considering health data infrastructure. This resolves the *intent-capability* dilemma, by ensuring a separation of responsibilities to those that are best placed to address the issues.}

\slides{### 

[\includeimg{../slides/diagrams/health/black-box-thinking.jpg}](https://www.amazon.co.uk/Black-Box-Thinking-Surprising-Success-ebook/dp/B00PW634YQ)
}

\notes{### Propagation of Best Practice


We must also be careful to maintain openness in this new genaration of digital solutions for patient care. Matthew Syed's book, "Black Box Thinking" [@Syed:blackbox15], emphasizes the importance of surfacing errors as a route to learning and improved process. Taking aviation as an example, and contrasting it with the culture in medicine, Matthew relates the story of [Martin Bromiley](https://chfg.org/trustees/martin-bromiley/), an airline pilot whose wife died during a routine hospital procedure and his efforts to improve the culture of safety in medicine. The motivation for the book is the difference in culture between aviation and medicine in how errors are acknowledged and dealt with. We must ensure that these high standards of oversight apply to the era of data-driven automated decision making. 

In particular, while there is much to be gained by involving comemrcial companies, if the process by which they are drawing inference about patient condition is hidden (for example, due to commercial confidentiality), this may prevent us from understanding errors in diagnosis or treatment. This would be a retrograde step. It may be that health device certification needs modification or reform for data-driven automated decision making, but we need a spirit of transparency around how these systems are deriving their inferences to ensure best practice.}
