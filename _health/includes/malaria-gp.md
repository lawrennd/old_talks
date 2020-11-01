\ifndef{malariaGp}
\define{malariaGp}
\editme

\subsection{Example: Prediction of Malaria Incidence in Uganda}

\centerdiv{\circleHead{\diagramsDir/people/martin-mubangizi.png}{Martin Mubangizi}{15%}{https://www.linkedin.com/in/martin-mubangizi-24177111/}\circleHead{\diagramsDir/people/ricardo-andrade-pacheco.png}{Ricardo Andrade Pacheco}{15%}{http://ric70x7.github.io/}\circleHead{\diagramsDir/people/john-quinn.jpg}{John Quinn}{15%}{http://cit.mak.ac.ug/staff/jquinn/}}

\notes{As an example of using Gaussian process models within the full pipeline from data to decsion, we'll consider the prediction of Malaria incidence in Uganda. For the purposes of this study malaria reports come in two forms, HMIS reports from health centres and Sentinel data, which is curated by the WHO. There are limited sentinel sites and many HMIS sites.

The work is from Ricardo Andrade Pacheco's PhD thesis, completed in collaboration with John Quinn and Martin Mubangizi [@Andrade:consistent14;@Mubangizi:malaria14]. John and Martin were initally from the AI-DEV group from the University of Makerere in Kampala and more latterly they were based at UN Global Pulse in Kampala.}

\slides{* Work with Ricardo Andrade Pacheco, John Quinn and Martin Mubaganzi (Makerere University, Uganda)
* See [AI-DEV Group](http://air.ug/research.html).}

\newslide{Malaria Prediction in Uganda}

\notes{Malaria data is spatial data. Uganda is split into districts, and health reports can be found for each district. This suggests that models such as conditional random fields could be used for spatial modelling, but there are two complexities with this. First of all, occasionally districts split into two. Secondly, sentinel sites are a specific location within a district, such as Nagongera which is a sentinel site based in the Tororo district.}

\figure{\includepng{\diagramsDir/health/uganda-districts-2006}{50%}}{Ugandan districs. Data SRTM/NASA from <https://dds.cr.usgs.gov/srtm/version2_1>.}{uganda-districts-2006}

\alignright{[@Andrade:consistent14;@Mubangizi:malaria14]}


\ifdef{olympicMarathonData}
\newslide{Kapchorwa District}

\figure{\includediagramclass{\diagramsDir/health/Kapchorwa_District_in_Uganda}{50%}}{The Kapchorwa District, home district of Stephen Kiprotich.}{kapchorwa-district-in-uganda}

\notes{Stephen Kiprotich, the 2012 gold medal winner from the London Olympics, comes from Kapchorwa district, in eastern Uganda, near the border with Kenya.}

\endif

\newslide{Tororo District}

\notes{The common standard for collecting health data on the African continent is from the Health management information systems (HMIS). However, this data suffers from missing values [@Gething:hmis06] and diagnosis of diseases like typhoid and malaria may be confounded.}

\figure{\includediagramclass{\diagramsDir/health/Tororo_District_in_Uganda}{50%}}{The Tororo district, where the sentinel site, Nagongera, is located.}{tororo-district-in-uganda}

\notes{[World Health Organization Sentinel Surveillance systems](https://www.who.int/immunization/monitoring_surveillance/burden/vpd/surveillance_type/sentinel/en/) are set up "when high-quality data are needed about a particular disease that cannot be obtained through a passive system". Several sentinel sites give accurate assessment of malaria disease levels in Uganda, including a site in Nagongera.}

\newslide{Malaria Prediction in Nagongera (Sentinel Site)}

\figure{\includepng{\diagramsDir/health/sentinel_nagongera}{100%}{negate}}{Sentinel and HMIS data along with rainfall and temperature for the Nagongera sentinel station in the Tororo district.}{sentinel-nagongera}

\notes{In collaboration with the AI Research Group at Makerere we chose to investigate whether Gaussian process models could be used to assimilate information from these two different sources of disease informaton. Further, we were interested in whether local information on rainfall and temperature could be used to improve malaria estimates.}

\notes{The aim of the project was to use WHO Sentinel sites, alongside rainfall and temperature, to improve predictions from HMIS data of levels of malaria.}

\newslide{Mubende District}

\figure{\includediagramclass{\diagramsDir/health/Mubende_District_in_Uganda}{50%}}{The Mubende District.}{mubende-district-in-uganda}

\newslide{Malaria Prediction in Uganda}

\figure{\includepng{\diagramsDir/health/mubende}{80%}}{Prediction of malaria incidence in Mubende.}{malaria-prediction-mubende}

\newslide{GP School at Makerere}

\figure{\includejpg{\diagramsDir/gpss/1157497_513423392066576_1845599035_n}{80%}}{The project arose out of the Gaussian process summer school held at Makerere in Kampala in 2013. The school led, in turn, to the Data Science Africa initiative.}

\notes{\subsection{Early Warning Systems}}

\newslide{Kabarole District}

\figure{\includediagramclass{\diagramsDir/health/Kabarole_District_in_Uganda}{50%}}{The Kabarole district in Uganda.}{kabarole-district-in-uganda}

\newslide{Early Warning System}

\figure{\includegif{\diagramsDir/health/kabarole}{100%}}{Estimate of the current disease situation in the Kabarole district over time. Estimate is constructed with a Gaussian process with an additive covariance funciton.}{kabarole-disease-over-time}

\notes{Health monitoring system for the Kabarole district. Here we have fitted the reports with a Gaussian process with an additive covariance function. It has two components, one is a long time scale component (in red above) the other is a short time scale component (in blue).}

\notes{Monitoring proceeds by considering two aspects of the curve. Is the blue line (the short term report signal) above the red (which represents the long term trend? If so we have higher than expected reports. If this is the case *and* the gradient is still positive (i.e. reports are going up) we encode this with a *red* color. If it is the case and the gradient of the blue line is negative (i.e. reports are going down) we encode this with an *amber* color. Conversely, if the blue line is below the red *and* decreasing, we color *green*. On the other hand if it is below red but increasing, we color *yellow*.}

\notes{This gives us an early warning system for disease. Red is a bad situation getting worse, amber is bad, but improving. Green is good and getting better and yellow good but degrading.}

\notes{Finally, there is a gray region which represents when the scale of the effect is small.}

\newslide{Early Warning Systems}

\figure{\includegif{\diagramsDir/health/monitor}{50%}}{The map of Ugandan districts with an overview of the Malaria situation in each district.}{early-warning-system-map}

\notes{These colors can now be observed directly on a spatial map of the districts to give an immediate impression of the current status of the disease across the country.}

\endif
