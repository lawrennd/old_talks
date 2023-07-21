\ifndef{conversationLlm}
\define{conversationLlm}
\editme
\newslide{}

\notes{\subsection{LLM Conversations}}

\setupdisplaycode{import notutils as nu
from ipywidgets import IntSlider}


\setupdisplaycode{import notutils as nu}
\displaycode{nu.display_plots('\stubname{sample:0>3}.svg', 
                            '\diagramsDir',  sample=IntSlider(0, 0, 7, 1))}

\define{\stubname}{anne-llm-conversation}

\define{\divoptions}{maxwidth:100vw; max-height:100vh}
\define{\widthVal}{80%}
\newslide{}

\slides{\includediagram{\diagramsDir/\concat{\stubname}{000}}{\widthVal}}

\newslide{}

\slides{\includediagram{\diagramsDir/\concat{\stubname}{001}}{\widthVal}}

\newslide{}

\slides{\includediagram{\diagramsDir/\concat{\stubname}{002}}{\widthVal}}

\newslide{}

\slides{\includediagram{\diagramsDir/\concat{\stubname}{003}}{\widthVal}}

\newslide{}

\slides{\includediagram{\diagramsDir/\concat{\stubname}{004}}{\widthVal}}

\newslide{}

\slides{\includediagram{\diagramsDir/\concat{\stubname}{005}}{\widthVal}}

\newslide{}

\slides{\includediagram{\diagramsDir/\concat{\stubname}{006}}{\widthVal}}

\newslide{}

\slides{\includediagram{\diagramsDir/\concat{\stubname}{007}}{\widthVal}}

\notes{\figure{\includediagram{\diagramsDir/\concat{\stubname}{006}}{80%}}{Conversation relies on internal models of other individuals.}{anne-llm-conversation-6}}

\notes{\figure{\includediagram{\diagramsDir/\concat{\stubname}{007}}{80%}}{Misunderstanding of context and who we are talking to leads to arguments.}{anne-llm-conversation-8}}

\notes{Inner Monologue: Embodied Reasoning through Planning
with Language Models
Conference on Robot Learning (CoRL), 2022
https://proceedings.mlr.press/v205/huang23c.html
https://innermonologue.github.io/
https://www.youtube.com/watch?v=0sJjdxn5kcI&t=136s
}
\endif
