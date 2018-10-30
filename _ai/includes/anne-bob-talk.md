

\setupdisplaycode{import pods
from ipywidgets import IntSlider}


\displaycode{pods.notebook.display_plots('\stubname{sample:0>3}.svg', 
                            '../slides/diagrams',  sample=IntSlider(0, 0, 7, 1))}

\define{\divoptions}{maxwidth:100vw; max-height:100vh}
\define{\svgstyle}{width:80%;}

\newslide{}

\slides{\div{\includesvg{../slides/diagrams/\concat{\stubname}{000.svg}}{}{}{\svgstyle}}{\stubname}{\divoptions}}

\newslide{}

\slides{\div{\includesvg{../slides/diagrams/\concat{\stubname}{001.svg}}{}{}{\svgstyle}}{\stubname}{\divoptions}}

\newslide{}

\slides{\div{\includesvg{../slides/diagrams/\concat{\stubname}{002.svg}}{}{}{\svgstyle}}{\stubname}{\divoptions}}

\newslide{}

\slides{\div{\includesvg{../slides/diagrams/\concat{\stubname}{003.svg}}{}{}{\svgstyle}}{\stubname}{\divoptions}}

\newslide{}

\slides{\div{\includesvg{../slides/diagrams/\concat{\stubname}{004.svg}}{}{}{\svgstyle}}{\stubname}{\divoptions}}

\newslide{}

\slides{\div{\includesvg{../slides/diagrams/\concat{\stubname}{005.svg}}{}{}{\svgstyle}}{\stubname}{\divoptions}}

\newslide{}

\slides{\div{\includesvg{../slides/diagrams/\concat{\stubname}{006.svg}}{}{}{\svgstyle}}{\stubname}{\divoptions}}

\newslide{}

\slides{\div{\includesvg{../slides/diagrams/\concat{\stubname}{007.svg}}{}{}{\svgstyle}}{\stubname}{\divoptions}}


\notesfigure{\includesvg{../slides/diagrams/\concat{\stubname}{006.svg}}}
\notes{\caption{Conversation relies on internal models of other individuals.}}
\notesfigure{\includesvg{../slides/diagrams/\concat{\stubname}{007.svg}}}
\notes{\caption{Misunderstanding of context and who we are talking to leads to arguments.}}
\speakernotes{This can be disturbing to humans because we are used to a low bandwidth communication rate. }
