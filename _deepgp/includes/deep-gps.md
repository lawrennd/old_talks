\ifndef{deepGps}
\define{deepGps}
\editme

\newslide{Structures for Extracting Information from Data}

\setupplotcode{}

\plotcode{pgm = plot.vertical_chain(depth=5)
pgm.render().figure.savefig("\writeDiagramsDir/deepgp/deep-markov-vertical.svg", transparent=True)}}

\columns{\includediagram{\diagramsDir/deepgp/stack-gp-sample-rbf-2}}{\includediagram{\diagramsDir/deepgp/deep-markov-vertical}{40%}{60%}

\newslide{} 
\slides{
\centerdiv{\andreasDamianouPicture{15%}}
\alignright{@Damianou:deepgp13} 

\includepng{\diagramsDir/deepgp/damianou13a.pdf}
<http://jmlr.org/proceedings/papers/v31/damianou13a.pdf>
}

\endif
