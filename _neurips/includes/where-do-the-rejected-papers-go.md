\ifndef{whereDoRejectedPapersGo}
\define{whereDoRejectedPapersGo}

\editme

\subsection{Where do Rejected Papers Go?}

\notes{One facet that we can explore is what the final fate of papers that are rejected by the conference is.}


\notes{Of the 1,678 papers submitted to NeurIPS 2014, only 414 were presented
at the final conference. Here we trace the fate of the rejected papers, we searched Semantic Scholar
for evidence of all 1,264 rejected papers. We looked for papers with
similar titles and where the NeurIPS submission's contact author was
also in the author list. We were able to track down 680 papers.}

\notes{This code analyzes those 680 papers extracting their final publication venue using the Semantic Scholar API.}

\installcode{cmtutils}


\setupcode{import cmtutils.nipsy as nipsy}

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


\figure{\html{\includehtml{\diagramsDir/neurips/where-do-neurips-papers-go.html}{600}{450}}\tex{\includediagram{\diagramsDir/neurips/where-do-neurips-papers-go}{80%}}\docx{\includediagram{\diagramsDir/neurips/where-do-neurips-papers-go}{80%}}}{Sankey diagram showing the flow of NeurIPS papers through the system from submission to eventual publication.}{where-do-neurips-papers-go}

\notes{Of the 680 papers 177 were only found on arXiv, 76 were found as PDFs online
without a publication venue and 427 were published in other
venues. The outlets that received ten or more papers from this group
were AAAI (72 papers), AISTATS (57 papers), ICML (33 papers), CVPR (17
papers), Later NeurIPS (15 papers), JMLR (14 papers), IJCAI (14
papers), ICLR (13 papers), UAI (11 papers).  Opinion about quality of
these different outlets will vary from individual, but from our
perspective all of these outlets are `top-tier' for machine learning
and related areas. Other papers appeared at less prestigious outlets, and citation scores were also recored for papers that remained available only on ArXiv.  Note that there is likely a bias towards outlets
that have a submission deadline shortly after NeurIPS decisions are
public, e.g.\ submission deadline for AAAI 2015 was six days after
NeurIPS decisions were sent to authors. AISTATS has a submission
deadline one month after.}

\notes{A Sankey diagram showing where papers
submitted to the conference ended up is shown below.}

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
                 node = node)}

\plotcode{fig = go.Figure(data=data)
fig.update_layout(template="plotly_dark")
fig.show()
fig.write_html(os.path.join("\writeDiagramsDir", "neurips", "where-do-neurips-papers-go.dark.html"))}

\plotcode{fig = go.Figure(data=data,
                layout = go.Layout(width=600,
                height=450))
fig.update_layout(template="plotly", font=dict(
        family="sans serif",
        size=14,
        color="Black"
    ))
fig.show()
fig.write_html(os.path.join("\writeDiagramsDir", "neurips", "where-do-neurips-papers-go.html"))
fig.write_image(os.path.join("\writeDiagramsDir", "neurips", "where-do-neurips-papers-go.svg"))
}

\figure{\ipynb{\includediagram{\diagramsDir/neurips/where-do-neurips-papers-go}{600}{450}}\html{\includehtml{\diagramsDir/neurips/where-do-neurips-papers-go.html}{600}{450}}\tex{\includediagram{\diagramsDir/neurips/where-do-neurips-papers-go}{80%}}\docx{\includediagram{\diagramsDir/neurips/where-do-neurips-papers-go}{80%}}}{Sankey diagram showing the flow of NeurIPS papers through the system from submission to eventual publication.}{where-do-neurips-papers-go}

\endif
