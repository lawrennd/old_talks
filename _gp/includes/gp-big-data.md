\ifndef{gpBigData}
\define{gpBigData}
\editme

\subsection{Nonparametrics for Very Large Data Sets}

\slides{\aligncenter{Modern data availability}}

\figure{\includepng{\diagramsDir/ml/house_price_country}{60%}{negate}}{House prices across the UK are now easily available. <http://landregistry.data.gov.uk/>}{house-price-country}

\newslide{Nonparametrics for Very Large Data Sets}

\aligncenter{Proxy for index of deprivation?}

\figure{\includepng{\diagramsDir/ml/house_price_peak_district}{60%}{negate}}{Zooming in on house prices across the UK's Peak District shows different areas of wealth. Could these house prices be used, e.g.,  as a proxy for the [Index of Multiple Deprivation](https://en.wikipedia.org/wiki/Multiple_deprivation_index). Or are such indices merely intermediate indices for the real measures we're interested in?}{house-price-peak-district}

\newslide{Nonparametrics for Very Large Data Sets}

\slides{\aligncenter{Actually index of deprivation is a proxy for this ...}}

\slides{\includepng{\diagramsDir/ml/house_price_peak_district}{60%}{negate}}

\newslide{}
\catdoc
\jamesHensmanPicture{10%}
\columns{\alignleft{[@Hensman:bigdata13]}}{\alignright{\jamesHensmanPicture{15%}}}

\figure{\includepng{\diagramsDir/health/244_1_clip}{90%}}{We can now take advantage of modern variational scaling techniques such as stochastic variational inference to fit Gaussian processes to very large data sets. <http://auai.org/uai2013/prints/papers/244.pdf>}{gps-for-big-data}
\aligncenter{<http://auai.org/uai2013/prints/papers/244.pdf>}

\newslide{}

\columns{\alignleft{[@Hensman:bigdata13]}}{\alignright{\jamesHensmanPicture{15%}}}

\figure{\includepng{\diagramsDir/health/244_6_clip}{90%}}{New approaches to scaling Gaussian processes bring the potential to model these indices and others directly. <http://auai.org/uai2013/prints/papers/244.pdf>}{svi-gps-for-big-data}

\aligncenter{<http://auai.org/uai2013/prints/papers/244.pdf>}

\endif
