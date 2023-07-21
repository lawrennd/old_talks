\ifndef{conversationProbability}
\define{conversationProbability}
\editme
\newslide{}

\notes{\subsection{Probability Conversations}}

\setupdisplaycode{import notutils as nu
from ipywidgets import IntSlider}


\setupdisplaycode{import notutils as nu}
\displaycode{nu.display_plots('\stubname{sample:0>3}.svg', 
                            '\diagramsDir/ai',  sample=IntSlider(0, 0, 7, 1))}

\define{\stubname}{anne-probability-conversation}

\define{\divoptions}{maxwidth:100vw; max-height:100vh}
\define{\widthVal}{80%}
\newslide{}

\slides{\includediagram{\diagramsDir/ai/\concat{\stubname}{000}}{\widthVal}}

\newslide{}

\slides{\includediagram{\diagramsDir/ai/\concat{\stubname}{001}}{\widthVal}}

\newslide{}

\slides{\includediagram{\diagramsDir/ai/\concat{\stubname}{002}}{\widthVal}}

\newslide{}

\slides{\includediagram{\diagramsDir/ai/\concat{\stubname}{003}}{\widthVal}}

\newslide{}

\slides{\includediagram{\diagramsDir/ai/\concat{\stubname}{004}}{\widthVal}}

\newslide{}

\slides{\includediagram{\diagramsDir/ai/\concat{\stubname}{005}}{\widthVal}}

\newslide{}

\slides{\includediagram{\diagramsDir/ai/\concat{\stubname}{006}}{\widthVal}}

\newslide{}

\slides{\includediagram{\diagramsDir/ai/\concat{\stubname}{007}}{\widthVal}}

\notes{\figure{\includediagram{\diagramsDir/ai/\concat{\stubname}{006}}{80%}}{The focus so far has been on reducing uncertainty to a few representative values and sharing numbers with human beings.}{anne-probability-conversation-6}}

\notes{\figure{\includediagram{\diagramsDir/ai/\concat{\stubname}{007}}{80%}}{We forget that most people can be confused by basic probabilities for example the prosecutor's fallacy.}{anne-probability-conversation-8}}


\notes{https://www.jstor.org/stable/1191906?origin=crossref
Are Juries Competent to Evaluate Statistical Evidence?
William C. Thompson
Law and Contemporary Problems, Vol. 52, No. 4, Is the Jury Competent? (Autumn, 1989), pp. 9-41 (33 pages)}

\endif
