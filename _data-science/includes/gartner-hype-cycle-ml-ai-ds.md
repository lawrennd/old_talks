\include{_data-science/includes/gartner-hype-cycle.md}



\setupcode{import matplotlib.pyplot as plt
import pods
import mlai
import teaching_plots as plot}

\code{# calling without arguments uses the default query terms
data = pods.datasets.google_trends(['big data', 'data science', 'internet of things', 'machine learning']) 
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
    mlai.write_figure('../slides/diagrams/data-science/bd-ds-iot-ml-google-trends{sample:0>3}.svg'.format(sample=i))
}

\displaycode{pods.notebook.display_plots('ml-ai-ds-google-trends-{sample:0>3}.svg', 
                            '../slides/diagrams/', sample=(1,4))}

\slides{
### {.slide: data-transition="none"}

\includesvg{../slides/diagrams/ml-ai-ds-google-trends-000.svg}

### {.slide: data-transition="none"}

\includesvg{../slides/diagrams/ml-ai-ds-google-trends-001.svg}

### {.slide: data-transition="none"}

\includesvg{../slides/diagrams/ml-ai-ds-google-trends-002.svg}

### {.slide: data-transition="none"}

\includesvg{../slides/diagrams/ml-ai-ds-google-trends-003.svg}

### {.slide: data-transition="none"}

\includesvg{../slides/diagrams/ml-ai-ds-google-trends-004.svg}
}

\notes{Google trends gives us insight into how far along various technological terms are on the hype cycle.}
