

\setupdisplaycode{import pods
from ipywidgets import IntSlider}


\displaycode{pods.notebook.display_plots('\stubname{sample:0>3}.svg', 
                            '../slides/diagrams',  sample=IntSlider(0, 0, 7, 1))}

\define{\divoptions}{maxwidth:100vw; max-height:100vh}
\define{\widthVal}{80%}

\newslide{}

\slides{\div{\includediagram{../slides/diagrams/\concat{\stubname}{000}}{\widthVal}}{\stubname}{\divoptions}}

\newslide{}

\slides{\div{\includediagram{../slides/diagrams/\concat{\stubname}{001}}{\widthVal}}{\stubname}{\divoptions}}

\newslide{}

\slides{\div{\includediagram{../slides/diagrams/\concat{\stubname}{002}}{\widthVal}}{\stubname}{\divoptions}}

\newslide{}

\slides{\div{\includediagram{../slides/diagrams/\concat{\stubname}{003}}{\widthVal}}{\stubname}{\divoptions}}

\newslide{}

\slides{\div{\includediagram{../slides/diagrams/\concat{\stubname}{004}}{\widthVal}}{\stubname}{\divoptions}}

\newslide{}

\slides{\div{\includediagram{../slides/diagrams/\concat{\stubname}{005}}{\widthVal}}{\stubname}{\divoptions}}

\newslide{}

\slides{\div{\includediagram{../slides/diagrams/\concat{\stubname}{006}}{\widthVal}}{\stubname}{\divoptions}}

\newslide{}

\slides{\div{\includediagram{../slides/diagrams/\concat{\stubname}{007}}{\widthVal}}{\stubname}{\divoptions}}

\notes{
\figure{
\includediagram{../slides/diagrams/\concat{\stubname}{006}}
\caption{Conversation relies on internal models of other individuals.}}}
\notes{
\figure{
\includediagram{../slides/diagrams/\concat{\stubname}{007}}
\caption{Misunderstanding of context and who we are talking to leads to arguments.}}}

\notes{Embodiment factors imply that, in our communication between humans, what is *not* said is, perhaps, more important than what is said. To communicate with each other we need to have a model of who each of us are.} 

\notes{To aid this, in society, we are required to perform roles. Whether as a parent, a teacher, an employee or a boss. Each of these roles requires that we conform to certain standards of behaviour to facilitate communication between ourselves.}

\notes{Control of self is vitally important to these communications.}

\notes{The high availability of data available to humans undermines human-to-human communication channels by providing new routes to undermining our control of self.}
