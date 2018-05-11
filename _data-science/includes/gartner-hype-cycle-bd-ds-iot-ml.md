\include{_data-science/includes/gartner-hype-cycle.md}



\setupcode{import matplotlib.pyplot as plt
import pods
import mlai
import teaching_plots as plot}

\code{# calling without arguments uses the default query terms
data = pods.datasets.google_trends(['big data', 'data science', 'internet of things', 'machine learning']) 
data['data frame'].set_index('Date', inplace=True)
}

\plotcode{fig, ax = plt.subplots(figsize=plot.big_wide_figsize)
data['data frame'].plot(ax=ax)
_ = ax.set_xticklabels(ax.xaxis.get_majorticklabels(), rotation=45)
plt.gcf().subplots_adjust(bottom=0.3)
handles = ax.get_lines()
for handle in handles:
    handle.set_visible(False)
for i, handle in enumerate(handles):
    handle.set_visible(True)
	handle.set_linewidth(3)
    mlai.write_figure('../slides/diagrams/data-science/bd-ds-iot-ml-google-trends{sample:0>3}.svg'.format(sample=i))
}

\notesfigure{\includesvg{../slides/diagrams/data-science/bd-ds-iot-ml-google-trends003.svg}
\aligncenter{*Google Trends data for different search terms in an attempt to assess their position on the "hype cycle"*}}

\displaycode{pods.notebook.display_plots('bd-ds-iot-ml-google-trends{sample:0>3}.svg', 
                            '../slides/diagrams/data-science', sample=(0,3))}

\slides{
### {.slide: data-transition="none"}

\includesvg{../slides/diagrams/data-science/bd-ds-iot-ml-google-trends000.svg}

### {.slide: data-transition="none"}

\includesvg{../slides/diagrams/data-science/bd-ds-iot-ml-google-trends001.svg}

### {.slide: data-transition="none"}

\includesvg{../slides/diagrams/data-science/bd-ds-iot-ml-google-trends002.svg}

### {.slide: data-transition="none"}

\includesvg{../slides/diagrams/data-science/bd-ds-iot-ml-google-trends003.svg}

}

\notes{Google trends gives us insight into how far along various technological terms are on the hype cycle.}
