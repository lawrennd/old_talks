\ifndef{crashMapKampala}
\define{crashMapKampala}

\editme

\subsection{Crash Map Kampala}

\notes{The Crash Map Kampala project is a good example of a data science project where a major challenge was *access*.}

\aligncenter{\jimmyKinyonyiPicture{15%}\michaelSmithPicture{15%}}

\figure{\includepng{\diagramsDir/data-science/crash-map-kampala}{60%}}{Crash Map Kampala was an initiative by Michael T. Smith and Bagonza Jimmy Owa Kinyonyi to map the location, date and severity of vehicle accidents across the city of Kampala. Original storage location for the data was in police log books.}{crash-map-kampala}

\notes{The project is work from [Bagonza Jimmy Owa Kinyony](https://www.linkedin.com/in/bagonza-jimmy-kinyonyi-b73620125/?originalSubdomain=ug) when he was an MSc student and [Michael T. Smith](https://www.sheffield.ac.uk/dcs/people/academic/michael-smith) when he was based at [Makerere University AI-LAB](https://air.ug/).}

\notes{The project was inspired by the observation that road traffic accidents are a leading cause of death for the young in many contexts, but the scale of the cause is difficult to compare directly because the number of deaths and serious injuries are difficult to access.}

\notes{In Kampala this data is stored in log books at local police stations. Jimmy was in the Kampala police at the time, so the project focus was transcribing this information into a digital format where it could be mapped.}

\newslide{}

\notes{Due to the scale of the task, the approach of crowd sourcing the work was considered. This approach was also what launched the AI revolution through the ImageNet challenge, where data was labelled through Mechanical Turk (@Russakovsky-imagenet15).}

\figure{\includepng{\diagramsDir/data-science/crash-map-kampala-location}{60%}}{}{The location of the crash requires some local understanding of Kampala and how different locations may be referred to locally vs by the map provider.}{crash-map-kampala-location}

\notes{But there are additional challenges with this data. The log books are typically accessed only by members of Kampala's police force, in their recording of the accidents. So, permission from the police force was important. Additionally, personal information about those involved in the accidents might have been revealed in the process of crowdsourcing the work.}

\newslide{}

\figure{\includepng{\diagramsDir/data-science/crash-map-kampala-date-time}{60%}}{Alongside the location, the date and time of the crash gives more information that can be used to map crashes over time.}{crash-map-kampala-date-time}

\notes{Much of the work here was therefore in the *access* of the data. Photographing the log books, obtaining legal permission from the Kampala police, ensuring that personal information was unlikely to be divulged.}

\newslide{}

\figure{\includepng{\diagramsDir/data-science/crash-map-kampala-severity}{60%}}{The severity of the crash is helpful in understanding how people are being affected by road accidents.}{crash-map-kampala-severity}

\notes{As well as software design and build, the work has legal and ethical issues. An important aspect in gaining progress was that Jimmy worked for the Kampala police. Indeed, the work eventually stalled when Jimmy was moved to a differen police location.}

\newslide{}

\figure{\includepng{\diagramsDir/data-science/crash-map-kampala-vehicles}{60%}}{Understanding which vehicles are involved in accidents could also help with interventions that may be necessary.}{crash-map-kampala-vehicles}

\notes{The possiblity of leaking personal information was reduced, by presenting only a portion of each log book page to users for analysis. So we can see in Figure \ref{crash-map-kampala-location} the interface for obtainin the location from the log book. But the the date and time (Figure \ref{crash-map-kampala-date-time}) the severity of the accident (Figure \ref{crash-map-kampala-severity}) and the vehicles involved (Figure \ref{crash-map-kampala-vehicles}) are all dealt with in separate parts of the interface.}

\newslide{}

\figure{\includepng{\diagramsDir/data-science/crash-map-kampala-vehicles-2}{60%}}{}{crash-map-kampala-vehicles-2}


\endif
