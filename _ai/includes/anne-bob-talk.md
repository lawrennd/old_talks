\notes{\subsubsection{Bandwidth Constrained Conversations}}

\setupdisplaycode{import notutils as nu
from ipywidgets import IntSlider}


\setupdisplaycode{import notutils as nu}
\displaycode{nu.display_plots('\stubname{sample:0>3}.svg', 
                            '\diagramsDir',  sample=IntSlider(0, 0, 7, 1))}

\define{\divoptions}{maxwidth:100vw; max-height:100vh}
\define{\widthVal}{70%}

\newslide{}

\slides{\div{\includediagram{\diagramsDir/\concat{\stubname}{000}}{\widthVal}}{\stubname}{\divoptions}}

\newslide{}

\slides{\div{\includediagram{\diagramsDir/\concat{\stubname}{001}}{\widthVal}}{\stubname}{\divoptions}}

\newslide{}

\slides{\div{\includediagram{\diagramsDir/\concat{\stubname}{002}}{\widthVal}}{\stubname}{\divoptions}}

\newslide{}

\slides{\div{\includediagram{\diagramsDir/\concat{\stubname}{003}}{\widthVal}}{\stubname}{\divoptions}}

\newslide{}

\slides{\div{\includediagram{\diagramsDir/\concat{\stubname}{004}}{\widthVal}}{\stubname}{\divoptions}}

\newslide{}

\slides{\div{\includediagram{\diagramsDir/\concat{\stubname}{005}}{\widthVal}}{\stubname}{\divoptions}}

\newslide{}

\slides{\div{\includediagram{\diagramsDir/\concat{\stubname}{006}}{\widthVal}}{\stubname}{\divoptions}}

\newslide{}

\slides{\div{\includediagram{\diagramsDir/\concat{\stubname}{007}}{\widthVal}}{\stubname}{\divoptions}}

\notes{\figure{\includediagram{\diagramsDir/\concat{\stubname}{006}}{\widthVal}}{Conversation relies on internal models of other individuals.}{\concat{\stubname}{-civil}}
\figure{\includediagram{\diagramsDir/\concat{\stubname}{007}}{\widthVal}}{Misunderstanding of context and who we are talking to leads to arguments.}{\concat{\stubname}{-argument}}}

\notes{Embodiment factors imply that, in our communication between humans, what is *not* said is, perhaps, more important than what is said. To communicate with each other we need to have a model of who each of us are.} 

\notes{To aid this, in society, we are required to perform roles. Whether as a parent, a teacher, an employee or a boss. Each of these roles requires that we conform to certain standards of behaviour to facilitate communication between ourselves.}

\notes{Control of self is vitally important to these communications.}

\notes{The high availability of data available to humans undermines human-to-human communication channels by providing new routes to undermining our control of self.}
