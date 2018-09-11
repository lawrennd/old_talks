\subsection{Human Communication}

\setupdisplaycode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('anne-bob-conversation{sample:0>3}.svg', 
                            '../slides/diagrams',  sample=IntSlider(0, 0, 7, 1))}



\notes{For human conversation to work, we require an internal model of who we are speaking to. We model each other, and combine our sense of who they are, who they think we are, and what has been said. This is our approach to dealing with the limited bandwidth connection we have. Empathy and understanding of intent. Mental dispositional concepts are used to augment our limited communication bandwidth.

Fritz Heider referred to the important point of a conversation as being that they are happenings that are "*psychologically represented* in each of the participants" (his emphasis) [@Heider:interpersonal58]}


\newslide{Conversation}
\slides{
\startslides{anne-bob-coversation{0}{7}
\includesvg{../slides/diagrams/anne-bob-conversation000.svg}{}{anne-bob-conversation}
\includesvg{../slides/diagrams/anne-bob-conversation001.svg}{}{anne-bob-conversation}
\includesvg{../slides/diagrams/anne-bob-conversation002.svg}{}{anne-bob-conversation}
\includesvg{../slides/diagrams/anne-bob-conversation003.svg}{}{anne-bob-conversation}
\includesvg{../slides/diagrams/anne-bob-conversation004.svg}{}{anne-bob-conversation}
\includesvg{../slides/diagrams/anne-bob-conversation005.svg}{}{anne-bob-conversation}
\includesvg{../slides/diagrams/anne-bob-conversation006.svg}{}{anne-bob-conversation}
\includesvg{../slides/diagrams/anne-bob-conversation007.svg}{}{anne-bob-conversation}
}

\notesfigure{\includesvg{../slides/diagrams/anne-bob-conversation006.svg}}
\notes{\caption{Conversation relies on internal models of other individuals.}}
\notesfigure{\includesvg{../slides/diagrams/anne-bob-conversation007.svg}}
\notes{\caption{Misunderstanding of context and who we are talking to leads to arguments.}}
\speakernotes{This can be disturbing to humans because we are used to a low bandwidth communication rate. }
