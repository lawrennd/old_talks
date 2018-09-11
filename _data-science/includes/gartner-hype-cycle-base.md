\setupplotcode{import matplotlib.pyplot as plt
import pods
import mlai
import teaching_plots as plot}

\plotcode{# calling without arguments uses the default query terms
data = pods.datasets.google_trends([\terms]) 
data['data frame'].set_index('Date', inplace=True)
}


\plotcode{fig, ax = plt.subplots(figsize=plot.wide_figsize)
data['data frame'].plot(ax=ax)
_ = ax.set_xticklabels(ax.xaxis.get_majorticklabels(), rotation=45)
handles = ax.get_lines()
for handle in handles:
    handle.set_visible(False)
for i, handle in enumerate(handles):
    handle.set_visible(True)
    mlai.write_figure('../slides/diagrams/data-science/\initials-google-trends{sample:0>3}.svg'.format(sample=i))
}

\setupdisplaycode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('\initials-google-trends{sample:0>3}.svg', 
                            '../slides/diagrams/data-science/', sample=IntSlider(1, 1, 4, 1))}

\newslide{Gartner Hype Cycle}

\slides{
\startslides{\initials-google-trends}{0}{4}
\includesvg{../slides/diagrams/data-science/\initials-google-trends000.svg}{}{\initials-google-trends}
\includesvg{../slides/diagrams/data-science/\initials-google-trends001.svg}{}{\initials-google-trends}
\includesvg{../slides/diagrams/data-science/\initials-google-trends002.svg}{}{\initials-google-trends}
\includesvg{../slides/diagrams/data-science/\initials-google-trends003.svg}{}{\initials-google-trends}
\includesvg{../slides/diagrams/data-science/\initials-google-trends004.svg}{}{\initials-google-trends}
}
\notesfigure{\includesvg{../slides/diagrams/data-science/\initials-google-trends004.svg}{}}
\notes{\caption{Google trends for different technological terms on the hype cycle.}}

\notes{Google trends gives us insight into how far along various technological terms are on the hype cycle.}
