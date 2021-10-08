\ifndef{joyceNabendeTextMiningCaseStudy}
\define{joyceNabendeTextMiningCaseStudy}

\editme

\subsection{Case Study: Text Mining for Misinformation}

\aligncenter{\joyceNabendePicture{15%}}

\notes{We consider a case study from Joyce Nabende, Head of the [Makerere AI Lab](https://air.ug/). This case study is based on a presentation given by Joyce to the DSA Research Grants, "Project Progress" session on 20th August 2021.}

\notes{The aim of the case study is to map some of the approaches used by Joyce onto the Access, Assess, Address paradigm.}

\notes{The aim of the project is to develop tools for automated misinformation detection. Web, mobile based social media platforms. Social media posts are invalid, inaccurate, potentially harmful. This is set within the context of the Covid-19 pandemic within Uganda.}

\newslide{}

\figure{\includepng{\diagramsDir/data-science/joyce-nabende-uganda-social-media-killing}{60%}}{Misinformation through media has been a challenge for as long as we've been communicating. Social media misinformation is a particular challenge due to the number of possible sources, the scale and speed with which it can propagate. Slide from Joyce Nabende's presentation.}{uganda-social-medial-killing}

\notes{In common with many applications of data science, and in line with traditional statistics, the question here comes first, at the beginning of the data collection. But the access of the data is made easier by the fact that the data exists in the digital space already. There are APIs for collecting data from Facebook and Twitter.}

\notes{The focus here will be trying to understand which parts of this data collection process might be reusable for others. The aim is to separate those reusable parts from aspects that are specific to the question.}

\newslide{}

\figure{\includepng{\diagramsDir/data-science/napoleoncat-social-media-statistics-facebook-users-in-uganda_2021_06}{70%}}{Social media is widespread in Uganda, perhaps largely due to widespread availability of mobile phone access.}{napoleoncat-social-media-statistics-facebook-users-in-uganda_2021_06}

\notes{As with any data science problem, it's vital that domain knowledge is included in the analysis of the problem. To set context, we see in Figure \ref{napoleoncat-social-media-statistics-facebook-users-in-uganda_2021_06} how widespread use of social media is in Uganda for different age groups. The total population of Uganda is around 47 million.}

\newslide{}

\figure{\includepng{\diagramsDir/data-science/joyce-nabende-data-science-objective}{90%}}{The objective of the project is to track misinformation and understandperceptions of Ugandan Government's COVID-19 transmission mitigation strategies.}{joyce-nabende-data-science-objective}

\notes{One particular challenge for this project is dealing with a data set with multiple languages. In Uganda, people don't just communicate in English, but they will [code-switch](https://en.wikipedia.org/wiki/Code-switching) or communicate purely in, e.g. Luganda. Tools and resources for dealing with code-switching or the Lugandan language in NLP are much less common than tools for dealing with high resource languages (e.g. German, English, French, Spanish, Mandarin). See @Magueresse-lowresource20 for a review of NLP in low resource languages, multilingual data sets bring their own problems @Aman-dataset20.}

\newslide{}

\slides{\figure{\includepng{\diagramsDir/data-science/joyce-nabende-the-luganda-language}{90%}}{}{joyce-nabende-the-luganda-language}}

\notes{The Luganda language is the most widely spoken indigenous language in Uganda with more than seven million speakers. By definition, a low resourced language has less capabilities for data annotation and augmentation, e.g. part of speech taggers.}

\subsection{Data Access}

\notes{The social media data was collected from a set of pages (media institutions, ministry of health, media personalities, top twitter/facebook users from Uganda. All data was then filtered using keywords, 'ssenyiga', 'kolona', 'corona' ,'virus' ,'obulwadde', 'corona', 'covid', 'abalwadde', 'ekirwadde', 'akawuka', 'staysafeug', 'stayhome', 'tonsemberera', 'tokwatakudereva', 'vaccine' to select with Covid-19 related tweets. Very short Facebook posts were also removed. Data was collected in two phases, from March 2020 - March 2021 and then from June 2021 - August 2021. Raw data points 15,354 posts from twitter and 430,075 from Facebook.}

\notes{Note that in this case, knowledge of the question has been used in accessing the data. The context of the data is Uganda and the focus is Covid-19. That focus is driven by the pandemic. However, as we see when we get to data assessment, there is still an amount of reusable work that could/should be automated.}

\newslide{}

\subsection{Data Assessment}

\slides{Data Exploration
- Used the initial data analysis phase to understand the data, uncover patterns, get insights within the data.
- Generated word clouds from the raw dataset.
- Performed topic modelling using Latent Dirichlet Allocation (LDA) to discover topics and similarity of the data for Covid-19 on social media.}

\notes{After collecting data, the initial assessment was formed to understand the data, uncover patterns and gain insights. Here various visualisations can be used to find any unexpected factors in the data.}

\newslide{}

\figure{\includepng{\diagramsDir/data-science/joyce-nabende-word-cloud-twitter}{60%}}{Word cloud from the Twitter data collected through the filtering.}{joyce-nabende-word-cloud-twitter}

\notes{In the case of the Uganda data set, Joyce found that mixed in with the Covid-19 data were topics focussed on popular Ugandan TV shows and the Ugandan election.}

\newslide{}

\figure{\includepng{\diagramsDir/data-science/joyce-nabende-word-cloud-facebook}{60%}}{Word cloud from the Facebook data collected through the filtering.}{joyce-nabende-word-cloud-twitter}

\newslide{}

\figure{\includepng{\diagramsDir/data-science/joyce-nabende-lda-topics}{90%}}{LDA topics and topic distance maps. Interspersed with the Covid-19 topics are topics associated with television dance shows, elections, and the president showing the importance of having domain knowledge.}{joyce-nabende-lda-topics}

\notes{Topic modeling highlights the different subjects present in the data, and how they interrelate.}

\newslide{Data Annotation Process}

\slides{- Carried out by 7 annotators who could read/comprehend English and Luganda
- Used the [Doccano Tool](https://github.com/doccano/doccano) - an open source text annotation tool.
- Annotation attributes:
a. Data source [Facebook, Twitter]
b. Language [English, Luganda, and codemixed]
c. Aspect [truck drivers, hospitals, vaccine, cases, SOPs, NPIs, Testing, Border, Covid19_Impact, Presidential address, death, elections and Covid19]
d. Sentiment [positive, negative and neutral]
e. Misinformation [Not Fake, Fake, Partially Fake, and Others]
- As part of quality assurance, the data was reviewed by an independent team to ensure that the annotation guidelines were followed.}

\notes{Annotation carried out by seven annotators who could understand both English and Luganda. The data was labeled with the [Doccano](https://github.com/doccano/doccano) text annotation tool. Annotations included the data source, the language, the label, the sentiment and the misinformation status.}

\notes{Quality assurance performed by reviewing data with an independent team for ensuring annotation guidelines were followed.

\newslide{}

\table{

|  | Twitter Data | Facebook Data |
| :--- | :--- | :--- |
| Initial dataset | 15,354 | 430,075 |
| Dataset after Annotation | 3,527 | 4,479 |

}{Portion of data that was annoted.}{annotated-portion-of-data}

\newslide{}

[Cohen's kappa](https://en.wikipedia.org/wiki/Cohen%27s_kappa) inter-annotation used to measure annotator agreement.

\table{

| Language | 0.89 |
| :--- | :--- |
| Aspect | 0.69 |
| Sentiment | 0.73 |
| Misinformation | 0.74 |

}{Cohen's kappa agreement scores for the data.}{cohen-kappa-agreement}


\newslide{}

\figure{\includepng{\diagramsDir/data-science/joyce-nabende-data-annotation-example}{70%}}{Example of data annotation for sentiment and misinformation from the data set.}{joyce-nabende-data-annotation-example}

\notes{The idea of the analysis is to bring this information together for sentiment and misinformation analysis in a [dashboard for Covid-19 in Uganda](https://dsa-uganda.herokuapp.com/dashboard/).}

\endif
