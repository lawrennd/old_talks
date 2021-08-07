\ifndef{whereDoRejectedPapersGo}
\define{whereDoRejectedPapersGo}

\editme

\subsection{Where do Rejected Papers Go?}

\setupcode{import os
import yaml}

\code{with open(os.path.join(nipsy.review_store, nipsy.outlet_name_mapping), 'r') as f:
    mapping = yaml.load(f, Loader=yaml.FullLoader)


date = "2021-06-11"

citations = nipsy.load_citation_counts(date=date)
decisions = nipsy.load_decisions()
nipsy.augment_decisions(decisions)
joindf = nipsy.join_decisions_citations(decisions, citations)

joindf['short_venue'] = joindf.venue.replace(mapping)}

\setupplotcode{import plotly.graph_objects as go}

\plotcode{thresh_to_show = 3

label = ['submitted', 'oral', 'spotlight', 'poster', 'reject', '/dev/null']
x = [0.1, 0.3, 0.3, 0.3, 0.3, 0.5]
y = [0.4, 0.95, 0.9, 0.85, 0.3, 0.01]
source = [0, 0, 0, 0, 4]
target = [1, 2, 3, 4, 5]
value = [(joindf['Status']=='Oral').sum(),
         (joindf['Status']=='Spotlight').sum(), 
         (joindf['Status']=='Poster').sum(),
         (joindf['Status']=='Reject').sum(),
        joindf.loc[joindf.reject]['venue'].isna().sum()]

venue_counts = joindf.loc[joindf.reject]['short_venue'].value_counts()
venue_show = venue_counts[venue_counts>=thresh_to_show]
target_val = target[-1]
for venue,count in venue_show.items():
    target_val += 1
    value.append(count)
    source.append(4)
    label.append(venue)
    target.append(target_val)
    if venue=='ArXiv':
        y.append(.15)
        x.append(0.75)
    
    elif venue == 'None':
        y.append(.20)
        x.append(0.75)

    else: 
        y.append(.27)
        x.append(0.8)
    

    
value.append(venue_counts[venue_counts<thresh_to_show].sum())
source.append(4)
label.append('other')
target.append(target_val+1)
x.append(0.85)
y.append(1.0)

link = dict(source = source, target = target, value = value)
node = dict(label=label,
            x = x,
            y = y,
            pad=12)
data=go.Sankey(arrangement = "snap",
                 link = link,
                 node = node)
fig = go.Figure(data=data)
fig.update_layout(template="plotly_dark")
fig.show()
fig.write_html(os.path.join(".", "neurips", "where-do-neurips-papers-go.dark.html"))
fig = go.Figure(data=data,
                layout = go.Layout(width=600,
                height=450))
fig.update_layout(template="plotly", textfont=dict(
        family="sans serif",
        size=14,
        color="White"
    ))
fig.show()
fig.write_html(os.path.join(".", "\writeDiagramDir/neurips", "where-do-neurips-papers-go.html"))
fig.write_image(os.path.join(".", "\writeDiagramDir/neurips", "where-do-neurips-papers-go.pdf"))
}

\figure{\html{\includehtml{\diagramsDir/neurips/where-do-neurips-papers-go.html}{600}{450}}\tex{\includediagram{\diagramsDir/neurips/where-do-neurips-papers-go}{80%}}}{Sankey diagram showing the flow of NeurIPS papers through the system from submission to eventual publication.}{where-do-neurips-papers-go}}


\endif
