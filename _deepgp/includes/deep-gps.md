\ifndef{deepGps}
\define{deepGps}
\editme

\newslide{Structures for Extracting Information from Data}

\setupplotcode{}

\plotcode{pgm = plot.vertical_chain(depth=5)
pgm.render().figure.savefig("../slides/diagrams/deepgp/deep-markov-vertical.svg", transparent=True)}}

\columns{\includediagram{../slides/diagrams/deepgp/stack-gp-sample-rbf-2}}{\includediagram{../slides/diagrams/deepgp/deep-markov-vertical}{40%}{60%}

\newslide{} 
\slides{
\alignleft{@Damianou:deepgp13} \alignright{\andreasPicture{1.5cm}}

\includepng{../slides/diagrams/deepgp/damianou13a.pdf}
<http://jmlr.org/proceedings/papers/v31/damianou13a.pdf>
}

\endif
