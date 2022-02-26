\ifndef{dataInfrastructure}
\define{dataInfrasrtucture}
\editme

\setupdisplaycode{import pods}
\setupdisplaycode{import notutils as nu}
\displaycode{nu.display_plots('uk_tin_coal_railways{sample:0>3}.svg', 
                            '\writeDiagramsDir/data-science', sample=(1,5))}

\notes{\figure{\columns{\includediagram{\diagramsDir/data-science/uk_tin_coal_railways004}{100%}}{\includediagram{\diagramsDir/data-science/uk_tin_coal_railways005}{100%}}{50%}{50%}}}{The evolution of the UK railway network in relation to tin and coal mines.}{uk-tin-coal-railways}

\newslide{}

\slides{
\define{width}{80%}
\startanimation{uk_tin_coal_railways}{1}{4}
\newframe{\includediagramclass{\diagramsDir/data-science/uk_tin_coal_railways001}{\width}}{uk_tin_coal_railways}
\newframe{\includediagramclass{\diagramsDir/data-science/uk_tin_coal_railways002}{\width}}{uk_tin_coal_railways}
\newframe{\includediagramclass{\diagramsDir/data-science/uk_tin_coal_railways003}{\width}}{uk_tin_coal_railways}
\newframe{\includediagramclass{\diagramsDir/data-science/uk_tin_coal_railways004}{\width}}{uk_tin_coal_railways}
\newframe{\includediagramclass{\diagramsDir/data-science/uk_tin_coal_railways005}{\width}}{uk_tin_coal_railways}
\endanimation
}

\notes{By analogy, we can think of the evolution of transport infrastructure during the industrial revolution. Earlier railways actually seem to be more focussed on the coal fields. Coal was the energy resource that drove the industrial revolution in the 19th century, just like data is the information resource that drives the ongoing digital revolution today.}

\endif
