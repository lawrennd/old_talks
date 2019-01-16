\ifndef{gartnerHypeCycleBase}
\define{gartnerHypeCycleBase}
\editme

\setupplotcode{import teaching_plots as plot}
\plotcode{plot.google_trends(terms=[\terms], 
                  initials='\initials', 
				  diagrams='../slides/diagrams/data-science')}
				  
\setupdisplaycode{import pods
from ipywidgets import IntSlider}
\displaycode{pods.notebook.display_plots('\initials-google-trends{sample:0>3}.svg', 
                            '../slides/diagrams/data-science/', sample=IntSlider(0, 1, 4, 1))}

\newslide{Gartner Hype Cycle}

\define{\divstyle}{max-width:100vw; max-height:100vh}
\slides{
\startanimation{\initials-google-trends}{0}{4}
\newframe{\includesvg{../slides/diagrams/data-science/\initials-google-trends000.svg}}{\initials-google-trends}{\divstyle}
\newframe{\includesvg{../slides/diagrams/data-science/\initials-google-trends001.svg}}{\initials-google-trends}{\divstyle}
\newframe{\includesvg{../slides/diagrams/data-science/\initials-google-trends002.svg}}{\initials-google-trends}{\divstyle}
\newframe{\includesvg{../slides/diagrams/data-science/\initials-google-trends003.svg}}{\initials-google-trends}{\divstyle}
\newframe{\includesvg{../slides/diagrams/data-science/\initials-google-trends004.svg}}{\initials-google-trends}{\divstyle}
\newframe{\includesvg{../slides/diagrams/data-science/\initials-google-trends.svg}}{\initials-google-trends}{\divstyle}
\endanimation
}

\figure{
\notesfigure{\includesvg{../slides/diagrams/data-science/\initials-google-trends.svg}{}}
\notes{\caption{Google trends for different technological terms on the hype cycle.}}
}

\notes{Google trends gives us insight into how far along various technological terms are on the hype cycle.}

\endif
