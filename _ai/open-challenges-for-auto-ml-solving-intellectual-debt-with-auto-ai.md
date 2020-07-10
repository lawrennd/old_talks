---
title: "Open Challenges for Automated Machine Learning: Solving Intellectual Debt with AutoAI"
abstract: Machine learning models are deployed as part of wider systems where outputs of one model are consumed by other models. This composite structure for machine learning systems is the dominant approach for deploying artificial intelligence. Such deployed systems can be complex to understand, they bring with them intellectual debt. In this talk we'll argue that the next frontier for automated machine learning is to move to automation of the systems design, going from AutoML to AutoAI.
author:
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Cambridge
  twitter: lawrennd
  url: http://inverseprobability.com
date: 2020-07-18
venue: ICML Workshop on Automated Machine Learning
transition: None
---

\include{../talk-macros.gpp}

\section{AI via ML Systems}

\subsection{Alexa}

\centerdiv{\circleHead{\diagramsDir/people/tom-taylor.png}{Tom Taylor}{15%}{https://www.linkedin.com/in/tom-taylor-835b03/}
\circleHead{\diagramsDir/people/joe-walowski.png}{Joe Walowski}{15%}{https://www.linkedin.com/in/joe-walowski-b2b7242/}
\circleHead{\diagramsDir/people/rohit-prasad.png}{Rohit Prasad}{15%}{https://www.linkedin.com/in/rohit-prasad-4a46251/}}
\includeyoutube{VQVZ2hvNVfo}{600}{450}

\subsection{Alexa}

\centerdiv{\circleHead{\diagramsDir/people/tom-taylor.png}{Tom Taylor}{15%}{https://www.linkedin.com/in/tom-taylor-835b03/}
\circleHead{\diagramsDir/people/joe-walowski.png}{Joe Walowski}{15%}{https://www.linkedin.com/in/joe-walowski-b2b7242/}
\circleHead{\diagramsDir/people/rohit-prasad.png}{Rohit Prasad}{15%}{https://www.linkedin.com/in/rohit-prasad-4a46251/}}
\includediagram{\diagramsDir/software/alexa-schematic}{40%}

\subsection{Speech to Text}

\circleHead{\diagramsDir/people/catherine-breslin.png}{Catherine Breslin}{15%}{https://www.linkedin.com/in/catherine-breslin-0592423a?originalSubdomain=uk} 

\subsection{Cloud Service: Knowledge Base}

\centerdiv{\circleHead{\diagramsDir/people/david-hardcastle.png}{David Hardcastle}{15%}{https://www.linkedin.com/in/dwhardcastle/}
\circleHead{\diagramsDir/people/arpit-mittal.png}{Arpit Mittal}{15%}{https://www.linkedin.com/in/arpit-mittal-71a789b/}
\circleHead{\diagramsDir/people/christos-christodoulopoulos.png}{Christos Christodoulopoulos}{15%}{https://www.linkedin.com/in/christos-christodoulopoulos-376b9831/}}

\subsection{Text to Speech}

\centerdiv{\circleHead{\diagramsDir/people/andrew-breen.png}{Andrew Breen}{15%}{https://www.linkedin.com/in/andrew-breen-b79111/}
\circleHead{\diagramsDir/people/roberto-barra-chicote.png}{Roberto Barra Chicote}{15%}{https://www.linkedin.com/in/roberto-barra-chicote-496699b/}}

\subsection{Prime Air}

\centerdiv{\circleHead{\diagramsDir/people/gur-kimchi.png}{Gur Kimchi}{15%}{https://www.linkedin.com/in/gurkimchi/}\circleHead{\diagramsDir/people/paul-viola.png}{Paul Viola}{15%}{https://www.linkedin.com/in/violapaul/}\circleHead{\diagramsDir/people/david-moro.png}{David Moro}{15%}{https://www.linkedin.com/in/dmorol/}}
\includeyoutube{3HJtmx5f1Fc}{600}{450} 

\include{_uq/includes/emulation.md}


\subsection{Supply Chain Optimization}

\centerdiv{\circleHead{\diagramsDir/people/llew-mason.png}{Llew Mason}{15%}{https://www.linkedin.com/in/llewmason/}\circleHead{\diagramsDir/people/devesh-mishra.png}{Devesh Mishra}{15%}{https://www.linkedin.com/in/demishra/}}
\includeyoutube{ncwsr1Of6Cw}{600}{450}

\subsection{Supply Chain Optimization}

\centerdiv{\circleHead{\diagramsDir/people/llew-mason.png}{Llew Mason}{15%}{https://www.linkedin.com/in/llewmason/}\circleHead{\diagramsDir/people/devesh-mishra.png}{Devesh Mishra}{15%}{https://www.linkedin.com/in/demishra/}}
\includediagram{\diagramsDir/software/buying-schematic}{40%}


\subsection{Forecasting}

\circleHead{\diagramsDir/people/jenny-freshwater.png}{Jenny Freshwater}{15%}{https://www.linkedin.com/in/jenny-freshwater-4710a21/}
\circleHead{\diagramsDir/people/ping-xu.png}{Ping Xu}{15%}{https://www.linkedin.com/in/pingjosephine/} 
\circleHead{\diagramsDir/people/dean-foster.png}{Dean Foster}{15%}{https://www.linkedin.com/in/pingjosephine/}

\subsection{Inventory and Buying}

\centerdiv{\circleHead{\diagramsDir/people/deepak-bhatia.png}{Deepak Bhatia}{15%}{https://www.linkedin.com/in/dbhatia/}
\circleHead{\diagramsDir/people/piyush-saraogi.png}{Piyush Saraogi}{15%}{https://www.linkedin.com/in/piyushsaraogi/} 
\circleHead{\diagramsDir/people/salal-humair.png}{Salal Humair}{15%}{https://www.linkedin.com/in/salal-humair-b45415/} 
\circleHead{\diagramsDir/people/narayan-venkatasubramanyan.png}{Narayan Venkatasubramanyan}{15%}{https://www.linkedin.com/in/narayan3rdeye/}}

\subsection{Service Oriented Architecture}

\centerdiv{\circleHead{\diagramsDir/people/charlie-bell.png}{Charlie Bell}{15%}{https://www.linkedin.com/in/charlie-bell-05446835/}
\circleHead{\diagramsDir/people/peter-vosshall.png}{Peter Vosshall}{15%}{https://www.linkedin.com/in/petervosshall/}}

\figure{\includediagram{\diagramsDir/ai/ml-system-monolith-purchasing}{60%}}{A potential path of models in a machine learning system.}{ml-system-monolith}

\subsection{Service Oriented Architecture}

\centerdiv{\circleHead{\diagramsDir/people/charlie-bell.png}{Charlie Bell}{15%}{https://www.linkedin.com/in/charlie-bell-05446835/}
\circleHead{\diagramsDir/people/peter-vosshall.png}{Peter Vosshall}{15%}{https://www.linkedin.com/in/petervosshall/}}

\figure{\includediagram{\diagramsDir/ai/ml-system-downstream-purchasing000}{60%}}{A potential path of models in a machine learning system.}{ml-system-downstream-purchasing}


\section{Intellectual Debt}

\subsection{Separation of Concerns}

\centerdiv{\circleHead{\diagramsDir/people/dave-clark.png}{Dave Clark}{15%}{https://www.linkedin.com/in/dave-clark-3a82684/}\circleHead{\diagramsDir/people/nevena-lalic.png}{Nevena Lalic}{15%}{https://www.linkedin.com/in/nevena-lalic-65561b53/}}


\section{Data Science Africa}

\subsection{Crop Monitoring}


\centerdiv{\circleHead{\diagramsDir/people/ernest-mwebaze.png}{Ernest Mwebaze}{15%}{https://www.linkedin.com/in/emwebaze/}}
\figure{\includepng{\diagramsDir/africa/mobile-monitoring-of-crop-disease}{60%}}{Mobile Monitoring of Crop Disease}{mobile-monitoring-crop}



\subsection{Biosurveillance}

\centerdiv{\circleHead{\diagramsDir/people/martin-mubangizi.png}{Martin Mubangizi}{15%}{https://www.linkedin.com/in/martin-mubangizi-24177111/}}
\figure{\includepng{\diagramsDir/africa/spatiotemporal-models-for-biosurveillance}{60%}}{Spatiotemporal Models for Biosurveillance}{spatiotemporal-models-biosurveillance}


\subsection{Community Radio}

\centerdiv{\circleHead{\diagramsDir/people/morine-amutorine.png}{Morine Amutorine}{15%}{https://www.linkedin.com/in/morine-amutorine/}}
\figure{\includepng{\diagramsDir/africa/ugandan-community-radio-project}{45%}}{Ugandan Community Radio Project}{ugandan-community-radio}


\subsection{Kudu Project}

\figure{\includepng{\diagramsDir/africa/kudu-project}{60%}}{Kudu Project}{kudu-project}

\subsection{Safe Boda}

\figure{\includepng{\diagramsDir/africa/safe-boda}{60%}}{Safe Boda}{safe-boda}

\section{AutoAI}


\include{_uq/includes/deep-emulation.md}



<!-- \include{_data-science/includes/milan.md} -->
<!-- \include{_uq/includes/emukit-software.md} -->

\newslide{Conclusion}

* For deployed ML, worrying about a single ML component isn't good enough.
* Real world systems involve interaction of components
* Leads to intellectual debt
* Need for sophisticated emulation techniques for making deployment scalable.

\thanks

