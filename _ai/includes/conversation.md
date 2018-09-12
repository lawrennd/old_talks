\subsection{Human Communication}

\setupdisplaycode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('anne-bob-conversation{sample:0>3}.svg', 
                            '../slides/diagrams',  sample=IntSlider(0, 0, 7, 1))}



\notes{For human conversation to work, we require an internal model of who we are speaking to. We model each other, and combine our sense of who they are, who they think we are, and what has been said. This is our approach to dealing with the limited bandwidth connection we have. Empathy and understanding of intent. Mental dispositional concepts are used to augment our limited communication bandwidth.

Fritz Heider referred to the important point of a conversation as being that they are happenings that are "*psychologically represented* in each of the participants" (his emphasis) [@Heider:interpersonal58]}


\newslide{Conversation}
\define{\stubname}{anne-bob-conversation}
\slides{
\define{\divoptions}{maxwidth:100vw; max-height:100vh}
\define{\svgstyle}{width:80%;}
\startslides{\stubname}{0}{7}
\div{\includesvg{../slides/diagrams/\concat{\stubname}{000.svg}}{}{}{\svgstyle}}{\stubname}{\divoptions}
\div{\includesvg{../slides/diagrams/\concat{\stubname}{001.svg}}{}{}{\svgstyle}}{\stubname}{\divoptions}
\div{\includesvg{../slides/diagrams/\concat{\stubname}{002.svg}}{}{}{\svgstyle}}{\stubname}{\divoptions}
\div{\includesvg{../slides/diagrams/\concat{\stubname}{003.svg}}{}{}{\svgstyle}}{\stubname}{\divoptions}
\div{\includesvg{../slides/diagrams/\concat{\stubname}{004.svg}}{}{}{\svgstyle}}{\stubname}{\divoptions}
\div{\includesvg{../slides/diagrams/\concat{\stubname}{005.svg}}{}{}{\svgstyle}}{\stubname}{\divoptions}
\div{\includesvg{../slides/diagrams/\concat{\stubname}{006.svg}}{}{}{\svgstyle}}{\stubname}{\divoptions}
\div{\includesvg{../slides/diagrams/\concat{\stubname}{007.svg}}{}{}{\svgstyle}}{\stubname}{\divoptions}
}

\notesfigure{\includesvg{../slides/diagrams/\concat{\stubname}{006.svg}}}
\notes{\caption{Conversation relies on internal models of other individuals.}}
\notesfigure{\includesvg{../slides/diagrams/\concat{\stubname}{007.svg}}}
\notes{\caption{Misunderstanding of context and who we are talking to leads to arguments.}}
\speakernotes{This can be disturbing to humans because we are used to a low bandwidth communication rate. }
