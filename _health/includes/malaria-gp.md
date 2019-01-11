\ifndef{malariaGp}
\define{malariaGp}
\editme

\subsection{Example: Prediction of Malaria Incidence in Uganda}

\alignright{\ricardoPicture{1.5cm}}

\notes{As an example we'll consider the prediction of Malaria incidence in Uganda. For the purposes of this study malaria reports come in two forms, HMIS reports from health centres and Sentinel data, which is curated by the WHO. There are limited sentinel sites and many HMIS sites.

The work is from Ricardo Andrade Pacheco's PhD thesis, completed in collaboration with John Quinn and Martin Mubangizi [@Andrade:consistent14,@Mubangizi:malaria14,]. John and Martin were initally from the AI-DEV group from the University of Makerere in Kampala and more latterly they were based at UN Global Pulse in Kampala.}

\slides{* Work with Ricardo Andrade Pacheco, John Quinn and Martin Mubaganzi (Makerere University, Uganda)
* See [AI-DEV Group](http://air.ug/research.html).}

\newslide{Malaria Prediction in Uganda}

\notes{Malaria data is spatial data. Uganda is split into districts, and health reports can be found for each district. This suggests that models such as conditional random fields could be used for spatial modelling, but there are two complexities with this. First of all, occasionally districts split into two. Secondly, sentinel sites are a specific location within a district, such as Nagongera which is a sentinel site based in the Tororo district.}

\includepng{../slides/diagrams/health/uganda-districts-2006}{50%}
\caption{Data SRTM/NASA from <https://dds.cr.usgs.gov/srtm/version2_1>}

\alignright{[@Andrade:consistent14,@Mubangizi:malaria14]}


\ifdef{olympicMarathonData}
\newslide{Kapchorwa District}

\includesvgclass{../slides/diagrams/health/Kapchorwa_District_in_Uganda.svg}
\notes{\caption{THe Kapchorwa District, home district of Stephen Kiprotich.}
\notes{Stephen Kiprotich, the 2012 gold medal winner from the London Olympics, comes from Kapchorwa district, in eastern Uganda, near the border with Kenya.}

\endif
\newslide{Tororo District}

\includesvgclass{../slides/diagrams/health/Tororo_District_in_Uganda.svg}
\notes{\caption{The Tororo District, where the sentinel site, Nagongera is located}}}

\newslide{Malaria Prediction in Nagongera (Sentinel Site)}

\includepng{../slides/diagrams/health/sentinel_nagongera}{100%}{negate}



\newslide{Mubende District}

\includesvgclass{../slides/diagrams/health/Mubende_District_in_Uganda.svg}{center}{svgplot_normal}

\newslide{Malaria Prediction in Uganda}

\includepng{../slides/diagrams/health/mubende}

\newslide{GP School at Makerere}

\includejpg{../slides/diagrams/gpss/1157497_513423392066576_1845599035_n}{90%}

\newslide{Kabarole District}

\includesvgclass{../slides/diagrams/health/Kabarole_District_in_Uganda.svg}

\subsection{Early Warning Systems}

\includegif{../slides/diagrams/health/kabarole}{100%}
\notes{\caption{Estimate of the current disease situation in the Kabarole district over time. Estimate is constructed with a Gaussian process with an additive covariance funciton.}}

\notes{Health monitoring system for the Kabarole district. Here we have fitted the reports with a Gaussian process with an additive covariance function. It has two components, one is a long time scale component (in red above) the other is a short time scale component (in blue). 

Monitoring proceeds by considering two aspects of the curve. Is the blue line (the short term report signal) above the red (which represents the long term trend? If so we have higher than expected reports. If this is the case *and* the gradient is still positive (i.e. reports are going up) we encode this with a *red* color. If it is the case and the gradient of the blue line is negative (i.e. reports are going down) we encode this with an *amber* color. Conversely, if the blue line is below the red *and* decreasing, we color *green*. On the other hand if it is below red but increasing, we color *yellow*. 

This gives us an early warning system for disease. Red is a bad situation getting worse, amber is bad, but improving. Green is good and getting better and yellow good but degrading. 

Finally, there is a gray region which represents when the scale of the effect is small.}

\newslide{Early Warning Systems}

\includegif{../slides/diagrams/health/monitor}{50%}
\notes{\caption{The map of Ugandan districts with an overview of the Malaria situation in each district.}}

\notes{These colors can now be observed directly on a spatial map of the districts to give an immediate impression of the current status of the disease across the country.}

\endif
